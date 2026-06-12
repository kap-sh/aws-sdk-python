"""Generated from Smithy shape ``com.amazonaws.sesv2#BulkEmailEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.bulk_email_entry

BulkEmailEntryList: TypeAlias = list[
    "aws_sdk_sesv2.types.bulk_email_entry.BulkEmailEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BulkEmailEntryList) -> list:
    import aws_sdk_sesv2.types.bulk_email_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_sesv2.types.bulk_email_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> BulkEmailEntryList:
    import aws_sdk_sesv2.types.bulk_email_entry

    out: BulkEmailEntryList = []
    for item in data:
        out.append(aws_sdk_sesv2.types.bulk_email_entry.deserialize_json(item))
    return out
