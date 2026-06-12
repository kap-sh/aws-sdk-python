"""Generated from Smithy shape ``com.amazonaws.firehose#SSLMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

SSLMode: TypeAlias = Literal[
    "Disabled",
    "Enabled",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Disabled",
        "Enabled",
    )
)


def serialize_aws_json_1_1(value: SSLMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SSLMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SSLMode value: {data!r}")
    return cast(SSLMode, data)
