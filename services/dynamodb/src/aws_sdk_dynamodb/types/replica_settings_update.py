"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaSettingsUpdate``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.auto_scaling_settings_update
    import aws_sdk_dynamodb.types.positive_long_object
    import aws_sdk_dynamodb.types.region_name
    import aws_sdk_dynamodb.types.replica_global_secondary_index_settings_update_list
    import aws_sdk_dynamodb.types.table_class


class ReplicaSettingsUpdate(TypedDict):
    region_name: "aws_sdk_dynamodb.types.region_name.RegionName"
    """<p>The Region of the replica to be added.</p>"""
    replica_provisioned_read_capacity_units: NotRequired[
        "aws_sdk_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>The maximum number of strongly consistent reads consumed per second before DynamoDB returns a <code>ThrottlingException</code>. For more information, see <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html#ProvisionedThroughput\">Specifying Read and Write Requirements</a> in the <i>Amazon DynamoDB Developer Guide</i>. </p>"""
    replica_provisioned_read_capacity_auto_scaling_settings_update: NotRequired[
        "aws_sdk_dynamodb.types.auto_scaling_settings_update.AutoScalingSettingsUpdate"
    ]
    """<p>Auto scaling settings for managing a global table replica's read capacity units.</p>"""
    replica_global_secondary_index_settings_update: NotRequired[
        "aws_sdk_dynamodb.types.replica_global_secondary_index_settings_update_list.ReplicaGlobalSecondaryIndexSettingsUpdateList"
    ]
    """<p>Represents the settings of a global secondary index for a global table that will be modified.</p>"""
    replica_table_class: NotRequired["aws_sdk_dynamodb.types.table_class.TableClass"]
    """<p>Replica-specific table class. If not specified, uses the source table's table class.</p>"""
