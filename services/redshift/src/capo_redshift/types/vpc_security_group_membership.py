"""Generated from Smithy shape ``com.amazonaws.redshift#VpcSecurityGroupMembership``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string


class VpcSecurityGroupMembership(TypedDict, closed=True):
    vpc_security_group_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of the VPC security group.</p>"""
    status: NotRequired["capo_redshift.types.string.String"]
    """<p>The status of the VPC security group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: VpcSecurityGroupMembership, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "vpc_security_group_id" in value:
        pairs.append(
            (f"{key_prefix}VpcSecurityGroupId", str(value["vpc_security_group_id"]))
        )
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))


def deserialize_query(el: Element) -> VpcSecurityGroupMembership:
    out: VpcSecurityGroupMembership = {}  # type: ignore[typeddict-item]
    child_vpc_security_group_id = el.find("VpcSecurityGroupId")
    if child_vpc_security_group_id is not None:
        out["vpc_security_group_id"] = str(child_vpc_security_group_id.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    return out
