"""Generated from Smithy shape ``com.amazonaws.kendra#ThesaurusSummaryItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.thesaurus_summary

ThesaurusSummaryItems: TypeAlias = list[
    "aws_sdk_kendra.types.thesaurus_summary.ThesaurusSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThesaurusSummaryItems) -> list:
    import aws_sdk_kendra.types.thesaurus_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_kendra.types.thesaurus_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ThesaurusSummaryItems:
    import aws_sdk_kendra.types.thesaurus_summary

    out: ThesaurusSummaryItems = []
    for item in data:
        out.append(
            aws_sdk_kendra.types.thesaurus_summary.deserialize_aws_json_1_1(item)
        )
    return out
