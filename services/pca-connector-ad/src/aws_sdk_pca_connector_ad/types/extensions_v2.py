"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ExtensionsV2``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pca_connector_ad.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pca_connector_ad.types.application_policies
    import aws_sdk_pca_connector_ad.types.key_usage


class ExtensionsV2(TypedDict, closed=True):
    key_usage: "aws_sdk_pca_connector_ad.types.key_usage.KeyUsage"
    """<p>The key usage extension defines the purpose (e.g., encipherment, signature, certificate signing) of the key contained in the certificate.</p>"""
    application_policies: NotRequired[
        "aws_sdk_pca_connector_ad.types.application_policies.ApplicationPolicies"
    ]
    """<p>Application policies specify what the certificate is used for and its purpose. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExtensionsV2) -> dict:
    out: dict = {}
    import aws_sdk_pca_connector_ad.types.key_usage

    out["KeyUsage"] = aws_sdk_pca_connector_ad.types.key_usage.serialize_json(
        value["key_usage"]
    )
    if "application_policies" in value:
        import aws_sdk_pca_connector_ad.types.application_policies

        out["ApplicationPolicies"] = (
            aws_sdk_pca_connector_ad.types.application_policies.serialize_json(
                value["application_policies"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExtensionsV2:
    out: ExtensionsV2 = {}  # type: ignore[typeddict-item]
    if "KeyUsage" in data:
        import aws_sdk_pca_connector_ad.types.key_usage

        out["key_usage"] = aws_sdk_pca_connector_ad.types.key_usage.deserialize_json(
            data["KeyUsage"]
        )
    else:
        raise DeserializationError("ExtensionsV2.key_usage required")
    if "ApplicationPolicies" in data:
        import aws_sdk_pca_connector_ad.types.application_policies

        out["application_policies"] = (
            aws_sdk_pca_connector_ad.types.application_policies.deserialize_json(
                data["ApplicationPolicies"]
            )
        )
    return out
