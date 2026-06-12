"""Generated from Smithy shape ``com.amazonaws.sesv2#InsightsEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.insights_event

InsightsEvents: TypeAlias = list["aws_sdk_sesv2.types.insights_event.InsightsEvent"]


# --- restJson1 ser/de ---
def serialize_json(value: InsightsEvents) -> list:
    import aws_sdk_sesv2.types.insights_event

    out: list = []
    for item in value:
        out.append(aws_sdk_sesv2.types.insights_event.serialize_json(item))
    return out


def deserialize_json(data: list) -> InsightsEvents:
    import aws_sdk_sesv2.types.insights_event

    out: InsightsEvents = []
    for item in data:
        out.append(aws_sdk_sesv2.types.insights_event.deserialize_json(item))
    return out
