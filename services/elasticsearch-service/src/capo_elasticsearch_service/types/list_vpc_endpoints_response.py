"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ListVpcEndpointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.next_token
    import capo_elasticsearch_service.types.vpc_endpoint_summary_list


class ListVpcEndpointsResponse(TypedDict, closed=True):
    vpc_endpoint_summary_list: "capo_elasticsearch_service.types.vpc_endpoint_summary_list.VpcEndpointSummaryList"
    """<p>Information about each endpoint.</p>"""
    next_token: "capo_elasticsearch_service.types.next_token.NextToken"
    """<p>Provides an identifier to allow retrieval of paginated results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVpcEndpointsResponse) -> dict:
    out: dict = {}
    import capo_elasticsearch_service.types.vpc_endpoint_summary_list

    out["VpcEndpointSummaryList"] = (
        capo_elasticsearch_service.types.vpc_endpoint_summary_list.serialize_json(
            value["vpc_endpoint_summary_list"]
        )
    )
    out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListVpcEndpointsResponse:
    out: ListVpcEndpointsResponse = {}  # type: ignore[typeddict-item]
    if "VpcEndpointSummaryList" in data:
        import capo_elasticsearch_service.types.vpc_endpoint_summary_list

        out["vpc_endpoint_summary_list"] = (
            capo_elasticsearch_service.types.vpc_endpoint_summary_list.deserialize_json(
                data["VpcEndpointSummaryList"]
            )
        )
    else:
        raise DeserializationError(
            "ListVpcEndpointsResponse.vpc_endpoint_summary_list required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    else:
        raise DeserializationError("ListVpcEndpointsResponse.next_token required")
    return out
