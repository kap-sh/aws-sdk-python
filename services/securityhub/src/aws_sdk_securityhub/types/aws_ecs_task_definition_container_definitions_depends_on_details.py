"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails(TypedDict, closed=True):
    condition: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The dependency condition of the dependent container. Indicates the required status of the dependent container before the current container can start. Valid values are as follows:</p> <ul> <li> <p> <code>COMPLETE</code> </p> </li> <li> <p> <code>HEALTHY</code> </p> </li> <li> <p> <code>SUCCESS</code> </p> </li> <li> <p> <code>START</code> </p> </li> </ul>"""
    container_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the dependent container.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails,
) -> dict:
    out: dict = {}
    if "condition" in value:
        out["Condition"] = value["condition"]
    if "container_name" in value:
        out["ContainerName"] = value["container_name"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails:
    out: AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails = {}  # type: ignore[typeddict-item]
    if "Condition" in data:
        out["condition"] = data["Condition"]
    if "ContainerName" in data:
        out["container_name"] = data["ContainerName"]
    return out
