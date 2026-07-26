"""Generated from Smithy shape ``com.amazonaws.opensearch#InsightFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.insight_field

InsightFieldList: TypeAlias = list["capo_opensearch.types.insight_field.InsightField"]


# --- restJson1 ser/de ---
def serialize_json(value: InsightFieldList) -> list:
    import capo_opensearch.types.insight_field

    out: list = []
    for item in value:
        out.append(capo_opensearch.types.insight_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> InsightFieldList:
    import capo_opensearch.types.insight_field

    out: InsightFieldList = []
    for item in data:
        out.append(capo_opensearch.types.insight_field.deserialize_json(item))
    return out
