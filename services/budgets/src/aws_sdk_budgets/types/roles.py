"""Generated from Smithy shape ``com.amazonaws.budgets#Roles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_budgets.types.role

Roles: TypeAlias = list["aws_sdk_budgets.types.role.Role"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Roles) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Roles:
    return list(data)
