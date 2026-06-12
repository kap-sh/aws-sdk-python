"""Generated from Smithy shape ``com.amazonaws.ses#Body``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.content


class Body(TypedDict):
    text: NotRequired["aws_sdk_ses.types.content.Content"]
    """<p>The content of the message, in text format. Use this for text-based email clients, or clients on high-latency networks (such as mobile devices).</p>"""
    html: NotRequired["aws_sdk_ses.types.content.Content"]
    """<p>The content of the message, in HTML format. Use this for email clients that can process HTML. You can include clickable links, formatted text, and much more in an HTML message.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Body, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "text" in value:
        import aws_sdk_ses.types.content

        aws_sdk_ses.types.content.serialize_query(
            value["text"], pairs, f"{prefix}.Text"
        )
    if "html" in value:
        import aws_sdk_ses.types.content

        aws_sdk_ses.types.content.serialize_query(
            value["html"], pairs, f"{prefix}.Html"
        )


def deserialize_query(el: Element) -> Body:
    out: Body = {}  # type: ignore[typeddict-item]
    child_text = el.find("Text")
    if child_text is not None:
        import aws_sdk_ses.types.content

        out["text"] = aws_sdk_ses.types.content.deserialize_query(child_text)
    child_html = el.find("Html")
    if child_html is not None:
        import aws_sdk_ses.types.content

        out["html"] = aws_sdk_ses.types.content.deserialize_query(child_html)
    return out
