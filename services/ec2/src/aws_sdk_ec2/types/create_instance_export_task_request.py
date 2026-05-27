"""Generated from Smithy shape ``com.amazonaws.ec2#CreateInstanceExportTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.export_environment
    import aws_sdk_ec2.types.export_to_s3_task_specification
    import aws_sdk_ec2.types.instance_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class CreateInstanceExportTaskRequest(TypedDict):
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the export instance task during creation.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the conversion task or the resource being exported. The maximum length is 255 characters.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance.</p>"""
    target_environment: NotRequired[
        "aws_sdk_ec2.types.export_environment.ExportEnvironment"
    ]
    """<p>The target virtualization environment.</p>"""
    export_to_s3_task: NotRequired[
        "aws_sdk_ec2.types.export_to_s3_task_specification.ExportToS3TaskSpecification"
    ]
    """<p>The format and location for an export instance task.</p>"""
