"""Generated from Smithy shape ``com.amazonaws.marketplacedeployment#DeploymentParameterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_marketplace_deployment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_deployment.types.deployment_parameter_name
    import aws_sdk_marketplace_deployment.types.secret_string


class DeploymentParameterInput(TypedDict, closed=True):
    name: "aws_sdk_marketplace_deployment.types.deployment_parameter_name.DeploymentParameterName"
    """<p>The desired name of the deployment parameter. This is the identifier on which deployment parameters are keyed for a given buyer and product. If this name matches an existing deployment parameter, this request will update the existing resource.</p>"""
    secret_string: "aws_sdk_marketplace_deployment.types.secret_string.SecretString"
    """<p>The text to encrypt and store in the secret.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentParameterInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["secretString"] = value["secret_string"]
    return out


def deserialize_json(data: dict) -> DeploymentParameterInput:
    out: DeploymentParameterInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeploymentParameterInput.name required")
    if "secretString" in data:
        out["secret_string"] = data["secretString"]
    else:
        raise DeserializationError("DeploymentParameterInput.secret_string required")
    return out
