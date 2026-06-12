"""Generated from Smithy shape ``com.amazonaws.memorydb#ShardDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.shard_configuration
    import aws_sdk_memorydb.types.string
    import aws_sdk_memorydb.types.t_stamp


class ShardDetail(TypedDict):
    name: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The name of the shard</p>"""
    configuration: NotRequired[
        "aws_sdk_memorydb.types.shard_configuration.ShardConfiguration"
    ]
    """<p>The configuration details of the shard</p>"""
    size: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The size of the shard's snapshot</p>"""
    snapshot_creation_time: NotRequired["aws_sdk_memorydb.types.t_stamp.TStamp"]
    """<p>The date and time that the shard's snapshot was created</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShardDetail) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "configuration" in value:
        import aws_sdk_memorydb.types.shard_configuration

        out["Configuration"] = (
            aws_sdk_memorydb.types.shard_configuration.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    if "size" in value:
        out["Size"] = value["size"]
    if "snapshot_creation_time" in value:
        import aws_sdk_memorydb.types.t_stamp

        out["SnapshotCreationTime"] = (
            aws_sdk_memorydb.types.t_stamp.serialize_aws_json_1_1(
                value["snapshot_creation_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ShardDetail:
    out: ShardDetail = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Configuration" in data:
        import aws_sdk_memorydb.types.shard_configuration

        out["configuration"] = (
            aws_sdk_memorydb.types.shard_configuration.deserialize_aws_json_1_1(
                data["Configuration"]
            )
        )
    if "Size" in data:
        out["size"] = data["Size"]
    if "SnapshotCreationTime" in data:
        import aws_sdk_memorydb.types.t_stamp

        out["snapshot_creation_time"] = (
            aws_sdk_memorydb.types.t_stamp.deserialize_aws_json_1_1(
                data["SnapshotCreationTime"]
            )
        )
    return out
