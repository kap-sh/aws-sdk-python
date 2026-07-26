"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfUsageRecord``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.usage_record

__listOfUsageRecord: TypeAlias = list["capo_macie2.types.usage_record.UsageRecord"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfUsageRecord) -> list:
    import capo_macie2.types.usage_record

    out: list = []
    for item in value:
        out.append(capo_macie2.types.usage_record.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfUsageRecord:
    import capo_macie2.types.usage_record

    out: __listOfUsageRecord = []
    for item in data:
        out.append(capo_macie2.types.usage_record.deserialize_json(item))
    return out
