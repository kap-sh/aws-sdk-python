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
    TextractError as TextractError,
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
from .bad_document_exception import BadDocumentException as BadDocumentException
from .conflict_exception import ConflictException as ConflictException
from .document_too_large_exception import (
    DocumentTooLargeException as DocumentTooLargeException,
)
from .human_loop_quota_exceeded_exception import (
    HumanLoopQuotaExceededException as HumanLoopQuotaExceededException,
)
from .idempotent_parameter_mismatch_exception import (
    IdempotentParameterMismatchException as IdempotentParameterMismatchException,
)
from .internal_server_error import InternalServerError as InternalServerError
from .invalid_job_id_exception import InvalidJobIdException as InvalidJobIdException
from .invalid_kms_key_exception import InvalidKMSKeyException as InvalidKMSKeyException
from .invalid_parameter_exception import (
    InvalidParameterException as InvalidParameterException,
)
from .invalid_s3_object_exception import (
    InvalidS3ObjectException as InvalidS3ObjectException,
)
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .provisioned_throughput_exceeded_exception import (
    ProvisionedThroughputExceededException as ProvisionedThroughputExceededException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .service_quota_exceeded_exception import (
    ServiceQuotaExceededException as ServiceQuotaExceededException,
)
from .throttling_exception import ThrottlingException as ThrottlingException
from .unsupported_document_exception import (
    UnsupportedDocumentException as UnsupportedDocumentException,
)
from .validation_exception import ValidationException as ValidationException
