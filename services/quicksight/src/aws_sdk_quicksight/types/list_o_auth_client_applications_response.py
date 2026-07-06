"""Generated from Smithy shape ``com.amazonaws.quicksight#ListOAuthClientApplicationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.o_auth_client_application_summary_list
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class ListOAuthClientApplicationsResponse(TypedDict, closed=True):
    o_auth_client_applications: NotRequired[
        "aws_sdk_quicksight.types.o_auth_client_application_summary_list.OAuthClientApplicationSummaryList"
    ]
    """<p>A list of OAuthClientApplication summaries.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>A pagination token that can be used in a subsequent request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOAuthClientApplicationsResponse) -> dict:
    out: dict = {}
    if "o_auth_client_applications" in value:
        import aws_sdk_quicksight.types.o_auth_client_application_summary_list

        out["OAuthClientApplications"] = (
            aws_sdk_quicksight.types.o_auth_client_application_summary_list.serialize_json(
                value["o_auth_client_applications"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListOAuthClientApplicationsResponse:
    out: ListOAuthClientApplicationsResponse = {}  # type: ignore[typeddict-item]
    if "OAuthClientApplications" in data:
        import aws_sdk_quicksight.types.o_auth_client_application_summary_list

        out["o_auth_client_applications"] = (
            aws_sdk_quicksight.types.o_auth_client_application_summary_list.deserialize_json(
                data["OAuthClientApplications"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
