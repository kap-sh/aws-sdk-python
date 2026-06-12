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
from .certificate_mismatch_exception import (
    CertificateMismatchException as CertificateMismatchException,
)
from .concurrent_modification_exception import (
    ConcurrentModificationException as ConcurrentModificationException,
)
from .invalid_args_exception import InvalidArgsException as InvalidArgsException
from .invalid_arn_exception import InvalidArnException as InvalidArnException
from .invalid_next_token_exception import (
    InvalidNextTokenException as InvalidNextTokenException,
)
from .invalid_policy_exception import InvalidPolicyException as InvalidPolicyException
from .invalid_request_exception import (
    InvalidRequestException as InvalidRequestException,
)
from .invalid_state_exception import InvalidStateException as InvalidStateException
from .invalid_tag_exception import InvalidTagException as InvalidTagException
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .lockout_prevented_exception import (
    LockoutPreventedException as LockoutPreventedException,
)
from .malformed_certificate_exception import (
    MalformedCertificateException as MalformedCertificateException,
)
from .malformed_csr_exception import MalformedCSRException as MalformedCSRException
from .permission_already_exists_exception import (
    PermissionAlreadyExistsException as PermissionAlreadyExistsException,
)
from .request_already_processed_exception import (
    RequestAlreadyProcessedException as RequestAlreadyProcessedException,
)
from .request_failed_exception import RequestFailedException as RequestFailedException
from .request_in_progress_exception import (
    RequestInProgressException as RequestInProgressException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .too_many_tags_exception import TooManyTagsException as TooManyTagsException
