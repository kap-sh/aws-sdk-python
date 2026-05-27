from __future__ import annotations
from ._base import (
    DeserializationError as DeserializationError,
    SerializationError as SerializationError,
    ServiceError as ServiceError,
    UnknownServiceError as UnknownServiceError,
    WaiterFailedError as WaiterFailedError,
    WaiterTimeoutError as WaiterTimeoutError,
)
from .backup_in_use_exception import BackupInUseException as BackupInUseException
from .backup_not_found_exception import (
    BackupNotFoundException as BackupNotFoundException,
)
from .conditional_check_failed_exception import (
    ConditionalCheckFailedException as ConditionalCheckFailedException,
)
from .continuous_backups_unavailable_exception import (
    ContinuousBackupsUnavailableException as ContinuousBackupsUnavailableException,
)
from .duplicate_item_exception import DuplicateItemException as DuplicateItemException
from .export_conflict_exception import (
    ExportConflictException as ExportConflictException,
)
from .export_not_found_exception import (
    ExportNotFoundException as ExportNotFoundException,
)
from .global_table_already_exists_exception import (
    GlobalTableAlreadyExistsException as GlobalTableAlreadyExistsException,
)
from .global_table_not_found_exception import (
    GlobalTableNotFoundException as GlobalTableNotFoundException,
)
from .idempotent_parameter_mismatch_exception import (
    IdempotentParameterMismatchException as IdempotentParameterMismatchException,
)
from .import_conflict_exception import (
    ImportConflictException as ImportConflictException,
)
from .import_not_found_exception import (
    ImportNotFoundException as ImportNotFoundException,
)
from .index_not_found_exception import IndexNotFoundException as IndexNotFoundException
from .internal_server_error import InternalServerError as InternalServerError
from .invalid_endpoint_exception import (
    InvalidEndpointException as InvalidEndpointException,
)
from .invalid_export_time_exception import (
    InvalidExportTimeException as InvalidExportTimeException,
)
from .invalid_restore_time_exception import (
    InvalidRestoreTimeException as InvalidRestoreTimeException,
)
from .item_collection_size_limit_exceeded_exception import (
    ItemCollectionSizeLimitExceededException as ItemCollectionSizeLimitExceededException,
)
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .point_in_time_recovery_unavailable_exception import (
    PointInTimeRecoveryUnavailableException as PointInTimeRecoveryUnavailableException,
)
from .policy_not_found_exception import (
    PolicyNotFoundException as PolicyNotFoundException,
)
from .provisioned_throughput_exceeded_exception import (
    ProvisionedThroughputExceededException as ProvisionedThroughputExceededException,
)
from .replica_already_exists_exception import (
    ReplicaAlreadyExistsException as ReplicaAlreadyExistsException,
)
from .replica_not_found_exception import (
    ReplicaNotFoundException as ReplicaNotFoundException,
)
from .replicated_write_conflict_exception import (
    ReplicatedWriteConflictException as ReplicatedWriteConflictException,
)
from .request_limit_exceeded import RequestLimitExceeded as RequestLimitExceeded
from .resource_in_use_exception import ResourceInUseException as ResourceInUseException
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .table_already_exists_exception import (
    TableAlreadyExistsException as TableAlreadyExistsException,
)
from .table_in_use_exception import TableInUseException as TableInUseException
from .table_not_found_exception import TableNotFoundException as TableNotFoundException
from .throttling_exception import ThrottlingException as ThrottlingException
from .transaction_canceled_exception import (
    TransactionCanceledException as TransactionCanceledException,
)
from .transaction_conflict_exception import (
    TransactionConflictException as TransactionConflictException,
)
from .transaction_in_progress_exception import (
    TransactionInProgressException as TransactionInProgressException,
)
