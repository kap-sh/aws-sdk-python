"""Generated from Smithy shape ``com.amazonaws.odb#RebootDbNodeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.resource_id


class RebootDbNodeInput(TypedDict, closed=True):
    cloud_vm_cluster_id: "aws_sdk_odb.types.resource_id.ResourceId"
    """<p>The unique identifier of the VM cluster that contains the DB node to reboot.</p>"""
    db_node_id: "aws_sdk_odb.types.resource_id.ResourceId"
    """<p>The unique identifier of the DB node to reboot.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RebootDbNodeInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> RebootDbNodeInput:
    out: RebootDbNodeInput = {}  # type: ignore[typeddict-item]
    return out
