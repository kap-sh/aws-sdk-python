"""Generated from Smithy shape ``com.amazonaws.ssmsap#ListOperationsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_sap.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.application_id
    import aws_sdk_ssm_sap.types.filter_list
    import aws_sdk_ssm_sap.types.max_results
    import aws_sdk_ssm_sap.types.next_token


class ListOperationsInput(TypedDict):
    application_id: "aws_sdk_ssm_sap.types.application_id.ApplicationId"
    """<p>The ID of the application.</p>"""
    max_results: NotRequired["aws_sdk_ssm_sap.types.max_results.MaxResults"]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value. If you do not specify a value for MaxResults, the request returns 50 items per page by default.</p>"""
    next_token: NotRequired["aws_sdk_ssm_sap.types.next_token.NextToken"]
    """<p>The token for the next page of results. </p>"""
    filters: NotRequired["aws_sdk_ssm_sap.types.filter_list.FilterList"]
    """<p>The filters of an operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOperationsInput) -> dict:
    out: dict = {}
    out["ApplicationId"] = value["application_id"]
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


def deserialize_json(data: dict) -> ListOperationsInput:
    out: ListOperationsInput = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    else:
        raise DeserializationError("ListOperationsInput.application_id required")
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
