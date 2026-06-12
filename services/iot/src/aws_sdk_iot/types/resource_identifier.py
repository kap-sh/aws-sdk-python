"""Generated from Smithy shape ``com.amazonaws.iot#ResourceIdentifier``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.aws_account_id
    import aws_sdk_iot.types.certificate_arn
    import aws_sdk_iot.types.certificate_id
    import aws_sdk_iot.types.client_id
    import aws_sdk_iot.types.cognito_identity_pool_id
    import aws_sdk_iot.types.issuer_certificate_identifier
    import aws_sdk_iot.types.policy_version_identifier
    import aws_sdk_iot.types.role_alias_arn
    import aws_sdk_iot.types.role_arn


class ResourceIdentifier(TypedDict):
    device_certificate_id: NotRequired["aws_sdk_iot.types.certificate_id.CertificateId"]
    """<p>The ID of the certificate attached to the resource.</p>"""
    ca_certificate_id: NotRequired["aws_sdk_iot.types.certificate_id.CertificateId"]
    """<p>The ID of the CA certificate used to authorize the certificate.</p>"""
    cognito_identity_pool_id: NotRequired[
        "aws_sdk_iot.types.cognito_identity_pool_id.CognitoIdentityPoolId"
    ]
    """<p>The ID of the Amazon Cognito identity pool.</p>"""
    client_id: NotRequired["aws_sdk_iot.types.client_id.ClientId"]
    """<p>The client ID.</p>"""
    policy_version_identifier: NotRequired[
        "aws_sdk_iot.types.policy_version_identifier.PolicyVersionIdentifier"
    ]
    """<p>The version of the policy associated with the resource.</p>"""
    account: NotRequired["aws_sdk_iot.types.aws_account_id.AwsAccountId"]
    """<p>The account with which the resource is associated.</p>"""
    iam_role_arn: NotRequired["aws_sdk_iot.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM role that has overly permissive actions.</p>"""
    role_alias_arn: NotRequired["aws_sdk_iot.types.role_alias_arn.RoleAliasArn"]
    """<p>The ARN of the role alias that has overly permissive actions.</p>"""
    issuer_certificate_identifier: NotRequired[
        "aws_sdk_iot.types.issuer_certificate_identifier.IssuerCertificateIdentifier"
    ]
    """<p>The issuer certificate identifier.</p>"""
    device_certificate_arn: NotRequired[
        "aws_sdk_iot.types.certificate_arn.CertificateArn"
    ]
    """<p>The ARN of the identified device certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceIdentifier) -> dict:
    out: dict = {}
    if "device_certificate_id" in value:
        out["deviceCertificateId"] = value["device_certificate_id"]
    if "ca_certificate_id" in value:
        out["caCertificateId"] = value["ca_certificate_id"]
    if "cognito_identity_pool_id" in value:
        out["cognitoIdentityPoolId"] = value["cognito_identity_pool_id"]
    if "client_id" in value:
        out["clientId"] = value["client_id"]
    if "policy_version_identifier" in value:
        import aws_sdk_iot.types.policy_version_identifier

        out["policyVersionIdentifier"] = (
            aws_sdk_iot.types.policy_version_identifier.serialize_json(
                value["policy_version_identifier"]
            )
        )
    if "account" in value:
        out["account"] = value["account"]
    if "iam_role_arn" in value:
        out["iamRoleArn"] = value["iam_role_arn"]
    if "role_alias_arn" in value:
        out["roleAliasArn"] = value["role_alias_arn"]
    if "issuer_certificate_identifier" in value:
        import aws_sdk_iot.types.issuer_certificate_identifier

        out["issuerCertificateIdentifier"] = (
            aws_sdk_iot.types.issuer_certificate_identifier.serialize_json(
                value["issuer_certificate_identifier"]
            )
        )
    if "device_certificate_arn" in value:
        out["deviceCertificateArn"] = value["device_certificate_arn"]
    return out


def deserialize_json(data: dict) -> ResourceIdentifier:
    out: ResourceIdentifier = {}  # type: ignore[typeddict-item]
    if "deviceCertificateId" in data:
        out["device_certificate_id"] = data["deviceCertificateId"]
    if "caCertificateId" in data:
        out["ca_certificate_id"] = data["caCertificateId"]
    if "cognitoIdentityPoolId" in data:
        out["cognito_identity_pool_id"] = data["cognitoIdentityPoolId"]
    if "clientId" in data:
        out["client_id"] = data["clientId"]
    if "policyVersionIdentifier" in data:
        import aws_sdk_iot.types.policy_version_identifier

        out["policy_version_identifier"] = (
            aws_sdk_iot.types.policy_version_identifier.deserialize_json(
                data["policyVersionIdentifier"]
            )
        )
    if "account" in data:
        out["account"] = data["account"]
    if "iamRoleArn" in data:
        out["iam_role_arn"] = data["iamRoleArn"]
    if "roleAliasArn" in data:
        out["role_alias_arn"] = data["roleAliasArn"]
    if "issuerCertificateIdentifier" in data:
        import aws_sdk_iot.types.issuer_certificate_identifier

        out["issuer_certificate_identifier"] = (
            aws_sdk_iot.types.issuer_certificate_identifier.deserialize_json(
                data["issuerCertificateIdentifier"]
            )
        )
    if "deviceCertificateArn" in data:
        out["device_certificate_arn"] = data["deviceCertificateArn"]
    return out
