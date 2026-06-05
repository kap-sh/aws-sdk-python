"""Generated from Smithy shape ``com.amazonaws.ec2#AccountAttributeValue``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class AccountAttributeValue(TypedDict):
    attribute_value: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The value of the attribute.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AccountAttributeValue, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "attribute_value" in value:
        pairs.append((f"{prefix}.AttributeValue", str(value["attribute_value"])))


def deserialize_ec2_query(el: Element) -> AccountAttributeValue:
    out: AccountAttributeValue = {}  # type: ignore[typeddict-item]
    child_attribute_value = el.find("AttributeValue")
    if child_attribute_value is not None:
        out["attribute_value"] = str(child_attribute_value.text or "")
    return out
