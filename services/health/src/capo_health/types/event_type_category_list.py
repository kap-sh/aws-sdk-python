"""Generated from Smithy shape ``com.amazonaws.health#EventTypeCategoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.event_type_category

EventTypeCategoryList: TypeAlias = list[
    "capo_health.types.event_type_category.eventTypeCategory"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventTypeCategoryList) -> list:
    import capo_health.types.event_type_category

    out: list = []
    for item in value:
        out.append(capo_health.types.event_type_category.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EventTypeCategoryList:
    import capo_health.types.event_type_category

    out: EventTypeCategoryList = []
    for item in data:
        out.append(capo_health.types.event_type_category.deserialize_aws_json_1_1(item))
    return out
