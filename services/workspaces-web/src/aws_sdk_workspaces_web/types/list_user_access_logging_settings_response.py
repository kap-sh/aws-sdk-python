"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ListUserAccessLoggingSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.pagination_token
    import aws_sdk_workspaces_web.types.user_access_logging_settings_list


class ListUserAccessLoggingSettingsResponse(TypedDict):
    user_access_logging_settings: NotRequired[
        "aws_sdk_workspaces_web.types.user_access_logging_settings_list.UserAccessLoggingSettingsList"
    ]
    """<p>The user access logging settings.</p>"""
    next_token: NotRequired[
        "aws_sdk_workspaces_web.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUserAccessLoggingSettingsResponse) -> dict:
    out: dict = {}
    if "user_access_logging_settings" in value:
        import aws_sdk_workspaces_web.types.user_access_logging_settings_list

        out["userAccessLoggingSettings"] = (
            aws_sdk_workspaces_web.types.user_access_logging_settings_list.serialize_json(
                value["user_access_logging_settings"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListUserAccessLoggingSettingsResponse:
    out: ListUserAccessLoggingSettingsResponse = {}  # type: ignore[typeddict-item]
    if "userAccessLoggingSettings" in data:
        import aws_sdk_workspaces_web.types.user_access_logging_settings_list

        out["user_access_logging_settings"] = (
            aws_sdk_workspaces_web.types.user_access_logging_settings_list.deserialize_json(
                data["userAccessLoggingSettings"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
