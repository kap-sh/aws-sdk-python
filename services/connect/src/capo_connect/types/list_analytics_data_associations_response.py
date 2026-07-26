"""Generated from Smithy shape ``com.amazonaws.connect#ListAnalyticsDataAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.analytics_data_association_results
    import capo_connect.types.next_token


class ListAnalyticsDataAssociationsResponse(TypedDict, closed=True):
    results: NotRequired[
        "capo_connect.types.analytics_data_association_results.AnalyticsDataAssociationResults"
    ]
    """<p>An array of successful results: <code>DataSetId</code>, <code>TargetAccountId</code>, <code>ResourceShareId</code>, <code>ResourceShareArn</code>. This is a paginated API, so <code>nextToken</code> is given if there are more results to be returned.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnalyticsDataAssociationsResponse) -> dict:
    out: dict = {}
    if "results" in value:
        import capo_connect.types.analytics_data_association_results

        out["Results"] = (
            capo_connect.types.analytics_data_association_results.serialize_json(
                value["results"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAnalyticsDataAssociationsResponse:
    out: ListAnalyticsDataAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "Results" in data:
        import capo_connect.types.analytics_data_association_results

        out["results"] = (
            capo_connect.types.analytics_data_association_results.deserialize_json(
                data["Results"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
