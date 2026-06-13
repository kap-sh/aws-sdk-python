"""Generated from Smithy shape ``com.amazonaws.groundstation#ListAntennasResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.antenna_list
    import aws_sdk_groundstation.types.pagination_token


class ListAntennasResponse(TypedDict):
    antenna_list: "aws_sdk_groundstation.types.antenna_list.AntennaList"
    """<p>List of antennas.</p>"""
    next_token: NotRequired[
        "aws_sdk_groundstation.types.pagination_token.PaginationToken"
    ]
    """<p>Next token to be used in a subsequent <code>ListAntennas</code> call to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAntennasResponse) -> dict:
    out: dict = {}
    import aws_sdk_groundstation.types.antenna_list

    out["antennaList"] = aws_sdk_groundstation.types.antenna_list.serialize_json(
        value["antenna_list"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAntennasResponse:
    out: ListAntennasResponse = {}  # type: ignore[typeddict-item]
    if "antennaList" in data:
        import aws_sdk_groundstation.types.antenna_list

        out["antenna_list"] = aws_sdk_groundstation.types.antenna_list.deserialize_json(
            data["antennaList"]
        )
    else:
        raise DeserializationError("ListAntennasResponse.antenna_list required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
