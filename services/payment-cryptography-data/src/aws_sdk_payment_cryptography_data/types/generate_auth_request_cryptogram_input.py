"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#GenerateAuthRequestCryptogramInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type
    import aws_sdk_payment_cryptography_data.types.major_key_derivation_mode
    import aws_sdk_payment_cryptography_data.types.session_key_derivation
    import aws_sdk_payment_cryptography_data.types.transaction_data_type


class GenerateAuthRequestCryptogramInput(TypedDict):
    key_identifier: "aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the IMK-AC (TR31_E0_EMV_MKEY_APP_CRYPTOGRAMS) that Amazon Web Services Payment Cryptography uses to generate the ARQC.</p>"""
    transaction_data: "aws_sdk_payment_cryptography_data.types.transaction_data_type.TransactionDataType"
    """<p>The transaction data that Amazon Web Services Payment Cryptography uses for ARQC generation. The same transaction data is used for ARQC verification by the issuer using <a>VerifyAuthRequestCryptogram</a>.</p>"""
    major_key_derivation_mode: "aws_sdk_payment_cryptography_data.types.major_key_derivation_mode.MajorKeyDerivationMode"
    """<p>The method to use when deriving the major encryption key for ARQC generation within Amazon Web Services Payment Cryptography.</p>"""
    session_key_derivation_attributes: "aws_sdk_payment_cryptography_data.types.session_key_derivation.SessionKeyDerivation"
    """<p>The attributes and values to use for deriving a session key for ARQC generation within Amazon Web Services Payment Cryptography.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateAuthRequestCryptogramInput) -> dict:
    out: dict = {}
    out["KeyIdentifier"] = value["key_identifier"]
    out["TransactionData"] = value["transaction_data"]
    import aws_sdk_payment_cryptography_data.types.major_key_derivation_mode

    out["MajorKeyDerivationMode"] = (
        aws_sdk_payment_cryptography_data.types.major_key_derivation_mode.serialize_json(
            value["major_key_derivation_mode"]
        )
    )
    import aws_sdk_payment_cryptography_data.types.session_key_derivation

    out["SessionKeyDerivationAttributes"] = (
        aws_sdk_payment_cryptography_data.types.session_key_derivation.serialize_json(
            value["session_key_derivation_attributes"]
        )
    )
    return out


def deserialize_json(data: dict) -> GenerateAuthRequestCryptogramInput:
    out: GenerateAuthRequestCryptogramInput = {}  # type: ignore[typeddict-item]
    if "KeyIdentifier" in data:
        out["key_identifier"] = data["KeyIdentifier"]
    else:
        raise DeserializationError(
            "GenerateAuthRequestCryptogramInput.key_identifier required"
        )
    if "TransactionData" in data:
        out["transaction_data"] = data["TransactionData"]
    else:
        raise DeserializationError(
            "GenerateAuthRequestCryptogramInput.transaction_data required"
        )
    if "MajorKeyDerivationMode" in data:
        import aws_sdk_payment_cryptography_data.types.major_key_derivation_mode

        out["major_key_derivation_mode"] = (
            aws_sdk_payment_cryptography_data.types.major_key_derivation_mode.deserialize_json(
                data["MajorKeyDerivationMode"]
            )
        )
    else:
        raise DeserializationError(
            "GenerateAuthRequestCryptogramInput.major_key_derivation_mode required"
        )
    if "SessionKeyDerivationAttributes" in data:
        import aws_sdk_payment_cryptography_data.types.session_key_derivation

        out["session_key_derivation_attributes"] = (
            aws_sdk_payment_cryptography_data.types.session_key_derivation.deserialize_json(
                data["SessionKeyDerivationAttributes"]
            )
        )
    else:
        raise DeserializationError(
            "GenerateAuthRequestCryptogramInput.session_key_derivation_attributes required"
        )
    return out
