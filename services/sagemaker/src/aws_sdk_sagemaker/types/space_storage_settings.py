"""Generated from Smithy shape ``com.amazonaws.sagemaker#SpaceStorageSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ebs_storage_settings


class SpaceStorageSettings(TypedDict, closed=True):
    ebs_storage_settings: NotRequired[
        "aws_sdk_sagemaker.types.ebs_storage_settings.EbsStorageSettings"
    ]
    """<p>A collection of EBS storage settings for a space.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SpaceStorageSettings) -> dict:
    out: dict = {}
    if "ebs_storage_settings" in value:
        import aws_sdk_sagemaker.types.ebs_storage_settings

        out["EbsStorageSettings"] = (
            aws_sdk_sagemaker.types.ebs_storage_settings.serialize_aws_json_1_1(
                value["ebs_storage_settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SpaceStorageSettings:
    out: SpaceStorageSettings = {}  # type: ignore[typeddict-item]
    if "EbsStorageSettings" in data:
        import aws_sdk_sagemaker.types.ebs_storage_settings

        out["ebs_storage_settings"] = (
            aws_sdk_sagemaker.types.ebs_storage_settings.deserialize_aws_json_1_1(
                data["EbsStorageSettings"]
            )
        )
    return out
