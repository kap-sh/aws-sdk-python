"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#UpdateMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

UpdateMode: TypeAlias = Literal[
    "Overwrite",
    "Merge",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Overwrite",
        "Merge",
    )
)


def serialize_aws_json_1_0(value: UpdateMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> UpdateMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpdateMode value: {data!r}")
    return cast(UpdateMode, data)
