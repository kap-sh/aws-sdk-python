"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#KeyUsage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pca_connector_ad.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.key_usage_flags


class KeyUsage(TypedDict, closed=True):
    critical: NotRequired["bool"]
    """<p>Sets the key usage extension to critical.</p>"""
    usage_flags: "capo_pca_connector_ad.types.key_usage_flags.KeyUsageFlags"
    """<p>The key usage flags represent the purpose (e.g., encipherment, signature) of the key contained in the certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KeyUsage) -> dict:
    out: dict = {}
    if "critical" in value:
        out["Critical"] = value["critical"]
    import capo_pca_connector_ad.types.key_usage_flags

    out["UsageFlags"] = capo_pca_connector_ad.types.key_usage_flags.serialize_json(
        value["usage_flags"]
    )
    return out


def deserialize_json(data: dict) -> KeyUsage:
    out: KeyUsage = {}  # type: ignore[typeddict-item]
    if "Critical" in data:
        out["critical"] = data["Critical"]
    if "UsageFlags" in data:
        import capo_pca_connector_ad.types.key_usage_flags

        out["usage_flags"] = (
            capo_pca_connector_ad.types.key_usage_flags.deserialize_json(
                data["UsageFlags"]
            )
        )
    else:
        raise DeserializationError("KeyUsage.usage_flags required")
    return out
