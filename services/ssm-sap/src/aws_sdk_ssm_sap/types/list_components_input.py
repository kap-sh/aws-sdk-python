"""Generated from Smithy shape ``com.amazonaws.ssmsap#ListComponentsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.application_id
    import aws_sdk_ssm_sap.types.max_results
    import aws_sdk_ssm_sap.types.next_token


class ListComponentsInput(TypedDict):
    application_id: NotRequired["aws_sdk_ssm_sap.types.application_id.ApplicationId"]
    """<p>The ID of the application.</p>"""
    next_token: NotRequired["aws_sdk_ssm_sap.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_ssm_sap.types.max_results.MaxResults"]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.</p> <p>If you do not specify a value for MaxResults, the request returns 50 items per page by default.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListComponentsInput) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListComponentsInput:
    out: ListComponentsInput = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
