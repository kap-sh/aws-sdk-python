"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ListCustomRoutingPortMappingsByDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import capo_global_accelerator.types.generic_string
    import capo_global_accelerator.types.port_mappings_max_results


class ListCustomRoutingPortMappingsByDestinationRequest(TypedDict, closed=True):
    endpoint_id: "capo_global_accelerator.types.generic_string.GenericString"
    """<p>The ID for the virtual private cloud (VPC) subnet.</p>"""
    destination_address: "capo_global_accelerator.types.generic_string.GenericString"
    """<p>The endpoint IP address in a virtual private cloud (VPC) subnet for which you want to receive back port mappings.</p>"""
    max_results: NotRequired[
        "capo_global_accelerator.types.port_mappings_max_results.PortMappingsMaxResults"
    ]
    """<p>The number of destination port mappings that you want to return with this call. The default value is 10.</p>"""
    next_token: NotRequired[
        "capo_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListCustomRoutingPortMappingsByDestinationRequest,
) -> dict:
    out: dict = {}
    out["EndpointId"] = value["endpoint_id"]
    out["DestinationAddress"] = value["destination_address"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListCustomRoutingPortMappingsByDestinationRequest:
    out: ListCustomRoutingPortMappingsByDestinationRequest = {}  # type: ignore[typeddict-item]
    if "EndpointId" in data:
        out["endpoint_id"] = data["EndpointId"]
    else:
        raise DeserializationError(
            "ListCustomRoutingPortMappingsByDestinationRequest.endpoint_id required"
        )
    if "DestinationAddress" in data:
        out["destination_address"] = data["DestinationAddress"]
    else:
        raise DeserializationError(
            "ListCustomRoutingPortMappingsByDestinationRequest.destination_address required"
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
