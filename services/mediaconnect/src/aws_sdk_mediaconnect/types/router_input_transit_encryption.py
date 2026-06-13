"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputTransitEncryption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_input_transit_encryption_key_configuration
    import aws_sdk_mediaconnect.types.router_input_transit_encryption_key_type


class RouterInputTransitEncryption(TypedDict):
    encryption_key_type: NotRequired[
        "aws_sdk_mediaconnect.types.router_input_transit_encryption_key_type.RouterInputTransitEncryptionKeyType"
    ]
    """<p>Specifies the type of encryption key to use for transit encryption.</p>"""
    encryption_key_configuration: "aws_sdk_mediaconnect.types.router_input_transit_encryption_key_configuration.RouterInputTransitEncryptionKeyConfiguration"
    """<p>Contains the configuration details for the encryption key used in transit encryption, including the key source and associated parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputTransitEncryption) -> dict:
    out: dict = {}
    if "encryption_key_type" in value:
        import aws_sdk_mediaconnect.types.router_input_transit_encryption_key_type

        out["encryptionKeyType"] = (
            aws_sdk_mediaconnect.types.router_input_transit_encryption_key_type.serialize_json(
                value["encryption_key_type"]
            )
        )
    import aws_sdk_mediaconnect.types.router_input_transit_encryption_key_configuration

    out["encryptionKeyConfiguration"] = (
        aws_sdk_mediaconnect.types.router_input_transit_encryption_key_configuration.serialize_json(
            value["encryption_key_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> RouterInputTransitEncryption:
    out: RouterInputTransitEncryption = {}  # type: ignore[typeddict-item]
    if "encryptionKeyType" in data:
        import aws_sdk_mediaconnect.types.router_input_transit_encryption_key_type

        out["encryption_key_type"] = (
            aws_sdk_mediaconnect.types.router_input_transit_encryption_key_type.deserialize_json(
                data["encryptionKeyType"]
            )
        )
    if "encryptionKeyConfiguration" in data:
        import aws_sdk_mediaconnect.types.router_input_transit_encryption_key_configuration

        out["encryption_key_configuration"] = (
            aws_sdk_mediaconnect.types.router_input_transit_encryption_key_configuration.deserialize_json(
                data["encryptionKeyConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "RouterInputTransitEncryption.encryption_key_configuration required"
        )
    return out
