"""Generated from Smithy shape ``com.amazonaws.sesv2#Body``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.content


class Body(TypedDict):
    text: NotRequired["aws_sdk_sesv2.types.content.Content"]
    """<p>An object that represents the version of the message that is displayed in email clients that don't support HTML, or clients where the recipient has disabled HTML rendering.</p>"""
    html: NotRequired["aws_sdk_sesv2.types.content.Content"]
    """<p>An object that represents the version of the message that is displayed in email clients that support HTML. HTML messages can include formatted text, hyperlinks, images, and more. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Body) -> dict:
    out: dict = {}
    if "text" in value:
        import aws_sdk_sesv2.types.content

        out["Text"] = aws_sdk_sesv2.types.content.serialize_json(value["text"])
    if "html" in value:
        import aws_sdk_sesv2.types.content

        out["Html"] = aws_sdk_sesv2.types.content.serialize_json(value["html"])
    return out


def deserialize_json(data: dict) -> Body:
    out: Body = {}  # type: ignore[typeddict-item]
    if "Text" in data:
        import aws_sdk_sesv2.types.content

        out["text"] = aws_sdk_sesv2.types.content.deserialize_json(data["Text"])
    if "Html" in data:
        import aws_sdk_sesv2.types.content

        out["html"] = aws_sdk_sesv2.types.content.deserialize_json(data["Html"])
    return out
