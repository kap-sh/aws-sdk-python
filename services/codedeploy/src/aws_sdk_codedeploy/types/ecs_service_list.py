"""Generated from Smithy shape ``com.amazonaws.codedeploy#ECSServiceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.ecs_service

ECSServiceList: TypeAlias = list["aws_sdk_codedeploy.types.ecs_service.ECSService"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ECSServiceList) -> list:
    import aws_sdk_codedeploy.types.ecs_service

    out: list = []
    for item in value:
        out.append(aws_sdk_codedeploy.types.ecs_service.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ECSServiceList:
    import aws_sdk_codedeploy.types.ecs_service

    out: ECSServiceList = []
    for item in data:
        out.append(aws_sdk_codedeploy.types.ecs_service.deserialize_aws_json_1_1(item))
    return out
