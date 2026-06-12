"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#DeleteAliasInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.alias_name


class DeleteAliasInput(TypedDict):
    alias_name: "aws_sdk_payment_cryptography.types.alias_name.AliasName"
    """<p>A friendly name that you can use to refer Amazon Web Services Payment Cryptography key. This value must begin with <code>alias/</code> followed by a name, such as <code>alias/ExampleAlias</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteAliasInput) -> dict:
    out: dict = {}
    out["AliasName"] = value["alias_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteAliasInput:
    out: DeleteAliasInput = {}  # type: ignore[typeddict-item]
    if "AliasName" in data:
        out["alias_name"] = data["AliasName"]
    else:
        raise DeserializationError("DeleteAliasInput.alias_name required")
    return out
