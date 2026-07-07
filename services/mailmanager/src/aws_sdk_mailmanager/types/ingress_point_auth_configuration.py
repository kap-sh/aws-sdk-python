"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressPointAuthConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.ingress_point_password_configuration
    import aws_sdk_mailmanager.types.secret_arn
    import aws_sdk_mailmanager.types.tls_auth_configuration


class IngressPointAuthConfiguration(TypedDict, closed=True):
    ingress_point_password_configuration: NotRequired[
        "aws_sdk_mailmanager.types.ingress_point_password_configuration.IngressPointPasswordConfiguration"
    ]
    """<p>The ingress endpoint password configuration for the ingress endpoint resource.</p>"""
    secret_arn: NotRequired["aws_sdk_mailmanager.types.secret_arn.SecretArn"]
    """<p>The ingress endpoint SecretsManager::Secret ARN configuration for the ingress endpoint resource.</p>"""
    tls_auth_configuration: NotRequired[
        "aws_sdk_mailmanager.types.tls_auth_configuration.TlsAuthConfiguration"
    ]
    """<p>The mutual TLS authentication configuration for the ingress endpoint resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressPointAuthConfiguration) -> dict:
    out: dict = {}
    if "ingress_point_password_configuration" in value:
        import aws_sdk_mailmanager.types.ingress_point_password_configuration

        out["IngressPointPasswordConfiguration"] = (
            aws_sdk_mailmanager.types.ingress_point_password_configuration.serialize_aws_json_1_0(
                value["ingress_point_password_configuration"]
            )
        )
    if "secret_arn" in value:
        out["SecretArn"] = value["secret_arn"]
    if "tls_auth_configuration" in value:
        import aws_sdk_mailmanager.types.tls_auth_configuration

        out["TlsAuthConfiguration"] = (
            aws_sdk_mailmanager.types.tls_auth_configuration.serialize_aws_json_1_0(
                value["tls_auth_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IngressPointAuthConfiguration:
    out: IngressPointAuthConfiguration = {}  # type: ignore[typeddict-item]
    if "IngressPointPasswordConfiguration" in data:
        import aws_sdk_mailmanager.types.ingress_point_password_configuration

        out["ingress_point_password_configuration"] = (
            aws_sdk_mailmanager.types.ingress_point_password_configuration.deserialize_aws_json_1_0(
                data["IngressPointPasswordConfiguration"]
            )
        )
    if "SecretArn" in data:
        out["secret_arn"] = data["SecretArn"]
    if "TlsAuthConfiguration" in data:
        import aws_sdk_mailmanager.types.tls_auth_configuration

        out["tls_auth_configuration"] = (
            aws_sdk_mailmanager.types.tls_auth_configuration.deserialize_aws_json_1_0(
                data["TlsAuthConfiguration"]
            )
        )
    return out
