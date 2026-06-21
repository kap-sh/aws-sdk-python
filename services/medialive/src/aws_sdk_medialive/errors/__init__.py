from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    MediaLiveError as MediaLiveError,
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
from .bad_gateway_exception import BadGatewayException as BadGatewayException
from .bad_request_exception import BadRequestException as BadRequestException
from .conflict_exception import ConflictException as ConflictException
from .forbidden_exception import ForbiddenException as ForbiddenException
from .gateway_timeout_exception import (
    GatewayTimeoutException as GatewayTimeoutException,
)
from .internal_server_error_exception import (
    InternalServerErrorException as InternalServerErrorException,
)
from .not_found_exception import NotFoundException as NotFoundException
from .too_many_requests_exception import (
    TooManyRequestsException as TooManyRequestsException,
)
from .unprocessable_entity_exception import (
    UnprocessableEntityException as UnprocessableEntityException,
)
