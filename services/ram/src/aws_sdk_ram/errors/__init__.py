from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    RAMError as RAMError,
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
from .idempotent_parameter_mismatch_exception import (
    IdempotentParameterMismatchException as IdempotentParameterMismatchException,
)
from .invalid_client_token_exception import (
    InvalidClientTokenException as InvalidClientTokenException,
)
from .invalid_max_results_exception import (
    InvalidMaxResultsException as InvalidMaxResultsException,
)
from .invalid_next_token_exception import (
    InvalidNextTokenException as InvalidNextTokenException,
)
from .invalid_parameter_exception import (
    InvalidParameterException as InvalidParameterException,
)
from .invalid_policy_exception import InvalidPolicyException as InvalidPolicyException
from .invalid_resource_type_exception import (
    InvalidResourceTypeException as InvalidResourceTypeException,
)
from .invalid_state_transition_exception import (
    InvalidStateTransitionException as InvalidStateTransitionException,
)
from .malformed_arn_exception import MalformedArnException as MalformedArnException
from .malformed_policy_template_exception import (
    MalformedPolicyTemplateException as MalformedPolicyTemplateException,
)
from .missing_required_parameter_exception import (
    MissingRequiredParameterException as MissingRequiredParameterException,
)
from .operation_not_permitted_exception import (
    OperationNotPermittedException as OperationNotPermittedException,
)
from .permission_already_exists_exception import (
    PermissionAlreadyExistsException as PermissionAlreadyExistsException,
)
from .permission_limit_exceeded_exception import (
    PermissionLimitExceededException as PermissionLimitExceededException,
)
from .permission_versions_limit_exceeded_exception import (
    PermissionVersionsLimitExceededException as PermissionVersionsLimitExceededException,
)
from .resource_arn_not_found_exception import (
    ResourceArnNotFoundException as ResourceArnNotFoundException,
)
from .resource_share_invitation_already_accepted_exception import (
    ResourceShareInvitationAlreadyAcceptedException as ResourceShareInvitationAlreadyAcceptedException,
)
from .resource_share_invitation_already_rejected_exception import (
    ResourceShareInvitationAlreadyRejectedException as ResourceShareInvitationAlreadyRejectedException,
)
from .resource_share_invitation_arn_not_found_exception import (
    ResourceShareInvitationArnNotFoundException as ResourceShareInvitationArnNotFoundException,
)
from .resource_share_invitation_expired_exception import (
    ResourceShareInvitationExpiredException as ResourceShareInvitationExpiredException,
)
from .resource_share_limit_exceeded_exception import (
    ResourceShareLimitExceededException as ResourceShareLimitExceededException,
)
from .server_internal_exception import (
    ServerInternalException as ServerInternalException,
)
from .service_unavailable_exception import (
    ServiceUnavailableException as ServiceUnavailableException,
)
from .tag_limit_exceeded_exception import (
    TagLimitExceededException as TagLimitExceededException,
)
from .tag_policy_violation_exception import (
    TagPolicyViolationException as TagPolicyViolationException,
)
from .throttling_exception import ThrottlingException as ThrottlingException
from .unknown_resource_exception import (
    UnknownResourceException as UnknownResourceException,
)
from .unmatched_policy_permission_exception import (
    UnmatchedPolicyPermissionException as UnmatchedPolicyPermissionException,
)
