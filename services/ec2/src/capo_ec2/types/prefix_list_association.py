"""Generated from Smithy shape ``com.amazonaws.ec2#PrefixListAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class PrefixListAssociation(TypedDict, closed=True):
    resource_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the resource.</p>"""
    resource_owner: NotRequired["capo_ec2.types.string.String"]
    """<p>The owner of the resource.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PrefixListAssociation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resource_id" in value:
        pairs.append((f"{key_prefix}ResourceId", str(value["resource_id"])))
    if "resource_owner" in value:
        pairs.append((f"{key_prefix}ResourceOwner", str(value["resource_owner"])))


def deserialize_ec2_query(el: Element) -> PrefixListAssociation:
    out: PrefixListAssociation = {}  # type: ignore[typeddict-item]
    child_resource_id = el.find("resourceId")
    if child_resource_id is not None:
        out["resource_id"] = str(child_resource_id.text or "")
    child_resource_owner = el.find("resourceOwner")
    if child_resource_owner is not None:
        out["resource_owner"] = str(child_resource_owner.text or "")
    return out
