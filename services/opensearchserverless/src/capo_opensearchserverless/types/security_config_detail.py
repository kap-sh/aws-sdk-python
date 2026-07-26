"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#SecurityConfigDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.config_description
    import capo_opensearchserverless.types.iam_federation_config_options
    import capo_opensearchserverless.types.iam_identity_center_config_options
    import capo_opensearchserverless.types.policy_version
    import capo_opensearchserverless.types.saml_config_options
    import capo_opensearchserverless.types.security_config_id
    import capo_opensearchserverless.types.security_config_type


class SecurityConfigDetail(TypedDict, closed=True):
    id: NotRequired[
        "capo_opensearchserverless.types.security_config_id.SecurityConfigId"
    ]
    """<p>The unique identifier of the security configuration.</p>"""
    type: NotRequired[
        "capo_opensearchserverless.types.security_config_type.SecurityConfigType"
    ]
    """<p>The type of security configuration.</p>"""
    config_version: NotRequired[
        "capo_opensearchserverless.types.policy_version.PolicyVersion"
    ]
    """<p>The version of the security configuration.</p>"""
    description: NotRequired[
        "capo_opensearchserverless.types.config_description.ConfigDescription"
    ]
    """<p>The description of the security configuration.</p>"""
    saml_options: NotRequired[
        "capo_opensearchserverless.types.saml_config_options.SamlConfigOptions"
    ]
    """<p>SAML options for the security configuration in the form of a key-value map.</p>"""
    iam_identity_center_options: NotRequired[
        "capo_opensearchserverless.types.iam_identity_center_config_options.IamIdentityCenterConfigOptions"
    ]
    """<p>Describes IAM Identity Center options in the form of a key-value map.</p>"""
    iam_federation_options: NotRequired[
        "capo_opensearchserverless.types.iam_federation_config_options.IamFederationConfigOptions"
    ]
    """<p>Describes IAM federation options in the form of a key-value map. Contains configuration details about how OpenSearch Serverless integrates with external identity providers through federation.</p>"""
    created_date: NotRequired["int"]
    """<p>The date the configuration was created.</p>"""
    last_modified_date: NotRequired["int"]
    """<p>The timestamp of when the configuration was last modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SecurityConfigDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "type" in value:
        out["type"] = value["type"]
    if "config_version" in value:
        out["configVersion"] = value["config_version"]
    if "description" in value:
        out["description"] = value["description"]
    if "saml_options" in value:
        import capo_opensearchserverless.types.saml_config_options

        out["samlOptions"] = (
            capo_opensearchserverless.types.saml_config_options.serialize_aws_json_1_0(
                value["saml_options"]
            )
        )
    if "iam_identity_center_options" in value:
        import capo_opensearchserverless.types.iam_identity_center_config_options

        out["iamIdentityCenterOptions"] = (
            capo_opensearchserverless.types.iam_identity_center_config_options.serialize_aws_json_1_0(
                value["iam_identity_center_options"]
            )
        )
    if "iam_federation_options" in value:
        import capo_opensearchserverless.types.iam_federation_config_options

        out["iamFederationOptions"] = (
            capo_opensearchserverless.types.iam_federation_config_options.serialize_aws_json_1_0(
                value["iam_federation_options"]
            )
        )
    if "created_date" in value:
        out["createdDate"] = value["created_date"]
    if "last_modified_date" in value:
        out["lastModifiedDate"] = value["last_modified_date"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SecurityConfigDetail:
    out: SecurityConfigDetail = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "type" in data:
        out["type"] = data["type"]
    if "configVersion" in data:
        out["config_version"] = data["configVersion"]
    if "description" in data:
        out["description"] = data["description"]
    if "samlOptions" in data:
        import capo_opensearchserverless.types.saml_config_options

        out["saml_options"] = (
            capo_opensearchserverless.types.saml_config_options.deserialize_aws_json_1_0(
                data["samlOptions"]
            )
        )
    if "iamIdentityCenterOptions" in data:
        import capo_opensearchserverless.types.iam_identity_center_config_options

        out["iam_identity_center_options"] = (
            capo_opensearchserverless.types.iam_identity_center_config_options.deserialize_aws_json_1_0(
                data["iamIdentityCenterOptions"]
            )
        )
    if "iamFederationOptions" in data:
        import capo_opensearchserverless.types.iam_federation_config_options

        out["iam_federation_options"] = (
            capo_opensearchserverless.types.iam_federation_config_options.deserialize_aws_json_1_0(
                data["iamFederationOptions"]
            )
        )
    if "createdDate" in data:
        out["created_date"] = data["createdDate"]
    if "lastModifiedDate" in data:
        out["last_modified_date"] = data["lastModifiedDate"]
    return out
