"""Generated from Smithy shape ``com.amazonaws.directconnect#AddressFamily``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_direct_connect.errors import DeserializationError

AddressFamily: TypeAlias = Literal[
    "ipv4",
    "ipv6",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ipv4",
        "ipv6",
    )
)


def serialize_aws_json_1_1(value: AddressFamily) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AddressFamily:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AddressFamily value: {data!r}")
    return cast(AddressFamily, data)
