"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaSettingsDescription``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.auto_scaling_settings_description
    import aws_sdk_dynamodb.types.billing_mode_summary
    import aws_sdk_dynamodb.types.non_negative_long_object
    import aws_sdk_dynamodb.types.region_name
    import aws_sdk_dynamodb.types.replica_global_secondary_index_settings_description_list
    import aws_sdk_dynamodb.types.replica_status
    import aws_sdk_dynamodb.types.table_class_summary


class ReplicaSettingsDescription(TypedDict):
    region_name: "aws_sdk_dynamodb.types.region_name.RegionName"
    """<p>The Region name of the replica.</p>"""
    replica_status: NotRequired["aws_sdk_dynamodb.types.replica_status.ReplicaStatus"]
    """<p>The current state of the Region:</p> <ul> <li> <p> <code>CREATING</code> - The Region is being created.</p> </li> <li> <p> <code>UPDATING</code> - The Region is being updated.</p> </li> <li> <p> <code>DELETING</code> - The Region is being deleted.</p> </li> <li> <p> <code>ACTIVE</code> - The Region is ready for use.</p> </li> </ul>"""
    replica_billing_mode_summary: NotRequired[
        "aws_sdk_dynamodb.types.billing_mode_summary.BillingModeSummary"
    ]
    """<p>The read/write capacity mode of the replica.</p>"""
    replica_provisioned_read_capacity_units: NotRequired[
        "aws_sdk_dynamodb.types.non_negative_long_object.NonNegativeLongObject"
    ]
    """<p>The maximum number of strongly consistent reads consumed per second before DynamoDB returns a <code>ThrottlingException</code>. For more information, see <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html#ProvisionedThroughput\">Specifying Read and Write Requirements</a> in the <i>Amazon DynamoDB Developer Guide</i>. </p>"""
    replica_provisioned_read_capacity_auto_scaling_settings: NotRequired[
        "aws_sdk_dynamodb.types.auto_scaling_settings_description.AutoScalingSettingsDescription"
    ]
    """<p>Auto scaling settings for a global table replica's read capacity units.</p>"""
    replica_provisioned_write_capacity_units: NotRequired[
        "aws_sdk_dynamodb.types.non_negative_long_object.NonNegativeLongObject"
    ]
    """<p>The maximum number of writes consumed per second before DynamoDB returns a <code>ThrottlingException</code>. For more information, see <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html#ProvisionedThroughput\">Specifying Read and Write Requirements</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    replica_provisioned_write_capacity_auto_scaling_settings: NotRequired[
        "aws_sdk_dynamodb.types.auto_scaling_settings_description.AutoScalingSettingsDescription"
    ]
    """<p>Auto scaling settings for a global table replica's write capacity units.</p>"""
    replica_global_secondary_index_settings: NotRequired[
        "aws_sdk_dynamodb.types.replica_global_secondary_index_settings_description_list.ReplicaGlobalSecondaryIndexSettingsDescriptionList"
    ]
    """<p>Replica global secondary index settings for the global table.</p>"""
    replica_table_class_summary: NotRequired[
        "aws_sdk_dynamodb.types.table_class_summary.TableClassSummary"
    ]
