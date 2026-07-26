"""Generated from Smithy shape ``com.amazonaws.sagemaker#CanvasAppSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.direct_deploy_settings
    import capo_sagemaker.types.emr_serverless_settings
    import capo_sagemaker.types.generative_ai_settings
    import capo_sagemaker.types.identity_provider_o_auth_settings
    import capo_sagemaker.types.kendra_settings
    import capo_sagemaker.types.model_register_settings
    import capo_sagemaker.types.time_series_forecasting_settings
    import capo_sagemaker.types.workspace_settings


class CanvasAppSettings(TypedDict, closed=True):
    time_series_forecasting_settings: NotRequired[
        "capo_sagemaker.types.time_series_forecasting_settings.TimeSeriesForecastingSettings"
    ]
    """<p>Time series forecast settings for the SageMaker Canvas application.</p>"""
    model_register_settings: NotRequired[
        "capo_sagemaker.types.model_register_settings.ModelRegisterSettings"
    ]
    """<p>The model registry settings for the SageMaker Canvas application.</p>"""
    workspace_settings: NotRequired[
        "capo_sagemaker.types.workspace_settings.WorkspaceSettings"
    ]
    """<p>The workspace settings for the SageMaker Canvas application.</p>"""
    identity_provider_o_auth_settings: NotRequired[
        "capo_sagemaker.types.identity_provider_o_auth_settings.IdentityProviderOAuthSettings"
    ]
    """<p>The settings for connecting to an external data source with OAuth.</p>"""
    direct_deploy_settings: NotRequired[
        "capo_sagemaker.types.direct_deploy_settings.DirectDeploySettings"
    ]
    """<p>The model deployment settings for the SageMaker Canvas application.</p>"""
    kendra_settings: NotRequired["capo_sagemaker.types.kendra_settings.KendraSettings"]
    """<p>The settings for document querying.</p>"""
    generative_ai_settings: NotRequired[
        "capo_sagemaker.types.generative_ai_settings.GenerativeAiSettings"
    ]
    """<p>The generative AI settings for the SageMaker Canvas application.</p>"""
    emr_serverless_settings: NotRequired[
        "capo_sagemaker.types.emr_serverless_settings.EmrServerlessSettings"
    ]
    """<p>The settings for running Amazon EMR Serverless data processing jobs in SageMaker Canvas.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CanvasAppSettings) -> dict:
    out: dict = {}
    if "time_series_forecasting_settings" in value:
        import capo_sagemaker.types.time_series_forecasting_settings

        out["TimeSeriesForecastingSettings"] = (
            capo_sagemaker.types.time_series_forecasting_settings.serialize_aws_json_1_1(
                value["time_series_forecasting_settings"]
            )
        )
    if "model_register_settings" in value:
        import capo_sagemaker.types.model_register_settings

        out["ModelRegisterSettings"] = (
            capo_sagemaker.types.model_register_settings.serialize_aws_json_1_1(
                value["model_register_settings"]
            )
        )
    if "workspace_settings" in value:
        import capo_sagemaker.types.workspace_settings

        out["WorkspaceSettings"] = (
            capo_sagemaker.types.workspace_settings.serialize_aws_json_1_1(
                value["workspace_settings"]
            )
        )
    if "identity_provider_o_auth_settings" in value:
        import capo_sagemaker.types.identity_provider_o_auth_settings

        out["IdentityProviderOAuthSettings"] = (
            capo_sagemaker.types.identity_provider_o_auth_settings.serialize_aws_json_1_1(
                value["identity_provider_o_auth_settings"]
            )
        )
    if "direct_deploy_settings" in value:
        import capo_sagemaker.types.direct_deploy_settings

        out["DirectDeploySettings"] = (
            capo_sagemaker.types.direct_deploy_settings.serialize_aws_json_1_1(
                value["direct_deploy_settings"]
            )
        )
    if "kendra_settings" in value:
        import capo_sagemaker.types.kendra_settings

        out["KendraSettings"] = (
            capo_sagemaker.types.kendra_settings.serialize_aws_json_1_1(
                value["kendra_settings"]
            )
        )
    if "generative_ai_settings" in value:
        import capo_sagemaker.types.generative_ai_settings

        out["GenerativeAiSettings"] = (
            capo_sagemaker.types.generative_ai_settings.serialize_aws_json_1_1(
                value["generative_ai_settings"]
            )
        )
    if "emr_serverless_settings" in value:
        import capo_sagemaker.types.emr_serverless_settings

        out["EmrServerlessSettings"] = (
            capo_sagemaker.types.emr_serverless_settings.serialize_aws_json_1_1(
                value["emr_serverless_settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CanvasAppSettings:
    out: CanvasAppSettings = {}  # type: ignore[typeddict-item]
    if "TimeSeriesForecastingSettings" in data:
        import capo_sagemaker.types.time_series_forecasting_settings

        out["time_series_forecasting_settings"] = (
            capo_sagemaker.types.time_series_forecasting_settings.deserialize_aws_json_1_1(
                data["TimeSeriesForecastingSettings"]
            )
        )
    if "ModelRegisterSettings" in data:
        import capo_sagemaker.types.model_register_settings

        out["model_register_settings"] = (
            capo_sagemaker.types.model_register_settings.deserialize_aws_json_1_1(
                data["ModelRegisterSettings"]
            )
        )
    if "WorkspaceSettings" in data:
        import capo_sagemaker.types.workspace_settings

        out["workspace_settings"] = (
            capo_sagemaker.types.workspace_settings.deserialize_aws_json_1_1(
                data["WorkspaceSettings"]
            )
        )
    if "IdentityProviderOAuthSettings" in data:
        import capo_sagemaker.types.identity_provider_o_auth_settings

        out["identity_provider_o_auth_settings"] = (
            capo_sagemaker.types.identity_provider_o_auth_settings.deserialize_aws_json_1_1(
                data["IdentityProviderOAuthSettings"]
            )
        )
    if "DirectDeploySettings" in data:
        import capo_sagemaker.types.direct_deploy_settings

        out["direct_deploy_settings"] = (
            capo_sagemaker.types.direct_deploy_settings.deserialize_aws_json_1_1(
                data["DirectDeploySettings"]
            )
        )
    if "KendraSettings" in data:
        import capo_sagemaker.types.kendra_settings

        out["kendra_settings"] = (
            capo_sagemaker.types.kendra_settings.deserialize_aws_json_1_1(
                data["KendraSettings"]
            )
        )
    if "GenerativeAiSettings" in data:
        import capo_sagemaker.types.generative_ai_settings

        out["generative_ai_settings"] = (
            capo_sagemaker.types.generative_ai_settings.deserialize_aws_json_1_1(
                data["GenerativeAiSettings"]
            )
        )
    if "EmrServerlessSettings" in data:
        import capo_sagemaker.types.emr_serverless_settings

        out["emr_serverless_settings"] = (
            capo_sagemaker.types.emr_serverless_settings.deserialize_aws_json_1_1(
                data["EmrServerlessSettings"]
            )
        )
    return out
