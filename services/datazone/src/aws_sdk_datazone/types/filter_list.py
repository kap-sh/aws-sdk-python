"""Generated from Smithy shape ``com.amazonaws.datazone#FilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.filter_clause

FilterList: TypeAlias = list["aws_sdk_datazone.types.filter_clause.FilterClause"]


# --- restJson1 ser/de ---
def serialize_json(value: FilterList) -> list:
    import aws_sdk_datazone.types.filter_clause

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.filter_clause.serialize_json(item))
    return out


def deserialize_json(data: list) -> FilterList:
    import aws_sdk_datazone.types.filter_clause

    out: FilterList = []
    for item in data:
        out.append(aws_sdk_datazone.types.filter_clause.deserialize_json(item))
    return out
