"""Generated from Smithy shape ``com.amazonaws.sesv2#DeleteMultiRegionEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.endpoint_name


class DeleteMultiRegionEndpointRequest(TypedDict):
    endpoint_name: "aws_sdk_sesv2.types.endpoint_name.EndpointName"
    """<p>The name of the multi-region endpoint (global-endpoint) to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMultiRegionEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMultiRegionEndpointRequest:
    out: DeleteMultiRegionEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
