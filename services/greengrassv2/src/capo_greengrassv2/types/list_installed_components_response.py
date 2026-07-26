"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ListInstalledComponentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.installed_component_list
    import capo_greengrassv2.types.next_token_string


class ListInstalledComponentsResponse(TypedDict, closed=True):
    installed_components: NotRequired[
        "capo_greengrassv2.types.installed_component_list.InstalledComponentList"
    ]
    """<p>A list that summarizes each component on the core device.</p> <note> <p>Greengrass nucleus v2.7.0 or later is required to get an accurate <code>lastStatusChangeTimestamp</code> response. This response can be inaccurate in earlier Greengrass nucleus versions.</p> </note> <note> <p>Greengrass nucleus v2.8.0 or later is required to get an accurate <code>lastInstallationSource</code> and <code>lastReportedTimestamp</code> response. This response can be inaccurate or null in earlier Greengrass nucleus versions.</p> </note>"""
    next_token: NotRequired["capo_greengrassv2.types.next_token_string.NextTokenString"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInstalledComponentsResponse) -> dict:
    out: dict = {}
    if "installed_components" in value:
        import capo_greengrassv2.types.installed_component_list

        out["installedComponents"] = (
            capo_greengrassv2.types.installed_component_list.serialize_json(
                value["installed_components"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInstalledComponentsResponse:
    out: ListInstalledComponentsResponse = {}  # type: ignore[typeddict-item]
    if "installedComponents" in data:
        import capo_greengrassv2.types.installed_component_list

        out["installed_components"] = (
            capo_greengrassv2.types.installed_component_list.deserialize_json(
                data["installedComponents"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
