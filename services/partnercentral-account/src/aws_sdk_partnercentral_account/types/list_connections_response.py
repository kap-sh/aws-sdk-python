"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ListConnectionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.connection_summary_list
    import aws_sdk_partnercentral_account.types.next_token


class ListConnectionsResponse(TypedDict, closed=True):
    connection_summaries: "aws_sdk_partnercentral_account.types.connection_summary_list.ConnectionSummaryList"
    """<p>A list of connection summaries matching the specified criteria.</p>"""
    next_token: NotRequired["aws_sdk_partnercentral_account.types.next_token.NextToken"]
    """<p>The token for retrieving the next page of results if more results are available.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListConnectionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_partnercentral_account.types.connection_summary_list

    out["ConnectionSummaries"] = (
        aws_sdk_partnercentral_account.types.connection_summary_list.serialize_aws_json_1_0(
            value["connection_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListConnectionsResponse:
    out: ListConnectionsResponse = {}  # type: ignore[typeddict-item]
    if "ConnectionSummaries" in data:
        import aws_sdk_partnercentral_account.types.connection_summary_list

        out["connection_summaries"] = (
            aws_sdk_partnercentral_account.types.connection_summary_list.deserialize_aws_json_1_0(
                data["ConnectionSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListConnectionsResponse.connection_summaries required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
