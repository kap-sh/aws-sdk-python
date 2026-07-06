"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyAggregatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_entries
    import aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_max_results
    import aws_sdk_iotsitewise.types.next_token


class BatchGetAssetPropertyAggregatesRequest(TypedDict, closed=True):
    entries: "aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_entries.BatchGetAssetPropertyAggregatesEntries"
    """<p>The list of asset property aggregate entries for the batch get request. You can specify up to 16 entries per request.</p>"""
    next_token: NotRequired["aws_sdk_iotsitewise.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""
    max_results: NotRequired[
        "aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_max_results.BatchGetAssetPropertyAggregatesMaxResults"
    ]
    """<p>The maximum number of results to return for each paginated request. A result set is returned in the two cases, whichever occurs first.</p> <ul> <li> <p>The size of the result set is equal to 1 MB.</p> </li> <li> <p>The number of data points in the result set is equal to the value of <code>maxResults</code>. The maximum value of <code>maxResults</code> is 4000.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyAggregatesRequest) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_entries

    out["entries"] = (
        aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_entries.serialize_json(
            value["entries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> BatchGetAssetPropertyAggregatesRequest:
    out: BatchGetAssetPropertyAggregatesRequest = {}  # type: ignore[typeddict-item]
    if "entries" in data:
        import aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_entries

        out["entries"] = (
            aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_entries.deserialize_json(
                data["entries"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetAssetPropertyAggregatesRequest.entries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
