from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    DirectoryServiceError as DirectoryServiceError,
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
from .ad_assessment_limit_exceeded_exception import (
    ADAssessmentLimitExceededException as ADAssessmentLimitExceededException,
)
from .authentication_failed_exception import (
    AuthenticationFailedException as AuthenticationFailedException,
)
from .certificate_already_exists_exception import (
    CertificateAlreadyExistsException as CertificateAlreadyExistsException,
)
from .certificate_does_not_exist_exception import (
    CertificateDoesNotExistException as CertificateDoesNotExistException,
)
from .certificate_in_use_exception import (
    CertificateInUseException as CertificateInUseException,
)
from .certificate_limit_exceeded_exception import (
    CertificateLimitExceededException as CertificateLimitExceededException,
)
from .client_exception import ClientException as ClientException
from .directory_already_in_region_exception import (
    DirectoryAlreadyInRegionException as DirectoryAlreadyInRegionException,
)
from .directory_already_shared_exception import (
    DirectoryAlreadySharedException as DirectoryAlreadySharedException,
)
from .directory_does_not_exist_exception import (
    DirectoryDoesNotExistException as DirectoryDoesNotExistException,
)
from .directory_in_desired_state_exception import (
    DirectoryInDesiredStateException as DirectoryInDesiredStateException,
)
from .directory_limit_exceeded_exception import (
    DirectoryLimitExceededException as DirectoryLimitExceededException,
)
from .directory_not_shared_exception import (
    DirectoryNotSharedException as DirectoryNotSharedException,
)
from .directory_unavailable_exception import (
    DirectoryUnavailableException as DirectoryUnavailableException,
)
from .disable_already_in_progress_exception import (
    DisableAlreadyInProgressException as DisableAlreadyInProgressException,
)
from .domain_controller_limit_exceeded_exception import (
    DomainControllerLimitExceededException as DomainControllerLimitExceededException,
)
from .enable_already_in_progress_exception import (
    EnableAlreadyInProgressException as EnableAlreadyInProgressException,
)
from .entity_already_exists_exception import (
    EntityAlreadyExistsException as EntityAlreadyExistsException,
)
from .entity_does_not_exist_exception import (
    EntityDoesNotExistException as EntityDoesNotExistException,
)
from .incompatible_settings_exception import (
    IncompatibleSettingsException as IncompatibleSettingsException,
)
from .insufficient_permissions_exception import (
    InsufficientPermissionsException as InsufficientPermissionsException,
)
from .invalid_certificate_exception import (
    InvalidCertificateException as InvalidCertificateException,
)
from .invalid_client_auth_status_exception import (
    InvalidClientAuthStatusException as InvalidClientAuthStatusException,
)
from .invalid_ldaps_status_exception import (
    InvalidLDAPSStatusException as InvalidLDAPSStatusException,
)
from .invalid_next_token_exception import (
    InvalidNextTokenException as InvalidNextTokenException,
)
from .invalid_parameter_exception import (
    InvalidParameterException as InvalidParameterException,
)
from .invalid_password_exception import (
    InvalidPasswordException as InvalidPasswordException,
)
from .invalid_target_exception import InvalidTargetException as InvalidTargetException
from .ip_route_limit_exceeded_exception import (
    IpRouteLimitExceededException as IpRouteLimitExceededException,
)
from .no_available_certificate_exception import (
    NoAvailableCertificateException as NoAvailableCertificateException,
)
from .organizations_exception import OrganizationsException as OrganizationsException
from .region_limit_exceeded_exception import (
    RegionLimitExceededException as RegionLimitExceededException,
)
from .service_exception import ServiceException as ServiceException
from .share_limit_exceeded_exception import (
    ShareLimitExceededException as ShareLimitExceededException,
)
from .snapshot_limit_exceeded_exception import (
    SnapshotLimitExceededException as SnapshotLimitExceededException,
)
from .tag_limit_exceeded_exception import (
    TagLimitExceededException as TagLimitExceededException,
)
from .unsupported_operation_exception import (
    UnsupportedOperationException as UnsupportedOperationException,
)
from .unsupported_settings_exception import (
    UnsupportedSettingsException as UnsupportedSettingsException,
)
from .user_does_not_exist_exception import (
    UserDoesNotExistException as UserDoesNotExistException,
)
