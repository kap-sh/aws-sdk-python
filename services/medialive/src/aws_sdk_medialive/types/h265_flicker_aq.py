"""Generated from Smithy shape ``com.amazonaws.medialive#H265FlickerAq``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H265 Flicker Aq"""
H265FlickerAq: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: H265FlickerAq) -> str:
    return value


def deserialize_json(data: str) -> H265FlickerAq:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H265FlickerAq value: {data!r}")
    return cast(H265FlickerAq, data)
