"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#Provider``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_channel.errors import DeserializationError

Provider: TypeAlias = Literal[
    "DISTRIBUTOR",
    "DISTRIBUTION_SELLER",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISTRIBUTOR",
        "DISTRIBUTION_SELLER",
    )
)


def serialize_aws_json_1_0(value: Provider) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Provider:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Provider value: {data!r}")
    return cast(Provider, data)
