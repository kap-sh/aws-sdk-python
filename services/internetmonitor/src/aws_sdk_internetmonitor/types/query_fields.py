"""Generated from Smithy shape ``com.amazonaws.internetmonitor#QueryFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_internetmonitor.types.query_field

QueryFields: TypeAlias = list["aws_sdk_internetmonitor.types.query_field.QueryField"]


# --- restJson1 ser/de ---
def serialize_json(value: QueryFields) -> list:
    import aws_sdk_internetmonitor.types.query_field

    out: list = []
    for item in value:
        out.append(aws_sdk_internetmonitor.types.query_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> QueryFields:
    import aws_sdk_internetmonitor.types.query_field

    out: QueryFields = []
    for item in data:
        out.append(aws_sdk_internetmonitor.types.query_field.deserialize_json(item))
    return out
