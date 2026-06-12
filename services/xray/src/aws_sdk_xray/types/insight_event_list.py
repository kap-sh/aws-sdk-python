"""Generated from Smithy shape ``com.amazonaws.xray#InsightEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.insight_event

InsightEventList: TypeAlias = list["aws_sdk_xray.types.insight_event.InsightEvent"]


# --- restJson1 ser/de ---
def serialize_json(value: InsightEventList) -> list:
    import aws_sdk_xray.types.insight_event

    out: list = []
    for item in value:
        out.append(aws_sdk_xray.types.insight_event.serialize_json(item))
    return out


def deserialize_json(data: list) -> InsightEventList:
    import aws_sdk_xray.types.insight_event

    out: InsightEventList = []
    for item in data:
        out.append(aws_sdk_xray.types.insight_event.deserialize_json(item))
    return out
