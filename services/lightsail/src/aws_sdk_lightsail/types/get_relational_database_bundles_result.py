"""Generated from Smithy shape ``com.amazonaws.lightsail#GetRelationalDatabaseBundlesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.relational_database_bundle_list
    import aws_sdk_lightsail.types.string


class GetRelationalDatabaseBundlesResult(TypedDict):
    bundles: NotRequired[
        "aws_sdk_lightsail.types.relational_database_bundle_list.RelationalDatabaseBundleList"
    ]
    """<p>An object describing the result of your get relational database bundles request.</p>"""
    next_page_token: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>A next page token is not returned if there are no more results to display.</p> <p>To get the next page of results, perform another <code>GetRelationalDatabaseBundles</code> request and specify the next page token using the <code>pageToken</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRelationalDatabaseBundlesResult) -> dict:
    out: dict = {}
    if "bundles" in value:
        import aws_sdk_lightsail.types.relational_database_bundle_list

        out["bundles"] = (
            aws_sdk_lightsail.types.relational_database_bundle_list.serialize_aws_json_1_1(
                value["bundles"]
            )
        )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRelationalDatabaseBundlesResult:
    out: GetRelationalDatabaseBundlesResult = {}  # type: ignore[typeddict-item]
    if "bundles" in data:
        import aws_sdk_lightsail.types.relational_database_bundle_list

        out["bundles"] = (
            aws_sdk_lightsail.types.relational_database_bundle_list.deserialize_aws_json_1_1(
                data["bundles"]
            )
        )
    if "nextPageToken" in data:
        out["next_page_token"] = data["nextPageToken"]
    return out
