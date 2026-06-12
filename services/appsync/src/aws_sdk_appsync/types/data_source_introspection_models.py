"""Generated from Smithy shape ``com.amazonaws.appsync#DataSourceIntrospectionModels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appsync.types.data_source_introspection_model

DataSourceIntrospectionModels: TypeAlias = list[
    "aws_sdk_appsync.types.data_source_introspection_model.DataSourceIntrospectionModel"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceIntrospectionModels) -> list:
    import aws_sdk_appsync.types.data_source_introspection_model

    out: list = []
    for item in value:
        out.append(
            aws_sdk_appsync.types.data_source_introspection_model.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DataSourceIntrospectionModels:
    import aws_sdk_appsync.types.data_source_introspection_model

    out: DataSourceIntrospectionModels = []
    for item in data:
        out.append(
            aws_sdk_appsync.types.data_source_introspection_model.deserialize_json(item)
        )
    return out
