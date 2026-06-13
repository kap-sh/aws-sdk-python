"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateVPCConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.dns_resolver_list
    import aws_sdk_quicksight.types.resource_name
    import aws_sdk_quicksight.types.role_arn
    import aws_sdk_quicksight.types.security_group_id_list
    import aws_sdk_quicksight.types.subnet_id_list
    import aws_sdk_quicksight.types.vpc_connection_resource_id_unrestricted


class UpdateVPCConnectionRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID of the account that contains the VPC connection that you want to update.</p>"""
    vpc_connection_id: "aws_sdk_quicksight.types.vpc_connection_resource_id_unrestricted.VPCConnectionResourceIdUnrestricted"
    """<p>The ID of the VPC connection that you're updating. This ID is a unique identifier for each Amazon Web Services Region in an Amazon Web Services account.</p>"""
    name: "aws_sdk_quicksight.types.resource_name.ResourceName"
    """<p>The display name for the VPC connection.</p>"""
    subnet_ids: "aws_sdk_quicksight.types.subnet_id_list.SubnetIdList"
    """<p>A list of subnet IDs for the VPC connection.</p>"""
    security_group_ids: (
        "aws_sdk_quicksight.types.security_group_id_list.SecurityGroupIdList"
    )
    """<p>A list of security group IDs for the VPC connection.</p>"""
    dns_resolvers: NotRequired[
        "aws_sdk_quicksight.types.dns_resolver_list.DnsResolverList"
    ]
    """<p>A list of IP addresses of DNS resolver endpoints for the VPC connection.</p>"""
    role_arn: "aws_sdk_quicksight.types.role_arn.RoleArn"
    """<p>An IAM role associated with the VPC connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVPCConnectionRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_quicksight.types.subnet_id_list

    out["SubnetIds"] = aws_sdk_quicksight.types.subnet_id_list.serialize_json(
        value["subnet_ids"]
    )
    import aws_sdk_quicksight.types.security_group_id_list

    out["SecurityGroupIds"] = (
        aws_sdk_quicksight.types.security_group_id_list.serialize_json(
            value["security_group_ids"]
        )
    )
    if "dns_resolvers" in value:
        import aws_sdk_quicksight.types.dns_resolver_list

        out["DnsResolvers"] = aws_sdk_quicksight.types.dns_resolver_list.serialize_json(
            value["dns_resolvers"]
        )
    out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> UpdateVPCConnectionRequest:
    out: UpdateVPCConnectionRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateVPCConnectionRequest.name required")
    if "SubnetIds" in data:
        import aws_sdk_quicksight.types.subnet_id_list

        out["subnet_ids"] = aws_sdk_quicksight.types.subnet_id_list.deserialize_json(
            data["SubnetIds"]
        )
    else:
        raise DeserializationError("UpdateVPCConnectionRequest.subnet_ids required")
    if "SecurityGroupIds" in data:
        import aws_sdk_quicksight.types.security_group_id_list

        out["security_group_ids"] = (
            aws_sdk_quicksight.types.security_group_id_list.deserialize_json(
                data["SecurityGroupIds"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateVPCConnectionRequest.security_group_ids required"
        )
    if "DnsResolvers" in data:
        import aws_sdk_quicksight.types.dns_resolver_list

        out["dns_resolvers"] = (
            aws_sdk_quicksight.types.dns_resolver_list.deserialize_json(
                data["DnsResolvers"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("UpdateVPCConnectionRequest.role_arn required")
    return out
