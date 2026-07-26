"""Generated from Smithy shape ``com.amazonaws.outposts#siteListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_outposts.types.site

siteListDefinition: TypeAlias = list["capo_outposts.types.site.Site"]


# --- restJson1 ser/de ---
def serialize_json(value: siteListDefinition) -> list:
    import capo_outposts.types.site

    out: list = []
    for item in value:
        out.append(capo_outposts.types.site.serialize_json(item))
    return out


def deserialize_json(data: list) -> siteListDefinition:
    import capo_outposts.types.site

    out: siteListDefinition = []
    for item in data:
        out.append(capo_outposts.types.site.deserialize_json(item))
    return out
