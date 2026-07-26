"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#AccountRecommendationLifecycleSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_trustedadvisor.types.account_recommendation_lifecycle_summary

AccountRecommendationLifecycleSummaryList: TypeAlias = list[
    "capo_trustedadvisor.types.account_recommendation_lifecycle_summary.AccountRecommendationLifecycleSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountRecommendationLifecycleSummaryList) -> list:
    import capo_trustedadvisor.types.account_recommendation_lifecycle_summary

    out: list = []
    for item in value:
        out.append(
            capo_trustedadvisor.types.account_recommendation_lifecycle_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AccountRecommendationLifecycleSummaryList:
    import capo_trustedadvisor.types.account_recommendation_lifecycle_summary

    out: AccountRecommendationLifecycleSummaryList = []
    for item in data:
        out.append(
            capo_trustedadvisor.types.account_recommendation_lifecycle_summary.deserialize_json(
                item
            )
        )
    return out
