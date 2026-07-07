"""Generated from Smithy shape ``com.amazonaws.guardduty#FreeTrialFeatureConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.free_trial_feature_result
    import aws_sdk_guardduty.types.integer


class FreeTrialFeatureConfigurationResult(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_guardduty.types.free_trial_feature_result.FreeTrialFeatureResult"
    ]
    """<p>The name of the feature for which the free trial is configured.</p>"""
    free_trial_days_remaining: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>The number of the remaining free trial days for the feature.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FreeTrialFeatureConfigurationResult) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_guardduty.types.free_trial_feature_result

        out["name"] = aws_sdk_guardduty.types.free_trial_feature_result.serialize_json(
            value["name"]
        )
    if "free_trial_days_remaining" in value:
        out["freeTrialDaysRemaining"] = value["free_trial_days_remaining"]
    return out


def deserialize_json(data: dict) -> FreeTrialFeatureConfigurationResult:
    out: FreeTrialFeatureConfigurationResult = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_guardduty.types.free_trial_feature_result

        out["name"] = (
            aws_sdk_guardduty.types.free_trial_feature_result.deserialize_json(
                data["name"]
            )
        )
    if "freeTrialDaysRemaining" in data:
        out["free_trial_days_remaining"] = data["freeTrialDaysRemaining"]
    return out
