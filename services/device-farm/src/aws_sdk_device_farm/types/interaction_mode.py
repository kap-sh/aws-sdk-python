"""Generated from Smithy shape ``com.amazonaws.devicefarm#InteractionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_device_farm.errors import DeserializationError

InteractionMode: TypeAlias = Literal[
    "INTERACTIVE",
    "NO_VIDEO",
    "VIDEO_ONLY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTERACTIVE",
        "NO_VIDEO",
        "VIDEO_ONLY",
    )
)


def serialize_aws_json_1_1(value: InteractionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InteractionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InteractionMode value: {data!r}")
    return cast(InteractionMode, data)
