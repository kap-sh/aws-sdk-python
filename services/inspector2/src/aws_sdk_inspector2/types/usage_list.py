"""Generated from Smithy shape ``com.amazonaws.inspector2#UsageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.usage

UsageList: TypeAlias = list["aws_sdk_inspector2.types.usage.Usage"]


# --- restJson1 ser/de ---
def serialize_json(value: UsageList) -> list:
    import aws_sdk_inspector2.types.usage

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.usage.serialize_json(item))
    return out


def deserialize_json(data: list) -> UsageList:
    import aws_sdk_inspector2.types.usage

    out: UsageList = []
    for item in data:
        out.append(aws_sdk_inspector2.types.usage.deserialize_json(item))
    return out
