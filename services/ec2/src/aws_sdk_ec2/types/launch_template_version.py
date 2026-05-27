"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateVersion``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.launch_template_name
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.operator_response
    import aws_sdk_ec2.types.response_launch_template_data
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.version_description


class LaunchTemplateVersion(TypedDict):
    launch_template_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the launch template.</p>"""
    launch_template_name: NotRequired[
        "aws_sdk_ec2.types.launch_template_name.LaunchTemplateName"
    ]
    """<p>The name of the launch template.</p>"""
    version_number: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The version number.</p>"""
    version_description: NotRequired[
        "aws_sdk_ec2.types.version_description.VersionDescription"
    ]
    """<p>The description for the version.</p>"""
    create_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time the version was created.</p>"""
    created_by: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The principal that created the version.</p>"""
    default_version: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the version is the default version.</p>"""
    launch_template_data: NotRequired[
        "aws_sdk_ec2.types.response_launch_template_data.ResponseLaunchTemplateData"
    ]
    """<p>Information about the launch template.</p>"""
    operator: NotRequired["aws_sdk_ec2.types.operator_response.OperatorResponse"]
    """<p>The entity that manages the launch template.</p>"""
