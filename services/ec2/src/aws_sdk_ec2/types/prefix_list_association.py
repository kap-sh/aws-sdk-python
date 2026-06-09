"""Generated from Smithy shape ``com.amazonaws.ec2#PrefixListAssociation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class PrefixListAssociation(TypedDict):
    resource_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the resource.</p>"""
    resource_owner: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The owner of the resource.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PrefixListAssociation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_id" in value:
        pairs.append((f"{prefix}.ResourceId", str(value["resource_id"])))
    if "resource_owner" in value:
        pairs.append((f"{prefix}.ResourceOwner", str(value["resource_owner"])))


def deserialize_ec2_query(el: Element) -> PrefixListAssociation:
    out: PrefixListAssociation = {}  # type: ignore[typeddict-item]
    child_resource_id = el.find("ResourceId")
    if child_resource_id is not None:
        out["resource_id"] = str(child_resource_id.text or "")
    child_resource_owner = el.find("ResourceOwner")
    if child_resource_owner is not None:
        out["resource_owner"] = str(child_resource_owner.text or "")
    return out
