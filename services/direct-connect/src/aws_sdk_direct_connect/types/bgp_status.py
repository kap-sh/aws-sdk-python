"""Generated from Smithy shape ``com.amazonaws.directconnect#BGPStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_direct_connect.errors import DeserializationError

BGPStatus: TypeAlias = Literal[
    "up",
    "down",
    "unknown",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "up",
        "down",
        "unknown",
    )
)


def serialize_aws_json_1_1(value: BGPStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BGPStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BGPStatus value: {data!r}")
    return cast(BGPStatus, data)
