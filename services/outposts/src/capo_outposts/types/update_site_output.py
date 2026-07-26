"""Generated from Smithy shape ``com.amazonaws.outposts#UpdateSiteOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.site


class UpdateSiteOutput(TypedDict, closed=True):
    site: NotRequired["capo_outposts.types.site.Site"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSiteOutput) -> dict:
    out: dict = {}
    if "site" in value:
        import capo_outposts.types.site

        out["Site"] = capo_outposts.types.site.serialize_json(value["site"])
    return out


def deserialize_json(data: dict) -> UpdateSiteOutput:
    out: UpdateSiteOutput = {}  # type: ignore[typeddict-item]
    if "Site" in data:
        import capo_outposts.types.site

        out["site"] = capo_outposts.types.site.deserialize_json(data["Site"])
    return out
