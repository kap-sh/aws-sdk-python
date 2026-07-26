"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeVpcEndpointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.vpc_endpoint_id_list


class DescribeVpcEndpointsRequest(TypedDict, closed=True):
    vpc_endpoint_ids: "capo_opensearch.types.vpc_endpoint_id_list.VpcEndpointIdList"
    """<p>The unique identifiers of the endpoints to get information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeVpcEndpointsRequest) -> dict:
    out: dict = {}
    import capo_opensearch.types.vpc_endpoint_id_list

    out["VpcEndpointIds"] = capo_opensearch.types.vpc_endpoint_id_list.serialize_json(
        value["vpc_endpoint_ids"]
    )
    return out


def deserialize_json(data: dict) -> DescribeVpcEndpointsRequest:
    out: DescribeVpcEndpointsRequest = {}  # type: ignore[typeddict-item]
    if "VpcEndpointIds" in data:
        import capo_opensearch.types.vpc_endpoint_id_list

        out["vpc_endpoint_ids"] = (
            capo_opensearch.types.vpc_endpoint_id_list.deserialize_json(
                data["VpcEndpointIds"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeVpcEndpointsRequest.vpc_endpoint_ids required"
        )
    return out
