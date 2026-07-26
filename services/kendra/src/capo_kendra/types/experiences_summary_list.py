"""Generated from Smithy shape ``com.amazonaws.kendra#ExperiencesSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.experiences_summary

ExperiencesSummaryList: TypeAlias = list[
    "capo_kendra.types.experiences_summary.ExperiencesSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExperiencesSummaryList) -> list:
    import capo_kendra.types.experiences_summary

    out: list = []
    for item in value:
        out.append(capo_kendra.types.experiences_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ExperiencesSummaryList:
    import capo_kendra.types.experiences_summary

    out: ExperiencesSummaryList = []
    for item in data:
        out.append(capo_kendra.types.experiences_summary.deserialize_aws_json_1_1(item))
    return out
