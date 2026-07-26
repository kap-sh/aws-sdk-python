"""Generated from Smithy shape ``com.amazonaws.cloudtrail#AdvancedEventSelectors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudtrail.types.advanced_event_selector

AdvancedEventSelectors: TypeAlias = list[
    "capo_cloudtrail.types.advanced_event_selector.AdvancedEventSelector"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdvancedEventSelectors) -> list:
    import capo_cloudtrail.types.advanced_event_selector

    out: list = []
    for item in value:
        out.append(
            capo_cloudtrail.types.advanced_event_selector.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AdvancedEventSelectors:
    import capo_cloudtrail.types.advanced_event_selector

    out: AdvancedEventSelectors = []
    for item in data:
        out.append(
            capo_cloudtrail.types.advanced_event_selector.deserialize_aws_json_1_1(item)
        )
    return out
