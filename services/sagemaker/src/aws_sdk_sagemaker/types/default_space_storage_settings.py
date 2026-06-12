"""Generated from Smithy shape ``com.amazonaws.sagemaker#DefaultSpaceStorageSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.default_ebs_storage_settings


class DefaultSpaceStorageSettings(TypedDict):
    default_ebs_storage_settings: NotRequired[
        "aws_sdk_sagemaker.types.default_ebs_storage_settings.DefaultEbsStorageSettings"
    ]
    """<p>The default EBS storage settings for a space.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DefaultSpaceStorageSettings) -> dict:
    out: dict = {}
    if "default_ebs_storage_settings" in value:
        import aws_sdk_sagemaker.types.default_ebs_storage_settings

        out["DefaultEbsStorageSettings"] = (
            aws_sdk_sagemaker.types.default_ebs_storage_settings.serialize_aws_json_1_1(
                value["default_ebs_storage_settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DefaultSpaceStorageSettings:
    out: DefaultSpaceStorageSettings = {}  # type: ignore[typeddict-item]
    if "DefaultEbsStorageSettings" in data:
        import aws_sdk_sagemaker.types.default_ebs_storage_settings

        out["default_ebs_storage_settings"] = (
            aws_sdk_sagemaker.types.default_ebs_storage_settings.deserialize_aws_json_1_1(
                data["DefaultEbsStorageSettings"]
            )
        )
    return out
