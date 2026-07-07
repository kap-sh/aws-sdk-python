"""Generated from Smithy shape ``com.amazonaws.qbusiness#OpenIDConnectProviderConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.role_arn
    import aws_sdk_qbusiness.types.secret_arn


class OpenIDConnectProviderConfiguration(TypedDict, closed=True):
    secrets_arn: "aws_sdk_qbusiness.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name (ARN) of a Secrets Manager secret containing the OIDC client secret.</p>"""
    secrets_role: "aws_sdk_qbusiness.types.role_arn.RoleArn"
    """<p>An IAM role with permissions to access KMS to decrypt the Secrets Manager secret containing your OIDC client secret.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OpenIDConnectProviderConfiguration) -> dict:
    out: dict = {}
    out["secretsArn"] = value["secrets_arn"]
    out["secretsRole"] = value["secrets_role"]
    return out


def deserialize_json(data: dict) -> OpenIDConnectProviderConfiguration:
    out: OpenIDConnectProviderConfiguration = {}  # type: ignore[typeddict-item]
    if "secretsArn" in data:
        out["secrets_arn"] = data["secretsArn"]
    else:
        raise DeserializationError(
            "OpenIDConnectProviderConfiguration.secrets_arn required"
        )
    if "secretsRole" in data:
        out["secrets_role"] = data["secretsRole"]
    else:
        raise DeserializationError(
            "OpenIDConnectProviderConfiguration.secrets_role required"
        )
    return out
