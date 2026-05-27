"""Generated from Smithy shape ``com.amazonaws.ec2#IpamAddressHistoryRecord``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

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
