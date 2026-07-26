"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateSiteToSiteVpnAttachmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.site_to_site_vpn_attachment


class CreateSiteToSiteVpnAttachmentResponse(TypedDict, closed=True):
    site_to_site_vpn_attachment: NotRequired[
        "capo_networkmanager.types.site_to_site_vpn_attachment.SiteToSiteVpnAttachment"
    ]
    """<p>Details about a site-to-site VPN attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSiteToSiteVpnAttachmentResponse) -> dict:
    out: dict = {}
    if "site_to_site_vpn_attachment" in value:
        import capo_networkmanager.types.site_to_site_vpn_attachment

        out["SiteToSiteVpnAttachment"] = (
            capo_networkmanager.types.site_to_site_vpn_attachment.serialize_json(
                value["site_to_site_vpn_attachment"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateSiteToSiteVpnAttachmentResponse:
    out: CreateSiteToSiteVpnAttachmentResponse = {}  # type: ignore[typeddict-item]
    if "SiteToSiteVpnAttachment" in data:
        import capo_networkmanager.types.site_to_site_vpn_attachment

        out["site_to_site_vpn_attachment"] = (
            capo_networkmanager.types.site_to_site_vpn_attachment.deserialize_json(
                data["SiteToSiteVpnAttachment"]
            )
        )
    return out
