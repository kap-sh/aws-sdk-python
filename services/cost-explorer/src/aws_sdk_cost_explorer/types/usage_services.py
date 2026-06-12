"""Generated from Smithy shape ``com.amazonaws.costexplorer#UsageServices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generic_string

UsageServices: TypeAlias = list[
    "aws_sdk_cost_explorer.types.generic_string.GenericString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsageServices) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> UsageServices:
    return list(data)
