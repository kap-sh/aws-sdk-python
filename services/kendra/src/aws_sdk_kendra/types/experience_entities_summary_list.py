"""Generated from Smithy shape ``com.amazonaws.kendra#ExperienceEntitiesSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.experience_entities_summary

ExperienceEntitiesSummaryList: TypeAlias = list[
    "aws_sdk_kendra.types.experience_entities_summary.ExperienceEntitiesSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExperienceEntitiesSummaryList) -> list:
    import aws_sdk_kendra.types.experience_entities_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kendra.types.experience_entities_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExperienceEntitiesSummaryList:
    import aws_sdk_kendra.types.experience_entities_summary

    out: ExperienceEntitiesSummaryList = []
    for item in data:
        out.append(
            aws_sdk_kendra.types.experience_entities_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
