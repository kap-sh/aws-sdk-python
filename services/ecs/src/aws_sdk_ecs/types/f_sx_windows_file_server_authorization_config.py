"""Generated from Smithy shape ``com.amazonaws.ecs#FSxWindowsFileServerAuthorizationConfig``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class FSxWindowsFileServerAuthorizationConfig(TypedDict):
    credentials_parameter: "aws_sdk_ecs.types.string.String"
    """<p>The authorization credential option to use. The authorization credential options can be provided using either the Amazon Resource Name (ARN) of an Secrets Manager secret or SSM Parameter Store parameter. The ARN refers to the stored credentials.</p>"""
    domain: "aws_sdk_ecs.types.string.String"
    """<p>A fully qualified domain name hosted by an <a href=\"https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html\">Directory Service</a> Managed Microsoft AD (Active Directory) or self-hosted AD on Amazon EC2.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FSxWindowsFileServerAuthorizationConfig) -> dict:
    out: dict = {}
    out["credentialsParameter"] = value["credentials_parameter"]
    out["domain"] = value["domain"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FSxWindowsFileServerAuthorizationConfig:
    out: FSxWindowsFileServerAuthorizationConfig = {}  # type: ignore[typeddict-item]
    if "credentialsParameter" in data:
        out["credentials_parameter"] = data["credentialsParameter"]
    else:
        raise DeserializationError(
            "FSxWindowsFileServerAuthorizationConfig.credentials_parameter required"
        )
    if "domain" in data:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError(
            "FSxWindowsFileServerAuthorizationConfig.domain required"
        )
    return out
