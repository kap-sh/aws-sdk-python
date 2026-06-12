"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#VisaAmexDerivationOutputs``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.key_arn
    import aws_sdk_payment_cryptography_data.types.key_check_value


class VisaAmexDerivationOutputs(TypedDict):
    authorization_request_key_arn: (
        "aws_sdk_payment_cryptography_data.types.key_arn.KeyArn"
    )
    """<p>The <code>keyArn</code> of the issuer master key for cryptogram (IMK-AC) used by the operation.</p>"""
    authorization_request_key_check_value: (
        "aws_sdk_payment_cryptography_data.types.key_check_value.KeyCheckValue"
    )
    """<p>The key check value (KCV) of the issuer master key for cryptogram (IMK-AC) used by the operation.</p>"""
    current_pin_pek_arn: NotRequired[
        "aws_sdk_payment_cryptography_data.types.key_arn.KeyArn"
    ]
    """<p>The <code>keyArn</code> of the current PIN PEK.</p>"""
    current_pin_pek_key_check_value: NotRequired[
        "aws_sdk_payment_cryptography_data.types.key_check_value.KeyCheckValue"
    ]
    """<p>The key check value (KCV) of the current PIN PEK.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VisaAmexDerivationOutputs) -> dict:
    out: dict = {}
    out["AuthorizationRequestKeyArn"] = value["authorization_request_key_arn"]
    out["AuthorizationRequestKeyCheckValue"] = value[
        "authorization_request_key_check_value"
    ]
    if "current_pin_pek_arn" in value:
        out["CurrentPinPekArn"] = value["current_pin_pek_arn"]
    if "current_pin_pek_key_check_value" in value:
        out["CurrentPinPekKeyCheckValue"] = value["current_pin_pek_key_check_value"]
    return out


def deserialize_json(data: dict) -> VisaAmexDerivationOutputs:
    out: VisaAmexDerivationOutputs = {}  # type: ignore[typeddict-item]
    if "AuthorizationRequestKeyArn" in data:
        out["authorization_request_key_arn"] = data["AuthorizationRequestKeyArn"]
    else:
        raise DeserializationError(
            "VisaAmexDerivationOutputs.authorization_request_key_arn required"
        )
    if "AuthorizationRequestKeyCheckValue" in data:
        out["authorization_request_key_check_value"] = data[
            "AuthorizationRequestKeyCheckValue"
        ]
    else:
        raise DeserializationError(
            "VisaAmexDerivationOutputs.authorization_request_key_check_value required"
        )
    if "CurrentPinPekArn" in data:
        out["current_pin_pek_arn"] = data["CurrentPinPekArn"]
    if "CurrentPinPekKeyCheckValue" in data:
        out["current_pin_pek_key_check_value"] = data["CurrentPinPekKeyCheckValue"]
    return out
