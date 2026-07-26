"""Generated from Smithy shape ``com.amazonaws.kinesis#ListShardsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.list_shards_input_limit
    import capo_kinesis.types.next_token
    import capo_kinesis.types.shard_filter
    import capo_kinesis.types.shard_id
    import capo_kinesis.types.stream_arn
    import capo_kinesis.types.stream_id
    import capo_kinesis.types.stream_name
    import capo_kinesis.types.timestamp


class ListShardsInput(TypedDict, closed=True):
    stream_name: NotRequired["capo_kinesis.types.stream_name.StreamName"]
    """<p>The name of the data stream whose shards you want to list. </p> <p>You cannot specify this parameter if you specify the <code>NextToken</code> parameter.</p>"""
    next_token: NotRequired["capo_kinesis.types.next_token.NextToken"]
    """<p>When the number of shards in the data stream is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of shards in the data stream, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListShards</code> to list the next set of shards.</p> <p>Don't specify <code>StreamName</code> or <code>StreamCreationTimestamp</code> if you specify <code>NextToken</code> because the latter unambiguously identifies the stream.</p> <p>You can optionally specify a value for the <code>MaxResults</code> parameter when you specify <code>NextToken</code>. If you specify a <code>MaxResults</code> value that is less than the number of shards that the operation returns if you don't specify <code>MaxResults</code>, the response will contain a new <code>NextToken</code> value. You can use the new <code>NextToken</code> value in a subsequent call to the <code>ListShards</code> operation.</p> <important> <p>Tokens expire after 300 seconds. When you obtain a value for <code>NextToken</code> in the response to a call to <code>ListShards</code>, you have 300 seconds to use that value. If you specify an expired token in a call to <code>ListShards</code>, you get <code>ExpiredNextTokenException</code>.</p> </important>"""
    exclusive_start_shard_id: NotRequired["capo_kinesis.types.shard_id.ShardId"]
    """<p>Specify this parameter to indicate that you want to list the shards starting with the shard whose ID immediately follows <code>ExclusiveStartShardId</code>.</p> <p>If you don't specify this parameter, the default behavior is for <code>ListShards</code> to list the shards starting with the first one in the stream.</p> <p>You cannot specify this parameter if you specify <code>NextToken</code>.</p>"""
    max_results: NotRequired[
        "capo_kinesis.types.list_shards_input_limit.ListShardsInputLimit"
    ]
    """<p>The maximum number of shards to return in a single call to <code>ListShards</code>. The maximum number of shards to return in a single call. The default value is 1000. If you specify a value greater than 1000, at most 1000 results are returned. </p> <p>When the number of shards to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListShards</code> to list the next set of shards.</p>"""
    stream_creation_timestamp: NotRequired["capo_kinesis.types.timestamp.Timestamp"]
    """<p>Specify this input parameter to distinguish data streams that have the same name. For example, if you create a data stream and then delete it, and you later create another data stream with the same name, you can use this input parameter to specify which of the two streams you want to list the shards for.</p> <p>You cannot specify this parameter if you specify the <code>NextToken</code> parameter.</p>"""
    shard_filter: NotRequired["capo_kinesis.types.shard_filter.ShardFilter"]
    """<p>Enables you to filter out the response of the <code>ListShards</code> API. You can only specify one filter at a time. </p> <p>If you use the <code>ShardFilter</code> parameter when invoking the ListShards API, the <code>Type</code> is the required property and must be specified. If you specify the <code>AT_TRIM_HORIZON</code>, <code>FROM_TRIM_HORIZON</code>, or <code>AT_LATEST</code> types, you do not need to specify either the <code>ShardId</code> or the <code>Timestamp</code> optional properties. </p> <p>If you specify the <code>AFTER_SHARD_ID</code> type, you must also provide the value for the optional <code>ShardId</code> property. The <code>ShardId</code> property is identical in fuctionality to the <code>ExclusiveStartShardId</code> parameter of the <code>ListShards</code> API. When <code>ShardId</code> property is specified, the response includes the shards starting with the shard whose ID immediately follows the <code>ShardId</code> that you provided. </p> <p>If you specify the <code>AT_TIMESTAMP</code> or <code>FROM_TIMESTAMP_ID</code> type, you must also provide the value for the optional <code>Timestamp</code> property. If you specify the AT_TIMESTAMP type, then all shards that were open at the provided timestamp are returned. If you specify the FROM_TIMESTAMP type, then all shards starting from the provided timestamp to TIP are returned. </p>"""
    stream_arn: NotRequired["capo_kinesis.types.stream_arn.StreamARN"]
    """<p>The ARN of the stream.</p>"""
    stream_id: NotRequired["capo_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListShardsInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "exclusive_start_shard_id" in value:
        out["ExclusiveStartShardId"] = value["exclusive_start_shard_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "stream_creation_timestamp" in value:
        import capo_kinesis.types.timestamp

        out["StreamCreationTimestamp"] = (
            capo_kinesis.types.timestamp.serialize_aws_json_1_1(
                value["stream_creation_timestamp"]
            )
        )
    if "shard_filter" in value:
        import capo_kinesis.types.shard_filter

        out["ShardFilter"] = capo_kinesis.types.shard_filter.serialize_aws_json_1_1(
            value["shard_filter"]
        )
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListShardsInput:
    out: ListShardsInput = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ExclusiveStartShardId" in data:
        out["exclusive_start_shard_id"] = data["ExclusiveStartShardId"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "StreamCreationTimestamp" in data:
        import capo_kinesis.types.timestamp

        out["stream_creation_timestamp"] = (
            capo_kinesis.types.timestamp.deserialize_aws_json_1_1(
                data["StreamCreationTimestamp"]
            )
        )
    if "ShardFilter" in data:
        import capo_kinesis.types.shard_filter

        out["shard_filter"] = capo_kinesis.types.shard_filter.deserialize_aws_json_1_1(
            data["ShardFilter"]
        )
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "StreamId" in data:
        out["stream_id"] = data["StreamId"]
    return out
