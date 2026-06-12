"""Generated from Smithy shape ``com.amazonaws.pinpoint#EndpointMessageResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__integer
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.delivery_status


class EndpointMessageResult(TypedDict):
    address: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The endpoint address that the message was delivered to.</p>"""
    delivery_status: NotRequired[
        "aws_sdk_pinpoint.types.delivery_status.DeliveryStatus"
    ]
    """<p>The delivery status of the message. Possible values are:</p> <ul> <li><p>DUPLICATE - The endpoint address is a duplicate of another endpoint address. Amazon Pinpoint won't attempt to send the message again.</p></li> <li><p>OPT_OUT - The user who's associated with the endpoint has opted out of receiving messages from you. Amazon Pinpoint won't attempt to send the message again.</p></li> <li><p>PERMANENT_FAILURE - An error occurred when delivering the message to the endpoint. Amazon Pinpoint won't attempt to send the message again.</p></li> <li><p>SUCCESSFUL - The message was successfully delivered to the endpoint.</p></li> <li><p>TEMPORARY_FAILURE - A temporary error occurred. Amazon Pinpoint won't attempt to send the message again.</p></li> <li><p>THROTTLED - Amazon Pinpoint throttled the operation to send the message to the endpoint.</p></li> <li><p>UNKNOWN_FAILURE - An unknown error occurred.</p></li></ul>"""
    message_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the message that was sent.</p>"""
    status_code: NotRequired["aws_sdk_pinpoint.types.__integer.__integer"]
    """<p>The downstream service status code for delivering the message.</p>"""
    status_message: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The status message for delivering the message.</p>"""
    updated_token: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>For push notifications that are sent through the GCM channel, specifies whether the endpoint's device registration token was updated as part of delivering the message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EndpointMessageResult) -> dict:
    out: dict = {}
    if "address" in value:
        out["Address"] = value["address"]
    if "delivery_status" in value:
        import aws_sdk_pinpoint.types.delivery_status

        out["DeliveryStatus"] = aws_sdk_pinpoint.types.delivery_status.serialize_json(
            value["delivery_status"]
        )
    if "message_id" in value:
        out["MessageId"] = value["message_id"]
    if "status_code" in value:
        out["StatusCode"] = value["status_code"]
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "updated_token" in value:
        out["UpdatedToken"] = value["updated_token"]
    return out


def deserialize_json(data: dict) -> EndpointMessageResult:
    out: EndpointMessageResult = {}  # type: ignore[typeddict-item]
    if "Address" in data:
        out["address"] = data["Address"]
    if "DeliveryStatus" in data:
        import aws_sdk_pinpoint.types.delivery_status

        out["delivery_status"] = (
            aws_sdk_pinpoint.types.delivery_status.deserialize_json(
                data["DeliveryStatus"]
            )
        )
    if "MessageId" in data:
        out["message_id"] = data["MessageId"]
    if "StatusCode" in data:
        out["status_code"] = data["StatusCode"]
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "UpdatedToken" in data:
        out["updated_token"] = data["UpdatedToken"]
    return out
