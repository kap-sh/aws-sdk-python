"""Generated from Smithy shape ``com.amazonaws.pinpoint#InAppMessageBodyConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.alignment


class InAppMessageBodyConfig(TypedDict, closed=True):
    alignment: NotRequired["aws_sdk_pinpoint.types.alignment.Alignment"]
    """<p>The alignment of the text. Valid values: LEFT, CENTER, RIGHT.</p>"""
    body: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>Message Body.</p>"""
    text_color: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The text color.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InAppMessageBodyConfig) -> dict:
    out: dict = {}
    if "alignment" in value:
        import aws_sdk_pinpoint.types.alignment

        out["Alignment"] = aws_sdk_pinpoint.types.alignment.serialize_json(
            value["alignment"]
        )
    if "body" in value:
        out["Body"] = value["body"]
    if "text_color" in value:
        out["TextColor"] = value["text_color"]
    return out


def deserialize_json(data: dict) -> InAppMessageBodyConfig:
    out: InAppMessageBodyConfig = {}  # type: ignore[typeddict-item]
    if "Alignment" in data:
        import aws_sdk_pinpoint.types.alignment

        out["alignment"] = aws_sdk_pinpoint.types.alignment.deserialize_json(
            data["Alignment"]
        )
    if "Body" in data:
        out["body"] = data["Body"]
    if "TextColor" in data:
        out["text_color"] = data["TextColor"]
    return out
