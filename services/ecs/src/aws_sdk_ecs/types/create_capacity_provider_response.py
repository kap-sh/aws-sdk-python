"""Generated from Smithy shape ``com.amazonaws.ecs#CreateCapacityProviderResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.capacity_provider


class CreateCapacityProviderResponse(TypedDict):
    capacity_provider: NotRequired[
        "aws_sdk_ecs.types.capacity_provider.CapacityProvider"
    ]
    """<p>The full description of the new capacity provider.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCapacityProviderResponse) -> dict:
    out: dict = {}
    if "capacity_provider" in value:
        import aws_sdk_ecs.types.capacity_provider

        out["capacityProvider"] = (
            aws_sdk_ecs.types.capacity_provider.serialize_aws_json_1_1(
                value["capacity_provider"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCapacityProviderResponse:
    out: CreateCapacityProviderResponse = {}  # type: ignore[typeddict-item]
    if "capacityProvider" in data:
        import aws_sdk_ecs.types.capacity_provider

        out["capacity_provider"] = (
            aws_sdk_ecs.types.capacity_provider.deserialize_aws_json_1_1(
                data["capacityProvider"]
            )
        )
    return out
