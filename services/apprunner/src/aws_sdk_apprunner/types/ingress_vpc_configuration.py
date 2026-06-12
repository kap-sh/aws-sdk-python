"""Generated from Smithy shape ``com.amazonaws.apprunner#IngressVpcConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.string


class IngressVpcConfiguration(TypedDict):
    vpc_id: NotRequired["aws_sdk_apprunner.types.string.String"]
    """<p>The ID of the VPC that is used for the VPC endpoint.</p>"""
    vpc_endpoint_id: NotRequired["aws_sdk_apprunner.types.string.String"]
    """<p>The ID of the VPC endpoint that your App Runner service connects to. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressVpcConfiguration) -> dict:
    out: dict = {}
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "vpc_endpoint_id" in value:
        out["VpcEndpointId"] = value["vpc_endpoint_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> IngressVpcConfiguration:
    out: IngressVpcConfiguration = {}  # type: ignore[typeddict-item]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "VpcEndpointId" in data:
        out["vpc_endpoint_id"] = data["VpcEndpointId"]
    return out
