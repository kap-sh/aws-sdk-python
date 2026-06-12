"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#GetAliasInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.alias_name


class GetAliasInput(TypedDict):
    alias_name: "aws_sdk_payment_cryptography.types.alias_name.AliasName"
    """<p>The alias of the Amazon Web Services Payment Cryptography key.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAliasInput) -> dict:
    out: dict = {}
    out["AliasName"] = value["alias_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAliasInput:
    out: GetAliasInput = {}  # type: ignore[typeddict-item]
    if "AliasName" in data:
        out["alias_name"] = data["AliasName"]
    else:
        raise DeserializationError("GetAliasInput.alias_name required")
    return out
