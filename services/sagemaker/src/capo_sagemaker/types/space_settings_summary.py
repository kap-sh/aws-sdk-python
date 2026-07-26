"""Generated from Smithy shape ``com.amazonaws.sagemaker#SpaceSettingsSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.app_type
    import capo_sagemaker.types.feature_status
    import capo_sagemaker.types.space_storage_settings


class SpaceSettingsSummary(TypedDict, closed=True):
    app_type: NotRequired["capo_sagemaker.types.app_type.AppType"]
    """<p>The type of app created within the space.</p>"""
    remote_access: NotRequired["capo_sagemaker.types.feature_status.FeatureStatus"]
    """<p>A setting that enables or disables remote access for a SageMaker space. When enabled, this allows you to connect to the remote space from your local IDE.</p>"""
    space_storage_settings: NotRequired[
        "capo_sagemaker.types.space_storage_settings.SpaceStorageSettings"
    ]
    """<p>The storage settings for a space.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SpaceSettingsSummary) -> dict:
    out: dict = {}
    if "app_type" in value:
        import capo_sagemaker.types.app_type

        out["AppType"] = capo_sagemaker.types.app_type.serialize_aws_json_1_1(
            value["app_type"]
        )
    if "remote_access" in value:
        import capo_sagemaker.types.feature_status

        out["RemoteAccess"] = (
            capo_sagemaker.types.feature_status.serialize_aws_json_1_1(
                value["remote_access"]
            )
        )
    if "space_storage_settings" in value:
        import capo_sagemaker.types.space_storage_settings

        out["SpaceStorageSettings"] = (
            capo_sagemaker.types.space_storage_settings.serialize_aws_json_1_1(
                value["space_storage_settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SpaceSettingsSummary:
    out: SpaceSettingsSummary = {}  # type: ignore[typeddict-item]
    if "AppType" in data:
        import capo_sagemaker.types.app_type

        out["app_type"] = capo_sagemaker.types.app_type.deserialize_aws_json_1_1(
            data["AppType"]
        )
    if "RemoteAccess" in data:
        import capo_sagemaker.types.feature_status

        out["remote_access"] = (
            capo_sagemaker.types.feature_status.deserialize_aws_json_1_1(
                data["RemoteAccess"]
            )
        )
    if "SpaceStorageSettings" in data:
        import capo_sagemaker.types.space_storage_settings

        out["space_storage_settings"] = (
            capo_sagemaker.types.space_storage_settings.deserialize_aws_json_1_1(
                data["SpaceStorageSettings"]
            )
        )
    return out
