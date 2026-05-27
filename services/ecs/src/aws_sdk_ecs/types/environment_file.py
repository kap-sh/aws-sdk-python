"""Generated from Smithy shape ``com.amazonaws.ecs#EnvironmentFile``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.environment_file_type
    import aws_sdk_ecs.types.string


class EnvironmentFile(TypedDict):
    value: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the Amazon S3 object containing the environment variable file.</p>"""
    type: "aws_sdk_ecs.types.environment_file_type.EnvironmentFileType"
    """<p>The file type to use. Environment files are objects in Amazon S3. The only supported value is <code>s3</code>.</p>"""
