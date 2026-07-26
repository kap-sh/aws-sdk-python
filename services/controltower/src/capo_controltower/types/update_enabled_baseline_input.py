"""Generated from Smithy shape ``com.amazonaws.controltower#UpdateEnabledBaselineInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import capo_controltower.types.arn
    import capo_controltower.types.baseline_version
    import capo_controltower.types.enabled_baseline_parameters


class UpdateEnabledBaselineInput(TypedDict, closed=True):
    baseline_version: "capo_controltower.types.baseline_version.BaselineVersion"
    """<p>Specifies the new <code>Baseline</code> version, to which the <code>EnabledBaseline</code> should be updated.</p>"""
    parameters: NotRequired[
        "capo_controltower.types.enabled_baseline_parameters.EnabledBaselineParameters"
    ]
    """<p>Parameters to apply when making an update.</p>"""
    enabled_baseline_identifier: "capo_controltower.types.arn.Arn"
    """<p>Specifies the <code>EnabledBaseline</code> resource to be updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEnabledBaselineInput) -> dict:
    out: dict = {}
    out["baselineVersion"] = value["baseline_version"]
    if "parameters" in value:
        import capo_controltower.types.enabled_baseline_parameters

        out["parameters"] = (
            capo_controltower.types.enabled_baseline_parameters.serialize_json(
                value["parameters"]
            )
        )
    out["enabledBaselineIdentifier"] = value["enabled_baseline_identifier"]
    return out


def deserialize_json(data: dict) -> UpdateEnabledBaselineInput:
    out: UpdateEnabledBaselineInput = {}  # type: ignore[typeddict-item]
    if "baselineVersion" in data:
        out["baseline_version"] = data["baselineVersion"]
    else:
        raise DeserializationError(
            "UpdateEnabledBaselineInput.baseline_version required"
        )
    if "parameters" in data:
        import capo_controltower.types.enabled_baseline_parameters

        out["parameters"] = (
            capo_controltower.types.enabled_baseline_parameters.deserialize_json(
                data["parameters"]
            )
        )
    if "enabledBaselineIdentifier" in data:
        out["enabled_baseline_identifier"] = data["enabledBaselineIdentifier"]
    else:
        raise DeserializationError(
            "UpdateEnabledBaselineInput.enabled_baseline_identifier required"
        )
    return out
