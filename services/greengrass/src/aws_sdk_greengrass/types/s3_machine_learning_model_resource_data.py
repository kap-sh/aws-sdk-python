"""Generated from Smithy shape ``com.amazonaws.greengrass#S3MachineLearningModelResourceData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string
    import aws_sdk_greengrass.types.resource_download_owner_setting


class S3MachineLearningModelResourceData(TypedDict):
    destination_path: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The absolute local path of the resource inside the Lambda environment."""
    owner_setting: NotRequired[
        "aws_sdk_greengrass.types.resource_download_owner_setting.ResourceDownloadOwnerSetting"
    ]
    s3_uri: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The URI of the source model in an S3 bucket. The model package must be in tar.gz or .zip format."""


# --- restJson1 ser/de ---
def serialize_json(value: S3MachineLearningModelResourceData) -> dict:
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
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    return out


def deserialize_json(data: dict) -> S3MachineLearningModelResourceData:
    out: S3MachineLearningModelResourceData = {}  # type: ignore[typeddict-item]
    if "DestinationPath" in data:
        out["destination_path"] = data["DestinationPath"]
    if "OwnerSetting" in data:
        import aws_sdk_greengrass.types.resource_download_owner_setting

        out["owner_setting"] = (
            aws_sdk_greengrass.types.resource_download_owner_setting.deserialize_json(
                data["OwnerSetting"]
            )
        )
    if "S3Uri" in data:
        out["s3_uri"] = data["S3Uri"]
    return out
