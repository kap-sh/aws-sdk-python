"""Generated from Smithy shape ``com.amazonaws.guardduty#ListPublishingDestinationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.destinations
    import aws_sdk_guardduty.types.string


class ListPublishingDestinationsResponse(TypedDict):
    destinations: NotRequired["aws_sdk_guardduty.types.destinations.Destinations"]
    """<p>A <code>Destinations</code> object that includes information about each publishing destination returned.</p>"""
    next_token: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the <code>NextToken</code> value returned from the previous request to continue listing results after the first page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPublishingDestinationsResponse) -> dict:
    out: dict = {}
    if "destinations" in value:
        import aws_sdk_guardduty.types.destinations

        out["destinations"] = aws_sdk_guardduty.types.destinations.serialize_json(
            value["destinations"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPublishingDestinationsResponse:
    out: ListPublishingDestinationsResponse = {}  # type: ignore[typeddict-item]
    if "destinations" in data:
        import aws_sdk_guardduty.types.destinations

        out["destinations"] = aws_sdk_guardduty.types.destinations.deserialize_json(
            data["destinations"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
