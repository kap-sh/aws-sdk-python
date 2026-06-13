"""Generated from Smithy shape ``com.amazonaws.quicksight#BrandStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

BrandStatus: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "CREATE_SUCCEEDED",
    "CREATE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_IN_PROGRESS",
        "CREATE_SUCCEEDED",
        "CREATE_FAILED",
        "DELETE_IN_PROGRESS",
        "DELETE_FAILED",
    )
)


def serialize_json(value: BrandStatus) -> str:
    return value


def deserialize_json(data: str) -> BrandStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BrandStatus value: {data!r}")
    return cast(BrandStatus, data)
