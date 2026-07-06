"""Generated from Smithy shape ``com.amazonaws.connect#ListDataTableValuesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_value_summary_list
    import aws_sdk_connect.types.next_token


class ListDataTableValuesResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    values: (
        "aws_sdk_connect.types.data_table_value_summary_list.DataTableValueSummaryList"
    )
    """<p>A list of data table values with their associated metadata, lock versions, and modification details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataTableValuesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import aws_sdk_connect.types.data_table_value_summary_list

    out["Values"] = aws_sdk_connect.types.data_table_value_summary_list.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> ListDataTableValuesResponse:
    out: ListDataTableValuesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Values" in data:
        import aws_sdk_connect.types.data_table_value_summary_list

        out["values"] = (
            aws_sdk_connect.types.data_table_value_summary_list.deserialize_json(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("ListDataTableValuesResponse.values required")
    return out
