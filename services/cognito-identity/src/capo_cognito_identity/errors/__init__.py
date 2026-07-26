from __future__ import annotations

from ._base import (
    CognitoIdentityError as CognitoIdentityError,
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
from .concurrent_modification_exception import (
    ConcurrentModificationException as ConcurrentModificationException,
)
from .developer_user_already_registered_exception import (
    DeveloperUserAlreadyRegisteredException as DeveloperUserAlreadyRegisteredException,
)
from .external_service_exception import (
    ExternalServiceException as ExternalServiceException,
)
from .internal_error_exception import InternalErrorException as InternalErrorException
from .invalid_identity_pool_configuration_exception import (
    InvalidIdentityPoolConfigurationException as InvalidIdentityPoolConfigurationException,
)
from .invalid_parameter_exception import (
    InvalidParameterException as InvalidParameterException,
)
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .not_authorized_exception import NotAuthorizedException as NotAuthorizedException
from .resource_conflict_exception import (
    ResourceConflictException as ResourceConflictException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .too_many_requests_exception import (
    TooManyRequestsException as TooManyRequestsException,
)
