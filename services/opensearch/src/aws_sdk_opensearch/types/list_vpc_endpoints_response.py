"""Generated from Smithy shape ``com.amazonaws.opensearch#ListVpcEndpointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.next_token
    import aws_sdk_opensearch.types.vpc_endpoint_summary_list


class ListVpcEndpointsResponse(TypedDict, closed=True):
    vpc_endpoint_summary_list: (
        "aws_sdk_opensearch.types.vpc_endpoint_summary_list.VpcEndpointSummaryList"
    )
    """<p>Information about each endpoint.</p>"""
    next_token: "aws_sdk_opensearch.types.next_token.NextToken"
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVpcEndpointsResponse) -> dict:
    out: dict = {}
    import aws_sdk_opensearch.types.vpc_endpoint_summary_list

    out["VpcEndpointSummaryList"] = (
        aws_sdk_opensearch.types.vpc_endpoint_summary_list.serialize_json(
            value["vpc_endpoint_summary_list"]
        )
    )
    out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListVpcEndpointsResponse:
    out: ListVpcEndpointsResponse = {}  # type: ignore[typeddict-item]
    if "VpcEndpointSummaryList" in data:
        import aws_sdk_opensearch.types.vpc_endpoint_summary_list

        out["vpc_endpoint_summary_list"] = (
            aws_sdk_opensearch.types.vpc_endpoint_summary_list.deserialize_json(
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
