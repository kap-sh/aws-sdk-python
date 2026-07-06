"""Generated from Smithy shape ``com.amazonaws.greengrass#SageMakerMachineLearningModelResourceData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string
    import aws_sdk_greengrass.types.resource_download_owner_setting


class SageMakerMachineLearningModelResourceData(TypedDict, closed=True):
    destination_path: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The absolute local path of the resource inside the Lambda environment."""
    owner_setting: NotRequired[
        "aws_sdk_greengrass.types.resource_download_owner_setting.ResourceDownloadOwnerSetting"
    ]
    sage_maker_job_arn: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ARN of the Amazon SageMaker training job that represents the source model."""


# --- restJson1 ser/de ---
def serialize_json(value: SageMakerMachineLearningModelResourceData) -> dict:
    out: dict = {}
    if "destination_path" in value:
        out["DestinationPath"] = value["destination_path"]
    if "owner_setting" in value:
        import aws_sdk_greengrass.types.resource_download_owner_setting

        out["OwnerSetting"] = (
            aws_sdk_greengrass.types.resource_download_owner_setting.serialize_json(
                value["owner_setting"]
            )
        )
    if "sage_maker_job_arn" in value:
        out["SageMakerJobArn"] = value["sage_maker_job_arn"]
    return out


def deserialize_json(data: dict) -> SageMakerMachineLearningModelResourceData:
    out: SageMakerMachineLearningModelResourceData = {}  # type: ignore[typeddict-item]
    if "DestinationPath" in data:
        out["destination_path"] = data["DestinationPath"]
    if "OwnerSetting" in data:
        import aws_sdk_greengrass.types.resource_download_owner_setting

        out["owner_setting"] = (
            aws_sdk_greengrass.types.resource_download_owner_setting.deserialize_json(
                data["OwnerSetting"]
            )
        )
    if "SageMakerJobArn" in data:
        out["sage_maker_job_arn"] = data["SageMakerJobArn"]
    return out
