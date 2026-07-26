"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#ListSimulationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_simspaceweaver.types.optional_string
    import capo_simspaceweaver.types.simulation_list


class ListSimulationsOutput(TypedDict, closed=True):
    simulations: NotRequired["capo_simspaceweaver.types.simulation_list.SimulationList"]
    """<p>The list of simulations.</p>"""
    next_token: NotRequired["capo_simspaceweaver.types.optional_string.OptionalString"]
    """<p>If SimSpace Weaver returns <code>nextToken</code>, then there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then <code>nextToken</code> is set to <code>null</code>. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an <i>HTTP 400 ValidationException</i> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSimulationsOutput) -> dict:
    out: dict = {}
    if "simulations" in value:
        import capo_simspaceweaver.types.simulation_list

        out["Simulations"] = capo_simspaceweaver.types.simulation_list.serialize_json(
            value["simulations"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSimulationsOutput:
    out: ListSimulationsOutput = {}  # type: ignore[typeddict-item]
    if "Simulations" in data:
        import capo_simspaceweaver.types.simulation_list

        out["simulations"] = capo_simspaceweaver.types.simulation_list.deserialize_json(
            data["Simulations"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
