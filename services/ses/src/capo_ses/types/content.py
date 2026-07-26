"""Generated from Smithy shape ``com.amazonaws.ses#Content``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.charset
    import capo_ses.types.message_data


class Content(TypedDict, closed=True):
    data: "capo_ses.types.message_data.MessageData"
    """<p>The textual data of the content.</p>"""
    charset: NotRequired["capo_ses.types.charset.Charset"]
    """<p>The character set of the content.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Content, pairs: list[tuple[str, str]], prefix: str) -> None:
    pairs.append((f"{prefix}.Data", str(value["data"])))
    if "charset" in value:
        pairs.append((f"{prefix}.Charset", str(value["charset"])))


def deserialize_query(el: Element) -> Content:
    out: Content = {}  # type: ignore[typeddict-item]
    child_data = el.find("Data")
    if child_data is not None:
        out["data"] = str(child_data.text or "")
    else:
        raise DeserializationError("Content.data required")
    child_charset = el.find("Charset")
    if child_charset is not None:
        out["charset"] = str(child_charset.text or "")
    return out
