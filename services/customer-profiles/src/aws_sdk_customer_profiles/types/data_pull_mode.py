"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DataPullMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

DataPullMode: TypeAlias = Literal[
    "Incremental",
    "Complete",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Incremental",
        "Complete",
    )
)


def serialize_json(value: DataPullMode) -> str:
    return value


def deserialize_json(data: str) -> DataPullMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataPullMode value: {data!r}")
    return cast(DataPullMode, data)
