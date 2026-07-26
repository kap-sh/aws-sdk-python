"""Generated from Smithy shape ``com.amazonaws.opensearch#DataSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.data_source_details

DataSourceList: TypeAlias = list[
    "capo_opensearch.types.data_source_details.DataSourceDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceList) -> list:
    import capo_opensearch.types.data_source_details

    out: list = []
    for item in value:
        out.append(capo_opensearch.types.data_source_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataSourceList:
    import capo_opensearch.types.data_source_details

    out: DataSourceList = []
    for item in data:
        out.append(capo_opensearch.types.data_source_details.deserialize_json(item))
    return out
