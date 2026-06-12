"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#CentralizationRuleSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.centralization_rule_summary

CentralizationRuleSummaries: TypeAlias = list[
    "aws_sdk_observabilityadmin.types.centralization_rule_summary.CentralizationRuleSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CentralizationRuleSummaries) -> list:
    import aws_sdk_observabilityadmin.types.centralization_rule_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_observabilityadmin.types.centralization_rule_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CentralizationRuleSummaries:
    import aws_sdk_observabilityadmin.types.centralization_rule_summary

    out: CentralizationRuleSummaries = []
    for item in data:
        out.append(
            aws_sdk_observabilityadmin.types.centralization_rule_summary.deserialize_json(
                item
            )
        )
    return out
