"""Generated from Smithy shape ``com.amazonaws.transfer#SecurityPolicyOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transfer.types.security_policy_option

SecurityPolicyOptions: TypeAlias = list[
    "capo_transfer.types.security_policy_option.SecurityPolicyOption"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityPolicyOptions) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SecurityPolicyOptions:
    return list(data)
