"""Generated from Smithy shape ``com.amazonaws.lambda#GetCapacityProviderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.capacity_provider_name


class GetCapacityProviderRequest(TypedDict, closed=True):
    capacity_provider_name: (
        "capo_lambda.types.capacity_provider_name.CapacityProviderName"
    )
    """<p>The name of the capacity provider to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCapacityProviderRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCapacityProviderRequest:
    out: GetCapacityProviderRequest = {}  # type: ignore[typeddict-item]
    return out
