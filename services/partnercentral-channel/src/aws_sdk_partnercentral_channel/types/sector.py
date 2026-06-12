"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#Sector``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_channel.errors import DeserializationError

Sector: TypeAlias = Literal[
    "COMMERCIAL",
    "GOVERNMENT",
    "GOVERNMENT_EXCEPTION",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMMERCIAL",
        "GOVERNMENT",
        "GOVERNMENT_EXCEPTION",
    )
)


def serialize_aws_json_1_0(value: Sector) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Sector:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Sector value: {data!r}")
    return cast(Sector, data)
