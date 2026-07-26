"""Generated from Smithy shape ``com.amazonaws.eventbridge#DescribeEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.endpoint_arn
    import capo_eventbridge.types.endpoint_description
    import capo_eventbridge.types.endpoint_event_bus_list
    import capo_eventbridge.types.endpoint_id
    import capo_eventbridge.types.endpoint_name
    import capo_eventbridge.types.endpoint_state
    import capo_eventbridge.types.endpoint_state_reason
    import capo_eventbridge.types.endpoint_url
    import capo_eventbridge.types.iam_role_arn
    import capo_eventbridge.types.replication_config
    import capo_eventbridge.types.routing_config
    import capo_eventbridge.types.timestamp


class DescribeEndpointResponse(TypedDict, closed=True):
    name: NotRequired["capo_eventbridge.types.endpoint_name.EndpointName"]
    """<p>The name of the endpoint you asked for information about.</p>"""
    description: NotRequired[
        "capo_eventbridge.types.endpoint_description.EndpointDescription"
    ]
    """<p>The description of the endpoint you asked for information about.</p>"""
    arn: NotRequired["capo_eventbridge.types.endpoint_arn.EndpointArn"]
    """<p>The ARN of the endpoint you asked for information about.</p>"""
    routing_config: NotRequired["capo_eventbridge.types.routing_config.RoutingConfig"]
    """<p>The routing configuration of the endpoint you asked for information about.</p>"""
    replication_config: NotRequired[
        "capo_eventbridge.types.replication_config.ReplicationConfig"
    ]
    """<p>Whether replication is enabled or disabled for the endpoint you asked for information about.</p>"""
    event_buses: NotRequired[
        "capo_eventbridge.types.endpoint_event_bus_list.EndpointEventBusList"
    ]
    """<p>The event buses being used by the endpoint you asked for information about.</p>"""
    role_arn: NotRequired["capo_eventbridge.types.iam_role_arn.IamRoleArn"]
    """<p>The ARN of the role used by the endpoint you asked for information about.</p>"""
    endpoint_id: NotRequired["capo_eventbridge.types.endpoint_id.EndpointId"]
    """<p>The ID of the endpoint you asked for information about.</p>"""
    endpoint_url: NotRequired["capo_eventbridge.types.endpoint_url.EndpointUrl"]
    """<p>The URL of the endpoint you asked for information about.</p>"""
    state: NotRequired["capo_eventbridge.types.endpoint_state.EndpointState"]
    """<p>The current state of the endpoint you asked for information about.</p>"""
    state_reason: NotRequired[
        "capo_eventbridge.types.endpoint_state_reason.EndpointStateReason"
    ]
    """<p>The reason the endpoint you asked for information about is in its current state.</p>"""
    creation_time: NotRequired["capo_eventbridge.types.timestamp.Timestamp"]
    """<p>The time the endpoint you asked for information about was created.</p>"""
    last_modified_time: NotRequired["capo_eventbridge.types.timestamp.Timestamp"]
    """<p>The last time the endpoint you asked for information about was modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEndpointResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
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
    if "endpoint_id" in value:
        out["EndpointId"] = value["endpoint_id"]
    if "endpoint_url" in value:
        out["EndpointUrl"] = value["endpoint_url"]
    if "state" in value:
        import capo_eventbridge.types.endpoint_state

        out["State"] = capo_eventbridge.types.endpoint_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "creation_time" in value:
        import capo_eventbridge.types.timestamp

        out["CreationTime"] = capo_eventbridge.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_eventbridge.types.timestamp

        out["LastModifiedTime"] = (
            capo_eventbridge.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEndpointResponse:
    out: DescribeEndpointResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
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
    if "EndpointId" in data:
        out["endpoint_id"] = data["EndpointId"]
    if "EndpointUrl" in data:
        out["endpoint_url"] = data["EndpointUrl"]
    if "State" in data:
        import capo_eventbridge.types.endpoint_state

        out["state"] = capo_eventbridge.types.endpoint_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "StateReason" in data:
        out["state_reason"] = data["StateReason"]
    if "CreationTime" in data:
        import capo_eventbridge.types.timestamp

        out["creation_time"] = (
            capo_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import capo_eventbridge.types.timestamp

        out["last_modified_time"] = (
            capo_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out
