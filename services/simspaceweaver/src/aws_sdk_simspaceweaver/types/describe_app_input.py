"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#DescribeAppInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_simspaceweaver.types.sim_space_weaver_long_resource_name
    import aws_sdk_simspaceweaver.types.sim_space_weaver_resource_name


class DescribeAppInput(TypedDict, closed=True):
    simulation: "aws_sdk_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    """<p>The name of the simulation of the app.</p>"""
    domain: "aws_sdk_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    """<p>The name of the domain of the app.</p>"""
    app: "aws_sdk_simspaceweaver.types.sim_space_weaver_long_resource_name.SimSpaceWeaverLongResourceName"
    """<p>The name of the app.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAppInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAppInput:
    out: DescribeAppInput = {}  # type: ignore[typeddict-item]
    return out
