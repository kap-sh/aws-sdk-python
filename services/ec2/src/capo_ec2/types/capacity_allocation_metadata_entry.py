"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityAllocationMetadataEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class CapacityAllocationMetadataEntry(TypedDict, closed=True):
    key: NotRequired["capo_ec2.types.string.String"]
    """<p>The key of the metadata entry.</p>"""
    value: NotRequired["capo_ec2.types.string.String"]
    """<p>The value of the metadata entry.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityAllocationMetadataEntry, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "key" in value:
        pairs.append((f"{key_prefix}Key", str(value["key"])))
    if "value" in value:
        pairs.append((f"{key_prefix}Value", str(value["value"])))


def deserialize_ec2_query(el: Element) -> CapacityAllocationMetadataEntry:
    out: CapacityAllocationMetadataEntry = {}  # type: ignore[typeddict-item]
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    return out
