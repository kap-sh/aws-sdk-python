"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ListVpcEndpointsForDomainResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.next_token
    import aws_sdk_elasticsearch_service.types.vpc_endpoint_summary_list


class ListVpcEndpointsForDomainResponse(TypedDict):
    vpc_endpoint_summary_list: "aws_sdk_elasticsearch_service.types.vpc_endpoint_summary_list.VpcEndpointSummaryList"
    """<p>Provides list of <code>VpcEndpointSummary</code> summarizing details of the VPC endpoints.</p>"""
    next_token: "aws_sdk_elasticsearch_service.types.next_token.NextToken"
    """<p>Information about each endpoint associated with the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVpcEndpointsForDomainResponse) -> dict:
    out: dict = {}
    import aws_sdk_elasticsearch_service.types.vpc_endpoint_summary_list

    out["VpcEndpointSummaryList"] = (
        aws_sdk_elasticsearch_service.types.vpc_endpoint_summary_list.serialize_json(
            value["vpc_endpoint_summary_list"]
        )
    )
    out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListVpcEndpointsForDomainResponse:
    out: ListVpcEndpointsForDomainResponse = {}  # type: ignore[typeddict-item]
    if "VpcEndpointSummaryList" in data:
        import aws_sdk_elasticsearch_service.types.vpc_endpoint_summary_list

        out["vpc_endpoint_summary_list"] = (
            aws_sdk_elasticsearch_service.types.vpc_endpoint_summary_list.deserialize_json(
                data["VpcEndpointSummaryList"]
            )
        )
    else:
        raise DeserializationError(
            "ListVpcEndpointsForDomainResponse.vpc_endpoint_summary_list required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    else:
        raise DeserializationError(
            "ListVpcEndpointsForDomainResponse.next_token required"
        )
    return out
