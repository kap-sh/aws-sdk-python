"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#BatchGetPolicyErrorCode``."""

from typing import Literal, TypeAlias, cast

BatchGetPolicyErrorCode: TypeAlias = Literal[
    "POLICY_STORE_NOT_FOUND",
    "POLICY_NOT_FOUND",
    "POLICY_STORE_ALIAS_NOT_FOUND",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetPolicyErrorCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BatchGetPolicyErrorCode:
    return cast(BatchGetPolicyErrorCode, data)
