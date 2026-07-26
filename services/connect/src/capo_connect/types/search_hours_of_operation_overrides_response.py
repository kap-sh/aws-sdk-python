"""Generated from Smithy shape ``com.amazonaws.connect#SearchHoursOfOperationOverridesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.approximate_total_count
    import capo_connect.types.hours_of_operation_override_list
    import capo_connect.types.next_token2500


class SearchHoursOfOperationOverridesResponse(TypedDict, closed=True):
    hours_of_operation_overrides: NotRequired[
        "capo_connect.types.hours_of_operation_override_list.HoursOfOperationOverrideList"
    ]
    """<p>Information about the hours of operations overrides.</p>"""
    next_token: NotRequired["capo_connect.types.next_token2500.NextToken2500"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""
    approximate_total_count: NotRequired[
        "capo_connect.types.approximate_total_count.ApproximateTotalCount"
    ]
    """<p>The total number of hours of operations which matched your search query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchHoursOfOperationOverridesResponse) -> dict:
    out: dict = {}
    if "hours_of_operation_overrides" in value:
        import capo_connect.types.hours_of_operation_override_list

        out["HoursOfOperationOverrides"] = (
            capo_connect.types.hours_of_operation_override_list.serialize_json(
                value["hours_of_operation_overrides"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "approximate_total_count" in value:
        out["ApproximateTotalCount"] = value["approximate_total_count"]
    return out


def deserialize_json(data: dict) -> SearchHoursOfOperationOverridesResponse:
    out: SearchHoursOfOperationOverridesResponse = {}  # type: ignore[typeddict-item]
    if "HoursOfOperationOverrides" in data:
        import capo_connect.types.hours_of_operation_override_list

        out["hours_of_operation_overrides"] = (
            capo_connect.types.hours_of_operation_override_list.deserialize_json(
                data["HoursOfOperationOverrides"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ApproximateTotalCount" in data:
        out["approximate_total_count"] = data["ApproximateTotalCount"]
    return out
