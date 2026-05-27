"""Generated from Smithy shape ``com.amazonaws.dynamodb#SourceTableFeatureDetails``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.global_secondary_indexes
    import aws_sdk_dynamodb.types.local_secondary_indexes
    import aws_sdk_dynamodb.types.sse_description
    import aws_sdk_dynamodb.types.stream_specification
    import aws_sdk_dynamodb.types.time_to_live_description


class SourceTableFeatureDetails(TypedDict):
    local_secondary_indexes: NotRequired[
        "aws_sdk_dynamodb.types.local_secondary_indexes.LocalSecondaryIndexes"
    ]
    """<p>Represents the LSI properties for the table when the backup was created. It includes the IndexName, KeySchema and Projection for the LSIs on the table at the time of backup. </p>"""
    global_secondary_indexes: NotRequired[
        "aws_sdk_dynamodb.types.global_secondary_indexes.GlobalSecondaryIndexes"
    ]
    """<p>Represents the GSI properties for the table when the backup was created. It includes the IndexName, KeySchema, Projection, and ProvisionedThroughput for the GSIs on the table at the time of backup. </p>"""
    stream_description: NotRequired[
        "aws_sdk_dynamodb.types.stream_specification.StreamSpecification"
    ]
    """<p>Stream settings on the table when the backup was created.</p>"""
    time_to_live_description: NotRequired[
        "aws_sdk_dynamodb.types.time_to_live_description.TimeToLiveDescription"
    ]
    """<p>Time to Live settings on the table when the backup was created.</p>"""
    sse_description: NotRequired[
        "aws_sdk_dynamodb.types.sse_description.SSEDescription"
    ]
    """<p>The description of the server-side encryption status on the table when the backup was created.</p>"""
