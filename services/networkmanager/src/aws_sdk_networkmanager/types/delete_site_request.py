"""Generated from Smithy shape ``com.amazonaws.networkmanager#DeleteSiteRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.global_network_id
    import aws_sdk_networkmanager.types.site_id


class DeleteSiteRequest(TypedDict):
    global_network_id: "aws_sdk_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    site_id: "aws_sdk_networkmanager.types.site_id.SiteId"
    """<p>The ID of the site.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSiteRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSiteRequest:
    out: DeleteSiteRequest = {}  # type: ignore[typeddict-item]
    return out
