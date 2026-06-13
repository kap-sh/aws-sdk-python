"""Generated from Smithy shape ``com.amazonaws.datazone#RuleSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.rule_summary

RuleSummaries: TypeAlias = list["aws_sdk_datazone.types.rule_summary.RuleSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: RuleSummaries) -> list:
    import aws_sdk_datazone.types.rule_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.rule_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> RuleSummaries:
    import aws_sdk_datazone.types.rule_summary

    out: RuleSummaries = []
    for item in data:
        out.append(aws_sdk_datazone.types.rule_summary.deserialize_json(item))
    return out
