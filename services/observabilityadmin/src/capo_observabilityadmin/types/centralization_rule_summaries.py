"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#CentralizationRuleSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.centralization_rule_summary

CentralizationRuleSummaries: TypeAlias = list[
    "capo_observabilityadmin.types.centralization_rule_summary.CentralizationRuleSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CentralizationRuleSummaries) -> list:
    import capo_observabilityadmin.types.centralization_rule_summary

    out: list = []
    for item in value:
        out.append(
            capo_observabilityadmin.types.centralization_rule_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CentralizationRuleSummaries:
    import capo_observabilityadmin.types.centralization_rule_summary

    out: CentralizationRuleSummaries = []
    for item in data:
        out.append(
            capo_observabilityadmin.types.centralization_rule_summary.deserialize_json(
                item
            )
        )
    return out
