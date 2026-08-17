"""Generated from Smithy shape ``com.amazonaws.lambda#CreateCapacityProviderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.capacity_provider


class CreateCapacityProviderResponse(TypedDict, closed=True):
    capacity_provider: "capo_lambda.types.capacity_provider.CapacityProvider"
    """<p>Information about the capacity provider that was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCapacityProviderResponse) -> dict:
    out: dict = {}
    import capo_lambda.types.capacity_provider

    out["CapacityProvider"] = capo_lambda.types.capacity_provider.serialize_json(
        value["capacity_provider"]
    )
    return out


def deserialize_json(data: dict) -> CreateCapacityProviderResponse:
    out: CreateCapacityProviderResponse = {}  # type: ignore[typeddict-item]
    if data.get("CapacityProvider") is not None:
        import capo_lambda.types.capacity_provider

        out["capacity_provider"] = capo_lambda.types.capacity_provider.deserialize_json(
            data["CapacityProvider"]
        )
    else:
        raise DeserializationError(
            "CreateCapacityProviderResponse.capacity_provider required"
        )
    return out
