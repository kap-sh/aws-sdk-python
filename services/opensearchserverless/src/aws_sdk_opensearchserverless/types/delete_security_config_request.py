"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#DeleteSecurityConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.client_token
    import aws_sdk_opensearchserverless.types.security_config_id


class DeleteSecurityConfigRequest(TypedDict, closed=True):
    id: "aws_sdk_opensearchserverless.types.security_config_id.SecurityConfigId"
    """<p>The security configuration identifier. For SAML the ID will be <code>saml/&lt;accountId&gt;/&lt;idpProviderName&gt;</code>. For example, <code>saml/123456789123/OKTADev</code>.</p>"""
    client_token: NotRequired[
        "aws_sdk_opensearchserverless.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteSecurityConfigRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteSecurityConfigRequest:
    out: DeleteSecurityConfigRequest = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DeleteSecurityConfigRequest.id required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
