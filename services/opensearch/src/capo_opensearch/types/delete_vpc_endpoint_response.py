"""Generated from Smithy shape ``com.amazonaws.opensearch#DeleteVpcEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.vpc_endpoint_summary


class DeleteVpcEndpointResponse(TypedDict, closed=True):
    vpc_endpoint_summary: (
        "capo_opensearch.types.vpc_endpoint_summary.VpcEndpointSummary"
    )
    """<p>Information about the deleted endpoint, including its current status (<code>DELETING</code> or <code>DELETE_FAILED</code>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVpcEndpointResponse) -> dict:
    out: dict = {}
    import capo_opensearch.types.vpc_endpoint_summary

    out["VpcEndpointSummary"] = (
        capo_opensearch.types.vpc_endpoint_summary.serialize_json(
            value["vpc_endpoint_summary"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteVpcEndpointResponse:
    out: DeleteVpcEndpointResponse = {}  # type: ignore[typeddict-item]
    if "VpcEndpointSummary" in data:
        import capo_opensearch.types.vpc_endpoint_summary

        out["vpc_endpoint_summary"] = (
            capo_opensearch.types.vpc_endpoint_summary.deserialize_json(
                data["VpcEndpointSummary"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteVpcEndpointResponse.vpc_endpoint_summary required"
        )
    return out
