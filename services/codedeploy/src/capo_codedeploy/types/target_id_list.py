"""Generated from Smithy shape ``com.amazonaws.codedeploy#TargetIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.target_id

TargetIdList: TypeAlias = list["capo_codedeploy.types.target_id.TargetId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TargetIdList:
    return list(data)
