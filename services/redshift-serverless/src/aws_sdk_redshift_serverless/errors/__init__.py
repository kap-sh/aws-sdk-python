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
from .dry_run_exception import DryRunException as DryRunException
from .insufficient_capacity_exception import (
    InsufficientCapacityException as InsufficientCapacityException,
)
from .internal_server_exception import (
    InternalServerException as InternalServerException,
)
from .invalid_pagination_exception import (
    InvalidPaginationException as InvalidPaginationException,
)
from .ipv6_cidr_block_not_found_exception import (
    Ipv6CidrBlockNotFoundException as Ipv6CidrBlockNotFoundException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .service_quota_exceeded_exception import (
    ServiceQuotaExceededException as ServiceQuotaExceededException,
)
from .throttling_exception import ThrottlingException as ThrottlingException
from .too_many_tags_exception import TooManyTagsException as TooManyTagsException
from .validation_exception import ValidationException as ValidationException
