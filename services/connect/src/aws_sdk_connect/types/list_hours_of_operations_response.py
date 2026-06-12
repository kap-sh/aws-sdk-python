"""Generated from Smithy shape ``com.amazonaws.connect#ListHoursOfOperationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.hours_of_operation_summary_list
    import aws_sdk_connect.types.next_token


class ListHoursOfOperationsResponse(TypedDict):
    hours_of_operation_summary_list: NotRequired[
        "aws_sdk_connect.types.hours_of_operation_summary_list.HoursOfOperationSummaryList"
    ]
    """<p>Information about the hours of operation.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListHoursOfOperationsResponse) -> dict:
    out: dict = {}
    if "hours_of_operation_summary_list" in value:
        import aws_sdk_connect.types.hours_of_operation_summary_list

        out["HoursOfOperationSummaryList"] = (
            aws_sdk_connect.types.hours_of_operation_summary_list.serialize_json(
                value["hours_of_operation_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListHoursOfOperationsResponse:
    out: ListHoursOfOperationsResponse = {}  # type: ignore[typeddict-item]
    if "HoursOfOperationSummaryList" in data:
        import aws_sdk_connect.types.hours_of_operation_summary_list

        out["hours_of_operation_summary_list"] = (
            aws_sdk_connect.types.hours_of_operation_summary_list.deserialize_json(
                data["HoursOfOperationSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
