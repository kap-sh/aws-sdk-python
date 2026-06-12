"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ProresInterlaceMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Choose the scan line type for the output. Keep the default value, Progressive to create a progressive output, regardless of the scan type of your input. Use Top field first or Bottom field first to create an output that's interlaced with the same field polarity throughout. Use Follow, default top or Follow, default bottom to produce outputs with the same field polarity as the source. For jobs that have multiple inputs, the output field polarity might change over the course of the output. Follow behavior depends on the input scan type. If the source is interlaced, the output will be interlaced with the same polarity as the source. If the source is progressive, the output will be interlaced with top field bottom field first, depending on which of the Follow options you choose."""
ProresInterlaceMode: TypeAlias = Literal[
    "PROGRESSIVE",
    "TOP_FIELD",
    "BOTTOM_FIELD",
    "FOLLOW_TOP_FIELD",
    "FOLLOW_BOTTOM_FIELD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROGRESSIVE",
        "TOP_FIELD",
        "BOTTOM_FIELD",
        "FOLLOW_TOP_FIELD",
        "FOLLOW_BOTTOM_FIELD",
    )
)


def serialize_json(value: ProresInterlaceMode) -> str:
    return value


def deserialize_json(data: str) -> ProresInterlaceMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProresInterlaceMode value: {data!r}")
    return cast(ProresInterlaceMode, data)
