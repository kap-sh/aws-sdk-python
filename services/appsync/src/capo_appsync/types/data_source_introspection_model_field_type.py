"""Generated from Smithy shape ``com.amazonaws.appsync#DataSourceIntrospectionModelFieldType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.data_source_introspection_model_field_type
    import capo_appsync.types.data_source_introspection_model_field_type_values
    import capo_appsync.types.string


class DataSourceIntrospectionModelFieldType(TypedDict, closed=True):
    kind: NotRequired["capo_appsync.types.string.String"]
    """<p>Specifies the classification of data. For example, this could be set to values like <code>Scalar</code> or <code>NonNull</code> to indicate a fundamental property of the field.</p> <p>Valid values include:</p> <ul> <li> <p> <code>Scalar</code>: Indicates the value is a primitive type (scalar).</p> </li> <li> <p> <code>NonNull</code>: Indicates the field cannot be <code>null</code>.</p> </li> <li> <p> <code>List</code>: Indicates the field contains a list.</p> </li> </ul>"""
    name: NotRequired["capo_appsync.types.string.String"]
    """<p>The name of the data type that represents the field. For example, <code>String</code> is a valid <code>name</code> value.</p>"""
    type: NotRequired[
        "capo_appsync.types.data_source_introspection_model_field_type.DataSourceIntrospectionModelFieldType"
    ]
    """<p>The <code>DataSourceIntrospectionModelFieldType</code> object data. The <code>type</code> is only present if <code>DataSourceIntrospectionModelFieldType.kind</code> is set to <code>NonNull</code> or <code>List</code>. </p> <p>The <code>type</code> typically contains its own <code>kind</code> and <code>name</code> fields to represent the actual type data. For instance, <code>type</code> could contain a <code>kind</code> value of <code>Scalar</code> with a <code>name</code> value of <code>String</code>. The values <code>Scalar</code> and <code>String</code> will be collectively stored in the <code>values</code> field.</p>"""
    values: NotRequired[
        "capo_appsync.types.data_source_introspection_model_field_type_values.DataSourceIntrospectionModelFieldTypeValues"
    ]
    """<p>The values of the <code>type</code> field. This field represents the AppSync data type equivalent of the introspected field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceIntrospectionModelFieldType) -> dict:
    out: dict = {}
    if "kind" in value:
        out["kind"] = value["kind"]
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        import capo_appsync.types.data_source_introspection_model_field_type

        out["type"] = (
            capo_appsync.types.data_source_introspection_model_field_type.serialize_json(
                value["type"]
            )
        )
    if "values" in value:
        import capo_appsync.types.data_source_introspection_model_field_type_values

        out["values"] = (
            capo_appsync.types.data_source_introspection_model_field_type_values.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSourceIntrospectionModelFieldType:
    out: DataSourceIntrospectionModelFieldType = {}  # type: ignore[typeddict-item]
    if "kind" in data:
        out["kind"] = data["kind"]
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        import capo_appsync.types.data_source_introspection_model_field_type

        out["type"] = (
            capo_appsync.types.data_source_introspection_model_field_type.deserialize_json(
                data["type"]
            )
        )
    if "values" in data:
        import capo_appsync.types.data_source_introspection_model_field_type_values

        out["values"] = (
            capo_appsync.types.data_source_introspection_model_field_type_values.deserialize_json(
                data["values"]
            )
        )
    return out
