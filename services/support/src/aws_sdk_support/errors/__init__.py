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
    SupportError as SupportError,
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
from .attachment_id_not_found import AttachmentIdNotFound as AttachmentIdNotFound
from .attachment_limit_exceeded import (
    AttachmentLimitExceeded as AttachmentLimitExceeded,
)
from .attachment_set_expired import AttachmentSetExpired as AttachmentSetExpired
from .attachment_set_id_not_found import (
    AttachmentSetIdNotFound as AttachmentSetIdNotFound,
)
from .attachment_set_size_limit_exceeded import (
    AttachmentSetSizeLimitExceeded as AttachmentSetSizeLimitExceeded,
)
from .case_creation_limit_exceeded import (
    CaseCreationLimitExceeded as CaseCreationLimitExceeded,
)
from .case_id_not_found import CaseIdNotFound as CaseIdNotFound
from .describe_attachment_limit_exceeded import (
    DescribeAttachmentLimitExceeded as DescribeAttachmentLimitExceeded,
)
from .internal_server_error import InternalServerError as InternalServerError
from .throttling_exception import ThrottlingException as ThrottlingException
