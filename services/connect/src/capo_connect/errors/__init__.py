from __future__ import annotations

from ._base import (
    ConnectError as ConnectError,
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
from .conditional_operation_failed_exception import (
    ConditionalOperationFailedException as ConditionalOperationFailedException,
)
from .conflict_exception import ConflictException as ConflictException
from .contact_flow_not_published_exception import (
    ContactFlowNotPublishedException as ContactFlowNotPublishedException,
)
from .contact_not_found_exception import (
    ContactNotFoundException as ContactNotFoundException,
)
from .destination_not_allowed_exception import (
    DestinationNotAllowedException as DestinationNotAllowedException,
)
from .duplicate_resource_exception import (
    DuplicateResourceException as DuplicateResourceException,
)
from .idempotency_exception import IdempotencyException as IdempotencyException
from .internal_service_exception import (
    InternalServiceException as InternalServiceException,
)
from .invalid_active_region_exception import (
    InvalidActiveRegionException as InvalidActiveRegionException,
)
from .invalid_contact_flow_exception import (
    InvalidContactFlowException as InvalidContactFlowException,
)
from .invalid_contact_flow_module_exception import (
    InvalidContactFlowModuleException as InvalidContactFlowModuleException,
)
from .invalid_parameter_exception import (
    InvalidParameterException as InvalidParameterException,
)
from .invalid_request_exception import (
    InvalidRequestException as InvalidRequestException,
)
from .invalid_test_case_exception import (
    InvalidTestCaseException as InvalidTestCaseException,
)
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .maximum_result_returned_exception import (
    MaximumResultReturnedException as MaximumResultReturnedException,
)
from .outbound_contact_not_permitted_exception import (
    OutboundContactNotPermittedException as OutboundContactNotPermittedException,
)
from .output_type_not_found_exception import (
    OutputTypeNotFoundException as OutputTypeNotFoundException,
)
from .property_validation_exception import (
    PropertyValidationException as PropertyValidationException,
)
from .resource_conflict_exception import (
    ResourceConflictException as ResourceConflictException,
)
from .resource_in_use_exception import ResourceInUseException as ResourceInUseException
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .resource_not_ready_exception import (
    ResourceNotReadyException as ResourceNotReadyException,
)
from .service_quota_exceeded_exception import (
    ServiceQuotaExceededException as ServiceQuotaExceededException,
)
from .throttling_exception import ThrottlingException as ThrottlingException
from .too_many_requests_exception import (
    TooManyRequestsException as TooManyRequestsException,
)
from .user_not_found_exception import UserNotFoundException as UserNotFoundException
