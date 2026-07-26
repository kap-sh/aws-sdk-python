"""Generated from Smithy shape ``com.amazonaws.pinpoint#MessageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.map_of_endpoint_message_result
    import capo_pinpoint.types.map_of_message_result


class MessageResponse(TypedDict, closed=True):
    application_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the application that was used to send the message.</p>"""
    endpoint_result: NotRequired[
        "capo_pinpoint.types.map_of_endpoint_message_result.MapOfEndpointMessageResult"
    ]
    """<p>A map that contains a multipart response for each address that the message was sent to. In the map, the endpoint ID is the key and the result is the value.</p>"""
    request_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The identifier for the original request that the message was delivered for.</p>"""
    result: NotRequired["capo_pinpoint.types.map_of_message_result.MapOfMessageResult"]
    """<p>A map that contains a multipart response for each address (email address, phone number, or push notification token) that the message was sent to. In the map, the address is the key and the result is the value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageResponse) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "endpoint_result" in value:
        import capo_pinpoint.types.map_of_endpoint_message_result

        out["EndpointResult"] = (
            capo_pinpoint.types.map_of_endpoint_message_result.serialize_json(
                value["endpoint_result"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "result" in value:
        import capo_pinpoint.types.map_of_message_result

        out["Result"] = capo_pinpoint.types.map_of_message_result.serialize_json(
            value["result"]
        )
    return out


def deserialize_json(data: dict) -> MessageResponse:
    out: MessageResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "EndpointResult" in data:
        import capo_pinpoint.types.map_of_endpoint_message_result

        out["endpoint_result"] = (
            capo_pinpoint.types.map_of_endpoint_message_result.deserialize_json(
                data["EndpointResult"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "Result" in data:
        import capo_pinpoint.types.map_of_message_result

        out["result"] = capo_pinpoint.types.map_of_message_result.deserialize_json(
            data["Result"]
        )
    return out
