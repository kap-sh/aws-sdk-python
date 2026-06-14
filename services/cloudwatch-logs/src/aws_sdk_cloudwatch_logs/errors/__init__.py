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
from .data_already_accepted_exception import (
    DataAlreadyAcceptedException as DataAlreadyAcceptedException,
)
from .internal_server_exception import (
    InternalServerException as InternalServerException,
)
from .internal_streaming_exception import (
    InternalStreamingException as InternalStreamingException,
)
from .invalid_operation_exception import (
    InvalidOperationException as InvalidOperationException,
)
from .invalid_parameter_exception import (
    InvalidParameterException as InvalidParameterException,
)
from .invalid_sequence_token_exception import (
    InvalidSequenceTokenException as InvalidSequenceTokenException,
)
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .malformed_query_exception import (
    MalformedQueryException as MalformedQueryException,
)
from .operation_aborted_exception import (
    OperationAbortedException as OperationAbortedException,
)
from .resource_already_exists_exception import (
    ResourceAlreadyExistsException as ResourceAlreadyExistsException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .service_quota_exceeded_exception import (
    ServiceQuotaExceededException as ServiceQuotaExceededException,
)
from .service_unavailable_exception import (
    ServiceUnavailableException as ServiceUnavailableException,
)
from .session_streaming_exception import (
    SessionStreamingException as SessionStreamingException,
)
from .session_timeout_exception import (
    SessionTimeoutException as SessionTimeoutException,
)
from .throttling_exception import ThrottlingException as ThrottlingException
from .too_many_tags_exception import TooManyTagsException as TooManyTagsException
from .unrecognized_client_exception import (
    UnrecognizedClientException as UnrecognizedClientException,
)
from .validation_exception import ValidationException as ValidationException
