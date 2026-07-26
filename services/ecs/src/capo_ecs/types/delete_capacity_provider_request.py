"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteCapacityProviderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.string


class DeleteCapacityProviderRequest(TypedDict, closed=True):
    capacity_provider: "capo_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the capacity provider to delete.</p>"""
    cluster: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of the cluster that contains the capacity provider to delete. Managed instances capacity providers are cluster-scoped and can only be deleted from their associated cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCapacityProviderRequest) -> dict:
    out: dict = {}
    out["capacityProvider"] = value["capacity_provider"]
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCapacityProviderRequest:
    out: DeleteCapacityProviderRequest = {}  # type: ignore[typeddict-item]
    if "capacityProvider" in data:
        out["capacity_provider"] = data["capacityProvider"]
    else:
        raise DeserializationError(
            "DeleteCapacityProviderRequest.capacity_provider required"
        )
    if "cluster" in data:
        out["cluster"] = data["cluster"]
    return out
