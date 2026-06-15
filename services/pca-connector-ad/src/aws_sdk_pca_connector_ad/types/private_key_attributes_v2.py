"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#PrivateKeyAttributesV2``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pca_connector_ad.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pca_connector_ad.types.crypto_providers_list
    import aws_sdk_pca_connector_ad.types.key_spec


class PrivateKeyAttributesV2(TypedDict):
    minimal_key_length: "int"
    """<p>Set the minimum key length of the private key.</p>"""
    key_spec: "aws_sdk_pca_connector_ad.types.key_spec.KeySpec"
    r"""<p>Defines the purpose of the private key. Set it to \"KEY_EXCHANGE\" or \"SIGNATURE\" value.</p>"""
    crypto_providers: NotRequired[
        "aws_sdk_pca_connector_ad.types.crypto_providers_list.CryptoProvidersList"
    ]
    """<p>Defines the cryptographic providers used to generate the private key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrivateKeyAttributesV2) -> dict:
    out: dict = {}
    out["MinimalKeyLength"] = value["minimal_key_length"]
    import aws_sdk_pca_connector_ad.types.key_spec

    out["KeySpec"] = aws_sdk_pca_connector_ad.types.key_spec.serialize_json(
        value["key_spec"]
    )
    if "crypto_providers" in value:
        import aws_sdk_pca_connector_ad.types.crypto_providers_list

        out["CryptoProviders"] = (
            aws_sdk_pca_connector_ad.types.crypto_providers_list.serialize_json(
                value["crypto_providers"]
            )
        )
    return out


def deserialize_json(data: dict) -> PrivateKeyAttributesV2:
    out: PrivateKeyAttributesV2 = {}  # type: ignore[typeddict-item]
    if "MinimalKeyLength" in data:
        out["minimal_key_length"] = data["MinimalKeyLength"]
    else:
        raise DeserializationError("PrivateKeyAttributesV2.minimal_key_length required")
    if "KeySpec" in data:
        import aws_sdk_pca_connector_ad.types.key_spec

        out["key_spec"] = aws_sdk_pca_connector_ad.types.key_spec.deserialize_json(
            data["KeySpec"]
        )
    else:
        raise DeserializationError("PrivateKeyAttributesV2.key_spec required")
    if "CryptoProviders" in data:
        import aws_sdk_pca_connector_ad.types.crypto_providers_list

        out["crypto_providers"] = (
            aws_sdk_pca_connector_ad.types.crypto_providers_list.deserialize_json(
                data["CryptoProviders"]
            )
        )
    return out
