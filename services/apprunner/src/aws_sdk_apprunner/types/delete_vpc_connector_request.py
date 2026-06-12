"""Generated from Smithy shape ``com.amazonaws.apprunner#DeleteVpcConnectorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.app_runner_resource_arn


class DeleteVpcConnectorRequest(TypedDict):
    vpc_connector_arn: (
        "aws_sdk_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the App Runner VPC connector that you want to delete.</p> <p>The ARN must be a full VPC connector ARN.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteVpcConnectorRequest) -> dict:
    out: dict = {}
    out["VpcConnectorArn"] = value["vpc_connector_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteVpcConnectorRequest:
    out: DeleteVpcConnectorRequest = {}  # type: ignore[typeddict-item]
    if "VpcConnectorArn" in data:
        out["vpc_connector_arn"] = data["VpcConnectorArn"]
    else:
        raise DeserializationError(
            "DeleteVpcConnectorRequest.vpc_connector_arn required"
        )
    return out
