"""Generated from Smithy shape ``com.amazonaws.lightsail#GetBlueprintsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.app_category
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.string


class GetBlueprintsRequest(TypedDict):
    include_inactive: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>A Boolean value that indicates whether to include inactive (unavailable) blueprints in the response of your request.</p>"""
    page_token: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetBlueprints</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>"""
    app_category: NotRequired["aws_sdk_lightsail.types.app_category.AppCategory"]
    """<p>Returns a list of blueprints that are specific to Lightsail for Research.</p> <important> <p>You must use this parameter to view Lightsail for Research blueprints.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBlueprintsRequest) -> dict:
    out: dict = {}
    if "include_inactive" in value:
        out["includeInactive"] = value["include_inactive"]
    if "page_token" in value:
        out["pageToken"] = value["page_token"]
    if "app_category" in value:
        import aws_sdk_lightsail.types.app_category

        out["appCategory"] = (
            aws_sdk_lightsail.types.app_category.serialize_aws_json_1_1(
                value["app_category"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBlueprintsRequest:
    out: GetBlueprintsRequest = {}  # type: ignore[typeddict-item]
    if "includeInactive" in data:
        out["include_inactive"] = data["includeInactive"]
    if "pageToken" in data:
        out["page_token"] = data["pageToken"]
    if "appCategory" in data:
        import aws_sdk_lightsail.types.app_category

        out["app_category"] = (
            aws_sdk_lightsail.types.app_category.deserialize_aws_json_1_1(
                data["appCategory"]
            )
        )
    return out
