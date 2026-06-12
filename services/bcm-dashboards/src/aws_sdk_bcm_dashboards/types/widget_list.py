"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#WidgetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.widget

WidgetList: TypeAlias = list["aws_sdk_bcm_dashboards.types.widget.Widget"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WidgetList) -> list:
    import aws_sdk_bcm_dashboards.types.widget

    out: list = []
    for item in value:
        out.append(aws_sdk_bcm_dashboards.types.widget.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> WidgetList:
    import aws_sdk_bcm_dashboards.types.widget

    out: WidgetList = []
    for item in data:
        out.append(aws_sdk_bcm_dashboards.types.widget.deserialize_aws_json_1_0(item))
    return out
