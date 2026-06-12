"""Generated from Smithy shape ``com.amazonaws.mediaconvert#InputRotate``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Use Rotate to specify how the service rotates your video. You can choose automatic rotation or specify a rotation. You can specify a clockwise rotation of 0, 90, 180, or 270 degrees. If your input video container is .mov or .mp4 and your input has rotation metadata, you can choose Automatic to have the service rotate your video according to the rotation specified in the metadata. The rotation must be within one degree of 90, 180, or 270 degrees. If the rotation metadata specifies any other rotation, the service will default to no rotation. By default, the service does no rotation, even if your input video has rotation metadata. The service doesn't pass through rotation metadata."""
InputRotate: TypeAlias = Literal[
    "DEGREE_0",
    "DEGREES_90",
    "DEGREES_180",
    "DEGREES_270",
    "AUTO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEGREE_0",
        "DEGREES_90",
        "DEGREES_180",
        "DEGREES_270",
        "AUTO",
    )
)


def serialize_json(value: InputRotate) -> str:
    return value


def deserialize_json(data: str) -> InputRotate:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputRotate value: {data!r}")
    return cast(InputRotate, data)
