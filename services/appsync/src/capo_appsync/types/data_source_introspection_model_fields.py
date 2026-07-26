"""Generated from Smithy shape ``com.amazonaws.appsync#DataSourceIntrospectionModelFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appsync.types.data_source_introspection_model_field

DataSourceIntrospectionModelFields: TypeAlias = list[
    "capo_appsync.types.data_source_introspection_model_field.DataSourceIntrospectionModelField"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceIntrospectionModelFields) -> list:
    import capo_appsync.types.data_source_introspection_model_field

    out: list = []
    for item in value:
        out.append(
            capo_appsync.types.data_source_introspection_model_field.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DataSourceIntrospectionModelFields:
    import capo_appsync.types.data_source_introspection_model_field

    out: DataSourceIntrospectionModelFields = []
    for item in data:
        out.append(
            capo_appsync.types.data_source_introspection_model_field.deserialize_json(
                item
            )
        )
    return out
