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
    ServiceQuotasError as ServiceQuotasError,
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
from .aws_service_access_not_enabled_exception import (
    AWSServiceAccessNotEnabledException as AWSServiceAccessNotEnabledException,
)
from .dependency_access_denied_exception import (
    DependencyAccessDeniedException as DependencyAccessDeniedException,
)
from .illegal_argument_exception import (
    IllegalArgumentException as IllegalArgumentException,
)
from .invalid_pagination_token_exception import (
    InvalidPaginationTokenException as InvalidPaginationTokenException,
)
from .invalid_resource_state_exception import (
    InvalidResourceStateException as InvalidResourceStateException,
)
from .no_available_organization_exception import (
    NoAvailableOrganizationException as NoAvailableOrganizationException,
)
from .no_such_resource_exception import (
    NoSuchResourceException as NoSuchResourceException,
)
from .organization_not_in_all_features_mode_exception import (
    OrganizationNotInAllFeaturesModeException as OrganizationNotInAllFeaturesModeException,
)
from .quota_exceeded_exception import QuotaExceededException as QuotaExceededException
from .resource_already_exists_exception import (
    ResourceAlreadyExistsException as ResourceAlreadyExistsException,
)
from .service_exception import ServiceException as ServiceException
from .service_quota_template_not_in_use_exception import (
    ServiceQuotaTemplateNotInUseException as ServiceQuotaTemplateNotInUseException,
)
from .tag_policy_violation_exception import (
    TagPolicyViolationException as TagPolicyViolationException,
)
from .templates_not_available_in_region_exception import (
    TemplatesNotAvailableInRegionException as TemplatesNotAvailableInRegionException,
)
from .too_many_requests_exception import (
    TooManyRequestsException as TooManyRequestsException,
)
from .too_many_tags_exception import TooManyTagsException as TooManyTagsException
