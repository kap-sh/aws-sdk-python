"""Generated from Smithy shape ``com.amazonaws.ssm#ResourcePolicyParameterNamesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string

ResourcePolicyParameterNamesList: TypeAlias = list["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourcePolicyParameterNamesList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResourcePolicyParameterNamesList:
    return list(data)
