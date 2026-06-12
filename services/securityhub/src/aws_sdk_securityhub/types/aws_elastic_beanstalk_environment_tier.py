"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElasticBeanstalkEnvironmentTier``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsElasticBeanstalkEnvironmentTier(TypedDict):
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the environment tier. Valid values are <code>WebServer</code> or <code>Worker</code>.</p>"""
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of environment tier. Valid values are <code>Standard</code> or <code>SQS/HTTP</code>.</p>"""
    version: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The version of the environment tier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsElasticBeanstalkEnvironmentTier) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        out["Type"] = value["type"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> AwsElasticBeanstalkEnvironmentTier:
    out: AwsElasticBeanstalkEnvironmentTier = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Version" in data:
        out["version"] = data["Version"]
    return out
