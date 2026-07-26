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
    SQSError as SQSError,
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
from .batch_entry_ids_not_distinct import (
    BatchEntryIdsNotDistinct as BatchEntryIdsNotDistinct,
)
from .batch_request_too_long import BatchRequestTooLong as BatchRequestTooLong
from .empty_batch_request import EmptyBatchRequest as EmptyBatchRequest
from .invalid_address import InvalidAddress as InvalidAddress
from .invalid_attribute_name import InvalidAttributeName as InvalidAttributeName
from .invalid_attribute_value import InvalidAttributeValue as InvalidAttributeValue
from .invalid_batch_entry_id import InvalidBatchEntryId as InvalidBatchEntryId
from .invalid_id_format import InvalidIdFormat as InvalidIdFormat
from .invalid_message_contents import InvalidMessageContents as InvalidMessageContents
from .invalid_security import InvalidSecurity as InvalidSecurity
from .kms_access_denied import KmsAccessDenied as KmsAccessDenied
from .kms_disabled import KmsDisabled as KmsDisabled
from .kms_invalid_key_usage import KmsInvalidKeyUsage as KmsInvalidKeyUsage
from .kms_invalid_state import KmsInvalidState as KmsInvalidState
from .kms_not_found import KmsNotFound as KmsNotFound
from .kms_opt_in_required import KmsOptInRequired as KmsOptInRequired
from .kms_throttled import KmsThrottled as KmsThrottled
from .message_not_inflight import MessageNotInflight as MessageNotInflight
from .over_limit import OverLimit as OverLimit
from .purge_queue_in_progress import PurgeQueueInProgress as PurgeQueueInProgress
from .queue_deleted_recently import QueueDeletedRecently as QueueDeletedRecently
from .queue_does_not_exist import QueueDoesNotExist as QueueDoesNotExist
from .queue_name_exists import QueueNameExists as QueueNameExists
from .receipt_handle_is_invalid import ReceiptHandleIsInvalid as ReceiptHandleIsInvalid
from .request_throttled import RequestThrottled as RequestThrottled
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .too_many_entries_in_batch_request import (
    TooManyEntriesInBatchRequest as TooManyEntriesInBatchRequest,
)
from .unsupported_operation import UnsupportedOperation as UnsupportedOperation
