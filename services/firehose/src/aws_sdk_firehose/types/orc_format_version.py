"""Generated from Smithy shape ``com.amazonaws.firehose#OrcFormatVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

OrcFormatVersion: TypeAlias = Literal[
    "V0_11",
    "V0_12",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "V0_11",
        "V0_12",
    )
)


def serialize_aws_json_1_1(value: OrcFormatVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OrcFormatVersion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OrcFormatVersion value: {data!r}")
    return cast(OrcFormatVersion, data)
