"""Generated from Smithy shape ``com.amazonaws.securityhub#InsightResultValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.insight_result_value

InsightResultValueList: TypeAlias = list[
    "capo_securityhub.types.insight_result_value.InsightResultValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightResultValueList) -> list:
    import capo_securityhub.types.insight_result_value

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.insight_result_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> InsightResultValueList:
    import capo_securityhub.types.insight_result_value

    out: InsightResultValueList = []
    for item in data:
        out.append(capo_securityhub.types.insight_result_value.deserialize_json(item))
    return out
