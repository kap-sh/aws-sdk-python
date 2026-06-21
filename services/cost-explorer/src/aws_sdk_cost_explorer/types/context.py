"""Generated from Smithy shape ``com.amazonaws.costexplorer#Context``."""

from typing import Literal, TypeAlias, cast

Context: TypeAlias = Literal[
    "COST_AND_USAGE",
    "RESERVATIONS",
    "SAVINGS_PLANS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Context) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Context:
    return cast(Context, data)
