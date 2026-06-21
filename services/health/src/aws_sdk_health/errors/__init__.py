from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    HealthError as HealthError,
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
from .concurrent_modification_exception import (
    ConcurrentModificationException as ConcurrentModificationException,
)
from .invalid_pagination_token import InvalidPaginationToken as InvalidPaginationToken
from .unsupported_locale import UnsupportedLocale as UnsupportedLocale
