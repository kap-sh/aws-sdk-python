"""Generated from Smithy shape ``com.amazonaws.waf#RateKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_waf.errors import DeserializationError

RateKey: TypeAlias = Literal["IP",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("IP",))


def serialize_aws_json_1_1(value: RateKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RateKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RateKey value: {data!r}")
    return cast(RateKey, data)
