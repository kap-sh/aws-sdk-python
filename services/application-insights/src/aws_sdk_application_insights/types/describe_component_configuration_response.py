"""Generated from Smithy shape ``com.amazonaws.applicationinsights#DescribeComponentConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.component_configuration
    import aws_sdk_application_insights.types.monitor
    import aws_sdk_application_insights.types.tier


class DescribeComponentConfigurationResponse(TypedDict, closed=True):
    monitor: NotRequired["aws_sdk_application_insights.types.monitor.Monitor"]
    """<p>Indicates whether the application component is monitored.</p>"""
    tier: NotRequired["aws_sdk_application_insights.types.tier.Tier"]
    """<p>The tier of the application component. Supported tiers include <code>DOT_NET_CORE</code>, <code>DOT_NET_WORKER</code>, <code>DOT_NET_WEB</code>, <code>SQL_SERVER</code>, and <code>DEFAULT</code> </p>"""
    component_configuration: NotRequired[
        "aws_sdk_application_insights.types.component_configuration.ComponentConfiguration"
    ]
    """<p>The configuration settings of the component. The value is the escaped JSON of the configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeComponentConfigurationResponse) -> dict:
    out: dict = {}
    if "monitor" in value:
        out["Monitor"] = value["monitor"]
    if "tier" in value:
        import aws_sdk_application_insights.types.tier

        out["Tier"] = aws_sdk_application_insights.types.tier.serialize_aws_json_1_1(
            value["tier"]
        )
    if "component_configuration" in value:
        out["ComponentConfiguration"] = value["component_configuration"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeComponentConfigurationResponse:
    out: DescribeComponentConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "Monitor" in data:
        out["monitor"] = data["Monitor"]
    if "Tier" in data:
        import aws_sdk_application_insights.types.tier

        out["tier"] = aws_sdk_application_insights.types.tier.deserialize_aws_json_1_1(
            data["Tier"]
        )
    if "ComponentConfiguration" in data:
        out["component_configuration"] = data["ComponentConfiguration"]
    return out
