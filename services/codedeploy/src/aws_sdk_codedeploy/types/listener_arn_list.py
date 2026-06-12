"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListenerArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.listener_arn

ListenerArnList: TypeAlias = list["aws_sdk_codedeploy.types.listener_arn.ListenerArn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListenerArnList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ListenerArnList:
    return list(data)
