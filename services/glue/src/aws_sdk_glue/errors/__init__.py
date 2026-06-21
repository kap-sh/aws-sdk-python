from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    GlueError as GlueError,
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
from .already_exists_exception import AlreadyExistsException as AlreadyExistsException
from .column_statistics_task_not_running_exception import (
    ColumnStatisticsTaskNotRunningException as ColumnStatisticsTaskNotRunningException,
)
from .column_statistics_task_running_exception import (
    ColumnStatisticsTaskRunningException as ColumnStatisticsTaskRunningException,
)
from .column_statistics_task_stopping_exception import (
    ColumnStatisticsTaskStoppingException as ColumnStatisticsTaskStoppingException,
)
from .concurrent_modification_exception import (
    ConcurrentModificationException as ConcurrentModificationException,
)
from .concurrent_runs_exceeded_exception import (
    ConcurrentRunsExceededException as ConcurrentRunsExceededException,
)
from .condition_check_failure_exception import (
    ConditionCheckFailureException as ConditionCheckFailureException,
)
from .conflict_exception import ConflictException as ConflictException
from .crawler_not_running_exception import (
    CrawlerNotRunningException as CrawlerNotRunningException,
)
from .crawler_running_exception import (
    CrawlerRunningException as CrawlerRunningException,
)
from .crawler_stopping_exception import (
    CrawlerStoppingException as CrawlerStoppingException,
)
from .entity_not_found_exception import (
    EntityNotFoundException as EntityNotFoundException,
)
from .federated_resource_already_exists_exception import (
    FederatedResourceAlreadyExistsException as FederatedResourceAlreadyExistsException,
)
from .federation_source_exception import (
    FederationSourceException as FederationSourceException,
)
from .federation_source_retryable_exception import (
    FederationSourceRetryableException as FederationSourceRetryableException,
)
from .glue_encryption_exception import (
    GlueEncryptionException as GlueEncryptionException,
)
from .idempotent_parameter_mismatch_exception import (
    IdempotentParameterMismatchException as IdempotentParameterMismatchException,
)
from .illegal_blueprint_state_exception import (
    IllegalBlueprintStateException as IllegalBlueprintStateException,
)
from .illegal_session_state_exception import (
    IllegalSessionStateException as IllegalSessionStateException,
)
from .illegal_workflow_state_exception import (
    IllegalWorkflowStateException as IllegalWorkflowStateException,
)
from .integration_conflict_operation_fault import (
    IntegrationConflictOperationFault as IntegrationConflictOperationFault,
)
from .integration_not_found_fault import (
    IntegrationNotFoundFault as IntegrationNotFoundFault,
)
from .integration_quota_exceeded_fault import (
    IntegrationQuotaExceededFault as IntegrationQuotaExceededFault,
)
from .internal_server_exception import (
    InternalServerException as InternalServerException,
)
from .internal_service_exception import (
    InternalServiceException as InternalServiceException,
)
from .invalid_input_exception import InvalidInputException as InvalidInputException
from .invalid_integration_state_fault import (
    InvalidIntegrationStateFault as InvalidIntegrationStateFault,
)
from .invalid_state_exception import InvalidStateException as InvalidStateException
from .kms_key_not_accessible_fault import (
    KMSKeyNotAccessibleFault as KMSKeyNotAccessibleFault,
)
from .materialized_view_refresh_task_not_running_exception import (
    MaterializedViewRefreshTaskNotRunningException as MaterializedViewRefreshTaskNotRunningException,
)
from .materialized_view_refresh_task_running_exception import (
    MaterializedViewRefreshTaskRunningException as MaterializedViewRefreshTaskRunningException,
)
from .materialized_view_refresh_task_stopping_exception import (
    MaterializedViewRefreshTaskStoppingException as MaterializedViewRefreshTaskStoppingException,
)
from .ml_transform_not_ready_exception import (
    MLTransformNotReadyException as MLTransformNotReadyException,
)
from .no_schedule_exception import NoScheduleException as NoScheduleException
from .operation_not_supported_exception import (
    OperationNotSupportedException as OperationNotSupportedException,
)
from .operation_timeout_exception import (
    OperationTimeoutException as OperationTimeoutException,
)
from .permission_type_mismatch_exception import (
    PermissionTypeMismatchException as PermissionTypeMismatchException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .resource_not_ready_exception import (
    ResourceNotReadyException as ResourceNotReadyException,
)
from .resource_number_limit_exceeded_exception import (
    ResourceNumberLimitExceededException as ResourceNumberLimitExceededException,
)
from .scheduler_not_running_exception import (
    SchedulerNotRunningException as SchedulerNotRunningException,
)
from .scheduler_running_exception import (
    SchedulerRunningException as SchedulerRunningException,
)
from .scheduler_transitioning_exception import (
    SchedulerTransitioningException as SchedulerTransitioningException,
)
from .session_busy_exception import SessionBusyException as SessionBusyException
from .target_resource_not_found import TargetResourceNotFound as TargetResourceNotFound
from .throttling_exception import ThrottlingException as ThrottlingException
from .validation_exception import ValidationException as ValidationException
from .version_mismatch_exception import (
    VersionMismatchException as VersionMismatchException,
)
