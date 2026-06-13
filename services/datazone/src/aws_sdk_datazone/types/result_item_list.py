"""Generated from Smithy shape ``com.amazonaws.datazone#ResultItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.result_item

ResultItemList: TypeAlias = list["aws_sdk_datazone.types.result_item.ResultItem"]


# --- restJson1 ser/de ---
def serialize_json(value: ResultItemList) -> list:
    import aws_sdk_datazone.types.result_item

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.result_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResultItemList:
    import aws_sdk_datazone.types.result_item

    out: ResultItemList = []
    for item in data:
        out.append(aws_sdk_datazone.types.result_item.deserialize_json(item))
    return out
