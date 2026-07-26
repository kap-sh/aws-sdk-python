"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#Aliases``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_payment_cryptography.types.alias

Aliases: TypeAlias = list["capo_payment_cryptography.types.alias.Alias"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Aliases) -> list:
    import capo_payment_cryptography.types.alias

    out: list = []
    for item in value:
        out.append(capo_payment_cryptography.types.alias.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Aliases:
    import capo_payment_cryptography.types.alias

    out: Aliases = []
    for item in data:
        out.append(capo_payment_cryptography.types.alias.deserialize_aws_json_1_0(item))
    return out
