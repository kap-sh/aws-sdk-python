"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemOpsDataKeysList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string

OpsItemOpsDataKeysList: TypeAlias = list["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemOpsDataKeysList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OpsItemOpsDataKeysList:
    return list(data)
