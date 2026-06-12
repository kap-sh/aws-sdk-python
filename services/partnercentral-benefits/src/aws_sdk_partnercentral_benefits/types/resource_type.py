"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#ResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_benefits.errors import DeserializationError

ResourceType: TypeAlias = Literal[
    "OPPORTUNITY",
    "BENEFIT_ALLOCATION",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OPPORTUNITY",
        "BENEFIT_ALLOCATION",
    )
)


def serialize_aws_json_1_0(value: ResourceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceType value: {data!r}")
    return cast(ResourceType, data)
