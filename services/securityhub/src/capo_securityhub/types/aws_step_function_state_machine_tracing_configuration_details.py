"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsStepFunctionStateMachineTracingConfigurationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean


class AwsStepFunctionStateMachineTracingConfigurationDetails(TypedDict, closed=True):
    enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p> When set to true, X-Ray tracing is enabled. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsStepFunctionStateMachineTracingConfigurationDetails,
) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_json(
    data: dict,
) -> AwsStepFunctionStateMachineTracingConfigurationDetails:
    out: AwsStepFunctionStateMachineTracingConfigurationDetails = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    return out
