"""Generated from Smithy shape ``com.amazonaws.customerprofiles#WorkflowType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

WorkflowType: TypeAlias = Literal["APPFLOW_INTEGRATION",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("APPFLOW_INTEGRATION",))


def serialize_json(value: WorkflowType) -> str:
    return value


def deserialize_json(data: str) -> WorkflowType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkflowType value: {data!r}")
    return cast(WorkflowType, data)
