"""Generated from Smithy shape ``com.amazonaws.rekognition#ProjectAutoUpdate``."""

from typing import Literal, TypeAlias, cast

ProjectAutoUpdate: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectAutoUpdate) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProjectAutoUpdate:
    return cast(ProjectAutoUpdate, data)
