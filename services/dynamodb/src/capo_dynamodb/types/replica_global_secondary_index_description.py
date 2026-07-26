"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaGlobalSecondaryIndexDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.global_secondary_index_warm_throughput_description
    import capo_dynamodb.types.index_name
    import capo_dynamodb.types.on_demand_throughput_override
    import capo_dynamodb.types.provisioned_throughput_override


class ReplicaGlobalSecondaryIndexDescription(TypedDict, closed=True):
    index_name: NotRequired["capo_dynamodb.types.index_name.IndexName"]
    """<p>The name of the global secondary index.</p>"""
    provisioned_throughput_override: NotRequired[
        "capo_dynamodb.types.provisioned_throughput_override.ProvisionedThroughputOverride"
    ]
    """<p>If not described, uses the source table GSI's read capacity settings.</p>"""
    on_demand_throughput_override: NotRequired[
        "capo_dynamodb.types.on_demand_throughput_override.OnDemandThroughputOverride"
    ]
    """<p>Overrides the maximum on-demand throughput for the specified global secondary index in the specified replica table.</p>"""
    warm_throughput: NotRequired[
        "capo_dynamodb.types.global_secondary_index_warm_throughput_description.GlobalSecondaryIndexWarmThroughputDescription"
    ]
    """<p>Represents the warm throughput of the global secondary index for this replica.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaGlobalSecondaryIndexDescription) -> dict:
    out: dict = {}
    if "index_name" in value:
        out["IndexName"] = value["index_name"]
    if "provisioned_throughput_override" in value:
        import capo_dynamodb.types.provisioned_throughput_override

        out["ProvisionedThroughputOverride"] = (
            capo_dynamodb.types.provisioned_throughput_override.serialize_aws_json_1_0(
                value["provisioned_throughput_override"]
            )
        )
    if "on_demand_throughput_override" in value:
        import capo_dynamodb.types.on_demand_throughput_override

        out["OnDemandThroughputOverride"] = (
            capo_dynamodb.types.on_demand_throughput_override.serialize_aws_json_1_0(
                value["on_demand_throughput_override"]
            )
        )
    if "warm_throughput" in value:
        import capo_dynamodb.types.global_secondary_index_warm_throughput_description

        out["WarmThroughput"] = (
            capo_dynamodb.types.global_secondary_index_warm_throughput_description.serialize_aws_json_1_0(
                value["warm_throughput"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReplicaGlobalSecondaryIndexDescription:
    out: ReplicaGlobalSecondaryIndexDescription = {}  # type: ignore[typeddict-item]
    if "IndexName" in data:
        out["index_name"] = data["IndexName"]
    if "ProvisionedThroughputOverride" in data:
        import capo_dynamodb.types.provisioned_throughput_override

        out["provisioned_throughput_override"] = (
            capo_dynamodb.types.provisioned_throughput_override.deserialize_aws_json_1_0(
                data["ProvisionedThroughputOverride"]
            )
        )
    if "OnDemandThroughputOverride" in data:
        import capo_dynamodb.types.on_demand_throughput_override

        out["on_demand_throughput_override"] = (
            capo_dynamodb.types.on_demand_throughput_override.deserialize_aws_json_1_0(
                data["OnDemandThroughputOverride"]
            )
        )
    if "WarmThroughput" in data:
        import capo_dynamodb.types.global_secondary_index_warm_throughput_description

        out["warm_throughput"] = (
            capo_dynamodb.types.global_secondary_index_warm_throughput_description.deserialize_aws_json_1_0(
                data["WarmThroughput"]
            )
        )
    return out
