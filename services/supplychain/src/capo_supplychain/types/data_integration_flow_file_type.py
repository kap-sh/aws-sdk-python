"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowFileType``."""

from typing import Literal, TypeAlias, cast

DataIntegrationFlowFileType: TypeAlias = Literal[
    "CSV",
    "PARQUET",
    "JSON",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowFileType) -> str:
    return value


def deserialize_json(data: str) -> DataIntegrationFlowFileType:
    return cast(DataIntegrationFlowFileType, data)
