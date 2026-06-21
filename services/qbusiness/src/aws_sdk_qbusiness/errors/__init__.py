from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    QBusinessError as QBusinessError,
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
from .external_resource_exception import (
    ExternalResourceException as ExternalResourceException,
)
from .internal_server_exception import (
    InternalServerException as InternalServerException,
)
from .license_not_found_exception import (
    LicenseNotFoundException as LicenseNotFoundException,
)
from .media_too_large_exception import MediaTooLargeException as MediaTooLargeException
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .service_quota_exceeded_exception import (
    ServiceQuotaExceededException as ServiceQuotaExceededException,
)
from .throttling_exception import ThrottlingException as ThrottlingException
from .validation_exception import ValidationException as ValidationException
