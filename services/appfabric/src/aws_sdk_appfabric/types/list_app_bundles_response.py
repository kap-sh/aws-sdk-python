"""Generated from Smithy shape ``com.amazonaws.appfabric#ListAppBundlesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.app_bundle_summary_list
    import aws_sdk_appfabric.types.string2048


class ListAppBundlesResponse(TypedDict, closed=True):
    app_bundle_summary_list: (
        "aws_sdk_appfabric.types.app_bundle_summary_list.AppBundleSummaryList"
    )
    """<p>Contains a list of app bundle summaries.</p>"""
    next_token: NotRequired["aws_sdk_appfabric.types.string2048.String2048"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppBundlesResponse) -> dict:
    out: dict = {}
    import aws_sdk_appfabric.types.app_bundle_summary_list

    out["appBundleSummaryList"] = (
        aws_sdk_appfabric.types.app_bundle_summary_list.serialize_json(
            value["app_bundle_summary_list"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAppBundlesResponse:
    out: ListAppBundlesResponse = {}  # type: ignore[typeddict-item]
    if "appBundleSummaryList" in data:
        import aws_sdk_appfabric.types.app_bundle_summary_list

        out["app_bundle_summary_list"] = (
            aws_sdk_appfabric.types.app_bundle_summary_list.deserialize_json(
                data["appBundleSummaryList"]
            )
        )
    else:
        raise DeserializationError(
            "ListAppBundlesResponse.app_bundle_summary_list required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
