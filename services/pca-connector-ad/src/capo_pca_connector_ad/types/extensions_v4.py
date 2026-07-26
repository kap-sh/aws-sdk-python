"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ExtensionsV4``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pca_connector_ad.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.application_policies
    import capo_pca_connector_ad.types.key_usage


class ExtensionsV4(TypedDict, closed=True):
    key_usage: "capo_pca_connector_ad.types.key_usage.KeyUsage"
    """<p>The key usage extension defines the purpose (e.g., encipherment, signature) of the key contained in the certificate.</p>"""
    application_policies: NotRequired[
        "capo_pca_connector_ad.types.application_policies.ApplicationPolicies"
    ]
    """<p>Application policies specify what the certificate is used for and its purpose.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExtensionsV4) -> dict:
    out: dict = {}
    import capo_pca_connector_ad.types.key_usage

    out["KeyUsage"] = capo_pca_connector_ad.types.key_usage.serialize_json(
        value["key_usage"]
    )
    if "application_policies" in value:
        import capo_pca_connector_ad.types.application_policies

        out["ApplicationPolicies"] = (
            capo_pca_connector_ad.types.application_policies.serialize_json(
                value["application_policies"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExtensionsV4:
    out: ExtensionsV4 = {}  # type: ignore[typeddict-item]
    if "KeyUsage" in data:
        import capo_pca_connector_ad.types.key_usage

        out["key_usage"] = capo_pca_connector_ad.types.key_usage.deserialize_json(
            data["KeyUsage"]
        )
    else:
        raise DeserializationError("ExtensionsV4.key_usage required")
    if "ApplicationPolicies" in data:
        import capo_pca_connector_ad.types.application_policies

        out["application_policies"] = (
            capo_pca_connector_ad.types.application_policies.deserialize_json(
                data["ApplicationPolicies"]
            )
        )
    return out
