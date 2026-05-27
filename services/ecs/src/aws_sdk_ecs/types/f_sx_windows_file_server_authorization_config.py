"""Generated from Smithy shape ``com.amazonaws.ecs#FSxWindowsFileServerAuthorizationConfig``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class FSxWindowsFileServerAuthorizationConfig(TypedDict):
    credentials_parameter: "aws_sdk_ecs.types.string.String"
    """<p>The authorization credential option to use. The authorization credential options can be provided using either the Amazon Resource Name (ARN) of an Secrets Manager secret or SSM Parameter Store parameter. The ARN refers to the stored credentials.</p>"""
    domain: "aws_sdk_ecs.types.string.String"
    """<p>A fully qualified domain name hosted by an <a href=\"https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html\">Directory Service</a> Managed Microsoft AD (Active Directory) or self-hosted AD on Amazon EC2.</p>"""
