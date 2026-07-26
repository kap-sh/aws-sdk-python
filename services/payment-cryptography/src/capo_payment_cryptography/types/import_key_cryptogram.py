"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ImportKeyCryptogram``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography.types.import_token_id
    import capo_payment_cryptography.types.key_attributes
    import capo_payment_cryptography.types.wrapped_key_cryptogram
    import capo_payment_cryptography.types.wrapping_key_spec


class ImportKeyCryptogram(TypedDict, closed=True):
    key_attributes: "capo_payment_cryptography.types.key_attributes.KeyAttributes"
    exportable: "bool"
    """<p>Specifies whether the key is exportable from the service.</p>"""
    wrapped_key_cryptogram: (
        "capo_payment_cryptography.types.wrapped_key_cryptogram.WrappedKeyCryptogram"
    )
    """<p>The RSA wrapped key cryptogram under import.</p>"""
    import_token: "capo_payment_cryptography.types.import_token_id.ImportTokenId"
    """<p>The import token that initiates key import using the asymmetric RSA wrap and unwrap key exchange method into AWS Payment Cryptography. It expires after 30 days. You can use the same import token to import multiple keys to the same service account.</p>"""
    wrapping_spec: NotRequired[
        "capo_payment_cryptography.types.wrapping_key_spec.WrappingKeySpec"
    ]
    """<p>The wrapping spec for the wrapped key cryptogram.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportKeyCryptogram) -> dict:
    out: dict = {}
    import capo_payment_cryptography.types.key_attributes

    out["KeyAttributes"] = (
        capo_payment_cryptography.types.key_attributes.serialize_aws_json_1_0(
            value["key_attributes"]
        )
    )
    out["Exportable"] = value["exportable"]
    out["WrappedKeyCryptogram"] = value["wrapped_key_cryptogram"]
    out["ImportToken"] = value["import_token"]
    if "wrapping_spec" in value:
        out["WrappingSpec"] = value["wrapping_spec"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ImportKeyCryptogram:
    out: ImportKeyCryptogram = {}  # type: ignore[typeddict-item]
    if "KeyAttributes" in data:
        import capo_payment_cryptography.types.key_attributes

        out["key_attributes"] = (
            capo_payment_cryptography.types.key_attributes.deserialize_aws_json_1_0(
                data["KeyAttributes"]
            )
        )
    else:
        raise DeserializationError("ImportKeyCryptogram.key_attributes required")
    if "Exportable" in data:
        out["exportable"] = data["Exportable"]
    else:
        raise DeserializationError("ImportKeyCryptogram.exportable required")
    if "WrappedKeyCryptogram" in data:
        out["wrapped_key_cryptogram"] = data["WrappedKeyCryptogram"]
    else:
        raise DeserializationError(
            "ImportKeyCryptogram.wrapped_key_cryptogram required"
        )
    if "ImportToken" in data:
        out["import_token"] = data["ImportToken"]
    else:
        raise DeserializationError("ImportKeyCryptogram.import_token required")
    if "WrappingSpec" in data:
        out["wrapping_spec"] = data["WrappingSpec"]
    return out
