"""Generated from Smithy shape ``com.amazonaws.pinpoint#SendUsersMessageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.direct_message_configuration
    import aws_sdk_pinpoint.types.map_of__string
    import aws_sdk_pinpoint.types.map_of_endpoint_send_configuration
    import aws_sdk_pinpoint.types.template_configuration


class SendUsersMessageRequest(TypedDict, closed=True):
    context: NotRequired["aws_sdk_pinpoint.types.map_of__string.MapOf__string"]
    """<p>A map of custom attribute-value pairs. For a push notification, Amazon Pinpoint adds these attributes to the data.pinpoint object in the body of the notification payload. Amazon Pinpoint also provides these attributes in the events that it generates for users-messages deliveries.</p>"""
    message_configuration: NotRequired[
        "aws_sdk_pinpoint.types.direct_message_configuration.DirectMessageConfiguration"
    ]
    """<p>The settings and content for the default message and any default messages that you defined for specific channels.</p>"""
    template_configuration: NotRequired[
        "aws_sdk_pinpoint.types.template_configuration.TemplateConfiguration"
    ]
    """<p>The message template to use for the message.</p>"""
    trace_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for tracing the message. This identifier is visible to message recipients.</p>"""
    users: NotRequired[
        "aws_sdk_pinpoint.types.map_of_endpoint_send_configuration.MapOfEndpointSendConfiguration"
    ]
    r"""<p>A map that associates user IDs with <a href=\"https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#apps-application-id-messages-model-endpointsendconfiguration\">EndpointSendConfiguration</a> objects. You can use an <a href=\"https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#apps-application-id-messages-model-endpointsendconfiguration\">EndpointSendConfiguration</a> object to tailor the message for a user by specifying settings such as content overrides and message variables.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendUsersMessageRequest) -> dict:
    out: dict = {}
    if "context" in value:
        import aws_sdk_pinpoint.types.map_of__string

        out["Context"] = aws_sdk_pinpoint.types.map_of__string.serialize_json(
            value["context"]
        )
    if "message_configuration" in value:
        import aws_sdk_pinpoint.types.direct_message_configuration

        out["MessageConfiguration"] = (
            aws_sdk_pinpoint.types.direct_message_configuration.serialize_json(
                value["message_configuration"]
            )
        )
    if "template_configuration" in value:
        import aws_sdk_pinpoint.types.template_configuration

        out["TemplateConfiguration"] = (
            aws_sdk_pinpoint.types.template_configuration.serialize_json(
                value["template_configuration"]
            )
        )
    if "trace_id" in value:
        out["TraceId"] = value["trace_id"]
    if "users" in value:
        import aws_sdk_pinpoint.types.map_of_endpoint_send_configuration

        out["Users"] = (
            aws_sdk_pinpoint.types.map_of_endpoint_send_configuration.serialize_json(
                value["users"]
            )
        )
    return out


def deserialize_json(data: dict) -> SendUsersMessageRequest:
    out: SendUsersMessageRequest = {}  # type: ignore[typeddict-item]
    if "Context" in data:
        import aws_sdk_pinpoint.types.map_of__string

        out["context"] = aws_sdk_pinpoint.types.map_of__string.deserialize_json(
            data["Context"]
        )
    if "MessageConfiguration" in data:
        import aws_sdk_pinpoint.types.direct_message_configuration

        out["message_configuration"] = (
            aws_sdk_pinpoint.types.direct_message_configuration.deserialize_json(
                data["MessageConfiguration"]
            )
        )
    if "TemplateConfiguration" in data:
        import aws_sdk_pinpoint.types.template_configuration

        out["template_configuration"] = (
            aws_sdk_pinpoint.types.template_configuration.deserialize_json(
                data["TemplateConfiguration"]
            )
        )
    if "TraceId" in data:
        out["trace_id"] = data["TraceId"]
    if "Users" in data:
        import aws_sdk_pinpoint.types.map_of_endpoint_send_configuration

        out["users"] = (
            aws_sdk_pinpoint.types.map_of_endpoint_send_configuration.deserialize_json(
                data["Users"]
            )
        )
    return out
