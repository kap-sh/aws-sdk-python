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
    STSError as STSError,
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
from .expired_token_exception import ExpiredTokenException as ExpiredTokenException
from .expired_trade_in_token_exception import (
    ExpiredTradeInTokenException as ExpiredTradeInTokenException,
)
from .idp_communication_error_exception import (
    IDPCommunicationErrorException as IDPCommunicationErrorException,
)
from .idp_rejected_claim_exception import (
    IDPRejectedClaimException as IDPRejectedClaimException,
)
from .invalid_authorization_message_exception import (
    InvalidAuthorizationMessageException as InvalidAuthorizationMessageException,
)
from .invalid_identity_token_exception import (
    InvalidIdentityTokenException as InvalidIdentityTokenException,
)
from .jwt_payload_size_exceeded_exception import (
    JWTPayloadSizeExceededException as JWTPayloadSizeExceededException,
)
from .malformed_policy_document_exception import (
    MalformedPolicyDocumentException as MalformedPolicyDocumentException,
)
from .outbound_web_identity_federation_disabled_exception import (
    OutboundWebIdentityFederationDisabledException as OutboundWebIdentityFederationDisabledException,
)
from .packed_policy_too_large_exception import (
    PackedPolicyTooLargeException as PackedPolicyTooLargeException,
)
from .region_disabled_exception import (
    RegionDisabledException as RegionDisabledException,
)
from .session_duration_escalation_exception import (
    SessionDurationEscalationException as SessionDurationEscalationException,
)
