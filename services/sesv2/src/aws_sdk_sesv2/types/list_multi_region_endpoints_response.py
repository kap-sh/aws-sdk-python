"""Generated from Smithy shape ``com.amazonaws.sesv2#ListMultiRegionEndpointsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.multi_region_endpoints
    import aws_sdk_sesv2.types.next_token_v2


class ListMultiRegionEndpointsResponse(TypedDict):
    multi_region_endpoints: NotRequired[
        "aws_sdk_sesv2.types.multi_region_endpoints.MultiRegionEndpoints"
    ]
    """<p>An array that contains key multi-region endpoint (global-endpoint) properties.</p>"""
    next_token: NotRequired["aws_sdk_sesv2.types.next_token_v2.NextTokenV2"]
    """<p>A token indicating that there are additional multi-region endpoints (global-endpoints) available to be listed. Pass this token to a subsequent <code>ListMultiRegionEndpoints</code> call to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMultiRegionEndpointsResponse) -> dict:
    out: dict = {}
    if "multi_region_endpoints" in value:
        import aws_sdk_sesv2.types.multi_region_endpoints

        out["MultiRegionEndpoints"] = (
            aws_sdk_sesv2.types.multi_region_endpoints.serialize_json(
                value["multi_region_endpoints"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMultiRegionEndpointsResponse:
    out: ListMultiRegionEndpointsResponse = {}  # type: ignore[typeddict-item]
    if "MultiRegionEndpoints" in data:
        import aws_sdk_sesv2.types.multi_region_endpoints

        out["multi_region_endpoints"] = (
            aws_sdk_sesv2.types.multi_region_endpoints.deserialize_json(
                data["MultiRegionEndpoints"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
