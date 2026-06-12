"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#AbortCriteriaAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

AbortCriteriaAction: TypeAlias = Literal["CANCEL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CANCEL",))


def serialize_json(value: AbortCriteriaAction) -> str:
    return value


def deserialize_json(data: str) -> AbortCriteriaAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AbortCriteriaAction value: {data!r}")
    return cast(AbortCriteriaAction, data)
