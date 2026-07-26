"""Generated from Smithy shape ``com.amazonaws.networkmanager#SiteToSiteVpnAttachment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.attachment
    import capo_networkmanager.types.vpn_connection_arn


class SiteToSiteVpnAttachment(TypedDict, closed=True):
    attachment: NotRequired["capo_networkmanager.types.attachment.Attachment"]
    """<p>Provides details about a site-to-site VPN attachment.</p>"""
    vpn_connection_arn: NotRequired[
        "capo_networkmanager.types.vpn_connection_arn.VpnConnectionArn"
    ]
    """<p>The ARN of the site-to-site VPN attachment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SiteToSiteVpnAttachment) -> dict:
    out: dict = {}
    if "attachment" in value:
        import capo_networkmanager.types.attachment

        out["Attachment"] = capo_networkmanager.types.attachment.serialize_json(
            value["attachment"]
        )
    if "vpn_connection_arn" in value:
        out["VpnConnectionArn"] = value["vpn_connection_arn"]
    return out


def deserialize_json(data: dict) -> SiteToSiteVpnAttachment:
    out: SiteToSiteVpnAttachment = {}  # type: ignore[typeddict-item]
    if "Attachment" in data:
        import capo_networkmanager.types.attachment

        out["attachment"] = capo_networkmanager.types.attachment.deserialize_json(
            data["Attachment"]
        )
    if "VpnConnectionArn" in data:
        out["vpn_connection_arn"] = data["VpnConnectionArn"]
    return out
