"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ExportKeyOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.wrapped_key


class ExportKeyOutput(TypedDict):
    wrapped_key: NotRequired[
        "aws_sdk_payment_cryptography.types.wrapped_key.WrappedKey"
    ]
    """<p>The key material under export as a TR-34 WrappedKeyBlock or a TR-31 WrappedKeyBlock. or a RSA WrappedKeyCryptogram.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportKeyOutput) -> dict:
    out: dict = {}
    if "wrapped_key" in value:
        import aws_sdk_payment_cryptography.types.wrapped_key

        out["WrappedKey"] = (
            aws_sdk_payment_cryptography.types.wrapped_key.serialize_aws_json_1_0(
                value["wrapped_key"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExportKeyOutput:
    out: ExportKeyOutput = {}  # type: ignore[typeddict-item]
    if "WrappedKey" in data:
        import aws_sdk_payment_cryptography.types.wrapped_key

        out["wrapped_key"] = (
            aws_sdk_payment_cryptography.types.wrapped_key.deserialize_aws_json_1_0(
                data["WrappedKey"]
            )
        )
    return out
