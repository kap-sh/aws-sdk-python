"""Generated from Smithy shape ``com.amazonaws.mediaconvert#VchipAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""The action to take on content advisory XDS packets. If you select PASSTHROUGH, packets will not be changed. If you select STRIP, any packets will be removed in output captions."""
VchipAction: TypeAlias = Literal[
    "PASSTHROUGH",
    "STRIP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASSTHROUGH",
        "STRIP",
    )
)


def serialize_json(value: VchipAction) -> str:
    return value


def deserialize_json(data: str) -> VchipAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VchipAction value: {data!r}")
    return cast(VchipAction, data)
