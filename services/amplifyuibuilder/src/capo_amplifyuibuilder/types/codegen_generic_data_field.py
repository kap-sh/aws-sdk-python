"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenGenericDataField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.codegen_generic_data_field_data_type
    import capo_amplifyuibuilder.types.codegen_generic_data_relationship_type


class CodegenGenericDataField(TypedDict, closed=True):
    data_type: "capo_amplifyuibuilder.types.codegen_generic_data_field_data_type.CodegenGenericDataFieldDataType"
    """<p>The data type for the generic data field.</p>"""
    data_type_value: "str"
    """<p>The value of the data type for the generic data field.</p>"""
    required: "bool"
    """<p>Specifies whether the generic data field is required.</p>"""
    read_only: "bool"
    """<p>Specifies whether the generic data field is read-only.</p>"""
    is_array: "bool"
    """<p>Specifies whether the generic data field is an array.</p>"""
    relationship: NotRequired[
        "capo_amplifyuibuilder.types.codegen_generic_data_relationship_type.CodegenGenericDataRelationshipType"
    ]
    """<p>The relationship of the generic data schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodegenGenericDataField) -> dict:
    out: dict = {}
    import capo_amplifyuibuilder.types.codegen_generic_data_field_data_type

    out["dataType"] = (
        capo_amplifyuibuilder.types.codegen_generic_data_field_data_type.serialize_json(
            value["data_type"]
        )
    )
    out["dataTypeValue"] = value["data_type_value"]
    out["required"] = value["required"]
    out["readOnly"] = value["read_only"]
    out["isArray"] = value["is_array"]
    if "relationship" in value:
        import capo_amplifyuibuilder.types.codegen_generic_data_relationship_type

        out["relationship"] = (
            capo_amplifyuibuilder.types.codegen_generic_data_relationship_type.serialize_json(
                value["relationship"]
            )
        )
    return out


def deserialize_json(data: dict) -> CodegenGenericDataField:
    out: CodegenGenericDataField = {}  # type: ignore[typeddict-item]
    if "dataType" in data:
        import capo_amplifyuibuilder.types.codegen_generic_data_field_data_type

        out["data_type"] = (
            capo_amplifyuibuilder.types.codegen_generic_data_field_data_type.deserialize_json(
                data["dataType"]
            )
        )
    else:
        raise DeserializationError("CodegenGenericDataField.data_type required")
    if "dataTypeValue" in data:
        out["data_type_value"] = data["dataTypeValue"]
    else:
        raise DeserializationError("CodegenGenericDataField.data_type_value required")
    if "required" in data:
        out["required"] = data["required"]
    else:
        raise DeserializationError("CodegenGenericDataField.required required")
    if "readOnly" in data:
        out["read_only"] = data["readOnly"]
    else:
        raise DeserializationError("CodegenGenericDataField.read_only required")
    if "isArray" in data:
        out["is_array"] = data["isArray"]
    else:
        raise DeserializationError("CodegenGenericDataField.is_array required")
    if "relationship" in data:
        import capo_amplifyuibuilder.types.codegen_generic_data_relationship_type

        out["relationship"] = (
            capo_amplifyuibuilder.types.codegen_generic_data_relationship_type.deserialize_json(
                data["relationship"]
            )
        )
    return out
