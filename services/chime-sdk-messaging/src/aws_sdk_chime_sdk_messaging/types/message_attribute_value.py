"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#MessageAttributeValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.message_attribute_string_values


class MessageAttributeValue(TypedDict):
    string_values: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.message_attribute_string_values.MessageAttributeStringValues"
    ]
    """<p>The strings in a message attribute value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageAttributeValue) -> dict:
    out: dict = {}
    if "string_values" in value:
        import aws_sdk_chime_sdk_messaging.types.message_attribute_string_values

        out["StringValues"] = (
            aws_sdk_chime_sdk_messaging.types.message_attribute_string_values.serialize_json(
                value["string_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> MessageAttributeValue:
    out: MessageAttributeValue = {}  # type: ignore[typeddict-item]
    if "StringValues" in data:
        import aws_sdk_chime_sdk_messaging.types.message_attribute_string_values

        out["string_values"] = (
            aws_sdk_chime_sdk_messaging.types.message_attribute_string_values.deserialize_json(
                data["StringValues"]
            )
        )
    return out
