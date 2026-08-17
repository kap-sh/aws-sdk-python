"""Generated from Smithy shape ``com.amazonaws.lambda#CapacityProviderSecurityGroupIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.security_group_id

CapacityProviderSecurityGroupIds: TypeAlias = list[
    "capo_lambda.types.security_group_id.SecurityGroupId"
]


# --- restJson1 ser/de ---
def serialize_json(value: CapacityProviderSecurityGroupIds) -> list:
    return list(value)


def deserialize_json(data: list) -> CapacityProviderSecurityGroupIds:
    return [item for item in data if item is not None]
