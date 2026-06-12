"""Generated from Smithy shape ``com.amazonaws.kinesis#DescribeLimitsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.on_demand_stream_count_limit_object
    import aws_sdk_kinesis.types.on_demand_stream_count_object
    import aws_sdk_kinesis.types.shard_count_object


class DescribeLimitsOutput(TypedDict):
    shard_limit: "aws_sdk_kinesis.types.shard_count_object.ShardCountObject"
    """<p>The maximum number of shards.</p>"""
    open_shard_count: "aws_sdk_kinesis.types.shard_count_object.ShardCountObject"
    """<p>The number of open shards.</p>"""
    on_demand_stream_count: (
        "aws_sdk_kinesis.types.on_demand_stream_count_object.OnDemandStreamCountObject"
    )
    """<p> Indicates the number of data streams with the on-demand capacity mode.</p>"""
    on_demand_stream_count_limit: "aws_sdk_kinesis.types.on_demand_stream_count_limit_object.OnDemandStreamCountLimitObject"
    """<p> The maximum number of data streams with the on-demand capacity mode. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLimitsOutput) -> dict:
    out: dict = {}
    out["ShardLimit"] = value["shard_limit"]
    out["OpenShardCount"] = value["open_shard_count"]
    out["OnDemandStreamCount"] = value["on_demand_stream_count"]
    out["OnDemandStreamCountLimit"] = value["on_demand_stream_count_limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLimitsOutput:
    out: DescribeLimitsOutput = {}  # type: ignore[typeddict-item]
    if "ShardLimit" in data:
        out["shard_limit"] = data["ShardLimit"]
    else:
        raise DeserializationError("DescribeLimitsOutput.shard_limit required")
    if "OpenShardCount" in data:
        out["open_shard_count"] = data["OpenShardCount"]
    else:
        raise DeserializationError("DescribeLimitsOutput.open_shard_count required")
    if "OnDemandStreamCount" in data:
        out["on_demand_stream_count"] = data["OnDemandStreamCount"]
    else:
        raise DeserializationError(
            "DescribeLimitsOutput.on_demand_stream_count required"
        )
    if "OnDemandStreamCountLimit" in data:
        out["on_demand_stream_count_limit"] = data["OnDemandStreamCountLimit"]
    else:
        raise DeserializationError(
            "DescribeLimitsOutput.on_demand_stream_count_limit required"
        )
    return out
