"""Generated from Smithy shape ``com.amazonaws.quicksight#ListActionConnectorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.action_connector_summary_list
    import aws_sdk_quicksight.types.status_code


class ListActionConnectorsResponse(TypedDict, closed=True):
    action_connector_summaries: "aws_sdk_quicksight.types.action_connector_summary_list.ActionConnectorSummaryList"
    """<p>A list of action connector summaries containing basic information about each connector.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token to retrieve the next set of results. If null, there are no more results to retrieve.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status code of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListActionConnectorsResponse) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.action_connector_summary_list

    out["ActionConnectorSummaries"] = (
        aws_sdk_quicksight.types.action_connector_summary_list.serialize_json(
            value["action_connector_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListActionConnectorsResponse:
    out: ListActionConnectorsResponse = {}  # type: ignore[typeddict-item]
    if "ActionConnectorSummaries" in data:
        import aws_sdk_quicksight.types.action_connector_summary_list

        out["action_connector_summaries"] = (
            aws_sdk_quicksight.types.action_connector_summary_list.deserialize_json(
                data["ActionConnectorSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListActionConnectorsResponse.action_connector_summaries required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
