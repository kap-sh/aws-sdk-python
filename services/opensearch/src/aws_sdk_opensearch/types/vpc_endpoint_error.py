"""Generated from Smithy shape ``com.amazonaws.opensearch#VpcEndpointError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.string
    import aws_sdk_opensearch.types.vpc_endpoint_error_code
    import aws_sdk_opensearch.types.vpc_endpoint_id


class VpcEndpointError(TypedDict):
    vpc_endpoint_id: NotRequired[
        "aws_sdk_opensearch.types.vpc_endpoint_id.VpcEndpointId"
    ]
    """<p>The unique identifier of the endpoint.</p>"""
    error_code: NotRequired[
        "aws_sdk_opensearch.types.vpc_endpoint_error_code.VpcEndpointErrorCode"
    ]
    """<p>The code associated with the error.</p>"""
    error_message: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>A message describing the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcEndpointError) -> dict:
    out: dict = {}
    if "vpc_endpoint_id" in value:
        out["VpcEndpointId"] = value["vpc_endpoint_id"]
    if "error_code" in value:
        import aws_sdk_opensearch.types.vpc_endpoint_error_code

        out["ErrorCode"] = (
            aws_sdk_opensearch.types.vpc_endpoint_error_code.serialize_json(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> VpcEndpointError:
    out: VpcEndpointError = {}  # type: ignore[typeddict-item]
    if "VpcEndpointId" in data:
        out["vpc_endpoint_id"] = data["VpcEndpointId"]
    if "ErrorCode" in data:
        import aws_sdk_opensearch.types.vpc_endpoint_error_code

        out["error_code"] = (
            aws_sdk_opensearch.types.vpc_endpoint_error_code.deserialize_json(
                data["ErrorCode"]
            )
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
