"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetSiteToSiteVpnAttachmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.site_to_site_vpn_attachment


class GetSiteToSiteVpnAttachmentResponse(TypedDict, closed=True):
    site_to_site_vpn_attachment: NotRequired[
        "aws_sdk_networkmanager.types.site_to_site_vpn_attachment.SiteToSiteVpnAttachment"
    ]
    """<p>Describes the site-to-site attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSiteToSiteVpnAttachmentResponse) -> dict:
    out: dict = {}
    if "site_to_site_vpn_attachment" in value:
        import aws_sdk_networkmanager.types.site_to_site_vpn_attachment

        out["SiteToSiteVpnAttachment"] = (
            aws_sdk_networkmanager.types.site_to_site_vpn_attachment.serialize_json(
                value["site_to_site_vpn_attachment"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSiteToSiteVpnAttachmentResponse:
    out: GetSiteToSiteVpnAttachmentResponse = {}  # type: ignore[typeddict-item]
    if "SiteToSiteVpnAttachment" in data:
        import aws_sdk_networkmanager.types.site_to_site_vpn_attachment

        out["site_to_site_vpn_attachment"] = (
            aws_sdk_networkmanager.types.site_to_site_vpn_attachment.deserialize_json(
                data["SiteToSiteVpnAttachment"]
            )
        )
    return out
