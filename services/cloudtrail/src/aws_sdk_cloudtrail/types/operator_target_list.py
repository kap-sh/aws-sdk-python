"""Generated from Smithy shape ``com.amazonaws.cloudtrail#OperatorTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.operator_target_list_member

OperatorTargetList: TypeAlias = list[
    "aws_sdk_cloudtrail.types.operator_target_list_member.OperatorTargetListMember"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperatorTargetList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OperatorTargetList:
    return list(data)
