from __future__ import annotations
from ._base import (
    DeserializationError as DeserializationError,
    SerializationError as SerializationError,
    ServiceError as ServiceError,
    UnknownServiceError as UnknownServiceError,
    WaiterFailedError as WaiterFailedError,
    WaiterTimeoutError as WaiterTimeoutError,
)
from .access_denied_exception import AccessDeniedException as AccessDeniedException
from .duplicate_resource_exception import DuplicateResourceException as DuplicateResourceException
from .internal_service_error import InternalServiceError as InternalServiceError
from .invalid_request_exception import InvalidRequestException as InvalidRequestException
from .resource_not_found_exception import ResourceNotFoundException as ResourceNotFoundException
from .resource_quota_exceeded_exception import ResourceQuotaExceededException as ResourceQuotaExceededException
from .throttling_exception import ThrottlingException as ThrottlingException
from .unsupported_operation_exception import UnsupportedOperationException as UnsupportedOperationException