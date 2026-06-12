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
from .access_point_already_owned_by_you import (
    AccessPointAlreadyOwnedByYou as AccessPointAlreadyOwnedByYou,
)
from .active_directory_error import ActiveDirectoryError as ActiveDirectoryError
from .backup_being_copied import BackupBeingCopied as BackupBeingCopied
from .backup_in_progress import BackupInProgress as BackupInProgress
from .backup_not_found import BackupNotFound as BackupNotFound
from .backup_restoring import BackupRestoring as BackupRestoring
from .bad_request import BadRequest as BadRequest
from .data_repository_association_not_found import (
    DataRepositoryAssociationNotFound as DataRepositoryAssociationNotFound,
)
from .data_repository_task_ended import (
    DataRepositoryTaskEnded as DataRepositoryTaskEnded,
)
from .data_repository_task_executing import (
    DataRepositoryTaskExecuting as DataRepositoryTaskExecuting,
)
from .data_repository_task_not_found import (
    DataRepositoryTaskNotFound as DataRepositoryTaskNotFound,
)
from .file_cache_not_found import FileCacheNotFound as FileCacheNotFound
from .file_system_not_found import FileSystemNotFound as FileSystemNotFound
from .incompatible_parameter_error import (
    IncompatibleParameterError as IncompatibleParameterError,
)
from .incompatible_region_for_multi_az import (
    IncompatibleRegionForMultiAZ as IncompatibleRegionForMultiAZ,
)
from .internal_server_error import InternalServerError as InternalServerError
from .invalid_access_point import InvalidAccessPoint as InvalidAccessPoint
from .invalid_data_repository_type import (
    InvalidDataRepositoryType as InvalidDataRepositoryType,
)
from .invalid_destination_kms_key import (
    InvalidDestinationKmsKey as InvalidDestinationKmsKey,
)
from .invalid_export_path import InvalidExportPath as InvalidExportPath
from .invalid_import_path import InvalidImportPath as InvalidImportPath
from .invalid_network_settings import InvalidNetworkSettings as InvalidNetworkSettings
from .invalid_per_unit_storage_throughput import (
    InvalidPerUnitStorageThroughput as InvalidPerUnitStorageThroughput,
)
from .invalid_region import InvalidRegion as InvalidRegion
from .invalid_request import InvalidRequest as InvalidRequest
from .invalid_source_kms_key import InvalidSourceKmsKey as InvalidSourceKmsKey
from .missing_file_cache_configuration import (
    MissingFileCacheConfiguration as MissingFileCacheConfiguration,
)
from .missing_file_system_configuration import (
    MissingFileSystemConfiguration as MissingFileSystemConfiguration,
)
from .missing_volume_configuration import (
    MissingVolumeConfiguration as MissingVolumeConfiguration,
)
from .not_service_resource_error import (
    NotServiceResourceError as NotServiceResourceError,
)
from .resource_does_not_support_tagging import (
    ResourceDoesNotSupportTagging as ResourceDoesNotSupportTagging,
)
from .resource_not_found import ResourceNotFound as ResourceNotFound
from .s3_access_point_attachment_not_found import (
    S3AccessPointAttachmentNotFound as S3AccessPointAttachmentNotFound,
)
from .service_limit_exceeded import ServiceLimitExceeded as ServiceLimitExceeded
from .snapshot_not_found import SnapshotNotFound as SnapshotNotFound
from .source_backup_unavailable import (
    SourceBackupUnavailable as SourceBackupUnavailable,
)
from .storage_virtual_machine_not_found import (
    StorageVirtualMachineNotFound as StorageVirtualMachineNotFound,
)
from .too_many_access_points import TooManyAccessPoints as TooManyAccessPoints
from .unsupported_operation import UnsupportedOperation as UnsupportedOperation
from .volume_not_found import VolumeNotFound as VolumeNotFound
