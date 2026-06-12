"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ArchiveRulesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.archive_rule_summary

ArchiveRulesList: TypeAlias = list[
    "aws_sdk_accessanalyzer.types.archive_rule_summary.ArchiveRuleSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ArchiveRulesList) -> list:
    import aws_sdk_accessanalyzer.types.archive_rule_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_accessanalyzer.types.archive_rule_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ArchiveRulesList:
    import aws_sdk_accessanalyzer.types.archive_rule_summary

    out: ArchiveRulesList = []
    for item in data:
        out.append(
            aws_sdk_accessanalyzer.types.archive_rule_summary.deserialize_json(item)
        )
    return out
