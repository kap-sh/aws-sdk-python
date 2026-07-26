"""Generated from Smithy shape ``com.amazonaws.inspector2#UsageTotalList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.usage_total

UsageTotalList: TypeAlias = list["capo_inspector2.types.usage_total.UsageTotal"]


# --- restJson1 ser/de ---
def serialize_json(value: UsageTotalList) -> list:
    import capo_inspector2.types.usage_total

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.usage_total.serialize_json(item))
    return out


def deserialize_json(data: list) -> UsageTotalList:
    import capo_inspector2.types.usage_total

    out: UsageTotalList = []
    for item in data:
        out.append(capo_inspector2.types.usage_total.deserialize_json(item))
    return out
