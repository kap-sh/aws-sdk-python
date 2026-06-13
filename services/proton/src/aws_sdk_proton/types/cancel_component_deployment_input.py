"""Generated from Smithy shape ``com.amazonaws.proton#CancelComponentDeploymentInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.resource_name


class CancelComponentDeploymentInput(TypedDict):
    component_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the component with the deployment to cancel.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelComponentDeploymentInput) -> dict:
    out: dict = {}
    out["componentName"] = value["component_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelComponentDeploymentInput:
    out: CancelComponentDeploymentInput = {}  # type: ignore[typeddict-item]
    if "componentName" in data:
        out["component_name"] = data["componentName"]
    else:
        raise DeserializationError(
            "CancelComponentDeploymentInput.component_name required"
        )
    return out
