from __future__ import annotations
from ._base import (
    DeserializationError as DeserializationError,
    SerializationError as SerializationError,
    ServiceError as ServiceError,
    UnknownServiceError as UnknownServiceError,
    WaiterFailedError as WaiterFailedError,
    WaiterTimeoutError as WaiterTimeoutError,
)
from .decryption_failure import DecryptionFailure as DecryptionFailure
from .encryption_failure import EncryptionFailure as EncryptionFailure
from .internal_service_error import InternalServiceError as InternalServiceError
from .invalid_next_token_exception import (
    InvalidNextTokenException as InvalidNextTokenException,
)
from .invalid_parameter_exception import (
    InvalidParameterException as InvalidParameterException,
)
from .invalid_request_exception import (
    InvalidRequestException as InvalidRequestException,
)
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .malformed_policy_document_exception import (
    MalformedPolicyDocumentException as MalformedPolicyDocumentException,
)
from .precondition_not_met_exception import (
    PreconditionNotMetException as PreconditionNotMetException,
)
from .public_policy_exception import PublicPolicyException as PublicPolicyException
from .resource_exists_exception import (
    ResourceExistsException as ResourceExistsException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
