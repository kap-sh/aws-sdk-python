"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalTableGlobalSecondaryIndexSettingsUpdate``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.auto_scaling_settings_update
    import aws_sdk_dynamodb.types.index_name
    import aws_sdk_dynamodb.types.positive_long_object


class GlobalTableGlobalSecondaryIndexSettingsUpdate(TypedDict):
    index_name: "aws_sdk_dynamodb.types.index_name.IndexName"
    """<p>The name of the global secondary index. The name must be unique among all other indexes on this table.</p>"""
    provisioned_write_capacity_units: NotRequired[
        "aws_sdk_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>The maximum number of writes consumed per second before DynamoDB returns a <code>ThrottlingException.</code> </p>"""
    provisioned_write_capacity_auto_scaling_settings_update: NotRequired[
        "aws_sdk_dynamodb.types.auto_scaling_settings_update.AutoScalingSettingsUpdate"
    ]
    """<p>Auto scaling settings for managing a global secondary index's write capacity units.</p>"""
