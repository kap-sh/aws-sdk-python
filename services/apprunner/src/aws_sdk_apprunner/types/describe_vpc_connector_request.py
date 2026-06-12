"""Generated from Smithy shape ``com.amazonaws.apprunner#DescribeVpcConnectorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.app_runner_resource_arn


class DescribeVpcConnectorRequest(TypedDict):
    vpc_connector_arn: (
        "aws_sdk_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the App Runner VPC connector that you want a description for.</p> <p>The ARN must be a full VPC connector ARN.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeVpcConnectorRequest) -> dict:
    out: dict = {}
    out["VpcConnectorArn"] = value["vpc_connector_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeVpcConnectorRequest:
    out: DescribeVpcConnectorRequest = {}  # type: ignore[typeddict-item]
    if "VpcConnectorArn" in data:
        out["vpc_connector_arn"] = data["VpcConnectorArn"]
    else:
        raise DeserializationError(
            "DescribeVpcConnectorRequest.vpc_connector_arn required"
        )
    return out
