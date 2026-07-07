"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CreateSecurityConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.client_token
    import aws_sdk_opensearchserverless.types.config_description
    import aws_sdk_opensearchserverless.types.config_name
    import aws_sdk_opensearchserverless.types.create_iam_identity_center_config_options
    import aws_sdk_opensearchserverless.types.iam_federation_config_options
    import aws_sdk_opensearchserverless.types.saml_config_options
    import aws_sdk_opensearchserverless.types.security_config_type


class CreateSecurityConfigRequest(TypedDict, closed=True):
    type: "aws_sdk_opensearchserverless.types.security_config_type.SecurityConfigType"
    """<p>The type of security configuration.</p>"""
    name: "aws_sdk_opensearchserverless.types.config_name.ConfigName"
    """<p>The name of the security configuration.</p>"""
    description: NotRequired[
        "aws_sdk_opensearchserverless.types.config_description.ConfigDescription"
    ]
    """<p>A description of the security configuration.</p>"""
    saml_options: NotRequired[
        "aws_sdk_opensearchserverless.types.saml_config_options.SamlConfigOptions"
    ]
    """<p>Describes SAML options in the form of a key-value map. This field is required if you specify <code>SAML</code> for the <code>type</code> parameter.</p>"""
    iam_identity_center_options: NotRequired[
        "aws_sdk_opensearchserverless.types.create_iam_identity_center_config_options.CreateIamIdentityCenterConfigOptions"
    ]
    """<p>Describes IAM Identity Center options in the form of a key-value map. This field is required if you specify <code>iamidentitycenter</code> for the <code>type</code> parameter.</p>"""
    iam_federation_options: NotRequired[
        "aws_sdk_opensearchserverless.types.iam_federation_config_options.IamFederationConfigOptions"
    ]
    """<p>Describes IAM federation options in the form of a key-value map. This field is required if you specify <code>iamFederation</code> for the <code>type</code> parameter.</p>"""
    client_token: NotRequired[
        "aws_sdk_opensearchserverless.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateSecurityConfigRequest) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "saml_options" in value:
        import aws_sdk_opensearchserverless.types.saml_config_options

        out["samlOptions"] = (
            aws_sdk_opensearchserverless.types.saml_config_options.serialize_aws_json_1_0(
                value["saml_options"]
            )
        )
    if "iam_identity_center_options" in value:
        import aws_sdk_opensearchserverless.types.create_iam_identity_center_config_options

        out["iamIdentityCenterOptions"] = (
            aws_sdk_opensearchserverless.types.create_iam_identity_center_config_options.serialize_aws_json_1_0(
                value["iam_identity_center_options"]
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


def deserialize_aws_json_1_0(data: dict) -> CreateSecurityConfigRequest:
    out: CreateSecurityConfigRequest = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("CreateSecurityConfigRequest.type required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateSecurityConfigRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "samlOptions" in data:
        import aws_sdk_opensearchserverless.types.saml_config_options

        out["saml_options"] = (
            aws_sdk_opensearchserverless.types.saml_config_options.deserialize_aws_json_1_0(
                data["samlOptions"]
            )
        )
    if "iamIdentityCenterOptions" in data:
        import aws_sdk_opensearchserverless.types.create_iam_identity_center_config_options

        out["iam_identity_center_options"] = (
            aws_sdk_opensearchserverless.types.create_iam_identity_center_config_options.deserialize_aws_json_1_0(
                data["iamIdentityCenterOptions"]
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
