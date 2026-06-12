"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsClusterDefaultCapacityProviderStrategyDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsClusterDefaultCapacityProviderStrategyDetails(TypedDict):
    base: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The minimum number of tasks to run on the specified capacity provider.</p>"""
    capacity_provider: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the capacity provider.</p>"""
    weight: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The relative percentage of the total number of tasks launched that should use the capacity provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsClusterDefaultCapacityProviderStrategyDetails) -> dict:
    out: dict = {}
    if "base" in value:
        out["Base"] = value["base"]
    if "capacity_provider" in value:
        out["CapacityProvider"] = value["capacity_provider"]
    if "weight" in value:
        out["Weight"] = value["weight"]
    return out


def deserialize_json(data: dict) -> AwsEcsClusterDefaultCapacityProviderStrategyDetails:
    out: AwsEcsClusterDefaultCapacityProviderStrategyDetails = {}  # type: ignore[typeddict-item]
    if "Base" in data:
        out["base"] = data["Base"]
    if "CapacityProvider" in data:
        out["capacity_provider"] = data["CapacityProvider"]
    if "Weight" in data:
        out["weight"] = data["Weight"]
    return out
