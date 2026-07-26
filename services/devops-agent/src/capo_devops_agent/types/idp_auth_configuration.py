"""Generated from Smithy shape ``com.amazonaws.devopsagent#IdpAuthConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class IdpAuthConfiguration(TypedDict, closed=True):
    issuer_url: "str"
    """<p>The OIDC issuer URL of the external Identity Provider</p>"""
    client_id: "str"
    """<p>The OIDC client ID for the IdP application</p>"""
    operator_app_role_arn: "str"
    """<p>The IAM role end users assume to access AIDevOps APIs</p>"""
    provider: "str"
    """<p>The Identity Provider name (e.g., Entra, Okta, Google)</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the Operator App IdP auth flow was enabled.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the Operator App IdP auth flow was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdpAuthConfiguration) -> dict:
    out: dict = {}
    out["issuerUrl"] = value["issuer_url"]
    out["clientId"] = value["client_id"]
    out["operatorAppRoleArn"] = value["operator_app_role_arn"]
    out["provider"] = value["provider"]
    import capo_devops_agent.types._prelude.timestamp

    out["createdAt"] = capo_devops_agent.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    if "updated_at" in value:
        import capo_devops_agent.types._prelude.timestamp

        out["updatedAt"] = capo_devops_agent.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> IdpAuthConfiguration:
    out: IdpAuthConfiguration = {}  # type: ignore[typeddict-item]
    if "issuerUrl" in data:
        out["issuer_url"] = data["issuerUrl"]
    else:
        raise DeserializationError("IdpAuthConfiguration.issuer_url required")
    if "clientId" in data:
        out["client_id"] = data["clientId"]
    else:
        raise DeserializationError("IdpAuthConfiguration.client_id required")
    if "operatorAppRoleArn" in data:
        out["operator_app_role_arn"] = data["operatorAppRoleArn"]
    else:
        raise DeserializationError(
            "IdpAuthConfiguration.operator_app_role_arn required"
        )
    if "provider" in data:
        out["provider"] = data["provider"]
    else:
        raise DeserializationError("IdpAuthConfiguration.provider required")
    if "createdAt" in data:
        import capo_devops_agent.types._prelude.timestamp

        out["created_at"] = capo_devops_agent.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("IdpAuthConfiguration.created_at required")
    if "updatedAt" in data:
        import capo_devops_agent.types._prelude.timestamp

        out["updated_at"] = capo_devops_agent.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    return out
