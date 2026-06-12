"""Generated from Smithy shape ``com.amazonaws.rekognition#ProjectPolicies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.project_policy

ProjectPolicies: TypeAlias = list[
    "aws_sdk_rekognition.types.project_policy.ProjectPolicy"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectPolicies) -> list:
    import aws_sdk_rekognition.types.project_policy

    out: list = []
    for item in value:
        out.append(
            aws_sdk_rekognition.types.project_policy.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProjectPolicies:
    import aws_sdk_rekognition.types.project_policy

    out: ProjectPolicies = []
    for item in data:
        out.append(
            aws_sdk_rekognition.types.project_policy.deserialize_aws_json_1_1(item)
        )
    return out
