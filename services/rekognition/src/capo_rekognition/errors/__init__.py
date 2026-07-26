from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    RekognitionError as RekognitionError,
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
from .human_loop_quota_exceeded_exception import (
    HumanLoopQuotaExceededException as HumanLoopQuotaExceededException,
)
from .idempotent_parameter_mismatch_exception import (
    IdempotentParameterMismatchException as IdempotentParameterMismatchException,
)
from .image_too_large_exception import ImageTooLargeException as ImageTooLargeException
from .internal_server_error import InternalServerError as InternalServerError
from .invalid_image_format_exception import (
    InvalidImageFormatException as InvalidImageFormatException,
)
from .invalid_manifest_exception import (
    InvalidManifestException as InvalidManifestException,
)
from .invalid_pagination_token_exception import (
    InvalidPaginationTokenException as InvalidPaginationTokenException,
)
from .invalid_parameter_exception import (
    InvalidParameterException as InvalidParameterException,
)
from .invalid_policy_revision_id_exception import (
    InvalidPolicyRevisionIdException as InvalidPolicyRevisionIdException,
)
from .invalid_s3_object_exception import (
    InvalidS3ObjectException as InvalidS3ObjectException,
)
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .malformed_policy_document_exception import (
    MalformedPolicyDocumentException as MalformedPolicyDocumentException,
)
from .provisioned_throughput_exceeded_exception import (
    ProvisionedThroughputExceededException as ProvisionedThroughputExceededException,
)
from .resource_already_exists_exception import (
    ResourceAlreadyExistsException as ResourceAlreadyExistsException,
)
from .resource_in_use_exception import ResourceInUseException as ResourceInUseException
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .resource_not_ready_exception import (
    ResourceNotReadyException as ResourceNotReadyException,
)
from .service_quota_exceeded_exception import (
    ServiceQuotaExceededException as ServiceQuotaExceededException,
)
from .session_not_found_exception import (
    SessionNotFoundException as SessionNotFoundException,
)
from .throttling_exception import ThrottlingException as ThrottlingException
from .video_too_large_exception import VideoTooLargeException as VideoTooLargeException
