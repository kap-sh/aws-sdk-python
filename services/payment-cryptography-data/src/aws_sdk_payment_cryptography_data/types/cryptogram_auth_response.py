"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#CryptogramAuthResponse``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.cryptogram_verification_arpc_method1
    import aws_sdk_payment_cryptography_data.types.cryptogram_verification_arpc_method2


class _CryptogramAuthResponse_ArpcMethod1(TypedDict, closed=True):
    ArpcMethod1: "aws_sdk_payment_cryptography_data.types.cryptogram_verification_arpc_method1.CryptogramVerificationArpcMethod1"


class _CryptogramAuthResponse_ArpcMethod2(TypedDict, closed=True):
    ArpcMethod2: "aws_sdk_payment_cryptography_data.types.cryptogram_verification_arpc_method2.CryptogramVerificationArpcMethod2"


CryptogramAuthResponse: TypeAlias = (
    _CryptogramAuthResponse_ArpcMethod1 | _CryptogramAuthResponse_ArpcMethod2
)


# --- restJson1 ser/de ---
def serialize_json(value: CryptogramAuthResponse) -> dict:
    if "ArpcMethod1" in value:
        import aws_sdk_payment_cryptography_data.types.cryptogram_verification_arpc_method1

        return {
            "ArpcMethod1": aws_sdk_payment_cryptography_data.types.cryptogram_verification_arpc_method1.serialize_json(
                value["ArpcMethod1"]
            )
        }
    elif "ArpcMethod2" in value:
        import aws_sdk_payment_cryptography_data.types.cryptogram_verification_arpc_method2

        return {
            "ArpcMethod2": aws_sdk_payment_cryptography_data.types.cryptogram_verification_arpc_method2.serialize_json(
                value["ArpcMethod2"]
            )
        }
    else:
        raise SerializationError("CryptogramAuthResponse: no variant present")


def deserialize_json(data: dict) -> CryptogramAuthResponse:
    if "ArpcMethod1" in data:
        import aws_sdk_payment_cryptography_data.types.cryptogram_verification_arpc_method1

        return {
            "ArpcMethod1": aws_sdk_payment_cryptography_data.types.cryptogram_verification_arpc_method1.deserialize_json(
                data["ArpcMethod1"]
            )
        }
    elif "ArpcMethod2" in data:
        import aws_sdk_payment_cryptography_data.types.cryptogram_verification_arpc_method2

        return {
            "ArpcMethod2": aws_sdk_payment_cryptography_data.types.cryptogram_verification_arpc_method2.deserialize_json(
                data["ArpcMethod2"]
            )
        }
    else:
        raise DeserializationError("CryptogramAuthResponse: no recognized variant key")
