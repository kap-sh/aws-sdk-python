"""Generated from Smithy shape ``com.amazonaws.personalize#Filters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize.types.filter_summary

Filters: TypeAlias = list["aws_sdk_personalize.types.filter_summary.FilterSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Filters) -> list:
    import aws_sdk_personalize.types.filter_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_personalize.types.filter_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> Filters:
    import aws_sdk_personalize.types.filter_summary

    out: Filters = []
    for item in data:
        out.append(
            aws_sdk_personalize.types.filter_summary.deserialize_aws_json_1_1(item)
        )
    return out
