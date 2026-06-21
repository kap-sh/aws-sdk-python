"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#As2805KeyVariant``."""

from typing import Literal, TypeAlias, cast

As2805KeyVariant: TypeAlias = Literal[
    "TERMINAL_MAJOR_KEY_VARIANT_00",
    "PIN_ENCRYPTION_KEY_VARIANT_28",
    "MESSAGE_AUTHENTICATION_KEY_VARIANT_24",
    "DATA_ENCRYPTION_KEY_VARIANT_22",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: As2805KeyVariant) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> As2805KeyVariant:
    return cast(As2805KeyVariant, data)
