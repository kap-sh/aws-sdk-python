"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisteredAzureIdentityDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.guid
    import aws_sdk_devops_agent.types.role_arn
    import aws_sdk_devops_agent.types.web_identity_token_audience_list


class RegisteredAzureIdentityDetails(TypedDict, closed=True):
    tenant_id: "aws_sdk_devops_agent.types.guid.Guid"
    """<p>The Azure Active Directory tenant ID for the identity.</p>"""
    client_id: "aws_sdk_devops_agent.types.guid.Guid"
    """<p>The client ID of the service principal or managed identity used for authentication.</p>"""
    web_identity_role_arn: "aws_sdk_devops_agent.types.role_arn.RoleArn"
    """<p>The role ARN to be assumed by DevOps Agent for requesting Web Identity Token.</p>"""
    web_identity_token_audiences: "aws_sdk_devops_agent.types.web_identity_token_audience_list.WebIdentityTokenAudienceList"
    """<p>The audiences for the Web Identity Token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredAzureIdentityDetails) -> dict:
    out: dict = {}
    out["tenantId"] = value["tenant_id"]
    out["clientId"] = value["client_id"]
    out["webIdentityRoleArn"] = value["web_identity_role_arn"]
    import aws_sdk_devops_agent.types.web_identity_token_audience_list

    out["webIdentityTokenAudiences"] = (
        aws_sdk_devops_agent.types.web_identity_token_audience_list.serialize_json(
            value["web_identity_token_audiences"]
        )
    )
    return out


def deserialize_json(data: dict) -> RegisteredAzureIdentityDetails:
    out: RegisteredAzureIdentityDetails = {}  # type: ignore[typeddict-item]
    if "tenantId" in data:
        out["tenant_id"] = data["tenantId"]
    else:
        raise DeserializationError("RegisteredAzureIdentityDetails.tenant_id required")
    if "clientId" in data:
        out["client_id"] = data["clientId"]
    else:
        raise DeserializationError("RegisteredAzureIdentityDetails.client_id required")
    if "webIdentityRoleArn" in data:
        out["web_identity_role_arn"] = data["webIdentityRoleArn"]
    else:
        raise DeserializationError(
            "RegisteredAzureIdentityDetails.web_identity_role_arn required"
        )
    if "webIdentityTokenAudiences" in data:
        import aws_sdk_devops_agent.types.web_identity_token_audience_list

        out["web_identity_token_audiences"] = (
            aws_sdk_devops_agent.types.web_identity_token_audience_list.deserialize_json(
                data["webIdentityTokenAudiences"]
            )
        )
    else:
        raise DeserializationError(
            "RegisteredAzureIdentityDetails.web_identity_token_audiences required"
        )
    return out
