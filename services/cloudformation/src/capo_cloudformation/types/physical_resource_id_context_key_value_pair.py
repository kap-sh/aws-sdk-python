"""Generated from Smithy shape ``com.amazonaws.cloudformation#PhysicalResourceIdContextKeyValuePair``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.key
    import capo_cloudformation.types.value


class PhysicalResourceIdContextKeyValuePair(TypedDict, closed=True):
    key: NotRequired["capo_cloudformation.types.key.Key"]
    """<p>The resource context key.</p>"""
    value: NotRequired["capo_cloudformation.types.value.Value"]
    """<p>The resource context value.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PhysicalResourceIdContextKeyValuePair,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "key" in value:
        pairs.append((f"{prefix}.Key", str(value["key"])))
    if "value" in value:
        pairs.append((f"{prefix}.Value", str(value["value"])))


def deserialize_query(el: Element) -> PhysicalResourceIdContextKeyValuePair:
    out: PhysicalResourceIdContextKeyValuePair = {}  # type: ignore[typeddict-item]
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    return out
