"""Generated from Smithy shape ``com.amazonaws.quicksight#SharingModel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

SharingModel: TypeAlias = Literal[
    "ACCOUNT",
    "NAMESPACE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCOUNT",
        "NAMESPACE",
    )
)


def serialize_json(value: SharingModel) -> str:
    return value


def deserialize_json(data: str) -> SharingModel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SharingModel value: {data!r}")
    return cast(SharingModel, data)
