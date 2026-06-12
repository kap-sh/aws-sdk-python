"""Generated from Smithy shape ``com.amazonaws.connectcases#SortList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.sort

SortList: TypeAlias = list["aws_sdk_connectcases.types.sort.Sort"]


# --- restJson1 ser/de ---
def serialize_json(value: SortList) -> list:
    import aws_sdk_connectcases.types.sort

    out: list = []
    for item in value:
        out.append(aws_sdk_connectcases.types.sort.serialize_json(item))
    return out


def deserialize_json(data: list) -> SortList:
    import aws_sdk_connectcases.types.sort

    out: SortList = []
    for item in data:
        out.append(aws_sdk_connectcases.types.sort.deserialize_json(item))
    return out
