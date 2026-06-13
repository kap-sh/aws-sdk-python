"""Generated from Smithy shape ``com.amazonaws.odb#ListAutonomousVirtualMachinesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_odb.types.resource_id


class ListAutonomousVirtualMachinesInput(TypedDict):
    max_results: NotRequired["int"]
    """<p>The maximum number of items to return per page.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token to continue listing from.</p>"""
    cloud_autonomous_vm_cluster_id: "aws_sdk_odb.types.resource_id.ResourceId"
    """<p>The unique identifier of the Autonomous VM cluster whose virtual machines you're listing.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutonomousVirtualMachinesInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutonomousVirtualMachinesInput:
    out: ListAutonomousVirtualMachinesInput = {}  # type: ignore[typeddict-item]
    return out
