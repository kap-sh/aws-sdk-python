"""Generated from Smithy shape ``com.amazonaws.ssm#PingStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

PingStatus: TypeAlias = Literal[
    "Online",
    "ConnectionLost",
    "Inactive",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Online",
        "ConnectionLost",
        "Inactive",
    )
)


def serialize_aws_json_1_1(value: PingStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PingStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PingStatus value: {data!r}")
    return cast(PingStatus, data)
