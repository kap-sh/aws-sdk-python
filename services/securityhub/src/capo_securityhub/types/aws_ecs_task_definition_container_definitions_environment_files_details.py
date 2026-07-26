"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetails(
    TypedDict, closed=True
):
    type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of environment file. The valid value is <code>s3</code>.</p>"""
    value: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the S3 object that contains the environment variable file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetails,
) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetails:
    out: AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetails = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
