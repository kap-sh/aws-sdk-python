"""Generated from Smithy shape ``com.amazonaws.outposts#ListSitesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.site_list_definition
    import capo_outposts.types.token


class ListSitesOutput(TypedDict, closed=True):
    sites: NotRequired["capo_outposts.types.site_list_definition.siteListDefinition"]
    next_token: NotRequired["capo_outposts.types.token.Token"]


# --- restJson1 ser/de ---
def serialize_json(value: ListSitesOutput) -> dict:
    out: dict = {}
    if "sites" in value:
        import capo_outposts.types.site_list_definition

        out["Sites"] = capo_outposts.types.site_list_definition.serialize_json(
            value["sites"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSitesOutput:
    out: ListSitesOutput = {}  # type: ignore[typeddict-item]
    if "Sites" in data:
        import capo_outposts.types.site_list_definition

        out["sites"] = capo_outposts.types.site_list_definition.deserialize_json(
            data["Sites"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
