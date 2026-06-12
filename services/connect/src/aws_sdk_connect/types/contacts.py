"""Generated from Smithy shape ``com.amazonaws.connect#Contacts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_search_summary

Contacts: TypeAlias = list[
    "aws_sdk_connect.types.contact_search_summary.ContactSearchSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: Contacts) -> list:
    import aws_sdk_connect.types.contact_search_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.contact_search_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> Contacts:
    import aws_sdk_connect.types.contact_search_summary

    out: Contacts = []
    for item in data:
        out.append(aws_sdk_connect.types.contact_search_summary.deserialize_json(item))
    return out
