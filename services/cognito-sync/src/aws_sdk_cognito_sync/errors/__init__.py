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
from .already_streamed_exception import (
    AlreadyStreamedException as AlreadyStreamedException,
)
from .concurrent_modification_exception import (
    ConcurrentModificationException as ConcurrentModificationException,
)
from .duplicate_request_exception import (
    DuplicateRequestException as DuplicateRequestException,
)
from .internal_error_exception import InternalErrorException as InternalErrorException
from .invalid_configuration_exception import (
    InvalidConfigurationException as InvalidConfigurationException,
)
from .invalid_lambda_function_output_exception import (
    InvalidLambdaFunctionOutputException as InvalidLambdaFunctionOutputException,
)
from .invalid_parameter_exception import (
    InvalidParameterException as InvalidParameterException,
)
from .lambda_throttled_exception import (
    LambdaThrottledException as LambdaThrottledException,
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
