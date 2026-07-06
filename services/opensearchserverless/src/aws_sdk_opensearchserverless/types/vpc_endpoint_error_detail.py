"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#VpcEndpointErrorDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.vpc_endpoint_id


class VpcEndpointErrorDetail(TypedDict, closed=True):
    id: NotRequired["aws_sdk_opensearchserverless.types.vpc_endpoint_id.VpcEndpointId"]
    """<p>The unique identifier of the VPC endpoint.</p>"""
    error_message: NotRequired["str"]
    """<p>An error message describing the reason for the failure.</p>"""
    error_code: NotRequired["str"]
    """<p>The error code for the failed request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcEndpointErrorDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    return out


def deserialize_aws_json_1_0(data: dict) -> VpcEndpointErrorDetail:
    out: VpcEndpointErrorDetail = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    return out
