"""Generated from Smithy shape ``com.amazonaws.networkmanager#DeleteSiteRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.site_id


class DeleteSiteRequest(TypedDict, closed=True):
    global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    site_id: "capo_networkmanager.types.site_id.SiteId"
    """<p>The ID of the site.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSiteRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSiteRequest:
    out: DeleteSiteRequest = {}  # type: ignore[typeddict-item]
    return out
