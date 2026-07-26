"""Generated from Smithy shape ``com.amazonaws.guardduty#AccountFreeTrialInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.data_sources_free_trial
    import capo_guardduty.types.free_trial_feature_configurations_results
    import capo_guardduty.types.string


class AccountFreeTrialInfo(TypedDict, closed=True):
    account_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The account identifier of the GuardDuty member account.</p>"""
    data_sources: NotRequired[
        "capo_guardduty.types.data_sources_free_trial.DataSourcesFreeTrial"
    ]
    """<p>Describes the data source enabled for the GuardDuty member account.</p>"""
    features: NotRequired[
        "capo_guardduty.types.free_trial_feature_configurations_results.FreeTrialFeatureConfigurationsResults"
    ]
    """<p>A list of features enabled for the GuardDuty account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountFreeTrialInfo) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "data_sources" in value:
        import capo_guardduty.types.data_sources_free_trial

        out["dataSources"] = (
            capo_guardduty.types.data_sources_free_trial.serialize_json(
                value["data_sources"]
            )
        )
    if "features" in value:
        import capo_guardduty.types.free_trial_feature_configurations_results

        out["features"] = (
            capo_guardduty.types.free_trial_feature_configurations_results.serialize_json(
                value["features"]
            )
        )
    return out


def deserialize_json(data: dict) -> AccountFreeTrialInfo:
    out: AccountFreeTrialInfo = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "dataSources" in data:
        import capo_guardduty.types.data_sources_free_trial

        out["data_sources"] = (
            capo_guardduty.types.data_sources_free_trial.deserialize_json(
                data["dataSources"]
            )
        )
    if "features" in data:
        import capo_guardduty.types.free_trial_feature_configurations_results

        out["features"] = (
            capo_guardduty.types.free_trial_feature_configurations_results.deserialize_json(
                data["features"]
            )
        )
    return out
