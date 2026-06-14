"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#LiveSimulationState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_simspaceweaver.types.domain_list
    import aws_sdk_simspaceweaver.types.simulation_clock_list


class LiveSimulationState(TypedDict):
    domains: NotRequired["aws_sdk_simspaceweaver.types.domain_list.DomainList"]
    r"""<p>A list of domains for the simulation. For more information about domains, see <a href=\"https://docs.aws.amazon.com/simspaceweaver/latest/userguide/what-is_key-concepts.html#what-is_key-concepts_domains\">Key concepts: Domains</a> in the <i>SimSpace Weaver User Guide</i>.</p>"""
    clocks: NotRequired[
        "aws_sdk_simspaceweaver.types.simulation_clock_list.SimulationClockList"
    ]
    """<p>A list of simulation clocks.</p> <note> <p>At this time, a simulation has only one clock.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: LiveSimulationState) -> dict:
    out: dict = {}
    if "domains" in value:
        import aws_sdk_simspaceweaver.types.domain_list

        out["Domains"] = aws_sdk_simspaceweaver.types.domain_list.serialize_json(
            value["domains"]
        )
    if "clocks" in value:
        import aws_sdk_simspaceweaver.types.simulation_clock_list

        out["Clocks"] = (
            aws_sdk_simspaceweaver.types.simulation_clock_list.serialize_json(
                value["clocks"]
            )
        )
    return out


def deserialize_json(data: dict) -> LiveSimulationState:
    out: LiveSimulationState = {}  # type: ignore[typeddict-item]
    if "Domains" in data:
        import aws_sdk_simspaceweaver.types.domain_list

        out["domains"] = aws_sdk_simspaceweaver.types.domain_list.deserialize_json(
            data["Domains"]
        )
    if "Clocks" in data:
        import aws_sdk_simspaceweaver.types.simulation_clock_list

        out["clocks"] = (
            aws_sdk_simspaceweaver.types.simulation_clock_list.deserialize_json(
                data["Clocks"]
            )
        )
    return out
