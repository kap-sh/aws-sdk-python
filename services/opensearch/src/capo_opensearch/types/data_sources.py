"""Generated from Smithy shape ``com.amazonaws.opensearch#DataSources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.data_source

DataSources: TypeAlias = list["capo_opensearch.types.data_source.DataSource"]


# --- restJson1 ser/de ---
def serialize_json(value: DataSources) -> list:
    import capo_opensearch.types.data_source

    out: list = []
    for item in value:
        out.append(capo_opensearch.types.data_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataSources:
    import capo_opensearch.types.data_source

    out: DataSources = []
    for item in data:
        out.append(capo_opensearch.types.data_source.deserialize_json(item))
    return out
