"""Generated from Smithy shape ``com.amazonaws.outposts#DeleteSiteInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.site_id


class DeleteSiteInput(TypedDict):
    site_id: "aws_sdk_outposts.types.site_id.SiteId"
    """<p> The ID or the Amazon Resource Name (ARN) of the site. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSiteInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSiteInput:
    out: DeleteSiteInput = {}  # type: ignore[typeddict-item]
    return out
