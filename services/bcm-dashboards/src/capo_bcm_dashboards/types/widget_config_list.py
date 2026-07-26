"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#WidgetConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.widget_config

WidgetConfigList: TypeAlias = list[
    "capo_bcm_dashboards.types.widget_config.WidgetConfig"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WidgetConfigList) -> list:
    import capo_bcm_dashboards.types.widget_config

    out: list = []
    for item in value:
        out.append(capo_bcm_dashboards.types.widget_config.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> WidgetConfigList:
    import capo_bcm_dashboards.types.widget_config

    out: WidgetConfigList = []
    for item in data:
        out.append(
            capo_bcm_dashboards.types.widget_config.deserialize_aws_json_1_0(item)
        )
    return out
