"""Generated from Smithy shape ``com.amazonaws.medialive#MediaConnectRouterOutputDestinationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.media_connect_router_output_encryption_type


class MediaConnectRouterOutputDestinationSettings(TypedDict, closed=True):
    encryption_type: NotRequired[
        "capo_medialive.types.media_connect_router_output_encryption_type.MediaConnectRouterOutputEncryptionType"
    ]
    """Encryption configuration for MediaConnect router. When using SECRETS_MANAGER encryption, you must provide the ARN of the secret used to encrypt data in transit. When using AUTOMATIC encryption, a service-managed secret will be used instead."""
    secret_arn: NotRequired["capo_medialive.types.__string.__string"]
    """ARN of the secret used to encrypt this input. Used only with the SECRETS_MANAGER encryption type."""


# --- restJson1 ser/de ---
def serialize_json(value: MediaConnectRouterOutputDestinationSettings) -> dict:
    out: dict = {}
    if "encryption_type" in value:
        import capo_medialive.types.media_connect_router_output_encryption_type

        out["encryptionType"] = (
            capo_medialive.types.media_connect_router_output_encryption_type.serialize_json(
                value["encryption_type"]
            )
        )
    if "secret_arn" in value:
        out["secretArn"] = value["secret_arn"]
    return out


def deserialize_json(data: dict) -> MediaConnectRouterOutputDestinationSettings:
    out: MediaConnectRouterOutputDestinationSettings = {}  # type: ignore[typeddict-item]
    if "encryptionType" in data:
        import capo_medialive.types.media_connect_router_output_encryption_type

        out["encryption_type"] = (
            capo_medialive.types.media_connect_router_output_encryption_type.deserialize_json(
                data["encryptionType"]
            )
        )
    if "secretArn" in data:
        out["secret_arn"] = data["secretArn"]
    return out
