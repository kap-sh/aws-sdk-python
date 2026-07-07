"""Generated from Smithy shape ``com.amazonaws.pipes#PipeTargetEventBridgeEventBusParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pipes.types.event_bridge_detail_type
    import aws_sdk_pipes.types.event_bridge_endpoint_id
    import aws_sdk_pipes.types.event_bridge_event_resource_list
    import aws_sdk_pipes.types.event_bridge_event_source
    import aws_sdk_pipes.types.json_path


class PipeTargetEventBridgeEventBusParameters(TypedDict, closed=True):
    endpoint_id: NotRequired[
        "aws_sdk_pipes.types.event_bridge_endpoint_id.EventBridgeEndpointId"
    ]
    """<p>The URL subdomain of the endpoint. For example, if the URL for Endpoint is https://abcde.veo.endpoints.event.amazonaws.com, then the EndpointId is <code>abcde.veo</code>.</p>"""
    detail_type: NotRequired[
        "aws_sdk_pipes.types.event_bridge_detail_type.EventBridgeDetailType"
    ]
    """<p>A free-form string, with a maximum of 128 characters, used to decide what fields to expect in the event detail.</p>"""
    source: NotRequired[
        "aws_sdk_pipes.types.event_bridge_event_source.EventBridgeEventSource"
    ]
    """<p>The source of the event.</p>"""
    resources: NotRequired[
        "aws_sdk_pipes.types.event_bridge_event_resource_list.EventBridgeEventResourceList"
    ]
    """<p>Amazon Web Services resources, identified by Amazon Resource Name (ARN), which the event primarily concerns. Any number, including zero, may be present.</p>"""
    time: NotRequired["aws_sdk_pipes.types.json_path.JsonPath"]
    r"""<p>The time stamp of the event, per <a href=\"https://www.rfc-editor.org/rfc/rfc3339.txt\">RFC3339</a>. If no time stamp is provided, the time stamp of the <a href=\"https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html\">PutEvents</a> call is used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipeTargetEventBridgeEventBusParameters) -> dict:
    out: dict = {}
    if "endpoint_id" in value:
        out["EndpointId"] = value["endpoint_id"]
    if "detail_type" in value:
        out["DetailType"] = value["detail_type"]
    if "source" in value:
        out["Source"] = value["source"]
    if "resources" in value:
        import aws_sdk_pipes.types.event_bridge_event_resource_list

        out["Resources"] = (
            aws_sdk_pipes.types.event_bridge_event_resource_list.serialize_json(
                value["resources"]
            )
        )
    if "time" in value:
        out["Time"] = value["time"]
    return out


def deserialize_json(data: dict) -> PipeTargetEventBridgeEventBusParameters:
    out: PipeTargetEventBridgeEventBusParameters = {}  # type: ignore[typeddict-item]
    if "EndpointId" in data:
        out["endpoint_id"] = data["EndpointId"]
    if "DetailType" in data:
        out["detail_type"] = data["DetailType"]
    if "Source" in data:
        out["source"] = data["Source"]
    if "Resources" in data:
        import aws_sdk_pipes.types.event_bridge_event_resource_list

        out["resources"] = (
            aws_sdk_pipes.types.event_bridge_event_resource_list.deserialize_json(
                data["Resources"]
            )
        )
    if "Time" in data:
        out["time"] = data["Time"]
    return out
