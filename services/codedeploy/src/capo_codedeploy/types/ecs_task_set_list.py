"""Generated from Smithy shape ``com.amazonaws.codedeploy#ECSTaskSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.ecs_task_set

ECSTaskSetList: TypeAlias = list["capo_codedeploy.types.ecs_task_set.ECSTaskSet"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ECSTaskSetList) -> list:
    import capo_codedeploy.types.ecs_task_set

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.ecs_task_set.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ECSTaskSetList:
    import capo_codedeploy.types.ecs_task_set

    out: ECSTaskSetList = []
    for item in data:
        out.append(capo_codedeploy.types.ecs_task_set.deserialize_aws_json_1_1(item))
    return out
