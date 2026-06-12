"""Generated from Smithy shape ``com.amazonaws.personalize#RankingInfluenceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_personalize.errors import DeserializationError

RankingInfluenceType: TypeAlias = Literal[
    "POPULARITY",
    "FRESHNESS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "POPULARITY",
        "FRESHNESS",
    )
)


def serialize_aws_json_1_1(value: RankingInfluenceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RankingInfluenceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RankingInfluenceType value: {data!r}")
    return cast(RankingInfluenceType, data)
