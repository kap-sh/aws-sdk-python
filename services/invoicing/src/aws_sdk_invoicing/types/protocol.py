"""Generated from Smithy shape ``com.amazonaws.invoicing#Protocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_invoicing.errors import DeserializationError

Protocol: TypeAlias = Literal["CXML",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("CXML",))


def serialize_aws_json_1_0(value: Protocol) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Protocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Protocol value: {data!r}")
    return cast(Protocol, data)
