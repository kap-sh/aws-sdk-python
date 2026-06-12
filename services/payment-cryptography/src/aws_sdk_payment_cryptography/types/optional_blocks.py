"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#OptionalBlocks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.optional_block_id
    import aws_sdk_payment_cryptography.types.optional_block_value

OptionalBlocks: TypeAlias = dict[
    "aws_sdk_payment_cryptography.types.optional_block_id.OptionalBlockId",
    "aws_sdk_payment_cryptography.types.optional_block_value.OptionalBlockValue",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: OptionalBlocks) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> OptionalBlocks:
    out: OptionalBlocks = {}
    for key, value in data.items():
        out[key] = value
    return out
