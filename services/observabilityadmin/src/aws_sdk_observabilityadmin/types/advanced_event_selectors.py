"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AdvancedEventSelectors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.advanced_event_selector

AdvancedEventSelectors: TypeAlias = list[
    "aws_sdk_observabilityadmin.types.advanced_event_selector.AdvancedEventSelector"
]


# --- restJson1 ser/de ---
def serialize_json(value: AdvancedEventSelectors) -> list:
    import aws_sdk_observabilityadmin.types.advanced_event_selector

    out: list = []
    for item in value:
        out.append(
            aws_sdk_observabilityadmin.types.advanced_event_selector.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AdvancedEventSelectors:
    import aws_sdk_observabilityadmin.types.advanced_event_selector

    out: AdvancedEventSelectors = []
    for item in data:
        out.append(
            aws_sdk_observabilityadmin.types.advanced_event_selector.deserialize_json(
                item
            )
        )
    return out
