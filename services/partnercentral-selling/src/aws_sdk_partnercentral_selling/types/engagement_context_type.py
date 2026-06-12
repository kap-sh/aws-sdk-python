"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementContextType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

EngagementContextType: TypeAlias = Literal[
    "CustomerProject",
    "Lead",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CustomerProject",
        "Lead",
    )
)


def serialize_aws_json_1_0(value: EngagementContextType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EngagementContextType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EngagementContextType value: {data!r}")
    return cast(EngagementContextType, data)
