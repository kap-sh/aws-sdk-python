"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DeliveryDestinationType``."""

from typing import Literal, TypeAlias, cast

DeliveryDestinationType: TypeAlias = Literal["KINESIS",]


# --- restJson1 ser/de ---
def serialize_json(value: DeliveryDestinationType) -> str:
    return value


def deserialize_json(data: str) -> DeliveryDestinationType:
    return cast(DeliveryDestinationType, data)
