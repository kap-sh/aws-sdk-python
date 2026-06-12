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
from .access_denied import AccessDenied as AccessDenied
from .batch_too_large import BatchTooLarge as BatchTooLarge
from .cache_policy_already_exists import (
    CachePolicyAlreadyExists as CachePolicyAlreadyExists,
)
from .cache_policy_in_use import CachePolicyInUse as CachePolicyInUse
from .cannot_change_immutable_public_key_fields import (
    CannotChangeImmutablePublicKeyFields as CannotChangeImmutablePublicKeyFields,
)
from .cannot_delete_entity_while_in_use import (
    CannotDeleteEntityWhileInUse as CannotDeleteEntityWhileInUse,
)
from .cannot_update_entity_while_in_use import (
    CannotUpdateEntityWhileInUse as CannotUpdateEntityWhileInUse,
)
from .cloud_front_origin_access_identity_already_exists import (
    CloudFrontOriginAccessIdentityAlreadyExists as CloudFrontOriginAccessIdentityAlreadyExists,
)
from .cloud_front_origin_access_identity_in_use import (
    CloudFrontOriginAccessIdentityInUse as CloudFrontOriginAccessIdentityInUse,
)
from .cname_already_exists import CNAMEAlreadyExists as CNAMEAlreadyExists
from .continuous_deployment_policy_already_exists import (
    ContinuousDeploymentPolicyAlreadyExists as ContinuousDeploymentPolicyAlreadyExists,
)
from .continuous_deployment_policy_in_use import (
    ContinuousDeploymentPolicyInUse as ContinuousDeploymentPolicyInUse,
)
from .distribution_already_exists import (
    DistributionAlreadyExists as DistributionAlreadyExists,
)
from .distribution_not_disabled import (
    DistributionNotDisabled as DistributionNotDisabled,
)
from .entity_already_exists import EntityAlreadyExists as EntityAlreadyExists
from .entity_limit_exceeded import EntityLimitExceeded as EntityLimitExceeded
from .entity_not_found import EntityNotFound as EntityNotFound
from .entity_size_limit_exceeded import (
    EntitySizeLimitExceeded as EntitySizeLimitExceeded,
)
from .field_level_encryption_config_already_exists import (
    FieldLevelEncryptionConfigAlreadyExists as FieldLevelEncryptionConfigAlreadyExists,
)
from .field_level_encryption_config_in_use import (
    FieldLevelEncryptionConfigInUse as FieldLevelEncryptionConfigInUse,
)
from .field_level_encryption_profile_already_exists import (
    FieldLevelEncryptionProfileAlreadyExists as FieldLevelEncryptionProfileAlreadyExists,
)
from .field_level_encryption_profile_in_use import (
    FieldLevelEncryptionProfileInUse as FieldLevelEncryptionProfileInUse,
)
from .field_level_encryption_profile_size_exceeded import (
    FieldLevelEncryptionProfileSizeExceeded as FieldLevelEncryptionProfileSizeExceeded,
)
from .function_already_exists import FunctionAlreadyExists as FunctionAlreadyExists
from .function_in_use import FunctionInUse as FunctionInUse
from .function_size_limit_exceeded import (
    FunctionSizeLimitExceeded as FunctionSizeLimitExceeded,
)
from .illegal_delete import IllegalDelete as IllegalDelete
from .illegal_field_level_encryption_config_association_with_cache_behavior import (
    IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior as IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior,
)
from .illegal_origin_access_configuration import (
    IllegalOriginAccessConfiguration as IllegalOriginAccessConfiguration,
)
from .illegal_update import IllegalUpdate as IllegalUpdate
from .inconsistent_quantities import InconsistentQuantities as InconsistentQuantities
from .invalid_argument import InvalidArgument as InvalidArgument
from .invalid_association import InvalidAssociation as InvalidAssociation
from .invalid_default_root_object import (
    InvalidDefaultRootObject as InvalidDefaultRootObject,
)
from .invalid_domain_name_for_origin_access_control import (
    InvalidDomainNameForOriginAccessControl as InvalidDomainNameForOriginAccessControl,
)
from .invalid_error_code import InvalidErrorCode as InvalidErrorCode
from .invalid_forward_cookies import InvalidForwardCookies as InvalidForwardCookies
from .invalid_function_association import (
    InvalidFunctionAssociation as InvalidFunctionAssociation,
)
from .invalid_geo_restriction_parameter import (
    InvalidGeoRestrictionParameter as InvalidGeoRestrictionParameter,
)
from .invalid_headers_for_s3_origin import (
    InvalidHeadersForS3Origin as InvalidHeadersForS3Origin,
)
from .invalid_if_match_version import InvalidIfMatchVersion as InvalidIfMatchVersion
from .invalid_lambda_function_association import (
    InvalidLambdaFunctionAssociation as InvalidLambdaFunctionAssociation,
)
from .invalid_location_code import InvalidLocationCode as InvalidLocationCode
from .invalid_minimum_protocol_version import (
    InvalidMinimumProtocolVersion as InvalidMinimumProtocolVersion,
)
from .invalid_origin import InvalidOrigin as InvalidOrigin
from .invalid_origin_access_control import (
    InvalidOriginAccessControl as InvalidOriginAccessControl,
)
from .invalid_origin_access_identity import (
    InvalidOriginAccessIdentity as InvalidOriginAccessIdentity,
)
from .invalid_origin_keepalive_timeout import (
    InvalidOriginKeepaliveTimeout as InvalidOriginKeepaliveTimeout,
)
from .invalid_origin_read_timeout import (
    InvalidOriginReadTimeout as InvalidOriginReadTimeout,
)
from .invalid_protocol_settings import (
    InvalidProtocolSettings as InvalidProtocolSettings,
)
from .invalid_query_string_parameters import (
    InvalidQueryStringParameters as InvalidQueryStringParameters,
)
from .invalid_relative_path import InvalidRelativePath as InvalidRelativePath
from .invalid_required_protocol import (
    InvalidRequiredProtocol as InvalidRequiredProtocol,
)
from .invalid_response_code import InvalidResponseCode as InvalidResponseCode
from .invalid_tagging import InvalidTagging as InvalidTagging
from .invalid_ttl_order import InvalidTTLOrder as InvalidTTLOrder
from .invalid_viewer_certificate import (
    InvalidViewerCertificate as InvalidViewerCertificate,
)
from .invalid_web_acl_id import InvalidWebACLId as InvalidWebACLId
from .key_group_already_exists import KeyGroupAlreadyExists as KeyGroupAlreadyExists
from .missing_body import MissingBody as MissingBody
from .monitoring_subscription_already_exists import (
    MonitoringSubscriptionAlreadyExists as MonitoringSubscriptionAlreadyExists,
)
from .no_such_cache_policy import NoSuchCachePolicy as NoSuchCachePolicy
from .no_such_cloud_front_origin_access_identity import (
    NoSuchCloudFrontOriginAccessIdentity as NoSuchCloudFrontOriginAccessIdentity,
)
from .no_such_continuous_deployment_policy import (
    NoSuchContinuousDeploymentPolicy as NoSuchContinuousDeploymentPolicy,
)
from .no_such_distribution import NoSuchDistribution as NoSuchDistribution
from .no_such_field_level_encryption_config import (
    NoSuchFieldLevelEncryptionConfig as NoSuchFieldLevelEncryptionConfig,
)
from .no_such_field_level_encryption_profile import (
    NoSuchFieldLevelEncryptionProfile as NoSuchFieldLevelEncryptionProfile,
)
from .no_such_function_exists import NoSuchFunctionExists as NoSuchFunctionExists
from .no_such_invalidation import NoSuchInvalidation as NoSuchInvalidation
from .no_such_monitoring_subscription import (
    NoSuchMonitoringSubscription as NoSuchMonitoringSubscription,
)
from .no_such_origin import NoSuchOrigin as NoSuchOrigin
from .no_such_origin_access_control import (
    NoSuchOriginAccessControl as NoSuchOriginAccessControl,
)
from .no_such_origin_request_policy import (
    NoSuchOriginRequestPolicy as NoSuchOriginRequestPolicy,
)
from .no_such_public_key import NoSuchPublicKey as NoSuchPublicKey
from .no_such_realtime_log_config import (
    NoSuchRealtimeLogConfig as NoSuchRealtimeLogConfig,
)
from .no_such_resource import NoSuchResource as NoSuchResource
from .no_such_response_headers_policy import (
    NoSuchResponseHeadersPolicy as NoSuchResponseHeadersPolicy,
)
from .no_such_streaming_distribution import (
    NoSuchStreamingDistribution as NoSuchStreamingDistribution,
)
from .origin_access_control_already_exists import (
    OriginAccessControlAlreadyExists as OriginAccessControlAlreadyExists,
)
from .origin_access_control_in_use import (
    OriginAccessControlInUse as OriginAccessControlInUse,
)
from .origin_request_policy_already_exists import (
    OriginRequestPolicyAlreadyExists as OriginRequestPolicyAlreadyExists,
)
from .origin_request_policy_in_use import (
    OriginRequestPolicyInUse as OriginRequestPolicyInUse,
)
from .precondition_failed import PreconditionFailed as PreconditionFailed
from .public_key_already_exists import PublicKeyAlreadyExists as PublicKeyAlreadyExists
from .public_key_in_use import PublicKeyInUse as PublicKeyInUse
from .query_arg_profile_empty import QueryArgProfileEmpty as QueryArgProfileEmpty
from .realtime_log_config_already_exists import (
    RealtimeLogConfigAlreadyExists as RealtimeLogConfigAlreadyExists,
)
from .realtime_log_config_in_use import RealtimeLogConfigInUse as RealtimeLogConfigInUse
from .realtime_log_config_owner_mismatch import (
    RealtimeLogConfigOwnerMismatch as RealtimeLogConfigOwnerMismatch,
)
from .resource_in_use import ResourceInUse as ResourceInUse
from .resource_not_disabled import ResourceNotDisabled as ResourceNotDisabled
from .response_headers_policy_already_exists import (
    ResponseHeadersPolicyAlreadyExists as ResponseHeadersPolicyAlreadyExists,
)
from .response_headers_policy_in_use import (
    ResponseHeadersPolicyInUse as ResponseHeadersPolicyInUse,
)
from .staging_distribution_in_use import (
    StagingDistributionInUse as StagingDistributionInUse,
)
from .streaming_distribution_already_exists import (
    StreamingDistributionAlreadyExists as StreamingDistributionAlreadyExists,
)
from .streaming_distribution_not_disabled import (
    StreamingDistributionNotDisabled as StreamingDistributionNotDisabled,
)
from .test_function_failed import TestFunctionFailed as TestFunctionFailed
from .too_long_csp_in_response_headers_policy import (
    TooLongCSPInResponseHeadersPolicy as TooLongCSPInResponseHeadersPolicy,
)
from .too_many_cache_behaviors import TooManyCacheBehaviors as TooManyCacheBehaviors
from .too_many_cache_policies import TooManyCachePolicies as TooManyCachePolicies
from .too_many_certificates import TooManyCertificates as TooManyCertificates
from .too_many_cloud_front_origin_access_identities import (
    TooManyCloudFrontOriginAccessIdentities as TooManyCloudFrontOriginAccessIdentities,
)
from .too_many_continuous_deployment_policies import (
    TooManyContinuousDeploymentPolicies as TooManyContinuousDeploymentPolicies,
)
from .too_many_cookie_names_in_white_list import (
    TooManyCookieNamesInWhiteList as TooManyCookieNamesInWhiteList,
)
from .too_many_cookies_in_cache_policy import (
    TooManyCookiesInCachePolicy as TooManyCookiesInCachePolicy,
)
from .too_many_cookies_in_origin_request_policy import (
    TooManyCookiesInOriginRequestPolicy as TooManyCookiesInOriginRequestPolicy,
)
from .too_many_custom_headers_in_response_headers_policy import (
    TooManyCustomHeadersInResponseHeadersPolicy as TooManyCustomHeadersInResponseHeadersPolicy,
)
from .too_many_distribution_cnam_es import (
    TooManyDistributionCNAMEs as TooManyDistributionCNAMEs,
)
from .too_many_distributions import TooManyDistributions as TooManyDistributions
from .too_many_distributions_associated_to_cache_policy import (
    TooManyDistributionsAssociatedToCachePolicy as TooManyDistributionsAssociatedToCachePolicy,
)
from .too_many_distributions_associated_to_field_level_encryption_config import (
    TooManyDistributionsAssociatedToFieldLevelEncryptionConfig as TooManyDistributionsAssociatedToFieldLevelEncryptionConfig,
)
from .too_many_distributions_associated_to_key_group import (
    TooManyDistributionsAssociatedToKeyGroup as TooManyDistributionsAssociatedToKeyGroup,
)
from .too_many_distributions_associated_to_origin_access_control import (
    TooManyDistributionsAssociatedToOriginAccessControl as TooManyDistributionsAssociatedToOriginAccessControl,
)
from .too_many_distributions_associated_to_origin_request_policy import (
    TooManyDistributionsAssociatedToOriginRequestPolicy as TooManyDistributionsAssociatedToOriginRequestPolicy,
)
from .too_many_distributions_associated_to_response_headers_policy import (
    TooManyDistributionsAssociatedToResponseHeadersPolicy as TooManyDistributionsAssociatedToResponseHeadersPolicy,
)
from .too_many_distributions_with_function_associations import (
    TooManyDistributionsWithFunctionAssociations as TooManyDistributionsWithFunctionAssociations,
)
from .too_many_distributions_with_lambda_associations import (
    TooManyDistributionsWithLambdaAssociations as TooManyDistributionsWithLambdaAssociations,
)
from .too_many_distributions_with_single_function_arn import (
    TooManyDistributionsWithSingleFunctionARN as TooManyDistributionsWithSingleFunctionARN,
)
from .too_many_field_level_encryption_configs import (
    TooManyFieldLevelEncryptionConfigs as TooManyFieldLevelEncryptionConfigs,
)
from .too_many_field_level_encryption_content_type_profiles import (
    TooManyFieldLevelEncryptionContentTypeProfiles as TooManyFieldLevelEncryptionContentTypeProfiles,
)
from .too_many_field_level_encryption_encryption_entities import (
    TooManyFieldLevelEncryptionEncryptionEntities as TooManyFieldLevelEncryptionEncryptionEntities,
)
from .too_many_field_level_encryption_field_patterns import (
    TooManyFieldLevelEncryptionFieldPatterns as TooManyFieldLevelEncryptionFieldPatterns,
)
from .too_many_field_level_encryption_profiles import (
    TooManyFieldLevelEncryptionProfiles as TooManyFieldLevelEncryptionProfiles,
)
from .too_many_field_level_encryption_query_arg_profiles import (
    TooManyFieldLevelEncryptionQueryArgProfiles as TooManyFieldLevelEncryptionQueryArgProfiles,
)
from .too_many_function_associations import (
    TooManyFunctionAssociations as TooManyFunctionAssociations,
)
from .too_many_functions import TooManyFunctions as TooManyFunctions
from .too_many_headers_in_cache_policy import (
    TooManyHeadersInCachePolicy as TooManyHeadersInCachePolicy,
)
from .too_many_headers_in_forwarded_values import (
    TooManyHeadersInForwardedValues as TooManyHeadersInForwardedValues,
)
from .too_many_headers_in_origin_request_policy import (
    TooManyHeadersInOriginRequestPolicy as TooManyHeadersInOriginRequestPolicy,
)
from .too_many_invalidations_in_progress import (
    TooManyInvalidationsInProgress as TooManyInvalidationsInProgress,
)
from .too_many_key_groups import TooManyKeyGroups as TooManyKeyGroups
from .too_many_key_groups_associated_to_distribution import (
    TooManyKeyGroupsAssociatedToDistribution as TooManyKeyGroupsAssociatedToDistribution,
)
from .too_many_lambda_function_associations import (
    TooManyLambdaFunctionAssociations as TooManyLambdaFunctionAssociations,
)
from .too_many_origin_access_controls import (
    TooManyOriginAccessControls as TooManyOriginAccessControls,
)
from .too_many_origin_custom_headers import (
    TooManyOriginCustomHeaders as TooManyOriginCustomHeaders,
)
from .too_many_origin_groups_per_distribution import (
    TooManyOriginGroupsPerDistribution as TooManyOriginGroupsPerDistribution,
)
from .too_many_origin_request_policies import (
    TooManyOriginRequestPolicies as TooManyOriginRequestPolicies,
)
from .too_many_origins import TooManyOrigins as TooManyOrigins
from .too_many_public_keys import TooManyPublicKeys as TooManyPublicKeys
from .too_many_public_keys_in_key_group import (
    TooManyPublicKeysInKeyGroup as TooManyPublicKeysInKeyGroup,
)
from .too_many_query_string_parameters import (
    TooManyQueryStringParameters as TooManyQueryStringParameters,
)
from .too_many_query_strings_in_cache_policy import (
    TooManyQueryStringsInCachePolicy as TooManyQueryStringsInCachePolicy,
)
from .too_many_query_strings_in_origin_request_policy import (
    TooManyQueryStringsInOriginRequestPolicy as TooManyQueryStringsInOriginRequestPolicy,
)
from .too_many_realtime_log_configs import (
    TooManyRealtimeLogConfigs as TooManyRealtimeLogConfigs,
)
from .too_many_remove_headers_in_response_headers_policy import (
    TooManyRemoveHeadersInResponseHeadersPolicy as TooManyRemoveHeadersInResponseHeadersPolicy,
)
from .too_many_response_headers_policies import (
    TooManyResponseHeadersPolicies as TooManyResponseHeadersPolicies,
)
from .too_many_streaming_distribution_cnam_es import (
    TooManyStreamingDistributionCNAMEs as TooManyStreamingDistributionCNAMEs,
)
from .too_many_streaming_distributions import (
    TooManyStreamingDistributions as TooManyStreamingDistributions,
)
from .too_many_trusted_signers import TooManyTrustedSigners as TooManyTrustedSigners
from .trusted_key_group_does_not_exist import (
    TrustedKeyGroupDoesNotExist as TrustedKeyGroupDoesNotExist,
)
from .trusted_signer_does_not_exist import (
    TrustedSignerDoesNotExist as TrustedSignerDoesNotExist,
)
from .unsupported_operation import UnsupportedOperation as UnsupportedOperation
