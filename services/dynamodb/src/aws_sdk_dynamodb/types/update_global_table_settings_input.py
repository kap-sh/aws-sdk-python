"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateGlobalTableSettingsInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.auto_scaling_settings_update
    import aws_sdk_dynamodb.types.billing_mode
    import aws_sdk_dynamodb.types.global_table_global_secondary_index_settings_update_list
    import aws_sdk_dynamodb.types.positive_long_object
    import aws_sdk_dynamodb.types.replica_settings_update_list
    import aws_sdk_dynamodb.types.table_name


class UpdateGlobalTableSettingsInput(TypedDict):
    global_table_name: "aws_sdk_dynamodb.types.table_name.TableName"
    """<p>The name of the global table</p>"""
    global_table_billing_mode: NotRequired[
        "aws_sdk_dynamodb.types.billing_mode.BillingMode"
    ]
    """<p>The billing mode of the global table. If <code>GlobalTableBillingMode</code> is not specified, the global table defaults to <code>PROVISIONED</code> capacity billing mode.</p> <ul> <li> <p> <code>PROVISIONED</code> - We recommend using <code>PROVISIONED</code> for predictable workloads. <code>PROVISIONED</code> sets the billing mode to <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/provisioned-capacity-mode.html\">Provisioned capacity mode</a>.</p> </li> <li> <p> <code>PAY_PER_REQUEST</code> - We recommend using <code>PAY_PER_REQUEST</code> for unpredictable workloads. <code>PAY_PER_REQUEST</code> sets the billing mode to <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/on-demand-capacity-mode.html\">On-demand capacity mode</a>. </p> </li> </ul>"""
    global_table_provisioned_write_capacity_units: NotRequired[
        "aws_sdk_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>The maximum number of writes consumed per second before DynamoDB returns a <code>ThrottlingException.</code> </p>"""
    global_table_provisioned_write_capacity_auto_scaling_settings_update: NotRequired[
        "aws_sdk_dynamodb.types.auto_scaling_settings_update.AutoScalingSettingsUpdate"
    ]
    """<p>Auto scaling settings for managing provisioned write capacity for the global table.</p>"""
    global_table_global_secondary_index_settings_update: NotRequired[
        "aws_sdk_dynamodb.types.global_table_global_secondary_index_settings_update_list.GlobalTableGlobalSecondaryIndexSettingsUpdateList"
    ]
    """<p>Represents the settings of a global secondary index for a global table that will be modified.</p>"""
    replica_settings_update: NotRequired[
        "aws_sdk_dynamodb.types.replica_settings_update_list.ReplicaSettingsUpdateList"
    ]
    """<p>Represents the settings for a global table in a Region that will be modified.</p>"""
