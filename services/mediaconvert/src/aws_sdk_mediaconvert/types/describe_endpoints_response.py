"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DescribeEndpointsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__list_of_endpoint
    import aws_sdk_mediaconvert.types.__string


class DescribeEndpointsResponse(TypedDict):
    endpoints: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_endpoint.__listOfEndpoint"
    ]
    """List of endpoints"""
    next_token: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """Use this string to request the next batch of endpoints."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeEndpointsResponse) -> dict:
    out: dict = {}
    if "endpoints" in value:
        import aws_sdk_mediaconvert.types.__list_of_endpoint

        out["endpoints"] = aws_sdk_mediaconvert.types.__list_of_endpoint.serialize_json(
            value["endpoints"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeEndpointsResponse:
    out: DescribeEndpointsResponse = {}  # type: ignore[typeddict-item]
    if "endpoints" in data:
        import aws_sdk_mediaconvert.types.__list_of_endpoint

        out["endpoints"] = (
            aws_sdk_mediaconvert.types.__list_of_endpoint.deserialize_json(
                data["endpoints"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
