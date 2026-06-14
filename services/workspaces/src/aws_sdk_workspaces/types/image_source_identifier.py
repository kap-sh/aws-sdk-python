"""Generated from Smithy shape ``com.amazonaws.workspaces#ImageSourceIdentifier``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_workspaces.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.ec2_image_id
    import aws_sdk_workspaces.types.ec2_import_task_id
    import aws_sdk_workspaces.types.image_build_version_arn


class _ImageSourceIdentifier_Ec2ImportTaskId(TypedDict):
    Ec2ImportTaskId: "aws_sdk_workspaces.types.ec2_import_task_id.Ec2ImportTaskId"


class _ImageSourceIdentifier_ImageBuildVersionArn(TypedDict):
    ImageBuildVersionArn: (
        "aws_sdk_workspaces.types.image_build_version_arn.ImageBuildVersionArn"
    )


class _ImageSourceIdentifier_Ec2ImageId(TypedDict):
    Ec2ImageId: "aws_sdk_workspaces.types.ec2_image_id.Ec2ImageId"


ImageSourceIdentifier: TypeAlias = (
    _ImageSourceIdentifier_Ec2ImportTaskId
    | _ImageSourceIdentifier_ImageBuildVersionArn
    | _ImageSourceIdentifier_Ec2ImageId
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageSourceIdentifier) -> dict:
    if "Ec2ImportTaskId" in value:
        return {"Ec2ImportTaskId": value["Ec2ImportTaskId"]}
    elif "ImageBuildVersionArn" in value:
        return {"ImageBuildVersionArn": value["ImageBuildVersionArn"]}
    elif "Ec2ImageId" in value:
        return {"Ec2ImageId": value["Ec2ImageId"]}
    else:
        raise SerializationError("ImageSourceIdentifier: no variant present")


def deserialize_aws_json_1_1(data: dict) -> ImageSourceIdentifier:
    if "Ec2ImportTaskId" in data:
        return {"Ec2ImportTaskId": data["Ec2ImportTaskId"]}
    elif "ImageBuildVersionArn" in data:
        return {"ImageBuildVersionArn": data["ImageBuildVersionArn"]}
    elif "Ec2ImageId" in data:
        return {"Ec2ImageId": data["Ec2ImageId"]}
    else:
        raise DeserializationError("ImageSourceIdentifier: no recognized variant key")
