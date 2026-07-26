from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    Route53ResolverError as Route53ResolverError,
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
from .internal_service_error_exception import (
    InternalServiceErrorException as InternalServiceErrorException,
)
from .invalid_next_token_exception import (
    InvalidNextTokenException as InvalidNextTokenException,
)
from .invalid_parameter_exception import (
    InvalidParameterException as InvalidParameterException,
)
from .invalid_policy_document import InvalidPolicyDocument as InvalidPolicyDocument
from .invalid_request_exception import (
    InvalidRequestException as InvalidRequestException,
)
from .invalid_tag_exception import InvalidTagException as InvalidTagException
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .resource_exists_exception import (
    ResourceExistsException as ResourceExistsException,
)
from .resource_in_use_exception import ResourceInUseException as ResourceInUseException
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .resource_unavailable_exception import (
    ResourceUnavailableException as ResourceUnavailableException,
)
from .service_quota_exceeded_exception import (
    ServiceQuotaExceededException as ServiceQuotaExceededException,
)
from .throttling_exception import ThrottlingException as ThrottlingException
from .unknown_resource_exception import (
    UnknownResourceException as UnknownResourceException,
)
from .validation_exception import ValidationException as ValidationException
