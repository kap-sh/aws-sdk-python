"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEventsEndpointRoutingConfigFailoverConfigDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_events_endpoint_routing_config_failover_config_primary_details
    import aws_sdk_securityhub.types.aws_events_endpoint_routing_config_failover_config_secondary_details


class AwsEventsEndpointRoutingConfigFailoverConfigDetails(TypedDict):
    primary: NotRequired[
        "aws_sdk_securityhub.types.aws_events_endpoint_routing_config_failover_config_primary_details.AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetails"
    ]
    """<p> The main Region of the endpoint.</p>"""
    secondary: NotRequired[
        "aws_sdk_securityhub.types.aws_events_endpoint_routing_config_failover_config_secondary_details.AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetails"
    ]
    """<p> The Region that events are routed to when failover is triggered or event replication is enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEventsEndpointRoutingConfigFailoverConfigDetails) -> dict:
    out: dict = {}
    if "primary" in value:
        import aws_sdk_securityhub.types.aws_events_endpoint_routing_config_failover_config_primary_details

        out["Primary"] = (
            aws_sdk_securityhub.types.aws_events_endpoint_routing_config_failover_config_primary_details.serialize_json(
                value["primary"]
            )
        )
    if "secondary" in value:
        import aws_sdk_securityhub.types.aws_events_endpoint_routing_config_failover_config_secondary_details

        out["Secondary"] = (
            aws_sdk_securityhub.types.aws_events_endpoint_routing_config_failover_config_secondary_details.serialize_json(
                value["secondary"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsEventsEndpointRoutingConfigFailoverConfigDetails:
    out: AwsEventsEndpointRoutingConfigFailoverConfigDetails = {}  # type: ignore[typeddict-item]
    if "Primary" in data:
        import aws_sdk_securityhub.types.aws_events_endpoint_routing_config_failover_config_primary_details

        out["primary"] = (
            aws_sdk_securityhub.types.aws_events_endpoint_routing_config_failover_config_primary_details.deserialize_json(
                data["Primary"]
            )
        )
    if "Secondary" in data:
        import aws_sdk_securityhub.types.aws_events_endpoint_routing_config_failover_config_secondary_details

        out["secondary"] = (
            aws_sdk_securityhub.types.aws_events_endpoint_routing_config_failover_config_secondary_details.deserialize_json(
                data["Secondary"]
            )
        )
    return out
