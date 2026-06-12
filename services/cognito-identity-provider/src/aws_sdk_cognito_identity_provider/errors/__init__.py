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
from .access_denied_exception import AccessDeniedException as AccessDeniedException
from .alias_exists_exception import AliasExistsException as AliasExistsException
from .code_delivery_failure_exception import (
    CodeDeliveryFailureException as CodeDeliveryFailureException,
)
from .code_mismatch_exception import CodeMismatchException as CodeMismatchException
from .concurrent_modification_exception import (
    ConcurrentModificationException as ConcurrentModificationException,
)
from .device_key_exists_exception import (
    DeviceKeyExistsException as DeviceKeyExistsException,
)
from .duplicate_provider_exception import (
    DuplicateProviderException as DuplicateProviderException,
)
from .enable_software_token_mfa_exception import (
    EnableSoftwareTokenMFAException as EnableSoftwareTokenMFAException,
)
from .expired_code_exception import ExpiredCodeException as ExpiredCodeException
from .feature_unavailable_in_tier_exception import (
    FeatureUnavailableInTierException as FeatureUnavailableInTierException,
)
from .forbidden_exception import ForbiddenException as ForbiddenException
from .group_exists_exception import GroupExistsException as GroupExistsException
from .internal_error_exception import InternalErrorException as InternalErrorException
from .internal_server_exception import (
    InternalServerException as InternalServerException,
)
from .invalid_email_role_access_policy_exception import (
    InvalidEmailRoleAccessPolicyException as InvalidEmailRoleAccessPolicyException,
)
from .invalid_lambda_response_exception import (
    InvalidLambdaResponseException as InvalidLambdaResponseException,
)
from .invalid_o_auth_flow_exception import (
    InvalidOAuthFlowException as InvalidOAuthFlowException,
)
from .invalid_parameter_exception import (
    InvalidParameterException as InvalidParameterException,
)
from .invalid_password_exception import (
    InvalidPasswordException as InvalidPasswordException,
)
from .invalid_sms_role_access_policy_exception import (
    InvalidSmsRoleAccessPolicyException as InvalidSmsRoleAccessPolicyException,
)
from .invalid_sms_role_trust_relationship_exception import (
    InvalidSmsRoleTrustRelationshipException as InvalidSmsRoleTrustRelationshipException,
)
from .invalid_user_pool_configuration_exception import (
    InvalidUserPoolConfigurationException as InvalidUserPoolConfigurationException,
)
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .managed_login_branding_exists_exception import (
    ManagedLoginBrandingExistsException as ManagedLoginBrandingExistsException,
)
from .mfa_method_not_found_exception import (
    MFAMethodNotFoundException as MFAMethodNotFoundException,
)
from .not_authorized_exception import NotAuthorizedException as NotAuthorizedException
from .operation_not_enabled_exception import (
    OperationNotEnabledException as OperationNotEnabledException,
)
from .password_history_policy_violation_exception import (
    PasswordHistoryPolicyViolationException as PasswordHistoryPolicyViolationException,
)
from .password_reset_required_exception import (
    PasswordResetRequiredException as PasswordResetRequiredException,
)
from .precondition_not_met_exception import (
    PreconditionNotMetException as PreconditionNotMetException,
)
from .refresh_token_reuse_exception import (
    RefreshTokenReuseException as RefreshTokenReuseException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .scope_does_not_exist_exception import (
    ScopeDoesNotExistException as ScopeDoesNotExistException,
)
from .software_token_mfa_not_found_exception import (
    SoftwareTokenMFANotFoundException as SoftwareTokenMFANotFoundException,
)
from .terms_exists_exception import TermsExistsException as TermsExistsException
from .tier_change_not_allowed_exception import (
    TierChangeNotAllowedException as TierChangeNotAllowedException,
)
from .too_many_failed_attempts_exception import (
    TooManyFailedAttemptsException as TooManyFailedAttemptsException,
)
from .too_many_requests_exception import (
    TooManyRequestsException as TooManyRequestsException,
)
from .unauthorized_exception import UnauthorizedException as UnauthorizedException
from .unexpected_lambda_exception import (
    UnexpectedLambdaException as UnexpectedLambdaException,
)
from .unsupported_identity_provider_exception import (
    UnsupportedIdentityProviderException as UnsupportedIdentityProviderException,
)
from .unsupported_operation_exception import (
    UnsupportedOperationException as UnsupportedOperationException,
)
from .unsupported_token_type_exception import (
    UnsupportedTokenTypeException as UnsupportedTokenTypeException,
)
from .unsupported_user_state_exception import (
    UnsupportedUserStateException as UnsupportedUserStateException,
)
from .user_import_in_progress_exception import (
    UserImportInProgressException as UserImportInProgressException,
)
from .user_lambda_validation_exception import (
    UserLambdaValidationException as UserLambdaValidationException,
)
from .user_not_confirmed_exception import (
    UserNotConfirmedException as UserNotConfirmedException,
)
from .user_not_found_exception import UserNotFoundException as UserNotFoundException
from .user_pool_add_on_not_enabled_exception import (
    UserPoolAddOnNotEnabledException as UserPoolAddOnNotEnabledException,
)
from .user_pool_tagging_exception import (
    UserPoolTaggingException as UserPoolTaggingException,
)
from .username_exists_exception import (
    UsernameExistsException as UsernameExistsException,
)
from .web_authn_challenge_not_found_exception import (
    WebAuthnChallengeNotFoundException as WebAuthnChallengeNotFoundException,
)
from .web_authn_client_mismatch_exception import (
    WebAuthnClientMismatchException as WebAuthnClientMismatchException,
)
from .web_authn_configuration_missing_exception import (
    WebAuthnConfigurationMissingException as WebAuthnConfigurationMissingException,
)
from .web_authn_credential_not_supported_exception import (
    WebAuthnCredentialNotSupportedException as WebAuthnCredentialNotSupportedException,
)
from .web_authn_not_enabled_exception import (
    WebAuthnNotEnabledException as WebAuthnNotEnabledException,
)
from .web_authn_origin_not_allowed_exception import (
    WebAuthnOriginNotAllowedException as WebAuthnOriginNotAllowedException,
)
from .web_authn_relying_party_mismatch_exception import (
    WebAuthnRelyingPartyMismatchException as WebAuthnRelyingPartyMismatchException,
)
