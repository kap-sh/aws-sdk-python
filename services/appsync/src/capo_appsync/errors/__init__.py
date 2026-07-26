from __future__ import annotations

from ._base import (
    AppSyncError as AppSyncError,
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
from .access_denied_exception import AccessDeniedException as AccessDeniedException
from .api_key_limit_exceeded_exception import (
    ApiKeyLimitExceededException as ApiKeyLimitExceededException,
)
from .api_key_validity_out_of_bounds_exception import (
    ApiKeyValidityOutOfBoundsException as ApiKeyValidityOutOfBoundsException,
)
from .api_limit_exceeded_exception import (
    ApiLimitExceededException as ApiLimitExceededException,
)
from .bad_request_exception import BadRequestException as BadRequestException
from .concurrent_modification_exception import (
    ConcurrentModificationException as ConcurrentModificationException,
)
from .conflict_exception import ConflictException as ConflictException
from .graph_ql_schema_exception import GraphQLSchemaException as GraphQLSchemaException
from .internal_failure_exception import (
    InternalFailureException as InternalFailureException,
)
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .not_found_exception import NotFoundException as NotFoundException
from .service_quota_exceeded_exception import (
    ServiceQuotaExceededException as ServiceQuotaExceededException,
)
from .unauthorized_exception import UnauthorizedException as UnauthorizedException
