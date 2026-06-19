"""Error types raised by generated service clients."""

from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    SerializationError as SerializationError,
)
from ._base import (
    ServiceError as ServiceError,
)
from ._base import (
    UnknownServiceError as UnknownServiceError,
)
from ._base import (
    WaiterFailedError as WaiterFailedError,
)
from ._base import (
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
