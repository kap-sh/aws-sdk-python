from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    IoTError as IoTError,
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
from .certificate_conflict_exception import (
    CertificateConflictException as CertificateConflictException,
)
from .certificate_state_exception import (
    CertificateStateException as CertificateStateException,
)
from .certificate_validation_exception import (
    CertificateValidationException as CertificateValidationException,
)
from .conflict_exception import ConflictException as ConflictException
from .conflicting_resource_update_exception import (
    ConflictingResourceUpdateException as ConflictingResourceUpdateException,
)
from .delete_conflict_exception import (
    DeleteConflictException as DeleteConflictException,
)
from .index_not_ready_exception import IndexNotReadyException as IndexNotReadyException
from .internal_exception import InternalException as InternalException
from .internal_failure_exception import (
    InternalFailureException as InternalFailureException,
)
from .internal_server_exception import (
    InternalServerException as InternalServerException,
)
from .invalid_aggregation_exception import (
    InvalidAggregationException as InvalidAggregationException,
)
from .invalid_query_exception import InvalidQueryException as InvalidQueryException
from .invalid_request_exception import (
    InvalidRequestException as InvalidRequestException,
)
from .invalid_response_exception import (
    InvalidResponseException as InvalidResponseException,
)
from .invalid_state_transition_exception import (
    InvalidStateTransitionException as InvalidStateTransitionException,
)
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .malformed_policy_exception import (
    MalformedPolicyException as MalformedPolicyException,
)
from .not_configured_exception import NotConfiguredException as NotConfiguredException
from .registration_code_validation_exception import (
    RegistrationCodeValidationException as RegistrationCodeValidationException,
)
from .resource_already_exists_exception import (
    ResourceAlreadyExistsException as ResourceAlreadyExistsException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .resource_registration_failure_exception import (
    ResourceRegistrationFailureException as ResourceRegistrationFailureException,
)
from .service_quota_exceeded_exception import (
    ServiceQuotaExceededException as ServiceQuotaExceededException,
)
from .service_unavailable_exception import (
    ServiceUnavailableException as ServiceUnavailableException,
)
from .sql_parse_exception import SqlParseException as SqlParseException
from .task_already_exists_exception import (
    TaskAlreadyExistsException as TaskAlreadyExistsException,
)
from .throttling_exception import ThrottlingException as ThrottlingException
from .transfer_already_completed_exception import (
    TransferAlreadyCompletedException as TransferAlreadyCompletedException,
)
from .transfer_conflict_exception import (
    TransferConflictException as TransferConflictException,
)
from .unauthorized_exception import UnauthorizedException as UnauthorizedException
from .validation_exception import ValidationException as ValidationException
from .version_conflict_exception import (
    VersionConflictException as VersionConflictException,
)
from .versions_limit_exceeded_exception import (
    VersionsLimitExceededException as VersionsLimitExceededException,
)
