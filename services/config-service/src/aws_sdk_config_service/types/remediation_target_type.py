"""Generated from Smithy shape ``com.amazonaws.configservice#RemediationTargetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

RemediationTargetType: TypeAlias = Literal["SSM_DOCUMENT",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SSM_DOCUMENT",))


def serialize_aws_json_1_1(value: RemediationTargetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RemediationTargetType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RemediationTargetType value: {data!r}")
    return cast(RemediationTargetType, data)
