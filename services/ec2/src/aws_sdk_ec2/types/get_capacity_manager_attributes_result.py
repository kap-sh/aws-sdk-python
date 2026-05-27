"""Generated from Smithy shape ``com.amazonaws.ec2#GetCapacityManagerAttributesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.capacity_manager_status
    import aws_sdk_ec2.types.ingestion_status
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class GetCapacityManagerAttributesResult(TypedDict):
    capacity_manager_status: NotRequired[
        "aws_sdk_ec2.types.capacity_manager_status.CapacityManagerStatus"
    ]
    """<p> The current status of Capacity Manager. </p>"""
    organizations_access: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p> Indicates whether Organizations access is enabled for cross-account data aggregation. </p>"""
    data_export_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p> The number of active data export configurations for this account. This count includes all data exports regardless of their current delivery status. </p>"""
    ingestion_status: NotRequired["aws_sdk_ec2.types.ingestion_status.IngestionStatus"]
    """<p> The current data ingestion status. Initial ingestion may take several hours after enabling Capacity Manager. </p>"""
    ingestion_status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> A descriptive message providing additional details about the current ingestion status. This may include error information if ingestion has failed or progress details during initial setup. </p>"""
    earliest_datapoint_timestamp: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p> The timestamp of the earliest data point available in Capacity Manager, in milliseconds since epoch. This indicates how far back historical data is available for queries. </p>"""
    latest_datapoint_timestamp: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p> The timestamp of the most recent data point ingested by Capacity Manager, in milliseconds since epoch. This indicates how current your capacity data is. </p>"""
