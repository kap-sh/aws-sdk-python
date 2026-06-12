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
from .concurrent_modification_exception import (
    ConcurrentModificationException as ConcurrentModificationException,
)
from .conflict_exception import ConflictException as ConflictException
from .dashboard_invalid_input_error import (
    DashboardInvalidInputError as DashboardInvalidInputError,
)
from .dashboard_not_found_error import DashboardNotFoundError as DashboardNotFoundError
from .internal_service_fault import InternalServiceFault as InternalServiceFault
from .invalid_format_fault import InvalidFormatFault as InvalidFormatFault
from .invalid_next_token import InvalidNextToken as InvalidNextToken
from .invalid_parameter_combination_exception import (
    InvalidParameterCombinationException as InvalidParameterCombinationException,
)
from .invalid_parameter_value_exception import (
    InvalidParameterValueException as InvalidParameterValueException,
)
from .kms_access_denied_exception import (
    KmsAccessDeniedException as KmsAccessDeniedException,
)
from .kms_key_disabled_exception import (
    KmsKeyDisabledException as KmsKeyDisabledException,
)
from .kms_key_not_found_exception import (
    KmsKeyNotFoundException as KmsKeyNotFoundException,
)
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .limit_exceeded_fault import LimitExceededFault as LimitExceededFault
from .missing_required_parameter_exception import (
    MissingRequiredParameterException as MissingRequiredParameterException,
)
from .resource_not_found import ResourceNotFound as ResourceNotFound
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
