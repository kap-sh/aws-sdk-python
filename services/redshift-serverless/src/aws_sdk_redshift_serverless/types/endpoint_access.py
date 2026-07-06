"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#EndpointAccess``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_redshift_serverless.types.subnet_id_list
    import aws_sdk_redshift_serverless.types.vpc_endpoint
    import aws_sdk_redshift_serverless.types.vpc_security_group_membership_list


class EndpointAccess(TypedDict, closed=True):
    endpoint_name: NotRequired["str"]
    """<p>The name of the VPC endpoint.</p>"""
    endpoint_status: NotRequired["str"]
    """<p>The status of the VPC endpoint.</p>"""
    workgroup_name: NotRequired["str"]
    """<p>The name of the workgroup associated with the endpoint.</p>"""
    endpoint_create_time: NotRequired["datetime.datetime"]
    """<p>The time that the endpoint was created.</p>"""
    port: NotRequired["int"]
    """<p>The port number on which Amazon Redshift Serverless accepts incoming connections.</p>"""
    address: NotRequired["str"]
    """<p>The DNS address of the endpoint.</p>"""
    subnet_ids: NotRequired[
        "aws_sdk_redshift_serverless.types.subnet_id_list.SubnetIdList"
    ]
    """<p>The unique identifier of subnets where Amazon Redshift Serverless choose to deploy the VPC endpoint.</p>"""
    vpc_security_groups: NotRequired[
        "aws_sdk_redshift_serverless.types.vpc_security_group_membership_list.VpcSecurityGroupMembershipList"
    ]
    """<p>The security groups associated with the endpoint.</p>"""
    vpc_endpoint: NotRequired[
        "aws_sdk_redshift_serverless.types.vpc_endpoint.VpcEndpoint"
    ]
    """<p>The connection endpoint for connecting to Amazon Redshift Serverless.</p>"""
    endpoint_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the VPC endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointAccess) -> dict:
    out: dict = {}
    if "endpoint_name" in value:
        out["endpointName"] = value["endpoint_name"]
    if "endpoint_status" in value:
        out["endpointStatus"] = value["endpoint_status"]
    if "workgroup_name" in value:
        out["workgroupName"] = value["workgroup_name"]
    if "endpoint_create_time" in value:
        import aws_sdk_redshift_serverless.types._prelude.timestamp

        out["endpointCreateTime"] = (
            aws_sdk_redshift_serverless.types._prelude.timestamp.serialize_aws_json_1_1(
                value["endpoint_create_time"]
            )
        )
    if "port" in value:
        out["port"] = value["port"]
    if "address" in value:
        out["address"] = value["address"]
    if "subnet_ids" in value:
        import aws_sdk_redshift_serverless.types.subnet_id_list

        out["subnetIds"] = (
            aws_sdk_redshift_serverless.types.subnet_id_list.serialize_aws_json_1_1(
                value["subnet_ids"]
            )
        )
    if "vpc_security_groups" in value:
        import aws_sdk_redshift_serverless.types.vpc_security_group_membership_list

        out["vpcSecurityGroups"] = (
            aws_sdk_redshift_serverless.types.vpc_security_group_membership_list.serialize_aws_json_1_1(
                value["vpc_security_groups"]
            )
        )
    if "vpc_endpoint" in value:
        import aws_sdk_redshift_serverless.types.vpc_endpoint

        out["vpcEndpoint"] = (
            aws_sdk_redshift_serverless.types.vpc_endpoint.serialize_aws_json_1_1(
                value["vpc_endpoint"]
            )
        )
    if "endpoint_arn" in value:
        out["endpointArn"] = value["endpoint_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EndpointAccess:
    out: EndpointAccess = {}  # type: ignore[typeddict-item]
    if "endpointName" in data:
        out["endpoint_name"] = data["endpointName"]
    if "endpointStatus" in data:
        out["endpoint_status"] = data["endpointStatus"]
    if "workgroupName" in data:
        out["workgroup_name"] = data["workgroupName"]
    if "endpointCreateTime" in data:
        import aws_sdk_redshift_serverless.types._prelude.timestamp

        out["endpoint_create_time"] = (
            aws_sdk_redshift_serverless.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["endpointCreateTime"]
            )
        )
    if "port" in data:
        out["port"] = data["port"]
    if "address" in data:
        out["address"] = data["address"]
    if "subnetIds" in data:
        import aws_sdk_redshift_serverless.types.subnet_id_list

        out["subnet_ids"] = (
            aws_sdk_redshift_serverless.types.subnet_id_list.deserialize_aws_json_1_1(
                data["subnetIds"]
            )
        )
    if "vpcSecurityGroups" in data:
        import aws_sdk_redshift_serverless.types.vpc_security_group_membership_list

        out["vpc_security_groups"] = (
            aws_sdk_redshift_serverless.types.vpc_security_group_membership_list.deserialize_aws_json_1_1(
                data["vpcSecurityGroups"]
            )
        )
    if "vpcEndpoint" in data:
        import aws_sdk_redshift_serverless.types.vpc_endpoint

        out["vpc_endpoint"] = (
            aws_sdk_redshift_serverless.types.vpc_endpoint.deserialize_aws_json_1_1(
                data["vpcEndpoint"]
            )
        )
    if "endpointArn" in data:
        out["endpoint_arn"] = data["endpointArn"]
    return out
