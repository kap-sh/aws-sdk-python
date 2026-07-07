"""Generated from Smithy shape ``com.amazonaws.inspector2#ListCisScanResultsAggregatedByChecksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_check_aggregation_list
    import aws_sdk_inspector2.types.next_token


class ListCisScanResultsAggregatedByChecksResponse(TypedDict, closed=True):
    check_aggregations: NotRequired[
        "aws_sdk_inspector2.types.cis_check_aggregation_list.CisCheckAggregationList"
    ]
    """<p>The check aggregations.</p>"""
    next_token: NotRequired["aws_sdk_inspector2.types.next_token.NextToken"]
    """<p>The pagination token from a previous request that's used to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCisScanResultsAggregatedByChecksResponse) -> dict:
    out: dict = {}
    if "check_aggregations" in value:
        import aws_sdk_inspector2.types.cis_check_aggregation_list

        out["checkAggregations"] = (
            aws_sdk_inspector2.types.cis_check_aggregation_list.serialize_json(
                value["check_aggregations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCisScanResultsAggregatedByChecksResponse:
    out: ListCisScanResultsAggregatedByChecksResponse = {}  # type: ignore[typeddict-item]
    if "checkAggregations" in data:
        import aws_sdk_inspector2.types.cis_check_aggregation_list

        out["check_aggregations"] = (
            aws_sdk_inspector2.types.cis_check_aggregation_list.deserialize_json(
                data["checkAggregations"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
