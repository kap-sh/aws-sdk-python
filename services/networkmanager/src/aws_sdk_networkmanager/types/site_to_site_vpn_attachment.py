"""Generated from Smithy shape ``com.amazonaws.networkmanager#SiteToSiteVpnAttachment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.attachment
    import aws_sdk_networkmanager.types.vpn_connection_arn


class SiteToSiteVpnAttachment(TypedDict):
    attachment: NotRequired["aws_sdk_networkmanager.types.attachment.Attachment"]
    """<p>Provides details about a site-to-site VPN attachment.</p>"""
    vpn_connection_arn: NotRequired[
        "aws_sdk_networkmanager.types.vpn_connection_arn.VpnConnectionArn"
    ]
    """<p>The ARN of the site-to-site VPN attachment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SiteToSiteVpnAttachment) -> dict:
    out: dict = {}
    if "attachment" in value:
        import aws_sdk_networkmanager.types.attachment

        out["Attachment"] = aws_sdk_networkmanager.types.attachment.serialize_json(
            value["attachment"]
        )
    if "vpn_connection_arn" in value:
        out["VpnConnectionArn"] = value["vpn_connection_arn"]
    return out


def deserialize_json(data: dict) -> SiteToSiteVpnAttachment:
    out: SiteToSiteVpnAttachment = {}  # type: ignore[typeddict-item]
    if "Attachment" in data:
        import aws_sdk_networkmanager.types.attachment

        out["attachment"] = aws_sdk_networkmanager.types.attachment.deserialize_json(
            data["Attachment"]
        )
    if "VpnConnectionArn" in data:
        out["vpn_connection_arn"] = data["VpnConnectionArn"]
    return out
