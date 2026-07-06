"""Generated from Smithy shape ``com.amazonaws.apprunner#VpcIngressConnectionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.app_runner_resource_arn


class VpcIngressConnectionSummary(TypedDict, closed=True):
    vpc_ingress_connection_arn: NotRequired[
        "aws_sdk_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the VPC Ingress Connection. </p>"""
    service_arn: NotRequired[
        "aws_sdk_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the service associated with the VPC Ingress Connection. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcIngressConnectionSummary) -> dict:
    out: dict = {}
    if "vpc_ingress_connection_arn" in value:
        out["VpcIngressConnectionArn"] = value["vpc_ingress_connection_arn"]
    if "service_arn" in value:
        out["ServiceArn"] = value["service_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> VpcIngressConnectionSummary:
    out: VpcIngressConnectionSummary = {}  # type: ignore[typeddict-item]
    if "VpcIngressConnectionArn" in data:
        out["vpc_ingress_connection_arn"] = data["VpcIngressConnectionArn"]
    if "ServiceArn" in data:
        out["service_arn"] = data["ServiceArn"]
    return out
