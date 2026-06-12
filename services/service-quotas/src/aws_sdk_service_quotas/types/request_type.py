"""Generated from Smithy shape ``com.amazonaws.servicequotas#RequestType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_quotas.errors import DeserializationError

RequestType: TypeAlias = Literal["AutomaticManagement",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("AutomaticManagement",))


def serialize_aws_json_1_1(value: RequestType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RequestType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RequestType value: {data!r}")
    return cast(RequestType, data)
