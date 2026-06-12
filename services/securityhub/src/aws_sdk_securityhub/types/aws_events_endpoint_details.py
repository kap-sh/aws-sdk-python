"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEventsEndpointDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_events_endpoint_event_buses_list
    import aws_sdk_securityhub.types.aws_events_endpoint_replication_config_details
    import aws_sdk_securityhub.types.aws_events_endpoint_routing_config_details
    import aws_sdk_securityhub.types.non_empty_string


class AwsEventsEndpointDetails(TypedDict):
    arn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The Amazon Resource Name (ARN) of the endpoint. </p>"""
    description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> A description of the endpoint. </p>"""
    endpoint_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The URL subdomain of the endpoint. For example, if <code>EndpointUrl</code> is <code>https://abcde.veo.endpoints.event.amazonaws.com</code>, then the <code>EndpointId</code> is <code>abcde.veo</code>.</p>"""
    endpoint_url: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The URL of the endpoint.</p>"""
    event_buses: NotRequired[
        "aws_sdk_securityhub.types.aws_events_endpoint_event_buses_list.AwsEventsEndpointEventBusesList"
    ]
    """<p> The event buses being used by the endpoint.</p>"""
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the endpoint.</p>"""
    replication_config: NotRequired[
        "aws_sdk_securityhub.types.aws_events_endpoint_replication_config_details.AwsEventsEndpointReplicationConfigDetails"
    ]
    """<p> Whether event replication was enabled or disabled for this endpoint. The default state is <code>ENABLED</code>, which means you must supply a <code>RoleArn</code>. If you don't have a <code>RoleArn</code> or you don't want event replication enabled, set the state to <code>DISABLED</code>.</p>"""
    role_arn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The ARN of the role used by event replication for the endpoint.</p>"""
    routing_config: NotRequired[
        "aws_sdk_securityhub.types.aws_events_endpoint_routing_config_details.AwsEventsEndpointRoutingConfigDetails"
    ]
    """<p> The routing configuration of the endpoint.</p>"""
    state: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The current state of the endpoint.</p>"""
    state_reason: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The reason the endpoint is in its current state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEventsEndpointDetails) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "endpoint_id" in value:
        out["EndpointId"] = value["endpoint_id"]
    if "endpoint_url" in value:
        out["EndpointUrl"] = value["endpoint_url"]
    if "event_buses" in value:
        import aws_sdk_securityhub.types.aws_events_endpoint_event_buses_list

        out["EventBuses"] = (
            aws_sdk_securityhub.types.aws_events_endpoint_event_buses_list.serialize_json(
                value["event_buses"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "replication_config" in value:
        import aws_sdk_securityhub.types.aws_events_endpoint_replication_config_details

        out["ReplicationConfig"] = (
            aws_sdk_securityhub.types.aws_events_endpoint_replication_config_details.serialize_json(
                value["replication_config"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "routing_config" in value:
        import aws_sdk_securityhub.types.aws_events_endpoint_routing_config_details

        out["RoutingConfig"] = (
            aws_sdk_securityhub.types.aws_events_endpoint_routing_config_details.serialize_json(
                value["routing_config"]
            )
        )
    if "state" in value:
        out["State"] = value["state"]
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    return out


def deserialize_json(data: dict) -> AwsEventsEndpointDetails:
    out: AwsEventsEndpointDetails = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "EndpointId" in data:
        out["endpoint_id"] = data["EndpointId"]
    if "EndpointUrl" in data:
        out["endpoint_url"] = data["EndpointUrl"]
    if "EventBuses" in data:
        import aws_sdk_securityhub.types.aws_events_endpoint_event_buses_list

        out["event_buses"] = (
            aws_sdk_securityhub.types.aws_events_endpoint_event_buses_list.deserialize_json(
                data["EventBuses"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "ReplicationConfig" in data:
        import aws_sdk_securityhub.types.aws_events_endpoint_replication_config_details

        out["replication_config"] = (
            aws_sdk_securityhub.types.aws_events_endpoint_replication_config_details.deserialize_json(
                data["ReplicationConfig"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "RoutingConfig" in data:
        import aws_sdk_securityhub.types.aws_events_endpoint_routing_config_details

        out["routing_config"] = (
            aws_sdk_securityhub.types.aws_events_endpoint_routing_config_details.deserialize_json(
                data["RoutingConfig"]
            )
        )
    if "State" in data:
        out["state"] = data["State"]
    if "StateReason" in data:
        out["state_reason"] = data["StateReason"]
    return out
