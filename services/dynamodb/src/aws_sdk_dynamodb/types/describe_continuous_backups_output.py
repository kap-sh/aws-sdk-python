"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeContinuousBackupsOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.continuous_backups_description


class DescribeContinuousBackupsOutput(TypedDict):
    continuous_backups_description: NotRequired[
        "aws_sdk_dynamodb.types.continuous_backups_description.ContinuousBackupsDescription"
    ]
    """<p>Represents the continuous backups and point in time recovery settings on the table.</p>"""
