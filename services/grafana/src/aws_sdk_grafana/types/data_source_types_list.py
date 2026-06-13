"""Generated from Smithy shape ``com.amazonaws.grafana#DataSourceTypesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_grafana.types.data_source_type

DataSourceTypesList: TypeAlias = list[
    "aws_sdk_grafana.types.data_source_type.DataSourceType"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceTypesList) -> list:
    return list(value)


def deserialize_json(data: list) -> DataSourceTypesList:
    return list(data)
