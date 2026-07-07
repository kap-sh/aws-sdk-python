"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListDataAccessorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.data_accessors
    import aws_sdk_qbusiness.types.next_token1500


class ListDataAccessorsResponse(TypedDict, closed=True):
    data_accessors: NotRequired["aws_sdk_qbusiness.types.data_accessors.DataAccessors"]
    """<p>The list of data accessors.</p>"""
    next_token: NotRequired["aws_sdk_qbusiness.types.next_token1500.NextToken1500"]
    """<p>The token to use to retrieve the next set of results, if there are any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataAccessorsResponse) -> dict:
    out: dict = {}
    if "data_accessors" in value:
        import aws_sdk_qbusiness.types.data_accessors

        out["dataAccessors"] = aws_sdk_qbusiness.types.data_accessors.serialize_json(
            value["data_accessors"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataAccessorsResponse:
    out: ListDataAccessorsResponse = {}  # type: ignore[typeddict-item]
    if "dataAccessors" in data:
        import aws_sdk_qbusiness.types.data_accessors

        out["data_accessors"] = aws_sdk_qbusiness.types.data_accessors.deserialize_json(
            data["dataAccessors"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
