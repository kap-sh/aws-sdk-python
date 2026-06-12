"""Generated from Smithy shape ``com.amazonaws.lightsail#GetOperationsForResourceResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.operation_list
    import aws_sdk_lightsail.types.string


class GetOperationsForResourceResult(TypedDict):
    operations: NotRequired["aws_sdk_lightsail.types.operation_list.OperationList"]
    """<p>An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.</p>"""
    next_page_count: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>(Discontinued) Returns the number of pages of results that remain.</p> <note> <p>In releases prior to June 12, 2017, this parameter returned <code>null</code> by the API. It is now discontinued, and the API returns the <code>next page token</code> parameter instead.</p> </note>"""
    next_page_token: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>A next page token is not returned if there are no more results to display.</p> <p>To get the next page of results, perform another <code>GetOperationsForResource</code> request and specify the next page token using the <code>pageToken</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOperationsForResourceResult) -> dict:
    out: dict = {}
    if "operations" in value:
        import aws_sdk_lightsail.types.operation_list

        out["operations"] = (
            aws_sdk_lightsail.types.operation_list.serialize_aws_json_1_1(
                value["operations"]
            )
        )
    if "next_page_count" in value:
        out["nextPageCount"] = value["next_page_count"]
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOperationsForResourceResult:
    out: GetOperationsForResourceResult = {}  # type: ignore[typeddict-item]
    if "operations" in data:
        import aws_sdk_lightsail.types.operation_list

        out["operations"] = (
            aws_sdk_lightsail.types.operation_list.deserialize_aws_json_1_1(
                data["operations"]
            )
        )
    if "nextPageCount" in data:
        out["next_page_count"] = data["nextPageCount"]
    if "nextPageToken" in data:
        out["next_page_token"] = data["nextPageToken"]
    return out
