"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ListComponentVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.component_version_list
    import capo_greengrassv2.types.next_token_string


class ListComponentVersionsResponse(TypedDict, closed=True):
    component_versions: NotRequired[
        "capo_greengrassv2.types.component_version_list.ComponentVersionList"
    ]
    """<p>A list of versions that exist for the component.</p>"""
    next_token: NotRequired["capo_greengrassv2.types.next_token_string.NextTokenString"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListComponentVersionsResponse) -> dict:
    out: dict = {}
    if "component_versions" in value:
        import capo_greengrassv2.types.component_version_list

        out["componentVersions"] = (
            capo_greengrassv2.types.component_version_list.serialize_json(
                value["component_versions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListComponentVersionsResponse:
    out: ListComponentVersionsResponse = {}  # type: ignore[typeddict-item]
    if "componentVersions" in data:
        import capo_greengrassv2.types.component_version_list

        out["component_versions"] = (
            capo_greengrassv2.types.component_version_list.deserialize_json(
                data["componentVersions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
