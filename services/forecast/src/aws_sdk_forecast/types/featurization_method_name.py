"""Generated from Smithy shape ``com.amazonaws.forecast#FeaturizationMethodName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_forecast.errors import DeserializationError

FeaturizationMethodName: TypeAlias = Literal["filling",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("filling",))


def serialize_aws_json_1_1(value: FeaturizationMethodName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FeaturizationMethodName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FeaturizationMethodName value: {data!r}")
    return cast(FeaturizationMethodName, data)
