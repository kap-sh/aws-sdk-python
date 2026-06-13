"""Generated from Smithy shape ``com.amazonaws.invoicing#BuyerDomain``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_invoicing.errors import DeserializationError

BuyerDomain: TypeAlias = Literal["NetworkID",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("NetworkID",))


def serialize_aws_json_1_0(value: BuyerDomain) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BuyerDomain:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BuyerDomain value: {data!r}")
    return cast(BuyerDomain, data)
