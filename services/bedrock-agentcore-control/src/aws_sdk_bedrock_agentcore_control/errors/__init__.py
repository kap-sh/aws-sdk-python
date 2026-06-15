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
from .access_denied_exception import AccessDeniedException as AccessDeniedException
from .concurrent_modification_exception import (
    ConcurrentModificationException as ConcurrentModificationException,
)
from .conflict_exception import ConflictException as ConflictException
from .decryption_failure import DecryptionFailure as DecryptionFailure
from .encryption_failure import EncryptionFailure as EncryptionFailure
from .internal_server_exception import (
    InternalServerException as InternalServerException,
)
from .resource_limit_exceeded_exception import (
    ResourceLimitExceededException as ResourceLimitExceededException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .service_exception import ServiceException as ServiceException
from .service_quota_exceeded_exception import (
    ServiceQuotaExceededException as ServiceQuotaExceededException,
)
from .throttled_exception import ThrottledException as ThrottledException
from .throttling_exception import ThrottlingException as ThrottlingException
from .unauthorized_exception import UnauthorizedException as UnauthorizedException
from .validation_exception import ValidationException as ValidationException
