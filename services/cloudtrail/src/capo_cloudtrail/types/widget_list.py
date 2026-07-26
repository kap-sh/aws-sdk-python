"""Generated from Smithy shape ``com.amazonaws.cloudtrail#WidgetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudtrail.types.widget

WidgetList: TypeAlias = list["capo_cloudtrail.types.widget.Widget"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WidgetList) -> list:
    import capo_cloudtrail.types.widget

    out: list = []
    for item in value:
        out.append(capo_cloudtrail.types.widget.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> WidgetList:
    import capo_cloudtrail.types.widget

    out: WidgetList = []
    for item in data:
        out.append(capo_cloudtrail.types.widget.deserialize_aws_json_1_1(item))
    return out
