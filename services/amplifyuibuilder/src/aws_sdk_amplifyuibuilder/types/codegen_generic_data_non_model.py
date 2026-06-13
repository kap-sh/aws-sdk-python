"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenGenericDataNonModel``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.codegen_generic_data_non_model_fields


class CodegenGenericDataNonModel(TypedDict):
    fields: "aws_sdk_amplifyuibuilder.types.codegen_generic_data_non_model_fields.CodegenGenericDataNonModelFields"
    """<p>The fields in a generic data schema non model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodegenGenericDataNonModel) -> dict:
    out: dict = {}
    import aws_sdk_amplifyuibuilder.types.codegen_generic_data_non_model_fields

    out["fields"] = (
        aws_sdk_amplifyuibuilder.types.codegen_generic_data_non_model_fields.serialize_json(
            value["fields"]
        )
    )
    return out


def deserialize_json(data: dict) -> CodegenGenericDataNonModel:
    out: CodegenGenericDataNonModel = {}  # type: ignore[typeddict-item]
    if "fields" in data:
        import aws_sdk_amplifyuibuilder.types.codegen_generic_data_non_model_fields

        out["fields"] = (
            aws_sdk_amplifyuibuilder.types.codegen_generic_data_non_model_fields.deserialize_json(
                data["fields"]
            )
        )
    else:
        raise DeserializationError("CodegenGenericDataNonModel.fields required")
    return out
