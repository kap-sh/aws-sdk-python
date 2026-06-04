from __future__ import annotations
from ._base import (
    DeserializationError as DeserializationError,
    SerializationError as SerializationError,
    ServiceError as ServiceError,
    UnknownServiceError as UnknownServiceError,
    WaiterFailedError as WaiterFailedError,
    WaiterTimeoutError as WaiterTimeoutError,
)
from .account_not_management_or_delegated_administrator_exception import (
    AccountNotManagementOrDelegatedAdministratorException as AccountNotManagementOrDelegatedAdministratorException,
)
from .caller_is_not_management_account_exception import (
    CallerIsNotManagementAccountException as CallerIsNotManagementAccountException,
)
from .concurrent_modification_exception import (
    ConcurrentModificationException as ConcurrentModificationException,
)
from .credential_report_expired_exception import (
    CredentialReportExpiredException as CredentialReportExpiredException,
)
from .credential_report_not_present_exception import (
    CredentialReportNotPresentException as CredentialReportNotPresentException,
)
from .credential_report_not_ready_exception import (
    CredentialReportNotReadyException as CredentialReportNotReadyException,
)
from .delete_conflict_exception import (
    DeleteConflictException as DeleteConflictException,
)
from .duplicate_certificate_exception import (
    DuplicateCertificateException as DuplicateCertificateException,
)
from .duplicate_ssh_public_key_exception import (
    DuplicateSSHPublicKeyException as DuplicateSSHPublicKeyException,
)
from .entity_already_exists_exception import (
    EntityAlreadyExistsException as EntityAlreadyExistsException,
)
from .entity_temporarily_unmodifiable_exception import (
    EntityTemporarilyUnmodifiableException as EntityTemporarilyUnmodifiableException,
)
from .feature_disabled_exception import (
    FeatureDisabledException as FeatureDisabledException,
)
from .feature_enabled_exception import (
    FeatureEnabledException as FeatureEnabledException,
)
from .invalid_authentication_code_exception import (
    InvalidAuthenticationCodeException as InvalidAuthenticationCodeException,
)
from .invalid_certificate_exception import (
    InvalidCertificateException as InvalidCertificateException,
)
from .invalid_input_exception import InvalidInputException as InvalidInputException
from .invalid_public_key_exception import (
    InvalidPublicKeyException as InvalidPublicKeyException,
)
from .invalid_user_type_exception import (
    InvalidUserTypeException as InvalidUserTypeException,
)
from .key_pair_mismatch_exception import (
    KeyPairMismatchException as KeyPairMismatchException,
)
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .malformed_certificate_exception import (
    MalformedCertificateException as MalformedCertificateException,
)
from .malformed_policy_document_exception import (
    MalformedPolicyDocumentException as MalformedPolicyDocumentException,
)
from .no_such_entity_exception import NoSuchEntityException as NoSuchEntityException
from .open_id_idp_communication_error_exception import (
    OpenIdIdpCommunicationErrorException as OpenIdIdpCommunicationErrorException,
)
from .organization_not_found_exception import (
    OrganizationNotFoundException as OrganizationNotFoundException,
)
from .organization_not_in_all_features_mode_exception import (
    OrganizationNotInAllFeaturesModeException as OrganizationNotInAllFeaturesModeException,
)
from .password_policy_violation_exception import (
    PasswordPolicyViolationException as PasswordPolicyViolationException,
)
from .policy_evaluation_exception import (
    PolicyEvaluationException as PolicyEvaluationException,
)
from .policy_not_attachable_exception import (
    PolicyNotAttachableException as PolicyNotAttachableException,
)
from .report_generation_limit_exceeded_exception import (
    ReportGenerationLimitExceededException as ReportGenerationLimitExceededException,
)
from .service_access_not_enabled_exception import (
    ServiceAccessNotEnabledException as ServiceAccessNotEnabledException,
)
from .service_failure_exception import (
    ServiceFailureException as ServiceFailureException,
)
from .service_not_supported_exception import (
    ServiceNotSupportedException as ServiceNotSupportedException,
)
from .unmodifiable_entity_exception import (
    UnmodifiableEntityException as UnmodifiableEntityException,
)
from .unrecognized_public_key_encoding_exception import (
    UnrecognizedPublicKeyEncodingException as UnrecognizedPublicKeyEncodingException,
)
