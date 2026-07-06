"""Generated from Smithy shape ``com.amazonaws.mediaconnect#GetRouterInputThumbnailResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_input_arn
    import aws_sdk_mediaconnect.types.router_input_thumbnail_details


class GetRouterInputThumbnailResponse(TypedDict, closed=True):
    arn: "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn"
    """<p>The ARN of the router input.</p>"""
    name: "str"
    """<p>The name of the router input.</p>"""
    thumbnail_details: "aws_sdk_mediaconnect.types.router_input_thumbnail_details.RouterInputThumbnailDetails"
    """<p>The details of the thumbnail associated with the router input, including the thumbnail image, timecode, timestamp, and any associated error messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRouterInputThumbnailResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    import aws_sdk_mediaconnect.types.router_input_thumbnail_details

    out["thumbnailDetails"] = (
        aws_sdk_mediaconnect.types.router_input_thumbnail_details.serialize_json(
            value["thumbnail_details"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetRouterInputThumbnailResponse:
    out: GetRouterInputThumbnailResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetRouterInputThumbnailResponse.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetRouterInputThumbnailResponse.name required")
    if "thumbnailDetails" in data:
        import aws_sdk_mediaconnect.types.router_input_thumbnail_details

        out["thumbnail_details"] = (
            aws_sdk_mediaconnect.types.router_input_thumbnail_details.deserialize_json(
                data["thumbnailDetails"]
            )
        )
    else:
        raise DeserializationError(
            "GetRouterInputThumbnailResponse.thumbnail_details required"
        )
    return out
