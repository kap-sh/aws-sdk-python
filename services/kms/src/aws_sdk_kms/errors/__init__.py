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
from .already_exists_exception import AlreadyExistsException as AlreadyExistsException
from .cloud_hsm_cluster_in_use_exception import (
    CloudHsmClusterInUseException as CloudHsmClusterInUseException,
)
from .cloud_hsm_cluster_invalid_configuration_exception import (
    CloudHsmClusterInvalidConfigurationException as CloudHsmClusterInvalidConfigurationException,
)
from .cloud_hsm_cluster_not_active_exception import (
    CloudHsmClusterNotActiveException as CloudHsmClusterNotActiveException,
)
from .cloud_hsm_cluster_not_found_exception import (
    CloudHsmClusterNotFoundException as CloudHsmClusterNotFoundException,
)
from .cloud_hsm_cluster_not_related_exception import (
    CloudHsmClusterNotRelatedException as CloudHsmClusterNotRelatedException,
)
from .conflict_exception import ConflictException as ConflictException
from .custom_key_store_has_cm_ks_exception import (
    CustomKeyStoreHasCMKsException as CustomKeyStoreHasCMKsException,
)
from .custom_key_store_invalid_state_exception import (
    CustomKeyStoreInvalidStateException as CustomKeyStoreInvalidStateException,
)
from .custom_key_store_name_in_use_exception import (
    CustomKeyStoreNameInUseException as CustomKeyStoreNameInUseException,
)
from .custom_key_store_not_found_exception import (
    CustomKeyStoreNotFoundException as CustomKeyStoreNotFoundException,
)
from .dependency_timeout_exception import (
    DependencyTimeoutException as DependencyTimeoutException,
)
from .disabled_exception import DisabledException as DisabledException
from .dry_run_operation_exception import (
    DryRunOperationException as DryRunOperationException,
)
from .expired_import_token_exception import (
    ExpiredImportTokenException as ExpiredImportTokenException,
)
from .incorrect_key_exception import IncorrectKeyException as IncorrectKeyException
from .incorrect_key_material_exception import (
    IncorrectKeyMaterialException as IncorrectKeyMaterialException,
)
from .incorrect_trust_anchor_exception import (
    IncorrectTrustAnchorException as IncorrectTrustAnchorException,
)
from .invalid_alias_name_exception import (
    InvalidAliasNameException as InvalidAliasNameException,
)
from .invalid_arn_exception import InvalidArnException as InvalidArnException
from .invalid_ciphertext_exception import (
    InvalidCiphertextException as InvalidCiphertextException,
)
from .invalid_grant_id_exception import (
    InvalidGrantIdException as InvalidGrantIdException,
)
from .invalid_grant_token_exception import (
    InvalidGrantTokenException as InvalidGrantTokenException,
)
from .invalid_import_token_exception import (
    InvalidImportTokenException as InvalidImportTokenException,
)
from .invalid_key_usage_exception import (
    InvalidKeyUsageException as InvalidKeyUsageException,
)
from .invalid_marker_exception import InvalidMarkerException as InvalidMarkerException
from .key_unavailable_exception import (
    KeyUnavailableException as KeyUnavailableException,
)
from .kms_internal_exception import KMSInternalException as KMSInternalException
from .kms_invalid_mac_exception import KMSInvalidMacException as KMSInvalidMacException
from .kms_invalid_signature_exception import (
    KMSInvalidSignatureException as KMSInvalidSignatureException,
)
from .kms_invalid_state_exception import (
    KMSInvalidStateException as KMSInvalidStateException,
)
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .malformed_policy_document_exception import (
    MalformedPolicyDocumentException as MalformedPolicyDocumentException,
)
from .not_found_exception import NotFoundException as NotFoundException
from .tag_exception import TagException as TagException
from .unsupported_operation_exception import (
    UnsupportedOperationException as UnsupportedOperationException,
)
from .xks_key_already_in_use_exception import (
    XksKeyAlreadyInUseException as XksKeyAlreadyInUseException,
)
from .xks_key_invalid_configuration_exception import (
    XksKeyInvalidConfigurationException as XksKeyInvalidConfigurationException,
)
from .xks_key_not_found_exception import (
    XksKeyNotFoundException as XksKeyNotFoundException,
)
from .xks_proxy_incorrect_authentication_credential_exception import (
    XksProxyIncorrectAuthenticationCredentialException as XksProxyIncorrectAuthenticationCredentialException,
)
from .xks_proxy_invalid_configuration_exception import (
    XksProxyInvalidConfigurationException as XksProxyInvalidConfigurationException,
)
from .xks_proxy_invalid_response_exception import (
    XksProxyInvalidResponseException as XksProxyInvalidResponseException,
)
from .xks_proxy_uri_endpoint_in_use_exception import (
    XksProxyUriEndpointInUseException as XksProxyUriEndpointInUseException,
)
from .xks_proxy_uri_in_use_exception import (
    XksProxyUriInUseException as XksProxyUriInUseException,
)
from .xks_proxy_uri_unreachable_exception import (
    XksProxyUriUnreachableException as XksProxyUriUnreachableException,
)
from .xks_proxy_vpc_endpoint_service_in_use_exception import (
    XksProxyVpcEndpointServiceInUseException as XksProxyVpcEndpointServiceInUseException,
)
from .xks_proxy_vpc_endpoint_service_invalid_configuration_exception import (
    XksProxyVpcEndpointServiceInvalidConfigurationException as XksProxyVpcEndpointServiceInvalidConfigurationException,
)
from .xks_proxy_vpc_endpoint_service_not_found_exception import (
    XksProxyVpcEndpointServiceNotFoundException as XksProxyVpcEndpointServiceNotFoundException,
)
