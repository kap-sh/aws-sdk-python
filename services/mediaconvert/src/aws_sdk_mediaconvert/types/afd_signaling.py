"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AfdSignaling``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""This setting only applies to H.264, H.265, and MPEG2 outputs. Use Insert AFD signaling to specify whether the service includes AFD values in the output video data and what those values are. * Choose None to remove all AFD values from this output. * Choose Fixed to ignore input AFD values and instead encode the value specified in the job. * Choose Auto to calculate output AFD values based on the input AFD scaler data."""
AfdSignaling: TypeAlias = Literal[
    "NONE",
    "AUTO",
    "FIXED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "AUTO",
        "FIXED",
    )
)


def serialize_json(value: AfdSignaling) -> str:
    return value


def deserialize_json(data: str) -> AfdSignaling:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AfdSignaling value: {data!r}")
    return cast(AfdSignaling, data)
