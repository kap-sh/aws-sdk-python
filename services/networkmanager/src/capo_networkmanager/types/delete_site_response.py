"""Generated from Smithy shape ``com.amazonaws.networkmanager#DeleteSiteResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.site


class DeleteSiteResponse(TypedDict, closed=True):
    site: NotRequired["capo_networkmanager.types.site.Site"]
    """<p>Information about the site.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSiteResponse) -> dict:
    out: dict = {}
    if "site" in value:
        import capo_networkmanager.types.site

        out["Site"] = capo_networkmanager.types.site.serialize_json(value["site"])
    return out


def deserialize_json(data: dict) -> DeleteSiteResponse:
    out: DeleteSiteResponse = {}  # type: ignore[typeddict-item]
    if "Site" in data:
        import capo_networkmanager.types.site

        out["site"] = capo_networkmanager.types.site.deserialize_json(data["Site"])
    return out
