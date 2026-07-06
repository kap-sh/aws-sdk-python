"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.endpoint_request


class UpdateEndpointRequest(TypedDict, closed=True):
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    endpoint_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The case insensitive unique identifier for the endpoint. The identifier can't contain <code>$</code>, <code>{</code> or <code>}</code>.</p>"""
    endpoint_request: NotRequired[
        "aws_sdk_pinpoint.types.endpoint_request.EndpointRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEndpointRequest) -> dict:
    out: dict = {}
    if "endpoint_request" in value:
        import aws_sdk_pinpoint.types.endpoint_request

        out["EndpointRequest"] = aws_sdk_pinpoint.types.endpoint_request.serialize_json(
            value["endpoint_request"]
        )
    return out


def deserialize_json(data: dict) -> UpdateEndpointRequest:
    out: UpdateEndpointRequest = {}  # type: ignore[typeddict-item]
    if "EndpointRequest" in data:
        import aws_sdk_pinpoint.types.endpoint_request

        out["endpoint_request"] = (
            aws_sdk_pinpoint.types.endpoint_request.deserialize_json(
                data["EndpointRequest"]
            )
        )
    return out
