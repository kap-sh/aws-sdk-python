"""Generated from Smithy shape ``com.amazonaws.dax#SSEStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dax.errors import DeserializationError

SSEStatus: TypeAlias = Literal[
    "ENABLING",
    "ENABLED",
    "DISABLING",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLING",
        "ENABLED",
        "DISABLING",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: SSEStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SSEStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SSEStatus value: {data!r}")
    return cast(SSEStatus, data)
