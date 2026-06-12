"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#AccountAggregations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.finding_aggregation_account_details

AccountAggregations: TypeAlias = list[
    "aws_sdk_accessanalyzer.types.finding_aggregation_account_details.FindingAggregationAccountDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountAggregations) -> list:
    import aws_sdk_accessanalyzer.types.finding_aggregation_account_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_accessanalyzer.types.finding_aggregation_account_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AccountAggregations:
    import aws_sdk_accessanalyzer.types.finding_aggregation_account_details

    out: AccountAggregations = []
    for item in data:
        out.append(
            aws_sdk_accessanalyzer.types.finding_aggregation_account_details.deserialize_json(
                item
            )
        )
    return out
