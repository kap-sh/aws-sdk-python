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
from .access_denied_exception import AccessDeniedException as AccessDeniedException
from .conflict_exception import ConflictException as ConflictException
from .invalid_args_exception import InvalidArgsException as InvalidArgsException
from .invalid_arn_exception import InvalidArnException as InvalidArnException
from .invalid_domain_validation_options_exception import (
    InvalidDomainValidationOptionsException as InvalidDomainValidationOptionsException,
)
from .invalid_parameter_exception import (
    InvalidParameterException as InvalidParameterException,
)
from .invalid_state_exception import InvalidStateException as InvalidStateException
from .invalid_tag_exception import InvalidTagException as InvalidTagException
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .request_in_progress_exception import (
    RequestInProgressException as RequestInProgressException,
)
from .resource_in_use_exception import ResourceInUseException as ResourceInUseException
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .tag_policy_exception import TagPolicyException as TagPolicyException
from .throttling_exception import ThrottlingException as ThrottlingException
from .too_many_tags_exception import TooManyTagsException as TooManyTagsException
from .validation_exception import ValidationException as ValidationException
