"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_amplifyuibuilder.types.app_id
    import capo_amplifyuibuilder.types.codegen_dependencies
    import capo_amplifyuibuilder.types.codegen_feature_flags
    import capo_amplifyuibuilder.types.codegen_job_asset
    import capo_amplifyuibuilder.types.codegen_job_generic_data_schema
    import capo_amplifyuibuilder.types.codegen_job_render_config
    import capo_amplifyuibuilder.types.codegen_job_status
    import capo_amplifyuibuilder.types.tags
    import capo_amplifyuibuilder.types.uuid


class CodegenJob(TypedDict, closed=True):
    id: "capo_amplifyuibuilder.types.uuid.Uuid"
    """<p>The unique ID for the code generation job.</p>"""
    app_id: "capo_amplifyuibuilder.types.app_id.AppId"
    """<p>The ID of the Amplify app associated with the code generation job.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment associated with the code generation job.</p>"""
    render_config: NotRequired[
        "capo_amplifyuibuilder.types.codegen_job_render_config.CodegenJobRenderConfig"
    ]
    generic_data_schema: NotRequired[
        "capo_amplifyuibuilder.types.codegen_job_generic_data_schema.CodegenJobGenericDataSchema"
    ]
    auto_generate_forms: NotRequired["bool"]
    """<p>Specifies whether to autogenerate forms in the code generation job.</p>"""
    features: NotRequired[
        "capo_amplifyuibuilder.types.codegen_feature_flags.CodegenFeatureFlags"
    ]
    status: NotRequired[
        "capo_amplifyuibuilder.types.codegen_job_status.CodegenJobStatus"
    ]
    """<p>The status of the code generation job.</p>"""
    status_message: NotRequired["str"]
    """<p>The customized status message for the code generation job.</p>"""
    asset: NotRequired["capo_amplifyuibuilder.types.codegen_job_asset.CodegenJobAsset"]
    """<p>The <code>CodegenJobAsset</code> to use for the code generation job.</p>"""
    tags: NotRequired["capo_amplifyuibuilder.types.tags.Tags"]
    """<p>One or more key-value pairs to use when tagging the code generation job.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The time that the code generation job was created.</p>"""
    modified_at: NotRequired["datetime.datetime"]
    """<p>The time that the code generation job was modified.</p>"""
    dependencies: NotRequired[
        "capo_amplifyuibuilder.types.codegen_dependencies.CodegenDependencies"
    ]
    """<p>Lists the dependency packages that may be required for the project code to run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodegenJob) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["appId"] = value["app_id"]
    out["environmentName"] = value["environment_name"]
    if "render_config" in value:
        import capo_amplifyuibuilder.types.codegen_job_render_config

        out["renderConfig"] = (
            capo_amplifyuibuilder.types.codegen_job_render_config.serialize_json(
                value["render_config"]
            )
        )
    if "generic_data_schema" in value:
        import capo_amplifyuibuilder.types.codegen_job_generic_data_schema

        out["genericDataSchema"] = (
            capo_amplifyuibuilder.types.codegen_job_generic_data_schema.serialize_json(
                value["generic_data_schema"]
            )
        )
    if "auto_generate_forms" in value:
        out["autoGenerateForms"] = value["auto_generate_forms"]
    if "features" in value:
        import capo_amplifyuibuilder.types.codegen_feature_flags

        out["features"] = (
            capo_amplifyuibuilder.types.codegen_feature_flags.serialize_json(
                value["features"]
            )
        )
    if "status" in value:
        import capo_amplifyuibuilder.types.codegen_job_status

        out["status"] = capo_amplifyuibuilder.types.codegen_job_status.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "asset" in value:
        import capo_amplifyuibuilder.types.codegen_job_asset

        out["asset"] = capo_amplifyuibuilder.types.codegen_job_asset.serialize_json(
            value["asset"]
        )
    if "tags" in value:
        import capo_amplifyuibuilder.types.tags

        out["tags"] = capo_amplifyuibuilder.types.tags.serialize_json(value["tags"])
    if "created_at" in value:
        import capo_amplifyuibuilder.types._prelude.timestamp

        out["createdAt"] = (
            capo_amplifyuibuilder.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "modified_at" in value:
        import capo_amplifyuibuilder.types._prelude.timestamp

        out["modifiedAt"] = (
            capo_amplifyuibuilder.types._prelude.timestamp.serialize_json(
                value["modified_at"]
            )
        )
    if "dependencies" in value:
        import capo_amplifyuibuilder.types.codegen_dependencies

        out["dependencies"] = (
            capo_amplifyuibuilder.types.codegen_dependencies.serialize_json(
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
        import capo_amplifyuibuilder.types.codegen_job_render_config

        out["render_config"] = (
            capo_amplifyuibuilder.types.codegen_job_render_config.deserialize_json(
                data["renderConfig"]
            )
        )
    if "genericDataSchema" in data:
        import capo_amplifyuibuilder.types.codegen_job_generic_data_schema

        out["generic_data_schema"] = (
            capo_amplifyuibuilder.types.codegen_job_generic_data_schema.deserialize_json(
                data["genericDataSchema"]
            )
        )
    if "autoGenerateForms" in data:
        out["auto_generate_forms"] = data["autoGenerateForms"]
    if "features" in data:
        import capo_amplifyuibuilder.types.codegen_feature_flags

        out["features"] = (
            capo_amplifyuibuilder.types.codegen_feature_flags.deserialize_json(
                data["features"]
            )
        )
    if "status" in data:
        import capo_amplifyuibuilder.types.codegen_job_status

        out["status"] = capo_amplifyuibuilder.types.codegen_job_status.deserialize_json(
            data["status"]
        )
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "asset" in data:
        import capo_amplifyuibuilder.types.codegen_job_asset

        out["asset"] = capo_amplifyuibuilder.types.codegen_job_asset.deserialize_json(
            data["asset"]
        )
    if "tags" in data:
        import capo_amplifyuibuilder.types.tags

        out["tags"] = capo_amplifyuibuilder.types.tags.deserialize_json(data["tags"])
    if "createdAt" in data:
        import capo_amplifyuibuilder.types._prelude.timestamp

        out["created_at"] = (
            capo_amplifyuibuilder.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "modifiedAt" in data:
        import capo_amplifyuibuilder.types._prelude.timestamp

        out["modified_at"] = (
            capo_amplifyuibuilder.types._prelude.timestamp.deserialize_json(
                data["modifiedAt"]
            )
        )
    if "dependencies" in data:
        import capo_amplifyuibuilder.types.codegen_dependencies

        out["dependencies"] = (
            capo_amplifyuibuilder.types.codegen_dependencies.deserialize_json(
                data["dependencies"]
            )
        )
    return out
