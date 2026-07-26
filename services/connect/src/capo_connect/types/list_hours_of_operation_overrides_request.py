"""Generated from Smithy shape ``com.amazonaws.connect#ListHoursOfOperationOverridesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.hours_of_operation_id
    import capo_connect.types.instance_id
    import capo_connect.types.max_result100
    import capo_connect.types.next_token


class ListHoursOfOperationOverridesRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance.</p>"""
    hours_of_operation_id: "capo_connect.types.hours_of_operation_id.HoursOfOperationId"
    """<p>The identifier for the hours of operation.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_connect.types.max_result100.MaxResult100"]
    """<p>The maximum number of results to return per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListHoursOfOperationOverridesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListHoursOfOperationOverridesRequest:
    out: ListHoursOfOperationOverridesRequest = {}  # type: ignore[typeddict-item]
    return out
