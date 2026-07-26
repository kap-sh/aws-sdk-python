"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ListUserAccessLoggingSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.pagination_token
    import capo_workspaces_web.types.user_access_logging_settings_list


class ListUserAccessLoggingSettingsResponse(TypedDict, closed=True):
    user_access_logging_settings: NotRequired[
        "capo_workspaces_web.types.user_access_logging_settings_list.UserAccessLoggingSettingsList"
    ]
    """<p>The user access logging settings.</p>"""
    next_token: NotRequired[
        "capo_workspaces_web.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUserAccessLoggingSettingsResponse) -> dict:
    out: dict = {}
    if "user_access_logging_settings" in value:
        import capo_workspaces_web.types.user_access_logging_settings_list

        out["userAccessLoggingSettings"] = (
            capo_workspaces_web.types.user_access_logging_settings_list.serialize_json(
                value["user_access_logging_settings"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListUserAccessLoggingSettingsResponse:
    out: ListUserAccessLoggingSettingsResponse = {}  # type: ignore[typeddict-item]
    if "userAccessLoggingSettings" in data:
        import capo_workspaces_web.types.user_access_logging_settings_list

        out["user_access_logging_settings"] = (
            capo_workspaces_web.types.user_access_logging_settings_list.deserialize_json(
                data["userAccessLoggingSettings"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
