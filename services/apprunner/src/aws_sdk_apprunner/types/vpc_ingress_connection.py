"""Generated from Smithy shape ``com.amazonaws.apprunner#VpcIngressConnection``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.app_runner_resource_arn
    import aws_sdk_apprunner.types.customer_account_id
    import aws_sdk_apprunner.types.domain_name
    import aws_sdk_apprunner.types.ingress_vpc_configuration
    import aws_sdk_apprunner.types.timestamp
    import aws_sdk_apprunner.types.vpc_ingress_connection_name
    import aws_sdk_apprunner.types.vpc_ingress_connection_status


class VpcIngressConnection(TypedDict):
    vpc_ingress_connection_arn: NotRequired[
        "aws_sdk_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the VPC Ingress Connection. </p>"""
    vpc_ingress_connection_name: NotRequired[
        "aws_sdk_apprunner.types.vpc_ingress_connection_name.VpcIngressConnectionName"
    ]
    """<p>The customer-provided VPC Ingress Connection name.</p>"""
    service_arn: NotRequired[
        "aws_sdk_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the service associated with the VPC Ingress Connection. </p>"""
    status: NotRequired[
        "aws_sdk_apprunner.types.vpc_ingress_connection_status.VpcIngressConnectionStatus"
    ]
    """<p>The current status of the VPC Ingress Connection. The VPC Ingress Connection displays one of the following statuses: <code>AVAILABLE</code>, <code>PENDING_CREATION</code>, <code>PENDING_UPDATE</code>, <code>PENDING_DELETION</code>,<code>FAILED_CREATION</code>, <code>FAILED_UPDATE</code>, <code>FAILED_DELETION</code>, and <code>DELETED</code>.. </p>"""
    account_id: NotRequired[
        "aws_sdk_apprunner.types.customer_account_id.CustomerAccountId"
    ]
    """<p>The Account Id you use to create the VPC Ingress Connection resource.</p>"""
    domain_name: NotRequired["aws_sdk_apprunner.types.domain_name.DomainName"]
    """<p>The domain name associated with the VPC Ingress Connection resource.</p>"""
    ingress_vpc_configuration: NotRequired[
        "aws_sdk_apprunner.types.ingress_vpc_configuration.IngressVpcConfiguration"
    ]
    """<p>Specifications for the customer’s VPC and related PrivateLink VPC endpoint that are used to associate with the VPC Ingress Connection resource.</p>"""
    created_at: NotRequired["aws_sdk_apprunner.types.timestamp.Timestamp"]
    """<p>The time when the VPC Ingress Connection was created. It's in the Unix time stamp format.</p> <ul> <li> <p> Type: Timestamp </p> </li> <li> <p> Required: Yes </p> </li> </ul>"""
    deleted_at: NotRequired["aws_sdk_apprunner.types.timestamp.Timestamp"]
    """<p>The time when the App Runner service was deleted. It's in the Unix time stamp format.</p> <ul> <li> <p> Type: Timestamp </p> </li> <li> <p> Required: No </p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcIngressConnection) -> dict:
    out: dict = {}
    if "vpc_ingress_connection_arn" in value:
        out["VpcIngressConnectionArn"] = value["vpc_ingress_connection_arn"]
    if "vpc_ingress_connection_name" in value:
        out["VpcIngressConnectionName"] = value["vpc_ingress_connection_name"]
    if "service_arn" in value:
        out["ServiceArn"] = value["service_arn"]
    if "status" in value:
        import aws_sdk_apprunner.types.vpc_ingress_connection_status

        out["Status"] = (
            aws_sdk_apprunner.types.vpc_ingress_connection_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "ingress_vpc_configuration" in value:
        import aws_sdk_apprunner.types.ingress_vpc_configuration

        out["IngressVpcConfiguration"] = (
            aws_sdk_apprunner.types.ingress_vpc_configuration.serialize_aws_json_1_0(
                value["ingress_vpc_configuration"]
            )
        )
    if "created_at" in value:
        import aws_sdk_apprunner.types.timestamp

        out["CreatedAt"] = aws_sdk_apprunner.types.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "deleted_at" in value:
        import aws_sdk_apprunner.types.timestamp

        out["DeletedAt"] = aws_sdk_apprunner.types.timestamp.serialize_aws_json_1_0(
            value["deleted_at"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> VpcIngressConnection:
    out: VpcIngressConnection = {}  # type: ignore[typeddict-item]
    if "VpcIngressConnectionArn" in data:
        out["vpc_ingress_connection_arn"] = data["VpcIngressConnectionArn"]
    if "VpcIngressConnectionName" in data:
        out["vpc_ingress_connection_name"] = data["VpcIngressConnectionName"]
    if "ServiceArn" in data:
        out["service_arn"] = data["ServiceArn"]
    if "Status" in data:
        import aws_sdk_apprunner.types.vpc_ingress_connection_status

        out["status"] = (
            aws_sdk_apprunner.types.vpc_ingress_connection_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "IngressVpcConfiguration" in data:
        import aws_sdk_apprunner.types.ingress_vpc_configuration

        out["ingress_vpc_configuration"] = (
            aws_sdk_apprunner.types.ingress_vpc_configuration.deserialize_aws_json_1_0(
                data["IngressVpcConfiguration"]
            )
        )
    if "CreatedAt" in data:
        import aws_sdk_apprunner.types.timestamp

        out["created_at"] = aws_sdk_apprunner.types.timestamp.deserialize_aws_json_1_0(
            data["CreatedAt"]
        )
    if "DeletedAt" in data:
        import aws_sdk_apprunner.types.timestamp

        out["deleted_at"] = aws_sdk_apprunner.types.timestamp.deserialize_aws_json_1_0(
            data["DeletedAt"]
        )
    return out
