"""Generated from Smithy shape ``com.amazonaws.clouddirectory#FacetStyle``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_clouddirectory.errors import DeserializationError

FacetStyle: TypeAlias = Literal[
    "STATIC",
    "DYNAMIC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STATIC",
        "DYNAMIC",
    )
)


def serialize_json(value: FacetStyle) -> str:
    return value


def deserialize_json(data: str) -> FacetStyle:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FacetStyle value: {data!r}")
    return cast(FacetStyle, data)
