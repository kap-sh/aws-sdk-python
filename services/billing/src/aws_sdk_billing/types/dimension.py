"""Generated from Smithy shape ``com.amazonaws.billing#Dimension``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_billing.errors import DeserializationError

Dimension: TypeAlias = Literal["LINKED_ACCOUNT",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("LINKED_ACCOUNT",))


def serialize_aws_json_1_0(value: Dimension) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Dimension:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Dimension value: {data!r}")
    return cast(Dimension, data)
