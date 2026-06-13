"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenGenericDataEnum``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.codegen_generic_data_enum_values_list


class CodegenGenericDataEnum(TypedDict):
    values: "aws_sdk_amplifyuibuilder.types.codegen_generic_data_enum_values_list.CodegenGenericDataEnumValuesList"
    """<p>The list of enum values in the generic data schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodegenGenericDataEnum) -> dict:
    out: dict = {}
    import aws_sdk_amplifyuibuilder.types.codegen_generic_data_enum_values_list

    out["values"] = (
        aws_sdk_amplifyuibuilder.types.codegen_generic_data_enum_values_list.serialize_json(
            value["values"]
        )
    )
    return out


def deserialize_json(data: dict) -> CodegenGenericDataEnum:
    out: CodegenGenericDataEnum = {}  # type: ignore[typeddict-item]
    if "values" in data:
        import aws_sdk_amplifyuibuilder.types.codegen_generic_data_enum_values_list

        out["values"] = (
            aws_sdk_amplifyuibuilder.types.codegen_generic_data_enum_values_list.deserialize_json(
                data["values"]
            )
        )
    else:
        raise DeserializationError("CodegenGenericDataEnum.values required")
    return out
