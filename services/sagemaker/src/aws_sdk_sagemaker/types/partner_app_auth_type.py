"""Generated from Smithy shape ``com.amazonaws.sagemaker#PartnerAppAuthType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

PartnerAppAuthType: TypeAlias = Literal["IAM",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("IAM",))


def serialize_aws_json_1_1(value: PartnerAppAuthType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PartnerAppAuthType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PartnerAppAuthType value: {data!r}")
    return cast(PartnerAppAuthType, data)
