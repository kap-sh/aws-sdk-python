"""Generated from Smithy shape ``com.amazonaws.lightsail#GetActiveNamesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.string
    import capo_lightsail.types.string_list


class GetActiveNamesResult(TypedDict, closed=True):
    active_names: NotRequired["capo_lightsail.types.string_list.StringList"]
    """<p>The list of active names returned by the get active names request.</p>"""
    next_page_token: NotRequired["capo_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>A next page token is not returned if there are no more results to display.</p> <p>To get the next page of results, perform another <code>GetActiveNames</code> request and specify the next page token using the <code>pageToken</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetActiveNamesResult) -> dict:
    out: dict = {}
    if "active_names" in value:
        import capo_lightsail.types.string_list

        out["activeNames"] = capo_lightsail.types.string_list.serialize_aws_json_1_1(
            value["active_names"]
        )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetActiveNamesResult:
    out: GetActiveNamesResult = {}  # type: ignore[typeddict-item]
    if "activeNames" in data:
        import capo_lightsail.types.string_list

        out["active_names"] = capo_lightsail.types.string_list.deserialize_aws_json_1_1(
            data["activeNames"]
        )
    if "nextPageToken" in data:
        out["next_page_token"] = data["nextPageToken"]
    return out
