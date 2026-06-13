"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#SummaryDimensions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.summary_dimension

SummaryDimensions: TypeAlias = list[
    "aws_sdk_compute_optimizer_automation.types.summary_dimension.SummaryDimension"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SummaryDimensions) -> list:
    import aws_sdk_compute_optimizer_automation.types.summary_dimension

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer_automation.types.summary_dimension.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SummaryDimensions:
    import aws_sdk_compute_optimizer_automation.types.summary_dimension

    out: SummaryDimensions = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer_automation.types.summary_dimension.deserialize_aws_json_1_0(
                item
            )
        )
    return out
