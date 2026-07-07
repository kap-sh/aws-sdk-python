"""Generated from Smithy shape ``com.amazonaws.appsync#DataSourceIntrospectionModel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.data_source_introspection_model_fields
    import aws_sdk_appsync.types.data_source_introspection_model_index
    import aws_sdk_appsync.types.data_source_introspection_model_indexes
    import aws_sdk_appsync.types.string


class DataSourceIntrospectionModel(TypedDict, closed=True):
    name: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>The name of the model. For example, this could be the name of a single table in a database.</p>"""
    fields: NotRequired[
        "aws_sdk_appsync.types.data_source_introspection_model_fields.DataSourceIntrospectionModelFields"
    ]
    """<p>The <code>DataSourceIntrospectionModelField</code> object data.</p>"""
    primary_key: NotRequired[
        "aws_sdk_appsync.types.data_source_introspection_model_index.DataSourceIntrospectionModelIndex"
    ]
    """<p>The primary key stored as a <code>DataSourceIntrospectionModelIndex</code> object.</p>"""
    indexes: NotRequired[
        "aws_sdk_appsync.types.data_source_introspection_model_indexes.DataSourceIntrospectionModelIndexes"
    ]
    """<p>The array of <code>DataSourceIntrospectionModelIndex</code> objects.</p>"""
    sdl: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>Contains the output of the SDL that was generated from the introspected types. This is controlled by the <code>includeModelsSDL</code> parameter of the <code>GetDataSourceIntrospection</code> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceIntrospectionModel) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "fields" in value:
        import aws_sdk_appsync.types.data_source_introspection_model_fields

        out["fields"] = (
            aws_sdk_appsync.types.data_source_introspection_model_fields.serialize_json(
                value["fields"]
            )
        )
    if "primary_key" in value:
        import aws_sdk_appsync.types.data_source_introspection_model_index

        out["primaryKey"] = (
            aws_sdk_appsync.types.data_source_introspection_model_index.serialize_json(
                value["primary_key"]
            )
        )
    if "indexes" in value:
        import aws_sdk_appsync.types.data_source_introspection_model_indexes

        out["indexes"] = (
            aws_sdk_appsync.types.data_source_introspection_model_indexes.serialize_json(
                value["indexes"]
            )
        )
    if "sdl" in value:
        out["sdl"] = value["sdl"]
    return out


def deserialize_json(data: dict) -> DataSourceIntrospectionModel:
    out: DataSourceIntrospectionModel = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "fields" in data:
        import aws_sdk_appsync.types.data_source_introspection_model_fields

        out["fields"] = (
            aws_sdk_appsync.types.data_source_introspection_model_fields.deserialize_json(
                data["fields"]
            )
        )
    if "primaryKey" in data:
        import aws_sdk_appsync.types.data_source_introspection_model_index

        out["primary_key"] = (
            aws_sdk_appsync.types.data_source_introspection_model_index.deserialize_json(
                data["primaryKey"]
            )
        )
    if "indexes" in data:
        import aws_sdk_appsync.types.data_source_introspection_model_indexes

        out["indexes"] = (
            aws_sdk_appsync.types.data_source_introspection_model_indexes.deserialize_json(
                data["indexes"]
            )
        )
    if "sdl" in data:
        out["sdl"] = data["sdl"]
    return out
