"""Generated from Smithy shape ``com.amazonaws.appsync#DataSourceIntrospectionModelIndexes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appsync.types.data_source_introspection_model_index

DataSourceIntrospectionModelIndexes: TypeAlias = list[
    "aws_sdk_appsync.types.data_source_introspection_model_index.DataSourceIntrospectionModelIndex"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceIntrospectionModelIndexes) -> list:
    import aws_sdk_appsync.types.data_source_introspection_model_index

    out: list = []
    for item in value:
        out.append(
            aws_sdk_appsync.types.data_source_introspection_model_index.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DataSourceIntrospectionModelIndexes:
    import aws_sdk_appsync.types.data_source_introspection_model_index

    out: DataSourceIntrospectionModelIndexes = []
    for item in data:
        out.append(
            aws_sdk_appsync.types.data_source_introspection_model_index.deserialize_json(
                item
            )
        )
    return out
