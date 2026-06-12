"""Generated from Smithy shape ``com.amazonaws.rekognition#ProjectNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.project_name

ProjectNames: TypeAlias = list["aws_sdk_rekognition.types.project_name.ProjectName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ProjectNames:
    return list(data)
