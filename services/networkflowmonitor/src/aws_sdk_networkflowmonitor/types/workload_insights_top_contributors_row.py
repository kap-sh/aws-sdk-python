"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#WorkloadInsightsTopContributorsRow``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.account_id
    import aws_sdk_networkflowmonitor.types.availability_zone
    import aws_sdk_networkflowmonitor.types.aws_region
    import aws_sdk_networkflowmonitor.types.subnet_arn
    import aws_sdk_networkflowmonitor.types.subnet_id
    import aws_sdk_networkflowmonitor.types.vpc_arn
    import aws_sdk_networkflowmonitor.types.vpc_id


class WorkloadInsightsTopContributorsRow(TypedDict):
    account_id: NotRequired["aws_sdk_networkflowmonitor.types.account_id.AccountId"]
    """<p>The account ID for a specific row of data.</p>"""
    local_subnet_id: NotRequired["aws_sdk_networkflowmonitor.types.subnet_id.SubnetId"]
    """<p>The subnet identifier for the local resource.</p>"""
    local_az: NotRequired[
        "aws_sdk_networkflowmonitor.types.availability_zone.AvailabilityZone"
    ]
    """<p>The identifier for the Availability Zone where the local resource is located.</p>"""
    local_vpc_id: NotRequired["aws_sdk_networkflowmonitor.types.vpc_id.VpcId"]
    """<p>The identifier for the VPC for the local resource.</p>"""
    local_region: NotRequired["aws_sdk_networkflowmonitor.types.aws_region.AwsRegion"]
    """<p>The Amazon Web Services Region where the local resource is located.</p>"""
    remote_identifier: NotRequired["str"]
    """<p>The identifier of a remote resource. For a VPC or subnet, this identifier is the VPC Amazon Resource Name (ARN) or subnet ARN. For an Availability Zone, this identifier is the AZ name, for example, us-west-2b. For an Amazon Web Services Region , this identifier is the Region name, for example, us-west-2.</p>"""
    value: NotRequired["int"]
    """<p>The value for a metric.</p>"""
    local_subnet_arn: NotRequired[
        "aws_sdk_networkflowmonitor.types.subnet_arn.SubnetArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a local subnet.</p>"""
    local_vpc_arn: NotRequired["aws_sdk_networkflowmonitor.types.vpc_arn.VpcArn"]
    """<p>The Amazon Resource Name (ARN) of a local VPC.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadInsightsTopContributorsRow) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "local_subnet_id" in value:
        out["localSubnetId"] = value["local_subnet_id"]
    if "local_az" in value:
        out["localAz"] = value["local_az"]
    if "local_vpc_id" in value:
        out["localVpcId"] = value["local_vpc_id"]
    if "local_region" in value:
        out["localRegion"] = value["local_region"]
    if "remote_identifier" in value:
        out["remoteIdentifier"] = value["remote_identifier"]
    if "value" in value:
        out["value"] = value["value"]
    if "local_subnet_arn" in value:
        out["localSubnetArn"] = value["local_subnet_arn"]
    if "local_vpc_arn" in value:
        out["localVpcArn"] = value["local_vpc_arn"]
    return out


def deserialize_json(data: dict) -> WorkloadInsightsTopContributorsRow:
    out: WorkloadInsightsTopContributorsRow = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "localSubnetId" in data:
        out["local_subnet_id"] = data["localSubnetId"]
    if "localAz" in data:
        out["local_az"] = data["localAz"]
    if "localVpcId" in data:
        out["local_vpc_id"] = data["localVpcId"]
    if "localRegion" in data:
        out["local_region"] = data["localRegion"]
    if "remoteIdentifier" in data:
        out["remote_identifier"] = data["remoteIdentifier"]
    if "value" in data:
        out["value"] = data["value"]
    if "localSubnetArn" in data:
        out["local_subnet_arn"] = data["localSubnetArn"]
    if "localVpcArn" in data:
        out["local_vpc_arn"] = data["localVpcArn"]
    return out
