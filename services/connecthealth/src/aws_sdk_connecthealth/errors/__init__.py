"""Error types raised by generated service clients."""
from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
    SerializationError as SerializationError,
    ServiceError as ServiceError,
    UnknownServiceError as UnknownServiceError,
    WaiterFailedError as WaiterFailedError,
    WaiterTimeoutError as WaiterTimeoutError,
)

__all__ = [
    "DeserializationError",
    "SerializationError",
    "ServiceError",
    "UnknownServiceError",
    "WaiterFailedError",
    "WaiterTimeoutError",
]
