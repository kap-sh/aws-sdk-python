"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#SearchFlowExecutionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotthingsgraph.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.flow_execution_id
    import aws_sdk_iotthingsgraph.types.max_results
    import aws_sdk_iotthingsgraph.types.next_token
    import aws_sdk_iotthingsgraph.types.timestamp
    import aws_sdk_iotthingsgraph.types.urn


class SearchFlowExecutionsRequest(TypedDict):
    system_instance_id: "aws_sdk_iotthingsgraph.types.urn.Urn"
    """<p>The ID of the system instance that contains the flow.</p>"""
    flow_execution_id: NotRequired[
        "aws_sdk_iotthingsgraph.types.flow_execution_id.FlowExecutionId"
    ]
    """<p>The ID of a flow execution.</p>"""
    start_time: NotRequired["aws_sdk_iotthingsgraph.types.timestamp.Timestamp"]
    """<p>The date and time of the earliest flow execution to return.</p>"""
    end_time: NotRequired["aws_sdk_iotthingsgraph.types.timestamp.Timestamp"]
    """<p>The date and time of the latest flow execution to return.</p>"""
    next_token: NotRequired["aws_sdk_iotthingsgraph.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results. Use this when you're paginating results.</p>"""
    max_results: NotRequired["aws_sdk_iotthingsgraph.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchFlowExecutionsRequest) -> dict:
    out: dict = {}
    out["systemInstanceId"] = value["system_instance_id"]
    if "flow_execution_id" in value:
        out["flowExecutionId"] = value["flow_execution_id"]
    if "start_time" in value:
        import aws_sdk_iotthingsgraph.types.timestamp

        out["startTime"] = (
            aws_sdk_iotthingsgraph.types.timestamp.serialize_aws_json_1_1(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import aws_sdk_iotthingsgraph.types.timestamp

        out["endTime"] = aws_sdk_iotthingsgraph.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchFlowExecutionsRequest:
    out: SearchFlowExecutionsRequest = {}  # type: ignore[typeddict-item]
    if "systemInstanceId" in data:
        out["system_instance_id"] = data["systemInstanceId"]
    else:
        raise DeserializationError(
            "SearchFlowExecutionsRequest.system_instance_id required"
        )
    if "flowExecutionId" in data:
        out["flow_execution_id"] = data["flowExecutionId"]
    if "startTime" in data:
        import aws_sdk_iotthingsgraph.types.timestamp

        out["start_time"] = (
            aws_sdk_iotthingsgraph.types.timestamp.deserialize_aws_json_1_1(
                data["startTime"]
            )
        )
    if "endTime" in data:
        import aws_sdk_iotthingsgraph.types.timestamp

        out["end_time"] = (
            aws_sdk_iotthingsgraph.types.timestamp.deserialize_aws_json_1_1(
                data["endTime"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
