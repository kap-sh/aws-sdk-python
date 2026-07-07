"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetails(TypedDict, closed=True):
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the environment variable.</p>"""
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of environment variable.</p>"""
    value: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The value of the environment variable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetails,
) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        out["Type"] = value["type"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(
    data: dict,
) -> AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetails:
    out: AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetails = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
