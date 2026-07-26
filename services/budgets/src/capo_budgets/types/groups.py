"""Generated from Smithy shape ``com.amazonaws.budgets#Groups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_budgets.types.group

Groups: TypeAlias = list["capo_budgets.types.group.Group"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Groups) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Groups:
    return list(data)
