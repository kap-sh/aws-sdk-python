"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#VerifyAuthRequestCryptogramInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.auth_request_cryptogram_type
    import aws_sdk_payment_cryptography_data.types.cryptogram_auth_response
    import aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type
    import aws_sdk_payment_cryptography_data.types.major_key_derivation_mode
    import aws_sdk_payment_cryptography_data.types.session_key_derivation
    import aws_sdk_payment_cryptography_data.types.transaction_data_type


class VerifyAuthRequestCryptogramInput(TypedDict):
    key_identifier: "aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the major encryption key that Amazon Web Services Payment Cryptography uses for ARQC verification.</p>"""
    transaction_data: "aws_sdk_payment_cryptography_data.types.transaction_data_type.TransactionDataType"
    """<p>The transaction data that Amazon Web Services Payment Cryptography uses for ARQC verification. The same transaction is used for ARQC generation outside of Amazon Web Services Payment Cryptography.</p>"""
    auth_request_cryptogram: "aws_sdk_payment_cryptography_data.types.auth_request_cryptogram_type.AuthRequestCryptogramType"
    """<p>The auth request cryptogram imported into Amazon Web Services Payment Cryptography for ARQC verification using a major encryption key and transaction data.</p>"""
    major_key_derivation_mode: "aws_sdk_payment_cryptography_data.types.major_key_derivation_mode.MajorKeyDerivationMode"
    """<p>The method to use when deriving the major encryption key for ARQC verification within Amazon Web Services Payment Cryptography. The same key derivation mode was used for ARQC generation outside of Amazon Web Services Payment Cryptography.</p>"""
    session_key_derivation_attributes: "aws_sdk_payment_cryptography_data.types.session_key_derivation.SessionKeyDerivation"
    """<p>The attributes and values to use for deriving a session key for ARQC verification within Amazon Web Services Payment Cryptography. The same attributes were used for ARQC generation outside of Amazon Web Services Payment Cryptography.</p>"""
    auth_response_attributes: NotRequired[
        "aws_sdk_payment_cryptography_data.types.cryptogram_auth_response.CryptogramAuthResponse"
    ]
    """<p>The attributes and values for auth request cryptogram verification. These parameters are required in case using ARPC Method 1 or Method 2 for ARQC verification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VerifyAuthRequestCryptogramInput) -> dict:
    out: dict = {}
    out["KeyIdentifier"] = value["key_identifier"]
    out["TransactionData"] = value["transaction_data"]
    out["AuthRequestCryptogram"] = value["auth_request_cryptogram"]
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
    if "auth_response_attributes" in value:
        import aws_sdk_payment_cryptography_data.types.cryptogram_auth_response

        out["AuthResponseAttributes"] = (
            aws_sdk_payment_cryptography_data.types.cryptogram_auth_response.serialize_json(
                value["auth_response_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> VerifyAuthRequestCryptogramInput:
    out: VerifyAuthRequestCryptogramInput = {}  # type: ignore[typeddict-item]
    if "KeyIdentifier" in data:
        out["key_identifier"] = data["KeyIdentifier"]
    else:
        raise DeserializationError(
            "VerifyAuthRequestCryptogramInput.key_identifier required"
        )
    if "TransactionData" in data:
        out["transaction_data"] = data["TransactionData"]
    else:
        raise DeserializationError(
            "VerifyAuthRequestCryptogramInput.transaction_data required"
        )
    if "AuthRequestCryptogram" in data:
        out["auth_request_cryptogram"] = data["AuthRequestCryptogram"]
    else:
        raise DeserializationError(
            "VerifyAuthRequestCryptogramInput.auth_request_cryptogram required"
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
            "VerifyAuthRequestCryptogramInput.major_key_derivation_mode required"
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
            "VerifyAuthRequestCryptogramInput.session_key_derivation_attributes required"
        )
    if "AuthResponseAttributes" in data:
        import aws_sdk_payment_cryptography_data.types.cryptogram_auth_response

        out["auth_response_attributes"] = (
            aws_sdk_payment_cryptography_data.types.cryptogram_auth_response.deserialize_json(
                data["AuthResponseAttributes"]
            )
        )
    return out
