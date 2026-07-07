"""Generated from Smithy shape ``com.amazonaws.appflow#StartFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.client_token
    import aws_sdk_appflow.types.flow_name


class StartFlowRequest(TypedDict, closed=True):
    flow_name: "aws_sdk_appflow.types.flow_name.FlowName"
    """<p> The specified name of the flow. Spaces are not allowed. Use underscores (_) or hyphens (-) only. </p>"""
    client_token: NotRequired["aws_sdk_appflow.types.client_token.ClientToken"]
    """<p>The <code>clientToken</code> parameter is an idempotency token. It ensures that your <code>StartFlow</code> request completes only once. You choose the value to pass. For example, if you don't receive a response from your request, you can safely retry the request with the same <code>clientToken</code> parameter value.</p> <p>If you omit a <code>clientToken</code> value, the Amazon Web Services SDK that you are using inserts a value for you. This way, the SDK can safely retry requests multiple times after a network error. You must provide your own value for other use cases.</p> <p>If you specify input parameters that differ from your first request, an error occurs for flows that run on a schedule or based on an event. However, the error doesn't occur for flows that run on demand. You set the conditions that initiate your flow for the <code>triggerConfig</code> parameter.</p> <p>If you use a different value for <code>clientToken</code>, Amazon AppFlow considers it a new call to <code>StartFlow</code>. The token is active for 8 hours.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartFlowRequest) -> dict:
    out: dict = {}
    out["flowName"] = value["flow_name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartFlowRequest:
    out: StartFlowRequest = {}  # type: ignore[typeddict-item]
    if "flowName" in data:
        out["flow_name"] = data["flowName"]
    else:
        raise DeserializationError("StartFlowRequest.flow_name required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
