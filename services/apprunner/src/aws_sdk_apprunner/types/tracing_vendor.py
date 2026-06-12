"""Generated from Smithy shape ``com.amazonaws.apprunner#TracingVendor``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apprunner.errors import DeserializationError

TracingVendor: TypeAlias = Literal["AWSXRAY",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("AWSXRAY",))


def serialize_aws_json_1_0(value: TracingVendor) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TracingVendor:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TracingVendor value: {data!r}")
    return cast(TracingVendor, data)
