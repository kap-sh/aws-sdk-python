"""Generated from Smithy shape ``com.amazonaws.pinpoint#EndpointSendConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.map_of__string
    import aws_sdk_pinpoint.types.map_of_list_of__string


class EndpointSendConfiguration(TypedDict):
    body_override: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The body of the message. If specified, this value overrides the default message body.</p>"""
    context: NotRequired["aws_sdk_pinpoint.types.map_of__string.MapOf__string"]
    """<p>A map of custom attributes to attach to the message for the address. Attribute names are case sensitive.</p> <p>For a push notification, this payload is added to the data.pinpoint object. For an email or text message, this payload is added to email/SMS delivery receipt event attributes.</p>"""
    raw_content: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The raw, JSON-formatted string to use as the payload for the message. If specified, this value overrides all other values for the message.</p>"""
    substitutions: NotRequired[
        "aws_sdk_pinpoint.types.map_of_list_of__string.MapOfListOf__string"
    ]
    """<p>A map of the message variables to merge with the variables specified for the default message (DefaultMessage.Substitutions). The variables specified in this map take precedence over all other variables.</p>"""
    title_override: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The title or subject line of the message. If specified, this value overrides the default message title or subject line.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EndpointSendConfiguration) -> dict:
    out: dict = {}
    if "body_override" in value:
        out["BodyOverride"] = value["body_override"]
    if "context" in value:
        import aws_sdk_pinpoint.types.map_of__string

        out["Context"] = aws_sdk_pinpoint.types.map_of__string.serialize_json(
            value["context"]
        )
    if "raw_content" in value:
        out["RawContent"] = value["raw_content"]
    if "substitutions" in value:
        import aws_sdk_pinpoint.types.map_of_list_of__string

        out["Substitutions"] = (
            aws_sdk_pinpoint.types.map_of_list_of__string.serialize_json(
                value["substitutions"]
            )
        )
    if "title_override" in value:
        out["TitleOverride"] = value["title_override"]
    return out


def deserialize_json(data: dict) -> EndpointSendConfiguration:
    out: EndpointSendConfiguration = {}  # type: ignore[typeddict-item]
    if "BodyOverride" in data:
        out["body_override"] = data["BodyOverride"]
    if "Context" in data:
        import aws_sdk_pinpoint.types.map_of__string

        out["context"] = aws_sdk_pinpoint.types.map_of__string.deserialize_json(
            data["Context"]
        )
    if "RawContent" in data:
        out["raw_content"] = data["RawContent"]
    if "Substitutions" in data:
        import aws_sdk_pinpoint.types.map_of_list_of__string

        out["substitutions"] = (
            aws_sdk_pinpoint.types.map_of_list_of__string.deserialize_json(
                data["Substitutions"]
            )
        )
    if "TitleOverride" in data:
        out["title_override"] = data["TitleOverride"]
    return out
