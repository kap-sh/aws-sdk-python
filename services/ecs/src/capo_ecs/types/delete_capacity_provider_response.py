"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteCapacityProviderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.capacity_provider


class DeleteCapacityProviderResponse(TypedDict, closed=True):
    capacity_provider: NotRequired["capo_ecs.types.capacity_provider.CapacityProvider"]
    """<p>The details of the capacity provider.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCapacityProviderResponse) -> dict:
    out: dict = {}
    if "capacity_provider" in value:
        import capo_ecs.types.capacity_provider

        out["capacityProvider"] = (
            capo_ecs.types.capacity_provider.serialize_aws_json_1_1(
                value["capacity_provider"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCapacityProviderResponse:
    out: DeleteCapacityProviderResponse = {}  # type: ignore[typeddict-item]
    if data.get("capacityProvider") is not None:
        import capo_ecs.types.capacity_provider

        out["capacity_provider"] = (
            capo_ecs.types.capacity_provider.deserialize_aws_json_1_1(
                data["capacityProvider"]
            )
        )
    return out
