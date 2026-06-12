"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#GetRecordsOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_keyspacesstreams.types.iterator_description
    import aws_sdk_keyspacesstreams.types.record_list
    import aws_sdk_keyspacesstreams.types.shard_iterator

class GetRecordsOutput(TypedDict):
    change_records: NotRequired["aws_sdk_keyspacesstreams.types.record_list.RecordList"]
    """<p> An array of change data records retrieved from the specified shard. Each record represents a single data modification (insert, update, or delete) to a row in the Amazon Keyspaces table. Records include the primary key columns and information about what data was modified. </p>"""
    next_shard_iterator: NotRequired["aws_sdk_keyspacesstreams.types.shard_iterator.ShardIterator"]
    """<p> The next position in the shard from which to start sequentially reading data records. If null, the shard has been closed and the requested iterator will not return any more data. </p>"""
    iterator_description: NotRequired["aws_sdk_keyspacesstreams.types.iterator_description.IteratorDescription"]
    """<p> Provides information about the current iterator at the time GetRecords request was processed by Keyspaces. </p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRecordsOutput) -> dict:
    out: dict = {}
    if "change_records" in value:
        import aws_sdk_keyspacesstreams.types.record_list
        out["changeRecords"] = aws_sdk_keyspacesstreams.types.record_list.serialize_aws_json_1_0(value["change_records"])
    if "next_shard_iterator" in value:
        out["nextShardIterator"] = value["next_shard_iterator"]
    if "iterator_description" in value:
        import aws_sdk_keyspacesstreams.types.iterator_description
        out["iteratorDescription"] = aws_sdk_keyspacesstreams.types.iterator_description.serialize_aws_json_1_0(value["iterator_description"])
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRecordsOutput:
    out: GetRecordsOutput = {}  # type: ignore[typeddict-item]
    if "changeRecords" in data:
        import aws_sdk_keyspacesstreams.types.record_list
        out["change_records"] = aws_sdk_keyspacesstreams.types.record_list.deserialize_aws_json_1_0(data["changeRecords"])
    if "nextShardIterator" in data:
        out["next_shard_iterator"] = data["nextShardIterator"]
    if "iteratorDescription" in data:
        import aws_sdk_keyspacesstreams.types.iterator_description
        out["iterator_description"] = aws_sdk_keyspacesstreams.types.iterator_description.deserialize_aws_json_1_0(data["iteratorDescription"])
    return out