from __future__ import annotations
from ._base import (
    DeserializationError as DeserializationError,
    SerializationError as SerializationError,
    ServiceError as ServiceError,
    UnknownServiceError as UnknownServiceError,
    WaiterFailedError as WaiterFailedError,
    WaiterTimeoutError as WaiterTimeoutError,
)
from .access_denied import AccessDenied as AccessDenied
from .bucket_already_exists import BucketAlreadyExists as BucketAlreadyExists
from .bucket_already_owned_by_you import (
    BucketAlreadyOwnedByYou as BucketAlreadyOwnedByYou,
)
from .encryption_type_mismatch import EncryptionTypeMismatch as EncryptionTypeMismatch
from .idempotency_parameter_mismatch import (
    IdempotencyParameterMismatch as IdempotencyParameterMismatch,
)
from .invalid_object_state import InvalidObjectState as InvalidObjectState
from .invalid_request import InvalidRequest as InvalidRequest
from .invalid_write_offset import InvalidWriteOffset as InvalidWriteOffset
from .no_such_bucket import NoSuchBucket as NoSuchBucket
from .no_such_key import NoSuchKey as NoSuchKey
from .no_such_upload import NoSuchUpload as NoSuchUpload
from .not_found import NotFound as NotFound
from .object_already_in_active_tier_error import (
    ObjectAlreadyInActiveTierError as ObjectAlreadyInActiveTierError,
)
from .object_not_in_active_tier_error import (
    ObjectNotInActiveTierError as ObjectNotInActiveTierError,
)
from .too_many_parts import TooManyParts as TooManyParts
