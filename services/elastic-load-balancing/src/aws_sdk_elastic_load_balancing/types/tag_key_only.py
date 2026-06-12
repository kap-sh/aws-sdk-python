"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#TagKeyOnly``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.tag_key


class TagKeyOnly(TypedDict):
    key: NotRequired["aws_sdk_elastic_load_balancing.types.tag_key.TagKey"]
    """<p>The name of the key.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TagKeyOnly, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "key" in value:
        pairs.append((f"{prefix}.Key", str(value["key"])))


def deserialize_query(el: Element) -> TagKeyOnly:
    out: TagKeyOnly = {}  # type: ignore[typeddict-item]
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    return out
