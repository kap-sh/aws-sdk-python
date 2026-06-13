"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#StartCodegenJobData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.codegen_feature_flags
    import aws_sdk_amplifyuibuilder.types.codegen_job_generic_data_schema
    import aws_sdk_amplifyuibuilder.types.codegen_job_render_config
    import aws_sdk_amplifyuibuilder.types.tags


class StartCodegenJobData(TypedDict):
    render_config: "aws_sdk_amplifyuibuilder.types.codegen_job_render_config.CodegenJobRenderConfig"
    """<p>The code generation configuration for the codegen job.</p>"""
    generic_data_schema: NotRequired[
        "aws_sdk_amplifyuibuilder.types.codegen_job_generic_data_schema.CodegenJobGenericDataSchema"
    ]
    """<p>The data schema to use for a code generation job.</p>"""
    auto_generate_forms: NotRequired["bool"]
    """<p>Specifies whether to autogenerate forms in the code generation job.</p>"""
    features: NotRequired[
        "aws_sdk_amplifyuibuilder.types.codegen_feature_flags.CodegenFeatureFlags"
    ]
    """<p>The feature flags for a code generation job.</p>"""
    tags: NotRequired["aws_sdk_amplifyuibuilder.types.tags.Tags"]
    """<p>One or more key-value pairs to use when tagging the code generation job data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCodegenJobData) -> dict:
    out: dict = {}
    import aws_sdk_amplifyuibuilder.types.codegen_job_render_config

    out["renderConfig"] = (
        aws_sdk_amplifyuibuilder.types.codegen_job_render_config.serialize_json(
            value["render_config"]
        )
    )
    if "generic_data_schema" in value:
        import aws_sdk_amplifyuibuilder.types.codegen_job_generic_data_schema

        out["genericDataSchema"] = (
            aws_sdk_amplifyuibuilder.types.codegen_job_generic_data_schema.serialize_json(
                value["generic_data_schema"]
            )
        )
    if "auto_generate_forms" in value:
        out["autoGenerateForms"] = value["auto_generate_forms"]
    if "features" in value:
        import aws_sdk_amplifyuibuilder.types.codegen_feature_flags

        out["features"] = (
            aws_sdk_amplifyuibuilder.types.codegen_feature_flags.serialize_json(
                value["features"]
            )
        )
    if "tags" in value:
        import aws_sdk_amplifyuibuilder.types.tags

        out["tags"] = aws_sdk_amplifyuibuilder.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartCodegenJobData:
    out: StartCodegenJobData = {}  # type: ignore[typeddict-item]
    if "renderConfig" in data:
        import aws_sdk_amplifyuibuilder.types.codegen_job_render_config

        out["render_config"] = (
            aws_sdk_amplifyuibuilder.types.codegen_job_render_config.deserialize_json(
                data["renderConfig"]
            )
        )
    else:
        raise DeserializationError("StartCodegenJobData.render_config required")
    if "genericDataSchema" in data:
        import aws_sdk_amplifyuibuilder.types.codegen_job_generic_data_schema

        out["generic_data_schema"] = (
            aws_sdk_amplifyuibuilder.types.codegen_job_generic_data_schema.deserialize_json(
                data["genericDataSchema"]
            )
        )
    if "autoGenerateForms" in data:
        out["auto_generate_forms"] = data["autoGenerateForms"]
    if "features" in data:
        import aws_sdk_amplifyuibuilder.types.codegen_feature_flags

        out["features"] = (
            aws_sdk_amplifyuibuilder.types.codegen_feature_flags.deserialize_json(
                data["features"]
            )
        )
    if "tags" in data:
        import aws_sdk_amplifyuibuilder.types.tags

        out["tags"] = aws_sdk_amplifyuibuilder.types.tags.deserialize_json(data["tags"])
    return out
