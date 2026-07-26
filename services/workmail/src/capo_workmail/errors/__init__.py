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
from ._base import (
    WorkMailError as WorkMailError,
)
from .directory_in_use_exception import (
    DirectoryInUseException as DirectoryInUseException,
)
from .directory_service_authentication_failed_exception import (
    DirectoryServiceAuthenticationFailedException as DirectoryServiceAuthenticationFailedException,
)
from .directory_unavailable_exception import (
    DirectoryUnavailableException as DirectoryUnavailableException,
)
from .email_address_in_use_exception import (
    EmailAddressInUseException as EmailAddressInUseException,
)
from .entity_already_registered_exception import (
    EntityAlreadyRegisteredException as EntityAlreadyRegisteredException,
)
from .entity_not_found_exception import (
    EntityNotFoundException as EntityNotFoundException,
)
from .entity_state_exception import EntityStateException as EntityStateException
from .invalid_configuration_exception import (
    InvalidConfigurationException as InvalidConfigurationException,
)
from .invalid_custom_ses_configuration_exception import (
    InvalidCustomSesConfigurationException as InvalidCustomSesConfigurationException,
)
from .invalid_parameter_exception import (
    InvalidParameterException as InvalidParameterException,
)
from .invalid_password_exception import (
    InvalidPasswordException as InvalidPasswordException,
)
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .mail_domain_in_use_exception import (
    MailDomainInUseException as MailDomainInUseException,
)
from .mail_domain_not_found_exception import (
    MailDomainNotFoundException as MailDomainNotFoundException,
)
from .mail_domain_state_exception import (
    MailDomainStateException as MailDomainStateException,
)
from .name_availability_exception import (
    NameAvailabilityException as NameAvailabilityException,
)
from .organization_not_found_exception import (
    OrganizationNotFoundException as OrganizationNotFoundException,
)
from .organization_state_exception import (
    OrganizationStateException as OrganizationStateException,
)
from .reserved_name_exception import ReservedNameException as ReservedNameException
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .too_many_tags_exception import TooManyTagsException as TooManyTagsException
from .unsupported_operation_exception import (
    UnsupportedOperationException as UnsupportedOperationException,
)
