from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    QConnectError as QConnectError,
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
from .access_denied_exception import AccessDeniedException as AccessDeniedException
from .conflict_exception import ConflictException as ConflictException
from .dependency_failed_exception import (
    DependencyFailedException as DependencyFailedException,
)
from .precondition_failed_exception import (
    PreconditionFailedException as PreconditionFailedException,
)
from .request_timeout_exception import (
    RequestTimeoutException as RequestTimeoutException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .service_quota_exceeded_exception import (
    ServiceQuotaExceededException as ServiceQuotaExceededException,
)
from .throttling_exception import ThrottlingException as ThrottlingException
from .too_many_tags_exception import TooManyTagsException as TooManyTagsException
from .unauthorized_exception import UnauthorizedException as UnauthorizedException
from .unprocessable_content_exception import (
    UnprocessableContentException as UnprocessableContentException,
)
from .validation_exception import ValidationException as ValidationException
