"""Generated from Smithy shape ``com.amazonaws.lambda#GetCapacityProviderRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.capacity_provider_name


class GetCapacityProviderRequest(TypedDict):
    capacity_provider_name: (
        "aws_sdk_lambda.types.capacity_provider_name.CapacityProviderName"
    )
    """<p>The name of the capacity provider to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCapacityProviderRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCapacityProviderRequest:
    out: GetCapacityProviderRequest = {}  # type: ignore[typeddict-item]
    return out
