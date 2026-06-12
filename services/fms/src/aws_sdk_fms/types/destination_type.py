"""Generated from Smithy shape ``com.amazonaws.fms#DestinationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fms.errors import DeserializationError

DestinationType: TypeAlias = Literal[
    "IPV4",
    "IPV6",
    "PREFIX_LIST",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IPV4",
        "IPV6",
        "PREFIX_LIST",
    )
)


def serialize_aws_json_1_1(value: DestinationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DestinationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DestinationType value: {data!r}")
    return cast(DestinationType, data)
