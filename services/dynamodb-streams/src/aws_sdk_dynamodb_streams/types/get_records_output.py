"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#GetRecordsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb_streams.types.record_list
    import aws_sdk_dynamodb_streams.types.shard_iterator


class GetRecordsOutput(TypedDict):
    records: NotRequired["aws_sdk_dynamodb_streams.types.record_list.RecordList"]
    """<p>The stream records from the shard, which were retrieved using the shard iterator.</p>"""
    next_shard_iterator: NotRequired[
        "aws_sdk_dynamodb_streams.types.shard_iterator.ShardIterator"
    ]
    """<p>The next position in the shard from which to start sequentially reading stream records. If set to <code>null</code>, the shard has been closed and the requested iterator will not return any more data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRecordsOutput) -> dict:
    out: dict = {}
    if "records" in value:
        import aws_sdk_dynamodb_streams.types.record_list

        out["Records"] = (
            aws_sdk_dynamodb_streams.types.record_list.serialize_aws_json_1_0(
                value["records"]
            )
        )
    if "next_shard_iterator" in value:
        out["NextShardIterator"] = value["next_shard_iterator"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRecordsOutput:
    out: GetRecordsOutput = {}  # type: ignore[typeddict-item]
    if "Records" in data:
        import aws_sdk_dynamodb_streams.types.record_list

        out["records"] = (
            aws_sdk_dynamodb_streams.types.record_list.deserialize_aws_json_1_0(
                data["Records"]
            )
        )
    if "NextShardIterator" in data:
        out["next_shard_iterator"] = data["NextShardIterator"]
    return out
