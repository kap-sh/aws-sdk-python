"""Generated from Smithy shape ``com.amazonaws.budgets#Values``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_budgets.types.value

Values: TypeAlias = list["capo_budgets.types.value.Value"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Values) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Values:
    return list(data)
