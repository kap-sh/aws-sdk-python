"""Generated from Smithy shape ``com.amazonaws.ivs#MultitrackMaximumResolution``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ivs.errors import DeserializationError

MultitrackMaximumResolution: TypeAlias = Literal[
    "SD",
    "HD",
    "FULL_HD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SD",
        "HD",
        "FULL_HD",
    )
)


def serialize_json(value: MultitrackMaximumResolution) -> str:
    return value


def deserialize_json(data: str) -> MultitrackMaximumResolution:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MultitrackMaximumResolution value: {data!r}"
        )
    return cast(MultitrackMaximumResolution, data)
