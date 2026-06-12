"""Generated from Smithy shape ``com.amazonaws.medialive#VideoDescriptionScalingBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Video Description Scaling Behavior"""
VideoDescriptionScalingBehavior: TypeAlias = Literal[
    "DEFAULT",
    "STRETCH_TO_OUTPUT",
    "SMART_CROP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT",
        "STRETCH_TO_OUTPUT",
        "SMART_CROP",
    )
)


def serialize_json(value: VideoDescriptionScalingBehavior) -> str:
    return value


def deserialize_json(data: str) -> VideoDescriptionScalingBehavior:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown VideoDescriptionScalingBehavior value: {data!r}"
        )
    return cast(VideoDescriptionScalingBehavior, data)
