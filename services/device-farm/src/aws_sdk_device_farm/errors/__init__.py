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
from .argument_exception import ArgumentException as ArgumentException
from .cannot_delete_exception import CannotDeleteException as CannotDeleteException
from .idempotency_exception import IdempotencyException as IdempotencyException
from .internal_service_exception import (
    InternalServiceException as InternalServiceException,
)
from .invalid_operation_exception import (
    InvalidOperationException as InvalidOperationException,
)
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .not_eligible_exception import NotEligibleException as NotEligibleException
from .not_found_exception import NotFoundException as NotFoundException
from .service_account_exception import (
    ServiceAccountException as ServiceAccountException,
)
from .tag_operation_exception import TagOperationException as TagOperationException
from .tag_policy_exception import TagPolicyException as TagPolicyException
from .too_many_tags_exception import TooManyTagsException as TooManyTagsException
