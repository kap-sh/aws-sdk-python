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
from .account_suspended_exception import (
    AccountSuspendedException as AccountSuspendedException,
)
from .already_exists_exception import AlreadyExistsException as AlreadyExistsException
from .bad_request_exception import BadRequestException as BadRequestException
from .concurrent_modification_exception import (
    ConcurrentModificationException as ConcurrentModificationException,
)
from .conflict_exception import ConflictException as ConflictException
from .internal_service_error_exception import (
    InternalServiceErrorException as InternalServiceErrorException,
)
from .invalid_next_token_exception import (
    InvalidNextTokenException as InvalidNextTokenException,
)
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .mail_from_domain_not_verified_exception import (
    MailFromDomainNotVerifiedException as MailFromDomainNotVerifiedException,
)
from .message_rejected import MessageRejected as MessageRejected
from .not_found_exception import NotFoundException as NotFoundException
from .sending_paused_exception import SendingPausedException as SendingPausedException
from .too_many_requests_exception import (
    TooManyRequestsException as TooManyRequestsException,
)
