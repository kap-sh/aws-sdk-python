"""Generated from Smithy shape ``com.amazonaws.memorydb#Shard``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.integer_optional
    import aws_sdk_memorydb.types.node_list
    import aws_sdk_memorydb.types.string


class Shard(TypedDict):
    name: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The name of the shard</p>"""
    status: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The current state of this replication group - creating, available, modifying, deleting.</p>"""
    slots: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The keyspace for this shard.</p>"""
    nodes: NotRequired["aws_sdk_memorydb.types.node_list.NodeList"]
    """<p>A list containing information about individual nodes within the shard</p>"""
    number_of_nodes: NotRequired[
        "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of nodes in the shard</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Shard) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        out["Status"] = value["status"]
    if "slots" in value:
        out["Slots"] = value["slots"]
    if "nodes" in value:
        import aws_sdk_memorydb.types.node_list

        out["Nodes"] = aws_sdk_memorydb.types.node_list.serialize_aws_json_1_1(
            value["nodes"]
        )
    if "number_of_nodes" in value:
        out["NumberOfNodes"] = value["number_of_nodes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Shard:
    out: Shard = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "Slots" in data:
        out["slots"] = data["Slots"]
    if "Nodes" in data:
        import aws_sdk_memorydb.types.node_list

        out["nodes"] = aws_sdk_memorydb.types.node_list.deserialize_aws_json_1_1(
            data["Nodes"]
        )
    if "NumberOfNodes" in data:
        out["number_of_nodes"] = data["NumberOfNodes"]
    return out
