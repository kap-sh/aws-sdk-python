"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaGlobalSecondaryIndex``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.index_name
    import aws_sdk_dynamodb.types.on_demand_throughput_override
    import aws_sdk_dynamodb.types.provisioned_throughput_override


class ReplicaGlobalSecondaryIndex(TypedDict):
    index_name: "aws_sdk_dynamodb.types.index_name.IndexName"
    """<p>The name of the global secondary index.</p>"""
    provisioned_throughput_override: NotRequired[
        "aws_sdk_dynamodb.types.provisioned_throughput_override.ProvisionedThroughputOverride"
    ]
    """<p>Replica table GSI-specific provisioned throughput. If not specified, uses the source table GSI's read capacity settings.</p>"""
    on_demand_throughput_override: NotRequired[
        "aws_sdk_dynamodb.types.on_demand_throughput_override.OnDemandThroughputOverride"
    ]
    """<p>Overrides the maximum on-demand throughput settings for the specified global secondary index in the specified replica table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaGlobalSecondaryIndex) -> dict:
    out: dict = {}
    out["IndexName"] = value["index_name"]
    if "provisioned_throughput_override" in value:
        import aws_sdk_dynamodb.types.provisioned_throughput_override

        out["ProvisionedThroughputOverride"] = (
            aws_sdk_dynamodb.types.provisioned_throughput_override.serialize_aws_json_1_0(
                value["provisioned_throughput_override"]
            )
        )
    if "on_demand_throughput_override" in value:
        import aws_sdk_dynamodb.types.on_demand_throughput_override

        out["OnDemandThroughputOverride"] = (
            aws_sdk_dynamodb.types.on_demand_throughput_override.serialize_aws_json_1_0(
                value["on_demand_throughput_override"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReplicaGlobalSecondaryIndex:
    out: ReplicaGlobalSecondaryIndex = {}  # type: ignore[typeddict-item]
    if "IndexName" in data:
        out["index_name"] = data["IndexName"]
    else:
        raise DeserializationError("ReplicaGlobalSecondaryIndex.index_name required")
    if "ProvisionedThroughputOverride" in data:
        import aws_sdk_dynamodb.types.provisioned_throughput_override

        out["provisioned_throughput_override"] = (
            aws_sdk_dynamodb.types.provisioned_throughput_override.deserialize_aws_json_1_0(
                data["ProvisionedThroughputOverride"]
            )
        )
    if "OnDemandThroughputOverride" in data:
        import aws_sdk_dynamodb.types.on_demand_throughput_override

        out["on_demand_throughput_override"] = (
            aws_sdk_dynamodb.types.on_demand_throughput_override.deserialize_aws_json_1_0(
                data["OnDemandThroughputOverride"]
            )
        )
    return out
