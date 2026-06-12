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
from .invalid_policy_revision_id_exception import (
    InvalidPolicyRevisionIdException as InvalidPolicyRevisionIdException,
)
from .invalid_request_exception import (
    InvalidRequestException as InvalidRequestException,
)
from .lockout_prevention_exception import (
    LockoutPreventionException as LockoutPreventionException,
)
from .malformed_policy_document_exception import (
    MalformedPolicyDocumentException as MalformedPolicyDocumentException,
)
from .policy_count_limit_exceeded_exception import (
    PolicyCountLimitExceededException as PolicyCountLimitExceededException,
)
from .policy_size_limit_exceeded_exception import (
    PolicySizeLimitExceededException as PolicySizeLimitExceededException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .rule_limit_exceeded_exception import (
    RuleLimitExceededException as RuleLimitExceededException,
)
from .throttled_exception import ThrottledException as ThrottledException
from .too_many_tags_exception import TooManyTagsException as TooManyTagsException
