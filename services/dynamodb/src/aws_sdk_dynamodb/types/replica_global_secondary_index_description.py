"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaGlobalSecondaryIndexDescription``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.global_secondary_index_warm_throughput_description
    import aws_sdk_dynamodb.types.index_name
    import aws_sdk_dynamodb.types.on_demand_throughput_override
    import aws_sdk_dynamodb.types.provisioned_throughput_override


class ReplicaGlobalSecondaryIndexDescription(TypedDict):
    index_name: NotRequired["aws_sdk_dynamodb.types.index_name.IndexName"]
    """<p>The name of the global secondary index.</p>"""
    provisioned_throughput_override: NotRequired[
        "aws_sdk_dynamodb.types.provisioned_throughput_override.ProvisionedThroughputOverride"
    ]
    """<p>If not described, uses the source table GSI's read capacity settings.</p>"""
    on_demand_throughput_override: NotRequired[
        "aws_sdk_dynamodb.types.on_demand_throughput_override.OnDemandThroughputOverride"
    ]
    """<p>Overrides the maximum on-demand throughput for the specified global secondary index in the specified replica table.</p>"""
    warm_throughput: NotRequired[
        "aws_sdk_dynamodb.types.global_secondary_index_warm_throughput_description.GlobalSecondaryIndexWarmThroughputDescription"
    ]
    """<p>Represents the warm throughput of the global secondary index for this replica.</p>"""
