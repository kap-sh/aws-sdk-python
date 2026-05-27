"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateTimeToLiveInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.table_arn
    import aws_sdk_dynamodb.types.time_to_live_specification


class UpdateTimeToLiveInput(TypedDict):
    table_name: "aws_sdk_dynamodb.types.table_arn.TableArn"
    """<p>The name of the table to be configured. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    time_to_live_specification: (
        "aws_sdk_dynamodb.types.time_to_live_specification.TimeToLiveSpecification"
    )
    """<p>Represents the settings used to enable or disable Time to Live for the specified table.</p>"""
