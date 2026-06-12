"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#StartKeyUsageInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.key_arn_or_key_alias_type


class StartKeyUsageInput(TypedDict):
    key_identifier: "aws_sdk_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>KeyArn</code> of the key.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartKeyUsageInput) -> dict:
    out: dict = {}
    out["KeyIdentifier"] = value["key_identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartKeyUsageInput:
    out: StartKeyUsageInput = {}  # type: ignore[typeddict-item]
    if "KeyIdentifier" in data:
        out["key_identifier"] = data["KeyIdentifier"]
    else:
        raise DeserializationError("StartKeyUsageInput.key_identifier required")
    return out
