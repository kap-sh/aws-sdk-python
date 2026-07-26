"""Generated from Smithy shape ``com.amazonaws.workspacesweb#IpAccessSettingsSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn
    import capo_workspaces_web.types.description
    import capo_workspaces_web.types.display_name
    import capo_workspaces_web.types.timestamp


class IpAccessSettingsSummary(TypedDict, closed=True):
    ip_access_settings_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of IP access settings.</p>"""
    display_name: NotRequired["capo_workspaces_web.types.display_name.DisplayName"]
    """<p>The display name of the IP access settings.</p>"""
    description: NotRequired["capo_workspaces_web.types.description.Description"]
    """<p>The description of the IP access settings.</p>"""
    creation_date: NotRequired["capo_workspaces_web.types.timestamp.Timestamp"]
    """<p>The creation date timestamp of the IP access settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IpAccessSettingsSummary) -> dict:
    out: dict = {}
    out["ipAccessSettingsArn"] = value["ip_access_settings_arn"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "creation_date" in value:
        import capo_workspaces_web.types.timestamp

        out["creationDate"] = capo_workspaces_web.types.timestamp.serialize_json(
            value["creation_date"]
        )
    return out


def deserialize_json(data: dict) -> IpAccessSettingsSummary:
    out: IpAccessSettingsSummary = {}  # type: ignore[typeddict-item]
    if "ipAccessSettingsArn" in data:
        out["ip_access_settings_arn"] = data["ipAccessSettingsArn"]
    else:
        raise DeserializationError(
            "IpAccessSettingsSummary.ip_access_settings_arn required"
        )
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "description" in data:
        out["description"] = data["description"]
    if "creationDate" in data:
        import capo_workspaces_web.types.timestamp

        out["creation_date"] = capo_workspaces_web.types.timestamp.deserialize_json(
            data["creationDate"]
        )
    return out
