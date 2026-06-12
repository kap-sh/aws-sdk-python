"""Generated from Smithy shape ``com.amazonaws.servicecatalog#TagOptionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.tag_option_summary

TagOptionSummaries: TypeAlias = list[
    "aws_sdk_service_catalog.types.tag_option_summary.TagOptionSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagOptionSummaries) -> list:
    import aws_sdk_service_catalog.types.tag_option_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_service_catalog.types.tag_option_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TagOptionSummaries:
    import aws_sdk_service_catalog.types.tag_option_summary

    out: TagOptionSummaries = []
    for item in data:
        out.append(
            aws_sdk_service_catalog.types.tag_option_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
