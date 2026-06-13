"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedListingInputs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.subscribed_listing_input

SubscribedListingInputs: TypeAlias = list[
    "aws_sdk_datazone.types.subscribed_listing_input.SubscribedListingInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedListingInputs) -> list:
    import aws_sdk_datazone.types.subscribed_listing_input

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.subscribed_listing_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> SubscribedListingInputs:
    import aws_sdk_datazone.types.subscribed_listing_input

    out: SubscribedListingInputs = []
    for item in data:
        out.append(
            aws_sdk_datazone.types.subscribed_listing_input.deserialize_json(item)
        )
    return out
