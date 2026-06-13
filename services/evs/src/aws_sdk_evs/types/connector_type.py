"""Generated from Smithy shape ``com.amazonaws.evs#ConnectorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_evs.errors import DeserializationError

ConnectorType: TypeAlias = Literal["VCENTER",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("VCENTER",))


def serialize_aws_json_1_0(value: ConnectorType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ConnectorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectorType value: {data!r}")
    return cast(ConnectorType, data)
