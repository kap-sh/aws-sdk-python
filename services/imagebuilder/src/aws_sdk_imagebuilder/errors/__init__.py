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
from .call_rate_limit_exceeded_exception import (
    CallRateLimitExceededException as CallRateLimitExceededException,
)
from .client_exception import ClientException as ClientException
from .dry_run_operation_exception import (
    DryRunOperationException as DryRunOperationException,
)
from .forbidden_exception import ForbiddenException as ForbiddenException
from .idempotent_parameter_mismatch_exception import (
    IdempotentParameterMismatchException as IdempotentParameterMismatchException,
)
from .invalid_pagination_token_exception import (
    InvalidPaginationTokenException as InvalidPaginationTokenException,
)
from .invalid_parameter_combination_exception import (
    InvalidParameterCombinationException as InvalidParameterCombinationException,
)
from .invalid_parameter_exception import (
    InvalidParameterException as InvalidParameterException,
)
from .invalid_parameter_value_exception import (
    InvalidParameterValueException as InvalidParameterValueException,
)
from .invalid_request_exception import (
    InvalidRequestException as InvalidRequestException,
)
from .invalid_version_number_exception import (
    InvalidVersionNumberException as InvalidVersionNumberException,
)
from .resource_already_exists_exception import (
    ResourceAlreadyExistsException as ResourceAlreadyExistsException,
)
from .resource_dependency_exception import (
    ResourceDependencyException as ResourceDependencyException,
)
from .resource_in_use_exception import ResourceInUseException as ResourceInUseException
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .service_exception import ServiceException as ServiceException
from .service_quota_exceeded_exception import (
    ServiceQuotaExceededException as ServiceQuotaExceededException,
)
from .service_unavailable_exception import (
    ServiceUnavailableException as ServiceUnavailableException,
)
from .too_many_requests_exception import (
    TooManyRequestsException as TooManyRequestsException,
)
