"""Generated from Smithy shape ``com.amazonaws.pinpoint#AddressConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.channel_type
    import aws_sdk_pinpoint.types.map_of__string
    import aws_sdk_pinpoint.types.map_of_list_of__string


class AddressConfiguration(TypedDict, closed=True):
    body_override: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The message body to use instead of the default message body. This value overrides the default message body.</p>"""
    channel_type: NotRequired["aws_sdk_pinpoint.types.channel_type.ChannelType"]
    """<p>The channel to use when sending the message.</p>"""
    context: NotRequired["aws_sdk_pinpoint.types.map_of__string.MapOf__string"]
    """<p>An object that maps custom attributes to attributes for the address and is attached to the message. Attribute names are case sensitive.</p> <p>For a push notification, this payload is added to the data.pinpoint object. For an email or text message, this payload is added to email/SMS delivery receipt event attributes.</p>"""
    raw_content: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The raw, JSON-formatted string to use as the payload for the message. If specified, this value overrides all other values for the message.</p>"""
    substitutions: NotRequired[
        "aws_sdk_pinpoint.types.map_of_list_of__string.MapOfListOf__string"
    ]
    """<p>A map of the message variables to merge with the variables specified by properties of the DefaultMessage object. The variables specified in this map take precedence over all other variables.</p>"""
    title_override: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The message title to use instead of the default message title. This value overrides the default message title.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddressConfiguration) -> dict:
    out: dict = {}
    if "body_override" in value:
        out["BodyOverride"] = value["body_override"]
    if "channel_type" in value:
        import aws_sdk_pinpoint.types.channel_type

        out["ChannelType"] = aws_sdk_pinpoint.types.channel_type.serialize_json(
            value["channel_type"]
        )
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


def deserialize_json(data: dict) -> AddressConfiguration:
    out: AddressConfiguration = {}  # type: ignore[typeddict-item]
    if "BodyOverride" in data:
        out["body_override"] = data["BodyOverride"]
    if "ChannelType" in data:
        import aws_sdk_pinpoint.types.channel_type

        out["channel_type"] = aws_sdk_pinpoint.types.channel_type.deserialize_json(
            data["ChannelType"]
        )
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
