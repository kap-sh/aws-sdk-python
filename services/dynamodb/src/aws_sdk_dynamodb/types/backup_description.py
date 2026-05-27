"""Generated from Smithy shape ``com.amazonaws.dynamodb#BackupDescription``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.backup_details
    import aws_sdk_dynamodb.types.source_table_details
    import aws_sdk_dynamodb.types.source_table_feature_details


class BackupDescription(TypedDict):
    backup_details: NotRequired["aws_sdk_dynamodb.types.backup_details.BackupDetails"]
    """<p>Contains the details of the backup created for the table. </p>"""
    source_table_details: NotRequired[
        "aws_sdk_dynamodb.types.source_table_details.SourceTableDetails"
    ]
    """<p>Contains the details of the table when the backup was created. </p>"""
    source_table_feature_details: NotRequired[
        "aws_sdk_dynamodb.types.source_table_feature_details.SourceTableFeatureDetails"
    ]
    """<p>Contains the details of the features enabled on the table when the backup was created. For example, LSIs, GSIs, streams, TTL.</p>"""
