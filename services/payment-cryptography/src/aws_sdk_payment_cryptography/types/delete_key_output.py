"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#DeleteKeyOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.key


class DeleteKeyOutput(TypedDict):
    key: "aws_sdk_payment_cryptography.types.key.Key"
    """<p>The <code>KeyARN</code> of the key that is scheduled for deletion.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteKeyOutput) -> dict:
    out: dict = {}
    import aws_sdk_payment_cryptography.types.key

    out["Key"] = aws_sdk_payment_cryptography.types.key.serialize_aws_json_1_0(
        value["key"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteKeyOutput:
    out: DeleteKeyOutput = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        import aws_sdk_payment_cryptography.types.key

        out["key"] = aws_sdk_payment_cryptography.types.key.deserialize_aws_json_1_0(
            data["Key"]
        )
    else:
        raise DeserializationError("DeleteKeyOutput.key required")
    return out
