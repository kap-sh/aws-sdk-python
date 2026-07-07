"""Generated from Smithy shape ``com.amazonaws.groundstation#ListEphemeridesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.ephemerides_list
    import aws_sdk_groundstation.types.pagination_token


class ListEphemeridesResponse(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_groundstation.types.pagination_token.PaginationToken"
    ]
    """<p>Pagination token.</p>"""
    ephemerides: NotRequired[
        "aws_sdk_groundstation.types.ephemerides_list.EphemeridesList"
    ]
    """<p>List of ephemerides.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEphemeridesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "ephemerides" in value:
        import aws_sdk_groundstation.types.ephemerides_list

        out["ephemerides"] = (
            aws_sdk_groundstation.types.ephemerides_list.serialize_json(
                value["ephemerides"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListEphemeridesResponse:
    out: ListEphemeridesResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "ephemerides" in data:
        import aws_sdk_groundstation.types.ephemerides_list

        out["ephemerides"] = (
            aws_sdk_groundstation.types.ephemerides_list.deserialize_json(
                data["ephemerides"]
            )
        )
    return out
