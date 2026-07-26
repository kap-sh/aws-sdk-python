"""Generated from Smithy shape ``com.amazonaws.eks#InsightStatusValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.insight_status_value

InsightStatusValueList: TypeAlias = list[
    "capo_eks.types.insight_status_value.InsightStatusValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightStatusValueList) -> list:
    import capo_eks.types.insight_status_value

    out: list = []
    for item in value:
        out.append(capo_eks.types.insight_status_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> InsightStatusValueList:
    import capo_eks.types.insight_status_value

    out: InsightStatusValueList = []
    for item in data:
        out.append(capo_eks.types.insight_status_value.deserialize_json(item))
    return out
