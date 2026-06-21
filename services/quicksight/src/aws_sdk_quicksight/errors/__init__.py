from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    QuickSightError as QuickSightError,
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
from .concurrent_updating_exception import (
    ConcurrentUpdatingException as ConcurrentUpdatingException,
)
from .conflict_exception import ConflictException as ConflictException
from .customer_managed_key_unavailable_exception import (
    CustomerManagedKeyUnavailableException as CustomerManagedKeyUnavailableException,
)
from .domain_not_whitelisted_exception import (
    DomainNotWhitelistedException as DomainNotWhitelistedException,
)
from .identity_type_not_supported_exception import (
    IdentityTypeNotSupportedException as IdentityTypeNotSupportedException,
)
from .internal_failure_exception import (
    InternalFailureException as InternalFailureException,
)
from .internal_server_exception import (
    InternalServerException as InternalServerException,
)
from .invalid_data_set_parameter_value_exception import (
    InvalidDataSetParameterValueException as InvalidDataSetParameterValueException,
)
from .invalid_next_token_exception import (
    InvalidNextTokenException as InvalidNextTokenException,
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
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .precondition_not_met_exception import (
    PreconditionNotMetException as PreconditionNotMetException,
)
from .quick_sight_user_not_found_exception import (
    QuickSightUserNotFoundException as QuickSightUserNotFoundException,
)
from .resource_exists_exception import (
    ResourceExistsException as ResourceExistsException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .resource_unavailable_exception import (
    ResourceUnavailableException as ResourceUnavailableException,
)
from .session_lifetime_in_minutes_invalid_exception import (
    SessionLifetimeInMinutesInvalidException as SessionLifetimeInMinutesInvalidException,
)
from .throttling_exception import ThrottlingException as ThrottlingException
from .unsupported_pricing_plan_exception import (
    UnsupportedPricingPlanException as UnsupportedPricingPlanException,
)
from .unsupported_user_edition_exception import (
    UnsupportedUserEditionException as UnsupportedUserEditionException,
)
