"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeploymentSpecifications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.key_string
    import aws_sdk_launch_wizard.types.value_string

DeploymentSpecifications: TypeAlias = dict[
    "aws_sdk_launch_wizard.types.key_string.KeyString",
    "aws_sdk_launch_wizard.types.value_string.ValueString",
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
