"""Generated from Smithy shape ``com.amazonaws.fms#CustomerPolicyScopeIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.customer_policy_scope_id

CustomerPolicyScopeIdList: TypeAlias = list[
    "aws_sdk_fms.types.customer_policy_scope_id.CustomerPolicyScopeId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomerPolicyScopeIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CustomerPolicyScopeIdList:
    return list(data)
