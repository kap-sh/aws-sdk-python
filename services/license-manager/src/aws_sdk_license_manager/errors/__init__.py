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
from .authorization_exception import AuthorizationException as AuthorizationException
from .conflict_exception import ConflictException as ConflictException
from .entitlement_not_allowed_exception import (
    EntitlementNotAllowedException as EntitlementNotAllowedException,
)
from .failed_dependency_exception import (
    FailedDependencyException as FailedDependencyException,
)
from .filter_limit_exceeded_exception import (
    FilterLimitExceededException as FilterLimitExceededException,
)
from .invalid_parameter_value_exception import (
    InvalidParameterValueException as InvalidParameterValueException,
)
from .invalid_resource_state_exception import (
    InvalidResourceStateException as InvalidResourceStateException,
)
from .license_usage_exception import LicenseUsageException as LicenseUsageException
from .no_entitlements_allowed_exception import (
    NoEntitlementsAllowedException as NoEntitlementsAllowedException,
)
from .rate_limit_exceeded_exception import (
    RateLimitExceededException as RateLimitExceededException,
)
from .redirect_exception import RedirectException as RedirectException
from .resource_limit_exceeded_exception import (
    ResourceLimitExceededException as ResourceLimitExceededException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .server_internal_exception import (
    ServerInternalException as ServerInternalException,
)
from .unsupported_digital_signature_method_exception import (
    UnsupportedDigitalSignatureMethodException as UnsupportedDigitalSignatureMethodException,
)
from .validation_exception import ValidationException as ValidationException
