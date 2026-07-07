"""Generated from Smithy shape ``com.amazonaws.groundstation#ListSatellitesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.pagination_token
    import aws_sdk_groundstation.types.satellite_list


class ListSatellitesResponse(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_groundstation.types.pagination_token.PaginationToken"
    ]
    """<p>Next token that can be supplied in the next call to get the next page of satellites.</p>"""
    satellites: NotRequired["aws_sdk_groundstation.types.satellite_list.SatelliteList"]
    """<p>List of satellites.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSatellitesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "satellites" in value:
        import aws_sdk_groundstation.types.satellite_list

        out["satellites"] = aws_sdk_groundstation.types.satellite_list.serialize_json(
            value["satellites"]
        )
    return out


def deserialize_json(data: dict) -> ListSatellitesResponse:
    out: ListSatellitesResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "satellites" in data:
        import aws_sdk_groundstation.types.satellite_list

        out["satellites"] = aws_sdk_groundstation.types.satellite_list.deserialize_json(
            data["satellites"]
        )
    return out
