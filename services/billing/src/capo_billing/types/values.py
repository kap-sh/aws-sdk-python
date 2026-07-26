"""Generated from Smithy shape ``com.amazonaws.billing#Values``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.value

Values: TypeAlias = list["capo_billing.types.value.Value"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Values) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> Values:
    return list(data)
