"""Generated from Smithy shape ``com.amazonaws.apprunner#DeleteVpcIngressConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.app_runner_resource_arn


class DeleteVpcIngressConnectionRequest(TypedDict):
    vpc_ingress_connection_arn: (
        "aws_sdk_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the App Runner VPC Ingress Connection that you want to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteVpcIngressConnectionRequest) -> dict:
    out: dict = {}
    out["VpcIngressConnectionArn"] = value["vpc_ingress_connection_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteVpcIngressConnectionRequest:
    out: DeleteVpcIngressConnectionRequest = {}  # type: ignore[typeddict-item]
    if "VpcIngressConnectionArn" in data:
        out["vpc_ingress_connection_arn"] = data["VpcIngressConnectionArn"]
    else:
        raise DeserializationError(
            "DeleteVpcIngressConnectionRequest.vpc_ingress_connection_arn required"
        )
    return out
