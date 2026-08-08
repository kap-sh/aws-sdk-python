"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPublicAddressSecurityGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class IpamPublicAddressSecurityGroup(TypedDict, closed=True):
    group_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The security group's name.</p>"""
    group_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The security group's ID.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPublicAddressSecurityGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "group_name" in value:
        pairs.append((f"{key_prefix}GroupName", str(value["group_name"])))
    if "group_id" in value:
        pairs.append((f"{key_prefix}GroupId", str(value["group_id"])))


def deserialize_ec2_query(el: Element) -> IpamPublicAddressSecurityGroup:
    out: IpamPublicAddressSecurityGroup = {}  # type: ignore[typeddict-item]
    child_group_name = el.find("groupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    child_group_id = el.find("groupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    return out
