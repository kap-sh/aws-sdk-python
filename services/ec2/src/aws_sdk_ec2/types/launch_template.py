"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplate``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.launch_template_name
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.operator_response
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class LaunchTemplate(TypedDict):
    launch_template_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the launch template.</p>"""
    launch_template_name: NotRequired[
        "aws_sdk_ec2.types.launch_template_name.LaunchTemplateName"
    ]
    """<p>The name of the launch template.</p>"""
    create_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time launch template was created.</p>"""
    created_by: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The principal that created the launch template. </p>"""
    default_version_number: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The version number of the default version of the launch template.</p>"""
    latest_version_number: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The version number of the latest version of the launch template.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags for the launch template.</p>"""
    operator: NotRequired["aws_sdk_ec2.types.operator_response.OperatorResponse"]
    """<p>The entity that manages the launch template.</p>"""
