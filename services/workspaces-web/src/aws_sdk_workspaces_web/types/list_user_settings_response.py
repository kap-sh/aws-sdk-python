"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ListUserSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.pagination_token
    import aws_sdk_workspaces_web.types.user_settings_list


class ListUserSettingsResponse(TypedDict):
    user_settings: NotRequired[
        "aws_sdk_workspaces_web.types.user_settings_list.UserSettingsList"
    ]
    """<p>The user settings.</p>"""
    next_token: NotRequired[
        "aws_sdk_workspaces_web.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token used to retrieve the next page of results for this operation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUserSettingsResponse) -> dict:
    out: dict = {}
    if "user_settings" in value:
        import aws_sdk_workspaces_web.types.user_settings_list

        out["userSettings"] = (
            aws_sdk_workspaces_web.types.user_settings_list.serialize_json(
                value["user_settings"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListUserSettingsResponse:
    out: ListUserSettingsResponse = {}  # type: ignore[typeddict-item]
    if "userSettings" in data:
        import aws_sdk_workspaces_web.types.user_settings_list

        out["user_settings"] = (
            aws_sdk_workspaces_web.types.user_settings_list.deserialize_json(
                data["userSettings"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
