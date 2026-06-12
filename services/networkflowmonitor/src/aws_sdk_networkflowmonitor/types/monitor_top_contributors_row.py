"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#MonitorTopContributorsRow``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.availability_zone
    import aws_sdk_networkflowmonitor.types.aws_region
    import aws_sdk_networkflowmonitor.types.destination_category
    import aws_sdk_networkflowmonitor.types.instance_arn
    import aws_sdk_networkflowmonitor.types.instance_id
    import aws_sdk_networkflowmonitor.types.kubernetes_metadata
    import aws_sdk_networkflowmonitor.types.subnet_arn
    import aws_sdk_networkflowmonitor.types.subnet_id
    import aws_sdk_networkflowmonitor.types.traversed_constructs_list
    import aws_sdk_networkflowmonitor.types.vpc_arn
    import aws_sdk_networkflowmonitor.types.vpc_id

class MonitorTopContributorsRow(TypedDict):
    local_ip: NotRequired["str"]
    """<p>The IP address of the local resource for a top contributor network flow.</p>"""
    snat_ip: NotRequired["str"]
    """<p>The secure network address translation (SNAT) IP address for a top contributor network flow.</p>"""
    local_instance_id: NotRequired["aws_sdk_networkflowmonitor.types.instance_id.InstanceId"]
    """<p>The instance identifier for the local resource for a top contributor network flow.</p>"""
    local_vpc_id: NotRequired["aws_sdk_networkflowmonitor.types.vpc_id.VpcId"]
    """<p>The VPC ID for a top contributor network flow for the local resource.</p>"""
    local_region: NotRequired["aws_sdk_networkflowmonitor.types.aws_region.AwsRegion"]
    """<p>The Amazon Web Services Region for the local resource for a top contributor network flow.</p>"""
    local_az: NotRequired["aws_sdk_networkflowmonitor.types.availability_zone.AvailabilityZone"]
    """<p>The Availability Zone for the local resource for a top contributor network flow.</p>"""
    local_subnet_id: NotRequired["aws_sdk_networkflowmonitor.types.subnet_id.SubnetId"]
    """<p>The subnet ID for the local resource for a top contributor network flow.</p>"""
    target_port: NotRequired["int"]
    """<p>The target port.</p>"""
    destination_category: NotRequired["aws_sdk_networkflowmonitor.types.destination_category.DestinationCategory"]
    """<p>The destination category for a top contributors row. Destination categories can be one of the following: </p> <ul> <li> <p> <code>INTRA_AZ</code>: Top contributor network flows within a single Availability Zone</p> </li> <li> <p> <code>INTER_AZ</code>: Top contributor network flows between Availability Zones</p> </li> <li> <p> <code>INTER_REGION</code>: Top contributor network flows between Regions (to the edge of another Region)</p> </li> <li> <p> <code>INTER_VPC</code>: Top contributor network flows between VPCs</p> </li> <li> <p> <code>AWS_SERVICES</code>: Top contributor network flows to or from Amazon Web Services services</p> </li> <li> <p> <code>UNCLASSIFIED</code>: Top contributor network flows that do not have a bucket classification</p> </li> </ul>"""
    remote_vpc_id: NotRequired["aws_sdk_networkflowmonitor.types.vpc_id.VpcId"]
    """<p>The VPC ID for a top contributor network flow for the remote resource.</p>"""
    remote_region: NotRequired["aws_sdk_networkflowmonitor.types.aws_region.AwsRegion"]
    """<p>The Amazon Web Services Region for the remote resource for a top contributor network flow.</p>"""
    remote_az: NotRequired["aws_sdk_networkflowmonitor.types.availability_zone.AvailabilityZone"]
    """<p>The Availability Zone for the remote resource for a top contributor network flow.</p>"""
    remote_subnet_id: NotRequired["aws_sdk_networkflowmonitor.types.subnet_id.SubnetId"]
    """<p>The subnet ID for the remote resource for a top contributor network flow.</p>"""
    remote_instance_id: NotRequired["aws_sdk_networkflowmonitor.types.instance_id.InstanceId"]
    """<p>The instance identifier for the remote resource for a top contributor network flow.</p>"""
    remote_ip: NotRequired["str"]
    """<p>The IP address of the remote resource for a top contributor network flow.</p>"""
    dnat_ip: NotRequired["str"]
    """<p>The destination network address translation (DNAT) IP address for a top contributor network flow.</p>"""
    value: NotRequired["int"]
    """<p>The value of the metric for a top contributor network flow.</p>"""
    traversed_constructs: NotRequired["aws_sdk_networkflowmonitor.types.traversed_constructs_list.TraversedConstructsList"]
    """<p>The constructs traversed by a network flow.</p>"""
    kubernetes_metadata: NotRequired["aws_sdk_networkflowmonitor.types.kubernetes_metadata.KubernetesMetadata"]
    """<p>Meta data about Kubernetes resources.</p>"""
    local_instance_arn: NotRequired["aws_sdk_networkflowmonitor.types.instance_arn.InstanceArn"]
    """<p>The Amazon Resource Name (ARN) of a local resource.</p>"""
    local_subnet_arn: NotRequired["aws_sdk_networkflowmonitor.types.subnet_arn.SubnetArn"]
    """<p>The Amazon Resource Name (ARN) of a local subnet.</p>"""
    local_vpc_arn: NotRequired["aws_sdk_networkflowmonitor.types.vpc_arn.VpcArn"]
    """<p>The Amazon Resource Name (ARN) of a local VPC.</p>"""
    remote_instance_arn: NotRequired["aws_sdk_networkflowmonitor.types.instance_arn.InstanceArn"]
    """<p>The Amazon Resource Name (ARN) of a remote resource.</p>"""
    remote_subnet_arn: NotRequired["aws_sdk_networkflowmonitor.types.subnet_arn.SubnetArn"]
    """<p>The Amazon Resource Name (ARN) of a remote subnet.</p>"""
    remote_vpc_arn: NotRequired["aws_sdk_networkflowmonitor.types.vpc_arn.VpcArn"]
    """<p>The Amazon Resource Name (ARN) of a remote VPC.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: MonitorTopContributorsRow) -> dict:
    out: dict = {}
    if "local_ip" in value:
        out["localIp"] = value["local_ip"]
    if "snat_ip" in value:
        out["snatIp"] = value["snat_ip"]
    if "local_instance_id" in value:
        out["localInstanceId"] = value["local_instance_id"]
    if "local_vpc_id" in value:
        out["localVpcId"] = value["local_vpc_id"]
    if "local_region" in value:
        out["localRegion"] = value["local_region"]
    if "local_az" in value:
        out["localAz"] = value["local_az"]
    if "local_subnet_id" in value:
        out["localSubnetId"] = value["local_subnet_id"]
    if "target_port" in value:
        out["targetPort"] = value["target_port"]
    if "destination_category" in value:
        import aws_sdk_networkflowmonitor.types.destination_category
        out["destinationCategory"] = aws_sdk_networkflowmonitor.types.destination_category.serialize_json(value["destination_category"])
    if "remote_vpc_id" in value:
        out["remoteVpcId"] = value["remote_vpc_id"]
    if "remote_region" in value:
        out["remoteRegion"] = value["remote_region"]
    if "remote_az" in value:
        out["remoteAz"] = value["remote_az"]
    if "remote_subnet_id" in value:
        out["remoteSubnetId"] = value["remote_subnet_id"]
    if "remote_instance_id" in value:
        out["remoteInstanceId"] = value["remote_instance_id"]
    if "remote_ip" in value:
        out["remoteIp"] = value["remote_ip"]
    if "dnat_ip" in value:
        out["dnatIp"] = value["dnat_ip"]
    if "value" in value:
        out["value"] = value["value"]
    if "traversed_constructs" in value:
        import aws_sdk_networkflowmonitor.types.traversed_constructs_list
        out["traversedConstructs"] = aws_sdk_networkflowmonitor.types.traversed_constructs_list.serialize_json(value["traversed_constructs"])
    if "kubernetes_metadata" in value:
        import aws_sdk_networkflowmonitor.types.kubernetes_metadata
        out["kubernetesMetadata"] = aws_sdk_networkflowmonitor.types.kubernetes_metadata.serialize_json(value["kubernetes_metadata"])
    if "local_instance_arn" in value:
        out["localInstanceArn"] = value["local_instance_arn"]
    if "local_subnet_arn" in value:
        out["localSubnetArn"] = value["local_subnet_arn"]
    if "local_vpc_arn" in value:
        out["localVpcArn"] = value["local_vpc_arn"]
    if "remote_instance_arn" in value:
        out["remoteInstanceArn"] = value["remote_instance_arn"]
    if "remote_subnet_arn" in value:
        out["remoteSubnetArn"] = value["remote_subnet_arn"]
    if "remote_vpc_arn" in value:
        out["remoteVpcArn"] = value["remote_vpc_arn"]
    return out


def deserialize_json(data: dict) -> MonitorTopContributorsRow:
    out: MonitorTopContributorsRow = {}  # type: ignore[typeddict-item]
    if "localIp" in data:
        out["local_ip"] = data["localIp"]
    if "snatIp" in data:
        out["snat_ip"] = data["snatIp"]
    if "localInstanceId" in data:
        out["local_instance_id"] = data["localInstanceId"]
    if "localVpcId" in data:
        out["local_vpc_id"] = data["localVpcId"]
    if "localRegion" in data:
        out["local_region"] = data["localRegion"]
    if "localAz" in data:
        out["local_az"] = data["localAz"]
    if "localSubnetId" in data:
        out["local_subnet_id"] = data["localSubnetId"]
    if "targetPort" in data:
        out["target_port"] = data["targetPort"]
    if "destinationCategory" in data:
        import aws_sdk_networkflowmonitor.types.destination_category
        out["destination_category"] = aws_sdk_networkflowmonitor.types.destination_category.deserialize_json(data["destinationCategory"])
    if "remoteVpcId" in data:
        out["remote_vpc_id"] = data["remoteVpcId"]
    if "remoteRegion" in data:
        out["remote_region"] = data["remoteRegion"]
    if "remoteAz" in data:
        out["remote_az"] = data["remoteAz"]
    if "remoteSubnetId" in data:
        out["remote_subnet_id"] = data["remoteSubnetId"]
    if "remoteInstanceId" in data:
        out["remote_instance_id"] = data["remoteInstanceId"]
    if "remoteIp" in data:
        out["remote_ip"] = data["remoteIp"]
    if "dnatIp" in data:
        out["dnat_ip"] = data["dnatIp"]
    if "value" in data:
        out["value"] = data["value"]
    if "traversedConstructs" in data:
        import aws_sdk_networkflowmonitor.types.traversed_constructs_list
        out["traversed_constructs"] = aws_sdk_networkflowmonitor.types.traversed_constructs_list.deserialize_json(data["traversedConstructs"])
    if "kubernetesMetadata" in data:
        import aws_sdk_networkflowmonitor.types.kubernetes_metadata
        out["kubernetes_metadata"] = aws_sdk_networkflowmonitor.types.kubernetes_metadata.deserialize_json(data["kubernetesMetadata"])
    if "localInstanceArn" in data:
        out["local_instance_arn"] = data["localInstanceArn"]
    if "localSubnetArn" in data:
        out["local_subnet_arn"] = data["localSubnetArn"]
    if "localVpcArn" in data:
        out["local_vpc_arn"] = data["localVpcArn"]
    if "remoteInstanceArn" in data:
        out["remote_instance_arn"] = data["remoteInstanceArn"]
    if "remoteSubnetArn" in data:
        out["remote_subnet_arn"] = data["remoteSubnetArn"]
    if "remoteVpcArn" in data:
        out["remote_vpc_arn"] = data["remoteVpcArn"]
    return out