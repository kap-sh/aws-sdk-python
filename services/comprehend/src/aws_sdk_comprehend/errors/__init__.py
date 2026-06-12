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
from .batch_size_limit_exceeded_exception import (
    BatchSizeLimitExceededException as BatchSizeLimitExceededException,
)
from .concurrent_modification_exception import (
    ConcurrentModificationException as ConcurrentModificationException,
)
from .internal_server_exception import (
    InternalServerException as InternalServerException,
)
from .invalid_filter_exception import InvalidFilterException as InvalidFilterException
from .invalid_request_exception import (
    InvalidRequestException as InvalidRequestException,
)
from .job_not_found_exception import JobNotFoundException as JobNotFoundException
from .kms_key_validation_exception import (
    KmsKeyValidationException as KmsKeyValidationException,
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
from .text_size_limit_exceeded_exception import (
    TextSizeLimitExceededException as TextSizeLimitExceededException,
)
from .too_many_requests_exception import (
    TooManyRequestsException as TooManyRequestsException,
)
from .too_many_tag_keys_exception import (
    TooManyTagKeysException as TooManyTagKeysException,
)
from .too_many_tags_exception import TooManyTagsException as TooManyTagsException
from .unsupported_language_exception import (
    UnsupportedLanguageException as UnsupportedLanguageException,
)
