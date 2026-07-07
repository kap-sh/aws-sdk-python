"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CustomRoutingEndpointConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.generic_string


class CustomRoutingEndpointConfiguration(TypedDict, closed=True):
    endpoint_id: NotRequired[
        "aws_sdk_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>An ID for the endpoint. For custom routing accelerators, this is the virtual private cloud (VPC) subnet ID. </p>"""
    attachment_arn: NotRequired[
        "aws_sdk_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The Amazon Resource Name (ARN) of the cross-account attachment that specifies the endpoints (resources) that can be added to accelerators and principals that have permission to add the endpoints.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomRoutingEndpointConfiguration) -> dict:
    out: dict = {}
    if "endpoint_id" in value:
        out["EndpointId"] = value["endpoint_id"]
    if "attachment_arn" in value:
        out["AttachmentArn"] = value["attachment_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomRoutingEndpointConfiguration:
    out: CustomRoutingEndpointConfiguration = {}  # type: ignore[typeddict-item]
    if "EndpointId" in data:
        out["endpoint_id"] = data["EndpointId"]
    if "AttachmentArn" in data:
        out["attachment_arn"] = data["AttachmentArn"]
    return out
