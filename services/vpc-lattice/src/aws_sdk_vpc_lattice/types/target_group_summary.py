"""Generated from Smithy shape ``com.amazonaws.vpclattice#TargetGroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.ip_address_type
    import aws_sdk_vpc_lattice.types.lambda_event_structure_version
    import aws_sdk_vpc_lattice.types.port
    import aws_sdk_vpc_lattice.types.service_arn_list
    import aws_sdk_vpc_lattice.types.target_group_arn
    import aws_sdk_vpc_lattice.types.target_group_id
    import aws_sdk_vpc_lattice.types.target_group_name
    import aws_sdk_vpc_lattice.types.target_group_protocol
    import aws_sdk_vpc_lattice.types.target_group_status
    import aws_sdk_vpc_lattice.types.target_group_type
    import aws_sdk_vpc_lattice.types.timestamp
    import aws_sdk_vpc_lattice.types.vpc_id


class TargetGroupSummary(TypedDict, closed=True):
    id: NotRequired["aws_sdk_vpc_lattice.types.target_group_id.TargetGroupId"]
    """<p>The ID of the target group.</p>"""
    arn: NotRequired["aws_sdk_vpc_lattice.types.target_group_arn.TargetGroupArn"]
    """<p>The ARN (Amazon Resource Name) of the target group.</p>"""
    name: NotRequired["aws_sdk_vpc_lattice.types.target_group_name.TargetGroupName"]
    """<p>The name of the target group.</p>"""
    type: NotRequired["aws_sdk_vpc_lattice.types.target_group_type.TargetGroupType"]
    """<p>The target group type.</p>"""
    created_at: NotRequired["aws_sdk_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the target group was created, in ISO-8601 format.</p>"""
    port: NotRequired["aws_sdk_vpc_lattice.types.port.Port"]
    """<p>The port of the target group.</p>"""
    protocol: NotRequired[
        "aws_sdk_vpc_lattice.types.target_group_protocol.TargetGroupProtocol"
    ]
    """<p>The protocol of the target group.</p>"""
    ip_address_type: NotRequired[
        "aws_sdk_vpc_lattice.types.ip_address_type.IpAddressType"
    ]
    """<p>The type of IP address used for the target group. The possible values are <code>IPV4</code> and <code>IPV6</code>. This is an optional parameter. If not specified, the default is <code>IPV4</code>.</p>"""
    vpc_identifier: NotRequired["aws_sdk_vpc_lattice.types.vpc_id.VpcId"]
    """<p>The ID of the VPC of the target group.</p>"""
    last_updated_at: NotRequired["aws_sdk_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the target group was last updated, in ISO-8601 format.</p>"""
    status: NotRequired[
        "aws_sdk_vpc_lattice.types.target_group_status.TargetGroupStatus"
    ]
    """<p>The status.</p>"""
    service_arns: NotRequired[
        "aws_sdk_vpc_lattice.types.service_arn_list.ServiceArnList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the service.</p>"""
    lambda_event_structure_version: NotRequired[
        "aws_sdk_vpc_lattice.types.lambda_event_structure_version.LambdaEventStructureVersion"
    ]
    """<p>The version of the event structure that your Lambda function receives. Supported only if the target group type is <code>LAMBDA</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetGroupSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        out["type"] = value["type"]
    if "created_at" in value:
        import aws_sdk_vpc_lattice.types.timestamp

        out["createdAt"] = aws_sdk_vpc_lattice.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "port" in value:
        out["port"] = value["port"]
    if "protocol" in value:
        out["protocol"] = value["protocol"]
    if "ip_address_type" in value:
        out["ipAddressType"] = value["ip_address_type"]
    if "vpc_identifier" in value:
        out["vpcIdentifier"] = value["vpc_identifier"]
    if "last_updated_at" in value:
        import aws_sdk_vpc_lattice.types.timestamp

        out["lastUpdatedAt"] = aws_sdk_vpc_lattice.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "status" in value:
        out["status"] = value["status"]
    if "service_arns" in value:
        import aws_sdk_vpc_lattice.types.service_arn_list

        out["serviceArns"] = aws_sdk_vpc_lattice.types.service_arn_list.serialize_json(
            value["service_arns"]
        )
    if "lambda_event_structure_version" in value:
        out["lambdaEventStructureVersion"] = value["lambda_event_structure_version"]
    return out


def deserialize_json(data: dict) -> TargetGroupSummary:
    out: TargetGroupSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        out["type"] = data["type"]
    if "createdAt" in data:
        import aws_sdk_vpc_lattice.types.timestamp

        out["created_at"] = aws_sdk_vpc_lattice.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "port" in data:
        out["port"] = data["port"]
    if "protocol" in data:
        out["protocol"] = data["protocol"]
    if "ipAddressType" in data:
        out["ip_address_type"] = data["ipAddressType"]
    if "vpcIdentifier" in data:
        out["vpc_identifier"] = data["vpcIdentifier"]
    if "lastUpdatedAt" in data:
        import aws_sdk_vpc_lattice.types.timestamp

        out["last_updated_at"] = aws_sdk_vpc_lattice.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "status" in data:
        out["status"] = data["status"]
    if "serviceArns" in data:
        import aws_sdk_vpc_lattice.types.service_arn_list

        out["service_arns"] = (
            aws_sdk_vpc_lattice.types.service_arn_list.deserialize_json(
                data["serviceArns"]
            )
        )
    if "lambdaEventStructureVersion" in data:
        out["lambda_event_structure_version"] = data["lambdaEventStructureVersion"]
    return out
