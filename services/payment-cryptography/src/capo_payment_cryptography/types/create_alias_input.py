"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#CreateAliasInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography.types.alias_name
    import capo_payment_cryptography.types.key_arn


class CreateAliasInput(TypedDict, closed=True):
    alias_name: "capo_payment_cryptography.types.alias_name.AliasName"
    """<p>A friendly name that you can use to refer to a key. An alias must begin with <code>alias/</code> followed by a name, for example <code>alias/ExampleAlias</code>. It can contain only alphanumeric characters, forward slashes (/), underscores (_), and dashes (-).</p> <important> <p>Don't include personal, confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.</p> </important>"""
    key_arn: NotRequired["capo_payment_cryptography.types.key_arn.KeyArn"]
    """<p>The <code>KeyARN</code> of the key to associate with the alias.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAliasInput) -> dict:
    out: dict = {}
    out["AliasName"] = value["alias_name"]
    if "key_arn" in value:
        out["KeyArn"] = value["key_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAliasInput:
    out: CreateAliasInput = {}  # type: ignore[typeddict-item]
    if "AliasName" in data:
        out["alias_name"] = data["AliasName"]
    else:
        raise DeserializationError("CreateAliasInput.alias_name required")
    if "KeyArn" in data:
        out["key_arn"] = data["KeyArn"]
    return out
