"""Generated from Smithy shape ``com.amazonaws.rds#DocLink``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string


class DocLink(TypedDict):
    text: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The text with the link to documentation for the recommendation.</p>"""
    url: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The URL for the documentation for the recommendation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: DocLink, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "text" in value:
        pairs.append((f"{prefix}.Text", str(value["text"])))
    if "url" in value:
        pairs.append((f"{prefix}.Url", str(value["url"])))


def deserialize_query(el: Element) -> DocLink:
    out: DocLink = {}  # type: ignore[typeddict-item]
    child_text = el.find("Text")
    if child_text is not None:
        out["text"] = str(child_text.text or "")
    child_url = el.find("Url")
    if child_url is not None:
        out["url"] = str(child_url.text or "")
    return out
