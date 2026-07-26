"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#ListAppsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_simspaceweaver.types.optional_string
    import capo_simspaceweaver.types.simulation_app_list


class ListAppsOutput(TypedDict, closed=True):
    apps: NotRequired["capo_simspaceweaver.types.simulation_app_list.SimulationAppList"]
    """<p>The list of apps for the given simulation and domain.</p>"""
    next_token: NotRequired["capo_simspaceweaver.types.optional_string.OptionalString"]
    """<p>If SimSpace Weaver returns <code>nextToken</code>, then there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then <code>nextToken</code> is set to <code>null</code>. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an <i>HTTP 400 ValidationException</i> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppsOutput) -> dict:
    out: dict = {}
    if "apps" in value:
        import capo_simspaceweaver.types.simulation_app_list

        out["Apps"] = capo_simspaceweaver.types.simulation_app_list.serialize_json(
            value["apps"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAppsOutput:
    out: ListAppsOutput = {}  # type: ignore[typeddict-item]
    if "Apps" in data:
        import capo_simspaceweaver.types.simulation_app_list

        out["apps"] = capo_simspaceweaver.types.simulation_app_list.deserialize_json(
            data["Apps"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
