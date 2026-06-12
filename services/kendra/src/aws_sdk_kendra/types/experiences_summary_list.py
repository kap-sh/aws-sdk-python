"""Generated from Smithy shape ``com.amazonaws.kendra#ExperiencesSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.experiences_summary

ExperiencesSummaryList: TypeAlias = list[
    "aws_sdk_kendra.types.experiences_summary.ExperiencesSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExperiencesSummaryList) -> list:
    import aws_sdk_kendra.types.experiences_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kendra.types.experiences_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExperiencesSummaryList:
    import aws_sdk_kendra.types.experiences_summary

    out: ExperiencesSummaryList = []
    for item in data:
        out.append(
            aws_sdk_kendra.types.experiences_summary.deserialize_aws_json_1_1(item)
        )
    return out
