"""Generated from Smithy shape ``com.amazonaws.sesv2#DeleteMultiRegionEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.endpoint_name


class DeleteMultiRegionEndpointRequest(TypedDict, closed=True):
    endpoint_name: "capo_sesv2.types.endpoint_name.EndpointName"
    """<p>The name of the multi-region endpoint (global-endpoint) to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMultiRegionEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMultiRegionEndpointRequest:
    out: DeleteMultiRegionEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
