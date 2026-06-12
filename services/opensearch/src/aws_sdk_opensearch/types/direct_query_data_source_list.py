"""Generated from Smithy shape ``com.amazonaws.opensearch#DirectQueryDataSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.direct_query_data_source

DirectQueryDataSourceList: TypeAlias = list[
    "aws_sdk_opensearch.types.direct_query_data_source.DirectQueryDataSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: DirectQueryDataSourceList) -> list:
    import aws_sdk_opensearch.types.direct_query_data_source

    out: list = []
    for item in value:
        out.append(
            aws_sdk_opensearch.types.direct_query_data_source.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DirectQueryDataSourceList:
    import aws_sdk_opensearch.types.direct_query_data_source

    out: DirectQueryDataSourceList = []
    for item in data:
        out.append(
            aws_sdk_opensearch.types.direct_query_data_source.deserialize_json(item)
        )
    return out
