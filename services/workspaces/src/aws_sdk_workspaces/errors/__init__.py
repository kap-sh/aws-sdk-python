from __future__ import annotations
from ._base import (
    DeserializationError as DeserializationError,
    SerializationError as SerializationError,
    ServiceError as ServiceError,
    UnknownServiceError as UnknownServiceError,
    WaiterFailedError as WaiterFailedError,
    WaiterTimeoutError as WaiterTimeoutError,
)
from .access_denied_exception import AccessDeniedException as AccessDeniedException
from .application_not_supported_exception import (
    ApplicationNotSupportedException as ApplicationNotSupportedException,
)
from .compute_not_compatible_exception import (
    ComputeNotCompatibleException as ComputeNotCompatibleException,
)
from .conflict_exception import ConflictException as ConflictException
from .incompatible_applications_exception import (
    IncompatibleApplicationsException as IncompatibleApplicationsException,
)
from .internal_server_exception import (
    InternalServerException as InternalServerException,
)
from .invalid_parameter_combination_exception import (
    InvalidParameterCombinationException as InvalidParameterCombinationException,
)
from .invalid_parameter_values_exception import (
    InvalidParameterValuesException as InvalidParameterValuesException,
)
from .invalid_resource_state_exception import (
    InvalidResourceStateException as InvalidResourceStateException,
)
from .operating_system_not_compatible_exception import (
    OperatingSystemNotCompatibleException as OperatingSystemNotCompatibleException,
)
from .operation_in_progress_exception import (
    OperationInProgressException as OperationInProgressException,
)
from .operation_not_supported_exception import (
    OperationNotSupportedException as OperationNotSupportedException,
)
from .resource_already_exists_exception import (
    ResourceAlreadyExistsException as ResourceAlreadyExistsException,
)
from .resource_associated_exception import (
    ResourceAssociatedException as ResourceAssociatedException,
)
from .resource_creation_failed_exception import (
    ResourceCreationFailedException as ResourceCreationFailedException,
)
from .resource_in_use_exception import ResourceInUseException as ResourceInUseException
from .resource_limit_exceeded_exception import (
    ResourceLimitExceededException as ResourceLimitExceededException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .resource_unavailable_exception import (
    ResourceUnavailableException as ResourceUnavailableException,
)
from .unsupported_network_configuration_exception import (
    UnsupportedNetworkConfigurationException as UnsupportedNetworkConfigurationException,
)
from .unsupported_workspace_configuration_exception import (
    UnsupportedWorkspaceConfigurationException as UnsupportedWorkspaceConfigurationException,
)
from .validation_exception import ValidationException as ValidationException
from .workspaces_default_role_not_found_exception import (
    WorkspacesDefaultRoleNotFoundException as WorkspacesDefaultRoleNotFoundException,
)
