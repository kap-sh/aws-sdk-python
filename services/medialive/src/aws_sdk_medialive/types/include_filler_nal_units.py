"""Generated from Smithy shape ``com.amazonaws.medialive#IncludeFillerNalUnits``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Include Filler Nal Units"""
IncludeFillerNalUnits: TypeAlias = Literal[
    "AUTO",
    "DROP",
    "INCLUDE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "DROP",
        "INCLUDE",
    )
)


def serialize_json(value: IncludeFillerNalUnits) -> str:
    return value


def deserialize_json(data: str) -> IncludeFillerNalUnits:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IncludeFillerNalUnits value: {data!r}")
    return cast(IncludeFillerNalUnits, data)
