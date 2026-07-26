"""Generated from Smithy shape ``com.amazonaws.eventbridge#CreateEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.endpoint_arn
    import capo_eventbridge.types.endpoint_event_bus_list
    import capo_eventbridge.types.endpoint_name
    import capo_eventbridge.types.endpoint_state
    import capo_eventbridge.types.iam_role_arn
    import capo_eventbridge.types.replication_config
    import capo_eventbridge.types.routing_config


class CreateEndpointResponse(TypedDict, closed=True):
    name: NotRequired["capo_eventbridge.types.endpoint_name.EndpointName"]
    """<p>The name of the endpoint that was created by this request.</p>"""
    arn: NotRequired["capo_eventbridge.types.endpoint_arn.EndpointArn"]
    """<p>The ARN of the endpoint that was created by this request.</p>"""
    routing_config: NotRequired["capo_eventbridge.types.routing_config.RoutingConfig"]
    """<p>The routing configuration defined by this request.</p>"""
    replication_config: NotRequired[
        "capo_eventbridge.types.replication_config.ReplicationConfig"
    ]
    """<p>Whether event replication was enabled or disabled by this request.</p>"""
    event_buses: NotRequired[
        "capo_eventbridge.types.endpoint_event_bus_list.EndpointEventBusList"
    ]
    """<p>The event buses used by this request.</p>"""
    role_arn: NotRequired["capo_eventbridge.types.iam_role_arn.IamRoleArn"]
    """<p>The ARN of the role used by event replication for this request.</p>"""
    state: NotRequired["capo_eventbridge.types.endpoint_state.EndpointState"]
    """<p>The state of the endpoint that was created by this request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEndpointResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "routing_config" in value:
        import capo_eventbridge.types.routing_config

        out["RoutingConfig"] = (
            capo_eventbridge.types.routing_config.serialize_aws_json_1_1(
                value["routing_config"]
            )
        )
    if "replication_config" in value:
        import capo_eventbridge.types.replication_config

        out["ReplicationConfig"] = (
            capo_eventbridge.types.replication_config.serialize_aws_json_1_1(
                value["replication_config"]
            )
        )
    if "event_buses" in value:
        import capo_eventbridge.types.endpoint_event_bus_list

        out["EventBuses"] = (
            capo_eventbridge.types.endpoint_event_bus_list.serialize_aws_json_1_1(
                value["event_buses"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "state" in value:
        import capo_eventbridge.types.endpoint_state

        out["State"] = capo_eventbridge.types.endpoint_state.serialize_aws_json_1_1(
            value["state"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEndpointResponse:
    out: CreateEndpointResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "RoutingConfig" in data:
        import capo_eventbridge.types.routing_config

        out["routing_config"] = (
            capo_eventbridge.types.routing_config.deserialize_aws_json_1_1(
                data["RoutingConfig"]
            )
        )
    if "ReplicationConfig" in data:
        import capo_eventbridge.types.replication_config

        out["replication_config"] = (
            capo_eventbridge.types.replication_config.deserialize_aws_json_1_1(
                data["ReplicationConfig"]
            )
        )
    if "EventBuses" in data:
        import capo_eventbridge.types.endpoint_event_bus_list

        out["event_buses"] = (
            capo_eventbridge.types.endpoint_event_bus_list.deserialize_aws_json_1_1(
                data["EventBuses"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "State" in data:
        import capo_eventbridge.types.endpoint_state

        out["state"] = capo_eventbridge.types.endpoint_state.deserialize_aws_json_1_1(
            data["State"]
        )
    return out
