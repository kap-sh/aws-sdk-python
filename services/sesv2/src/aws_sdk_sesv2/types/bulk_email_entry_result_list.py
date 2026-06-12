"""Generated from Smithy shape ``com.amazonaws.sesv2#BulkEmailEntryResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.bulk_email_entry_result

BulkEmailEntryResultList: TypeAlias = list[
    "aws_sdk_sesv2.types.bulk_email_entry_result.BulkEmailEntryResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: BulkEmailEntryResultList) -> list:
    import aws_sdk_sesv2.types.bulk_email_entry_result

    out: list = []
    for item in value:
        out.append(aws_sdk_sesv2.types.bulk_email_entry_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> BulkEmailEntryResultList:
    import aws_sdk_sesv2.types.bulk_email_entry_result

    out: BulkEmailEntryResultList = []
    for item in data:
        out.append(aws_sdk_sesv2.types.bulk_email_entry_result.deserialize_json(item))
    return out
