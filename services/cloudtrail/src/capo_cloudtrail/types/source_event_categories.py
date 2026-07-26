"""Generated from Smithy shape ``com.amazonaws.cloudtrail#SourceEventCategories``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudtrail.types.source_event_category

SourceEventCategories: TypeAlias = list[
    "capo_cloudtrail.types.source_event_category.SourceEventCategory"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceEventCategories) -> list:
    import capo_cloudtrail.types.source_event_category

    out: list = []
    for item in value:
        out.append(
            capo_cloudtrail.types.source_event_category.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SourceEventCategories:
    import capo_cloudtrail.types.source_event_category

    out: SourceEventCategories = []
    for item in data:
        out.append(
            capo_cloudtrail.types.source_event_category.deserialize_aws_json_1_1(item)
        )
    return out
