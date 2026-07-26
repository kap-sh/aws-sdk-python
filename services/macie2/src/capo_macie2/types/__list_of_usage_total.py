"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfUsageTotal``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.usage_total

__listOfUsageTotal: TypeAlias = list["capo_macie2.types.usage_total.UsageTotal"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfUsageTotal) -> list:
    import capo_macie2.types.usage_total

    out: list = []
    for item in value:
        out.append(capo_macie2.types.usage_total.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfUsageTotal:
    import capo_macie2.types.usage_total

    out: __listOfUsageTotal = []
    for item in data:
        out.append(capo_macie2.types.usage_total.deserialize_json(item))
    return out
