"""Generated from Smithy shape ``com.amazonaws.odb#GetDbNodeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.resource_id


class GetDbNodeInput(TypedDict, closed=True):
    cloud_vm_cluster_id: "aws_sdk_odb.types.resource_id.ResourceId"
    """<p>The unique identifier of the VM cluster that contains the DB node.</p>"""
    db_node_id: "aws_sdk_odb.types.resource_id.ResourceId"
    """<p>The unique identifier of the DB node to retrieve information about.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetDbNodeInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> GetDbNodeInput:
    out: GetDbNodeInput = {}  # type: ignore[typeddict-item]
    return out
