"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowFileType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_supplychain.errors import DeserializationError

DataIntegrationFlowFileType: TypeAlias = Literal[
    "CSV",
    "PARQUET",
    "JSON",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CSV",
        "PARQUET",
        "JSON",
    )
)


def serialize_json(value: DataIntegrationFlowFileType) -> str:
    return value


def deserialize_json(data: str) -> DataIntegrationFlowFileType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataIntegrationFlowFileType value: {data!r}"
        )
    return cast(DataIntegrationFlowFileType, data)
