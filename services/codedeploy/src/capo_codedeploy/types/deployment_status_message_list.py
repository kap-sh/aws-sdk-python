"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentStatusMessageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.error_message

DeploymentStatusMessageList: TypeAlias = list[
    "capo_codedeploy.types.error_message.ErrorMessage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentStatusMessageList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DeploymentStatusMessageList:
    return list(data)
