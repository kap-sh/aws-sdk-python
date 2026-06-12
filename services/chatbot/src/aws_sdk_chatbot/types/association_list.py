"""Generated from Smithy shape ``com.amazonaws.chatbot#AssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.association_listing

AssociationList: TypeAlias = list[
    "aws_sdk_chatbot.types.association_listing.AssociationListing"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociationList) -> list:
    import aws_sdk_chatbot.types.association_listing

    out: list = []
    for item in value:
        out.append(aws_sdk_chatbot.types.association_listing.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssociationList:
    import aws_sdk_chatbot.types.association_listing

    out: AssociationList = []
    for item in data:
        out.append(aws_sdk_chatbot.types.association_listing.deserialize_json(item))
    return out
