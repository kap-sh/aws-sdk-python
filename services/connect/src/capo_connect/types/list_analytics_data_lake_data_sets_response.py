"""Generated from Smithy shape ``com.amazonaws.connect#ListAnalyticsDataLakeDataSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.analytics_data_sets_results
    import capo_connect.types.next_token


class ListAnalyticsDataLakeDataSetsResponse(TypedDict, closed=True):
    results: NotRequired[
        "capo_connect.types.analytics_data_sets_results.AnalyticsDataSetsResults"
    ]
    """<p>An array of successful results: <code>DataSetId</code>, <code>DataSetName</code>. This is a paginated API, so <code>nextToken</code> is given if there are more results to be returned.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnalyticsDataLakeDataSetsResponse) -> dict:
    out: dict = {}
    if "results" in value:
        import capo_connect.types.analytics_data_sets_results

        out["Results"] = capo_connect.types.analytics_data_sets_results.serialize_json(
            value["results"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAnalyticsDataLakeDataSetsResponse:
    out: ListAnalyticsDataLakeDataSetsResponse = {}  # type: ignore[typeddict-item]
    if "Results" in data:
        import capo_connect.types.analytics_data_sets_results

        out["results"] = (
            capo_connect.types.analytics_data_sets_results.deserialize_json(
                data["Results"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
