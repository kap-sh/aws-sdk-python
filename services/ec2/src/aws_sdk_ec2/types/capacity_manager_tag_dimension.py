"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityManagerTagDimension``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class CapacityManagerTagDimension(TypedDict):
    key: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The tag key. </p>"""
    value: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The tag value. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityManagerTagDimension, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "key" in value:
        pairs.append((f"{prefix}.Key", str(value["key"])))
    if "value" in value:
        pairs.append((f"{prefix}.Value", str(value["value"])))


def deserialize_ec2_query(el: Element) -> CapacityManagerTagDimension:
    out: CapacityManagerTagDimension = {}  # type: ignore[typeddict-item]
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    return out
