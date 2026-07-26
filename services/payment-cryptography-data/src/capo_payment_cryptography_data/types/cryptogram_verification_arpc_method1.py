"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#CryptogramVerificationArpcMethod1``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.hex_length_equals4


class CryptogramVerificationArpcMethod1(TypedDict, closed=True):
    auth_response_code: (
        "capo_payment_cryptography_data.types.hex_length_equals4.HexLengthEquals4"
    )
    """<p>The auth code used to calculate APRC after ARQC verification is successful. This is the same auth code used for ARQC generation outside of Amazon Web Services Payment Cryptography.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CryptogramVerificationArpcMethod1) -> dict:
    out: dict = {}
    out["AuthResponseCode"] = value["auth_response_code"]
    return out


def deserialize_json(data: dict) -> CryptogramVerificationArpcMethod1:
    out: CryptogramVerificationArpcMethod1 = {}  # type: ignore[typeddict-item]
    if "AuthResponseCode" in data:
        out["auth_response_code"] = data["AuthResponseCode"]
    else:
        raise DeserializationError(
            "CryptogramVerificationArpcMethod1.auth_response_code required"
        )
    return out
