"""Generated from Smithy shape ``com.amazonaws.budgets#Users``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_budgets.types.user

Users: TypeAlias = list["capo_budgets.types.user.User"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Users) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Users:
    return list(data)
