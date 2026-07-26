"""Generated from Smithy shape ``com.amazonaws.drs#DescribeSourceNetworksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.describe_source_networks_request_filters
    import capo_drs.types.pagination_token
    import capo_drs.types.strictly_positive_integer


class DescribeSourceNetworksRequest(TypedDict, closed=True):
    filters: NotRequired[
        "capo_drs.types.describe_source_networks_request_filters.DescribeSourceNetworksRequestFilters"
    ]
    """<p>A set of filters by which to return Source Networks.</p>"""
    max_results: NotRequired[
        "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
    ]
    """<p>Maximum number of Source Networks to retrieve.</p>"""
    next_token: NotRequired["capo_drs.types.pagination_token.PaginationToken"]
    """<p>The token of the next Source Networks to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSourceNetworksRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_drs.types.describe_source_networks_request_filters

        out["filters"] = (
            capo_drs.types.describe_source_networks_request_filters.serialize_json(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeSourceNetworksRequest:
    out: DescribeSourceNetworksRequest = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import capo_drs.types.describe_source_networks_request_filters

        out["filters"] = (
            capo_drs.types.describe_source_networks_request_filters.deserialize_json(
                data["filters"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
