"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListDataAccessorsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.max_results_integer_for_list_data_accessors
    import aws_sdk_qbusiness.types.next_token1500


class ListDataAccessorsRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The unique identifier of the Amazon Q Business application.</p>"""
    next_token: NotRequired["aws_sdk_qbusiness.types.next_token1500.NextToken1500"]
    """<p>The token for the next set of results. (You received this token from a previous call.)</p>"""
    max_results: NotRequired[
        "aws_sdk_qbusiness.types.max_results_integer_for_list_data_accessors.MaxResultsIntegerForListDataAccessors"
    ]
    """<p>The maximum number of results to return in a single call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataAccessorsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDataAccessorsRequest:
    out: ListDataAccessorsRequest = {}  # type: ignore[typeddict-item]
    return out
