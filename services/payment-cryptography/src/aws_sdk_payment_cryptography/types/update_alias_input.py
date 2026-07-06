"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#UpdateAliasInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.alias_name
    import aws_sdk_payment_cryptography.types.key_arn


class UpdateAliasInput(TypedDict, closed=True):
    alias_name: "aws_sdk_payment_cryptography.types.alias_name.AliasName"
    """<p>The alias whose associated key is changing.</p>"""
    key_arn: NotRequired["aws_sdk_payment_cryptography.types.key_arn.KeyArn"]
    """<p>The <code>KeyARN</code> for the key that you are updating or removing from the alias.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateAliasInput) -> dict:
    out: dict = {}
    out["AliasName"] = value["alias_name"]
    if "key_arn" in value:
        out["KeyArn"] = value["key_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateAliasInput:
    out: UpdateAliasInput = {}  # type: ignore[typeddict-item]
    if "AliasName" in data:
        out["alias_name"] = data["AliasName"]
    else:
        raise DeserializationError("UpdateAliasInput.alias_name required")
    if "KeyArn" in data:
        out["key_arn"] = data["KeyArn"]
    return out
