"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListDataSetsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.list_of_data_set_entry
    import aws_sdk_dataexchange.types.next_token


class ListDataSetsResponse(TypedDict):
    data_sets: NotRequired[
        "aws_sdk_dataexchange.types.list_of_data_set_entry.ListOfDataSetEntry"
    ]
    """<p>The data set objects listed by the request.</p>"""
    next_token: NotRequired["aws_sdk_dataexchange.types.next_token.NextToken"]
    """<p>The token value retrieved from a previous call to access the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataSetsResponse) -> dict:
    out: dict = {}
    if "data_sets" in value:
        import aws_sdk_dataexchange.types.list_of_data_set_entry

        out["DataSets"] = (
            aws_sdk_dataexchange.types.list_of_data_set_entry.serialize_json(
                value["data_sets"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataSetsResponse:
    out: ListDataSetsResponse = {}  # type: ignore[typeddict-item]
    if "DataSets" in data:
        import aws_sdk_dataexchange.types.list_of_data_set_entry

        out["data_sets"] = (
            aws_sdk_dataexchange.types.list_of_data_set_entry.deserialize_json(
                data["DataSets"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
