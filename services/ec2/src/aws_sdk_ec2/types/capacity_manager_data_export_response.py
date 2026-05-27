"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityManagerDataExportResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_manager_data_export_id
    import aws_sdk_ec2.types.capacity_manager_data_export_status
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.output_format
    import aws_sdk_ec2.types.schedule
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class CapacityManagerDataExportResponse(TypedDict):
    capacity_manager_data_export_id: NotRequired[
        "aws_sdk_ec2.types.capacity_manager_data_export_id.CapacityManagerDataExportId"
    ]
    """<p> The unique identifier for the data export configuration. </p>"""
    s3_bucket_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The name of the S3 bucket where export files are delivered. </p>"""
    s3_bucket_prefix: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The S3 key prefix used for organizing export files within the bucket. </p>"""
    schedule: NotRequired["aws_sdk_ec2.types.schedule.Schedule"]
    """<p> The frequency at which data exports are generated. </p>"""
    output_format: NotRequired["aws_sdk_ec2.types.output_format.OutputFormat"]
    """<p> The file format of the exported data. </p>"""
    create_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p> The timestamp when the data export configuration was created. </p>"""
    latest_delivery_status: NotRequired[
        "aws_sdk_ec2.types.capacity_manager_data_export_status.CapacityManagerDataExportStatus"
    ]
    """<p> The status of the most recent export delivery. </p>"""
    latest_delivery_status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> A message describing the status of the most recent export delivery, including any error details if the delivery failed. </p>"""
    latest_delivery_s3_location_uri: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The S3 URI of the most recently delivered export file. </p>"""
    latest_delivery_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p> The timestamp when the most recent export was delivered to S3. </p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p> The tags associated with the data export configuration. </p>"""
