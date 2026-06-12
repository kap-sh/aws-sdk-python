"""Generated from Smithy shape ``com.amazonaws.codecommit#ApprovalList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.approval

ApprovalList: TypeAlias = list["aws_sdk_codecommit.types.approval.Approval"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApprovalList) -> list:
    import aws_sdk_codecommit.types.approval

    out: list = []
    for item in value:
        out.append(aws_sdk_codecommit.types.approval.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ApprovalList:
    import aws_sdk_codecommit.types.approval

    out: ApprovalList = []
    for item in data:
        out.append(aws_sdk_codecommit.types.approval.deserialize_aws_json_1_1(item))
    return out
