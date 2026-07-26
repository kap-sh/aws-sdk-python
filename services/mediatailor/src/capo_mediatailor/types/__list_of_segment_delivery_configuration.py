"""Generated from Smithy shape ``com.amazonaws.mediatailor#__listOfSegmentDeliveryConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediatailor.types.segment_delivery_configuration

__listOfSegmentDeliveryConfiguration: TypeAlias = list[
    "capo_mediatailor.types.segment_delivery_configuration.SegmentDeliveryConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSegmentDeliveryConfiguration) -> list:
    import capo_mediatailor.types.segment_delivery_configuration

    out: list = []
    for item in value:
        out.append(
            capo_mediatailor.types.segment_delivery_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfSegmentDeliveryConfiguration:
    import capo_mediatailor.types.segment_delivery_configuration

    out: __listOfSegmentDeliveryConfiguration = []
    for item in data:
        out.append(
            capo_mediatailor.types.segment_delivery_configuration.deserialize_json(item)
        )
    return out
