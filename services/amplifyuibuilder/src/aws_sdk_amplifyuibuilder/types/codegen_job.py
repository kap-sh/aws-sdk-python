"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_amplifyuibuilder.types.app_id
    import aws_sdk_amplifyuibuilder.types.codegen_dependencies
    import aws_sdk_amplifyuibuilder.types.codegen_feature_flags
    import aws_sdk_amplifyuibuilder.types.codegen_job_asset
    import aws_sdk_amplifyuibuilder.types.codegen_job_generic_data_schema
    import aws_sdk_amplifyuibuilder.types.codegen_job_render_config
    import aws_sdk_amplifyuibuilder.types.codegen_job_status
    import aws_sdk_amplifyuibuilder.types.tags
    import aws_sdk_amplifyuibuilder.types.uuid


class CodegenJob(TypedDict, closed=True):
    id: "aws_sdk_amplifyuibuilder.types.uuid.Uuid"
    """<p>The unique ID for the code generation job.</p>"""
    app_id: "aws_sdk_amplifyuibuilder.types.app_id.AppId"
    """<p>The ID of the Amplify app associated with the code generation job.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment associated with the code generation job.</p>"""
    render_config: NotRequired[
        "aws_sdk_amplifyuibuilder.types.codegen_job_render_config.CodegenJobRenderConfig"
    ]
    generic_data_schema: NotRequired[
        "aws_sdk_amplifyuibuilder.types.codegen_job_generic_data_schema.CodegenJobGenericDataSchema"
    ]
    auto_generate_forms: NotRequired["bool"]
    """<p>Specifies whether to autogenerate forms in the code generation job.</p>"""
    features: NotRequired[
        "aws_sdk_amplifyuibuilder.types.codegen_feature_flags.CodegenFeatureFlags"
    ]
    status: NotRequired[
        "aws_sdk_amplifyuibuilder.types.codegen_job_status.CodegenJobStatus"
    ]
    """<p>The status of the code generation job.</p>"""
    status_message: NotRequired["str"]
    """<p>The customized status message for the code generation job.</p>"""
    asset: NotRequired[
        "aws_sdk_amplifyuibuilder.types.codegen_job_asset.CodegenJobAsset"
    ]
    """<p>The <code>CodegenJobAsset</code> to use for the code generation job.</p>"""
    tags: NotRequired["aws_sdk_amplifyuibuilder.types.tags.Tags"]
    """<p>One or more key-value pairs to use when tagging the code generation job.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The time that the code generation job was created.</p>"""
    modified_at: NotRequired["datetime.datetime"]
    """<p>The time that the code generation job was modified.</p>"""
    dependencies: NotRequired[
        "aws_sdk_amplifyuibuilder.types.codegen_dependencies.CodegenDependencies"
    ]
    """<p>Lists the dependency packages that may be required for the project code to run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodegenJob) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["appId"] = value["app_id"]
    out["environmentName"] = value["environment_name"]
    if "render_config" in value:
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
    if "status" in value:
        import aws_sdk_amplifyuibuilder.types.codegen_job_status

        out["status"] = (
            aws_sdk_amplifyuibuilder.types.codegen_job_status.serialize_json(
                value["status"]
            )
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "asset" in value:
        import aws_sdk_amplifyuibuilder.types.codegen_job_asset

        out["asset"] = aws_sdk_amplifyuibuilder.types.codegen_job_asset.serialize_json(
            value["asset"]
        )
    if "tags" in value:
        import aws_sdk_amplifyuibuilder.types.tags

        out["tags"] = aws_sdk_amplifyuibuilder.types.tags.serialize_json(value["tags"])
    if "created_at" in value:
        import aws_sdk_amplifyuibuilder.types._prelude.timestamp

        out["createdAt"] = (
            aws_sdk_amplifyuibuilder.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "modified_at" in value:
        import aws_sdk_amplifyuibuilder.types._prelude.timestamp

        out["modifiedAt"] = (
            aws_sdk_amplifyuibuilder.types._prelude.timestamp.serialize_json(
                value["modified_at"]
            )
        )
    if "dependencies" in value:
        import aws_sdk_amplifyuibuilder.types.codegen_dependencies

        out["dependencies"] = (
            aws_sdk_amplifyuibuilder.types.codegen_dependencies.serialize_json(
                value["dependencies"]
            )
        )
    return out


def deserialize_json(data: dict) -> CodegenJob:
    out: CodegenJob = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CodegenJob.id required")
    if "appId" in data:
        out["app_id"] = data["appId"]
    else:
        raise DeserializationError("CodegenJob.app_id required")
    if "environmentName" in data:
        out["environment_name"] = data["environmentName"]
    else:
        raise DeserializationError("CodegenJob.environment_name required")
    if "renderConfig" in data:
        import aws_sdk_amplifyuibuilder.types.codegen_job_render_config

        out["render_config"] = (
            aws_sdk_amplifyuibuilder.types.codegen_job_render_config.deserialize_json(
                data["renderConfig"]
            )
        )
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
    if "status" in data:
        import aws_sdk_amplifyuibuilder.types.codegen_job_status

        out["status"] = (
            aws_sdk_amplifyuibuilder.types.codegen_job_status.deserialize_json(
                data["status"]
            )
        )
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "asset" in data:
        import aws_sdk_amplifyuibuilder.types.codegen_job_asset

        out["asset"] = (
            aws_sdk_amplifyuibuilder.types.codegen_job_asset.deserialize_json(
                data["asset"]
            )
        )
    if "tags" in data:
        import aws_sdk_amplifyuibuilder.types.tags

        out["tags"] = aws_sdk_amplifyuibuilder.types.tags.deserialize_json(data["tags"])
    if "createdAt" in data:
        import aws_sdk_amplifyuibuilder.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_amplifyuibuilder.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "modifiedAt" in data:
        import aws_sdk_amplifyuibuilder.types._prelude.timestamp

        out["modified_at"] = (
            aws_sdk_amplifyuibuilder.types._prelude.timestamp.deserialize_json(
                data["modifiedAt"]
            )
        )
    if "dependencies" in data:
        import aws_sdk_amplifyuibuilder.types.codegen_dependencies

        out["dependencies"] = (
            aws_sdk_amplifyuibuilder.types.codegen_dependencies.deserialize_json(
                data["dependencies"]
            )
        )
    return out
