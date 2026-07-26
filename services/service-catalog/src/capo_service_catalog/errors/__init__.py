from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    SerializationError as SerializationError,
)
from ._base import (
    ServiceCatalogError as ServiceCatalogError,
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
from .duplicate_resource_exception import (
    DuplicateResourceException as DuplicateResourceException,
)
from .invalid_parameters_exception import (
    InvalidParametersException as InvalidParametersException,
)
from .invalid_state_exception import InvalidStateException as InvalidStateException
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .operation_not_supported_exception import (
    OperationNotSupportedException as OperationNotSupportedException,
)
from .resource_in_use_exception import ResourceInUseException as ResourceInUseException
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .tag_option_not_migrated_exception import (
    TagOptionNotMigratedException as TagOptionNotMigratedException,
)
