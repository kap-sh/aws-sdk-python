"""Generated from Smithy shape ``com.amazonaws.inspector2#UsageTotalList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.usage_total

UsageTotalList: TypeAlias = list["aws_sdk_inspector2.types.usage_total.UsageTotal"]


# --- restJson1 ser/de ---
def serialize_json(value: UsageTotalList) -> list:
    import aws_sdk_inspector2.types.usage_total

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.usage_total.serialize_json(item))
    return out


def deserialize_json(data: list) -> UsageTotalList:
    import aws_sdk_inspector2.types.usage_total

    out: UsageTotalList = []
    for item in data:
        out.append(aws_sdk_inspector2.types.usage_total.deserialize_json(item))
    return out
