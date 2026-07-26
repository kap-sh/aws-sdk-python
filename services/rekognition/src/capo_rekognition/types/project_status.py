"""Generated from Smithy shape ``com.amazonaws.rekognition#ProjectStatus``."""

from typing import Literal, TypeAlias, cast

ProjectStatus: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "DELETING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProjectStatus:
    return cast(ProjectStatus, data)
