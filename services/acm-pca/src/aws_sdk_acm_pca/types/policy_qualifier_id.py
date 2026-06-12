"""Generated from Smithy shape ``com.amazonaws.acmpca#PolicyQualifierId``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm_pca.errors import DeserializationError

PolicyQualifierId: TypeAlias = Literal["CPS",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CPS",))


def serialize_aws_json_1_1(value: PolicyQualifierId) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PolicyQualifierId:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PolicyQualifierId value: {data!r}")
    return cast(PolicyQualifierId, data)
