"""Generated from Smithy shape ``com.amazonaws.rds#ContextAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string


class ContextAttribute(TypedDict, closed=True):
    key: NotRequired["capo_rds.types.string.String"]
    """<p>The key of <code>ContextAttribute</code>.</p>"""
    value: NotRequired["capo_rds.types.string.String"]
    """<p>The value of <code>ContextAttribute</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ContextAttribute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "key" in value:
        pairs.append((f"{key_prefix}Key", str(value["key"])))
    if "value" in value:
        pairs.append((f"{key_prefix}Value", str(value["value"])))


def deserialize_query(el: Element) -> ContextAttribute:
    out: ContextAttribute = {}  # type: ignore[typeddict-item]
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    return out
