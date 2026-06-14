from __future__ import annotations
from ._base import (
    DeserializationError as DeserializationError,
    SerializationError as SerializationError,
    ServiceError as ServiceError,
    UnknownServiceError as UnknownServiceError,
    WaiterFailedError as WaiterFailedError,
    WaiterTimeoutError as WaiterTimeoutError,
)
from .bad_request_exception import BadRequestException as BadRequestException
from .internal_server_exception import InternalServerException as InternalServerException
from .resource_not_found_exception import ResourceNotFoundException as ResourceNotFoundException
from .throttling_exception import ThrottlingException as ThrottlingException