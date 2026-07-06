"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetails(
    TypedDict, closed=True
):
    namespace: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The namespaced kernel parameter for which to set a value.</p>"""
    value: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The value of the parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetails,
) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetails:
    out: AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetails = {}  # type: ignore[typeddict-item]
    if "Namespace" in data:
        out["namespace"] = data["Namespace"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
