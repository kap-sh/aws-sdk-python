"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ListComponentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.component_list
    import capo_greengrassv2.types.next_token_string


class ListComponentsResponse(TypedDict, closed=True):
    components: NotRequired["capo_greengrassv2.types.component_list.ComponentList"]
    """<p>A list that summarizes each component.</p>"""
    next_token: NotRequired["capo_greengrassv2.types.next_token_string.NextTokenString"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListComponentsResponse) -> dict:
    out: dict = {}
    if "components" in value:
        import capo_greengrassv2.types.component_list

        out["components"] = capo_greengrassv2.types.component_list.serialize_json(
            value["components"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListComponentsResponse:
    out: ListComponentsResponse = {}  # type: ignore[typeddict-item]
    if "components" in data:
        import capo_greengrassv2.types.component_list

        out["components"] = capo_greengrassv2.types.component_list.deserialize_json(
            data["components"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
