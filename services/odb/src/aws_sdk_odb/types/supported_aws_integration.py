"""Generated from Smithy shape ``com.amazonaws.odb#SupportedAwsIntegration``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

SupportedAwsIntegration: TypeAlias = Literal["KmsTde",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("KmsTde",))


def serialize_aws_json_1_0(value: SupportedAwsIntegration) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SupportedAwsIntegration:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SupportedAwsIntegration value: {data!r}")
    return cast(SupportedAwsIntegration, data)
