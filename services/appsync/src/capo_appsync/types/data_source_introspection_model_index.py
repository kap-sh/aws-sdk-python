"""Generated from Smithy shape ``com.amazonaws.appsync#DataSourceIntrospectionModelIndex``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.data_source_introspection_model_index_fields
    import capo_appsync.types.string


class DataSourceIntrospectionModelIndex(TypedDict, closed=True):
    name: NotRequired["capo_appsync.types.string.String"]
    """<p>The name of the index.</p>"""
    fields: NotRequired[
        "capo_appsync.types.data_source_introspection_model_index_fields.DataSourceIntrospectionModelIndexFields"
    ]
    """<p>The fields of the index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceIntrospectionModelIndex) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "fields" in value:
        import capo_appsync.types.data_source_introspection_model_index_fields

        out["fields"] = (
            capo_appsync.types.data_source_introspection_model_index_fields.serialize_json(
                value["fields"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSourceIntrospectionModelIndex:
    out: DataSourceIntrospectionModelIndex = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "fields" in data:
        import capo_appsync.types.data_source_introspection_model_index_fields

        out["fields"] = (
            capo_appsync.types.data_source_introspection_model_index_fields.deserialize_json(
                data["fields"]
            )
        )
    return out
