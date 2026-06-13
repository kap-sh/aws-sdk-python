"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#PrivateKeyFlagsV2``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pca_connector_ad.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pca_connector_ad.types.client_compatibility_v2


class PrivateKeyFlagsV2(TypedDict):
    exportable_key: NotRequired["bool"]
    """<p>Allows the private key to be exported.</p>"""
    strong_key_protection_required: NotRequired["bool"]
    """<p>Require user input when using the private key for enrollment.</p>"""
    client_version: (
        "aws_sdk_pca_connector_ad.types.client_compatibility_v2.ClientCompatibilityV2"
    )
    """<p>Defines the minimum client compatibility.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrivateKeyFlagsV2) -> dict:
    out: dict = {}
    if "exportable_key" in value:
        out["ExportableKey"] = value["exportable_key"]
    if "strong_key_protection_required" in value:
        out["StrongKeyProtectionRequired"] = value["strong_key_protection_required"]
    import aws_sdk_pca_connector_ad.types.client_compatibility_v2

    out["ClientVersion"] = (
        aws_sdk_pca_connector_ad.types.client_compatibility_v2.serialize_json(
            value["client_version"]
        )
    )
    return out


def deserialize_json(data: dict) -> PrivateKeyFlagsV2:
    out: PrivateKeyFlagsV2 = {}  # type: ignore[typeddict-item]
    if "ExportableKey" in data:
        out["exportable_key"] = data["ExportableKey"]
    if "StrongKeyProtectionRequired" in data:
        out["strong_key_protection_required"] = data["StrongKeyProtectionRequired"]
    if "ClientVersion" in data:
        import aws_sdk_pca_connector_ad.types.client_compatibility_v2

        out["client_version"] = (
            aws_sdk_pca_connector_ad.types.client_compatibility_v2.deserialize_json(
                data["ClientVersion"]
            )
        )
    else:
        raise DeserializationError("PrivateKeyFlagsV2.client_version required")
    return out
