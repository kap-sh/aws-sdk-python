"""Generated from Smithy shape ``com.amazonaws.apprunner#VpcDNSTarget``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.app_runner_resource_arn
    import aws_sdk_apprunner.types.domain_name
    import aws_sdk_apprunner.types.string


class VpcDNSTarget(TypedDict):
    vpc_ingress_connection_arn: NotRequired[
        "aws_sdk_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the VPC Ingress Connection that is associated with your service.</p>"""
    vpc_id: NotRequired["aws_sdk_apprunner.types.string.String"]
    """<p>The ID of the Amazon VPC that is associated with the custom domain name of the target DNS.</p>"""
    domain_name: NotRequired["aws_sdk_apprunner.types.domain_name.DomainName"]
    """<p>The domain name of your target DNS that is associated with the Amazon VPC.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcDNSTarget) -> dict:
    out: dict = {}
    if "vpc_ingress_connection_arn" in value:
        out["VpcIngressConnectionArn"] = value["vpc_ingress_connection_arn"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> VpcDNSTarget:
    out: VpcDNSTarget = {}  # type: ignore[typeddict-item]
    if "VpcIngressConnectionArn" in data:
        out["vpc_ingress_connection_arn"] = data["VpcIngressConnectionArn"]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    return out
