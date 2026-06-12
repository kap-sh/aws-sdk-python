"""Generated from Smithy shape ``com.amazonaws.outposts#UpdateSiteInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.site_description
    import aws_sdk_outposts.types.site_id
    import aws_sdk_outposts.types.site_name
    import aws_sdk_outposts.types.site_notes


class UpdateSiteInput(TypedDict):
    site_id: "aws_sdk_outposts.types.site_id.SiteId"
    """<p> The ID or the Amazon Resource Name (ARN) of the site. </p>"""
    name: NotRequired["aws_sdk_outposts.types.site_name.SiteName"]
    description: NotRequired["aws_sdk_outposts.types.site_description.SiteDescription"]
    notes: NotRequired["aws_sdk_outposts.types.site_notes.SiteNotes"]
    """<p>Notes about a site.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSiteInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "notes" in value:
        out["Notes"] = value["notes"]
    return out


def deserialize_json(data: dict) -> UpdateSiteInput:
    out: UpdateSiteInput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Notes" in data:
        out["notes"] = data["Notes"]
    return out
