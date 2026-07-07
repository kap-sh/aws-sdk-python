"""Generated from Smithy shape ``com.amazonaws.eventbridge#UpdateEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.endpoint_description
    import aws_sdk_eventbridge.types.endpoint_event_bus_list
    import aws_sdk_eventbridge.types.endpoint_name
    import aws_sdk_eventbridge.types.iam_role_arn
    import aws_sdk_eventbridge.types.replication_config
    import aws_sdk_eventbridge.types.routing_config


class UpdateEndpointRequest(TypedDict, closed=True):
    name: "aws_sdk_eventbridge.types.endpoint_name.EndpointName"
    """<p>The name of the endpoint you want to update.</p>"""
    description: NotRequired[
        "aws_sdk_eventbridge.types.endpoint_description.EndpointDescription"
    ]
    """<p>A description for the endpoint.</p>"""
    routing_config: NotRequired[
        "aws_sdk_eventbridge.types.routing_config.RoutingConfig"
    ]
    """<p>Configure the routing policy, including the health check and secondary Region.</p>"""
    replication_config: NotRequired[
        "aws_sdk_eventbridge.types.replication_config.ReplicationConfig"
    ]
    """<p>Whether event replication was enabled or disabled by this request.</p>"""
    event_buses: NotRequired[
        "aws_sdk_eventbridge.types.endpoint_event_bus_list.EndpointEventBusList"
    ]
    """<p>Define event buses used for replication.</p>"""
    role_arn: NotRequired["aws_sdk_eventbridge.types.iam_role_arn.IamRoleArn"]
    """<p>The ARN of the role used by event replication for this request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateEndpointRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "routing_config" in value:
        import aws_sdk_eventbridge.types.routing_config

        out["RoutingConfig"] = (
            aws_sdk_eventbridge.types.routing_config.serialize_aws_json_1_1(
                value["routing_config"]
            )
        )
    if "replication_config" in value:
        import aws_sdk_eventbridge.types.replication_config

        out["ReplicationConfig"] = (
            aws_sdk_eventbridge.types.replication_config.serialize_aws_json_1_1(
                value["replication_config"]
            )
        )
    if "event_buses" in value:
        import aws_sdk_eventbridge.types.endpoint_event_bus_list

        out["EventBuses"] = (
            aws_sdk_eventbridge.types.endpoint_event_bus_list.serialize_aws_json_1_1(
                value["event_buses"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateEndpointRequest:
    out: UpdateEndpointRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateEndpointRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "RoutingConfig" in data:
        import aws_sdk_eventbridge.types.routing_config

        out["routing_config"] = (
            aws_sdk_eventbridge.types.routing_config.deserialize_aws_json_1_1(
                data["RoutingConfig"]
            )
        )
    if "ReplicationConfig" in data:
        import aws_sdk_eventbridge.types.replication_config

        out["replication_config"] = (
            aws_sdk_eventbridge.types.replication_config.deserialize_aws_json_1_1(
                data["ReplicationConfig"]
            )
        )
    if "EventBuses" in data:
        import aws_sdk_eventbridge.types.endpoint_event_bus_list

        out["event_buses"] = (
            aws_sdk_eventbridge.types.endpoint_event_bus_list.deserialize_aws_json_1_1(
                data["EventBuses"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    return out
