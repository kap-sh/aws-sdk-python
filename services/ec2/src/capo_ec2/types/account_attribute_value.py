"""Generated from Smithy shape ``com.amazonaws.ec2#AccountAttributeValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class AccountAttributeValue(TypedDict, closed=True):
    attribute_value: NotRequired["capo_ec2.types.string.String"]
    """<p>The value of the attribute.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AccountAttributeValue, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "attribute_value" in value:
        pairs.append((f"{key_prefix}AttributeValue", str(value["attribute_value"])))


def deserialize_ec2_query(el: Element) -> AccountAttributeValue:
    out: AccountAttributeValue = {}  # type: ignore[typeddict-item]
    child_attribute_value = el.find("AttributeValue")
    if child_attribute_value is not None:
        out["attribute_value"] = str(child_attribute_value.text or "")
    return out
