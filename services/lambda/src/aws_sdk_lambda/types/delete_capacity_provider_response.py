"""Generated from Smithy shape ``com.amazonaws.lambda#DeleteCapacityProviderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.capacity_provider


class DeleteCapacityProviderResponse(TypedDict, closed=True):
    capacity_provider: "aws_sdk_lambda.types.capacity_provider.CapacityProvider"
    """<p>Information about the deleted capacity provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCapacityProviderResponse) -> dict:
    out: dict = {}
    import aws_sdk_lambda.types.capacity_provider

    out["CapacityProvider"] = aws_sdk_lambda.types.capacity_provider.serialize_json(
        value["capacity_provider"]
    )
    return out


def deserialize_json(data: dict) -> DeleteCapacityProviderResponse:
    out: DeleteCapacityProviderResponse = {}  # type: ignore[typeddict-item]
    if "CapacityProvider" in data:
        import aws_sdk_lambda.types.capacity_provider

        out["capacity_provider"] = (
            aws_sdk_lambda.types.capacity_provider.deserialize_json(
                data["CapacityProvider"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteCapacityProviderResponse.capacity_provider required"
        )
    return out
