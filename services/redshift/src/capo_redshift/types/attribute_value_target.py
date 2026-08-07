"""Generated from Smithy shape ``com.amazonaws.redshift#AttributeValueTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string


class AttributeValueTarget(TypedDict, closed=True):
    attribute_value: NotRequired["capo_redshift.types.string.String"]
    """<p>The value of the attribute.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AttributeValueTarget, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "attribute_value" in value:
        pairs.append((f"{key_prefix}AttributeValue", str(value["attribute_value"])))


def deserialize_query(el: Element) -> AttributeValueTarget:
    out: AttributeValueTarget = {}  # type: ignore[typeddict-item]
    child_attribute_value = el.find("AttributeValue")
    if child_attribute_value is not None:
        out["attribute_value"] = str(child_attribute_value.text or "")
    return out
