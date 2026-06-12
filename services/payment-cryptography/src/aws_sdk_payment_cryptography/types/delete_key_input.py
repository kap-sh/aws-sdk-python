"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#DeleteKeyInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.key_arn_or_key_alias_type


class DeleteKeyInput(TypedDict):
    key_identifier: "aws_sdk_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>KeyARN</code> of the key that is scheduled for deletion.</p>"""
    delete_key_in_days: NotRequired["int"]
    """<p>The waiting period for key deletion. The default value is seven days.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteKeyInput) -> dict:
    out: dict = {}
    out["KeyIdentifier"] = value["key_identifier"]
    if "delete_key_in_days" in value:
        out["DeleteKeyInDays"] = value["delete_key_in_days"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteKeyInput:
    out: DeleteKeyInput = {}  # type: ignore[typeddict-item]
    if "KeyIdentifier" in data:
        out["key_identifier"] = data["KeyIdentifier"]
    else:
        raise DeserializationError("DeleteKeyInput.key_identifier required")
    if "DeleteKeyInDays" in data:
        out["delete_key_in_days"] = data["DeleteKeyInDays"]
    return out
