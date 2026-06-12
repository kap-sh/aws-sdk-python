"""Generated from Smithy shape ``com.amazonaws.sagemaker#StudioLifecycleConfigDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.studio_lifecycle_config_app_type
    import aws_sdk_sagemaker.types.studio_lifecycle_config_arn
    import aws_sdk_sagemaker.types.studio_lifecycle_config_name
    import aws_sdk_sagemaker.types.timestamp


class StudioLifecycleConfigDetails(TypedDict):
    studio_lifecycle_config_arn: NotRequired[
        "aws_sdk_sagemaker.types.studio_lifecycle_config_arn.StudioLifecycleConfigArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the Lifecycle Configuration.</p>"""
    studio_lifecycle_config_name: NotRequired[
        "aws_sdk_sagemaker.types.studio_lifecycle_config_name.StudioLifecycleConfigName"
    ]
    """<p>The name of the Amazon SageMaker AI Studio Lifecycle Configuration.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The creation time of the Amazon SageMaker AI Studio Lifecycle Configuration.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>This value is equivalent to CreationTime because Amazon SageMaker AI Studio Lifecycle Configurations are immutable.</p>"""
    studio_lifecycle_config_app_type: NotRequired[
        "aws_sdk_sagemaker.types.studio_lifecycle_config_app_type.StudioLifecycleConfigAppType"
    ]
    """<p>The App type to which the Lifecycle Configuration is attached.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StudioLifecycleConfigDetails) -> dict:
    out: dict = {}
    if "studio_lifecycle_config_arn" in value:
        out["StudioLifecycleConfigArn"] = value["studio_lifecycle_config_arn"]
    if "studio_lifecycle_config_name" in value:
        out["StudioLifecycleConfigName"] = value["studio_lifecycle_config_name"]
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "studio_lifecycle_config_app_type" in value:
        import aws_sdk_sagemaker.types.studio_lifecycle_config_app_type

        out["StudioLifecycleConfigAppType"] = (
            aws_sdk_sagemaker.types.studio_lifecycle_config_app_type.serialize_aws_json_1_1(
                value["studio_lifecycle_config_app_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StudioLifecycleConfigDetails:
    out: StudioLifecycleConfigDetails = {}  # type: ignore[typeddict-item]
    if "StudioLifecycleConfigArn" in data:
        out["studio_lifecycle_config_arn"] = data["StudioLifecycleConfigArn"]
    if "StudioLifecycleConfigName" in data:
        out["studio_lifecycle_config_name"] = data["StudioLifecycleConfigName"]
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "StudioLifecycleConfigAppType" in data:
        import aws_sdk_sagemaker.types.studio_lifecycle_config_app_type

        out["studio_lifecycle_config_app_type"] = (
            aws_sdk_sagemaker.types.studio_lifecycle_config_app_type.deserialize_aws_json_1_1(
                data["StudioLifecycleConfigAppType"]
            )
        )
    return out
