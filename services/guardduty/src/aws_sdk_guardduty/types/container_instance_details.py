"""Generated from Smithy shape ``com.amazonaws.guardduty#ContainerInstanceDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.long


class ContainerInstanceDetails(TypedDict):
    covered_container_instances: NotRequired["aws_sdk_guardduty.types.long.Long"]
    """<p>Represents the nodes in the Amazon ECS cluster that has a <code>HEALTHY</code> coverage status.</p>"""
    compatible_container_instances: NotRequired["aws_sdk_guardduty.types.long.Long"]
    """<p>Represents total number of nodes in the Amazon ECS cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerInstanceDetails) -> dict:
    out: dict = {}
    if "covered_container_instances" in value:
        out["coveredContainerInstances"] = value["covered_container_instances"]
    if "compatible_container_instances" in value:
        out["compatibleContainerInstances"] = value["compatible_container_instances"]
    return out


def deserialize_json(data: dict) -> ContainerInstanceDetails:
    out: ContainerInstanceDetails = {}  # type: ignore[typeddict-item]
    if "coveredContainerInstances" in data:
        out["covered_container_instances"] = data["coveredContainerInstances"]
    if "compatibleContainerInstances" in data:
        out["compatible_container_instances"] = data["compatibleContainerInstances"]
    return out
