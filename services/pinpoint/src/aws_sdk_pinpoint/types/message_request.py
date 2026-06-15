"""Generated from Smithy shape ``com.amazonaws.pinpoint#MessageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.direct_message_configuration
    import aws_sdk_pinpoint.types.map_of__string
    import aws_sdk_pinpoint.types.map_of_address_configuration
    import aws_sdk_pinpoint.types.map_of_endpoint_send_configuration
    import aws_sdk_pinpoint.types.template_configuration


class MessageRequest(TypedDict):
    addresses: NotRequired[
        "aws_sdk_pinpoint.types.map_of_address_configuration.MapOfAddressConfiguration"
    ]
    r"""<p>A map of key-value pairs, where each key is an address and each value is an <a href=\"https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#apps-application-id-messages-model-addressconfiguration\">AddressConfiguration</a> object. An address can be a push notification token, a phone number, or an email address. You can use an <a href=\"https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#apps-application-id-messages-model-addressconfiguration\">AddressConfiguration</a> object to tailor the message for an address by specifying settings such as content overrides and message variables.</p>"""
    context: NotRequired["aws_sdk_pinpoint.types.map_of__string.MapOf__string"]
    """<p>A map of custom attributes to attach to the message. For a push notification, this payload is added to the data.pinpoint object. For an email or text message, this payload is added to email/SMS delivery receipt event attributes.</p>"""
    endpoints: NotRequired[
        "aws_sdk_pinpoint.types.map_of_endpoint_send_configuration.MapOfEndpointSendConfiguration"
    ]
    r"""<p>A map of key-value pairs, where each key is an endpoint ID and each value is an <a href=\"https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#apps-application-id-messages-model-endpointsendconfiguration\">EndpointSendConfiguration</a> object. You can use an <a href=\"https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#apps-application-id-messages-model-endpointsendconfiguration\">EndpointSendConfiguration</a> object to tailor the message for an endpoint by specifying settings such as content overrides and message variables.</p>"""
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


# --- restJson1 ser/de ---
def serialize_json(value: MessageRequest) -> dict:
    out: dict = {}
    if "addresses" in value:
        import aws_sdk_pinpoint.types.map_of_address_configuration

        out["Addresses"] = (
            aws_sdk_pinpoint.types.map_of_address_configuration.serialize_json(
                value["addresses"]
            )
        )
    if "context" in value:
        import aws_sdk_pinpoint.types.map_of__string

        out["Context"] = aws_sdk_pinpoint.types.map_of__string.serialize_json(
            value["context"]
        )
    if "endpoints" in value:
        import aws_sdk_pinpoint.types.map_of_endpoint_send_configuration

        out["Endpoints"] = (
            aws_sdk_pinpoint.types.map_of_endpoint_send_configuration.serialize_json(
                value["endpoints"]
            )
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
    return out


def deserialize_json(data: dict) -> MessageRequest:
    out: MessageRequest = {}  # type: ignore[typeddict-item]
    if "Addresses" in data:
        import aws_sdk_pinpoint.types.map_of_address_configuration

        out["addresses"] = (
            aws_sdk_pinpoint.types.map_of_address_configuration.deserialize_json(
                data["Addresses"]
            )
        )
    if "Context" in data:
        import aws_sdk_pinpoint.types.map_of__string

        out["context"] = aws_sdk_pinpoint.types.map_of__string.deserialize_json(
            data["Context"]
        )
    if "Endpoints" in data:
        import aws_sdk_pinpoint.types.map_of_endpoint_send_configuration

        out["endpoints"] = (
            aws_sdk_pinpoint.types.map_of_endpoint_send_configuration.deserialize_json(
                data["Endpoints"]
            )
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
    return out
