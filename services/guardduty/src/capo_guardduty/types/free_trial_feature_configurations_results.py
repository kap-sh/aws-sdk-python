"""Generated from Smithy shape ``com.amazonaws.guardduty#FreeTrialFeatureConfigurationsResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.free_trial_feature_configuration_result

FreeTrialFeatureConfigurationsResults: TypeAlias = list[
    "capo_guardduty.types.free_trial_feature_configuration_result.FreeTrialFeatureConfigurationResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: FreeTrialFeatureConfigurationsResults) -> list:
    import capo_guardduty.types.free_trial_feature_configuration_result

    out: list = []
    for item in value:
        out.append(
            capo_guardduty.types.free_trial_feature_configuration_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FreeTrialFeatureConfigurationsResults:
    import capo_guardduty.types.free_trial_feature_configuration_result

    out: FreeTrialFeatureConfigurationsResults = []
    for item in data:
        out.append(
            capo_guardduty.types.free_trial_feature_configuration_result.deserialize_json(
                item
            )
        )
    return out
