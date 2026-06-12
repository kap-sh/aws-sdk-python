"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsPartition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

AwsPartition: TypeAlias = Literal["aws-eusc",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("aws-eusc",))


def serialize_aws_json_1_0(value: AwsPartition) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AwsPartition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AwsPartition value: {data!r}")
    return cast(AwsPartition, data)
