"""Generated from Smithy shape ``com.amazonaws.securityhub#InsightList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.insight

InsightList: TypeAlias = list["capo_securityhub.types.insight.Insight"]


# --- restJson1 ser/de ---
def serialize_json(value: InsightList) -> list:
    import capo_securityhub.types.insight

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.insight.serialize_json(item))
    return out


def deserialize_json(data: list) -> InsightList:
    import capo_securityhub.types.insight

    out: InsightList = []
    for item in data:
        out.append(capo_securityhub.types.insight.deserialize_json(item))
    return out
