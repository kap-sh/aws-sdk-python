"""Generated from Smithy shape ``com.amazonaws.ec2#ExportImageTask``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.export_task_s3_location
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class ExportImageTask(TypedDict):
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description of the image being exported.</p>"""
    export_image_task_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the export image task.</p>"""
    image_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the image.</p>"""
    progress: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The percent complete of the export image task.</p>"""
    s3_export_location: NotRequired[
        "aws_sdk_ec2.types.export_task_s3_location.ExportTaskS3Location"
    ]
    """<p>Information about the destination Amazon S3 bucket.</p>"""
    status: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status of the export image task. The possible values are <code>active</code>, <code>completed</code>, <code>deleting</code>, and <code>deleted</code>.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status message for the export image task.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the export image task.</p>"""
