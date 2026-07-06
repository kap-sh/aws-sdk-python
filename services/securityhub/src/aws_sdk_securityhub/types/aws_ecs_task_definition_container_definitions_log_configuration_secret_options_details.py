"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetails(
    TypedDict, closed=True
):
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the secret.</p>"""
    value_from: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The secret to expose to the container.</p> <p>The value is either the full ARN of the Secrets Manager secret or the full ARN of the parameter in the Systems Manager Parameter Store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetails,
) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value_from" in value:
        out["ValueFrom"] = value["value_from"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetails:
    out: AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetails = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ValueFrom" in data:
        out["value_from"] = data["ValueFrom"]
    return out
