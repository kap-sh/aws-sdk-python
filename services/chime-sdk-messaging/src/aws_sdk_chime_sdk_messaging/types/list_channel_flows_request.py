"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ListChannelFlowsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.max_results
    import aws_sdk_chime_sdk_messaging.types.next_token


class ListChannelFlowsRequest(TypedDict):
    app_instance_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the app instance.</p>"""
    max_results: NotRequired["aws_sdk_chime_sdk_messaging.types.max_results.MaxResults"]
    """<p>The maximum number of channel flows that you want to return.</p>"""
    next_token: NotRequired["aws_sdk_chime_sdk_messaging.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested channel flows are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelFlowsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListChannelFlowsRequest:
    out: ListChannelFlowsRequest = {}  # type: ignore[typeddict-item]
    return out
