"""Generated from Smithy shape ``com.amazonaws.workspacesweb#AssociateNetworkSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn


class AssociateNetworkSettingsResponse(TypedDict, closed=True):
    portal_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the web portal.</p>"""
    network_settings_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the network settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateNetworkSettingsResponse) -> dict:
    out: dict = {}
    out["portalArn"] = value["portal_arn"]
    out["networkSettingsArn"] = value["network_settings_arn"]
    return out


def deserialize_json(data: dict) -> AssociateNetworkSettingsResponse:
    out: AssociateNetworkSettingsResponse = {}  # type: ignore[typeddict-item]
    if "portalArn" in data:
        out["portal_arn"] = data["portalArn"]
    else:
        raise DeserializationError(
            "AssociateNetworkSettingsResponse.portal_arn required"
        )
    if "networkSettingsArn" in data:
        out["network_settings_arn"] = data["networkSettingsArn"]
    else:
        raise DeserializationError(
            "AssociateNetworkSettingsResponse.network_settings_arn required"
        )
    return out
