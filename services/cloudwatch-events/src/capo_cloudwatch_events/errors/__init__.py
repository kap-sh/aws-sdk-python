from __future__ import annotations

from ._base import (
    CloudWatchEventsError as CloudWatchEventsError,
)
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
from .concurrent_modification_exception import (
    ConcurrentModificationException as ConcurrentModificationException,
)
from .illegal_status_exception import IllegalStatusException as IllegalStatusException
from .internal_exception import InternalException as InternalException
from .invalid_event_pattern_exception import (
    InvalidEventPatternException as InvalidEventPatternException,
)
from .invalid_state_exception import InvalidStateException as InvalidStateException
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .managed_rule_exception import ManagedRuleException as ManagedRuleException
from .operation_disabled_exception import (
    OperationDisabledException as OperationDisabledException,
)
from .policy_length_exceeded_exception import (
    PolicyLengthExceededException as PolicyLengthExceededException,
)
from .resource_already_exists_exception import (
    ResourceAlreadyExistsException as ResourceAlreadyExistsException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
