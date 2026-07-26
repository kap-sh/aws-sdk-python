"""Generated from Smithy shape ``com.amazonaws.connect#SearchHoursOfOperationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.approximate_total_count
    import capo_connect.types.hours_of_operation_list
    import capo_connect.types.next_token2500


class SearchHoursOfOperationsResponse(TypedDict, closed=True):
    hours_of_operations: NotRequired[
        "capo_connect.types.hours_of_operation_list.HoursOfOperationList"
    ]
    """<p>Information about the hours of operations.</p>"""
    next_token: NotRequired["capo_connect.types.next_token2500.NextToken2500"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    approximate_total_count: NotRequired[
        "capo_connect.types.approximate_total_count.ApproximateTotalCount"
    ]
    """<p>The total number of hours of operations which matched your search query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchHoursOfOperationsResponse) -> dict:
    out: dict = {}
    if "hours_of_operations" in value:
        import capo_connect.types.hours_of_operation_list

        out["HoursOfOperations"] = (
            capo_connect.types.hours_of_operation_list.serialize_json(
                value["hours_of_operations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "approximate_total_count" in value:
        out["ApproximateTotalCount"] = value["approximate_total_count"]
    return out


def deserialize_json(data: dict) -> SearchHoursOfOperationsResponse:
    out: SearchHoursOfOperationsResponse = {}  # type: ignore[typeddict-item]
    if "HoursOfOperations" in data:
        import capo_connect.types.hours_of_operation_list

        out["hours_of_operations"] = (
            capo_connect.types.hours_of_operation_list.deserialize_json(
                data["HoursOfOperations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ApproximateTotalCount" in data:
        out["approximate_total_count"] = data["ApproximateTotalCount"]
    return out
