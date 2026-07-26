"""Generated from Smithy shape ``com.amazonaws.outposts#GetSiteInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.site_id


class GetSiteInput(TypedDict, closed=True):
    site_id: "capo_outposts.types.site_id.SiteId"
    """<p> The ID or the Amazon Resource Name (ARN) of the site. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSiteInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSiteInput:
    out: GetSiteInput = {}  # type: ignore[typeddict-item]
    return out
