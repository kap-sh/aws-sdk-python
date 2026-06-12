"""Generated from Smithy shape ``com.amazonaws.controltower#ResetEnabledBaselineInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.arn


class ResetEnabledBaselineInput(TypedDict):
    enabled_baseline_identifier: "aws_sdk_controltower.types.arn.Arn"
    """<p>Specifies the ID of the <code>EnabledBaseline</code> resource to be re-enabled, in ARN format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResetEnabledBaselineInput) -> dict:
    out: dict = {}
    out["enabledBaselineIdentifier"] = value["enabled_baseline_identifier"]
    return out


def deserialize_json(data: dict) -> ResetEnabledBaselineInput:
    out: ResetEnabledBaselineInput = {}  # type: ignore[typeddict-item]
    if "enabledBaselineIdentifier" in data:
        out["enabled_baseline_identifier"] = data["enabledBaselineIdentifier"]
    else:
        raise DeserializationError(
            "ResetEnabledBaselineInput.enabled_baseline_identifier required"
        )
    return out
