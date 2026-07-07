"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class GetEndpointRequest(TypedDict, closed=True):
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    endpoint_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The case insensitive unique identifier for the endpoint. The identifier can't contain <code>$</code>, <code>{</code> or <code>}</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEndpointRequest:
    out: GetEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
