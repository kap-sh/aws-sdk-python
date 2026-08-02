"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcTenancyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.vpc_id
    import capo_ec2.types.vpc_tenancy


class ModifyVpcTenancyRequest(TypedDict, closed=True):
    vpc_id: NotRequired["capo_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC.</p>"""
    instance_tenancy: NotRequired["capo_ec2.types.vpc_tenancy.VpcTenancy"]
    """<p>The instance tenancy attribute for the VPC. </p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVpcTenancyRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "instance_tenancy" in value:
        import capo_ec2.types.vpc_tenancy

        capo_ec2.types.vpc_tenancy.serialize_ec2_query(
            value["instance_tenancy"], pairs, f"{key_prefix}InstanceTenancy"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ModifyVpcTenancyRequest:
    out: ModifyVpcTenancyRequest = {}  # type: ignore[typeddict-item]
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_instance_tenancy = el.find("InstanceTenancy")
    if child_instance_tenancy is not None:
        import capo_ec2.types.vpc_tenancy

        out["instance_tenancy"] = capo_ec2.types.vpc_tenancy.deserialize_ec2_query(
            child_instance_tenancy
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
