"""Generated from Smithy shape ``com.amazonaws.datasync#PreserveDevices``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

PreserveDevices: TypeAlias = Literal[
    "NONE",
    "PRESERVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "PRESERVE",
    )
)


def serialize_aws_json_1_1(value: PreserveDevices) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PreserveDevices:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PreserveDevices value: {data!r}")
    return cast(PreserveDevices, data)
