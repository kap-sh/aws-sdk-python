"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeploymentSpecifications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_launch_wizard.types.key_string
    import capo_launch_wizard.types.value_string

DeploymentSpecifications: TypeAlias = dict[
    "capo_launch_wizard.types.key_string.KeyString",
    "capo_launch_wizard.types.value_string.ValueString",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DeploymentSpecifications) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> DeploymentSpecifications:
    out: DeploymentSpecifications = {}
    for key, value in data.items():
        out[key] = value
    return out
