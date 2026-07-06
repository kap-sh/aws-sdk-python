"""Generated from Smithy shape ``com.amazonaws.inspector2#ListCoverageStatisticsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.counts_list
    import aws_sdk_inspector2.types.next_token


class ListCoverageStatisticsResponse(TypedDict, closed=True):
    counts_by_group: NotRequired["aws_sdk_inspector2.types.counts_list.CountsList"]
    """<p>An array with the number for each group.</p>"""
    total_counts: "int"
    """<p>The total number for all groups.</p>"""
    next_token: NotRequired["aws_sdk_inspector2.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the <code>NextToken</code> value returned from the previous request to continue listing results after the first page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCoverageStatisticsResponse) -> dict:
    out: dict = {}
    if "counts_by_group" in value:
        import aws_sdk_inspector2.types.counts_list

        out["countsByGroup"] = aws_sdk_inspector2.types.counts_list.serialize_json(
            value["counts_by_group"]
        )
    out["totalCounts"] = value["total_counts"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCoverageStatisticsResponse:
    out: ListCoverageStatisticsResponse = {}  # type: ignore[typeddict-item]
    if "countsByGroup" in data:
        import aws_sdk_inspector2.types.counts_list

        out["counts_by_group"] = aws_sdk_inspector2.types.counts_list.deserialize_json(
            data["countsByGroup"]
        )
    if "totalCounts" in data:
        out["total_counts"] = data["totalCounts"]
    else:
        raise DeserializationError(
            "ListCoverageStatisticsResponse.total_counts required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
