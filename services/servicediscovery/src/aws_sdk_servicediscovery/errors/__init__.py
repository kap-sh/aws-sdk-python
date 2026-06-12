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
from .custom_health_not_found import CustomHealthNotFound as CustomHealthNotFound
from .duplicate_request import DuplicateRequest as DuplicateRequest
from .instance_not_found import InstanceNotFound as InstanceNotFound
from .invalid_input import InvalidInput as InvalidInput
from .namespace_already_exists import NamespaceAlreadyExists as NamespaceAlreadyExists
from .namespace_not_found import NamespaceNotFound as NamespaceNotFound
from .operation_not_found import OperationNotFound as OperationNotFound
from .request_limit_exceeded import RequestLimitExceeded as RequestLimitExceeded
from .resource_in_use import ResourceInUse as ResourceInUse
from .resource_limit_exceeded import ResourceLimitExceeded as ResourceLimitExceeded
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .service_already_exists import ServiceAlreadyExists as ServiceAlreadyExists
from .service_attributes_limit_exceeded_exception import (
    ServiceAttributesLimitExceededException as ServiceAttributesLimitExceededException,
)
from .service_not_found import ServiceNotFound as ServiceNotFound
from .too_many_tags_exception import TooManyTagsException as TooManyTagsException
