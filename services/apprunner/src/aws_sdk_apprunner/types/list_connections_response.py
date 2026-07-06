"""Generated from Smithy shape ``com.amazonaws.apprunner#ListConnectionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.connection_summary_list
    import aws_sdk_apprunner.types.next_token


class ListConnectionsResponse(TypedDict, closed=True):
    connection_summary_list: (
        "aws_sdk_apprunner.types.connection_summary_list.ConnectionSummaryList"
    )
    """<p>A list of summary information records for connections. In a paginated request, the request returns up to <code>MaxResults</code> records for each call.</p>"""
    next_token: NotRequired["aws_sdk_apprunner.types.next_token.NextToken"]
    """<p>The token that you can pass in a subsequent request to get the next result page. Returned in a paginated request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListConnectionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_apprunner.types.connection_summary_list

    out["ConnectionSummaryList"] = (
        aws_sdk_apprunner.types.connection_summary_list.serialize_aws_json_1_0(
            value["connection_summary_list"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListConnectionsResponse:
    out: ListConnectionsResponse = {}  # type: ignore[typeddict-item]
    if "ConnectionSummaryList" in data:
        import aws_sdk_apprunner.types.connection_summary_list

        out["connection_summary_list"] = (
            aws_sdk_apprunner.types.connection_summary_list.deserialize_aws_json_1_0(
                data["ConnectionSummaryList"]
            )
        )
    else:
        raise DeserializationError(
            "ListConnectionsResponse.connection_summary_list required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
