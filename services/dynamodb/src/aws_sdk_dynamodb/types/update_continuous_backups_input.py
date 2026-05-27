"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateContinuousBackupsInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.point_in_time_recovery_specification
    import aws_sdk_dynamodb.types.table_arn


class UpdateContinuousBackupsInput(TypedDict):
    table_name: "aws_sdk_dynamodb.types.table_arn.TableArn"
    """<p>The name of the table. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    point_in_time_recovery_specification: "aws_sdk_dynamodb.types.point_in_time_recovery_specification.PointInTimeRecoverySpecification"
    """<p>Represents the settings used to enable point in time recovery.</p>"""
