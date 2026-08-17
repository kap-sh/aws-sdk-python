"""Generated from Smithy shape ``com.amazonaws.ecs#ListAccountSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.settings
    import capo_ecs.types.string


class ListAccountSettingsResponse(TypedDict, closed=True):
    settings: NotRequired["capo_ecs.types.settings.Settings"]
    """<p>The account settings for the resource.</p>"""
    next_token: NotRequired["capo_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListAccountSettings</code> request. When the results of a <code>ListAccountSettings</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAccountSettingsResponse) -> dict:
    out: dict = {}
    if "settings" in value:
        import capo_ecs.types.settings

        out["settings"] = capo_ecs.types.settings.serialize_aws_json_1_1(
            value["settings"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAccountSettingsResponse:
    out: ListAccountSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("settings") is not None:
        import capo_ecs.types.settings

        out["settings"] = capo_ecs.types.settings.deserialize_aws_json_1_1(
            data["settings"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
