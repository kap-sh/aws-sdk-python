"""Generated from Smithy shape ``com.amazonaws.kendra#ExperienceStatus``."""

from typing import Literal, TypeAlias, cast

ExperienceStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExperienceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExperienceStatus:
    return cast(ExperienceStatus, data)
