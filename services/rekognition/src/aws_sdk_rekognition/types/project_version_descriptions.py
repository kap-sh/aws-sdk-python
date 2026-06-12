"""Generated from Smithy shape ``com.amazonaws.rekognition#ProjectVersionDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.project_version_description

ProjectVersionDescriptions: TypeAlias = list[
    "aws_sdk_rekognition.types.project_version_description.ProjectVersionDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectVersionDescriptions) -> list:
    import aws_sdk_rekognition.types.project_version_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_rekognition.types.project_version_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProjectVersionDescriptions:
    import aws_sdk_rekognition.types.project_version_description

    out: ProjectVersionDescriptions = []
    for item in data:
        out.append(
            aws_sdk_rekognition.types.project_version_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
