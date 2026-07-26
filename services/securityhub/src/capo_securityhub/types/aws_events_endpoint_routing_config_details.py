"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEventsEndpointRoutingConfigDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_events_endpoint_routing_config_failover_config_details


class AwsEventsEndpointRoutingConfigDetails(TypedDict, closed=True):
    failover_config: NotRequired[
        "capo_securityhub.types.aws_events_endpoint_routing_config_failover_config_details.AwsEventsEndpointRoutingConfigFailoverConfigDetails"
    ]
    """<p> The failover configuration for an endpoint. This includes what triggers failover and what happens when it's triggered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEventsEndpointRoutingConfigDetails) -> dict:
    out: dict = {}
    if "failover_config" in value:
        import capo_securityhub.types.aws_events_endpoint_routing_config_failover_config_details

        out["FailoverConfig"] = (
            capo_securityhub.types.aws_events_endpoint_routing_config_failover_config_details.serialize_json(
                value["failover_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsEventsEndpointRoutingConfigDetails:
    out: AwsEventsEndpointRoutingConfigDetails = {}  # type: ignore[typeddict-item]
    if "FailoverConfig" in data:
        import capo_securityhub.types.aws_events_endpoint_routing_config_failover_config_details

        out["failover_config"] = (
            capo_securityhub.types.aws_events_endpoint_routing_config_failover_config_details.deserialize_json(
                data["FailoverConfig"]
            )
        )
    return out
