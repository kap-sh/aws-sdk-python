"""Generated from Smithy shape ``com.amazonaws.appsync#DataSourceIntrospectionModelField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.data_source_introspection_model_field_type
    import capo_appsync.types.long
    import capo_appsync.types.string


class DataSourceIntrospectionModelField(TypedDict, closed=True):
    name: NotRequired["capo_appsync.types.string.String"]
    """<p>The name of the field that was retrieved from the introspected data.</p>"""
    type: NotRequired[
        "capo_appsync.types.data_source_introspection_model_field_type.DataSourceIntrospectionModelFieldType"
    ]
    """<p>The <code>DataSourceIntrospectionModelFieldType</code> object data.</p>"""
    length: "capo_appsync.types.long.Long"
    """<p>The length value of the introspected field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceIntrospectionModelField) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        import capo_appsync.types.data_source_introspection_model_field_type

        out["type"] = (
            capo_appsync.types.data_source_introspection_model_field_type.serialize_json(
                value["type"]
            )
        )
    out["length"] = value.get("length", 0)
    return out


def deserialize_json(data: dict) -> DataSourceIntrospectionModelField:
    out: DataSourceIntrospectionModelField = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        import capo_appsync.types.data_source_introspection_model_field_type

        out["type"] = (
            capo_appsync.types.data_source_introspection_model_field_type.deserialize_json(
                data["type"]
            )
        )
    if "length" in data:
        out["length"] = data["length"]
    else:
        out["length"] = 0
    return out
