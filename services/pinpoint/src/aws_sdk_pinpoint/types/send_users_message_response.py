"""Generated from Smithy shape ``com.amazonaws.pinpoint#SendUsersMessageResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.map_of_map_of_endpoint_message_result


class SendUsersMessageResponse(TypedDict):
    application_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the application that was used to send the message.</p>"""
    request_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier that was assigned to the message request.</p>"""
    result: NotRequired[
        "aws_sdk_pinpoint.types.map_of_map_of_endpoint_message_result.MapOfMapOfEndpointMessageResult"
    ]
    """<p>An object that indicates which endpoints the message was sent to, for each user. The object lists user IDs and, for each user ID, provides the endpoint IDs that the message was sent to. For each endpoint ID, it provides an EndpointMessageResult object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendUsersMessageResponse) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "result" in value:
        import aws_sdk_pinpoint.types.map_of_map_of_endpoint_message_result

        out["Result"] = (
            aws_sdk_pinpoint.types.map_of_map_of_endpoint_message_result.serialize_json(
                value["result"]
            )
        )
    return out


def deserialize_json(data: dict) -> SendUsersMessageResponse:
    out: SendUsersMessageResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "Result" in data:
        import aws_sdk_pinpoint.types.map_of_map_of_endpoint_message_result

        out["result"] = (
            aws_sdk_pinpoint.types.map_of_map_of_endpoint_message_result.deserialize_json(
                data["Result"]
            )
        )
    return out
