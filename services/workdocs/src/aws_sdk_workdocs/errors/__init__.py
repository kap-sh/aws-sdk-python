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
from .concurrent_modification_exception import (
    ConcurrentModificationException as ConcurrentModificationException,
)
from .conflicting_operation_exception import (
    ConflictingOperationException as ConflictingOperationException,
)
from .custom_metadata_limit_exceeded_exception import (
    CustomMetadataLimitExceededException as CustomMetadataLimitExceededException,
)
from .deactivating_last_system_user_exception import (
    DeactivatingLastSystemUserException as DeactivatingLastSystemUserException,
)
from .document_locked_for_comments_exception import (
    DocumentLockedForCommentsException as DocumentLockedForCommentsException,
)
from .draft_upload_out_of_sync_exception import (
    DraftUploadOutOfSyncException as DraftUploadOutOfSyncException,
)
from .entity_already_exists_exception import (
    EntityAlreadyExistsException as EntityAlreadyExistsException,
)
from .entity_not_exists_exception import (
    EntityNotExistsException as EntityNotExistsException,
)
from .failed_dependency_exception import (
    FailedDependencyException as FailedDependencyException,
)
from .illegal_user_state_exception import (
    IllegalUserStateException as IllegalUserStateException,
)
from .invalid_argument_exception import (
    InvalidArgumentException as InvalidArgumentException,
)
from .invalid_comment_operation_exception import (
    InvalidCommentOperationException as InvalidCommentOperationException,
)
from .invalid_operation_exception import (
    InvalidOperationException as InvalidOperationException,
)
from .invalid_password_exception import (
    InvalidPasswordException as InvalidPasswordException,
)
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .prohibited_state_exception import (
    ProhibitedStateException as ProhibitedStateException,
)
from .requested_entity_too_large_exception import (
    RequestedEntityTooLargeException as RequestedEntityTooLargeException,
)
from .resource_already_checked_out_exception import (
    ResourceAlreadyCheckedOutException as ResourceAlreadyCheckedOutException,
)
from .service_unavailable_exception import (
    ServiceUnavailableException as ServiceUnavailableException,
)
from .storage_limit_exceeded_exception import (
    StorageLimitExceededException as StorageLimitExceededException,
)
from .storage_limit_will_exceed_exception import (
    StorageLimitWillExceedException as StorageLimitWillExceedException,
)
from .too_many_labels_exception import TooManyLabelsException as TooManyLabelsException
from .too_many_subscriptions_exception import (
    TooManySubscriptionsException as TooManySubscriptionsException,
)
from .unauthorized_operation_exception import (
    UnauthorizedOperationException as UnauthorizedOperationException,
)
from .unauthorized_resource_access_exception import (
    UnauthorizedResourceAccessException as UnauthorizedResourceAccessException,
)
