"""Generated from Smithy shape ``com.amazonaws.greengrassv2#DeploymentConfigurationValidationPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.optional_integer


class DeploymentConfigurationValidationPolicy(TypedDict):
    timeout_in_seconds: NotRequired[
        "aws_sdk_greengrassv2.types.optional_integer.OptionalInteger"
    ]
    """<p>The amount of time in seconds that a component can validate its configuration updates. If the validation time exceeds this timeout, then the deployment proceeds for the device.</p> <p>Default: <code>30</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentConfigurationValidationPolicy) -> dict:
    out: dict = {}
    if "timeout_in_seconds" in value:
        out["timeoutInSeconds"] = value["timeout_in_seconds"]
    return out


def deserialize_json(data: dict) -> DeploymentConfigurationValidationPolicy:
    out: DeploymentConfigurationValidationPolicy = {}  # type: ignore[typeddict-item]
    if "timeoutInSeconds" in data:
        out["timeout_in_seconds"] = data["timeoutInSeconds"]
    return out
