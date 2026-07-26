"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DescribeEndpointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__list_of_endpoint
    import capo_mediaconvert.types.__string


class DescribeEndpointsResponse(TypedDict, closed=True):
    endpoints: NotRequired[
        "capo_mediaconvert.types.__list_of_endpoint.__listOfEndpoint"
    ]
    """List of endpoints"""
    next_token: NotRequired["capo_mediaconvert.types.__string.__string"]
    """Use this string to request the next batch of endpoints."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeEndpointsResponse) -> dict:
    out: dict = {}
    if "endpoints" in value:
        import capo_mediaconvert.types.__list_of_endpoint

        out["endpoints"] = capo_mediaconvert.types.__list_of_endpoint.serialize_json(
            value["endpoints"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeEndpointsResponse:
    out: DescribeEndpointsResponse = {}  # type: ignore[typeddict-item]
    if "endpoints" in data:
        import capo_mediaconvert.types.__list_of_endpoint

        out["endpoints"] = capo_mediaconvert.types.__list_of_endpoint.deserialize_json(
            data["endpoints"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
