"""Generated from Smithy shape ``com.amazonaws.ec2#IpamAddressHistoryRecord``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_address_history_resource_type
    import aws_sdk_ec2.types.ipam_compliance_status
    import aws_sdk_ec2.types.ipam_overlap_status
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class IpamAddressHistoryRecord(TypedDict):
    resource_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the resource owner.</p>"""
    resource_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services Region of the resource.</p>"""
    resource_type: NotRequired[
        "aws_sdk_ec2.types.ipam_address_history_resource_type.IpamAddressHistoryResourceType"
    ]
    """<p>The type of the resource.</p>"""
    resource_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the resource.</p>"""
    resource_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The CIDR of the resource.</p>"""
    resource_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the resource.</p>"""
    resource_compliance_status: NotRequired[
        "aws_sdk_ec2.types.ipam_compliance_status.IpamComplianceStatus"
    ]
    """<p>The compliance status of a resource. For more information on compliance statuses, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/monitor-cidr-compliance-ipam.html\">Monitor CIDR usage by resource</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    resource_overlap_status: NotRequired[
        "aws_sdk_ec2.types.ipam_overlap_status.IpamOverlapStatus"
    ]
    """<p>The overlap status of an IPAM resource. The overlap status tells you if the CIDR for a resource overlaps with another CIDR in the scope. For more information on overlap statuses, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/monitor-cidr-compliance-ipam.html\">Monitor CIDR usage by resource</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The VPC ID of the resource.</p>"""
    sampled_start_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>Sampled start time of the resource-to-CIDR association within the IPAM scope. Changes are picked up in periodic snapshots, so the start time may have occurred before this specific time.</p>"""
    sampled_end_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>Sampled end time of the resource-to-CIDR association within the IPAM scope. Changes are picked up in periodic snapshots, so the end time may have occurred before this specific time.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamAddressHistoryRecord, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_owner_id" in value:
        pairs.append((f"{prefix}.ResourceOwnerId", str(value["resource_owner_id"])))
    if "resource_region" in value:
        pairs.append((f"{prefix}.ResourceRegion", str(value["resource_region"])))
    if "resource_type" in value:
        import aws_sdk_ec2.types.ipam_address_history_resource_type

        aws_sdk_ec2.types.ipam_address_history_resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{prefix}.ResourceType"
        )
    if "resource_id" in value:
        pairs.append((f"{prefix}.ResourceId", str(value["resource_id"])))
    if "resource_cidr" in value:
        pairs.append((f"{prefix}.ResourceCidr", str(value["resource_cidr"])))
    if "resource_name" in value:
        pairs.append((f"{prefix}.ResourceName", str(value["resource_name"])))
    if "resource_compliance_status" in value:
        import aws_sdk_ec2.types.ipam_compliance_status

        aws_sdk_ec2.types.ipam_compliance_status.serialize_ec2_query(
            value["resource_compliance_status"],
            pairs,
            f"{prefix}.ResourceComplianceStatus",
        )
    if "resource_overlap_status" in value:
        import aws_sdk_ec2.types.ipam_overlap_status

        aws_sdk_ec2.types.ipam_overlap_status.serialize_ec2_query(
            value["resource_overlap_status"], pairs, f"{prefix}.ResourceOverlapStatus"
        )
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "sampled_start_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["sampled_start_time"], pairs, f"{prefix}.SampledStartTime"
        )
    if "sampled_end_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["sampled_end_time"], pairs, f"{prefix}.SampledEndTime"
        )


def deserialize_ec2_query(el: Element) -> IpamAddressHistoryRecord:
    out: IpamAddressHistoryRecord = {}  # type: ignore[typeddict-item]
    child_resource_owner_id = el.find("ResourceOwnerId")
    if child_resource_owner_id is not None:
        out["resource_owner_id"] = str(child_resource_owner_id.text or "")
    child_resource_region = el.find("ResourceRegion")
    if child_resource_region is not None:
        out["resource_region"] = str(child_resource_region.text or "")
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        import aws_sdk_ec2.types.ipam_address_history_resource_type

        out["resource_type"] = (
            aws_sdk_ec2.types.ipam_address_history_resource_type.deserialize_ec2_query(
                child_resource_type
            )
        )
    child_resource_id = el.find("ResourceId")
    if child_resource_id is not None:
        out["resource_id"] = str(child_resource_id.text or "")
    child_resource_cidr = el.find("ResourceCidr")
    if child_resource_cidr is not None:
        out["resource_cidr"] = str(child_resource_cidr.text or "")
    child_resource_name = el.find("ResourceName")
    if child_resource_name is not None:
        out["resource_name"] = str(child_resource_name.text or "")
    child_resource_compliance_status = el.find("ResourceComplianceStatus")
    if child_resource_compliance_status is not None:
        import aws_sdk_ec2.types.ipam_compliance_status

        out["resource_compliance_status"] = (
            aws_sdk_ec2.types.ipam_compliance_status.deserialize_ec2_query(
                child_resource_compliance_status
            )
        )
    child_resource_overlap_status = el.find("ResourceOverlapStatus")
    if child_resource_overlap_status is not None:
        import aws_sdk_ec2.types.ipam_overlap_status

        out["resource_overlap_status"] = (
            aws_sdk_ec2.types.ipam_overlap_status.deserialize_ec2_query(
                child_resource_overlap_status
            )
        )
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_sampled_start_time = el.find("SampledStartTime")
    if child_sampled_start_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["sampled_start_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_sampled_start_time
            )
        )
    child_sampled_end_time = el.find("SampledEndTime")
    if child_sampled_end_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["sampled_end_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_sampled_end_time
            )
        )
    return out
