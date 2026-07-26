"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ListDataProtectionSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.data_protection_settings_list
    import capo_workspaces_web.types.pagination_token


class ListDataProtectionSettingsResponse(TypedDict, closed=True):
    data_protection_settings: NotRequired[
        "capo_workspaces_web.types.data_protection_settings_list.DataProtectionSettingsList"
    ]
    """<p>The data protection settings.</p>"""
    next_token: NotRequired[
        "capo_workspaces_web.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataProtectionSettingsResponse) -> dict:
    out: dict = {}
    if "data_protection_settings" in value:
        import capo_workspaces_web.types.data_protection_settings_list

        out["dataProtectionSettings"] = (
            capo_workspaces_web.types.data_protection_settings_list.serialize_json(
                value["data_protection_settings"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataProtectionSettingsResponse:
    out: ListDataProtectionSettingsResponse = {}  # type: ignore[typeddict-item]
    if "dataProtectionSettings" in data:
        import capo_workspaces_web.types.data_protection_settings_list

        out["data_protection_settings"] = (
            capo_workspaces_web.types.data_protection_settings_list.deserialize_json(
                data["dataProtectionSettings"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
