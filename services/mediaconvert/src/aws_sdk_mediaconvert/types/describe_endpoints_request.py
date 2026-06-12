"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DescribeEndpointsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer
    import aws_sdk_mediaconvert.types.__string
    import aws_sdk_mediaconvert.types.describe_endpoints_mode


class DescribeEndpointsRequest(TypedDict):
    max_results: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """Optional. Max number of endpoints, up to twenty, that will be returned at one time."""
    mode: NotRequired[
        "aws_sdk_mediaconvert.types.describe_endpoints_mode.DescribeEndpointsMode"
    ]
    """Optional field, defaults to DEFAULT. Specify DEFAULT for this operation to return your endpoints if any exist, or to create an endpoint for you and return it if one doesn't already exist. Specify GET_ONLY to return your endpoints if any exist, or an empty list if none exist."""
    next_token: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """Use this string, provided with the response to a previous request, to request the next batch of endpoints."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeEndpointsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "mode" in value:
        import aws_sdk_mediaconvert.types.describe_endpoints_mode

        out["mode"] = aws_sdk_mediaconvert.types.describe_endpoints_mode.serialize_json(
            value["mode"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeEndpointsRequest:
    out: DescribeEndpointsRequest = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "mode" in data:
        import aws_sdk_mediaconvert.types.describe_endpoints_mode

        out["mode"] = (
            aws_sdk_mediaconvert.types.describe_endpoints_mode.deserialize_json(
                data["mode"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
