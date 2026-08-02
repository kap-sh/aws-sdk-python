"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPolicyOrganizationTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class IpamPolicyOrganizationTarget(TypedDict, closed=True):
    organization_target_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services Organizations target.</p> <p>A target can be an individual Amazon Web Services account or an entity within an Amazon Web Services Organization to which an IPAM policy can be applied.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPolicyOrganizationTarget, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "organization_target_id" in value:
        pairs.append(
            (f"{key_prefix}OrganizationTargetId", str(value["organization_target_id"]))
        )


def deserialize_ec2_query(el: Element) -> IpamPolicyOrganizationTarget:
    out: IpamPolicyOrganizationTarget = {}  # type: ignore[typeddict-item]
    child_organization_target_id = el.find("OrganizationTargetId")
    if child_organization_target_id is not None:
        out["organization_target_id"] = str(child_organization_target_id.text or "")
    return out
