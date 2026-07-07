"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#RestoreKeyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.key_arn_or_key_alias_type


class RestoreKeyInput(TypedDict, closed=True):
    key_identifier: "aws_sdk_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>KeyARN</code> of the key to be restored within Amazon Web Services Payment Cryptography.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RestoreKeyInput) -> dict:
    out: dict = {}
    out["KeyIdentifier"] = value["key_identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RestoreKeyInput:
    out: RestoreKeyInput = {}  # type: ignore[typeddict-item]
    if "KeyIdentifier" in data:
        out["key_identifier"] = data["KeyIdentifier"]
    else:
        raise DeserializationError("RestoreKeyInput.key_identifier required")
    return out
