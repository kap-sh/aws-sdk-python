"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DescribeFlowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.flow
    import aws_sdk_mediaconnect.types.messages


class DescribeFlowResponse(TypedDict, closed=True):
    flow: NotRequired["aws_sdk_mediaconnect.types.flow.Flow"]
    """<p>The flow that you requested a description of. </p>"""
    messages: NotRequired["aws_sdk_mediaconnect.types.messages.Messages"]
    """<p> Any errors that apply currently to the flow. If there are no errors, MediaConnect will not include this field in the response. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFlowResponse) -> dict:
    out: dict = {}
    if "flow" in value:
        import aws_sdk_mediaconnect.types.flow

        out["flow"] = aws_sdk_mediaconnect.types.flow.serialize_json(value["flow"])
    if "messages" in value:
        import aws_sdk_mediaconnect.types.messages

        out["messages"] = aws_sdk_mediaconnect.types.messages.serialize_json(
            value["messages"]
        )
    return out


def deserialize_json(data: dict) -> DescribeFlowResponse:
    out: DescribeFlowResponse = {}  # type: ignore[typeddict-item]
    if "flow" in data:
        import aws_sdk_mediaconnect.types.flow

        out["flow"] = aws_sdk_mediaconnect.types.flow.deserialize_json(data["flow"])
    if "messages" in data:
        import aws_sdk_mediaconnect.types.messages

        out["messages"] = aws_sdk_mediaconnect.types.messages.deserialize_json(
            data["messages"]
        )
    return out
