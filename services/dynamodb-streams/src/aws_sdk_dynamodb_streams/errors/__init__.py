from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    DynamoDBStreamsError as DynamoDBStreamsError,
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
from .expired_iterator_exception import (
    ExpiredIteratorException as ExpiredIteratorException,
)
from .internal_server_error import InternalServerError as InternalServerError
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .trimmed_data_access_exception import (
    TrimmedDataAccessException as TrimmedDataAccessException,
)
