"""Generated from Smithy shape ``com.amazonaws.servicequotas#OptInLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_quotas.errors import DeserializationError

OptInLevel: TypeAlias = Literal["ACCOUNT",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ACCOUNT",))


def serialize_aws_json_1_1(value: OptInLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OptInLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OptInLevel value: {data!r}")
    return cast(OptInLevel, data)
