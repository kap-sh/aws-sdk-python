"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DeliveryDestinationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

DeliveryDestinationType: TypeAlias = Literal["KINESIS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("KINESIS",))


def serialize_json(value: DeliveryDestinationType) -> str:
    return value


def deserialize_json(data: str) -> DeliveryDestinationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeliveryDestinationType value: {data!r}")
    return cast(DeliveryDestinationType, data)
