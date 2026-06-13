"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedListings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.subscribed_listing

SubscribedListings: TypeAlias = list[
    "aws_sdk_datazone.types.subscribed_listing.SubscribedListing"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedListings) -> list:
    import aws_sdk_datazone.types.subscribed_listing

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.subscribed_listing.serialize_json(item))
    return out


def deserialize_json(data: list) -> SubscribedListings:
    import aws_sdk_datazone.types.subscribed_listing

    out: SubscribedListings = []
    for item in data:
        out.append(aws_sdk_datazone.types.subscribed_listing.deserialize_json(item))
    return out
