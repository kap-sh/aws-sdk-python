"""Generated from Smithy shape ``com.amazonaws.mediaconvert#M2tsForceTsVideoEbpOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Keep the default value unless you know that your audio EBP markers are incorrectly appearing before your video EBP markers. To correct this problem, set this value to Force."""
M2tsForceTsVideoEbpOrder: TypeAlias = Literal[
    "FORCE",
    "DEFAULT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FORCE",
        "DEFAULT",
    )
)


def serialize_json(value: M2tsForceTsVideoEbpOrder) -> str:
    return value


def deserialize_json(data: str) -> M2tsForceTsVideoEbpOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown M2tsForceTsVideoEbpOrder value: {data!r}")
    return cast(M2tsForceTsVideoEbpOrder, data)
