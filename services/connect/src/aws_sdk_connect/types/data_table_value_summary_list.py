"""Generated from Smithy shape ``com.amazonaws.connect#DataTableValueSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_value_summary

DataTableValueSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.data_table_value_summary.DataTableValueSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataTableValueSummaryList) -> list:
    import aws_sdk_connect.types.data_table_value_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.data_table_value_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataTableValueSummaryList:
    import aws_sdk_connect.types.data_table_value_summary

    out: DataTableValueSummaryList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.data_table_value_summary.deserialize_json(item)
        )
    return out
