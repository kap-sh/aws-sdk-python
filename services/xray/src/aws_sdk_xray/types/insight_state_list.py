"""Generated from Smithy shape ``com.amazonaws.xray#InsightStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.insight_state

InsightStateList: TypeAlias = list["aws_sdk_xray.types.insight_state.InsightState"]


# --- restJson1 ser/de ---
def serialize_json(value: InsightStateList) -> list:
    import aws_sdk_xray.types.insight_state

    out: list = []
    for item in value:
        out.append(aws_sdk_xray.types.insight_state.serialize_json(item))
    return out


def deserialize_json(data: list) -> InsightStateList:
    import aws_sdk_xray.types.insight_state

    out: InsightStateList = []
    for item in data:
        out.append(aws_sdk_xray.types.insight_state.deserialize_json(item))
    return out
