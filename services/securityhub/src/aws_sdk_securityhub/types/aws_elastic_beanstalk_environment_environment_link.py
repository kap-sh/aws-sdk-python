"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElasticBeanstalkEnvironmentEnvironmentLink``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsElasticBeanstalkEnvironmentEnvironmentLink(TypedDict):
    environment_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the linked environment.</p>"""
    link_name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the environment link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsElasticBeanstalkEnvironmentEnvironmentLink) -> dict:
    out: dict = {}
    if "environment_name" in value:
        out["EnvironmentName"] = value["environment_name"]
    if "link_name" in value:
        out["LinkName"] = value["link_name"]
    return out


def deserialize_json(data: dict) -> AwsElasticBeanstalkEnvironmentEnvironmentLink:
    out: AwsElasticBeanstalkEnvironmentEnvironmentLink = {}  # type: ignore[typeddict-item]
    if "EnvironmentName" in data:
        out["environment_name"] = data["EnvironmentName"]
    if "LinkName" in data:
        out["link_name"] = data["LinkName"]
    return out
