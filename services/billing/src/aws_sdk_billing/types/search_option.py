"""Generated from Smithy shape ``com.amazonaws.billing#SearchOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_billing.errors import DeserializationError

SearchOption: TypeAlias = Literal["STARTS_WITH",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("STARTS_WITH",))


def serialize_aws_json_1_0(value: SearchOption) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SearchOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SearchOption value: {data!r}")
    return cast(SearchOption, data)
