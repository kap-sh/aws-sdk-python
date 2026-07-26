"""Generated from Smithy shape ``com.amazonaws.mediapackage#Authorization``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage.types.__string


class Authorization(TypedDict, closed=True):
    cdn_identifier_secret: NotRequired["capo_mediapackage.types.__string.__string"]
    """The Amazon Resource Name (ARN) for the secret in Secrets Manager that your Content Distribution Network (CDN) uses for authorization to access your endpoint."""
    secrets_role_arn: NotRequired["capo_mediapackage.types.__string.__string"]
    """The Amazon Resource Name (ARN) for the IAM role that allows MediaPackage to communicate with AWS Secrets Manager."""


# --- restJson1 ser/de ---
def serialize_json(value: Authorization) -> dict:
    out: dict = {}
    if "cdn_identifier_secret" in value:
        out["cdnIdentifierSecret"] = value["cdn_identifier_secret"]
    if "secrets_role_arn" in value:
        out["secretsRoleArn"] = value["secrets_role_arn"]
    return out


def deserialize_json(data: dict) -> Authorization:
    out: Authorization = {}  # type: ignore[typeddict-item]
    if "cdnIdentifierSecret" in data:
        out["cdn_identifier_secret"] = data["cdnIdentifierSecret"]
    if "secretsRoleArn" in data:
        out["secrets_role_arn"] = data["secretsRoleArn"]
    return out
