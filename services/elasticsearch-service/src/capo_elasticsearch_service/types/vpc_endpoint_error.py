"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#VpcEndpointError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.string
    import capo_elasticsearch_service.types.vpc_endpoint_error_code
    import capo_elasticsearch_service.types.vpc_endpoint_id


class VpcEndpointError(TypedDict, closed=True):
    vpc_endpoint_id: NotRequired[
        "capo_elasticsearch_service.types.vpc_endpoint_id.VpcEndpointId"
    ]
    """<p>The unique identifier of the endpoint. </p>"""
    error_code: NotRequired[
        "capo_elasticsearch_service.types.vpc_endpoint_error_code.VpcEndpointErrorCode"
    ]
    """<p>The code associated with the error.</p>"""
    error_message: NotRequired["capo_elasticsearch_service.types.string.String"]
    """<p>A message describing the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcEndpointError) -> dict:
    out: dict = {}
    if "vpc_endpoint_id" in value:
        out["VpcEndpointId"] = value["vpc_endpoint_id"]
    if "error_code" in value:
        import capo_elasticsearch_service.types.vpc_endpoint_error_code

        out["ErrorCode"] = (
            capo_elasticsearch_service.types.vpc_endpoint_error_code.serialize_json(
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
        import capo_elasticsearch_service.types.vpc_endpoint_error_code

        out["error_code"] = (
            capo_elasticsearch_service.types.vpc_endpoint_error_code.deserialize_json(
                data["ErrorCode"]
            )
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
