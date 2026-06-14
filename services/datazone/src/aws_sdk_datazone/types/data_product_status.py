"""Generated from Smithy shape ``com.amazonaws.datazone#DataProductStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

DataProductStatus: TypeAlias = Literal[
    "CREATED",
    "CREATING",
    "CREATE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED",
        "CREATING",
        "CREATE_FAILED",
    )
)


def serialize_json(value: DataProductStatus) -> str:
    return value


def deserialize_json(data: str) -> DataProductStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataProductStatus value: {data!r}")
    return cast(DataProductStatus, data)
