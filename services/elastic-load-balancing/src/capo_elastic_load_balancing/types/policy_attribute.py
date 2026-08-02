"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#PolicyAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.attribute_name
    import capo_elastic_load_balancing.types.attribute_value


class PolicyAttribute(TypedDict, closed=True):
    attribute_name: NotRequired[
        "capo_elastic_load_balancing.types.attribute_name.AttributeName"
    ]
    """<p>The name of the attribute.</p>"""
    attribute_value: NotRequired[
        "capo_elastic_load_balancing.types.attribute_value.AttributeValue"
    ]
    """<p>The value of the attribute.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PolicyAttribute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "attribute_name" in value:
        pairs.append((f"{key_prefix}AttributeName", str(value["attribute_name"])))
    if "attribute_value" in value:
        pairs.append((f"{key_prefix}AttributeValue", str(value["attribute_value"])))


def deserialize_query(el: Element) -> PolicyAttribute:
    out: PolicyAttribute = {}  # type: ignore[typeddict-item]
    child_attribute_name = el.find("AttributeName")
    if child_attribute_name is not None:
        out["attribute_name"] = str(child_attribute_name.text or "")
    child_attribute_value = el.find("AttributeValue")
    if child_attribute_value is not None:
        out["attribute_value"] = str(child_attribute_value.text or "")
    return out
