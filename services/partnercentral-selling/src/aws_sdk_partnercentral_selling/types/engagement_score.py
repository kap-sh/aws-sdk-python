"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementScore``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

EngagementScore: TypeAlias = Literal[
    "High",
    "Medium",
    "Low",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "High",
        "Medium",
        "Low",
    )
)


def serialize_aws_json_1_0(value: EngagementScore) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EngagementScore:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EngagementScore value: {data!r}")
    return cast(EngagementScore, data)
