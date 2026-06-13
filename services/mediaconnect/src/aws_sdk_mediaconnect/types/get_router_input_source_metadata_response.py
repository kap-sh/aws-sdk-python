"""Generated from Smithy shape ``com.amazonaws.mediaconnect#GetRouterInputSourceMetadataResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_input_arn
    import aws_sdk_mediaconnect.types.router_input_source_metadata_details


class GetRouterInputSourceMetadataResponse(TypedDict):
    arn: "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn"
    """<p>The Amazon Resource Name (ARN) of the router input.</p>"""
    name: "str"
    """<p>The name of the router input.</p>"""
    source_metadata_details: "aws_sdk_mediaconnect.types.router_input_source_metadata_details.RouterInputSourceMetadataDetails"
    """<p>Detailed metadata information about the router input source, including connection state, timestamps, and stream configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRouterInputSourceMetadataResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    import aws_sdk_mediaconnect.types.router_input_source_metadata_details

    out["sourceMetadataDetails"] = (
        aws_sdk_mediaconnect.types.router_input_source_metadata_details.serialize_json(
            value["source_metadata_details"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetRouterInputSourceMetadataResponse:
    out: GetRouterInputSourceMetadataResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetRouterInputSourceMetadataResponse.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetRouterInputSourceMetadataResponse.name required")
    if "sourceMetadataDetails" in data:
        import aws_sdk_mediaconnect.types.router_input_source_metadata_details

        out["source_metadata_details"] = (
            aws_sdk_mediaconnect.types.router_input_source_metadata_details.deserialize_json(
                data["sourceMetadataDetails"]
            )
        )
    else:
        raise DeserializationError(
            "GetRouterInputSourceMetadataResponse.source_metadata_details required"
        )
    return out
