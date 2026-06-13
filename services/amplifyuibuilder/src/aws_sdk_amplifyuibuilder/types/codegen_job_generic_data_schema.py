"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenJobGenericDataSchema``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.codegen_generic_data_enums
    import aws_sdk_amplifyuibuilder.types.codegen_generic_data_models
    import aws_sdk_amplifyuibuilder.types.codegen_generic_data_non_models
    import aws_sdk_amplifyuibuilder.types.codegen_job_generic_data_source_type


class CodegenJobGenericDataSchema(TypedDict):
    data_source_type: "aws_sdk_amplifyuibuilder.types.codegen_job_generic_data_source_type.CodegenJobGenericDataSourceType"
    """<p>The type of the data source for the schema. Currently, the only valid value is an Amplify <code>DataStore</code>.</p>"""
    models: "aws_sdk_amplifyuibuilder.types.codegen_generic_data_models.CodegenGenericDataModels"
    """<p>The name of a <code>CodegenGenericDataModel</code>.</p>"""
    enums: "aws_sdk_amplifyuibuilder.types.codegen_generic_data_enums.CodegenGenericDataEnums"
    """<p>The name of a <code>CodegenGenericDataEnum</code>.</p>"""
    non_models: "aws_sdk_amplifyuibuilder.types.codegen_generic_data_non_models.CodegenGenericDataNonModels"
    """<p>The name of a <code>CodegenGenericDataNonModel</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodegenJobGenericDataSchema) -> dict:
    out: dict = {}
    import aws_sdk_amplifyuibuilder.types.codegen_job_generic_data_source_type

    out["dataSourceType"] = (
        aws_sdk_amplifyuibuilder.types.codegen_job_generic_data_source_type.serialize_json(
            value["data_source_type"]
        )
    )
    import aws_sdk_amplifyuibuilder.types.codegen_generic_data_models

    out["models"] = (
        aws_sdk_amplifyuibuilder.types.codegen_generic_data_models.serialize_json(
            value["models"]
        )
    )
    import aws_sdk_amplifyuibuilder.types.codegen_generic_data_enums

    out["enums"] = (
        aws_sdk_amplifyuibuilder.types.codegen_generic_data_enums.serialize_json(
            value["enums"]
        )
    )
    import aws_sdk_amplifyuibuilder.types.codegen_generic_data_non_models

    out["nonModels"] = (
        aws_sdk_amplifyuibuilder.types.codegen_generic_data_non_models.serialize_json(
            value["non_models"]
        )
    )
    return out


def deserialize_json(data: dict) -> CodegenJobGenericDataSchema:
    out: CodegenJobGenericDataSchema = {}  # type: ignore[typeddict-item]
    if "dataSourceType" in data:
        import aws_sdk_amplifyuibuilder.types.codegen_job_generic_data_source_type

        out["data_source_type"] = (
            aws_sdk_amplifyuibuilder.types.codegen_job_generic_data_source_type.deserialize_json(
                data["dataSourceType"]
            )
        )
    else:
        raise DeserializationError(
            "CodegenJobGenericDataSchema.data_source_type required"
        )
    if "models" in data:
        import aws_sdk_amplifyuibuilder.types.codegen_generic_data_models

        out["models"] = (
            aws_sdk_amplifyuibuilder.types.codegen_generic_data_models.deserialize_json(
                data["models"]
            )
        )
    else:
        raise DeserializationError("CodegenJobGenericDataSchema.models required")
    if "enums" in data:
        import aws_sdk_amplifyuibuilder.types.codegen_generic_data_enums

        out["enums"] = (
            aws_sdk_amplifyuibuilder.types.codegen_generic_data_enums.deserialize_json(
                data["enums"]
            )
        )
    else:
        raise DeserializationError("CodegenJobGenericDataSchema.enums required")
    if "nonModels" in data:
        import aws_sdk_amplifyuibuilder.types.codegen_generic_data_non_models

        out["non_models"] = (
            aws_sdk_amplifyuibuilder.types.codegen_generic_data_non_models.deserialize_json(
                data["nonModels"]
            )
        )
    else:
        raise DeserializationError("CodegenJobGenericDataSchema.non_models required")
    return out
