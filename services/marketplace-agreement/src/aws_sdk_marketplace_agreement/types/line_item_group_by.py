"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#LineItemGroupBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_agreement.errors import DeserializationError

LineItemGroupBy: TypeAlias = Literal["INVOICE_ID",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("INVOICE_ID",))


def serialize_aws_json_1_0(value: LineItemGroupBy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LineItemGroupBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LineItemGroupBy value: {data!r}")
    return cast(LineItemGroupBy, data)
