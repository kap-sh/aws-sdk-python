"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomContentImageScalingConfiguration``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

CustomContentImageScalingConfiguration: TypeAlias = Literal[
    "FIT_TO_HEIGHT",
    "FIT_TO_WIDTH",
    "DO_NOT_SCALE",
    "SCALE_TO_VISUAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FIT_TO_HEIGHT",
        "FIT_TO_WIDTH",
        "DO_NOT_SCALE",
        "SCALE_TO_VISUAL",
    )
)


def serialize_json(value: CustomContentImageScalingConfiguration) -> str:
    return value


def deserialize_json(data: str) -> CustomContentImageScalingConfiguration:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CustomContentImageScalingConfiguration value: {data!r}"
        )
    return cast(CustomContentImageScalingConfiguration, data)
