"""Generated from Smithy shape ``com.amazonaws.eventbridge#Endpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.endpoint_arn
    import aws_sdk_eventbridge.types.endpoint_description
    import aws_sdk_eventbridge.types.endpoint_event_bus_list
    import aws_sdk_eventbridge.types.endpoint_id
    import aws_sdk_eventbridge.types.endpoint_name
    import aws_sdk_eventbridge.types.endpoint_state
    import aws_sdk_eventbridge.types.endpoint_state_reason
    import aws_sdk_eventbridge.types.endpoint_url
    import aws_sdk_eventbridge.types.iam_role_arn
    import aws_sdk_eventbridge.types.replication_config
    import aws_sdk_eventbridge.types.routing_config
    import aws_sdk_eventbridge.types.timestamp


class Endpoint(TypedDict, closed=True):
    name: NotRequired["aws_sdk_eventbridge.types.endpoint_name.EndpointName"]
    """<p>The name of the endpoint.</p>"""
    description: NotRequired[
        "aws_sdk_eventbridge.types.endpoint_description.EndpointDescription"
    ]
    """<p>A description for the endpoint.</p>"""
    arn: NotRequired["aws_sdk_eventbridge.types.endpoint_arn.EndpointArn"]
    """<p>The ARN of the endpoint.</p>"""
    routing_config: NotRequired[
        "aws_sdk_eventbridge.types.routing_config.RoutingConfig"
    ]
    """<p>The routing configuration of the endpoint.</p>"""
    replication_config: NotRequired[
        "aws_sdk_eventbridge.types.replication_config.ReplicationConfig"
    ]
    """<p>Whether event replication was enabled or disabled for this endpoint. The default state is <code>ENABLED</code> which means you must supply a <code>RoleArn</code>. If you don't have a <code>RoleArn</code> or you don't want event replication enabled, set the state to <code>DISABLED</code>.</p>"""
    event_buses: NotRequired[
        "aws_sdk_eventbridge.types.endpoint_event_bus_list.EndpointEventBusList"
    ]
    """<p>The event buses being used by the endpoint.</p>"""
    role_arn: NotRequired["aws_sdk_eventbridge.types.iam_role_arn.IamRoleArn"]
    """<p>The ARN of the role used by event replication for the endpoint.</p>"""
    endpoint_id: NotRequired["aws_sdk_eventbridge.types.endpoint_id.EndpointId"]
    """<p>The URL subdomain of the endpoint. For example, if the URL for Endpoint is https://abcde.veo.endpoints.event.amazonaws.com, then the EndpointId is <code>abcde.veo</code>.</p>"""
    endpoint_url: NotRequired["aws_sdk_eventbridge.types.endpoint_url.EndpointUrl"]
    """<p>The URL of the endpoint.</p>"""
    state: NotRequired["aws_sdk_eventbridge.types.endpoint_state.EndpointState"]
    """<p>The current state of the endpoint.</p>"""
    state_reason: NotRequired[
        "aws_sdk_eventbridge.types.endpoint_state_reason.EndpointStateReason"
    ]
    """<p>The reason the endpoint is in its current state.</p>"""
    creation_time: NotRequired["aws_sdk_eventbridge.types.timestamp.Timestamp"]
    """<p>The time the endpoint was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_eventbridge.types.timestamp.Timestamp"]
    """<p>The last time the endpoint was modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Endpoint) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "arn" in value:
        out["Arn"] = value["arn"]
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
    if "endpoint_id" in value:
        out["EndpointId"] = value["endpoint_id"]
    if "endpoint_url" in value:
        out["EndpointUrl"] = value["endpoint_url"]
    if "state" in value:
        import aws_sdk_eventbridge.types.endpoint_state

        out["State"] = aws_sdk_eventbridge.types.endpoint_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "creation_time" in value:
        import aws_sdk_eventbridge.types.timestamp

        out["CreationTime"] = (
            aws_sdk_eventbridge.types.timestamp.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_eventbridge.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_eventbridge.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Endpoint:
    out: Endpoint = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
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
    if "EndpointId" in data:
        out["endpoint_id"] = data["EndpointId"]
    if "EndpointUrl" in data:
        out["endpoint_url"] = data["EndpointUrl"]
    if "State" in data:
        import aws_sdk_eventbridge.types.endpoint_state

        out["state"] = (
            aws_sdk_eventbridge.types.endpoint_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if "StateReason" in data:
        out["state_reason"] = data["StateReason"]
    if "CreationTime" in data:
        import aws_sdk_eventbridge.types.timestamp

        out["creation_time"] = (
            aws_sdk_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_eventbridge.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out
