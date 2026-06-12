"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfResultRow``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.result_row

ListOfResultRow: TypeAlias = list["aws_sdk_pinpoint.types.result_row.ResultRow"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfResultRow) -> list:
    import aws_sdk_pinpoint.types.result_row

    out: list = []
    for item in value:
        out.append(aws_sdk_pinpoint.types.result_row.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfResultRow:
    import aws_sdk_pinpoint.types.result_row

    out: ListOfResultRow = []
    for item in data:
        out.append(aws_sdk_pinpoint.types.result_row.deserialize_json(item))
    return out
