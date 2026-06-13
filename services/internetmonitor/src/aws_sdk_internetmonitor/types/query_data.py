"""Generated from Smithy shape ``com.amazonaws.internetmonitor#QueryData``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_internetmonitor.types.query_row

QueryData: TypeAlias = list["aws_sdk_internetmonitor.types.query_row.QueryRow"]


# --- restJson1 ser/de ---
def serialize_json(value: QueryData) -> list:
    import aws_sdk_internetmonitor.types.query_row

    out: list = []
    for item in value:
        out.append(aws_sdk_internetmonitor.types.query_row.serialize_json(item))
    return out


def deserialize_json(data: list) -> QueryData:
    import aws_sdk_internetmonitor.types.query_row

    out: QueryData = []
    for item in data:
        out.append(aws_sdk_internetmonitor.types.query_row.deserialize_json(item))
    return out
