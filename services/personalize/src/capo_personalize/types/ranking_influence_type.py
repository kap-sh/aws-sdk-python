"""Generated from Smithy shape ``com.amazonaws.personalize#RankingInfluenceType``."""

from typing import Literal, TypeAlias, cast

RankingInfluenceType: TypeAlias = Literal[
    "POPULARITY",
    "FRESHNESS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RankingInfluenceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RankingInfluenceType:
    return cast(RankingInfluenceType, data)
