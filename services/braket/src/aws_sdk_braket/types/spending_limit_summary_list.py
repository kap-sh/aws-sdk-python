"""Generated from Smithy shape ``com.amazonaws.braket#SpendingLimitSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_braket.types.spending_limit_summary

SpendingLimitSummaryList: TypeAlias = list[
    "aws_sdk_braket.types.spending_limit_summary.SpendingLimitSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SpendingLimitSummaryList) -> list:
    import aws_sdk_braket.types.spending_limit_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_braket.types.spending_limit_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> SpendingLimitSummaryList:
    import aws_sdk_braket.types.spending_limit_summary

    out: SpendingLimitSummaryList = []
    for item in data:
        out.append(aws_sdk_braket.types.spending_limit_summary.deserialize_json(item))
    return out
