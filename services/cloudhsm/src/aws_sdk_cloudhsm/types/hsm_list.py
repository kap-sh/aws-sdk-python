"""Generated from Smithy shape ``com.amazonaws.cloudhsm#HsmList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.hsm_arn

HsmList: TypeAlias = list["aws_sdk_cloudhsm.types.hsm_arn.HsmArn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HsmList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> HsmList:
    return list(data)
