"""Generated from Smithy shape ``com.amazonaws.comprehend#ListEndpointsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.endpoint_filter
    import aws_sdk_comprehend.types.max_results_integer
    import aws_sdk_comprehend.types.string


class ListEndpointsRequest(TypedDict):
    filter: NotRequired["aws_sdk_comprehend.types.endpoint_filter.EndpointFilter"]
    """<p>Filters the endpoints that are returned. You can filter endpoints on their name, model, status, or the date and time that they were created. You can only set one filter at a time. </p>"""
    next_token: NotRequired["aws_sdk_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""
    max_results: NotRequired[
        "aws_sdk_comprehend.types.max_results_integer.MaxResultsInteger"
    ]
    """<p>The maximum number of results to return in each page. The default is 100.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEndpointsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import aws_sdk_comprehend.types.endpoint_filter

        out["Filter"] = aws_sdk_comprehend.types.endpoint_filter.serialize_aws_json_1_1(
            value["filter"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEndpointsRequest:
    out: ListEndpointsRequest = {}  # type: ignore[typeddict-item]
    if "Filter" in data:
        import aws_sdk_comprehend.types.endpoint_filter

        out["filter"] = (
            aws_sdk_comprehend.types.endpoint_filter.deserialize_aws_json_1_1(
                data["Filter"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
