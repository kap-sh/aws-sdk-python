"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetails(
    TypedDict, closed=True
):
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of resource to assign to a container. Valid values are <code>GPU</code> or <code>InferenceAccelerator</code>.</p>"""
    value: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The value for the specified resource type.</p> <p>For <code>GPU</code>, the value is the number of physical GPUs the Amazon ECS container agent reserves for the container.</p> <p>For <code>InferenceAccelerator</code>, the value should match the <code>DeviceName</code> attribute of an entry in <code>InferenceAccelerators</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetails,
) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetails:
    out: AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetails = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
