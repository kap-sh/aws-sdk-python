"""Generated from Smithy shape ``com.amazonaws.ssmsap#ApplicationArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_sap.types.ssm_sap_arn

ApplicationArnList: TypeAlias = list["capo_ssm_sap.types.ssm_sap_arn.SsmSapArn"]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> ApplicationArnList:
    return list(data)
