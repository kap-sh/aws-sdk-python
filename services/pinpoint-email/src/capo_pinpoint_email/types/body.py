"""Generated from Smithy shape ``com.amazonaws.pinpointemail#Body``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.content


class Body(TypedDict, closed=True):
    text: NotRequired["capo_pinpoint_email.types.content.Content"]
    """<p>An object that represents the version of the message that is displayed in email clients that don't support HTML, or clients where the recipient has disabled HTML rendering.</p>"""
    html: NotRequired["capo_pinpoint_email.types.content.Content"]
    """<p>An object that represents the version of the message that is displayed in email clients that support HTML. HTML messages can include formatted text, hyperlinks, images, and more. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Body) -> dict:
    out: dict = {}
    if "text" in value:
        import capo_pinpoint_email.types.content

        out["Text"] = capo_pinpoint_email.types.content.serialize_json(value["text"])
    if "html" in value:
        import capo_pinpoint_email.types.content

        out["Html"] = capo_pinpoint_email.types.content.serialize_json(value["html"])
    return out


def deserialize_json(data: dict) -> Body:
    out: Body = {}  # type: ignore[typeddict-item]
    if "Text" in data:
        import capo_pinpoint_email.types.content

        out["text"] = capo_pinpoint_email.types.content.deserialize_json(data["Text"])
    if "Html" in data:
        import capo_pinpoint_email.types.content

        out["html"] = capo_pinpoint_email.types.content.deserialize_json(data["Html"])
    return out
