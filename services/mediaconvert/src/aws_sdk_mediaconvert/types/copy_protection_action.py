"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CopyProtectionAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""The action to take on copy and redistribution control XDS packets. If you select PASSTHROUGH, packets will not be changed. If you select STRIP, any packets will be removed in output captions."""
CopyProtectionAction: TypeAlias = Literal[
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


def serialize_json(value: CopyProtectionAction) -> str:
    return value


def deserialize_json(data: str) -> CopyProtectionAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CopyProtectionAction value: {data!r}")
    return cast(CopyProtectionAction, data)
