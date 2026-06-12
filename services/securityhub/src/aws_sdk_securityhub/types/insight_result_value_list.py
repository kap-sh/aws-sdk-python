"""Generated from Smithy shape ``com.amazonaws.securityhub#InsightResultValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.insight_result_value

InsightResultValueList: TypeAlias = list[
    "aws_sdk_securityhub.types.insight_result_value.InsightResultValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightResultValueList) -> list:
    import aws_sdk_securityhub.types.insight_result_value

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.insight_result_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> InsightResultValueList:
    import aws_sdk_securityhub.types.insight_result_value

    out: InsightResultValueList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.insight_result_value.deserialize_json(item)
        )
    return out
