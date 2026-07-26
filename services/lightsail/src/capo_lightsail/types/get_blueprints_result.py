"""Generated from Smithy shape ``com.amazonaws.lightsail#GetBlueprintsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.blueprint_list
    import capo_lightsail.types.string


class GetBlueprintsResult(TypedDict, closed=True):
    blueprints: NotRequired["capo_lightsail.types.blueprint_list.BlueprintList"]
    """<p>An array of key-value pairs that contains information about the available blueprints.</p>"""
    next_page_token: NotRequired["capo_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>A next page token is not returned if there are no more results to display.</p> <p>To get the next page of results, perform another <code>GetBlueprints</code> request and specify the next page token using the <code>pageToken</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBlueprintsResult) -> dict:
    out: dict = {}
    if "blueprints" in value:
        import capo_lightsail.types.blueprint_list

        out["blueprints"] = capo_lightsail.types.blueprint_list.serialize_aws_json_1_1(
            value["blueprints"]
        )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBlueprintsResult:
    out: GetBlueprintsResult = {}  # type: ignore[typeddict-item]
    if "blueprints" in data:
        import capo_lightsail.types.blueprint_list

        out["blueprints"] = (
            capo_lightsail.types.blueprint_list.deserialize_aws_json_1_1(
                data["blueprints"]
            )
        )
    if "nextPageToken" in data:
        out["next_page_token"] = data["nextPageToken"]
    return out
