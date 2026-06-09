"""Generated from Smithy shape ``com.amazonaws.ec2#CreateIpamResourceDiscoveryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.add_ipam_operating_region_set
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class CreateIpamResourceDiscoveryRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the IPAM resource discovery.</p>"""
    operating_regions: NotRequired[
        "aws_sdk_ec2.types.add_ipam_operating_region_set.AddIpamOperatingRegionSet"
    ]
    """<p>Operating Regions for the IPAM resource discovery. Operating Regions are Amazon Web Services Regions where the IPAM is allowed to manage IP address CIDRs. IPAM only discovers and monitors resources in the Amazon Web Services Regions you select as operating Regions.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>Tag specifications for the IPAM resource discovery.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A client token for the IPAM resource discovery.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateIpamResourceDiscoveryRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "operating_regions" in value:
        import aws_sdk_ec2.types.add_ipam_operating_region_set

        aws_sdk_ec2.types.add_ipam_operating_region_set.serialize_ec2_query(
            value["operating_regions"], pairs, f"{prefix}.OperatingRegions"
        )
    if "tag_specifications" in value:
        import aws_sdk_ec2.types.tag_specification_list

        aws_sdk_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> CreateIpamResourceDiscoveryRequest:
    out: CreateIpamResourceDiscoveryRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    if el.find("OperatingRegions") is not None:
        import aws_sdk_ec2.types.add_ipam_operating_region_set

        out["operating_regions"] = (
            aws_sdk_ec2.types.add_ipam_operating_region_set.deserialize_ec2_query(
                el, "OperatingRegions"
            )
        )
    if el.find("TagSpecifications") is not None:
        import aws_sdk_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            aws_sdk_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
