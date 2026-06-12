"""Generated from Smithy shape ``com.amazonaws.medialive#LastFrameClippingBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""If you specify a StopTimecode in an input (in order to clip the file), you can specify if you want the clip to exclude (the default) or include the frame specified by the timecode."""
LastFrameClippingBehavior: TypeAlias = Literal[
    "EXCLUDE_LAST_FRAME",
    "INCLUDE_LAST_FRAME",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXCLUDE_LAST_FRAME",
        "INCLUDE_LAST_FRAME",
    )
)


def serialize_json(value: LastFrameClippingBehavior) -> str:
    return value


def deserialize_json(data: str) -> LastFrameClippingBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LastFrameClippingBehavior value: {data!r}")
    return cast(LastFrameClippingBehavior, data)
