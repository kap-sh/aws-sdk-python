"""Generated from Smithy shape ``com.amazonaws.resiliencehub#RecommendationItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.alarm
    import capo_resiliencehub.types.aws_region
    import capo_resiliencehub.types.boolean_optional
    import capo_resiliencehub.types.customer_id
    import capo_resiliencehub.types.exclude_recommendation_reason
    import capo_resiliencehub.types.experiment
    import capo_resiliencehub.types.string500


class RecommendationItem(TypedDict, closed=True):
    resource_id: NotRequired["capo_resiliencehub.types.string500.String500"]
    """<p>Identifier of the resource.</p>"""
    target_account_id: NotRequired["capo_resiliencehub.types.customer_id.CustomerId"]
    """<p>Identifier of the target account.</p>"""
    target_region: NotRequired["capo_resiliencehub.types.aws_region.AwsRegion"]
    """<p>The target region.</p>"""
    already_implemented: NotRequired[
        "capo_resiliencehub.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies if the recommendation has already been implemented.</p>"""
    excluded: NotRequired["capo_resiliencehub.types.boolean_optional.BooleanOptional"]
    """<p>Indicates if an operational recommendation item is excluded.</p>"""
    exclude_reason: NotRequired[
        "capo_resiliencehub.types.exclude_recommendation_reason.ExcludeRecommendationReason"
    ]
    """<p>Indicates the reason for excluding an operational recommendation.</p>"""
    latest_discovered_experiment: NotRequired[
        "capo_resiliencehub.types.experiment.Experiment"
    ]
    """<p>Indicates the experiment created in FIS that was discovered by Resilience Hub, which matches the recommendation.</p>"""
    discovered_alarm: NotRequired["capo_resiliencehub.types.alarm.Alarm"]
    """<p>Indicates the previously implemented Amazon CloudWatch alarm discovered by Resilience Hub.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationItem) -> dict:
    out: dict = {}
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "target_account_id" in value:
        out["targetAccountId"] = value["target_account_id"]
    if "target_region" in value:
        out["targetRegion"] = value["target_region"]
    if "already_implemented" in value:
        out["alreadyImplemented"] = value["already_implemented"]
    if "excluded" in value:
        out["excluded"] = value["excluded"]
    if "exclude_reason" in value:
        import capo_resiliencehub.types.exclude_recommendation_reason

        out["excludeReason"] = (
            capo_resiliencehub.types.exclude_recommendation_reason.serialize_json(
                value["exclude_reason"]
            )
        )
    if "latest_discovered_experiment" in value:
        import capo_resiliencehub.types.experiment

        out["latestDiscoveredExperiment"] = (
            capo_resiliencehub.types.experiment.serialize_json(
                value["latest_discovered_experiment"]
            )
        )
    if "discovered_alarm" in value:
        import capo_resiliencehub.types.alarm

        out["discoveredAlarm"] = capo_resiliencehub.types.alarm.serialize_json(
            value["discovered_alarm"]
        )
    return out


def deserialize_json(data: dict) -> RecommendationItem:
    out: RecommendationItem = {}  # type: ignore[typeddict-item]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "targetAccountId" in data:
        out["target_account_id"] = data["targetAccountId"]
    if "targetRegion" in data:
        out["target_region"] = data["targetRegion"]
    if "alreadyImplemented" in data:
        out["already_implemented"] = data["alreadyImplemented"]
    if "excluded" in data:
        out["excluded"] = data["excluded"]
    if "excludeReason" in data:
        import capo_resiliencehub.types.exclude_recommendation_reason

        out["exclude_reason"] = (
            capo_resiliencehub.types.exclude_recommendation_reason.deserialize_json(
                data["excludeReason"]
            )
        )
    if "latestDiscoveredExperiment" in data:
        import capo_resiliencehub.types.experiment

        out["latest_discovered_experiment"] = (
            capo_resiliencehub.types.experiment.deserialize_json(
                data["latestDiscoveredExperiment"]
            )
        )
    if "discoveredAlarm" in data:
        import capo_resiliencehub.types.alarm

        out["discovered_alarm"] = capo_resiliencehub.types.alarm.deserialize_json(
            data["discoveredAlarm"]
        )
    return out
