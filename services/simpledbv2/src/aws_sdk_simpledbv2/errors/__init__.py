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
    SimpleDBv2Error as SimpleDBv2Error,
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
from .conflict_exception import ConflictException as ConflictException
from .invalid_next_token_exception import (
    InvalidNextTokenException as InvalidNextTokenException,
)
from .invalid_parameter_combination_exception import (
    InvalidParameterCombinationException as InvalidParameterCombinationException,
)
from .invalid_parameter_value_exception import (
    InvalidParameterValueException as InvalidParameterValueException,
)
from .no_such_domain_exception import NoSuchDomainException as NoSuchDomainException
from .no_such_export_exception import NoSuchExportException as NoSuchExportException
from .number_exports_limit_exceeded import (
    NumberExportsLimitExceeded as NumberExportsLimitExceeded,
)
