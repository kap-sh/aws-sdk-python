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
from .conflict_exception import ConflictException as ConflictException
from .forbidden_exception import ForbiddenException as ForbiddenException
from .gateway_timeout_exception import (
    GatewayTimeoutException as GatewayTimeoutException,
)
from .internal_failure_exception import (
    InternalFailureException as InternalFailureException,
)
from .invalid_request_exception import (
    InvalidRequestException as InvalidRequestException,
)
from .method_not_allowed_exception import (
    MethodNotAllowedException as MethodNotAllowedException,
)
from .request_entity_too_large_exception import (
    RequestEntityTooLargeException as RequestEntityTooLargeException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .service_unavailable_exception import (
    ServiceUnavailableException as ServiceUnavailableException,
)
from .throttling_exception import ThrottlingException as ThrottlingException
from .unauthorized_exception import UnauthorizedException as UnauthorizedException
from .unsupported_document_encoding_exception import (
    UnsupportedDocumentEncodingException as UnsupportedDocumentEncodingException,
)
