"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCapacityManagerDataExportRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.output_format
    import aws_sdk_ec2.types.schedule
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class CreateCapacityManagerDataExportRequest(TypedDict):
    s3_bucket_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The name of the S3 bucket where the capacity data export files will be delivered. The bucket must exist and you must have write permissions to it. </p>"""
    s3_bucket_prefix: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The S3 key prefix for the exported data files. This allows you to organize exports in a specific folder structure within your bucket. If not specified, files are placed at the bucket root. </p>"""
    schedule: NotRequired["aws_sdk_ec2.types.schedule.Schedule"]
    """<p> The frequency at which data exports are generated. </p>"""
    output_format: NotRequired["aws_sdk_ec2.types.output_format.OutputFormat"]
    """<p> The file format for the exported data. Parquet format is recommended for large datasets and better compression. </p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see Ensure Idempotency. </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p> Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>. </p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p> The tags to apply to the data export configuration. You can tag the export for organization and cost tracking purposes. </p>"""
