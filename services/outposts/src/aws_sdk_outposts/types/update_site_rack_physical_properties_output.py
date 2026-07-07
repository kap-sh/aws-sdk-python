"""Generated from Smithy shape ``com.amazonaws.outposts#UpdateSiteRackPhysicalPropertiesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.site


class UpdateSiteRackPhysicalPropertiesOutput(TypedDict, closed=True):
    site: NotRequired["aws_sdk_outposts.types.site.Site"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSiteRackPhysicalPropertiesOutput) -> dict:
    out: dict = {}
    if "site" in value:
        import aws_sdk_outposts.types.site

        out["Site"] = aws_sdk_outposts.types.site.serialize_json(value["site"])
    return out


def deserialize_json(data: dict) -> UpdateSiteRackPhysicalPropertiesOutput:
    out: UpdateSiteRackPhysicalPropertiesOutput = {}  # type: ignore[typeddict-item]
    if "Site" in data:
        import aws_sdk_outposts.types.site

        out["site"] = aws_sdk_outposts.types.site.deserialize_json(data["Site"])
    return out
