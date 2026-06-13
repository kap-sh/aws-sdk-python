"""Generated from Smithy shape ``com.amazonaws.quicksight#BrandVersionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

BrandVersionStatus: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "CREATE_SUCCEEDED",
    "CREATE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_IN_PROGRESS",
        "CREATE_SUCCEEDED",
        "CREATE_FAILED",
    )
)


def serialize_json(value: BrandVersionStatus) -> str:
    return value


def deserialize_json(data: str) -> BrandVersionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BrandVersionStatus value: {data!r}")
    return cast(BrandVersionStatus, data)
