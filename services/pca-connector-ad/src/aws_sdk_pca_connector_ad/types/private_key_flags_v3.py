"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#PrivateKeyFlagsV3``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pca_connector_ad.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pca_connector_ad.types.client_compatibility_v3


class PrivateKeyFlagsV3(TypedDict, closed=True):
    exportable_key: NotRequired["bool"]
    """<p>Allows the private key to be exported.</p>"""
    strong_key_protection_required: NotRequired["bool"]
    """<p>Requirer user input when using the private key for enrollment.</p>"""
    require_alternate_signature_algorithm: NotRequired["bool"]
    """<p>Reguires the PKCS #1 v2.1 signature format for certificates. You should verify that your CA, objects, and applications can accept this signature format.</p>"""
    client_version: (
        "aws_sdk_pca_connector_ad.types.client_compatibility_v3.ClientCompatibilityV3"
    )
    """<p>Defines the minimum client compatibility.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrivateKeyFlagsV3) -> dict:
    out: dict = {}
    if "exportable_key" in value:
        out["ExportableKey"] = value["exportable_key"]
    if "strong_key_protection_required" in value:
        out["StrongKeyProtectionRequired"] = value["strong_key_protection_required"]
    if "require_alternate_signature_algorithm" in value:
        out["RequireAlternateSignatureAlgorithm"] = value[
            "require_alternate_signature_algorithm"
        ]
    import aws_sdk_pca_connector_ad.types.client_compatibility_v3

    out["ClientVersion"] = (
        aws_sdk_pca_connector_ad.types.client_compatibility_v3.serialize_json(
            value["client_version"]
        )
    )
    return out


def deserialize_json(data: dict) -> PrivateKeyFlagsV3:
    out: PrivateKeyFlagsV3 = {}  # type: ignore[typeddict-item]
    if "ExportableKey" in data:
        out["exportable_key"] = data["ExportableKey"]
    if "StrongKeyProtectionRequired" in data:
        out["strong_key_protection_required"] = data["StrongKeyProtectionRequired"]
    if "RequireAlternateSignatureAlgorithm" in data:
        out["require_alternate_signature_algorithm"] = data[
            "RequireAlternateSignatureAlgorithm"
        ]
    if "ClientVersion" in data:
        import aws_sdk_pca_connector_ad.types.client_compatibility_v3

        out["client_version"] = (
            aws_sdk_pca_connector_ad.types.client_compatibility_v3.deserialize_json(
                data["ClientVersion"]
            )
        )
    else:
        raise DeserializationError("PrivateKeyFlagsV3.client_version required")
    return out
