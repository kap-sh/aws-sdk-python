"""Generated from Smithy shape ``com.amazonaws.cloudhsm#HapgList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.hapg_arn

HapgList: TypeAlias = list["aws_sdk_cloudhsm.types.hapg_arn.HapgArn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HapgList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> HapgList:
    return list(data)
