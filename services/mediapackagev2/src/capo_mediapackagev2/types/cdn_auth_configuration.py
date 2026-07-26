"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#CdnAuthConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediapackagev2.types.cdn_identifier_secret_arns


class CdnAuthConfiguration(TypedDict, closed=True):
    cdn_identifier_secret_arns: (
        "capo_mediapackagev2.types.cdn_identifier_secret_arns.CdnIdentifierSecretArns"
    )
    """<p>The ARN for the secret in Secrets Manager that your CDN uses for authorization to access the endpoint.</p>"""
    secrets_role_arn: "str"
    """<p>The ARN for the IAM role that gives MediaPackage read access to Secrets Manager and KMS for CDN authorization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CdnAuthConfiguration) -> dict:
    out: dict = {}
    import capo_mediapackagev2.types.cdn_identifier_secret_arns

    out["CdnIdentifierSecretArns"] = (
        capo_mediapackagev2.types.cdn_identifier_secret_arns.serialize_json(
            value["cdn_identifier_secret_arns"]
        )
    )
    out["SecretsRoleArn"] = value["secrets_role_arn"]
    return out


def deserialize_json(data: dict) -> CdnAuthConfiguration:
    out: CdnAuthConfiguration = {}  # type: ignore[typeddict-item]
    if "CdnIdentifierSecretArns" in data:
        import capo_mediapackagev2.types.cdn_identifier_secret_arns

        out["cdn_identifier_secret_arns"] = (
            capo_mediapackagev2.types.cdn_identifier_secret_arns.deserialize_json(
                data["CdnIdentifierSecretArns"]
            )
        )
    else:
        raise DeserializationError(
            "CdnAuthConfiguration.cdn_identifier_secret_arns required"
        )
    if "SecretsRoleArn" in data:
        out["secrets_role_arn"] = data["SecretsRoleArn"]
    else:
        raise DeserializationError("CdnAuthConfiguration.secrets_role_arn required")
    return out
