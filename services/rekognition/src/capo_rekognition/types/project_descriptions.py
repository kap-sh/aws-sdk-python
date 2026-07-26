"""Generated from Smithy shape ``com.amazonaws.rekognition#ProjectDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.project_description

ProjectDescriptions: TypeAlias = list[
    "capo_rekognition.types.project_description.ProjectDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectDescriptions) -> list:
    import capo_rekognition.types.project_description

    out: list = []
    for item in value:
        out.append(
            capo_rekognition.types.project_description.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProjectDescriptions:
    import capo_rekognition.types.project_description

    out: ProjectDescriptions = []
    for item in data:
        out.append(
            capo_rekognition.types.project_description.deserialize_aws_json_1_1(item)
        )
    return out
