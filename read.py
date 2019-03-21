import json

rankings={}
basicInfo={}
episodes={}
with open("title.ratings.tsv", "r", encoding="utf8") as ratingsFile:
    next(ratingsFile)
    for title in ratingsFile:
        vals = title.split("\t")
        if int(vals[2][:-1]) >= 100:
            rankings.update({
                vals[0]:{
                    "averageRating": vals[1],
                    "numVotes"     : vals[2][:-1]
                }
            })

numWithRank=0
isFirstLine=True

with open("title.basics.tsv", "r", encoding="utf8") as basicsFile:
    next(basicsFile)
    for title in basicsFile:
        vals = title.split("\t")
        try:
            type(rankings[vals[0]])
            if int(vals[5]) >= 1990: 
                if vals[1] == "tvSeries":
                    basicInfo.update({
                        vals[0]:{
                            "titleType": vals[1],
                            "primaryTitle": vals[2],
                            "startYear": vals[5],
                            "endYear": vals[6],
                            "genres": vals[8],
                            "averageRating": rankings[vals[0]]["averageRating"],
                            "numVotes": rankings[vals[0]]["numVotes"]
                        }
                    })
                elif vals[1] == "tvEpisode":
                    episodes.update({
                        vals[0]:{
                            "titleType": vals[1],
                            "primaryTitle": vals[2],
                            "startYear": vals[5],
                            "endYear": vals[6],
                            "genres": vals[8],
                            "averageRating": rankings[vals[0]]["averageRating"],
                            "numVotes": rankings[vals[0]]["numVotes"]
                        }
                    })

        except:
            numWithRank+=0

jDump = json.dumps(episodes, indent=4)

with open("episodes.json", "a", encoding="utf8") as rankFile:
    rankFile.write(jDump)
