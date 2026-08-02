"""Generated from Smithy shape ``com.amazonaws.rds#DocLink``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string


class DocLink(TypedDict, closed=True):
    text: NotRequired["capo_rds.types.string.String"]
    """<p>The text with the link to documentation for the recommendation.</p>"""
    url: NotRequired["capo_rds.types.string.String"]
    """<p>The URL for the documentation for the recommendation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: DocLink, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "text" in value:
        pairs.append((f"{key_prefix}Text", str(value["text"])))
    if "url" in value:
        pairs.append((f"{key_prefix}Url", str(value["url"])))


def deserialize_query(el: Element) -> DocLink:
    out: DocLink = {}  # type: ignore[typeddict-item]
    child_text = el.find("Text")
    if child_text is not None:
        out["text"] = str(child_text.text or "")
    child_url = el.find("Url")
    if child_url is not None:
        out["url"] = str(child_url.text or "")
    return out
