"""Generated from Smithy shape ``com.amazonaws.iot#CommandPayload``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.command_payload_blob
    import aws_sdk_iot.types.mime_type


class CommandPayload(TypedDict):
    content: NotRequired["aws_sdk_iot.types.command_payload_blob.CommandPayloadBlob"]
    """<p>The static payload file for the command.</p>"""
    content_type: NotRequired["aws_sdk_iot.types.mime_type.MimeType"]
    r"""<p>The content type that specifies the format type of the payload file. This field must use a type/subtype format, such as <code>application/json</code>. For information about various content types, see <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types\">Common MIME types</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommandPayload) -> dict:
    out: dict = {}
    if "content" in value:
        import aws_sdk_iot.types.command_payload_blob

        out["content"] = aws_sdk_iot.types.command_payload_blob.serialize_json(
            value["content"]
        )
    if "content_type" in value:
        out["contentType"] = value["content_type"]
    return out


def deserialize_json(data: dict) -> CommandPayload:
    out: CommandPayload = {}  # type: ignore[typeddict-item]
    if "content" in data:
        import aws_sdk_iot.types.command_payload_blob

        out["content"] = aws_sdk_iot.types.command_payload_blob.deserialize_json(
            data["content"]
        )
    if "contentType" in data:
        out["content_type"] = data["contentType"]
    return out
