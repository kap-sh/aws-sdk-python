"""Generated from Smithy shape ``com.amazonaws.lambda#DeleteCapacityProviderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.capacity_provider_name


class DeleteCapacityProviderRequest(TypedDict, closed=True):
    capacity_provider_name: (
        "aws_sdk_lambda.types.capacity_provider_name.CapacityProviderName"
    )
    """<p>The name of the capacity provider to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCapacityProviderRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCapacityProviderRequest:
    out: DeleteCapacityProviderRequest = {}  # type: ignore[typeddict-item]
    return out
