"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DifferentialPrivacyPrivacyBudgetAggregationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.differential_privacy_privacy_budget_aggregation

DifferentialPrivacyPrivacyBudgetAggregationList: TypeAlias = list[
    "capo_cleanrooms.types.differential_privacy_privacy_budget_aggregation.DifferentialPrivacyPrivacyBudgetAggregation"
]


# --- restJson1 ser/de ---
def serialize_json(value: DifferentialPrivacyPrivacyBudgetAggregationList) -> list:
    import capo_cleanrooms.types.differential_privacy_privacy_budget_aggregation

    out: list = []
    for item in value:
        out.append(
            capo_cleanrooms.types.differential_privacy_privacy_budget_aggregation.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DifferentialPrivacyPrivacyBudgetAggregationList:
    import capo_cleanrooms.types.differential_privacy_privacy_budget_aggregation

    out: DifferentialPrivacyPrivacyBudgetAggregationList = []
    for item in data:
        out.append(
            capo_cleanrooms.types.differential_privacy_privacy_budget_aggregation.deserialize_json(
                item
            )
        )
    return out
