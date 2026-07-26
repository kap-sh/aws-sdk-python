"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#DeleteAppInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_simspaceweaver.types.sim_space_weaver_resource_name


class DeleteAppInput(TypedDict, closed=True):
    simulation: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    """<p>The name of the simulation of the app.</p>"""
    domain: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    """<p>The name of the domain of the app.</p>"""
    app: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    """<p>The name of the app.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAppInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAppInput:
    out: DeleteAppInput = {}  # type: ignore[typeddict-item]
    return out
