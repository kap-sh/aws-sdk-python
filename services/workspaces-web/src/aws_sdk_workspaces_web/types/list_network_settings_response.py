"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ListNetworkSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.network_settings_list
    import aws_sdk_workspaces_web.types.pagination_token


class ListNetworkSettingsResponse(TypedDict, closed=True):
    network_settings: NotRequired[
        "aws_sdk_workspaces_web.types.network_settings_list.NetworkSettingsList"
    ]
    """<p>The network settings.</p>"""
    next_token: NotRequired[
        "aws_sdk_workspaces_web.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkSettingsResponse) -> dict:
    out: dict = {}
    if "network_settings" in value:
        import aws_sdk_workspaces_web.types.network_settings_list

        out["networkSettings"] = (
            aws_sdk_workspaces_web.types.network_settings_list.serialize_json(
                value["network_settings"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNetworkSettingsResponse:
    out: ListNetworkSettingsResponse = {}  # type: ignore[typeddict-item]
    if "networkSettings" in data:
        import aws_sdk_workspaces_web.types.network_settings_list

        out["network_settings"] = (
            aws_sdk_workspaces_web.types.network_settings_list.deserialize_json(
                data["networkSettings"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
