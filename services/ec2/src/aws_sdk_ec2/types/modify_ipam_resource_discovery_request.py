"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamResourceDiscoveryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.add_ipam_operating_region_set
    import aws_sdk_ec2.types.add_ipam_organizational_unit_exclusion_set
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_resource_discovery_id
    import aws_sdk_ec2.types.remove_ipam_operating_region_set
    import aws_sdk_ec2.types.remove_ipam_organizational_unit_exclusion_set
    import aws_sdk_ec2.types.string


class ModifyIpamResourceDiscoveryRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_resource_discovery_id: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_discovery_id.IpamResourceDiscoveryId"
    ]
    """<p>A resource discovery ID.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A resource discovery description.</p>"""
    add_operating_regions: NotRequired[
        "aws_sdk_ec2.types.add_ipam_operating_region_set.AddIpamOperatingRegionSet"
    ]
    """<p>Add operating Regions to the resource discovery. Operating Regions are Amazon Web Services Regions where the IPAM is allowed to manage IP address CIDRs. IPAM only discovers and monitors resources in the Amazon Web Services Regions you select as operating Regions.</p>"""
    remove_operating_regions: NotRequired[
        "aws_sdk_ec2.types.remove_ipam_operating_region_set.RemoveIpamOperatingRegionSet"
    ]
    """<p>Remove operating Regions.</p>"""
    add_organizational_unit_exclusions: NotRequired[
        "aws_sdk_ec2.types.add_ipam_organizational_unit_exclusion_set.AddIpamOrganizationalUnitExclusionSet"
    ]
    r"""<p>Add an Organizational Unit (OU) exclusion to your IPAM. If your IPAM is integrated with Amazon Web Services Organizations and you add an organizational unit (OU) exclusion, IPAM will not manage the IP addresses in accounts in that OU exclusion. There is a limit on the number of exclusions you can create. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html\">Quotas for your IPAM</a> in the <i>Amazon VPC IPAM User Guide</i>.</p> <note> <p>The resulting set of exclusions must not result in \"overlap\", meaning two or more OU exclusions must not exclude the same OU. For more information and examples, see the Amazon Web Services CLI request process in <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/exclude-ous.html#exclude-ous-create-delete\">Add or remove OU exclusions </a> in the <i>Amazon VPC User Guide</i>.</p> </note>"""
    remove_organizational_unit_exclusions: NotRequired[
        "aws_sdk_ec2.types.remove_ipam_organizational_unit_exclusion_set.RemoveIpamOrganizationalUnitExclusionSet"
    ]
    r"""<p>Remove an Organizational Unit (OU) exclusion to your IPAM. If your IPAM is integrated with Amazon Web Services Organizations and you add an organizational unit (OU) exclusion, IPAM will not manage the IP addresses in accounts in that OU exclusion. There is a limit on the number of exclusions you can create. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html\">Quotas for your IPAM</a> in the <i>Amazon VPC IPAM User Guide</i>.</p> <note> <p>The resulting set of exclusions must not result in \"overlap\", meaning two or more OU exclusions must not exclude the same OU. For more information and examples, see the Amazon Web Services CLI request process in <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/exclude-ous.html#exclude-ous-create-delete\">Add or remove OU exclusions </a> in the <i>Amazon VPC User Guide</i>.</p> </note>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyIpamResourceDiscoveryRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_resource_discovery_id" in value:
        pairs.append(
            (
                f"{prefix}.IpamResourceDiscoveryId",
                str(value["ipam_resource_discovery_id"]),
            )
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "add_operating_regions" in value:
        import aws_sdk_ec2.types.add_ipam_operating_region_set

        aws_sdk_ec2.types.add_ipam_operating_region_set.serialize_ec2_query(
            value["add_operating_regions"], pairs, f"{prefix}.AddOperatingRegions"
        )
    if "remove_operating_regions" in value:
        import aws_sdk_ec2.types.remove_ipam_operating_region_set

        aws_sdk_ec2.types.remove_ipam_operating_region_set.serialize_ec2_query(
            value["remove_operating_regions"], pairs, f"{prefix}.RemoveOperatingRegions"
        )
    if "add_organizational_unit_exclusions" in value:
        import aws_sdk_ec2.types.add_ipam_organizational_unit_exclusion_set

        aws_sdk_ec2.types.add_ipam_organizational_unit_exclusion_set.serialize_ec2_query(
            value["add_organizational_unit_exclusions"],
            pairs,
            f"{prefix}.AddOrganizationalUnitExclusions",
        )
    if "remove_organizational_unit_exclusions" in value:
        import aws_sdk_ec2.types.remove_ipam_organizational_unit_exclusion_set

        aws_sdk_ec2.types.remove_ipam_organizational_unit_exclusion_set.serialize_ec2_query(
            value["remove_organizational_unit_exclusions"],
            pairs,
            f"{prefix}.RemoveOrganizationalUnitExclusions",
        )


def deserialize_ec2_query(el: Element) -> ModifyIpamResourceDiscoveryRequest:
    out: ModifyIpamResourceDiscoveryRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_resource_discovery_id = el.find("IpamResourceDiscoveryId")
    if child_ipam_resource_discovery_id is not None:
        out["ipam_resource_discovery_id"] = str(
            child_ipam_resource_discovery_id.text or ""
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    if el.find("AddOperatingRegions") is not None:
        import aws_sdk_ec2.types.add_ipam_operating_region_set

        out["add_operating_regions"] = (
            aws_sdk_ec2.types.add_ipam_operating_region_set.deserialize_ec2_query(
                el, "AddOperatingRegions"
            )
        )
    if el.find("RemoveOperatingRegions") is not None:
        import aws_sdk_ec2.types.remove_ipam_operating_region_set

        out["remove_operating_regions"] = (
            aws_sdk_ec2.types.remove_ipam_operating_region_set.deserialize_ec2_query(
                el, "RemoveOperatingRegions"
            )
        )
    if el.find("AddOrganizationalUnitExclusions") is not None:
        import aws_sdk_ec2.types.add_ipam_organizational_unit_exclusion_set

        out["add_organizational_unit_exclusions"] = (
            aws_sdk_ec2.types.add_ipam_organizational_unit_exclusion_set.deserialize_ec2_query(
                el, "AddOrganizationalUnitExclusions"
            )
        )
    if el.find("RemoveOrganizationalUnitExclusions") is not None:
        import aws_sdk_ec2.types.remove_ipam_organizational_unit_exclusion_set

        out["remove_organizational_unit_exclusions"] = (
            aws_sdk_ec2.types.remove_ipam_organizational_unit_exclusion_set.deserialize_ec2_query(
                el, "RemoveOrganizationalUnitExclusions"
            )
        )
    return out
