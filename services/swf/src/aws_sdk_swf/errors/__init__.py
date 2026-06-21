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
    SWFError as SWFError,
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
from .default_undefined_fault import DefaultUndefinedFault as DefaultUndefinedFault
from .domain_already_exists_fault import (
    DomainAlreadyExistsFault as DomainAlreadyExistsFault,
)
from .domain_deprecated_fault import DomainDeprecatedFault as DomainDeprecatedFault
from .limit_exceeded_fault import LimitExceededFault as LimitExceededFault
from .operation_not_permitted_fault import (
    OperationNotPermittedFault as OperationNotPermittedFault,
)
from .too_many_tags_fault import TooManyTagsFault as TooManyTagsFault
from .type_already_exists_fault import TypeAlreadyExistsFault as TypeAlreadyExistsFault
from .type_deprecated_fault import TypeDeprecatedFault as TypeDeprecatedFault
from .type_not_deprecated_fault import TypeNotDeprecatedFault as TypeNotDeprecatedFault
from .unknown_resource_fault import UnknownResourceFault as UnknownResourceFault
from .workflow_execution_already_started_fault import (
    WorkflowExecutionAlreadyStartedFault as WorkflowExecutionAlreadyStartedFault,
)
