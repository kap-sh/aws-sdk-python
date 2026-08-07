"""Generated from Smithy shape ``com.amazonaws.ses#Body``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.content


class Body(TypedDict, closed=True):
    text: NotRequired["capo_ses.types.content.Content"]
    """<p>The content of the message, in text format. Use this for text-based email clients, or clients on high-latency networks (such as mobile devices).</p>"""
    html: NotRequired["capo_ses.types.content.Content"]
    """<p>The content of the message, in HTML format. Use this for email clients that can process HTML. You can include clickable links, formatted text, and much more in an HTML message.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Body, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "text" in value:
        import capo_ses.types.content

        capo_ses.types.content.serialize_query(
            value["text"], pairs, f"{key_prefix}Text"
        )
    if "html" in value:
        import capo_ses.types.content

        capo_ses.types.content.serialize_query(
            value["html"], pairs, f"{key_prefix}Html"
        )


def deserialize_query(el: Element) -> Body:
    out: Body = {}  # type: ignore[typeddict-item]
    child_text = el.find("Text")
    if child_text is not None:
        import capo_ses.types.content

        out["text"] = capo_ses.types.content.deserialize_query(child_text)
    child_html = el.find("Html")
    if child_html is not None:
        import capo_ses.types.content

        out["html"] = capo_ses.types.content.deserialize_query(child_html)
    return out
