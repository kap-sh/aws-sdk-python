"""Generated from Smithy shape ``com.amazonaws.m2#ListDataSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.data_sets_summary_list
    import aws_sdk_m2.types.next_token


class ListDataSetsResponse(TypedDict, closed=True):
    data_sets: "aws_sdk_m2.types.data_sets_summary_list.DataSetsSummaryList"
    """<p>The list of data sets, containing information including the creation time, the data set name, the data set organization, the data set format, and the last time the data set was referenced or updated.</p>"""
    next_token: NotRequired["aws_sdk_m2.types.next_token.NextToken"]
    """<p>If there are more items to return, this contains a token that is passed to a subsequent call to this operation to retrieve the next set of items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataSetsResponse) -> dict:
    out: dict = {}
    import aws_sdk_m2.types.data_sets_summary_list

    out["dataSets"] = aws_sdk_m2.types.data_sets_summary_list.serialize_json(
        value["data_sets"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataSetsResponse:
    out: ListDataSetsResponse = {}  # type: ignore[typeddict-item]
    if "dataSets" in data:
        import aws_sdk_m2.types.data_sets_summary_list

        out["data_sets"] = aws_sdk_m2.types.data_sets_summary_list.deserialize_json(
            data["dataSets"]
        )
    else:
        raise DeserializationError("ListDataSetsResponse.data_sets required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
