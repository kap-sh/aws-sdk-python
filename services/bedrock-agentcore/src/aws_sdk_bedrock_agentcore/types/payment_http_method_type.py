"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentHttpMethodType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

PaymentHttpMethodType: TypeAlias = Literal[
    "GET",
    "POST",
    "PUT",
    "DELETE",
    "PATCH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GET",
        "POST",
        "PUT",
        "DELETE",
        "PATCH",
    )
)


def serialize_json(value: PaymentHttpMethodType) -> str:
    return value


def deserialize_json(data: str) -> PaymentHttpMethodType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PaymentHttpMethodType value: {data!r}")
    return cast(PaymentHttpMethodType, data)
