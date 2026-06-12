"""Generated from Smithy shape ``com.amazonaws.medialive#H265MvOverPictureBoundaries``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H265 Mv Over Picture Boundaries"""
H265MvOverPictureBoundaries: TypeAlias = Literal[
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


def serialize_json(value: H265MvOverPictureBoundaries) -> str:
    return value


def deserialize_json(data: str) -> H265MvOverPictureBoundaries:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown H265MvOverPictureBoundaries value: {data!r}"
        )
    return cast(H265MvOverPictureBoundaries, data)
