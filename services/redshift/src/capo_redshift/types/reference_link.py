"""Generated from Smithy shape ``com.amazonaws.redshift#ReferenceLink``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string


class ReferenceLink(TypedDict, closed=True):
    text: NotRequired["capo_redshift.types.string.String"]
    """<p>The hyperlink text that describes the link to more information.</p>"""
    link: NotRequired["capo_redshift.types.string.String"]
    """<p>The URL address to find more information.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReferenceLink, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "text" in value:
        pairs.append((f"{prefix}.Text", str(value["text"])))
    if "link" in value:
        pairs.append((f"{prefix}.Link", str(value["link"])))


def deserialize_query(el: Element) -> ReferenceLink:
    out: ReferenceLink = {}  # type: ignore[typeddict-item]
    child_text = el.find("Text")
    if child_text is not None:
        out["text"] = str(child_text.text or "")
    child_link = el.find("Link")
    if child_link is not None:
        out["link"] = str(child_link.text or "")
    return out
