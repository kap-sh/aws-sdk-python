"""Generated from Smithy shape ``com.amazonaws.kinesis#ListShardsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.next_token
    import aws_sdk_kinesis.types.shard_list


class ListShardsOutput(TypedDict):
    shards: NotRequired["aws_sdk_kinesis.types.shard_list.ShardList"]
    """<p>An array of JSON objects. Each object represents one shard and specifies the IDs of the shard, the shard's parent, and the shard that's adjacent to the shard's parent. Each object also contains the starting and ending hash keys and the starting and ending sequence numbers for the shard.</p>"""
    next_token: NotRequired["aws_sdk_kinesis.types.next_token.NextToken"]
    """<p>When the number of shards in the data stream is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of shards in the data stream, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListShards</code> to list the next set of shards. For more information about the use of this pagination token when calling the <code>ListShards</code> operation, see <a>ListShardsInput$NextToken</a>.</p> <important> <p>Tokens expire after 300 seconds. When you obtain a value for <code>NextToken</code> in the response to a call to <code>ListShards</code>, you have 300 seconds to use that value. If you specify an expired token in a call to <code>ListShards</code>, you get <code>ExpiredNextTokenException</code>.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListShardsOutput) -> dict:
    out: dict = {}
    if "shards" in value:
        import aws_sdk_kinesis.types.shard_list

        out["Shards"] = aws_sdk_kinesis.types.shard_list.serialize_aws_json_1_1(
            value["shards"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListShardsOutput:
    out: ListShardsOutput = {}  # type: ignore[typeddict-item]
    if "Shards" in data:
        import aws_sdk_kinesis.types.shard_list

        out["shards"] = aws_sdk_kinesis.types.shard_list.deserialize_aws_json_1_1(
            data["Shards"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
