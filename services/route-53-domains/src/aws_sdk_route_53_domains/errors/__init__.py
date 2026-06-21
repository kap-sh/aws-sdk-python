from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    Route53DomainsError as Route53DomainsError,
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
from .dnssec_limit_exceeded import DnssecLimitExceeded as DnssecLimitExceeded
from .domain_limit_exceeded import DomainLimitExceeded as DomainLimitExceeded
from .duplicate_request import DuplicateRequest as DuplicateRequest
from .invalid_input import InvalidInput as InvalidInput
from .operation_limit_exceeded import OperationLimitExceeded as OperationLimitExceeded
from .tld_in_maintenance import TLDInMaintenance as TLDInMaintenance
from .tld_rules_violation import TLDRulesViolation as TLDRulesViolation
from .unsupported_tld import UnsupportedTLD as UnsupportedTLD
