"""Generated from Smithy shape ``com.amazonaws.emr#Instance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.ebs_volume_list
    import aws_sdk_emr.types.instance_fleet_id
    import aws_sdk_emr.types.instance_id
    import aws_sdk_emr.types.instance_status
    import aws_sdk_emr.types.instance_type
    import aws_sdk_emr.types.market_type
    import aws_sdk_emr.types.string


class Instance(TypedDict, closed=True):
    id: NotRequired["aws_sdk_emr.types.instance_id.InstanceId"]
    """<p>The unique identifier for the instance in Amazon EMR.</p>"""
    ec2_instance_id: NotRequired["aws_sdk_emr.types.instance_id.InstanceId"]
    """<p>The unique identifier of the instance in Amazon EC2.</p>"""
    public_dns_name: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The public DNS name of the instance.</p>"""
    public_ip_address: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The public IP address of the instance.</p>"""
    private_dns_name: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The private DNS name of the instance.</p>"""
    private_ip_address: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The private IP address of the instance.</p>"""
    status: NotRequired["aws_sdk_emr.types.instance_status.InstanceStatus"]
    """<p>The current status of the instance.</p>"""
    instance_group_id: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The identifier of the instance group to which this instance belongs.</p>"""
    instance_fleet_id: NotRequired[
        "aws_sdk_emr.types.instance_fleet_id.InstanceFleetId"
    ]
    """<p>The unique identifier of the instance fleet to which an Amazon EC2 instance belongs.</p>"""
    market: NotRequired["aws_sdk_emr.types.market_type.MarketType"]
    """<p>The instance purchasing option. Valid values are <code>ON_DEMAND</code> or <code>SPOT</code>. </p>"""
    instance_type: NotRequired["aws_sdk_emr.types.instance_type.InstanceType"]
    """<p>The Amazon EC2 instance type, for example <code>m3.xlarge</code>.</p>"""
    ebs_volumes: NotRequired["aws_sdk_emr.types.ebs_volume_list.EbsVolumeList"]
    """<p>The list of Amazon EBS volumes that are attached to this instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Instance) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "ec2_instance_id" in value:
        out["Ec2InstanceId"] = value["ec2_instance_id"]
    if "public_dns_name" in value:
        out["PublicDnsName"] = value["public_dns_name"]
    if "public_ip_address" in value:
        out["PublicIpAddress"] = value["public_ip_address"]
    if "private_dns_name" in value:
        out["PrivateDnsName"] = value["private_dns_name"]
    if "private_ip_address" in value:
        out["PrivateIpAddress"] = value["private_ip_address"]
    if "status" in value:
        import aws_sdk_emr.types.instance_status

        out["Status"] = aws_sdk_emr.types.instance_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "instance_group_id" in value:
        out["InstanceGroupId"] = value["instance_group_id"]
    if "instance_fleet_id" in value:
        out["InstanceFleetId"] = value["instance_fleet_id"]
    if "market" in value:
        import aws_sdk_emr.types.market_type

        out["Market"] = aws_sdk_emr.types.market_type.serialize_aws_json_1_1(
            value["market"]
        )
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "ebs_volumes" in value:
        import aws_sdk_emr.types.ebs_volume_list

        out["EbsVolumes"] = aws_sdk_emr.types.ebs_volume_list.serialize_aws_json_1_1(
            value["ebs_volumes"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Instance:
    out: Instance = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Ec2InstanceId" in data:
        out["ec2_instance_id"] = data["Ec2InstanceId"]
    if "PublicDnsName" in data:
        out["public_dns_name"] = data["PublicDnsName"]
    if "PublicIpAddress" in data:
        out["public_ip_address"] = data["PublicIpAddress"]
    if "PrivateDnsName" in data:
        out["private_dns_name"] = data["PrivateDnsName"]
    if "PrivateIpAddress" in data:
        out["private_ip_address"] = data["PrivateIpAddress"]
    if "Status" in data:
        import aws_sdk_emr.types.instance_status

        out["status"] = aws_sdk_emr.types.instance_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "InstanceGroupId" in data:
        out["instance_group_id"] = data["InstanceGroupId"]
    if "InstanceFleetId" in data:
        out["instance_fleet_id"] = data["InstanceFleetId"]
    if "Market" in data:
        import aws_sdk_emr.types.market_type

        out["market"] = aws_sdk_emr.types.market_type.deserialize_aws_json_1_1(
            data["Market"]
        )
    if "InstanceType" in data:
        out["instance_type"] = data["InstanceType"]
    if "EbsVolumes" in data:
        import aws_sdk_emr.types.ebs_volume_list

        out["ebs_volumes"] = aws_sdk_emr.types.ebs_volume_list.deserialize_aws_json_1_1(
            data["EbsVolumes"]
        )
    return out
