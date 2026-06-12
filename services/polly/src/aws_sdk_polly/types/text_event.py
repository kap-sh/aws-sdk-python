"""Generated from Smithy shape ``com.amazonaws.polly#TextEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_polly.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_polly.types.flush_stream_configuration
    import aws_sdk_polly.types.text
    import aws_sdk_polly.types.text_type


class TextEvent(TypedDict):
    text: "aws_sdk_polly.types.text.Text"
    """<p>The text content to synthesize. If you specify <code>ssml</code> as the <code>TextType</code>, follow the SSML format for the input text.</p>"""
    text_type: NotRequired["aws_sdk_polly.types.text_type.TextType"]
    """<p>Specifies whether the input text is plain text or SSML. Default: plain text.</p>"""
    flush_stream_configuration: NotRequired[
        "aws_sdk_polly.types.flush_stream_configuration.FlushStreamConfiguration"
    ]
    """<p>Configuration for controlling when synthesized audio flushes to the output stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextEvent) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    if "text_type" in value:
        import aws_sdk_polly.types.text_type

        out["TextType"] = aws_sdk_polly.types.text_type.serialize_json(
            value["text_type"]
        )
    if "flush_stream_configuration" in value:
        import aws_sdk_polly.types.flush_stream_configuration

        out["FlushStreamConfiguration"] = (
            aws_sdk_polly.types.flush_stream_configuration.serialize_json(
                value["flush_stream_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> TextEvent:
    out: TextEvent = {}  # type: ignore[typeddict-item]
    if "Text" in data:
        out["text"] = data["Text"]
    else:
        raise DeserializationError("TextEvent.text required")
    if "TextType" in data:
        import aws_sdk_polly.types.text_type

        out["text_type"] = aws_sdk_polly.types.text_type.deserialize_json(
            data["TextType"]
        )
    if "FlushStreamConfiguration" in data:
        import aws_sdk_polly.types.flush_stream_configuration

        out["flush_stream_configuration"] = (
            aws_sdk_polly.types.flush_stream_configuration.deserialize_json(
                data["FlushStreamConfiguration"]
            )
        )
    return out
