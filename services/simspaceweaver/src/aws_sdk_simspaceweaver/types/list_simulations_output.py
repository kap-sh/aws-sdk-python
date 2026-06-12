"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#ListSimulationsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_simspaceweaver.types.optional_string
    import aws_sdk_simspaceweaver.types.simulation_list


class ListSimulationsOutput(TypedDict):
    simulations: NotRequired[
        "aws_sdk_simspaceweaver.types.simulation_list.SimulationList"
    ]
    """<p>The list of simulations.</p>"""
    next_token: NotRequired[
        "aws_sdk_simspaceweaver.types.optional_string.OptionalString"
    ]
    """<p>If SimSpace Weaver returns <code>nextToken</code>, then there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then <code>nextToken</code> is set to <code>null</code>. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an <i>HTTP 400 ValidationException</i> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSimulationsOutput) -> dict:
    out: dict = {}
    if "simulations" in value:
        import aws_sdk_simspaceweaver.types.simulation_list

        out["Simulations"] = (
            aws_sdk_simspaceweaver.types.simulation_list.serialize_json(
                value["simulations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSimulationsOutput:
    out: ListSimulationsOutput = {}  # type: ignore[typeddict-item]
    if "Simulations" in data:
        import aws_sdk_simspaceweaver.types.simulation_list

        out["simulations"] = (
            aws_sdk_simspaceweaver.types.simulation_list.deserialize_json(
                data["Simulations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
