"""Generated from Smithy shape ``com.amazonaws.devopsagent#EnableOperatorAppInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space_id
    import aws_sdk_devops_agent.types.auth_flow
    import aws_sdk_devops_agent.types.idp_client_id
    import aws_sdk_devops_agent.types.idp_client_secret
    import aws_sdk_devops_agent.types.role_arn


class EnableOperatorAppInput(TypedDict, closed=True):
    agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the AgentSpace</p>"""
    auth_flow: "aws_sdk_devops_agent.types.auth_flow.AuthFlow"
    """<p>The authentication flow configured for the operator App. e.g. iam or idc</p>"""
    operator_app_role_arn: "aws_sdk_devops_agent.types.role_arn.RoleArn"
    """<p>The IAM role end users assume to access AIDevOps APIs</p>"""
    idc_instance_arn: NotRequired["str"]
    """<p>The IdC instance Arn used to create an IdC auth application</p>"""
    issuer_url: NotRequired["str"]
    """<p>The OIDC issuer URL of the external Identity Provider</p>"""
    idp_client_id: NotRequired["aws_sdk_devops_agent.types.idp_client_id.IdpClientId"]
    """<p>The OIDC client ID for the IdP application</p>"""
    idp_client_secret: NotRequired[
        "aws_sdk_devops_agent.types.idp_client_secret.IdpClientSecret"
    ]
    """<p>The OIDC client secret for the IdP application</p>"""
    provider: NotRequired["str"]
    """<p>The Identity Provider name (e.g., Entra, Okta, Google)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableOperatorAppInput) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.auth_flow

    out["authFlow"] = aws_sdk_devops_agent.types.auth_flow.serialize_json(
        value["auth_flow"]
    )
    out["operatorAppRoleArn"] = value["operator_app_role_arn"]
    if "idc_instance_arn" in value:
        out["idcInstanceArn"] = value["idc_instance_arn"]
    if "issuer_url" in value:
        out["issuerUrl"] = value["issuer_url"]
    if "idp_client_id" in value:
        out["idpClientId"] = value["idp_client_id"]
    if "idp_client_secret" in value:
        out["idpClientSecret"] = value["idp_client_secret"]
    if "provider" in value:
        out["provider"] = value["provider"]
    return out


def deserialize_json(data: dict) -> EnableOperatorAppInput:
    out: EnableOperatorAppInput = {}  # type: ignore[typeddict-item]
    if "authFlow" in data:
        import aws_sdk_devops_agent.types.auth_flow

        out["auth_flow"] = aws_sdk_devops_agent.types.auth_flow.deserialize_json(
            data["authFlow"]
        )
    else:
        raise DeserializationError("EnableOperatorAppInput.auth_flow required")
    if "operatorAppRoleArn" in data:
        out["operator_app_role_arn"] = data["operatorAppRoleArn"]
    else:
        raise DeserializationError(
            "EnableOperatorAppInput.operator_app_role_arn required"
        )
    if "idcInstanceArn" in data:
        out["idc_instance_arn"] = data["idcInstanceArn"]
    if "issuerUrl" in data:
        out["issuer_url"] = data["issuerUrl"]
    if "idpClientId" in data:
        out["idp_client_id"] = data["idpClientId"]
    if "idpClientSecret" in data:
        out["idp_client_secret"] = data["idpClientSecret"]
    if "provider" in data:
        out["provider"] = data["provider"]
    return out
