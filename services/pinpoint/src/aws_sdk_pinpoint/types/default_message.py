"""Generated from Smithy shape ``com.amazonaws.pinpoint#DefaultMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.map_of_list_of__string


class DefaultMessage(TypedDict):
    body: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The default body of the message.</p>"""
    substitutions: NotRequired[
        "aws_sdk_pinpoint.types.map_of_list_of__string.MapOfListOf__string"
    ]
    """<p>The default message variables to use in the message. You can override these default variables with individual address variables.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultMessage) -> dict:
    out: dict = {}
    if "body" in value:
        out["Body"] = value["body"]
    if "substitutions" in value:
        import aws_sdk_pinpoint.types.map_of_list_of__string

        out["Substitutions"] = (
            aws_sdk_pinpoint.types.map_of_list_of__string.serialize_json(
                value["substitutions"]
            )
        )
    return out


def deserialize_json(data: dict) -> DefaultMessage:
    out: DefaultMessage = {}  # type: ignore[typeddict-item]
    if "Body" in data:
        out["body"] = data["Body"]
    if "Substitutions" in data:
        import aws_sdk_pinpoint.types.map_of_list_of__string

        out["substitutions"] = (
            aws_sdk_pinpoint.types.map_of_list_of__string.deserialize_json(
                data["Substitutions"]
            )
        )
    return out
