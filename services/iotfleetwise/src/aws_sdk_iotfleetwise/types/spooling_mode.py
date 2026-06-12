"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#SpoolingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

SpoolingMode: TypeAlias = Literal[
    "OFF",
    "TO_DISK",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OFF",
        "TO_DISK",
    )
)


def serialize_aws_json_1_0(value: SpoolingMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SpoolingMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SpoolingMode value: {data!r}")
    return cast(SpoolingMode, data)
