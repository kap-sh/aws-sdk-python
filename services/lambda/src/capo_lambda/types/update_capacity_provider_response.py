"""Generated from Smithy shape ``com.amazonaws.lambda#UpdateCapacityProviderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.capacity_provider


class UpdateCapacityProviderResponse(TypedDict, closed=True):
    capacity_provider: "capo_lambda.types.capacity_provider.CapacityProvider"
    """<p>Information about the updated capacity provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCapacityProviderResponse) -> dict:
    out: dict = {}
    import capo_lambda.types.capacity_provider

    out["CapacityProvider"] = capo_lambda.types.capacity_provider.serialize_json(
        value["capacity_provider"]
    )
    return out


def deserialize_json(data: dict) -> UpdateCapacityProviderResponse:
    out: UpdateCapacityProviderResponse = {}  # type: ignore[typeddict-item]
    if data.get("CapacityProvider") is not None:
        import capo_lambda.types.capacity_provider

        out["capacity_provider"] = capo_lambda.types.capacity_provider.deserialize_json(
            data["CapacityProvider"]
        )
    else:
        raise DeserializationError(
            "UpdateCapacityProviderResponse.capacity_provider required"
        )
    return out
