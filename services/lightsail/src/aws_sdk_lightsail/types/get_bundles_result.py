"""Generated from Smithy shape ``com.amazonaws.lightsail#GetBundlesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.bundle_list
    import aws_sdk_lightsail.types.string


class GetBundlesResult(TypedDict):
    bundles: NotRequired["aws_sdk_lightsail.types.bundle_list.BundleList"]
    """<p>An array of key-value pairs that contains information about the available bundles.</p>"""
    next_page_token: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>A next page token is not returned if there are no more results to display.</p> <p>To get the next page of results, perform another <code>GetBundles</code> request and specify the next page token using the <code>pageToken</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBundlesResult) -> dict:
    out: dict = {}
    if "bundles" in value:
        import aws_sdk_lightsail.types.bundle_list

        out["bundles"] = aws_sdk_lightsail.types.bundle_list.serialize_aws_json_1_1(
            value["bundles"]
        )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBundlesResult:
    out: GetBundlesResult = {}  # type: ignore[typeddict-item]
    if "bundles" in data:
        import aws_sdk_lightsail.types.bundle_list

        out["bundles"] = aws_sdk_lightsail.types.bundle_list.deserialize_aws_json_1_1(
            data["bundles"]
        )
    if "nextPageToken" in data:
        out["next_page_token"] = data["nextPageToken"]
    return out
