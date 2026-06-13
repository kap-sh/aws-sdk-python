"""Generated from Smithy shape ``com.amazonaws.backupsearch#Results``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backupsearch.types.result_item

Results: TypeAlias = list["aws_sdk_backupsearch.types.result_item.ResultItem"]


# --- restJson1 ser/de ---
def serialize_json(value: Results) -> list:
    import aws_sdk_backupsearch.types.result_item

    out: list = []
    for item in value:
        out.append(aws_sdk_backupsearch.types.result_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> Results:
    import aws_sdk_backupsearch.types.result_item

    out: Results = []
    for item in data:
        out.append(aws_sdk_backupsearch.types.result_item.deserialize_json(item))
    return out
