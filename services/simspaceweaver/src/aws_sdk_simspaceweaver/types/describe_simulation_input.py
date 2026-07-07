"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#DescribeSimulationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_simspaceweaver.types.sim_space_weaver_resource_name


class DescribeSimulationInput(TypedDict, closed=True):
    simulation: "aws_sdk_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    """<p>The name of the simulation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSimulationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeSimulationInput:
    out: DescribeSimulationInput = {}  # type: ignore[typeddict-item]
    return out
