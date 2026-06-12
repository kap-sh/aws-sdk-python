"""Generated from Smithy shape ``com.amazonaws.appsync#DataSourceIntrospectionModelFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appsync.types.data_source_introspection_model_field

DataSourceIntrospectionModelFields: TypeAlias = list[
    "aws_sdk_appsync.types.data_source_introspection_model_field.DataSourceIntrospectionModelField"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceIntrospectionModelFields) -> list:
    import aws_sdk_appsync.types.data_source_introspection_model_field

    out: list = []
    for item in value:
        out.append(
            aws_sdk_appsync.types.data_source_introspection_model_field.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DataSourceIntrospectionModelFields:
    import aws_sdk_appsync.types.data_source_introspection_model_field

    out: DataSourceIntrospectionModelFields = []
    for item in data:
        out.append(
            aws_sdk_appsync.types.data_source_introspection_model_field.deserialize_json(
                item
            )
        )
    return out
