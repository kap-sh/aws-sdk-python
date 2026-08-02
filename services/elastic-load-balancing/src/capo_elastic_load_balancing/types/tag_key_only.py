"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#TagKeyOnly``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.tag_key


class TagKeyOnly(TypedDict, closed=True):
    key: NotRequired["capo_elastic_load_balancing.types.tag_key.TagKey"]
    """<p>The name of the key.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TagKeyOnly, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "key" in value:
        pairs.append((f"{key_prefix}Key", str(value["key"])))


def deserialize_query(el: Element) -> TagKeyOnly:
    out: TagKeyOnly = {}  # type: ignore[typeddict-item]
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    return out
