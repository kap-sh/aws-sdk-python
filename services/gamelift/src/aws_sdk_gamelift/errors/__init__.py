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
from .conflict_exception import ConflictException as ConflictException
from .fleet_capacity_exceeded_exception import (
    FleetCapacityExceededException as FleetCapacityExceededException,
)
from .game_session_full_exception import (
    GameSessionFullException as GameSessionFullException,
)
from .idempotent_parameter_mismatch_exception import (
    IdempotentParameterMismatchException as IdempotentParameterMismatchException,
)
from .internal_service_exception import (
    InternalServiceException as InternalServiceException,
)
from .invalid_fleet_status_exception import (
    InvalidFleetStatusException as InvalidFleetStatusException,
)
from .invalid_game_session_status_exception import (
    InvalidGameSessionStatusException as InvalidGameSessionStatusException,
)
from .invalid_request_exception import (
    InvalidRequestException as InvalidRequestException,
)
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .not_found_exception import NotFoundException as NotFoundException
from .not_ready_exception import NotReadyException as NotReadyException
from .out_of_capacity_exception import OutOfCapacityException as OutOfCapacityException
from .tagging_failed_exception import TaggingFailedException as TaggingFailedException
from .terminal_routing_strategy_exception import (
    TerminalRoutingStrategyException as TerminalRoutingStrategyException,
)
from .unauthorized_exception import UnauthorizedException as UnauthorizedException
from .unsupported_region_exception import (
    UnsupportedRegionException as UnsupportedRegionException,
)
