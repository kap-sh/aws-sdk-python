"""Generated from Smithy shape ``com.amazonaws.pi#InsightList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pi.types.insight

InsightList: TypeAlias = list["aws_sdk_pi.types.insight.Insight"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InsightList) -> list:
    import aws_sdk_pi.types.insight

    out: list = []
    for item in value:
        out.append(aws_sdk_pi.types.insight.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InsightList:
    import aws_sdk_pi.types.insight

    out: InsightList = []
    for item in data:
        out.append(aws_sdk_pi.types.insight.deserialize_aws_json_1_1(item))
    return out
