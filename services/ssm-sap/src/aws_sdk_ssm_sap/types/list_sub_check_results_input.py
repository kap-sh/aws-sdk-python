"""Generated from Smithy shape ``com.amazonaws.ssmsap#ListSubCheckResultsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_sap.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.max_results
    import aws_sdk_ssm_sap.types.next_token
    import aws_sdk_ssm_sap.types.operation_id


class ListSubCheckResultsInput(TypedDict):
    operation_id: "aws_sdk_ssm_sap.types.operation_id.OperationId"
    """<p>The ID of the configuration check operation.</p>"""
    max_results: NotRequired["aws_sdk_ssm_sap.types.max_results.MaxResults"]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.</p>"""
    next_token: NotRequired["aws_sdk_ssm_sap.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSubCheckResultsInput) -> dict:
    out: dict = {}
    out["OperationId"] = value["operation_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSubCheckResultsInput:
    out: ListSubCheckResultsInput = {}  # type: ignore[typeddict-item]
    if "OperationId" in data:
        out["operation_id"] = data["OperationId"]
    else:
        raise DeserializationError("ListSubCheckResultsInput.operation_id required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
