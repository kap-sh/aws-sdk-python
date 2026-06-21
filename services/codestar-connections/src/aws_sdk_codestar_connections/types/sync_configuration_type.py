"""Generated from Smithy shape ``com.amazonaws.codestarconnections#SyncConfigurationType``."""

from typing import Literal, TypeAlias, cast

SyncConfigurationType: TypeAlias = Literal["CFN_STACK_SYNC",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SyncConfigurationType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SyncConfigurationType:
    return cast(SyncConfigurationType, data)
