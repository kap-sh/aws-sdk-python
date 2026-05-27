"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateGlobalSecondaryIndexAction``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.index_name
    import aws_sdk_dynamodb.types.on_demand_throughput
    import aws_sdk_dynamodb.types.provisioned_throughput
    import aws_sdk_dynamodb.types.warm_throughput


class UpdateGlobalSecondaryIndexAction(TypedDict):
    index_name: "aws_sdk_dynamodb.types.index_name.IndexName"
    """<p>The name of the global secondary index to be updated.</p>"""
    provisioned_throughput: NotRequired[
        "aws_sdk_dynamodb.types.provisioned_throughput.ProvisionedThroughput"
    ]
    """<p>Represents the provisioned throughput settings for the specified global secondary index.</p> <p>For current minimum and maximum provisioned throughput values, see <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html\">Service, Account, and Table Quotas</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    on_demand_throughput: NotRequired[
        "aws_sdk_dynamodb.types.on_demand_throughput.OnDemandThroughput"
    ]
    """<p>Updates the maximum number of read and write units for the specified global secondary index. If you use this parameter, you must specify <code>MaxReadRequestUnits</code>, <code>MaxWriteRequestUnits</code>, or both.</p>"""
    warm_throughput: NotRequired[
        "aws_sdk_dynamodb.types.warm_throughput.WarmThroughput"
    ]
    """<p>Represents the warm throughput value of the new provisioned throughput settings to be applied to a global secondary index.</p>"""
