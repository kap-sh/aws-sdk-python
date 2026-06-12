"""Generated from Smithy shape ``com.amazonaws.mediaconvert#M2tsScte35Source``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""For SCTE-35 markers from your input-- Choose Passthrough if you want SCTE-35 markers that appear in your input to also appear in this output. Choose None if you don't want SCTE-35 markers in this output. For SCTE-35 markers from an ESAM XML document-- Choose None. Also provide the ESAM XML as a string in the setting Signal processing notification XML. Also enable ESAM SCTE-35 (include the property scte35Esam)."""
M2tsScte35Source: TypeAlias = Literal[
    "PASSTHROUGH",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASSTHROUGH",
        "NONE",
    )
)


def serialize_json(value: M2tsScte35Source) -> str:
    return value


def deserialize_json(data: str) -> M2tsScte35Source:
    if data not in _VALUES:
        raise DeserializationError(f"unknown M2tsScte35Source value: {data!r}")
    return cast(M2tsScte35Source, data)
