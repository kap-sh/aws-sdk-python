"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsServiceCapacityProviderStrategyDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsServiceCapacityProviderStrategyDetails(TypedDict):
    base: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The minimum number of tasks to run on the capacity provider. Only one strategy item can specify a value for <code>Base</code>.</p> <p>The value must be between 0 and 100000.</p>"""
    capacity_provider: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The short name of the capacity provider.</p>"""
    weight: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The relative percentage of the total number of tasks that should use the capacity provider.</p> <p>If no weight is specified, the default value is 0. At least one capacity provider must have a weight greater than 0.</p> <p>The value can be between 0 and 1000.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsServiceCapacityProviderStrategyDetails) -> dict:
    out: dict = {}
    if "base" in value:
        out["Base"] = value["base"]
    if "capacity_provider" in value:
        out["CapacityProvider"] = value["capacity_provider"]
    if "weight" in value:
        out["Weight"] = value["weight"]
    return out


def deserialize_json(data: dict) -> AwsEcsServiceCapacityProviderStrategyDetails:
    out: AwsEcsServiceCapacityProviderStrategyDetails = {}  # type: ignore[typeddict-item]
    if "Base" in data:
        out["base"] = data["Base"]
    if "CapacityProvider" in data:
        out["capacity_provider"] = data["CapacityProvider"]
    if "Weight" in data:
        out["weight"] = data["Weight"]
    return out
