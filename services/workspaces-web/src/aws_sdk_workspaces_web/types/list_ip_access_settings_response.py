"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ListIpAccessSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.ip_access_settings_list
    import aws_sdk_workspaces_web.types.pagination_token


class ListIpAccessSettingsResponse(TypedDict):
    ip_access_settings: NotRequired[
        "aws_sdk_workspaces_web.types.ip_access_settings_list.IpAccessSettingsList"
    ]
    """<p>The IP access settings.</p>"""
    next_token: NotRequired[
        "aws_sdk_workspaces_web.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIpAccessSettingsResponse) -> dict:
    out: dict = {}
    if "ip_access_settings" in value:
        import aws_sdk_workspaces_web.types.ip_access_settings_list

        out["ipAccessSettings"] = (
            aws_sdk_workspaces_web.types.ip_access_settings_list.serialize_json(
                value["ip_access_settings"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIpAccessSettingsResponse:
    out: ListIpAccessSettingsResponse = {}  # type: ignore[typeddict-item]
    if "ipAccessSettings" in data:
        import aws_sdk_workspaces_web.types.ip_access_settings_list

        out["ip_access_settings"] = (
            aws_sdk_workspaces_web.types.ip_access_settings_list.deserialize_json(
                data["ipAccessSettings"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
