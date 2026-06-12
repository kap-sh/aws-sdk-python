"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsKlv``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""M2ts Klv"""
M2tsKlv: TypeAlias = Literal[
    "NONE",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "PASSTHROUGH",
    )
)


def serialize_json(value: M2tsKlv) -> str:
    return value


def deserialize_json(data: str) -> M2tsKlv:
    if data not in _VALUES:
        raise DeserializationError(f"unknown M2tsKlv value: {data!r}")
    return cast(M2tsKlv, data)
