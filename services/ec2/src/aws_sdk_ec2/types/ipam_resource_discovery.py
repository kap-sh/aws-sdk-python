"""Generated from Smithy shape ``com.amazonaws.ec2#IpamResourceDiscovery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_operating_region_set
    import aws_sdk_ec2.types.ipam_organizational_unit_exclusion_set
    import aws_sdk_ec2.types.ipam_resource_discovery_id
    import aws_sdk_ec2.types.ipam_resource_discovery_state
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class IpamResourceDiscovery(TypedDict, closed=True):
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the owner.</p>"""
    ipam_resource_discovery_id: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_discovery_id.IpamResourceDiscoveryId"
    ]
    """<p>The resource discovery ID.</p>"""
    ipam_resource_discovery_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The resource discovery Amazon Resource Name (ARN).</p>"""
    ipam_resource_discovery_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The resource discovery Region.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The resource discovery description.</p>"""
    operating_regions: NotRequired[
        "aws_sdk_ec2.types.ipam_operating_region_set.IpamOperatingRegionSet"
    ]
    """<p>The operating Regions for the resource discovery. Operating Regions are Amazon Web Services Regions where the IPAM is allowed to manage IP address CIDRs. IPAM only discovers and monitors resources in the Amazon Web Services Regions you select as operating Regions.</p>"""
    is_default: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Defines if the resource discovery is the default. The default resource discovery is the resource discovery automatically created when you create an IPAM.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_discovery_state.IpamResourceDiscoveryState"
    ]
    """<p>The lifecycle state of the resource discovery.</p> <ul> <li> <p> <code>create-in-progress</code> - Resource discovery is being created.</p> </li> <li> <p> <code>create-complete</code> - Resource discovery creation is complete.</p> </li> <li> <p> <code>create-failed</code> - Resource discovery creation has failed.</p> </li> <li> <p> <code>modify-in-progress</code> - Resource discovery is being modified.</p> </li> <li> <p> <code>modify-complete</code> - Resource discovery modification is complete.</p> </li> <li> <p> <code>modify-failed</code> - Resource discovery modification has failed.</p> </li> <li> <p> <code>delete-in-progress</code> - Resource discovery is being deleted.</p> </li> <li> <p> <code>delete-complete</code> - Resource discovery deletion is complete.</p> </li> <li> <p> <code>delete-failed</code> - Resource discovery deletion has failed.</p> </li> <li> <p> <code>isolate-in-progress</code> - Amazon Web Services account that created the resource discovery has been removed and the resource discovery is being isolated.</p> </li> <li> <p> <code>isolate-complete</code> - Resource discovery isolation is complete.</p> </li> <li> <p> <code>restore-in-progress</code> - Amazon Web Services account that created the resource discovery and was isolated has been restored.</p> </li> </ul>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.</p>"""
    organizational_unit_exclusions: NotRequired[
        "aws_sdk_ec2.types.ipam_organizational_unit_exclusion_set.IpamOrganizationalUnitExclusionSet"
    ]
    """<p>If your IPAM is integrated with Amazon Web Services Organizations and you add an organizational unit (OU) exclusion, IPAM will not manage the IP addresses in accounts in that OU exclusion.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamResourceDiscovery, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "ipam_resource_discovery_id" in value:
        pairs.append(
            (
                f"{prefix}.IpamResourceDiscoveryId",
                str(value["ipam_resource_discovery_id"]),
            )
        )
    if "ipam_resource_discovery_arn" in value:
        pairs.append(
            (
                f"{prefix}.IpamResourceDiscoveryArn",
                str(value["ipam_resource_discovery_arn"]),
            )
        )
    if "ipam_resource_discovery_region" in value:
        pairs.append(
            (
                f"{prefix}.IpamResourceDiscoveryRegion",
                str(value["ipam_resource_discovery_region"]),
            )
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "operating_regions" in value:
        import aws_sdk_ec2.types.ipam_operating_region_set

        aws_sdk_ec2.types.ipam_operating_region_set.serialize_ec2_query(
            value["operating_regions"], pairs, f"{prefix}.OperatingRegionSet"
        )
    if "is_default" in value:
        pairs.append(
            (f"{prefix}.IsDefault", "true" if value["is_default"] else "false")
        )
    if "state" in value:
        import aws_sdk_ec2.types.ipam_resource_discovery_state

        aws_sdk_ec2.types.ipam_resource_discovery_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "organizational_unit_exclusions" in value:
        import aws_sdk_ec2.types.ipam_organizational_unit_exclusion_set

        aws_sdk_ec2.types.ipam_organizational_unit_exclusion_set.serialize_ec2_query(
            value["organizational_unit_exclusions"],
            pairs,
            f"{prefix}.OrganizationalUnitExclusionSet",
        )


def deserialize_ec2_query(el: Element) -> IpamResourceDiscovery:
    out: IpamResourceDiscovery = {}  # type: ignore[typeddict-item]
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_ipam_resource_discovery_id = el.find("IpamResourceDiscoveryId")
    if child_ipam_resource_discovery_id is not None:
        out["ipam_resource_discovery_id"] = str(
            child_ipam_resource_discovery_id.text or ""
        )
    child_ipam_resource_discovery_arn = el.find("IpamResourceDiscoveryArn")
    if child_ipam_resource_discovery_arn is not None:
        out["ipam_resource_discovery_arn"] = str(
            child_ipam_resource_discovery_arn.text or ""
        )
    child_ipam_resource_discovery_region = el.find("IpamResourceDiscoveryRegion")
    if child_ipam_resource_discovery_region is not None:
        out["ipam_resource_discovery_region"] = str(
            child_ipam_resource_discovery_region.text or ""
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    if el.find("OperatingRegionSet") is not None:
        import aws_sdk_ec2.types.ipam_operating_region_set

        out["operating_regions"] = (
            aws_sdk_ec2.types.ipam_operating_region_set.deserialize_ec2_query(
                el, "OperatingRegionSet"
            )
        )
    child_is_default = el.find("IsDefault")
    if child_is_default is not None:
        out["is_default"] = (child_is_default.text or "").lower() == "true"
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.ipam_resource_discovery_state

        out["state"] = (
            aws_sdk_ec2.types.ipam_resource_discovery_state.deserialize_ec2_query(
                child_state
            )
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    if el.find("OrganizationalUnitExclusionSet") is not None:
        import aws_sdk_ec2.types.ipam_organizational_unit_exclusion_set

        out["organizational_unit_exclusions"] = (
            aws_sdk_ec2.types.ipam_organizational_unit_exclusion_set.deserialize_ec2_query(
                el, "OrganizationalUnitExclusionSet"
            )
        )
    return out
