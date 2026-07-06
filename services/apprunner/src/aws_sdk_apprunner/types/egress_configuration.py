"""Generated from Smithy shape ``com.amazonaws.apprunner#EgressConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.app_runner_resource_arn
    import aws_sdk_apprunner.types.egress_type


class EgressConfiguration(TypedDict, closed=True):
    egress_type: NotRequired["aws_sdk_apprunner.types.egress_type.EgressType"]
    """<p>The type of egress configuration.</p> <p>Set to <code>DEFAULT</code> for access to resources hosted on public networks.</p> <p>Set to <code>VPC</code> to associate your service to a custom VPC specified by <code>VpcConnectorArn</code>.</p>"""
    vpc_connector_arn: NotRequired[
        "aws_sdk_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the App Runner VPC connector that you want to associate with your App Runner service. Only valid when <code>EgressType = VPC</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EgressConfiguration) -> dict:
    out: dict = {}
    if "egress_type" in value:
        import aws_sdk_apprunner.types.egress_type

        out["EgressType"] = aws_sdk_apprunner.types.egress_type.serialize_aws_json_1_0(
            value["egress_type"]
        )
    if "vpc_connector_arn" in value:
        out["VpcConnectorArn"] = value["vpc_connector_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EgressConfiguration:
    out: EgressConfiguration = {}  # type: ignore[typeddict-item]
    if "EgressType" in data:
        import aws_sdk_apprunner.types.egress_type

        out["egress_type"] = (
            aws_sdk_apprunner.types.egress_type.deserialize_aws_json_1_0(
                data["EgressType"]
            )
        )
    if "VpcConnectorArn" in data:
        out["vpc_connector_arn"] = data["VpcConnectorArn"]
    return out
