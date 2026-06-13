"""Generated from Smithy shape ``com.amazonaws.odb#OciAwsIntegration``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

OciAwsIntegration: TypeAlias = Literal["KmsTde",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("KmsTde",))


def serialize_aws_json_1_0(value: OciAwsIntegration) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OciAwsIntegration:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OciAwsIntegration value: {data!r}")
    return cast(OciAwsIntegration, data)
