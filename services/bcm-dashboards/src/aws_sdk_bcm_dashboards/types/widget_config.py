"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#WidgetConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.display_config
    import aws_sdk_bcm_dashboards.types.query_parameters


class WidgetConfig(TypedDict, closed=True):
    query_parameters: "aws_sdk_bcm_dashboards.types.query_parameters.QueryParameters"
    """<p>The parameters that define what data the widget should retrieve and how it should be filtered or grouped.</p>"""
    display_config: "aws_sdk_bcm_dashboards.types.display_config.DisplayConfig"
    """<p>The configuration that determines how the retrieved data should be visualized in the widget.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WidgetConfig) -> dict:
    out: dict = {}
    import aws_sdk_bcm_dashboards.types.query_parameters

    out["queryParameters"] = (
        aws_sdk_bcm_dashboards.types.query_parameters.serialize_aws_json_1_0(
            value["query_parameters"]
        )
    )
    import aws_sdk_bcm_dashboards.types.display_config

    out["displayConfig"] = (
        aws_sdk_bcm_dashboards.types.display_config.serialize_aws_json_1_0(
            value["display_config"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> WidgetConfig:
    out: WidgetConfig = {}  # type: ignore[typeddict-item]
    if "queryParameters" in data:
        import aws_sdk_bcm_dashboards.types.query_parameters

        out["query_parameters"] = (
            aws_sdk_bcm_dashboards.types.query_parameters.deserialize_aws_json_1_0(
                data["queryParameters"]
            )
        )
    else:
        raise DeserializationError("WidgetConfig.query_parameters required")
    if "displayConfig" in data:
        import aws_sdk_bcm_dashboards.types.display_config

        out["display_config"] = (
            aws_sdk_bcm_dashboards.types.display_config.deserialize_aws_json_1_0(
                data["displayConfig"]
            )
        )
    else:
        raise DeserializationError("WidgetConfig.display_config required")
    return out
