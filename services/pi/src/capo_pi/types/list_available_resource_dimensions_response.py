"""Generated from Smithy shape ``com.amazonaws.pi#ListAvailableResourceDimensionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.metric_dimensions_list
    import capo_pi.types.next_token


class ListAvailableResourceDimensionsResponse(TypedDict, closed=True):
    metric_dimensions: NotRequired[
        "capo_pi.types.metric_dimensions_list.MetricDimensionsList"
    ]
    """<p>The dimension information returned for requested metric types.</p>"""
    next_token: NotRequired["capo_pi.types.next_token.NextToken"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAvailableResourceDimensionsResponse) -> dict:
    out: dict = {}
    if "metric_dimensions" in value:
        import capo_pi.types.metric_dimensions_list

        out["MetricDimensions"] = (
            capo_pi.types.metric_dimensions_list.serialize_aws_json_1_1(
                value["metric_dimensions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAvailableResourceDimensionsResponse:
    out: ListAvailableResourceDimensionsResponse = {}  # type: ignore[typeddict-item]
    if "MetricDimensions" in data:
        import capo_pi.types.metric_dimensions_list

        out["metric_dimensions"] = (
            capo_pi.types.metric_dimensions_list.deserialize_aws_json_1_1(
                data["MetricDimensions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
