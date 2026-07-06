"""Generated from Smithy shape ``com.amazonaws.lightsail#GetRelationalDatabaseBundlesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.string


class GetRelationalDatabaseBundlesRequest(TypedDict, closed=True):
    page_token: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetRelationalDatabaseBundles</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>"""
    include_inactive: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>A Boolean value that indicates whether to include inactive (unavailable) bundles in the response of your request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRelationalDatabaseBundlesRequest) -> dict:
    out: dict = {}
    if "page_token" in value:
        out["pageToken"] = value["page_token"]
    if "include_inactive" in value:
        out["includeInactive"] = value["include_inactive"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRelationalDatabaseBundlesRequest:
    out: GetRelationalDatabaseBundlesRequest = {}  # type: ignore[typeddict-item]
    if "pageToken" in data:
        out["page_token"] = data["pageToken"]
    if "includeInactive" in data:
        out["include_inactive"] = data["includeInactive"]
    return out
