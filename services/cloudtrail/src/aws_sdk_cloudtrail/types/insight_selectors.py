"""Generated from Smithy shape ``com.amazonaws.cloudtrail#InsightSelectors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.insight_selector

InsightSelectors: TypeAlias = list[
    "aws_sdk_cloudtrail.types.insight_selector.InsightSelector"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InsightSelectors) -> list:
    import aws_sdk_cloudtrail.types.insight_selector

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudtrail.types.insight_selector.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InsightSelectors:
    import aws_sdk_cloudtrail.types.insight_selector

    out: InsightSelectors = []
    for item in data:
        out.append(
            aws_sdk_cloudtrail.types.insight_selector.deserialize_aws_json_1_1(item)
        )
    return out
