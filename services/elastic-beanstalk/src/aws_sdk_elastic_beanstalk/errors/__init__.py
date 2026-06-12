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
from .code_build_not_in_service_region_exception import (
    CodeBuildNotInServiceRegionException as CodeBuildNotInServiceRegionException,
)
from .elastic_beanstalk_service_exception import (
    ElasticBeanstalkServiceException as ElasticBeanstalkServiceException,
)
from .insufficient_privileges_exception import (
    InsufficientPrivilegesException as InsufficientPrivilegesException,
)
from .invalid_request_exception import (
    InvalidRequestException as InvalidRequestException,
)
from .managed_action_invalid_state_exception import (
    ManagedActionInvalidStateException as ManagedActionInvalidStateException,
)
from .operation_in_progress_exception import (
    OperationInProgressException as OperationInProgressException,
)
from .platform_version_still_referenced_exception import (
    PlatformVersionStillReferencedException as PlatformVersionStillReferencedException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .resource_type_not_supported_exception import (
    ResourceTypeNotSupportedException as ResourceTypeNotSupportedException,
)
from .s3_location_not_in_service_region_exception import (
    S3LocationNotInServiceRegionException as S3LocationNotInServiceRegionException,
)
from .s3_subscription_required_exception import (
    S3SubscriptionRequiredException as S3SubscriptionRequiredException,
)
from .source_bundle_deletion_exception import (
    SourceBundleDeletionException as SourceBundleDeletionException,
)
from .too_many_application_versions_exception import (
    TooManyApplicationVersionsException as TooManyApplicationVersionsException,
)
from .too_many_applications_exception import (
    TooManyApplicationsException as TooManyApplicationsException,
)
from .too_many_buckets_exception import (
    TooManyBucketsException as TooManyBucketsException,
)
from .too_many_configuration_templates_exception import (
    TooManyConfigurationTemplatesException as TooManyConfigurationTemplatesException,
)
from .too_many_environments_exception import (
    TooManyEnvironmentsException as TooManyEnvironmentsException,
)
from .too_many_platforms_exception import (
    TooManyPlatformsException as TooManyPlatformsException,
)
from .too_many_tags_exception import TooManyTagsException as TooManyTagsException
