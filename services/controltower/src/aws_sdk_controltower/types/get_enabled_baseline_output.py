"""Generated from Smithy shape ``com.amazonaws.controltower#GetEnabledBaselineOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_controltower.types.enabled_baseline_details


class GetEnabledBaselineOutput(TypedDict, closed=True):
    enabled_baseline_details: NotRequired[
        "aws_sdk_controltower.types.enabled_baseline_details.EnabledBaselineDetails"
    ]
    """<p>Details of the <code>EnabledBaseline</code> resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnabledBaselineOutput) -> dict:
    out: dict = {}
    if "enabled_baseline_details" in value:
        import aws_sdk_controltower.types.enabled_baseline_details

        out["enabledBaselineDetails"] = (
            aws_sdk_controltower.types.enabled_baseline_details.serialize_json(
                value["enabled_baseline_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetEnabledBaselineOutput:
    out: GetEnabledBaselineOutput = {}  # type: ignore[typeddict-item]
    if "enabledBaselineDetails" in data:
        import aws_sdk_controltower.types.enabled_baseline_details

        out["enabled_baseline_details"] = (
            aws_sdk_controltower.types.enabled_baseline_details.deserialize_json(
                data["enabledBaselineDetails"]
            )
        )
    return out
