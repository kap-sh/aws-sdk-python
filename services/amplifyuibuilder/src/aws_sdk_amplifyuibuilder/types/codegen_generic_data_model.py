"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenGenericDataModel``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.codegen_generic_data_fields
    import aws_sdk_amplifyuibuilder.types.codegen_primary_keys_list


class CodegenGenericDataModel(TypedDict):
    fields: "aws_sdk_amplifyuibuilder.types.codegen_generic_data_fields.CodegenGenericDataFields"
    """<p>The fields in the generic data model.</p>"""
    is_join_table: NotRequired["bool"]
    """<p>Specifies whether the generic data model is a join table.</p>"""
    primary_keys: "aws_sdk_amplifyuibuilder.types.codegen_primary_keys_list.CodegenPrimaryKeysList"
    """<p>The primary keys of the generic data model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodegenGenericDataModel) -> dict:
    out: dict = {}
    import aws_sdk_amplifyuibuilder.types.codegen_generic_data_fields

    out["fields"] = (
        aws_sdk_amplifyuibuilder.types.codegen_generic_data_fields.serialize_json(
            value["fields"]
        )
    )
    if "is_join_table" in value:
        out["isJoinTable"] = value["is_join_table"]
    import aws_sdk_amplifyuibuilder.types.codegen_primary_keys_list

    out["primaryKeys"] = (
        aws_sdk_amplifyuibuilder.types.codegen_primary_keys_list.serialize_json(
            value["primary_keys"]
        )
    )
    return out


def deserialize_json(data: dict) -> CodegenGenericDataModel:
    out: CodegenGenericDataModel = {}  # type: ignore[typeddict-item]
    if "fields" in data:
        import aws_sdk_amplifyuibuilder.types.codegen_generic_data_fields

        out["fields"] = (
            aws_sdk_amplifyuibuilder.types.codegen_generic_data_fields.deserialize_json(
                data["fields"]
            )
        )
    else:
        raise DeserializationError("CodegenGenericDataModel.fields required")
    if "isJoinTable" in data:
        out["is_join_table"] = data["isJoinTable"]
    if "primaryKeys" in data:
        import aws_sdk_amplifyuibuilder.types.codegen_primary_keys_list

        out["primary_keys"] = (
            aws_sdk_amplifyuibuilder.types.codegen_primary_keys_list.deserialize_json(
                data["primaryKeys"]
            )
        )
    else:
        raise DeserializationError("CodegenGenericDataModel.primary_keys required")
    return out
