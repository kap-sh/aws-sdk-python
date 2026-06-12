"""Generated from Smithy shape ``com.amazonaws.comprehend#FlywheelSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.flywheel_summary

FlywheelSummaryList: TypeAlias = list[
    "aws_sdk_comprehend.types.flywheel_summary.FlywheelSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlywheelSummaryList) -> list:
    import aws_sdk_comprehend.types.flywheel_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehend.types.flywheel_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FlywheelSummaryList:
    import aws_sdk_comprehend.types.flywheel_summary

    out: FlywheelSummaryList = []
    for item in data:
        out.append(
            aws_sdk_comprehend.types.flywheel_summary.deserialize_aws_json_1_1(item)
        )
    return out
