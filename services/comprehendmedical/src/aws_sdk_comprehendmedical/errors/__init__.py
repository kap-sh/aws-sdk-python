from __future__ import annotations

from ._base import (
    ComprehendMedicalError as ComprehendMedicalError,
)
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
from .internal_server_exception import (
    InternalServerException as InternalServerException,
)
from .invalid_encoding_exception import (
    InvalidEncodingException as InvalidEncodingException,
)
from .invalid_request_exception import (
    InvalidRequestException as InvalidRequestException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .service_unavailable_exception import (
    ServiceUnavailableException as ServiceUnavailableException,
)
from .text_size_limit_exceeded_exception import (
    TextSizeLimitExceededException as TextSizeLimitExceededException,
)
from .too_many_requests_exception import (
    TooManyRequestsException as TooManyRequestsException,
)
from .validation_exception import ValidationException as ValidationException
