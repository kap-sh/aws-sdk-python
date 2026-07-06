"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#TranslateKeyMaterialOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.wrapped_working_key


class TranslateKeyMaterialOutput(TypedDict, closed=True):
    wrapped_key: (
        "aws_sdk_payment_cryptography_data.types.wrapped_working_key.WrappedWorkingKey"
    )
    """<p>The outgoing KEK wrapped TR31WrappedKeyBlock.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TranslateKeyMaterialOutput) -> dict:
    out: dict = {}
    import aws_sdk_payment_cryptography_data.types.wrapped_working_key

    out["WrappedKey"] = (
        aws_sdk_payment_cryptography_data.types.wrapped_working_key.serialize_json(
            value["wrapped_key"]
        )
    )
    return out


def deserialize_json(data: dict) -> TranslateKeyMaterialOutput:
    out: TranslateKeyMaterialOutput = {}  # type: ignore[typeddict-item]
    if "WrappedKey" in data:
        import aws_sdk_payment_cryptography_data.types.wrapped_working_key

        out["wrapped_key"] = (
            aws_sdk_payment_cryptography_data.types.wrapped_working_key.deserialize_json(
                data["WrappedKey"]
            )
        )
    else:
        raise DeserializationError("TranslateKeyMaterialOutput.wrapped_key required")
    return out
