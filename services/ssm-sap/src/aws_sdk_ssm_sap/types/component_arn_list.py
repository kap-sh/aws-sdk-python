"""Generated from Smithy shape ``com.amazonaws.ssmsap#ComponentArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.ssm_sap_arn

ComponentArnList: TypeAlias = list["aws_sdk_ssm_sap.types.ssm_sap_arn.SsmSapArn"]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> ComponentArnList:
    return list(data)
