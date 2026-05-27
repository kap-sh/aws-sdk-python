"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeGlobalTableSettingsOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.replica_settings_description_list
    import aws_sdk_dynamodb.types.table_name


class DescribeGlobalTableSettingsOutput(TypedDict):
    global_table_name: NotRequired["aws_sdk_dynamodb.types.table_name.TableName"]
    """<p>The name of the global table.</p>"""
    replica_settings: NotRequired[
        "aws_sdk_dynamodb.types.replica_settings_description_list.ReplicaSettingsDescriptionList"
    ]
    """<p>The Region-specific settings for the global table.</p>"""
