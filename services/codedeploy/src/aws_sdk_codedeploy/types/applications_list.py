"""Generated from Smithy shape ``com.amazonaws.codedeploy#ApplicationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.application_name

ApplicationsList: TypeAlias = list[
    "aws_sdk_codedeploy.types.application_name.ApplicationName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ApplicationsList:
    return list(data)
