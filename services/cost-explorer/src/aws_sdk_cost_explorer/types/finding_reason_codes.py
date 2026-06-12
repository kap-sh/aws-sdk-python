"""Generated from Smithy shape ``com.amazonaws.costexplorer#FindingReasonCodes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.finding_reason_code

FindingReasonCodes: TypeAlias = list[
    "aws_sdk_cost_explorer.types.finding_reason_code.FindingReasonCode"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FindingReasonCodes) -> list:
    import aws_sdk_cost_explorer.types.finding_reason_code

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_explorer.types.finding_reason_code.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FindingReasonCodes:
    import aws_sdk_cost_explorer.types.finding_reason_code

    out: FindingReasonCodes = []
    for item in data:
        out.append(
            aws_sdk_cost_explorer.types.finding_reason_code.deserialize_aws_json_1_1(
                item
            )
        )
    return out
