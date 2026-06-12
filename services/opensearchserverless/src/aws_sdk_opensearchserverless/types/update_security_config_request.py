"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#UpdateSecurityConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.client_token
    import aws_sdk_opensearchserverless.types.config_description
    import aws_sdk_opensearchserverless.types.iam_federation_config_options
    import aws_sdk_opensearchserverless.types.policy_version
    import aws_sdk_opensearchserverless.types.saml_config_options
    import aws_sdk_opensearchserverless.types.security_config_id
    import aws_sdk_opensearchserverless.types.update_iam_identity_center_config_options


class UpdateSecurityConfigRequest(TypedDict):
    id: "aws_sdk_opensearchserverless.types.security_config_id.SecurityConfigId"
    """<p>The security configuration identifier. For SAML the ID will be <code>saml/&lt;accountId&gt;/&lt;idpProviderName&gt;</code>. For example, <code>saml/123456789123/OKTADev</code>.</p>"""
    config_version: "aws_sdk_opensearchserverless.types.policy_version.PolicyVersion"
    """<p>The version of the security configuration to be updated. You can find the most recent version of a security configuration using the <code>GetSecurityPolicy</code> command.</p>"""
    description: NotRequired[
        "aws_sdk_opensearchserverless.types.config_description.ConfigDescription"
    ]
    """<p>A description of the security configuration.</p>"""
    saml_options: NotRequired[
        "aws_sdk_opensearchserverless.types.saml_config_options.SamlConfigOptions"
    ]
    """<p>SAML options in in the form of a key-value map.</p>"""
    iam_identity_center_options_updates: NotRequired[
        "aws_sdk_opensearchserverless.types.update_iam_identity_center_config_options.UpdateIamIdentityCenterConfigOptions"
    ]
    """<p>Describes IAM Identity Center options in the form of a key-value map.</p>"""
    iam_federation_options: NotRequired[
        "aws_sdk_opensearchserverless.types.iam_federation_config_options.IamFederationConfigOptions"
    ]
    """<p>Describes IAM federation options in the form of a key-value map for updating an existing security configuration. Use this field to modify IAM federation settings for the security configuration.</p>"""
    client_token: NotRequired[
        "aws_sdk_opensearchserverless.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateSecurityConfigRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["configVersion"] = value["config_version"]
    if "description" in value:
        out["description"] = value["description"]
    if "saml_options" in value:
        import aws_sdk_opensearchserverless.types.saml_config_options

        out["samlOptions"] = (
            aws_sdk_opensearchserverless.types.saml_config_options.serialize_aws_json_1_0(
                value["saml_options"]
            )
        )
    if "iam_identity_center_options_updates" in value:
        import aws_sdk_opensearchserverless.types.update_iam_identity_center_config_options

        out["iamIdentityCenterOptionsUpdates"] = (
            aws_sdk_opensearchserverless.types.update_iam_identity_center_config_options.serialize_aws_json_1_0(
                value["iam_identity_center_options_updates"]
            )
        )
    if "iam_federation_options" in value:
        import aws_sdk_opensearchserverless.types.iam_federation_config_options

        out["iamFederationOptions"] = (
            aws_sdk_opensearchserverless.types.iam_federation_config_options.serialize_aws_json_1_0(
                value["iam_federation_options"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateSecurityConfigRequest:
    out: UpdateSecurityConfigRequest = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateSecurityConfigRequest.id required")
    if "configVersion" in data:
        out["config_version"] = data["configVersion"]
    else:
        raise DeserializationError(
            "UpdateSecurityConfigRequest.config_version required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "samlOptions" in data:
        import aws_sdk_opensearchserverless.types.saml_config_options

        out["saml_options"] = (
            aws_sdk_opensearchserverless.types.saml_config_options.deserialize_aws_json_1_0(
                data["samlOptions"]
            )
        )
    if "iamIdentityCenterOptionsUpdates" in data:
        import aws_sdk_opensearchserverless.types.update_iam_identity_center_config_options

        out["iam_identity_center_options_updates"] = (
            aws_sdk_opensearchserverless.types.update_iam_identity_center_config_options.deserialize_aws_json_1_0(
                data["iamIdentityCenterOptionsUpdates"]
            )
        )
    if "iamFederationOptions" in data:
        import aws_sdk_opensearchserverless.types.iam_federation_config_options

        out["iam_federation_options"] = (
            aws_sdk_opensearchserverless.types.iam_federation_config_options.deserialize_aws_json_1_0(
                data["iamFederationOptions"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
