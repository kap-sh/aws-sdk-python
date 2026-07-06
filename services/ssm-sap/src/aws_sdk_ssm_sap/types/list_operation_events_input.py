"""Generated from Smithy shape ``com.amazonaws.ssmsap#ListOperationEventsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_sap.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.filter_list
    import aws_sdk_ssm_sap.types.max_results
    import aws_sdk_ssm_sap.types.next_token
    import aws_sdk_ssm_sap.types.operation_id


class ListOperationEventsInput(TypedDict, closed=True):
    operation_id: "aws_sdk_ssm_sap.types.operation_id.OperationId"
    """<p>The ID of the operation.</p>"""
    max_results: NotRequired["aws_sdk_ssm_sap.types.max_results.MaxResults"]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.</p> <p>If you do not specify a value for <code>MaxResults</code>, the request returns 50 items per page by default.</p>"""
    next_token: NotRequired["aws_sdk_ssm_sap.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""
    filters: NotRequired["aws_sdk_ssm_sap.types.filter_list.FilterList"]
    """<p>Optionally specify filters to narrow the returned operation event items.</p> <p>Valid filter names include <code>status</code>, <code>resourceID</code>, and <code>resourceType</code>. The valid operator for all three filters is <code>Equals</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOperationEventsInput) -> dict:
    out: dict = {}
    out["OperationId"] = value["operation_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filters" in value:
        import aws_sdk_ssm_sap.types.filter_list

        out["Filters"] = aws_sdk_ssm_sap.types.filter_list.serialize_json(
            value["filters"]
        )
    return out


def deserialize_json(data: dict) -> ListOperationEventsInput:
    out: ListOperationEventsInput = {}  # type: ignore[typeddict-item]
    if "OperationId" in data:
        out["operation_id"] = data["OperationId"]
    else:
        raise DeserializationError("ListOperationEventsInput.operation_id required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Filters" in data:
        import aws_sdk_ssm_sap.types.filter_list

        out["filters"] = aws_sdk_ssm_sap.types.filter_list.deserialize_json(
            data["Filters"]
        )
    return out
