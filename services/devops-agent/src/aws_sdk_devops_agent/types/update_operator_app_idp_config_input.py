"""Generated from Smithy shape ``com.amazonaws.devopsagent#UpdateOperatorAppIdpConfigInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space_id
    import aws_sdk_devops_agent.types.idp_client_secret


class UpdateOperatorAppIdpConfigInput(TypedDict):
    agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the AgentSpace</p>"""
    idp_client_secret: NotRequired[
        "aws_sdk_devops_agent.types.idp_client_secret.IdpClientSecret"
    ]
    """<p>The OIDC client secret for the IdP application</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOperatorAppIdpConfigInput) -> dict:
    out: dict = {}
    if "idp_client_secret" in value:
        out["idpClientSecret"] = value["idp_client_secret"]
    return out


def deserialize_json(data: dict) -> UpdateOperatorAppIdpConfigInput:
    out: UpdateOperatorAppIdpConfigInput = {}  # type: ignore[typeddict-item]
    if "idpClientSecret" in data:
        out["idp_client_secret"] = data["idpClientSecret"]
    return out
