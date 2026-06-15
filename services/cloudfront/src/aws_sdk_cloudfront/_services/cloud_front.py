"""Generated from Smithy shape ``com.amazonaws.cloudfront#Cloudfront2020_05_31``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_cloudfront._auth._signers
import aws_sdk_cloudfront._auth._sigv4
from aws_sdk_cloudfront._auth._identity import Credentials
from aws_sdk_cloudfront._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_cloudfront._auth._zapros_handler import AuthMiddleware
from aws_sdk_cloudfront._pagination import resolve_path as _resolve_path
from aws_sdk_cloudfront._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.alias_string
    import aws_sdk_cloudfront.types.anycast_ip_list_name
    import aws_sdk_cloudfront.types.associate_alias_request
    import aws_sdk_cloudfront.types.associate_distribution_tenant_web_acl_request
    import aws_sdk_cloudfront.types.associate_distribution_tenant_web_acl_result
    import aws_sdk_cloudfront.types.associate_distribution_web_acl_request
    import aws_sdk_cloudfront.types.associate_distribution_web_acl_result
    import aws_sdk_cloudfront.types.boolean
    import aws_sdk_cloudfront.types.ca_certificates_bundle_source
    import aws_sdk_cloudfront.types.cache_policy_config
    import aws_sdk_cloudfront.types.cache_policy_type
    import aws_sdk_cloudfront.types.cloud_front_origin_access_identity_config
    import aws_sdk_cloudfront.types.cloud_front_origin_access_identity_summary
    import aws_sdk_cloudfront.types.connection_function_summary
    import aws_sdk_cloudfront.types.connection_group_association_filter
    import aws_sdk_cloudfront.types.connection_group_summary
    import aws_sdk_cloudfront.types.connection_mode
    import aws_sdk_cloudfront.types.continuous_deployment_policy_config
    import aws_sdk_cloudfront.types.copy_distribution_request
    import aws_sdk_cloudfront.types.copy_distribution_result
    import aws_sdk_cloudfront.types.create_anycast_ip_list_request
    import aws_sdk_cloudfront.types.create_anycast_ip_list_result
    import aws_sdk_cloudfront.types.create_cache_policy_request
    import aws_sdk_cloudfront.types.create_cache_policy_result
    import aws_sdk_cloudfront.types.create_cloud_front_origin_access_identity_request
    import aws_sdk_cloudfront.types.create_cloud_front_origin_access_identity_result
    import aws_sdk_cloudfront.types.create_connection_function_request
    import aws_sdk_cloudfront.types.create_connection_function_result
    import aws_sdk_cloudfront.types.create_connection_group_request
    import aws_sdk_cloudfront.types.create_connection_group_result
    import aws_sdk_cloudfront.types.create_continuous_deployment_policy_request
    import aws_sdk_cloudfront.types.create_continuous_deployment_policy_result
    import aws_sdk_cloudfront.types.create_distribution_request
    import aws_sdk_cloudfront.types.create_distribution_result
    import aws_sdk_cloudfront.types.create_distribution_tenant_request
    import aws_sdk_cloudfront.types.create_distribution_tenant_result
    import aws_sdk_cloudfront.types.create_distribution_with_tags_request
    import aws_sdk_cloudfront.types.create_distribution_with_tags_result
    import aws_sdk_cloudfront.types.create_field_level_encryption_config_request
    import aws_sdk_cloudfront.types.create_field_level_encryption_config_result
    import aws_sdk_cloudfront.types.create_field_level_encryption_profile_request
    import aws_sdk_cloudfront.types.create_field_level_encryption_profile_result
    import aws_sdk_cloudfront.types.create_function_request
    import aws_sdk_cloudfront.types.create_function_result
    import aws_sdk_cloudfront.types.create_invalidation_for_distribution_tenant_request
    import aws_sdk_cloudfront.types.create_invalidation_for_distribution_tenant_result
    import aws_sdk_cloudfront.types.create_invalidation_request
    import aws_sdk_cloudfront.types.create_invalidation_result
    import aws_sdk_cloudfront.types.create_key_group_request
    import aws_sdk_cloudfront.types.create_key_group_result
    import aws_sdk_cloudfront.types.create_key_value_store_request
    import aws_sdk_cloudfront.types.create_key_value_store_result
    import aws_sdk_cloudfront.types.create_monitoring_subscription_request
    import aws_sdk_cloudfront.types.create_monitoring_subscription_result
    import aws_sdk_cloudfront.types.create_origin_access_control_request
    import aws_sdk_cloudfront.types.create_origin_access_control_result
    import aws_sdk_cloudfront.types.create_origin_request_policy_request
    import aws_sdk_cloudfront.types.create_origin_request_policy_result
    import aws_sdk_cloudfront.types.create_public_key_request
    import aws_sdk_cloudfront.types.create_public_key_result
    import aws_sdk_cloudfront.types.create_realtime_log_config_request
    import aws_sdk_cloudfront.types.create_realtime_log_config_result
    import aws_sdk_cloudfront.types.create_response_headers_policy_request
    import aws_sdk_cloudfront.types.create_response_headers_policy_result
    import aws_sdk_cloudfront.types.create_streaming_distribution_request
    import aws_sdk_cloudfront.types.create_streaming_distribution_result
    import aws_sdk_cloudfront.types.create_streaming_distribution_with_tags_request
    import aws_sdk_cloudfront.types.create_streaming_distribution_with_tags_result
    import aws_sdk_cloudfront.types.create_trust_store_request
    import aws_sdk_cloudfront.types.create_trust_store_result
    import aws_sdk_cloudfront.types.create_vpc_origin_request
    import aws_sdk_cloudfront.types.create_vpc_origin_result
    import aws_sdk_cloudfront.types.customizations
    import aws_sdk_cloudfront.types.delete_anycast_ip_list_request
    import aws_sdk_cloudfront.types.delete_cache_policy_request
    import aws_sdk_cloudfront.types.delete_cloud_front_origin_access_identity_request
    import aws_sdk_cloudfront.types.delete_connection_function_request
    import aws_sdk_cloudfront.types.delete_connection_group_request
    import aws_sdk_cloudfront.types.delete_continuous_deployment_policy_request
    import aws_sdk_cloudfront.types.delete_distribution_request
    import aws_sdk_cloudfront.types.delete_distribution_tenant_request
    import aws_sdk_cloudfront.types.delete_field_level_encryption_config_request
    import aws_sdk_cloudfront.types.delete_field_level_encryption_profile_request
    import aws_sdk_cloudfront.types.delete_function_request
    import aws_sdk_cloudfront.types.delete_key_group_request
    import aws_sdk_cloudfront.types.delete_key_value_store_request
    import aws_sdk_cloudfront.types.delete_monitoring_subscription_request
    import aws_sdk_cloudfront.types.delete_monitoring_subscription_result
    import aws_sdk_cloudfront.types.delete_origin_access_control_request
    import aws_sdk_cloudfront.types.delete_origin_request_policy_request
    import aws_sdk_cloudfront.types.delete_public_key_request
    import aws_sdk_cloudfront.types.delete_realtime_log_config_request
    import aws_sdk_cloudfront.types.delete_resource_policy_request
    import aws_sdk_cloudfront.types.delete_response_headers_policy_request
    import aws_sdk_cloudfront.types.delete_streaming_distribution_request
    import aws_sdk_cloudfront.types.delete_trust_store_request
    import aws_sdk_cloudfront.types.delete_vpc_origin_request
    import aws_sdk_cloudfront.types.delete_vpc_origin_result
    import aws_sdk_cloudfront.types.describe_connection_function_request
    import aws_sdk_cloudfront.types.describe_connection_function_result
    import aws_sdk_cloudfront.types.describe_function_request
    import aws_sdk_cloudfront.types.describe_function_result
    import aws_sdk_cloudfront.types.describe_key_value_store_request
    import aws_sdk_cloudfront.types.describe_key_value_store_result
    import aws_sdk_cloudfront.types.disassociate_distribution_tenant_web_acl_request
    import aws_sdk_cloudfront.types.disassociate_distribution_tenant_web_acl_result
    import aws_sdk_cloudfront.types.disassociate_distribution_web_acl_request
    import aws_sdk_cloudfront.types.disassociate_distribution_web_acl_result
    import aws_sdk_cloudfront.types.distribution_config
    import aws_sdk_cloudfront.types.distribution_config_with_tags
    import aws_sdk_cloudfront.types.distribution_id_string
    import aws_sdk_cloudfront.types.distribution_resource_id
    import aws_sdk_cloudfront.types.distribution_summary
    import aws_sdk_cloudfront.types.distribution_tenant_association_filter
    import aws_sdk_cloudfront.types.distribution_tenant_summary
    import aws_sdk_cloudfront.types.domain_conflict
    import aws_sdk_cloudfront.types.domain_list
    import aws_sdk_cloudfront.types.end_point_list
    import aws_sdk_cloudfront.types.field_level_encryption_config
    import aws_sdk_cloudfront.types.field_level_encryption_profile_config
    import aws_sdk_cloudfront.types.field_list
    import aws_sdk_cloudfront.types.function_blob
    import aws_sdk_cloudfront.types.function_config
    import aws_sdk_cloudfront.types.function_event_object
    import aws_sdk_cloudfront.types.function_name
    import aws_sdk_cloudfront.types.function_stage
    import aws_sdk_cloudfront.types.get_anycast_ip_list_request
    import aws_sdk_cloudfront.types.get_anycast_ip_list_result
    import aws_sdk_cloudfront.types.get_cache_policy_config_request
    import aws_sdk_cloudfront.types.get_cache_policy_config_result
    import aws_sdk_cloudfront.types.get_cache_policy_request
    import aws_sdk_cloudfront.types.get_cache_policy_result
    import aws_sdk_cloudfront.types.get_cloud_front_origin_access_identity_config_request
    import aws_sdk_cloudfront.types.get_cloud_front_origin_access_identity_config_result
    import aws_sdk_cloudfront.types.get_cloud_front_origin_access_identity_request
    import aws_sdk_cloudfront.types.get_cloud_front_origin_access_identity_result
    import aws_sdk_cloudfront.types.get_connection_function_request
    import aws_sdk_cloudfront.types.get_connection_function_result
    import aws_sdk_cloudfront.types.get_connection_group_by_routing_endpoint_request
    import aws_sdk_cloudfront.types.get_connection_group_by_routing_endpoint_result
    import aws_sdk_cloudfront.types.get_connection_group_request
    import aws_sdk_cloudfront.types.get_connection_group_result
    import aws_sdk_cloudfront.types.get_continuous_deployment_policy_config_request
    import aws_sdk_cloudfront.types.get_continuous_deployment_policy_config_result
    import aws_sdk_cloudfront.types.get_continuous_deployment_policy_request
    import aws_sdk_cloudfront.types.get_continuous_deployment_policy_result
    import aws_sdk_cloudfront.types.get_distribution_config_request
    import aws_sdk_cloudfront.types.get_distribution_config_result
    import aws_sdk_cloudfront.types.get_distribution_request
    import aws_sdk_cloudfront.types.get_distribution_result
    import aws_sdk_cloudfront.types.get_distribution_tenant_by_domain_request
    import aws_sdk_cloudfront.types.get_distribution_tenant_by_domain_result
    import aws_sdk_cloudfront.types.get_distribution_tenant_request
    import aws_sdk_cloudfront.types.get_distribution_tenant_result
    import aws_sdk_cloudfront.types.get_field_level_encryption_config_request
    import aws_sdk_cloudfront.types.get_field_level_encryption_config_result
    import aws_sdk_cloudfront.types.get_field_level_encryption_profile_config_request
    import aws_sdk_cloudfront.types.get_field_level_encryption_profile_config_result
    import aws_sdk_cloudfront.types.get_field_level_encryption_profile_request
    import aws_sdk_cloudfront.types.get_field_level_encryption_profile_result
    import aws_sdk_cloudfront.types.get_field_level_encryption_request
    import aws_sdk_cloudfront.types.get_field_level_encryption_result
    import aws_sdk_cloudfront.types.get_function_request
    import aws_sdk_cloudfront.types.get_function_result
    import aws_sdk_cloudfront.types.get_invalidation_for_distribution_tenant_request
    import aws_sdk_cloudfront.types.get_invalidation_for_distribution_tenant_result
    import aws_sdk_cloudfront.types.get_invalidation_request
    import aws_sdk_cloudfront.types.get_invalidation_result
    import aws_sdk_cloudfront.types.get_key_group_config_request
    import aws_sdk_cloudfront.types.get_key_group_config_result
    import aws_sdk_cloudfront.types.get_key_group_request
    import aws_sdk_cloudfront.types.get_key_group_result
    import aws_sdk_cloudfront.types.get_managed_certificate_details_request
    import aws_sdk_cloudfront.types.get_managed_certificate_details_result
    import aws_sdk_cloudfront.types.get_monitoring_subscription_request
    import aws_sdk_cloudfront.types.get_monitoring_subscription_result
    import aws_sdk_cloudfront.types.get_origin_access_control_config_request
    import aws_sdk_cloudfront.types.get_origin_access_control_config_result
    import aws_sdk_cloudfront.types.get_origin_access_control_request
    import aws_sdk_cloudfront.types.get_origin_access_control_result
    import aws_sdk_cloudfront.types.get_origin_request_policy_config_request
    import aws_sdk_cloudfront.types.get_origin_request_policy_config_result
    import aws_sdk_cloudfront.types.get_origin_request_policy_request
    import aws_sdk_cloudfront.types.get_origin_request_policy_result
    import aws_sdk_cloudfront.types.get_public_key_config_request
    import aws_sdk_cloudfront.types.get_public_key_config_result
    import aws_sdk_cloudfront.types.get_public_key_request
    import aws_sdk_cloudfront.types.get_public_key_result
    import aws_sdk_cloudfront.types.get_realtime_log_config_request
    import aws_sdk_cloudfront.types.get_realtime_log_config_result
    import aws_sdk_cloudfront.types.get_resource_policy_request
    import aws_sdk_cloudfront.types.get_resource_policy_result
    import aws_sdk_cloudfront.types.get_response_headers_policy_config_request
    import aws_sdk_cloudfront.types.get_response_headers_policy_config_result
    import aws_sdk_cloudfront.types.get_response_headers_policy_request
    import aws_sdk_cloudfront.types.get_response_headers_policy_result
    import aws_sdk_cloudfront.types.get_streaming_distribution_config_request
    import aws_sdk_cloudfront.types.get_streaming_distribution_config_result
    import aws_sdk_cloudfront.types.get_streaming_distribution_request
    import aws_sdk_cloudfront.types.get_streaming_distribution_result
    import aws_sdk_cloudfront.types.get_trust_store_request
    import aws_sdk_cloudfront.types.get_trust_store_result
    import aws_sdk_cloudfront.types.get_vpc_origin_request
    import aws_sdk_cloudfront.types.get_vpc_origin_result
    import aws_sdk_cloudfront.types.import_source
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.invalidation_batch
    import aws_sdk_cloudfront.types.invalidation_summary
    import aws_sdk_cloudfront.types.ip_address_type
    import aws_sdk_cloudfront.types.ipam_cidr_config_list
    import aws_sdk_cloudfront.types.key_group_config
    import aws_sdk_cloudfront.types.key_value_store
    import aws_sdk_cloudfront.types.key_value_store_comment
    import aws_sdk_cloudfront.types.key_value_store_name
    import aws_sdk_cloudfront.types.list_anycast_ip_lists_request
    import aws_sdk_cloudfront.types.list_anycast_ip_lists_result
    import aws_sdk_cloudfront.types.list_cache_policies_request
    import aws_sdk_cloudfront.types.list_cache_policies_result
    import aws_sdk_cloudfront.types.list_cloud_front_origin_access_identities_request
    import aws_sdk_cloudfront.types.list_cloud_front_origin_access_identities_result
    import aws_sdk_cloudfront.types.list_conflicting_aliases_max_items_integer
    import aws_sdk_cloudfront.types.list_conflicting_aliases_request
    import aws_sdk_cloudfront.types.list_conflicting_aliases_result
    import aws_sdk_cloudfront.types.list_connection_functions_request
    import aws_sdk_cloudfront.types.list_connection_functions_result
    import aws_sdk_cloudfront.types.list_connection_groups_request
    import aws_sdk_cloudfront.types.list_connection_groups_result
    import aws_sdk_cloudfront.types.list_continuous_deployment_policies_request
    import aws_sdk_cloudfront.types.list_continuous_deployment_policies_result
    import aws_sdk_cloudfront.types.list_distribution_tenants_by_customization_request
    import aws_sdk_cloudfront.types.list_distribution_tenants_by_customization_result
    import aws_sdk_cloudfront.types.list_distribution_tenants_request
    import aws_sdk_cloudfront.types.list_distribution_tenants_result
    import aws_sdk_cloudfront.types.list_distributions_by_anycast_ip_list_id_request
    import aws_sdk_cloudfront.types.list_distributions_by_anycast_ip_list_id_result
    import aws_sdk_cloudfront.types.list_distributions_by_cache_policy_id_request
    import aws_sdk_cloudfront.types.list_distributions_by_cache_policy_id_result
    import aws_sdk_cloudfront.types.list_distributions_by_connection_function_request
    import aws_sdk_cloudfront.types.list_distributions_by_connection_function_result
    import aws_sdk_cloudfront.types.list_distributions_by_connection_mode_request
    import aws_sdk_cloudfront.types.list_distributions_by_connection_mode_result
    import aws_sdk_cloudfront.types.list_distributions_by_key_group_request
    import aws_sdk_cloudfront.types.list_distributions_by_key_group_result
    import aws_sdk_cloudfront.types.list_distributions_by_origin_request_policy_id_request
    import aws_sdk_cloudfront.types.list_distributions_by_origin_request_policy_id_result
    import aws_sdk_cloudfront.types.list_distributions_by_owned_resource_request
    import aws_sdk_cloudfront.types.list_distributions_by_owned_resource_result
    import aws_sdk_cloudfront.types.list_distributions_by_realtime_log_config_request
    import aws_sdk_cloudfront.types.list_distributions_by_realtime_log_config_result
    import aws_sdk_cloudfront.types.list_distributions_by_response_headers_policy_id_request
    import aws_sdk_cloudfront.types.list_distributions_by_response_headers_policy_id_result
    import aws_sdk_cloudfront.types.list_distributions_by_trust_store_request
    import aws_sdk_cloudfront.types.list_distributions_by_trust_store_result
    import aws_sdk_cloudfront.types.list_distributions_by_vpc_origin_id_request
    import aws_sdk_cloudfront.types.list_distributions_by_vpc_origin_id_result
    import aws_sdk_cloudfront.types.list_distributions_by_web_acl_id_request
    import aws_sdk_cloudfront.types.list_distributions_by_web_acl_id_result
    import aws_sdk_cloudfront.types.list_distributions_request
    import aws_sdk_cloudfront.types.list_distributions_result
    import aws_sdk_cloudfront.types.list_domain_conflicts_request
    import aws_sdk_cloudfront.types.list_domain_conflicts_result
    import aws_sdk_cloudfront.types.list_field_level_encryption_configs_request
    import aws_sdk_cloudfront.types.list_field_level_encryption_configs_result
    import aws_sdk_cloudfront.types.list_field_level_encryption_profiles_request
    import aws_sdk_cloudfront.types.list_field_level_encryption_profiles_result
    import aws_sdk_cloudfront.types.list_functions_request
    import aws_sdk_cloudfront.types.list_functions_result
    import aws_sdk_cloudfront.types.list_invalidations_for_distribution_tenant_request
    import aws_sdk_cloudfront.types.list_invalidations_for_distribution_tenant_result
    import aws_sdk_cloudfront.types.list_invalidations_request
    import aws_sdk_cloudfront.types.list_invalidations_result
    import aws_sdk_cloudfront.types.list_key_groups_request
    import aws_sdk_cloudfront.types.list_key_groups_result
    import aws_sdk_cloudfront.types.list_key_value_stores_request
    import aws_sdk_cloudfront.types.list_key_value_stores_result
    import aws_sdk_cloudfront.types.list_origin_access_controls_request
    import aws_sdk_cloudfront.types.list_origin_access_controls_result
    import aws_sdk_cloudfront.types.list_origin_request_policies_request
    import aws_sdk_cloudfront.types.list_origin_request_policies_result
    import aws_sdk_cloudfront.types.list_public_keys_request
    import aws_sdk_cloudfront.types.list_public_keys_result
    import aws_sdk_cloudfront.types.list_realtime_log_configs_request
    import aws_sdk_cloudfront.types.list_realtime_log_configs_result
    import aws_sdk_cloudfront.types.list_response_headers_policies_request
    import aws_sdk_cloudfront.types.list_response_headers_policies_result
    import aws_sdk_cloudfront.types.list_streaming_distributions_request
    import aws_sdk_cloudfront.types.list_streaming_distributions_result
    import aws_sdk_cloudfront.types.list_tags_for_resource_request
    import aws_sdk_cloudfront.types.list_tags_for_resource_result
    import aws_sdk_cloudfront.types.list_trust_stores_request
    import aws_sdk_cloudfront.types.list_trust_stores_result
    import aws_sdk_cloudfront.types.list_vpc_origins_request
    import aws_sdk_cloudfront.types.list_vpc_origins_result
    import aws_sdk_cloudfront.types.long
    import aws_sdk_cloudfront.types.managed_certificate_request
    import aws_sdk_cloudfront.types.monitoring_subscription
    import aws_sdk_cloudfront.types.origin_access_control_config
    import aws_sdk_cloudfront.types.origin_access_control_summary
    import aws_sdk_cloudfront.types.origin_request_policy_config
    import aws_sdk_cloudfront.types.origin_request_policy_type
    import aws_sdk_cloudfront.types.parameters
    import aws_sdk_cloudfront.types.public_key_config
    import aws_sdk_cloudfront.types.public_key_summary
    import aws_sdk_cloudfront.types.publish_connection_function_request
    import aws_sdk_cloudfront.types.publish_connection_function_result
    import aws_sdk_cloudfront.types.publish_function_request
    import aws_sdk_cloudfront.types.publish_function_result
    import aws_sdk_cloudfront.types.put_resource_policy_request
    import aws_sdk_cloudfront.types.put_resource_policy_result
    import aws_sdk_cloudfront.types.resource_arn
    import aws_sdk_cloudfront.types.resource_id
    import aws_sdk_cloudfront.types.response_headers_policy_config
    import aws_sdk_cloudfront.types.response_headers_policy_type
    import aws_sdk_cloudfront.types.streaming_distribution_config
    import aws_sdk_cloudfront.types.streaming_distribution_config_with_tags
    import aws_sdk_cloudfront.types.streaming_distribution_summary
    import aws_sdk_cloudfront.types.string
    import aws_sdk_cloudfront.types.tag_keys
    import aws_sdk_cloudfront.types.tag_resource_request
    import aws_sdk_cloudfront.types.tags
    import aws_sdk_cloudfront.types.test_connection_function_request
    import aws_sdk_cloudfront.types.test_connection_function_result
    import aws_sdk_cloudfront.types.test_function_request
    import aws_sdk_cloudfront.types.test_function_result
    import aws_sdk_cloudfront.types.trust_store_summary
    import aws_sdk_cloudfront.types.untag_resource_request
    import aws_sdk_cloudfront.types.update_anycast_ip_list_request
    import aws_sdk_cloudfront.types.update_anycast_ip_list_result
    import aws_sdk_cloudfront.types.update_cache_policy_request
    import aws_sdk_cloudfront.types.update_cache_policy_result
    import aws_sdk_cloudfront.types.update_cloud_front_origin_access_identity_request
    import aws_sdk_cloudfront.types.update_cloud_front_origin_access_identity_result
    import aws_sdk_cloudfront.types.update_connection_function_request
    import aws_sdk_cloudfront.types.update_connection_function_result
    import aws_sdk_cloudfront.types.update_connection_group_request
    import aws_sdk_cloudfront.types.update_connection_group_result
    import aws_sdk_cloudfront.types.update_continuous_deployment_policy_request
    import aws_sdk_cloudfront.types.update_continuous_deployment_policy_result
    import aws_sdk_cloudfront.types.update_distribution_request
    import aws_sdk_cloudfront.types.update_distribution_result
    import aws_sdk_cloudfront.types.update_distribution_tenant_request
    import aws_sdk_cloudfront.types.update_distribution_tenant_result
    import aws_sdk_cloudfront.types.update_distribution_with_staging_config_request
    import aws_sdk_cloudfront.types.update_distribution_with_staging_config_result
    import aws_sdk_cloudfront.types.update_domain_association_request
    import aws_sdk_cloudfront.types.update_domain_association_result
    import aws_sdk_cloudfront.types.update_field_level_encryption_config_request
    import aws_sdk_cloudfront.types.update_field_level_encryption_config_result
    import aws_sdk_cloudfront.types.update_field_level_encryption_profile_request
    import aws_sdk_cloudfront.types.update_field_level_encryption_profile_result
    import aws_sdk_cloudfront.types.update_function_request
    import aws_sdk_cloudfront.types.update_function_result
    import aws_sdk_cloudfront.types.update_key_group_request
    import aws_sdk_cloudfront.types.update_key_group_result
    import aws_sdk_cloudfront.types.update_key_value_store_request
    import aws_sdk_cloudfront.types.update_key_value_store_result
    import aws_sdk_cloudfront.types.update_origin_access_control_request
    import aws_sdk_cloudfront.types.update_origin_access_control_result
    import aws_sdk_cloudfront.types.update_origin_request_policy_request
    import aws_sdk_cloudfront.types.update_origin_request_policy_result
    import aws_sdk_cloudfront.types.update_public_key_request
    import aws_sdk_cloudfront.types.update_public_key_result
    import aws_sdk_cloudfront.types.update_realtime_log_config_request
    import aws_sdk_cloudfront.types.update_realtime_log_config_result
    import aws_sdk_cloudfront.types.update_response_headers_policy_request
    import aws_sdk_cloudfront.types.update_response_headers_policy_result
    import aws_sdk_cloudfront.types.update_streaming_distribution_request
    import aws_sdk_cloudfront.types.update_streaming_distribution_result
    import aws_sdk_cloudfront.types.update_trust_store_request
    import aws_sdk_cloudfront.types.update_trust_store_result
    import aws_sdk_cloudfront.types.update_vpc_origin_request
    import aws_sdk_cloudfront.types.update_vpc_origin_result
    import aws_sdk_cloudfront.types.verify_dns_configuration_request
    import aws_sdk_cloudfront.types.verify_dns_configuration_result
    import aws_sdk_cloudfront.types.vpc_origin_endpoint_config


class CloudFrontClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


def ensure_sync_iterator(it: Iterator[bytes] | bytes) -> Iterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        for chunk in it:
            yield chunk


class CloudFrontClient:
    """A client for the ``CloudFront`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self._config = CloudFrontClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[CloudFrontClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: CloudFrontClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self._config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def associate_alias(
        self,
        target_distribution_id: "aws_sdk_cloudfront.types.string.string",
        alias: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> None:
        r"""<note> <p>The <code>AssociateAlias</code> API operation only supports standard distributions. To move domains between distribution tenants and/or standard distributions, we recommend that you use the <a href=\"https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateDomainAssociation.html\">UpdateDomainAssociation</a> API operation instead.</p> </note> <p>Associates an alias with a CloudFront standard distribution. An alias is commonly known as a custom domain or vanity domain. It can also be called a CNAME or alternate domain name.</p> <p>With this operation, you can move an alias that's already used for a standard distribution to a different standard distribution. This prevents the downtime that could occur if you first remove the alias from one standard distribution and then separately add the alias to another standard distribution.</p> <p>To use this operation, specify the alias and the ID of the target standard distribution.</p> <p>For more information, including how to set up the target standard distribution, prerequisites that you must complete, and other restrictions, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html#alternate-domain-names-move\">Moving an alternate domain name to a different standard distribution or distribution tenant</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            target_distribution_id: <p>The ID of the standard distribution that you're associating the alias with.</p>
            alias: <p>The alias (also known as a CNAME) to add to the target standard distribution.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.associate_alias_request.AssociateAliasRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.associate_alias

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.associate_alias.associate_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.associate_alias_request.AssociateAliasRequest = {}  # type: ignore[typeddict-item]
        input_["target_distribution_id"] = target_distribution_id
        input_["alias"] = alias

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def associate_distribution_tenant_web_acl(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        web_acl_arn: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> "aws_sdk_cloudfront.types.associate_distribution_tenant_web_acl_result.AssociateDistributionTenantWebACLResult":
        """<p>Associates the WAF web ACL with a distribution tenant.</p>

        Args:
            id: <p>The ID of the distribution tenant.</p>
            web_acl_arn: <p>The Amazon Resource Name (ARN) of the WAF web ACL to associate.</p>
            if_match: <p>The current <code>ETag</code> of the distribution tenant. This value is returned in the response of the <code>GetDistributionTenant</code> API operation.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.associate_distribution_tenant_web_acl_request.AssociateDistributionTenantWebACLRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.associate_distribution_tenant_web_acl_result.AssociateDistributionTenantWebACLResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.associate_distribution_tenant_web_acl

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.associate_distribution_tenant_web_acl.associate_distribution_tenant_web_acl(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.associate_distribution_tenant_web_acl_request.AssociateDistributionTenantWebACLRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["web_acl_arn"] = web_acl_arn
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def associate_distribution_web_acl(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        web_acl_arn: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> "aws_sdk_cloudfront.types.associate_distribution_web_acl_result.AssociateDistributionWebACLResult":
        """<p>Associates the WAF web ACL with a distribution.</p>

        Args:
            id: <p>The ID of the distribution.</p>
            web_acl_arn: <p>The Amazon Resource Name (ARN) of the WAF web ACL to associate.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the distribution that you're associating with the WAF web ACL.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.associate_distribution_web_acl_request.AssociateDistributionWebACLRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.associate_distribution_web_acl_result.AssociateDistributionWebACLResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.associate_distribution_web_acl

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.associate_distribution_web_acl.associate_distribution_web_acl(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.associate_distribution_web_acl_request.AssociateDistributionWebACLRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["web_acl_arn"] = web_acl_arn
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def copy_distribution(
        self,
        primary_distribution_id: "aws_sdk_cloudfront.types.string.string",
        caller_reference: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        staging: Optional["aws_sdk_cloudfront.types.boolean.boolean"] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        enabled: Optional["aws_sdk_cloudfront.types.boolean.boolean"] = None,
    ) -> "aws_sdk_cloudfront.types.copy_distribution_result.CopyDistributionResult":
        r"""<p>Creates a staging distribution using the configuration of the provided primary distribution. A staging distribution is a copy of an existing distribution (called the primary distribution) that you can use in a continuous deployment workflow.</p> <p>After you create a staging distribution, you can use <code>UpdateDistribution</code> to modify the staging distribution's configuration. Then you can use <code>CreateContinuousDeploymentPolicy</code> to incrementally move traffic to the staging distribution.</p> <p>This API operation requires the following IAM permissions:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetDistribution.html\">GetDistribution</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateDistribution.html\">CreateDistribution</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CopyDistribution.html\">CopyDistribution</a> </p> </li> </ul>

        Args:
            primary_distribution_id: <p>The identifier of the primary distribution whose configuration you are copying. To get a distribution ID, use <code>ListDistributions</code>.</p>
            staging: <p>The type of distribution that your primary distribution will be copied to. The only valid value is <code>True</code>, indicating that you are copying to a staging distribution.</p>
            if_match: <p>The version identifier of the primary distribution whose configuration you are copying. This is the <code>ETag</code> value returned in the response to <code>GetDistribution</code> and <code>GetDistributionConfig</code>.</p>
            caller_reference: <p>A value that uniquely identifies a request to create a resource. This helps to prevent CloudFront from creating a duplicate resource if you accidentally resubmit an identical request.</p>
            enabled: <p>A Boolean flag to specify the state of the staging distribution when it's created. When you set this value to <code>True</code>, the staging distribution is enabled. When you set this value to <code>False</code>, the staging distribution is disabled.</p> <p>If you omit this field, the default value is <code>True</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.copy_distribution_request.CopyDistributionRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.copy_distribution_result.CopyDistributionResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.copy_distribution

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.copy_distribution.copy_distribution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.copy_distribution_request.CopyDistributionRequest = {}  # type: ignore[typeddict-item]
        input_["primary_distribution_id"] = primary_distribution_id
        if staging is not None:
            input_["staging"] = staging
        if if_match is not None:
            input_["if_match"] = if_match
        input_["caller_reference"] = caller_reference
        if enabled is not None:
            input_["enabled"] = enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_anycast_ip_list(
        self,
        name: "aws_sdk_cloudfront.types.anycast_ip_list_name.AnycastIpListName",
        ip_count: "aws_sdk_cloudfront.types.integer.integer",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        tags: Optional["aws_sdk_cloudfront.types.tags.Tags"] = None,
        ip_address_type: Optional[
            "aws_sdk_cloudfront.types.ip_address_type.IpAddressType"
        ] = None,
        ipam_cidr_configs: Optional[
            "aws_sdk_cloudfront.types.ipam_cidr_config_list.IpamCidrConfigList"
        ] = None,
    ) -> "aws_sdk_cloudfront.types.create_anycast_ip_list_result.CreateAnycastIpListResult":
        """<p>Creates an Anycast static IP list.</p>

        Args:
            name: <p>Name of the Anycast static IP list.</p>
            ip_count: <p>The number of static IP addresses that are allocated to the Anycast static IP list. Valid values: 21 or 3.</p>
            ip_address_type: <p>The IP address type for the Anycast static IP list. You can specify one of the following options:</p> <ul> <li> <p> <code>ipv4</code> only</p> </li> <li> <p> <code>ipv6</code> only </p> </li> <li> <p> <code>dualstack</code> - Allocate a list of both IPv4 and IPv6 addresses</p> </li> </ul>
            ipam_cidr_configs: <p> A list of IPAM CIDR configurations that specify the IP address ranges and IPAM pool settings for creating the Anycast static IP list. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.create_anycast_ip_list_request.CreateAnycastIpListRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.create_anycast_ip_list_result.CreateAnycastIpListResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_anycast_ip_list

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_anycast_ip_list.create_anycast_ip_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.create_anycast_ip_list_request.CreateAnycastIpListRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["ip_count"] = ip_count
        if tags is not None:
            input_["tags"] = tags
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if ipam_cidr_configs is not None:
            input_["ipam_cidr_configs"] = ipam_cidr_configs

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_cache_policy(
        self,
        cache_policy_config: "aws_sdk_cloudfront.types.cache_policy_config.CachePolicyConfig",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.create_cache_policy_result.CreateCachePolicyResult":
        r"""<p>Creates a cache policy.</p> <p>After you create a cache policy, you can attach it to one or more cache behaviors. When it's attached to a cache behavior, the cache policy determines the following:</p> <ul> <li> <p>The values that CloudFront includes in the <i>cache key</i>. These values can include HTTP headers, cookies, and URL query strings. CloudFront uses the cache key to find an object in its cache that it can return to the viewer.</p> </li> <li> <p>The default, minimum, and maximum time to live (TTL) values that you want objects to stay in the CloudFront cache.</p> <important> <p>If your minimum TTL is greater than 0, CloudFront will cache content for at least the duration specified in the cache policy's minimum TTL, even if the <code>Cache-Control: no-cache</code>, <code>no-store</code>, or <code>private</code> directives are present in the origin headers.</p> </important> </li> </ul> <p>The headers, cookies, and query strings that are included in the cache key are also included in requests that CloudFront sends to the origin. CloudFront sends a request when it can't find an object in its cache that matches the request's cache key. If you want to send values to the origin but <i>not</i> include them in the cache key, use <code>OriginRequestPolicy</code>.</p> <p>For more information about cache policies, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html\">Controlling the cache key</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            cache_policy_config: <p>A cache policy configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.create_cache_policy_request.CreateCachePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.create_cache_policy_result.CreateCachePolicyResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_cache_policy

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_cache_policy.create_cache_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.create_cache_policy_request.CreateCachePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["cache_policy_config"] = cache_policy_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_cloud_front_origin_access_identity(
        self,
        cloud_front_origin_access_identity_config: "aws_sdk_cloudfront.types.cloud_front_origin_access_identity_config.CloudFrontOriginAccessIdentityConfig",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.create_cloud_front_origin_access_identity_result.CreateCloudFrontOriginAccessIdentityResult":
        r"""<p>Creates a new origin access identity. If you're using Amazon S3 for your origin, you can use an origin access identity to require users to access your content using a CloudFront URL instead of the Amazon S3 URL. For more information about how to use origin access identities, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html\">Serving Private Content through CloudFront</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            cloud_front_origin_access_identity_config: <p>The current configuration information for the identity.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.create_cloud_front_origin_access_identity_request.CreateCloudFrontOriginAccessIdentityRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.create_cloud_front_origin_access_identity_result.CreateCloudFrontOriginAccessIdentityResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_cloud_front_origin_access_identity

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_cloud_front_origin_access_identity.create_cloud_front_origin_access_identity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.create_cloud_front_origin_access_identity_request.CreateCloudFrontOriginAccessIdentityRequest = {}  # type: ignore[typeddict-item]
        input_["cloud_front_origin_access_identity_config"] = (
            cloud_front_origin_access_identity_config
        )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_connection_function(
        self,
        name: "aws_sdk_cloudfront.types.function_name.FunctionName",
        connection_function_config: "aws_sdk_cloudfront.types.function_config.FunctionConfig",
        connection_function_code: "aws_sdk_cloudfront.types.function_blob.FunctionBlob",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        tags: Optional["aws_sdk_cloudfront.types.tags.Tags"] = None,
    ) -> "aws_sdk_cloudfront.types.create_connection_function_result.CreateConnectionFunctionResult":
        """<p>Creates a connection function.</p>

        Args:
            name: <p>A name for the connection function.</p>
            connection_function_code: <p>The code for the connection function.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.create_connection_function_request.CreateConnectionFunctionRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.create_connection_function_result.CreateConnectionFunctionResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_connection_function

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_connection_function.create_connection_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.create_connection_function_request.CreateConnectionFunctionRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["connection_function_config"] = connection_function_config
        input_["connection_function_code"] = connection_function_code
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_connection_group(
        self,
        name: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        ipv6_enabled: Optional["aws_sdk_cloudfront.types.boolean.boolean"] = None,
        tags: Optional["aws_sdk_cloudfront.types.tags.Tags"] = None,
        anycast_ip_list_id: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        enabled: Optional["aws_sdk_cloudfront.types.boolean.boolean"] = None,
    ) -> "aws_sdk_cloudfront.types.create_connection_group_result.CreateConnectionGroupResult":
        r"""<p>Creates a connection group.</p>

        Args:
            name: <p>The name of the connection group. Enter a friendly identifier that is unique within your Amazon Web Services account. This name can't be updated after you create the connection group.</p>
            ipv6_enabled: <p>Enable IPv6 for the connection group. The default is <code>true</code>. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesEnableIPv6\">Enable IPv6</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>
            anycast_ip_list_id: <p>The ID of the Anycast static IP list.</p>
            enabled: <p>Enable the connection group.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.create_connection_group_request.CreateConnectionGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.create_connection_group_result.CreateConnectionGroupResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_connection_group

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_connection_group.create_connection_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.create_connection_group_request.CreateConnectionGroupRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if ipv6_enabled is not None:
            input_["ipv6_enabled"] = ipv6_enabled
        if tags is not None:
            input_["tags"] = tags
        if anycast_ip_list_id is not None:
            input_["anycast_ip_list_id"] = anycast_ip_list_id
        if enabled is not None:
            input_["enabled"] = enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_continuous_deployment_policy(
        self,
        continuous_deployment_policy_config: "aws_sdk_cloudfront.types.continuous_deployment_policy_config.ContinuousDeploymentPolicyConfig",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.create_continuous_deployment_policy_result.CreateContinuousDeploymentPolicyResult":
        """<p>Creates a continuous deployment policy that distributes traffic for a custom domain name to two different CloudFront distributions.</p> <p>To use a continuous deployment policy, first use <code>CopyDistribution</code> to create a staging distribution, then use <code>UpdateDistribution</code> to modify the staging distribution's configuration.</p> <p>After you create and update a staging distribution, you can use a continuous deployment policy to incrementally move traffic to the staging distribution. This workflow enables you to test changes to a distribution's configuration before moving all of your domain's production traffic to the new configuration.</p>

        Args:
            continuous_deployment_policy_config: <p>Contains the configuration for a continuous deployment policy.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.create_continuous_deployment_policy_request.CreateContinuousDeploymentPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.create_continuous_deployment_policy_result.CreateContinuousDeploymentPolicyResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_continuous_deployment_policy

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_continuous_deployment_policy.create_continuous_deployment_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.create_continuous_deployment_policy_request.CreateContinuousDeploymentPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["continuous_deployment_policy_config"] = (
            continuous_deployment_policy_config
        )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_distribution(
        self,
        distribution_config: "aws_sdk_cloudfront.types.distribution_config.DistributionConfig",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.create_distribution_result.CreateDistributionResult":
        """<p>Creates a CloudFront distribution.</p>

        Args:
            distribution_config: <p>The distribution's configuration information.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.create_distribution_request.CreateDistributionRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.create_distribution_result.CreateDistributionResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_distribution

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_distribution.create_distribution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.create_distribution_request.CreateDistributionRequest = {}  # type: ignore[typeddict-item]
        input_["distribution_config"] = distribution_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_distribution_tenant(
        self,
        distribution_id: "aws_sdk_cloudfront.types.string.string",
        name: "aws_sdk_cloudfront.types.string.string",
        domains: "aws_sdk_cloudfront.types.domain_list.DomainList",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        tags: Optional["aws_sdk_cloudfront.types.tags.Tags"] = None,
        customizations: Optional[
            "aws_sdk_cloudfront.types.customizations.Customizations"
        ] = None,
        parameters: Optional["aws_sdk_cloudfront.types.parameters.Parameters"] = None,
        connection_group_id: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        managed_certificate_request: Optional[
            "aws_sdk_cloudfront.types.managed_certificate_request.ManagedCertificateRequest"
        ] = None,
        enabled: Optional["aws_sdk_cloudfront.types.boolean.boolean"] = None,
    ) -> "aws_sdk_cloudfront.types.create_distribution_tenant_result.CreateDistributionTenantResult":
        """<p>Creates a distribution tenant.</p>

        Args:
            distribution_id: <p>The ID of the multi-tenant distribution to use for creating the distribution tenant.</p>
            name: <p>The name of the distribution tenant. Enter a friendly identifier that is unique within your Amazon Web Services account. This name can't be updated after you create the distribution tenant.</p>
            domains: <p>The domains associated with the distribution tenant. You must specify at least one domain in the request.</p>
            customizations: <p>Customizations for the distribution tenant. For each distribution tenant, you can specify the geographic restrictions, and the Amazon Resource Names (ARNs) for the ACM certificate and WAF web ACL. These are specific values that you can override or disable from the multi-tenant distribution that was used to create the distribution tenant.</p>
            parameters: <p>A list of parameter values to add to the resource. A parameter is specified as a key-value pair. A valid parameter value must exist for any parameter that is marked as required in the multi-tenant distribution.</p>
            connection_group_id: <p>The ID of the connection group to associate with the distribution tenant.</p>
            managed_certificate_request: <p>The configuration for the CloudFront managed ACM certificate request.</p>
            enabled: <p>Indicates whether the distribution tenant should be enabled when created. If the distribution tenant is disabled, the distribution tenant won't serve traffic.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.create_distribution_tenant_request.CreateDistributionTenantRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.create_distribution_tenant_result.CreateDistributionTenantResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_distribution_tenant

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_distribution_tenant.create_distribution_tenant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.create_distribution_tenant_request.CreateDistributionTenantRequest = {}  # type: ignore[typeddict-item]
        input_["distribution_id"] = distribution_id
        input_["name"] = name
        input_["domains"] = domains
        if tags is not None:
            input_["tags"] = tags
        if customizations is not None:
            input_["customizations"] = customizations
        if parameters is not None:
            input_["parameters"] = parameters
        if connection_group_id is not None:
            input_["connection_group_id"] = connection_group_id
        if managed_certificate_request is not None:
            input_["managed_certificate_request"] = managed_certificate_request
        if enabled is not None:
            input_["enabled"] = enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_distribution_with_tags(
        self,
        distribution_config_with_tags: "aws_sdk_cloudfront.types.distribution_config_with_tags.DistributionConfigWithTags",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.create_distribution_with_tags_result.CreateDistributionWithTagsResult":
        r"""<p>Create a new distribution with tags. This API operation requires the following IAM permissions:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateDistribution.html\">CreateDistribution</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_TagResource.html\">TagResource</a> </p> </li> </ul>

        Args:
            distribution_config_with_tags: <p>The distribution's configuration information.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.create_distribution_with_tags_request.CreateDistributionWithTagsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.create_distribution_with_tags_result.CreateDistributionWithTagsResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_distribution_with_tags

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_distribution_with_tags.create_distribution_with_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.create_distribution_with_tags_request.CreateDistributionWithTagsRequest = {}  # type: ignore[typeddict-item]
        input_["distribution_config_with_tags"] = distribution_config_with_tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_field_level_encryption_config(
        self,
        field_level_encryption_config: "aws_sdk_cloudfront.types.field_level_encryption_config.FieldLevelEncryptionConfig",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.create_field_level_encryption_config_result.CreateFieldLevelEncryptionConfigResult":
        """<p>Create a new field-level encryption configuration.</p>

        Args:
            field_level_encryption_config: <p>The request to create a new field-level encryption configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.create_field_level_encryption_config_request.CreateFieldLevelEncryptionConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.create_field_level_encryption_config_result.CreateFieldLevelEncryptionConfigResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_field_level_encryption_config

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_field_level_encryption_config.create_field_level_encryption_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.create_field_level_encryption_config_request.CreateFieldLevelEncryptionConfigRequest = {}  # type: ignore[typeddict-item]
        input_["field_level_encryption_config"] = field_level_encryption_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_field_level_encryption_profile(
        self,
        field_level_encryption_profile_config: "aws_sdk_cloudfront.types.field_level_encryption_profile_config.FieldLevelEncryptionProfileConfig",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.create_field_level_encryption_profile_result.CreateFieldLevelEncryptionProfileResult":
        """<p>Create a field-level encryption profile.</p>

        Args:
            field_level_encryption_profile_config: <p>The request to create a field-level encryption profile.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.create_field_level_encryption_profile_request.CreateFieldLevelEncryptionProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.create_field_level_encryption_profile_result.CreateFieldLevelEncryptionProfileResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_field_level_encryption_profile

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_field_level_encryption_profile.create_field_level_encryption_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.create_field_level_encryption_profile_request.CreateFieldLevelEncryptionProfileRequest = {}  # type: ignore[typeddict-item]
        input_["field_level_encryption_profile_config"] = (
            field_level_encryption_profile_config
        )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_function(
        self,
        name: "aws_sdk_cloudfront.types.function_name.FunctionName",
        function_config: "aws_sdk_cloudfront.types.function_config.FunctionConfig",
        function_code: "aws_sdk_cloudfront.types.function_blob.FunctionBlob",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        tags: Optional["aws_sdk_cloudfront.types.tags.Tags"] = None,
    ) -> "aws_sdk_cloudfront.types.create_function_result.CreateFunctionResult":
        r"""<p>Creates a CloudFront function.</p> <p>To create a function, you provide the function code and some configuration information about the function. The response contains an Amazon Resource Name (ARN) that uniquely identifies the function.</p> <p>When you create a function, it's in the <code>DEVELOPMENT</code> stage. In this stage, you can test the function with <code>TestFunction</code>, and update it with <code>UpdateFunction</code>.</p> <p>When you're ready to use your function with a CloudFront distribution, use <code>PublishFunction</code> to copy the function from the <code>DEVELOPMENT</code> stage to <code>LIVE</code>. When it's live, you can attach the function to a distribution's cache behavior, using the function's ARN.</p>

        Args:
            name: <p>A name to identify the function.</p>
            function_config: <p>Configuration information about the function, including an optional comment and the function's runtime.</p>
            function_code: <p>The function code. For more information about writing a CloudFront function, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/writing-function-code.html\">Writing function code for CloudFront Functions</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Examples:
            To create a function
            Use the following command to create a function.

            >>> client.create_function(name='my-function-name', function_config={'Comment': 'my-function-comment', 'Runtime': 'cloudfront-js-2.0', 'KeyValueStoreAssociations': {'Quantity': 1, 'Items': [{'KeyValueStoreARN': 'arn:aws:cloudfront::123456789012:key-value-store/54947df8-0e9e-4471-a2f9-9af509fb5889'}]}}, function_code='function-code.js')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.create_function_request.CreateFunctionRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.create_function_result.CreateFunctionResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_function

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_function.create_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.create_function_request.CreateFunctionRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["function_config"] = function_config
        input_["function_code"] = function_code
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_invalidation(
        self,
        distribution_id: "aws_sdk_cloudfront.types.string.string",
        invalidation_batch: "aws_sdk_cloudfront.types.invalidation_batch.InvalidationBatch",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.create_invalidation_result.CreateInvalidationResult":
        r"""<p>Create a new invalidation. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html\">Invalidating files</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            distribution_id: <p>The distribution's id.</p>
            invalidation_batch: <p>The batch information for the invalidation.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.create_invalidation_request.CreateInvalidationRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.create_invalidation_result.CreateInvalidationResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_invalidation

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_invalidation.create_invalidation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.create_invalidation_request.CreateInvalidationRequest = {}  # type: ignore[typeddict-item]
        input_["distribution_id"] = distribution_id
        input_["invalidation_batch"] = invalidation_batch

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_invalidation_for_distribution_tenant(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        invalidation_batch: "aws_sdk_cloudfront.types.invalidation_batch.InvalidationBatch",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.create_invalidation_for_distribution_tenant_result.CreateInvalidationForDistributionTenantResult":
        r"""<p>Creates an invalidation for a distribution tenant. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html\">Invalidating files</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            id: <p>The ID of the distribution tenant.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.create_invalidation_for_distribution_tenant_request.CreateInvalidationForDistributionTenantRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.create_invalidation_for_distribution_tenant_result.CreateInvalidationForDistributionTenantResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_invalidation_for_distribution_tenant

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_invalidation_for_distribution_tenant.create_invalidation_for_distribution_tenant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.create_invalidation_for_distribution_tenant_request.CreateInvalidationForDistributionTenantRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["invalidation_batch"] = invalidation_batch

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_key_group(
        self,
        key_group_config: "aws_sdk_cloudfront.types.key_group_config.KeyGroupConfig",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.create_key_group_result.CreateKeyGroupResult":
        r"""<p>Creates a key group that you can use with <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html\">CloudFront signed URLs and signed cookies</a>.</p> <p>To create a key group, you must specify at least one public key for the key group. After you create a key group, you can reference it from one or more cache behaviors. When you reference a key group in a cache behavior, CloudFront requires signed URLs or signed cookies for all requests that match the cache behavior. The URLs or cookies must be signed with a private key whose corresponding public key is in the key group. The signed URL or cookie contains information about which public key CloudFront should use to verify the signature. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html\">Serving private content</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            key_group_config: <p>A key group configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.create_key_group_request.CreateKeyGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.create_key_group_result.CreateKeyGroupResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_key_group

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_key_group.create_key_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.create_key_group_request.CreateKeyGroupRequest = {}  # type: ignore[typeddict-item]
        input_["key_group_config"] = key_group_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_key_value_store(
        self,
        name: "aws_sdk_cloudfront.types.key_value_store_name.KeyValueStoreName",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        comment: Optional[
            "aws_sdk_cloudfront.types.key_value_store_comment.KeyValueStoreComment"
        ] = None,
        import_source: Optional[
            "aws_sdk_cloudfront.types.import_source.ImportSource"
        ] = None,
        tags: Optional["aws_sdk_cloudfront.types.tags.Tags"] = None,
    ) -> "aws_sdk_cloudfront.types.create_key_value_store_result.CreateKeyValueStoreResult":
        """<p>Specifies the key value store resource to add to your account. In your account, the key value store names must be unique. You can also import key value store data in JSON format from an S3 bucket by providing a valid <code>ImportSource</code> that you own.</p>

        Args:
            name: <p>The name of the key value store. The minimum length is 1 character and the maximum length is 64 characters.</p>
            comment: <p>The comment of the key value store.</p>
            import_source: <p>The S3 bucket that provides the source for the import. The source must be in a valid JSON format.</p>

        Examples:
            To create a KeyValueStore
            Use the following command to create a KeyValueStore.

            >>> client.create_key_value_store(name='my-keyvaluestore-name', comment='my-key-valuestore-comment', import_source={'SourceType': 'S3', 'SourceARN': 'arn:aws:s3:::amzn-s3-demo-bucket/validJSON.json'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.create_key_value_store_request.CreateKeyValueStoreRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.create_key_value_store_result.CreateKeyValueStoreResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_key_value_store

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_key_value_store.create_key_value_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.create_key_value_store_request.CreateKeyValueStoreRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if comment is not None:
            input_["comment"] = comment
        if import_source is not None:
            input_["import_source"] = import_source
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_monitoring_subscription(
        self,
        distribution_id: "aws_sdk_cloudfront.types.string.string",
        monitoring_subscription: "aws_sdk_cloudfront.types.monitoring_subscription.MonitoringSubscription",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.create_monitoring_subscription_result.CreateMonitoringSubscriptionResult":
        r"""<p>Enables or disables additional Amazon CloudWatch metrics for the specified CloudFront distribution. The additional metrics incur an additional cost.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/viewing-cloudfront-metrics.html#monitoring-console.distributions-additional\">Viewing additional CloudFront distribution metrics</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            distribution_id: <p>The ID of the distribution that you are enabling metrics for.</p>
            monitoring_subscription: <p>A monitoring subscription. This structure contains information about whether additional CloudWatch metrics are enabled for a given CloudFront distribution.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.create_monitoring_subscription_request.CreateMonitoringSubscriptionRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.create_monitoring_subscription_result.CreateMonitoringSubscriptionResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_monitoring_subscription

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_monitoring_subscription.create_monitoring_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.create_monitoring_subscription_request.CreateMonitoringSubscriptionRequest = {}  # type: ignore[typeddict-item]
        input_["distribution_id"] = distribution_id
        input_["monitoring_subscription"] = monitoring_subscription

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_origin_access_control(
        self,
        origin_access_control_config: "aws_sdk_cloudfront.types.origin_access_control_config.OriginAccessControlConfig",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.create_origin_access_control_result.CreateOriginAccessControlResult":
        r"""<p>Creates a new origin access control in CloudFront. After you create an origin access control, you can add it to an origin in a CloudFront distribution so that CloudFront sends authenticated (signed) requests to the origin.</p> <p>This makes it possible to block public access to the origin, allowing viewers (users) to access the origin's content only through CloudFront.</p> <p>For more information about using a CloudFront origin access control, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-origin.html\">Restricting access to an Amazon Web Services origin</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            origin_access_control_config: <p>Contains the origin access control.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.create_origin_access_control_request.CreateOriginAccessControlRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.create_origin_access_control_result.CreateOriginAccessControlResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_origin_access_control

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_origin_access_control.create_origin_access_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.create_origin_access_control_request.CreateOriginAccessControlRequest = {}  # type: ignore[typeddict-item]
        input_["origin_access_control_config"] = origin_access_control_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_origin_request_policy(
        self,
        origin_request_policy_config: "aws_sdk_cloudfront.types.origin_request_policy_config.OriginRequestPolicyConfig",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.create_origin_request_policy_result.CreateOriginRequestPolicyResult":
        r"""<p>Creates an origin request policy.</p> <p>After you create an origin request policy, you can attach it to one or more cache behaviors. When it's attached to a cache behavior, the origin request policy determines the values that CloudFront includes in requests that it sends to the origin. Each request that CloudFront sends to the origin includes the following:</p> <ul> <li> <p>The request body and the URL path (without the domain name) from the viewer request.</p> </li> <li> <p>The headers that CloudFront automatically includes in every origin request, including <code>Host</code>, <code>User-Agent</code>, and <code>X-Amz-Cf-Id</code>.</p> </li> <li> <p>All HTTP headers, cookies, and URL query strings that are specified in the cache policy or the origin request policy. These can include items from the viewer request and, in the case of headers, additional ones that are added by CloudFront.</p> </li> </ul> <p>CloudFront sends a request when it can't find a valid object in its cache that matches the request. If you want to send values to the origin and also include them in the cache key, use <code>CachePolicy</code>.</p> <p>For more information about origin request policies, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html\">Controlling origin requests</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            origin_request_policy_config: <p>An origin request policy configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.create_origin_request_policy_request.CreateOriginRequestPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.create_origin_request_policy_result.CreateOriginRequestPolicyResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_origin_request_policy

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_origin_request_policy.create_origin_request_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.create_origin_request_policy_request.CreateOriginRequestPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["origin_request_policy_config"] = origin_request_policy_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_public_key(
        self,
        public_key_config: "aws_sdk_cloudfront.types.public_key_config.PublicKeyConfig",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.create_public_key_result.CreatePublicKeyResult":
        r"""<p>Uploads a public key to CloudFront that you can use with <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html\">signed URLs and signed cookies</a>, or with <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html\">field-level encryption</a>.</p>

        Args:
            public_key_config: <p>A CloudFront public key configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.create_public_key_request.CreatePublicKeyRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.create_public_key_result.CreatePublicKeyResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_public_key

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_public_key.create_public_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.create_public_key_request.CreatePublicKeyRequest = {}  # type: ignore[typeddict-item]
        input_["public_key_config"] = public_key_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_realtime_log_config(
        self,
        end_points: "aws_sdk_cloudfront.types.end_point_list.EndPointList",
        fields: "aws_sdk_cloudfront.types.field_list.FieldList",
        name: "aws_sdk_cloudfront.types.string.string",
        sampling_rate: "aws_sdk_cloudfront.types.long.long",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.create_realtime_log_config_result.CreateRealtimeLogConfigResult":
        r"""<p>Creates a real-time log configuration.</p> <p>After you create a real-time log configuration, you can attach it to one or more cache behaviors to send real-time log data to the specified Amazon Kinesis data stream.</p> <p>For more information about real-time log configurations, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html\">Real-time logs</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            end_points: <p>Contains information about the Amazon Kinesis data stream where you are sending real-time log data.</p>
            fields: <p>A list of fields to include in each real-time log record.</p> <p>For more information about fields, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html#understand-real-time-log-config-fields\">Real-time log configuration fields</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>
            name: <p>A unique name to identify this real-time log configuration.</p>
            sampling_rate: <p>The sampling rate for this real-time log configuration. You can specify a whole number between 1 and 100 (inclusive) to determine the percentage of viewer requests that are represented in the real-time log data.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.create_realtime_log_config_request.CreateRealtimeLogConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.create_realtime_log_config_result.CreateRealtimeLogConfigResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_realtime_log_config

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_realtime_log_config.create_realtime_log_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.create_realtime_log_config_request.CreateRealtimeLogConfigRequest = {}  # type: ignore[typeddict-item]
        input_["end_points"] = end_points
        input_["fields"] = fields
        input_["name"] = name
        input_["sampling_rate"] = sampling_rate

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_response_headers_policy(
        self,
        response_headers_policy_config: "aws_sdk_cloudfront.types.response_headers_policy_config.ResponseHeadersPolicyConfig",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.create_response_headers_policy_result.CreateResponseHeadersPolicyResult":
        r"""<p>Creates a response headers policy.</p> <p>A response headers policy contains information about a set of HTTP headers. To create a response headers policy, you provide some metadata about the policy and a set of configurations that specify the headers.</p> <p>After you create a response headers policy, you can use its ID to attach it to one or more cache behaviors in a CloudFront distribution. When it's attached to a cache behavior, the response headers policy affects the HTTP headers that CloudFront includes in HTTP responses to requests that match the cache behavior. CloudFront adds or removes response headers according to the configuration of the response headers policy.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/modifying-response-headers.html\">Adding or removing HTTP headers in CloudFront responses</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            response_headers_policy_config: <p>Contains metadata about the response headers policy, and a set of configurations that specify the HTTP headers.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.create_response_headers_policy_request.CreateResponseHeadersPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.create_response_headers_policy_result.CreateResponseHeadersPolicyResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_response_headers_policy

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_response_headers_policy.create_response_headers_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.create_response_headers_policy_request.CreateResponseHeadersPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["response_headers_policy_config"] = response_headers_policy_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_streaming_distribution(
        self,
        streaming_distribution_config: "aws_sdk_cloudfront.types.streaming_distribution_config.StreamingDistributionConfig",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.create_streaming_distribution_result.CreateStreamingDistributionResult":
        r"""<p>This API is deprecated. Amazon CloudFront is deprecating real-time messaging protocol (RTMP) distributions on December 31, 2020. For more information, <a href=\"http://forums.aws.amazon.com/ann.jspa?annID=7356\">read the announcement</a> on the Amazon CloudFront discussion forum.</p>

        Args:
            streaming_distribution_config: <p>The streaming distribution's configuration information.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.create_streaming_distribution_request.CreateStreamingDistributionRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.create_streaming_distribution_result.CreateStreamingDistributionResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_streaming_distribution

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_streaming_distribution.create_streaming_distribution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.create_streaming_distribution_request.CreateStreamingDistributionRequest = {}  # type: ignore[typeddict-item]
        input_["streaming_distribution_config"] = streaming_distribution_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_streaming_distribution_with_tags(
        self,
        streaming_distribution_config_with_tags: "aws_sdk_cloudfront.types.streaming_distribution_config_with_tags.StreamingDistributionConfigWithTags",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.create_streaming_distribution_with_tags_result.CreateStreamingDistributionWithTagsResult":
        r"""<p>This API is deprecated. Amazon CloudFront is deprecating real-time messaging protocol (RTMP) distributions on December 31, 2020. For more information, <a href=\"http://forums.aws.amazon.com/ann.jspa?annID=7356\">read the announcement</a> on the Amazon CloudFront discussion forum.</p>

        Args:
            streaming_distribution_config_with_tags: <p>The streaming distribution's configuration information.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.create_streaming_distribution_with_tags_request.CreateStreamingDistributionWithTagsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.create_streaming_distribution_with_tags_result.CreateStreamingDistributionWithTagsResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_streaming_distribution_with_tags

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_streaming_distribution_with_tags.create_streaming_distribution_with_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.create_streaming_distribution_with_tags_request.CreateStreamingDistributionWithTagsRequest = {}  # type: ignore[typeddict-item]
        input_["streaming_distribution_config_with_tags"] = (
            streaming_distribution_config_with_tags
        )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_trust_store(
        self,
        name: "aws_sdk_cloudfront.types.string.string",
        ca_certificates_bundle_source: "aws_sdk_cloudfront.types.ca_certificates_bundle_source.CaCertificatesBundleSource",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        use_client_certificate_ocsp_endpoint: Optional[
            "aws_sdk_cloudfront.types.boolean.boolean"
        ] = None,
        tags: Optional["aws_sdk_cloudfront.types.tags.Tags"] = None,
    ) -> "aws_sdk_cloudfront.types.create_trust_store_result.CreateTrustStoreResult":
        """<p>Creates a trust store.</p>

        Args:
            name: <p>A name for the trust store.</p>
            ca_certificates_bundle_source: <p>The CA certificates bundle source for the trust store.</p>
            use_client_certificate_ocsp_endpoint: <p>A Boolean that determines whether to use the CA certificate's OCSP endpoint to check certificate revocation status.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.create_trust_store_request.CreateTrustStoreRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.create_trust_store_result.CreateTrustStoreResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_trust_store

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_trust_store.create_trust_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.create_trust_store_request.CreateTrustStoreRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["ca_certificates_bundle_source"] = ca_certificates_bundle_source
        if use_client_certificate_ocsp_endpoint is not None:
            input_["use_client_certificate_ocsp_endpoint"] = (
                use_client_certificate_ocsp_endpoint
            )
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_vpc_origin(
        self,
        vpc_origin_endpoint_config: "aws_sdk_cloudfront.types.vpc_origin_endpoint_config.VpcOriginEndpointConfig",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        tags: Optional["aws_sdk_cloudfront.types.tags.Tags"] = None,
    ) -> "aws_sdk_cloudfront.types.create_vpc_origin_result.CreateVpcOriginResult":
        """<p>Create an Amazon CloudFront VPC origin.</p>

        Args:
            vpc_origin_endpoint_config: <p>The VPC origin endpoint configuration.</p>

        Examples:
            To create a VPC origin
            The following command creates a VPC origin:

            >>> client.create_vpc_origin(vpc_origin_endpoint_config={'Name': 'my-vpcorigin-name', 'Arn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-alb-us-west-2/e6aa5c7d26415c6d', 'HTTPPort': 80, 'HTTPSPort': 443, 'OriginProtocolPolicy': 'match-viewer', 'OriginSslProtocols': {'Quantity': 2, 'Items': ['TLSv1.1', 'TLSv1.2']}})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.create_vpc_origin_request.CreateVpcOriginRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.create_vpc_origin_result.CreateVpcOriginResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_vpc_origin

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.create_vpc_origin.create_vpc_origin(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.create_vpc_origin_request.CreateVpcOriginRequest = {}  # type: ignore[typeddict-item]
        input_["vpc_origin_endpoint_config"] = vpc_origin_endpoint_config
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_anycast_ip_list(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        if_match: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> None:
        """<p>Deletes an Anycast static IP list.</p>

        Args:
            id: <p>The ID of the Anycast static IP list.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the Anycast static IP list that you are deleting.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.delete_anycast_ip_list_request.DeleteAnycastIpListRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_anycast_ip_list

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_anycast_ip_list.delete_anycast_ip_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.delete_anycast_ip_list_request.DeleteAnycastIpListRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_cache_policy(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> None:
        """<p>Deletes a cache policy.</p> <p>You cannot delete a cache policy if it's attached to a cache behavior. First update your distributions to remove the cache policy from all cache behaviors, then delete the cache policy.</p> <p>To delete a cache policy, you must provide the policy's identifier and version. To get these values, you can use <code>ListCachePolicies</code> or <code>GetCachePolicy</code>.</p>

        Args:
            id: <p>The unique identifier for the cache policy that you are deleting. To get the identifier, you can use <code>ListCachePolicies</code>.</p>
            if_match: <p>The version of the cache policy that you are deleting. The version is the cache policy's <code>ETag</code> value, which you can get using <code>ListCachePolicies</code>, <code>GetCachePolicy</code>, or <code>GetCachePolicyConfig</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.delete_cache_policy_request.DeleteCachePolicyRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_cache_policy

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_cache_policy.delete_cache_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.delete_cache_policy_request.DeleteCachePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_cloud_front_origin_access_identity(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> None:
        """<p>Delete an origin access identity.</p>

        Args:
            id: <p>The origin access identity's ID.</p>
            if_match: <p>The value of the <code>ETag</code> header you received from a previous <code>GET</code> or <code>PUT</code> request. For example: <code>E2QWRUHAPOMQZL</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.delete_cloud_front_origin_access_identity_request.DeleteCloudFrontOriginAccessIdentityRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_cloud_front_origin_access_identity

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_cloud_front_origin_access_identity.delete_cloud_front_origin_access_identity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.delete_cloud_front_origin_access_identity_request.DeleteCloudFrontOriginAccessIdentityRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_connection_function(
        self,
        id: "aws_sdk_cloudfront.types.resource_id.ResourceId",
        if_match: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> None:
        """<p>Deletes a connection function.</p>

        Args:
            id: <p>The connection function's ID.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the connection function you are deleting.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.delete_connection_function_request.DeleteConnectionFunctionRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_connection_function

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_connection_function.delete_connection_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.delete_connection_function_request.DeleteConnectionFunctionRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_connection_group(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        if_match: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> None:
        """<p>Deletes a connection group.</p>

        Args:
            id: <p>The ID of the connection group to delete.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the connection group to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.delete_connection_group_request.DeleteConnectionGroupRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_connection_group

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_connection_group.delete_connection_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.delete_connection_group_request.DeleteConnectionGroupRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_continuous_deployment_policy(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> None:
        """<p>Deletes a continuous deployment policy.</p> <p>You cannot delete a continuous deployment policy that's attached to a primary distribution. First update your distribution to remove the continuous deployment policy, then you can delete the policy.</p>

        Args:
            id: <p>The identifier of the continuous deployment policy that you are deleting.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the continuous deployment policy that you are deleting.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.delete_continuous_deployment_policy_request.DeleteContinuousDeploymentPolicyRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_continuous_deployment_policy

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_continuous_deployment_policy.delete_continuous_deployment_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.delete_continuous_deployment_policy_request.DeleteContinuousDeploymentPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_distribution(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> None:
        """<p>Delete a distribution.</p> <important> <p>Before you can delete a distribution, you must disable it, which requires permission to update the distribution. Once deleted, a distribution cannot be recovered.</p> </important>

        Args:
            id: <p>The distribution ID.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when you disabled the distribution. For example: <code>E2QWRUHAPOMQZL</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.delete_distribution_request.DeleteDistributionRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_distribution

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_distribution.delete_distribution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.delete_distribution_request.DeleteDistributionRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_distribution_tenant(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        if_match: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> None:
        """<p>Deletes a distribution tenant. If you use this API operation to delete a distribution tenant that is currently enabled, the request will fail.</p> <p>To delete a distribution tenant, you must first disable the distribution tenant by using the <code>UpdateDistributionTenant</code> API operation.</p>

        Args:
            id: <p>The ID of the distribution tenant to delete.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the distribution tenant. This value is returned in the response of the <code>GetDistributionTenant</code> API operation.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.delete_distribution_tenant_request.DeleteDistributionTenantRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_distribution_tenant

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_distribution_tenant.delete_distribution_tenant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.delete_distribution_tenant_request.DeleteDistributionTenantRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_field_level_encryption_config(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> None:
        """<p>Remove a field-level encryption configuration.</p>

        Args:
            id: <p>The ID of the configuration you want to delete from CloudFront.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the configuration identity to delete. For example: <code>E2QWRUHAPOMQZL</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.delete_field_level_encryption_config_request.DeleteFieldLevelEncryptionConfigRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_field_level_encryption_config

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_field_level_encryption_config.delete_field_level_encryption_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.delete_field_level_encryption_config_request.DeleteFieldLevelEncryptionConfigRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_field_level_encryption_profile(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> None:
        """<p>Remove a field-level encryption profile.</p>

        Args:
            id: <p>Request the ID of the profile you want to delete from CloudFront.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the profile to delete. For example: <code>E2QWRUHAPOMQZL</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.delete_field_level_encryption_profile_request.DeleteFieldLevelEncryptionProfileRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_field_level_encryption_profile

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_field_level_encryption_profile.delete_field_level_encryption_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.delete_field_level_encryption_profile_request.DeleteFieldLevelEncryptionProfileRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_function(
        self,
        name: "aws_sdk_cloudfront.types.function_name.FunctionName",
        if_match: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> None:
        """<p>Deletes a CloudFront function.</p> <p>You cannot delete a function if it's associated with a cache behavior. First, update your distributions to remove the function association from all cache behaviors, then delete the function.</p> <p>To delete a function, you must provide the function's name and version (<code>ETag</code> value). To get these values, you can use <code>ListFunctions</code> and <code>DescribeFunction</code>.</p>

        Args:
            name: <p>The name of the function that you are deleting.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the function that you are deleting, which you can get using <code>DescribeFunction</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.delete_function_request.DeleteFunctionRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_function

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_function.delete_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.delete_function_request.DeleteFunctionRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_key_group(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> None:
        """<p>Deletes a key group.</p> <p>You cannot delete a key group that is referenced in a cache behavior. First update your distributions to remove the key group from all cache behaviors, then delete the key group.</p> <p>To delete a key group, you must provide the key group's identifier and version. To get these values, use <code>ListKeyGroups</code> followed by <code>GetKeyGroup</code> or <code>GetKeyGroupConfig</code>.</p>

        Args:
            id: <p>The identifier of the key group that you are deleting. To get the identifier, use <code>ListKeyGroups</code>.</p>
            if_match: <p>The version of the key group that you are deleting. The version is the key group's <code>ETag</code> value. To get the <code>ETag</code>, use <code>GetKeyGroup</code> or <code>GetKeyGroupConfig</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.delete_key_group_request.DeleteKeyGroupRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_key_group

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_key_group.delete_key_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.delete_key_group_request.DeleteKeyGroupRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_key_value_store(
        self,
        name: "aws_sdk_cloudfront.types.key_value_store_name.KeyValueStoreName",
        if_match: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> None:
        """<p>Specifies the key value store to delete.</p>

        Args:
            name: <p>The name of the key value store.</p>
            if_match: <p>The key value store to delete, if a match occurs.</p>

        Examples:
            To delete a KeyValueStore
            Use the following command to delete a KeyValueStore.

            >>> client.delete_key_value_store(name='my-keyvaluestore-name', if_match='ETVPDKIKX0DER')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.delete_key_value_store_request.DeleteKeyValueStoreRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_key_value_store

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_key_value_store.delete_key_value_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.delete_key_value_store_request.DeleteKeyValueStoreRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_monitoring_subscription(
        self,
        distribution_id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.delete_monitoring_subscription_result.DeleteMonitoringSubscriptionResult":
        """<p>Disables additional CloudWatch metrics for the specified CloudFront distribution.</p>

        Args:
            distribution_id: <p>The ID of the distribution that you are disabling metrics for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.delete_monitoring_subscription_request.DeleteMonitoringSubscriptionRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.delete_monitoring_subscription_result.DeleteMonitoringSubscriptionResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_monitoring_subscription

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_monitoring_subscription.delete_monitoring_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.delete_monitoring_subscription_request.DeleteMonitoringSubscriptionRequest = {}  # type: ignore[typeddict-item]
        input_["distribution_id"] = distribution_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_origin_access_control(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> None:
        """<p>Deletes a CloudFront origin access control.</p> <p>You cannot delete an origin access control if it's in use. First, update all distributions to remove the origin access control from all origins, then delete the origin access control.</p>

        Args:
            id: <p>The unique identifier of the origin access control that you are deleting.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the origin access control that you are deleting.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.delete_origin_access_control_request.DeleteOriginAccessControlRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_origin_access_control

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_origin_access_control.delete_origin_access_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.delete_origin_access_control_request.DeleteOriginAccessControlRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_origin_request_policy(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> None:
        """<p>Deletes an origin request policy.</p> <p>You cannot delete an origin request policy if it's attached to any cache behaviors. First update your distributions to remove the origin request policy from all cache behaviors, then delete the origin request policy.</p> <p>To delete an origin request policy, you must provide the policy's identifier and version. To get the identifier, you can use <code>ListOriginRequestPolicies</code> or <code>GetOriginRequestPolicy</code>.</p>

        Args:
            id: <p>The unique identifier for the origin request policy that you are deleting. To get the identifier, you can use <code>ListOriginRequestPolicies</code>.</p>
            if_match: <p>The version of the origin request policy that you are deleting. The version is the origin request policy's <code>ETag</code> value, which you can get using <code>ListOriginRequestPolicies</code>, <code>GetOriginRequestPolicy</code>, or <code>GetOriginRequestPolicyConfig</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.delete_origin_request_policy_request.DeleteOriginRequestPolicyRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_origin_request_policy

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_origin_request_policy.delete_origin_request_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.delete_origin_request_policy_request.DeleteOriginRequestPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_public_key(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> None:
        """<p>Remove a public key you previously added to CloudFront.</p>

        Args:
            id: <p>The ID of the public key you want to remove from CloudFront.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the public key identity to delete. For example: <code>E2QWRUHAPOMQZL</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.delete_public_key_request.DeletePublicKeyRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_public_key

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_public_key.delete_public_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.delete_public_key_request.DeletePublicKeyRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_realtime_log_config(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        name: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        arn: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> None:
        """<p>Deletes a real-time log configuration.</p> <p>You cannot delete a real-time log configuration if it's attached to a cache behavior. First update your distributions to remove the real-time log configuration from all cache behaviors, then delete the real-time log configuration.</p> <p>To delete a real-time log configuration, you can provide the configuration's name or its Amazon Resource Name (ARN). You must provide at least one. If you provide both, CloudFront uses the name to identify the real-time log configuration to delete.</p>

        Args:
            name: <p>The name of the real-time log configuration to delete.</p>
            arn: <p>The Amazon Resource Name (ARN) of the real-time log configuration to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.delete_realtime_log_config_request.DeleteRealtimeLogConfigRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_realtime_log_config

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_realtime_log_config.delete_realtime_log_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.delete_realtime_log_config_request.DeleteRealtimeLogConfigRequest = {}  # type: ignore[typeddict-item]
        if name is not None:
            input_["name"] = name
        if arn is not None:
            input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_resource_policy(
        self,
        resource_arn: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> None:
        """<p>Deletes the resource policy attached to the CloudFront resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the CloudFront resource for which the resource policy should be deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_resource_policy

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_resource_policy.delete_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_response_headers_policy(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> None:
        """<p>Deletes a response headers policy.</p> <p>You cannot delete a response headers policy if it's attached to a cache behavior. First update your distributions to remove the response headers policy from all cache behaviors, then delete the response headers policy.</p> <p>To delete a response headers policy, you must provide the policy's identifier and version. To get these values, you can use <code>ListResponseHeadersPolicies</code> or <code>GetResponseHeadersPolicy</code>.</p>

        Args:
            id: <p>The identifier for the response headers policy that you are deleting.</p> <p>To get the identifier, you can use <code>ListResponseHeadersPolicies</code>.</p>
            if_match: <p>The version of the response headers policy that you are deleting.</p> <p>The version is the response headers policy's <code>ETag</code> value, which you can get using <code>ListResponseHeadersPolicies</code>, <code>GetResponseHeadersPolicy</code>, or <code>GetResponseHeadersPolicyConfig</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.delete_response_headers_policy_request.DeleteResponseHeadersPolicyRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_response_headers_policy

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_response_headers_policy.delete_response_headers_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.delete_response_headers_policy_request.DeleteResponseHeadersPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_streaming_distribution(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> None:
        r"""<p>Delete a streaming distribution. To delete an RTMP distribution using the CloudFront API, perform the following steps.</p> <p> <b>To delete an RTMP distribution using the CloudFront API</b>:</p> <ol> <li> <p>Disable the RTMP distribution.</p> </li> <li> <p>Submit a <code>GET Streaming Distribution Config</code> request to get the current configuration and the <code>Etag</code> header for the distribution. </p> </li> <li> <p>Update the XML document that was returned in the response to your <code>GET Streaming Distribution Config</code> request to change the value of <code>Enabled</code> to <code>false</code>.</p> </li> <li> <p>Submit a <code>PUT Streaming Distribution Config</code> request to update the configuration for your distribution. In the request body, include the XML document that you updated in Step 3. Then set the value of the HTTP <code>If-Match</code> header to the value of the <code>ETag</code> header that CloudFront returned when you submitted the <code>GET Streaming Distribution Config</code> request in Step 2.</p> </li> <li> <p>Review the response to the <code>PUT Streaming Distribution Config</code> request to confirm that the distribution was successfully disabled.</p> </li> <li> <p>Submit a <code>GET Streaming Distribution Config</code> request to confirm that your changes have propagated. When propagation is complete, the value of <code>Status</code> is <code>Deployed</code>.</p> </li> <li> <p>Submit a <code>DELETE Streaming Distribution</code> request. Set the value of the HTTP <code>If-Match</code> header to the value of the <code>ETag</code> header that CloudFront returned when you submitted the <code>GET Streaming Distribution Config</code> request in Step 2.</p> </li> <li> <p>Review the response to your <code>DELETE Streaming Distribution</code> request to confirm that the distribution was successfully deleted.</p> </li> </ol> <p>For information about deleting a distribution using the CloudFront console, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowToDeleteDistribution.html\">Deleting a Distribution</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            id: <p>The distribution ID.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when you disabled the streaming distribution. For example: <code>E2QWRUHAPOMQZL</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.delete_streaming_distribution_request.DeleteStreamingDistributionRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_streaming_distribution

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_streaming_distribution.delete_streaming_distribution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.delete_streaming_distribution_request.DeleteStreamingDistributionRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_trust_store(
        self,
        id: "aws_sdk_cloudfront.types.resource_id.ResourceId",
        if_match: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> None:
        """<p>Deletes a trust store.</p>

        Args:
            id: <p>The trust store's ID.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the trust store you are deleting.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.delete_trust_store_request.DeleteTrustStoreRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_trust_store

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_trust_store.delete_trust_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.delete_trust_store_request.DeleteTrustStoreRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_vpc_origin(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        if_match: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.delete_vpc_origin_result.DeleteVpcOriginResult":
        """<p>Delete an Amazon CloudFront VPC origin.</p>

        Args:
            id: <p>The VPC origin ID.</p>
            if_match: <p>The version identifier of the VPC origin to delete. This is the <code>ETag</code> value returned in the response to <a>GetVpcOrigin</a>.</p>

        Examples:
            To delete a VPC origin
            The following command deletes a VPC origin:

            >>> client.delete_vpc_origin(id='vo_BQwjxxQxjCaBcQLzJUFkDM', if_match='E1F83G8C2ARO7P')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.delete_vpc_origin_request.DeleteVpcOriginRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.delete_vpc_origin_result.DeleteVpcOriginResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_vpc_origin

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.delete_vpc_origin.delete_vpc_origin(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.delete_vpc_origin_request.DeleteVpcOriginRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_connection_function(
        self,
        identifier: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        stage: Optional["aws_sdk_cloudfront.types.function_stage.FunctionStage"] = None,
    ) -> "aws_sdk_cloudfront.types.describe_connection_function_result.DescribeConnectionFunctionResult":
        """<p>Describes a connection function.</p>

        Args:
            identifier: <p>The connection function's identifier.</p>
            stage: <p>The connection function's stage.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.describe_connection_function_request.DescribeConnectionFunctionRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.describe_connection_function_result.DescribeConnectionFunctionResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.describe_connection_function

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.describe_connection_function.describe_connection_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.describe_connection_function_request.DescribeConnectionFunctionRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier
        if stage is not None:
            input_["stage"] = stage

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_function(
        self,
        name: "aws_sdk_cloudfront.types.function_name.FunctionName",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        stage: Optional["aws_sdk_cloudfront.types.function_stage.FunctionStage"] = None,
    ) -> "aws_sdk_cloudfront.types.describe_function_result.DescribeFunctionResult":
        """<p>Gets configuration information and metadata about a CloudFront function, but not the function's code. To get a function's code, use <code>GetFunction</code>.</p> <p>To get configuration information and metadata about a function, you must provide the function's name and stage. To get these values, you can use <code>ListFunctions</code>.</p>

        Args:
            name: <p>The name of the function that you are getting information about.</p>
            stage: <p>The function's stage, either <code>DEVELOPMENT</code> or <code>LIVE</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.describe_function_request.DescribeFunctionRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.describe_function_result.DescribeFunctionResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.describe_function

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.describe_function.describe_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.describe_function_request.DescribeFunctionRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if stage is not None:
            input_["stage"] = stage

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_key_value_store(
        self,
        name: "aws_sdk_cloudfront.types.key_value_store_name.KeyValueStoreName",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.describe_key_value_store_result.DescribeKeyValueStoreResult":
        """<p>Specifies the key value store and its configuration.</p>

        Args:
            name: <p>The name of the key value store.</p>

        Examples:
            To describe a KeyValueStore
            Use the following command to describe a KeyValueStore.

            >>> client.describe_key_value_store(name='my-keyvaluestore-name')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.describe_key_value_store_request.DescribeKeyValueStoreRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.describe_key_value_store_result.DescribeKeyValueStoreResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.describe_key_value_store

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.describe_key_value_store.describe_key_value_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.describe_key_value_store_request.DescribeKeyValueStoreRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_distribution_tenant_web_acl(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> "aws_sdk_cloudfront.types.disassociate_distribution_tenant_web_acl_result.DisassociateDistributionTenantWebACLResult":
        """<p>Disassociates a distribution tenant from the WAF web ACL.</p>

        Args:
            id: <p>The ID of the distribution tenant.</p>
            if_match: <p>The current version of the distribution tenant that you're disassociating from the WAF web ACL. This is the <code>ETag</code> value returned in the response to the <code>GetDistributionTenant</code> API operation.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.disassociate_distribution_tenant_web_acl_request.DisassociateDistributionTenantWebACLRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.disassociate_distribution_tenant_web_acl_result.DisassociateDistributionTenantWebACLResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.disassociate_distribution_tenant_web_acl

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.disassociate_distribution_tenant_web_acl.disassociate_distribution_tenant_web_acl(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.disassociate_distribution_tenant_web_acl_request.DisassociateDistributionTenantWebACLRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_distribution_web_acl(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> "aws_sdk_cloudfront.types.disassociate_distribution_web_acl_result.DisassociateDistributionWebACLResult":
        """<p>Disassociates a distribution from the WAF web ACL.</p>

        Args:
            id: <p>The ID of the distribution.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the distribution that you're disassociating from the WAF web ACL.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.disassociate_distribution_web_acl_request.DisassociateDistributionWebACLRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.disassociate_distribution_web_acl_result.DisassociateDistributionWebACLResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.disassociate_distribution_web_acl

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.disassociate_distribution_web_acl.disassociate_distribution_web_acl(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.disassociate_distribution_web_acl_request.DisassociateDistributionWebACLRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_anycast_ip_list(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_anycast_ip_list_result.GetAnycastIpListResult":
        """<p>Gets an Anycast static IP list.</p>

        Args:
            id: <p>The ID of the Anycast static IP list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_anycast_ip_list_request.GetAnycastIpListRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_anycast_ip_list_result.GetAnycastIpListResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_anycast_ip_list

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_anycast_ip_list.get_anycast_ip_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_anycast_ip_list_request.GetAnycastIpListRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_cache_policy(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_cache_policy_result.GetCachePolicyResult":
        """<p>Gets a cache policy, including the following metadata:</p> <ul> <li> <p>The policy's identifier.</p> </li> <li> <p>The date and time when the policy was last modified.</p> </li> </ul> <p>To get a cache policy, you must provide the policy's identifier. If the cache policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the cache policy is not attached to a cache behavior, you can get the identifier using <code>ListCachePolicies</code>.</p>

        Args:
            id: <p>The unique identifier for the cache policy. If the cache policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the cache policy is not attached to a cache behavior, you can get the identifier using <code>ListCachePolicies</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_cache_policy_request.GetCachePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_cache_policy_result.GetCachePolicyResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_cache_policy

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_cache_policy.get_cache_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_cache_policy_request.GetCachePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_cache_policy_config(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_cache_policy_config_result.GetCachePolicyConfigResult":
        """<p>Gets a cache policy configuration.</p> <p>To get a cache policy configuration, you must provide the policy's identifier. If the cache policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the cache policy is not attached to a cache behavior, you can get the identifier using <code>ListCachePolicies</code>.</p>

        Args:
            id: <p>The unique identifier for the cache policy. If the cache policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the cache policy is not attached to a cache behavior, you can get the identifier using <code>ListCachePolicies</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_cache_policy_config_request.GetCachePolicyConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_cache_policy_config_result.GetCachePolicyConfigResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_cache_policy_config

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_cache_policy_config.get_cache_policy_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_cache_policy_config_request.GetCachePolicyConfigRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_cloud_front_origin_access_identity(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_cloud_front_origin_access_identity_result.GetCloudFrontOriginAccessIdentityResult":
        """<p>Get the information about an origin access identity.</p>

        Args:
            id: <p>The identity's ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_cloud_front_origin_access_identity_request.GetCloudFrontOriginAccessIdentityRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_cloud_front_origin_access_identity_result.GetCloudFrontOriginAccessIdentityResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_cloud_front_origin_access_identity

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_cloud_front_origin_access_identity.get_cloud_front_origin_access_identity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_cloud_front_origin_access_identity_request.GetCloudFrontOriginAccessIdentityRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_cloud_front_origin_access_identity_config(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_cloud_front_origin_access_identity_config_result.GetCloudFrontOriginAccessIdentityConfigResult":
        """<p>Get the configuration information about an origin access identity.</p>

        Args:
            id: <p>The identity's ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_cloud_front_origin_access_identity_config_request.GetCloudFrontOriginAccessIdentityConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_cloud_front_origin_access_identity_config_result.GetCloudFrontOriginAccessIdentityConfigResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_cloud_front_origin_access_identity_config

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_cloud_front_origin_access_identity_config.get_cloud_front_origin_access_identity_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_cloud_front_origin_access_identity_config_request.GetCloudFrontOriginAccessIdentityConfigRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_connection_function(
        self,
        identifier: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        stage: Optional["aws_sdk_cloudfront.types.function_stage.FunctionStage"] = None,
    ) -> "aws_sdk_cloudfront.types.get_connection_function_result.GetConnectionFunctionResult":
        """<p>Gets a connection function.</p>

        Args:
            identifier: <p>The connection function's identifier.</p>
            stage: <p>The connection function's stage.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_connection_function_request.GetConnectionFunctionRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_connection_function_result.GetConnectionFunctionResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_connection_function

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_connection_function.get_connection_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_connection_function_request.GetConnectionFunctionRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier
        if stage is not None:
            input_["stage"] = stage

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_connection_group(
        self,
        identifier: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> (
        "aws_sdk_cloudfront.types.get_connection_group_result.GetConnectionGroupResult"
    ):
        """<p>Gets information about a connection group.</p>

        Args:
            identifier: <p>The ID, name, or Amazon Resource Name (ARN) of the connection group.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_connection_group_request.GetConnectionGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_connection_group_result.GetConnectionGroupResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_connection_group

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_connection_group.get_connection_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_connection_group_request.GetConnectionGroupRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_connection_group_by_routing_endpoint(
        self,
        routing_endpoint: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_connection_group_by_routing_endpoint_result.GetConnectionGroupByRoutingEndpointResult":
        """<p>Gets information about a connection group by using the endpoint that you specify.</p>

        Args:
            routing_endpoint: <p>The routing endpoint for the target connection group, such as d111111abcdef8.cloudfront.net.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_connection_group_by_routing_endpoint_request.GetConnectionGroupByRoutingEndpointRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_connection_group_by_routing_endpoint_result.GetConnectionGroupByRoutingEndpointResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_connection_group_by_routing_endpoint

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_connection_group_by_routing_endpoint.get_connection_group_by_routing_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_connection_group_by_routing_endpoint_request.GetConnectionGroupByRoutingEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["routing_endpoint"] = routing_endpoint

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_continuous_deployment_policy(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_continuous_deployment_policy_result.GetContinuousDeploymentPolicyResult":
        """<p>Gets a continuous deployment policy, including metadata (the policy's identifier and the date and time when the policy was last modified).</p>

        Args:
            id: <p>The identifier of the continuous deployment policy that you are getting.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_continuous_deployment_policy_request.GetContinuousDeploymentPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_continuous_deployment_policy_result.GetContinuousDeploymentPolicyResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_continuous_deployment_policy

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_continuous_deployment_policy.get_continuous_deployment_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_continuous_deployment_policy_request.GetContinuousDeploymentPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_continuous_deployment_policy_config(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_continuous_deployment_policy_config_result.GetContinuousDeploymentPolicyConfigResult":
        """<p>Gets configuration information about a continuous deployment policy.</p>

        Args:
            id: <p>The identifier of the continuous deployment policy whose configuration you are getting.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_continuous_deployment_policy_config_request.GetContinuousDeploymentPolicyConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_continuous_deployment_policy_config_result.GetContinuousDeploymentPolicyConfigResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_continuous_deployment_policy_config

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_continuous_deployment_policy_config.get_continuous_deployment_policy_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_continuous_deployment_policy_config_request.GetContinuousDeploymentPolicyConfigRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_distribution(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_distribution_result.GetDistributionResult":
        """<p>Get the information about a distribution.</p>

        Args:
            id: <p>The distribution's ID. If the ID is empty, an empty distribution configuration is returned.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_distribution_request.GetDistributionRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_distribution_result.GetDistributionResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_distribution

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_distribution.get_distribution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_distribution_request.GetDistributionRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_distribution_config(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_distribution_config_result.GetDistributionConfigResult":
        """<p>Get the configuration information about a distribution.</p>

        Args:
            id: <p>The distribution's ID. If the ID is empty, an empty distribution configuration is returned.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_distribution_config_request.GetDistributionConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_distribution_config_result.GetDistributionConfigResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_distribution_config

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_distribution_config.get_distribution_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_distribution_config_request.GetDistributionConfigRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_distribution_tenant(
        self,
        identifier: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_distribution_tenant_result.GetDistributionTenantResult":
        """<p>Gets information about a distribution tenant.</p>

        Args:
            identifier: <p>The identifier of the distribution tenant. You can specify the ARN, ID, or name of the distribution tenant.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_distribution_tenant_request.GetDistributionTenantRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_distribution_tenant_result.GetDistributionTenantResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_distribution_tenant

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_distribution_tenant.get_distribution_tenant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_distribution_tenant_request.GetDistributionTenantRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_distribution_tenant_by_domain(
        self,
        domain: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_distribution_tenant_by_domain_result.GetDistributionTenantByDomainResult":
        """<p>Gets information about a distribution tenant by the associated domain.</p>

        Args:
            domain: <p>A domain name associated with the target distribution tenant.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_distribution_tenant_by_domain_request.GetDistributionTenantByDomainRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_distribution_tenant_by_domain_result.GetDistributionTenantByDomainResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_distribution_tenant_by_domain

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_distribution_tenant_by_domain.get_distribution_tenant_by_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_distribution_tenant_by_domain_request.GetDistributionTenantByDomainRequest = {}  # type: ignore[typeddict-item]
        input_["domain"] = domain

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_field_level_encryption(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_field_level_encryption_result.GetFieldLevelEncryptionResult":
        """<p>Get the field-level encryption configuration information.</p>

        Args:
            id: <p>Request the ID for the field-level encryption configuration information.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_field_level_encryption_request.GetFieldLevelEncryptionRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_field_level_encryption_result.GetFieldLevelEncryptionResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_field_level_encryption

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_field_level_encryption.get_field_level_encryption(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_field_level_encryption_request.GetFieldLevelEncryptionRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_field_level_encryption_config(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_field_level_encryption_config_result.GetFieldLevelEncryptionConfigResult":
        """<p>Get the field-level encryption configuration information.</p>

        Args:
            id: <p>Request the ID for the field-level encryption configuration information.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_field_level_encryption_config_request.GetFieldLevelEncryptionConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_field_level_encryption_config_result.GetFieldLevelEncryptionConfigResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_field_level_encryption_config

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_field_level_encryption_config.get_field_level_encryption_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_field_level_encryption_config_request.GetFieldLevelEncryptionConfigRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_field_level_encryption_profile(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_field_level_encryption_profile_result.GetFieldLevelEncryptionProfileResult":
        """<p>Get the field-level encryption profile information.</p>

        Args:
            id: <p>Get the ID for the field-level encryption profile information.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_field_level_encryption_profile_request.GetFieldLevelEncryptionProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_field_level_encryption_profile_result.GetFieldLevelEncryptionProfileResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_field_level_encryption_profile

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_field_level_encryption_profile.get_field_level_encryption_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_field_level_encryption_profile_request.GetFieldLevelEncryptionProfileRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_field_level_encryption_profile_config(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_field_level_encryption_profile_config_result.GetFieldLevelEncryptionProfileConfigResult":
        """<p>Get the field-level encryption profile configuration information.</p>

        Args:
            id: <p>Get the ID for the field-level encryption profile configuration information.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_field_level_encryption_profile_config_request.GetFieldLevelEncryptionProfileConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_field_level_encryption_profile_config_result.GetFieldLevelEncryptionProfileConfigResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_field_level_encryption_profile_config

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_field_level_encryption_profile_config.get_field_level_encryption_profile_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_field_level_encryption_profile_config_request.GetFieldLevelEncryptionProfileConfigRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_function(
        self,
        name: "aws_sdk_cloudfront.types.function_name.FunctionName",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        stage: Optional["aws_sdk_cloudfront.types.function_stage.FunctionStage"] = None,
    ) -> "aws_sdk_cloudfront.types.get_function_result.GetFunctionResult":
        """<p>Gets the code of a CloudFront function. To get configuration information and metadata about a function, use <code>DescribeFunction</code>.</p> <p>To get a function's code, you must provide the function's name and stage. To get these values, you can use <code>ListFunctions</code>.</p>

        Args:
            name: <p>The name of the function whose code you are getting.</p>
            stage: <p>The function's stage, either <code>DEVELOPMENT</code> or <code>LIVE</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_function_request.GetFunctionRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_function_result.GetFunctionResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_function

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_function.get_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_function_request.GetFunctionRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if stage is not None:
            input_["stage"] = stage

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_invalidation(
        self,
        distribution_id: "aws_sdk_cloudfront.types.string.string",
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_invalidation_result.GetInvalidationResult":
        """<p>Get the information about an invalidation.</p>

        Args:
            distribution_id: <p>The distribution's ID.</p>
            id: <p>The identifier for the invalidation request, for example, <code>IDFDVBD632BHDS5</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_invalidation_request.GetInvalidationRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_invalidation_result.GetInvalidationResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_invalidation

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_invalidation.get_invalidation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_invalidation_request.GetInvalidationRequest = {}  # type: ignore[typeddict-item]
        input_["distribution_id"] = distribution_id
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_invalidation_for_distribution_tenant(
        self,
        distribution_tenant_id: "aws_sdk_cloudfront.types.string.string",
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_invalidation_for_distribution_tenant_result.GetInvalidationForDistributionTenantResult":
        """<p>Gets information about a specific invalidation for a distribution tenant.</p>

        Args:
            distribution_tenant_id: <p>The ID of the distribution tenant.</p>
            id: <p>The ID of the invalidation to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_invalidation_for_distribution_tenant_request.GetInvalidationForDistributionTenantRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_invalidation_for_distribution_tenant_result.GetInvalidationForDistributionTenantResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_invalidation_for_distribution_tenant

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_invalidation_for_distribution_tenant.get_invalidation_for_distribution_tenant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_invalidation_for_distribution_tenant_request.GetInvalidationForDistributionTenantRequest = {}  # type: ignore[typeddict-item]
        input_["distribution_tenant_id"] = distribution_tenant_id
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_key_group(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_key_group_result.GetKeyGroupResult":
        """<p>Gets a key group, including the date and time when the key group was last modified.</p> <p>To get a key group, you must provide the key group's identifier. If the key group is referenced in a distribution's cache behavior, you can get the key group's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the key group is not referenced in a cache behavior, you can get the identifier using <code>ListKeyGroups</code>.</p>

        Args:
            id: <p>The identifier of the key group that you are getting. To get the identifier, use <code>ListKeyGroups</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_key_group_request.GetKeyGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_key_group_result.GetKeyGroupResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_key_group

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_key_group.get_key_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_key_group_request.GetKeyGroupRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_key_group_config(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_key_group_config_result.GetKeyGroupConfigResult":
        """<p>Gets a key group configuration.</p> <p>To get a key group configuration, you must provide the key group's identifier. If the key group is referenced in a distribution's cache behavior, you can get the key group's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the key group is not referenced in a cache behavior, you can get the identifier using <code>ListKeyGroups</code>.</p>

        Args:
            id: <p>The identifier of the key group whose configuration you are getting. To get the identifier, use <code>ListKeyGroups</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_key_group_config_request.GetKeyGroupConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_key_group_config_result.GetKeyGroupConfigResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_key_group_config

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_key_group_config.get_key_group_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_key_group_config_request.GetKeyGroupConfigRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_managed_certificate_details(
        self,
        identifier: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_managed_certificate_details_result.GetManagedCertificateDetailsResult":
        """<p>Gets details about the CloudFront managed ACM certificate.</p>

        Args:
            identifier: <p>The identifier of the distribution tenant. You can specify the ARN, ID, or name of the distribution tenant.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_managed_certificate_details_request.GetManagedCertificateDetailsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_managed_certificate_details_result.GetManagedCertificateDetailsResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_managed_certificate_details

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_managed_certificate_details.get_managed_certificate_details(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_managed_certificate_details_request.GetManagedCertificateDetailsRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_monitoring_subscription(
        self,
        distribution_id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_monitoring_subscription_result.GetMonitoringSubscriptionResult":
        """<p>Gets information about whether additional CloudWatch metrics are enabled for the specified CloudFront distribution.</p>

        Args:
            distribution_id: <p>The ID of the distribution that you are getting metrics information for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_monitoring_subscription_request.GetMonitoringSubscriptionRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_monitoring_subscription_result.GetMonitoringSubscriptionResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_monitoring_subscription

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_monitoring_subscription.get_monitoring_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_monitoring_subscription_request.GetMonitoringSubscriptionRequest = {}  # type: ignore[typeddict-item]
        input_["distribution_id"] = distribution_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_origin_access_control(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_origin_access_control_result.GetOriginAccessControlResult":
        """<p>Gets a CloudFront origin access control, including its unique identifier.</p>

        Args:
            id: <p>The unique identifier of the origin access control.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_origin_access_control_request.GetOriginAccessControlRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_origin_access_control_result.GetOriginAccessControlResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_origin_access_control

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_origin_access_control.get_origin_access_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_origin_access_control_request.GetOriginAccessControlRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_origin_access_control_config(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_origin_access_control_config_result.GetOriginAccessControlConfigResult":
        """<p>Gets a CloudFront origin access control configuration.</p>

        Args:
            id: <p>The unique identifier of the origin access control.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_origin_access_control_config_request.GetOriginAccessControlConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_origin_access_control_config_result.GetOriginAccessControlConfigResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_origin_access_control_config

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_origin_access_control_config.get_origin_access_control_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_origin_access_control_config_request.GetOriginAccessControlConfigRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_origin_request_policy(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_origin_request_policy_result.GetOriginRequestPolicyResult":
        """<p>Gets an origin request policy, including the following metadata:</p> <ul> <li> <p>The policy's identifier.</p> </li> <li> <p>The date and time when the policy was last modified.</p> </li> </ul> <p>To get an origin request policy, you must provide the policy's identifier. If the origin request policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the origin request policy is not attached to a cache behavior, you can get the identifier using <code>ListOriginRequestPolicies</code>.</p>

        Args:
            id: <p>The unique identifier for the origin request policy. If the origin request policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the origin request policy is not attached to a cache behavior, you can get the identifier using <code>ListOriginRequestPolicies</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_origin_request_policy_request.GetOriginRequestPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_origin_request_policy_result.GetOriginRequestPolicyResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_origin_request_policy

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_origin_request_policy.get_origin_request_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_origin_request_policy_request.GetOriginRequestPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_origin_request_policy_config(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_origin_request_policy_config_result.GetOriginRequestPolicyConfigResult":
        """<p>Gets an origin request policy configuration.</p> <p>To get an origin request policy configuration, you must provide the policy's identifier. If the origin request policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the origin request policy is not attached to a cache behavior, you can get the identifier using <code>ListOriginRequestPolicies</code>.</p>

        Args:
            id: <p>The unique identifier for the origin request policy. If the origin request policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the origin request policy is not attached to a cache behavior, you can get the identifier using <code>ListOriginRequestPolicies</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_origin_request_policy_config_request.GetOriginRequestPolicyConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_origin_request_policy_config_result.GetOriginRequestPolicyConfigResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_origin_request_policy_config

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_origin_request_policy_config.get_origin_request_policy_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_origin_request_policy_config_request.GetOriginRequestPolicyConfigRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_public_key(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_public_key_result.GetPublicKeyResult":
        """<p>Gets a public key.</p>

        Args:
            id: <p>The identifier of the public key you are getting.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_public_key_request.GetPublicKeyRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_public_key_result.GetPublicKeyResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_public_key

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_public_key.get_public_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_public_key_request.GetPublicKeyRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_public_key_config(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> (
        "aws_sdk_cloudfront.types.get_public_key_config_result.GetPublicKeyConfigResult"
    ):
        """<p>Gets a public key configuration.</p>

        Args:
            id: <p>The identifier of the public key whose configuration you are getting.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_public_key_config_request.GetPublicKeyConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_public_key_config_result.GetPublicKeyConfigResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_public_key_config

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_public_key_config.get_public_key_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_public_key_config_request.GetPublicKeyConfigRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_realtime_log_config(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        name: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        arn: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> "aws_sdk_cloudfront.types.get_realtime_log_config_result.GetRealtimeLogConfigResult":
        """<p>Gets a real-time log configuration.</p> <p>To get a real-time log configuration, you can provide the configuration's name or its Amazon Resource Name (ARN). You must provide at least one. If you provide both, CloudFront uses the name to identify the real-time log configuration to get.</p>

        Args:
            name: <p>The name of the real-time log configuration to get.</p>
            arn: <p>The Amazon Resource Name (ARN) of the real-time log configuration to get.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_realtime_log_config_request.GetRealtimeLogConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_realtime_log_config_result.GetRealtimeLogConfigResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_realtime_log_config

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_realtime_log_config.get_realtime_log_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_realtime_log_config_request.GetRealtimeLogConfigRequest = {}  # type: ignore[typeddict-item]
        if name is not None:
            input_["name"] = name
        if arn is not None:
            input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_resource_policy(
        self,
        resource_arn: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_resource_policy_result.GetResourcePolicyResult":
        """<p>Retrieves the resource policy for the specified CloudFront resource that you own and have shared.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the CloudFront resource that is associated with the resource policy.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_resource_policy_result.GetResourcePolicyResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_resource_policy

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_resource_policy.get_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_resource_policy_request.GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_response_headers_policy(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_response_headers_policy_result.GetResponseHeadersPolicyResult":
        """<p>Gets a response headers policy, including metadata (the policy's identifier and the date and time when the policy was last modified).</p> <p>To get a response headers policy, you must provide the policy's identifier. If the response headers policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the response headers policy is not attached to a cache behavior, you can get the identifier using <code>ListResponseHeadersPolicies</code>.</p>

        Args:
            id: <p>The identifier for the response headers policy.</p> <p>If the response headers policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the response headers policy is not attached to a cache behavior, you can get the identifier using <code>ListResponseHeadersPolicies</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_response_headers_policy_request.GetResponseHeadersPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_response_headers_policy_result.GetResponseHeadersPolicyResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_response_headers_policy

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_response_headers_policy.get_response_headers_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_response_headers_policy_request.GetResponseHeadersPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_response_headers_policy_config(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_response_headers_policy_config_result.GetResponseHeadersPolicyConfigResult":
        """<p>Gets a response headers policy configuration.</p> <p>To get a response headers policy configuration, you must provide the policy's identifier. If the response headers policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the response headers policy is not attached to a cache behavior, you can get the identifier using <code>ListResponseHeadersPolicies</code>.</p>

        Args:
            id: <p>The identifier for the response headers policy.</p> <p>If the response headers policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the response headers policy is not attached to a cache behavior, you can get the identifier using <code>ListResponseHeadersPolicies</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_response_headers_policy_config_request.GetResponseHeadersPolicyConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_response_headers_policy_config_result.GetResponseHeadersPolicyConfigResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_response_headers_policy_config

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_response_headers_policy_config.get_response_headers_policy_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_response_headers_policy_config_request.GetResponseHeadersPolicyConfigRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_streaming_distribution(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_streaming_distribution_result.GetStreamingDistributionResult":
        """<p>Gets information about a specified RTMP distribution, including the distribution configuration.</p>

        Args:
            id: <p>The streaming distribution's ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_streaming_distribution_request.GetStreamingDistributionRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_streaming_distribution_result.GetStreamingDistributionResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_streaming_distribution

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_streaming_distribution.get_streaming_distribution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_streaming_distribution_request.GetStreamingDistributionRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_streaming_distribution_config(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_streaming_distribution_config_result.GetStreamingDistributionConfigResult":
        """<p>Get the configuration information about a streaming distribution.</p>

        Args:
            id: <p>The streaming distribution's ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_streaming_distribution_config_request.GetStreamingDistributionConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_streaming_distribution_config_result.GetStreamingDistributionConfigResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_streaming_distribution_config

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_streaming_distribution_config.get_streaming_distribution_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_streaming_distribution_config_request.GetStreamingDistributionConfigRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_trust_store(
        self,
        identifier: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_trust_store_result.GetTrustStoreResult":
        """<p>Gets a trust store.</p>

        Args:
            identifier: <p>The trust store's identifier.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_trust_store_request.GetTrustStoreRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_trust_store_result.GetTrustStoreResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_trust_store

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_trust_store.get_trust_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_trust_store_request.GetTrustStoreRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_vpc_origin(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.get_vpc_origin_result.GetVpcOriginResult":
        """<p>Get the details of an Amazon CloudFront VPC origin.</p>

        Args:
            id: <p>The VPC origin ID.</p>

        Examples:
            To get a VPC origin
            The following command gets a VPC origin:

            >>> client.get_vpc_origin(id='vo_BQwjxxQxjCaBcQLzJUFkDM')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.get_vpc_origin_request.GetVpcOriginRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.get_vpc_origin_result.GetVpcOriginResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_vpc_origin

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.get_vpc_origin.get_vpc_origin(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.get_vpc_origin_request.GetVpcOriginRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_anycast_ip_lists(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> (
        "aws_sdk_cloudfront.types.list_anycast_ip_lists_result.ListAnycastIpListsResult"
    ):
        """<p>Lists your Anycast static IP lists.</p>

        Args:
            marker: <p>Use this field when paginating results to indicate where to begin in your list. The response includes items in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of Anycast static IP lists that you want returned in the response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_anycast_ip_lists_request.ListAnycastIpListsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_anycast_ip_lists_result.ListAnycastIpListsResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_anycast_ip_lists

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_anycast_ip_lists.list_anycast_ip_lists(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_anycast_ip_lists_request.ListAnycastIpListsRequest = {}  # type: ignore[typeddict-item]
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_cache_policies(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        type: Optional[
            "aws_sdk_cloudfront.types.cache_policy_type.CachePolicyType"
        ] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_cache_policies_result.ListCachePoliciesResult":
        """<p>Gets a list of cache policies.</p> <p>You can optionally apply a filter to return only the managed policies created by Amazon Web Services, or only the custom policies created in your Amazon Web Services account.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the subsequent request.</p>

        Args:
            type: <p>A filter to return only the specified kinds of cache policies. Valid values are:</p> <ul> <li> <p> <code>managed</code> – Returns only the managed policies created by Amazon Web Services.</p> </li> <li> <p> <code>custom</code> – Returns only the custom policies created in your Amazon Web Services account.</p> </li> </ul>
            marker: <p>Use this field when paginating results to indicate where to begin in your list of cache policies. The response includes cache policies in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of cache policies that you want in the response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_cache_policies_request.ListCachePoliciesRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_cache_policies_result.ListCachePoliciesResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_cache_policies

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_cache_policies.list_cache_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_cache_policies_request.ListCachePoliciesRequest = {}  # type: ignore[typeddict-item]
        if type is not None:
            input_["type"] = type
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_cloud_front_origin_access_identities(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_cloud_front_origin_access_identities_result.ListCloudFrontOriginAccessIdentitiesResult":
        """<p>Lists origin access identities.</p>

        Args:
            marker: <p>Use this when paginating results to indicate where to begin in your list of origin access identities. The results include identities in the list that occur after the marker. To get the next page of results, set the <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response (which is also the ID of the last identity on that page).</p>
            max_items: <p>The maximum number of origin access identities you want in the response body.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_cloud_front_origin_access_identities_request.ListCloudFrontOriginAccessIdentitiesRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_cloud_front_origin_access_identities_result.ListCloudFrontOriginAccessIdentitiesResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_cloud_front_origin_access_identities

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_cloud_front_origin_access_identities.list_cloud_front_origin_access_identities(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_cloud_front_origin_access_identities_request.ListCloudFrontOriginAccessIdentitiesRequest = {}  # type: ignore[typeddict-item]
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_cloud_front_origin_access_identities(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "Iterator[aws_sdk_cloudfront.types.cloud_front_origin_access_identity_summary.CloudFrontOriginAccessIdentitySummary]":
        _token = marker
        while True:
            _response = self.list_cloud_front_origin_access_identities(
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(
                _response, ("cloud_front_origin_access_identity_list", "items")
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(
                _response, ("cloud_front_origin_access_identity_list", "next_marker")
            )
            if not _token:
                break

    def list_conflicting_aliases(
        self,
        distribution_id: "aws_sdk_cloudfront.types.distribution_id_string.distributionIdString",
        alias: "aws_sdk_cloudfront.types.alias_string.aliasString",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional[
            "aws_sdk_cloudfront.types.list_conflicting_aliases_max_items_integer.listConflictingAliasesMaxItemsInteger"
        ] = None,
    ) -> "aws_sdk_cloudfront.types.list_conflicting_aliases_result.ListConflictingAliasesResult":
        r"""<note> <p>The <code>ListConflictingAliases</code> API operation only supports standard distributions. To list domain conflicts for both standard distributions and distribution tenants, we recommend that you use the <a href=\"https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListDomainConflicts.html\">ListDomainConflicts</a> API operation instead.</p> </note> <p>Gets a list of aliases that conflict or overlap with the provided alias, and the associated CloudFront standard distribution and Amazon Web Services accounts for each conflicting alias. An alias is commonly known as a custom domain or vanity domain. It can also be called a CNAME or alternate domain name.</p> <p>In the returned list, the standard distribution and account IDs are partially hidden, which allows you to identify the standard distribution and accounts that you own, and helps to protect the information of ones that you don't own.</p> <p>Use this operation to find aliases that are in use in CloudFront that conflict or overlap with the provided alias. For example, if you provide <code>www.example.com</code> as input, the returned list can include <code>www.example.com</code> and the overlapping wildcard alternate domain name (<code>*.example.com</code>), if they exist. If you provide <code>*.example.com</code> as input, the returned list can include <code>*.example.com</code> and any alternate domain names covered by that wildcard (for example, <code>www.example.com</code>, <code>test.example.com</code>, <code>dev.example.com</code>, and so on), if they exist.</p> <p>To list conflicting aliases, specify the alias to search and the ID of a standard distribution in your account that has an attached TLS certificate that includes the provided alias. For more information, including how to set up the standard distribution and certificate, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html#alternate-domain-names-move\">Moving an alternate domain name to a different standard distribution or distribution tenant</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the subsequent request.</p>

        Args:
            distribution_id: <p>The ID of a standard distribution in your account that has an attached TLS certificate that includes the provided alias.</p>
            alias: <p>The alias (also called a CNAME) to search for conflicting aliases.</p>
            marker: <p>Use this field when paginating results to indicate where to begin in the list of conflicting aliases. The response includes conflicting aliases in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of conflicting aliases that you want in the response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_conflicting_aliases_request.ListConflictingAliasesRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_conflicting_aliases_result.ListConflictingAliasesResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_conflicting_aliases

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_conflicting_aliases.list_conflicting_aliases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_conflicting_aliases_request.ListConflictingAliasesRequest = {}  # type: ignore[typeddict-item]
        input_["distribution_id"] = distribution_id
        input_["alias"] = alias
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_connection_functions(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
        stage: Optional["aws_sdk_cloudfront.types.function_stage.FunctionStage"] = None,
    ) -> "aws_sdk_cloudfront.types.list_connection_functions_result.ListConnectionFunctionsResult":
        """<p>Lists connection functions.</p>

        Args:
            marker: <p>Use this field when paginating results to indicate where to begin in your list. The response includes items in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of connection functions that you want returned in the response.</p>
            stage: <p>The connection function's stage.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_connection_functions_request.ListConnectionFunctionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_connection_functions_result.ListConnectionFunctionsResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_connection_functions

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_connection_functions.list_connection_functions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_connection_functions_request.ListConnectionFunctionsRequest = {}  # type: ignore[typeddict-item]
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items
        if stage is not None:
            input_["stage"] = stage

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_connection_functions(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
        stage: Optional["aws_sdk_cloudfront.types.function_stage.FunctionStage"] = None,
    ) -> "Iterator[aws_sdk_cloudfront.types.connection_function_summary.ConnectionFunctionSummary]":
        _token = marker
        while True:
            _response = self.list_connection_functions(
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
                stage=stage,
            )
            _page = _resolve_path(_response, ("connection_functions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    def list_connection_groups(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        association_filter: Optional[
            "aws_sdk_cloudfront.types.connection_group_association_filter.ConnectionGroupAssociationFilter"
        ] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_connection_groups_result.ListConnectionGroupsResult":
        """<p>Lists the connection groups in your Amazon Web Services account.</p>

        Args:
            association_filter: <p>Filter by associated Anycast IP list ID.</p>
            marker: <p>The marker for the next set of connection groups to retrieve.</p>
            max_items: <p>The maximum number of connection groups to return.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_connection_groups_request.ListConnectionGroupsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_connection_groups_result.ListConnectionGroupsResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_connection_groups

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_connection_groups.list_connection_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_connection_groups_request.ListConnectionGroupsRequest = {}  # type: ignore[typeddict-item]
        if association_filter is not None:
            input_["association_filter"] = association_filter
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_connection_groups(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        association_filter: Optional[
            "aws_sdk_cloudfront.types.connection_group_association_filter.ConnectionGroupAssociationFilter"
        ] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "Iterator[aws_sdk_cloudfront.types.connection_group_summary.ConnectionGroupSummary]":
        _token = marker
        while True:
            _response = self.list_connection_groups(
                config_overrides=config_overrides,
                association_filter=association_filter,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("connection_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    def list_continuous_deployment_policies(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_continuous_deployment_policies_result.ListContinuousDeploymentPoliciesResult":
        """<p>Gets a list of the continuous deployment policies in your Amazon Web Services account.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the subsequent request.</p>

        Args:
            marker: <p>Use this field when paginating results to indicate where to begin in your list of continuous deployment policies. The response includes policies in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of continuous deployment policies that you want returned in the response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_continuous_deployment_policies_request.ListContinuousDeploymentPoliciesRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_continuous_deployment_policies_result.ListContinuousDeploymentPoliciesResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_continuous_deployment_policies

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_continuous_deployment_policies.list_continuous_deployment_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_continuous_deployment_policies_request.ListContinuousDeploymentPoliciesRequest = {}  # type: ignore[typeddict-item]
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_distributions(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_distributions_result.ListDistributionsResult":
        """<p>List CloudFront distributions.</p>

        Args:
            marker: <p>Use this when paginating results to indicate where to begin in your list of distributions. The results include distributions in the list that occur after the marker. To get the next page of results, set the <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response (which is also the ID of the last distribution on that page).</p>
            max_items: <p>The maximum number of distributions you want in the response body.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_distributions_request.ListDistributionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_distributions_result.ListDistributionsResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distributions

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distributions.list_distributions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_distributions_request.ListDistributionsRequest = {}  # type: ignore[typeddict-item]
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_distributions(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "Iterator[aws_sdk_cloudfront.types.distribution_summary.DistributionSummary]":
        _token = marker
        while True:
            _response = self.list_distributions(
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("distribution_list", "items"))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("distribution_list", "next_marker"))
            if not _token:
                break

    def list_distributions_by_anycast_ip_list_id(
        self,
        anycast_ip_list_id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_distributions_by_anycast_ip_list_id_result.ListDistributionsByAnycastIpListIdResult":
        """<p>Lists the distributions in your account that are associated with the specified <code>AnycastIpListId</code>.</p>

        Args:
            marker: <p>Use this field when paginating results to indicate where to begin in your list. The response includes items in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of distributions that you want returned in the response.</p>
            anycast_ip_list_id: <p>The ID of the Anycast static IP list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_distributions_by_anycast_ip_list_id_request.ListDistributionsByAnycastIpListIdRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_distributions_by_anycast_ip_list_id_result.ListDistributionsByAnycastIpListIdResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_anycast_ip_list_id

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_anycast_ip_list_id.list_distributions_by_anycast_ip_list_id(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_distributions_by_anycast_ip_list_id_request.ListDistributionsByAnycastIpListIdRequest = {}  # type: ignore[typeddict-item]
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items
        input_["anycast_ip_list_id"] = anycast_ip_list_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_distributions_by_cache_policy_id(
        self,
        cache_policy_id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_distributions_by_cache_policy_id_result.ListDistributionsByCachePolicyIdResult":
        """<p>Gets a list of distribution IDs for distributions that have a cache behavior that's associated with the specified cache policy.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the subsequent request.</p>

        Args:
            marker: <p>Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of distribution IDs that you want in the response.</p>
            cache_policy_id: <p>The ID of the cache policy whose associated distribution IDs you want to list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_distributions_by_cache_policy_id_request.ListDistributionsByCachePolicyIdRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_distributions_by_cache_policy_id_result.ListDistributionsByCachePolicyIdResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_cache_policy_id

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_cache_policy_id.list_distributions_by_cache_policy_id(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_distributions_by_cache_policy_id_request.ListDistributionsByCachePolicyIdRequest = {}  # type: ignore[typeddict-item]
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items
        input_["cache_policy_id"] = cache_policy_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_distributions_by_connection_function(
        self,
        connection_function_identifier: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_distributions_by_connection_function_result.ListDistributionsByConnectionFunctionResult":
        """<p>Lists distributions by connection function.</p>

        Args:
            marker: <p>Use this field when paginating results to indicate where to begin in your list. The response includes items in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of distributions that you want returned in the response.</p>
            connection_function_identifier: <p>The distributions by connection function identifier.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_distributions_by_connection_function_request.ListDistributionsByConnectionFunctionRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_distributions_by_connection_function_result.ListDistributionsByConnectionFunctionResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_connection_function

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_connection_function.list_distributions_by_connection_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_distributions_by_connection_function_request.ListDistributionsByConnectionFunctionRequest = {}  # type: ignore[typeddict-item]
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items
        input_["connection_function_identifier"] = connection_function_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_distributions_by_connection_function(
        self,
        connection_function_identifier: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "Iterator[aws_sdk_cloudfront.types.distribution_summary.DistributionSummary]":
        _token = marker
        while True:
            _response = self.list_distributions_by_connection_function(
                connection_function_identifier,
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("distribution_list", "items"))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("distribution_list", "next_marker"))
            if not _token:
                break

    def list_distributions_by_connection_mode(
        self,
        connection_mode: "aws_sdk_cloudfront.types.connection_mode.ConnectionMode",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_distributions_by_connection_mode_result.ListDistributionsByConnectionModeResult":
        """<p>Lists the distributions by the connection mode that you specify.</p>

        Args:
            marker: <p> The marker for the next set of distributions to retrieve.</p>
            max_items: <p>The maximum number of distributions to return.</p>
            connection_mode: <p>This field specifies whether the connection mode is through a standard distribution (direct) or a multi-tenant distribution with distribution tenants (tenant-only).</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_distributions_by_connection_mode_request.ListDistributionsByConnectionModeRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_distributions_by_connection_mode_result.ListDistributionsByConnectionModeResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_connection_mode

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_connection_mode.list_distributions_by_connection_mode(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_distributions_by_connection_mode_request.ListDistributionsByConnectionModeRequest = {}  # type: ignore[typeddict-item]
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items
        input_["connection_mode"] = connection_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_distributions_by_connection_mode(
        self,
        connection_mode: "aws_sdk_cloudfront.types.connection_mode.ConnectionMode",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "Iterator[aws_sdk_cloudfront.types.distribution_summary.DistributionSummary]":
        _token = marker
        while True:
            _response = self.list_distributions_by_connection_mode(
                connection_mode,
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("distribution_list", "items"))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("distribution_list", "next_marker"))
            if not _token:
                break

    def list_distributions_by_key_group(
        self,
        key_group_id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_distributions_by_key_group_result.ListDistributionsByKeyGroupResult":
        """<p>Gets a list of distribution IDs for distributions that have a cache behavior that references the specified key group.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the subsequent request.</p>

        Args:
            marker: <p>Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of distribution IDs that you want in the response.</p>
            key_group_id: <p>The ID of the key group whose associated distribution IDs you are listing.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_distributions_by_key_group_request.ListDistributionsByKeyGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_distributions_by_key_group_result.ListDistributionsByKeyGroupResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_key_group

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_key_group.list_distributions_by_key_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_distributions_by_key_group_request.ListDistributionsByKeyGroupRequest = {}  # type: ignore[typeddict-item]
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items
        input_["key_group_id"] = key_group_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_distributions_by_origin_request_policy_id(
        self,
        origin_request_policy_id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_distributions_by_origin_request_policy_id_result.ListDistributionsByOriginRequestPolicyIdResult":
        """<p>Gets a list of distribution IDs for distributions that have a cache behavior that's associated with the specified origin request policy.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the subsequent request.</p>

        Args:
            marker: <p>Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of distribution IDs that you want in the response.</p>
            origin_request_policy_id: <p>The ID of the origin request policy whose associated distribution IDs you want to list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_distributions_by_origin_request_policy_id_request.ListDistributionsByOriginRequestPolicyIdRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_distributions_by_origin_request_policy_id_result.ListDistributionsByOriginRequestPolicyIdResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_origin_request_policy_id

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_origin_request_policy_id.list_distributions_by_origin_request_policy_id(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_distributions_by_origin_request_policy_id_request.ListDistributionsByOriginRequestPolicyIdRequest = {}  # type: ignore[typeddict-item]
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items
        input_["origin_request_policy_id"] = origin_request_policy_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_distributions_by_owned_resource(
        self,
        resource_arn: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_distributions_by_owned_resource_result.ListDistributionsByOwnedResourceResult":
        """<p>Lists the CloudFront distributions that are associated with the specified resource that you own.</p>

        Args:
            resource_arn: <p>The ARN of the CloudFront resource that you've shared with other Amazon Web Services accounts.</p>
            marker: <p>Use this field when paginating results to indicate where to begin in your list of distributions. The response includes distributions in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of distributions to return.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_distributions_by_owned_resource_request.ListDistributionsByOwnedResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_distributions_by_owned_resource_result.ListDistributionsByOwnedResourceResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_owned_resource

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_owned_resource.list_distributions_by_owned_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_distributions_by_owned_resource_request.ListDistributionsByOwnedResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_distributions_by_realtime_log_config(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
        realtime_log_config_name: Optional[
            "aws_sdk_cloudfront.types.string.string"
        ] = None,
        realtime_log_config_arn: Optional[
            "aws_sdk_cloudfront.types.string.string"
        ] = None,
    ) -> "aws_sdk_cloudfront.types.list_distributions_by_realtime_log_config_result.ListDistributionsByRealtimeLogConfigResult":
        """<p>Gets a list of distributions that have a cache behavior that's associated with the specified real-time log configuration.</p> <p>You can specify the real-time log configuration by its name or its Amazon Resource Name (ARN). You must provide at least one. If you provide both, CloudFront uses the name to identify the real-time log configuration to list distributions for.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the subsequent request.</p>

        Args:
            marker: <p>Use this field when paginating results to indicate where to begin in your list of distributions. The response includes distributions in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of distributions that you want in the response.</p>
            realtime_log_config_name: <p>The name of the real-time log configuration whose associated distributions you want to list.</p>
            realtime_log_config_arn: <p>The Amazon Resource Name (ARN) of the real-time log configuration whose associated distributions you want to list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_distributions_by_realtime_log_config_request.ListDistributionsByRealtimeLogConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_distributions_by_realtime_log_config_result.ListDistributionsByRealtimeLogConfigResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_realtime_log_config

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_realtime_log_config.list_distributions_by_realtime_log_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_distributions_by_realtime_log_config_request.ListDistributionsByRealtimeLogConfigRequest = {}  # type: ignore[typeddict-item]
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items
        if realtime_log_config_name is not None:
            input_["realtime_log_config_name"] = realtime_log_config_name
        if realtime_log_config_arn is not None:
            input_["realtime_log_config_arn"] = realtime_log_config_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_distributions_by_response_headers_policy_id(
        self,
        response_headers_policy_id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_distributions_by_response_headers_policy_id_result.ListDistributionsByResponseHeadersPolicyIdResult":
        """<p>Gets a list of distribution IDs for distributions that have a cache behavior that's associated with the specified response headers policy.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the subsequent request.</p>

        Args:
            marker: <p>Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of distribution IDs that you want to get in the response.</p>
            response_headers_policy_id: <p>The ID of the response headers policy whose associated distribution IDs you want to list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_distributions_by_response_headers_policy_id_request.ListDistributionsByResponseHeadersPolicyIdRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_distributions_by_response_headers_policy_id_result.ListDistributionsByResponseHeadersPolicyIdResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_response_headers_policy_id

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_response_headers_policy_id.list_distributions_by_response_headers_policy_id(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_distributions_by_response_headers_policy_id_request.ListDistributionsByResponseHeadersPolicyIdRequest = {}  # type: ignore[typeddict-item]
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items
        input_["response_headers_policy_id"] = response_headers_policy_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_distributions_by_trust_store(
        self,
        trust_store_identifier: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_distributions_by_trust_store_result.ListDistributionsByTrustStoreResult":
        """<p>Lists distributions by trust store.</p>

        Args:
            trust_store_identifier: <p>The distributions by trust store identifier.</p>
            marker: <p>Use this field when paginating results to indicate where to begin in your list. The response includes items in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of distributions that you want returned in the response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_distributions_by_trust_store_request.ListDistributionsByTrustStoreRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_distributions_by_trust_store_result.ListDistributionsByTrustStoreResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_trust_store

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_trust_store.list_distributions_by_trust_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_distributions_by_trust_store_request.ListDistributionsByTrustStoreRequest = {}  # type: ignore[typeddict-item]
        input_["trust_store_identifier"] = trust_store_identifier
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_distributions_by_trust_store(
        self,
        trust_store_identifier: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "Iterator[aws_sdk_cloudfront.types.distribution_summary.DistributionSummary]":
        _token = marker
        while True:
            _response = self.list_distributions_by_trust_store(
                trust_store_identifier,
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("distribution_list", "items"))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("distribution_list", "next_marker"))
            if not _token:
                break

    def list_distributions_by_vpc_origin_id(
        self,
        vpc_origin_id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_distributions_by_vpc_origin_id_result.ListDistributionsByVpcOriginIdResult":
        """<p>List CloudFront distributions by their VPC origin ID.</p>

        Args:
            marker: <p>The marker associated with the VPC origin distributions list.</p>
            max_items: <p>The maximum number of items included in the list.</p>
            vpc_origin_id: <p>The VPC origin ID.</p>

        Examples:
            To list distributions by VPC origin ID
            The following command lists distributions by VPC origin ID:

            >>> client.list_distributions_by_vpc_origin_id(vpc_origin_id='vo_BQwjxxQxjCaBcQLzJUFkDM')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_distributions_by_vpc_origin_id_request.ListDistributionsByVpcOriginIdRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_distributions_by_vpc_origin_id_result.ListDistributionsByVpcOriginIdResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_vpc_origin_id

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_vpc_origin_id.list_distributions_by_vpc_origin_id(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_distributions_by_vpc_origin_id_request.ListDistributionsByVpcOriginIdRequest = {}  # type: ignore[typeddict-item]
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items
        input_["vpc_origin_id"] = vpc_origin_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_distributions_by_web_acl_id(
        self,
        web_acl_id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_distributions_by_web_acl_id_result.ListDistributionsByWebACLIdResult":
        r"""<p>List the distributions that are associated with a specified WAF web ACL.</p>

        Args:
            marker: <p>Use <code>Marker</code> and <code>MaxItems</code> to control pagination of results. If you have more than <code>MaxItems</code> distributions that satisfy the request, the response includes a <code>NextMarker</code> element. To get the next page of results, submit another request. For the value of <code>Marker</code>, specify the value of <code>NextMarker</code> from the last response. (For the first request, omit <code>Marker</code>.)</p>
            max_items: <p>The maximum number of distributions that you want CloudFront to return in the response body. The maximum and default values are both 100.</p>
            web_acl_id: <p>The ID of the WAF web ACL that you want to list the associated distributions. If you specify \"null\" for the ID, the request returns a list of the distributions that aren't associated with a web ACL. </p> <p>For WAFV2, this is the ARN of the web ACL, such as <code>arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111</code>.</p> <p>For WAF Classic, this is the ID of the web ACL, such as <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE11111</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_distributions_by_web_acl_id_request.ListDistributionsByWebACLIdRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_distributions_by_web_acl_id_result.ListDistributionsByWebACLIdResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_web_acl_id

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_web_acl_id.list_distributions_by_web_acl_id(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_distributions_by_web_acl_id_request.ListDistributionsByWebACLIdRequest = {}  # type: ignore[typeddict-item]
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items
        input_["web_acl_id"] = web_acl_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_distribution_tenants(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        association_filter: Optional[
            "aws_sdk_cloudfront.types.distribution_tenant_association_filter.DistributionTenantAssociationFilter"
        ] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_distribution_tenants_result.ListDistributionTenantsResult":
        """<p>Lists the distribution tenants in your Amazon Web Services account.</p>

        Args:
            marker: <p>The marker for the next set of results.</p>
            max_items: <p>The maximum number of distribution tenants to return.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_distribution_tenants_request.ListDistributionTenantsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_distribution_tenants_result.ListDistributionTenantsResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distribution_tenants

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distribution_tenants.list_distribution_tenants(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_distribution_tenants_request.ListDistributionTenantsRequest = {}  # type: ignore[typeddict-item]
        if association_filter is not None:
            input_["association_filter"] = association_filter
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_distribution_tenants(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        association_filter: Optional[
            "aws_sdk_cloudfront.types.distribution_tenant_association_filter.DistributionTenantAssociationFilter"
        ] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "Iterator[aws_sdk_cloudfront.types.distribution_tenant_summary.DistributionTenantSummary]":
        _token = marker
        while True:
            _response = self.list_distribution_tenants(
                config_overrides=config_overrides,
                association_filter=association_filter,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("distribution_tenant_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    def list_distribution_tenants_by_customization(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        web_acl_arn: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        certificate_arn: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_distribution_tenants_by_customization_result.ListDistributionTenantsByCustomizationResult":
        """<p>Lists distribution tenants by the customization that you specify.</p> <p>You must specify either the <code>CertificateArn</code> parameter or <code>WebACLArn</code> parameter, but not both in the same request.</p>

        Args:
            web_acl_arn: <p>Filter by the ARN of the associated WAF web ACL.</p>
            certificate_arn: <p>Filter by the ARN of the associated ACM certificate.</p>
            marker: <p>The marker for the next set of results.</p>
            max_items: <p>The maximum number of distribution tenants to return by the specified customization.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_distribution_tenants_by_customization_request.ListDistributionTenantsByCustomizationRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_distribution_tenants_by_customization_result.ListDistributionTenantsByCustomizationResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distribution_tenants_by_customization

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_distribution_tenants_by_customization.list_distribution_tenants_by_customization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_distribution_tenants_by_customization_request.ListDistributionTenantsByCustomizationRequest = {}  # type: ignore[typeddict-item]
        if web_acl_arn is not None:
            input_["web_acl_arn"] = web_acl_arn
        if certificate_arn is not None:
            input_["certificate_arn"] = certificate_arn
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_distribution_tenants_by_customization(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        web_acl_arn: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        certificate_arn: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "Iterator[aws_sdk_cloudfront.types.distribution_tenant_summary.DistributionTenantSummary]":
        _token = marker
        while True:
            _response = self.list_distribution_tenants_by_customization(
                config_overrides=config_overrides,
                web_acl_arn=web_acl_arn,
                certificate_arn=certificate_arn,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("distribution_tenant_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    def list_domain_conflicts(
        self,
        domain: "aws_sdk_cloudfront.types.string.string",
        domain_control_validation_resource: "aws_sdk_cloudfront.types.distribution_resource_id.DistributionResourceId",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> "aws_sdk_cloudfront.types.list_domain_conflicts_result.ListDomainConflictsResult":
        r"""<note> <p>We recommend that you use the <code>ListDomainConflicts</code> API operation to check for domain conflicts, as it supports both standard distributions and distribution tenants. <a href=\"https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListConflictingAliases.html\">ListConflictingAliases</a> performs similar checks but only supports standard distributions.</p> </note> <p>Lists existing domain associations that conflict with the domain that you specify.</p> <p>You can use this API operation to identify potential domain conflicts when moving domains between standard distributions and/or distribution tenants. Domain conflicts must be resolved first before they can be moved. </p> <p>For example, if you provide <code>www.example.com</code> as input, the returned list can include <code>www.example.com</code> and the overlapping wildcard alternate domain name (<code>*.example.com</code>), if they exist. If you provide <code>*.example.com</code> as input, the returned list can include <code>*.example.com</code> and any alternate domain names covered by that wildcard (for example, <code>www.example.com</code>, <code>test.example.com</code>, <code>dev.example.com</code>, and so on), if they exist.</p> <p>To list conflicting domains, specify the following:</p> <ul> <li> <p>The domain to search for</p> </li> <li> <p>The ID of a standard distribution or distribution tenant in your account that has an attached TLS certificate, which covers the specified domain</p> </li> </ul> <p>For more information, including how to set up the standard distribution or distribution tenant, and the certificate, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html#alternate-domain-names-move\">Moving an alternate domain name to a different standard distribution or distribution tenant</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the subsequent request.</p>

        Args:
            domain: <p>The domain to check for conflicts.</p>
            domain_control_validation_resource: <p>The distribution resource identifier. This can be the standard distribution or distribution tenant that has a valid certificate, which covers the domain that you specify.</p>
            max_items: <p>The maximum number of domain conflicts to return.</p>
            marker: <p>The marker for the next set of domain conflicts.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_domain_conflicts_request.ListDomainConflictsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_domain_conflicts_result.ListDomainConflictsResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_domain_conflicts

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_domain_conflicts.list_domain_conflicts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_domain_conflicts_request.ListDomainConflictsRequest = {}  # type: ignore[typeddict-item]
        input_["domain"] = domain
        input_["domain_control_validation_resource"] = (
            domain_control_validation_resource
        )
        if max_items is not None:
            input_["max_items"] = max_items
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_domain_conflicts(
        self,
        domain: "aws_sdk_cloudfront.types.string.string",
        domain_control_validation_resource: "aws_sdk_cloudfront.types.distribution_resource_id.DistributionResourceId",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> "Iterator[aws_sdk_cloudfront.types.domain_conflict.DomainConflict]":
        _token = marker
        while True:
            _response = self.list_domain_conflicts(
                domain,
                domain_control_validation_resource,
                config_overrides=config_overrides,
                max_items=max_items,
                marker=_token,
            )
            _page = _resolve_path(_response, ("domain_conflicts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    def list_field_level_encryption_configs(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_field_level_encryption_configs_result.ListFieldLevelEncryptionConfigsResult":
        """<p>List all field-level encryption configurations that have been created in CloudFront for this account.</p>

        Args:
            marker: <p>Use this when paginating results to indicate where to begin in your list of configurations. The results include configurations in the list that occur after the marker. To get the next page of results, set the <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response (which is also the ID of the last configuration on that page).</p>
            max_items: <p>The maximum number of field-level encryption configurations you want in the response body.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_field_level_encryption_configs_request.ListFieldLevelEncryptionConfigsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_field_level_encryption_configs_result.ListFieldLevelEncryptionConfigsResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_field_level_encryption_configs

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_field_level_encryption_configs.list_field_level_encryption_configs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_field_level_encryption_configs_request.ListFieldLevelEncryptionConfigsRequest = {}  # type: ignore[typeddict-item]
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_field_level_encryption_profiles(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_field_level_encryption_profiles_result.ListFieldLevelEncryptionProfilesResult":
        """<p>Request a list of field-level encryption profiles that have been created in CloudFront for this account.</p>

        Args:
            marker: <p>Use this when paginating results to indicate where to begin in your list of profiles. The results include profiles in the list that occur after the marker. To get the next page of results, set the <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response (which is also the ID of the last profile on that page).</p>
            max_items: <p>The maximum number of field-level encryption profiles you want in the response body. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_field_level_encryption_profiles_request.ListFieldLevelEncryptionProfilesRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_field_level_encryption_profiles_result.ListFieldLevelEncryptionProfilesResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_field_level_encryption_profiles

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_field_level_encryption_profiles.list_field_level_encryption_profiles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_field_level_encryption_profiles_request.ListFieldLevelEncryptionProfilesRequest = {}  # type: ignore[typeddict-item]
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_functions(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
        stage: Optional["aws_sdk_cloudfront.types.function_stage.FunctionStage"] = None,
    ) -> "aws_sdk_cloudfront.types.list_functions_result.ListFunctionsResult":
        """<p>Gets a list of all CloudFront functions in your Amazon Web Services account.</p> <p>You can optionally apply a filter to return only the functions that are in the specified stage, either <code>DEVELOPMENT</code> or <code>LIVE</code>.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the subsequent request.</p>

        Args:
            marker: <p>Use this field when paginating results to indicate where to begin in your list of functions. The response includes functions in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of functions that you want in the response.</p>
            stage: <p>An optional filter to return only the functions that are in the specified stage, either <code>DEVELOPMENT</code> or <code>LIVE</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_functions_request.ListFunctionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_functions_result.ListFunctionsResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_functions

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_functions.list_functions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_functions_request.ListFunctionsRequest = {}  # type: ignore[typeddict-item]
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items
        if stage is not None:
            input_["stage"] = stage

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_invalidations(
        self,
        distribution_id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_invalidations_result.ListInvalidationsResult":
        """<p>Lists invalidation batches.</p>

        Args:
            distribution_id: <p>The distribution's ID.</p>
            marker: <p>Use this parameter when paginating results to indicate where to begin in your list of invalidation batches. Because the results are returned in decreasing order from most recent to oldest, the most recent results are on the first page, the second page will contain earlier results, and so on. To get the next page of results, set <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response. This value is the same as the ID of the last invalidation batch on that page.</p>
            max_items: <p>The maximum number of invalidation batches that you want in the response body.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_invalidations_request.ListInvalidationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_invalidations_result.ListInvalidationsResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_invalidations

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_invalidations.list_invalidations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_invalidations_request.ListInvalidationsRequest = {}  # type: ignore[typeddict-item]
        input_["distribution_id"] = distribution_id
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_invalidations(
        self,
        distribution_id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "Iterator[aws_sdk_cloudfront.types.invalidation_summary.InvalidationSummary]":
        _token = marker
        while True:
            _response = self.list_invalidations(
                distribution_id,
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("invalidation_list", "items"))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("invalidation_list", "next_marker"))
            if not _token:
                break

    def list_invalidations_for_distribution_tenant(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_invalidations_for_distribution_tenant_result.ListInvalidationsForDistributionTenantResult":
        """<p>Lists the invalidations for a distribution tenant.</p>

        Args:
            id: <p>The ID of the distribution tenant.</p>
            marker: <p>Use this parameter when paginating results to indicate where to begin in your list of invalidation batches. Because the results are returned in decreasing order from most recent to oldest, the most recent results are on the first page, the second page will contain earlier results, and so on. To get the next page of results, set <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response. This value is the same as the ID of the last invalidation batch on that page.</p>
            max_items: <p>The maximum number of invalidations to return for the distribution tenant.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_invalidations_for_distribution_tenant_request.ListInvalidationsForDistributionTenantRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_invalidations_for_distribution_tenant_result.ListInvalidationsForDistributionTenantResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_invalidations_for_distribution_tenant

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_invalidations_for_distribution_tenant.list_invalidations_for_distribution_tenant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_invalidations_for_distribution_tenant_request.ListInvalidationsForDistributionTenantRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_invalidations_for_distribution_tenant(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "Iterator[aws_sdk_cloudfront.types.invalidation_summary.InvalidationSummary]":
        _token = marker
        while True:
            _response = self.list_invalidations_for_distribution_tenant(
                id,
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("invalidation_list", "items"))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("invalidation_list", "next_marker"))
            if not _token:
                break

    def list_key_groups(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_key_groups_result.ListKeyGroupsResult":
        """<p>Gets a list of key groups.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the subsequent request.</p>

        Args:
            marker: <p>Use this field when paginating results to indicate where to begin in your list of key groups. The response includes key groups in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of key groups that you want in the response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_key_groups_request.ListKeyGroupsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_key_groups_result.ListKeyGroupsResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_key_groups

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_key_groups.list_key_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_key_groups_request.ListKeyGroupsRequest = {}  # type: ignore[typeddict-item]
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_key_value_stores(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
        status: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> (
        "aws_sdk_cloudfront.types.list_key_value_stores_result.ListKeyValueStoresResult"
    ):
        """<p>Specifies the key value stores to list.</p>

        Args:
            marker: <p>The marker associated with the key value stores list.</p>
            max_items: <p>The maximum number of items in the key value stores list.</p>
            status: <p>The status of the request for the key value stores list.</p>

        Examples:
            To get a list of KeyValueStores
            The following command retrieves a list of KeyValueStores with READY status.

            >>> client.list_key_value_stores(status='READY')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_key_value_stores_request.ListKeyValueStoresRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_key_value_stores_result.ListKeyValueStoresResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_key_value_stores

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_key_value_stores.list_key_value_stores(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_key_value_stores_request.ListKeyValueStoresRequest = {}  # type: ignore[typeddict-item]
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_key_value_stores(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
        status: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> "Iterator[aws_sdk_cloudfront.types.key_value_store.KeyValueStore]":
        _token = marker
        while True:
            _response = self.list_key_value_stores(
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
                status=status,
            )
            _page = _resolve_path(_response, ("key_value_store_list", "items"))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("key_value_store_list", "next_marker"))
            if not _token:
                break

    def list_origin_access_controls(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_origin_access_controls_result.ListOriginAccessControlsResult":
        """<p>Gets the list of CloudFront origin access controls (OACs) in this Amazon Web Services account.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send another request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the next request.</p> <note> <p>If you're not using origin access controls for your Amazon Web Services account, the <code>ListOriginAccessControls</code> operation doesn't return the <code>Items</code> element in the response.</p> </note>

        Args:
            marker: <p>Use this field when paginating results to indicate where to begin in your list of origin access controls. The response includes the items in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of origin access controls that you want in the response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_origin_access_controls_request.ListOriginAccessControlsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_origin_access_controls_result.ListOriginAccessControlsResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_origin_access_controls

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_origin_access_controls.list_origin_access_controls(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_origin_access_controls_request.ListOriginAccessControlsRequest = {}  # type: ignore[typeddict-item]
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_origin_access_controls(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "Iterator[aws_sdk_cloudfront.types.origin_access_control_summary.OriginAccessControlSummary]":
        _token = marker
        while True:
            _response = self.list_origin_access_controls(
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("origin_access_control_list", "items"))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(
                _response, ("origin_access_control_list", "next_marker")
            )
            if not _token:
                break

    def list_origin_request_policies(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        type: Optional[
            "aws_sdk_cloudfront.types.origin_request_policy_type.OriginRequestPolicyType"
        ] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_origin_request_policies_result.ListOriginRequestPoliciesResult":
        """<p>Gets a list of origin request policies.</p> <p>You can optionally apply a filter to return only the managed policies created by Amazon Web Services, or only the custom policies created in your Amazon Web Services account.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the subsequent request.</p>

        Args:
            type: <p>A filter to return only the specified kinds of origin request policies. Valid values are:</p> <ul> <li> <p> <code>managed</code> – Returns only the managed policies created by Amazon Web Services.</p> </li> <li> <p> <code>custom</code> – Returns only the custom policies created in your Amazon Web Services account.</p> </li> </ul>
            marker: <p>Use this field when paginating results to indicate where to begin in your list of origin request policies. The response includes origin request policies in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of origin request policies that you want in the response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_origin_request_policies_request.ListOriginRequestPoliciesRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_origin_request_policies_result.ListOriginRequestPoliciesResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_origin_request_policies

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_origin_request_policies.list_origin_request_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_origin_request_policies_request.ListOriginRequestPoliciesRequest = {}  # type: ignore[typeddict-item]
        if type is not None:
            input_["type"] = type
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_public_keys(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_public_keys_result.ListPublicKeysResult":
        """<p>List all public keys that have been added to CloudFront for this account.</p>

        Args:
            marker: <p>Use this when paginating results to indicate where to begin in your list of public keys. The results include public keys in the list that occur after the marker. To get the next page of results, set the <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response (which is also the ID of the last public key on that page).</p>
            max_items: <p>The maximum number of public keys you want in the response body.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_public_keys_request.ListPublicKeysRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_public_keys_result.ListPublicKeysResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_public_keys

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_public_keys.list_public_keys(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_public_keys_request.ListPublicKeysRequest = {}  # type: ignore[typeddict-item]
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_public_keys(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "Iterator[aws_sdk_cloudfront.types.public_key_summary.PublicKeySummary]":
        _token = marker
        while True:
            _response = self.list_public_keys(
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("public_key_list", "items"))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("public_key_list", "next_marker"))
            if not _token:
                break

    def list_realtime_log_configs(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> "aws_sdk_cloudfront.types.list_realtime_log_configs_result.ListRealtimeLogConfigsResult":
        """<p>Gets a list of real-time log configurations.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the subsequent request.</p>

        Args:
            max_items: <p>The maximum number of real-time log configurations that you want in the response.</p>
            marker: <p>Use this field when paginating results to indicate where to begin in your list of real-time log configurations. The response includes real-time log configurations in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_realtime_log_configs_request.ListRealtimeLogConfigsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_realtime_log_configs_result.ListRealtimeLogConfigsResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_realtime_log_configs

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_realtime_log_configs.list_realtime_log_configs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_realtime_log_configs_request.ListRealtimeLogConfigsRequest = {}  # type: ignore[typeddict-item]
        if max_items is not None:
            input_["max_items"] = max_items
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_response_headers_policies(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        type: Optional[
            "aws_sdk_cloudfront.types.response_headers_policy_type.ResponseHeadersPolicyType"
        ] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_response_headers_policies_result.ListResponseHeadersPoliciesResult":
        """<p>Gets a list of response headers policies.</p> <p>You can optionally apply a filter to get only the managed policies created by Amazon Web Services, or only the custom policies created in your Amazon Web Services account.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the subsequent request.</p>

        Args:
            type: <p>A filter to get only the specified kind of response headers policies. Valid values are:</p> <ul> <li> <p> <code>managed</code> – Gets only the managed policies created by Amazon Web Services.</p> </li> <li> <p> <code>custom</code> – Gets only the custom policies created in your Amazon Web Services account.</p> </li> </ul>
            marker: <p>Use this field when paginating results to indicate where to begin in your list of response headers policies. The response includes response headers policies in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of response headers policies that you want to get in the response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_response_headers_policies_request.ListResponseHeadersPoliciesRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_response_headers_policies_result.ListResponseHeadersPoliciesResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_response_headers_policies

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_response_headers_policies.list_response_headers_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_response_headers_policies_request.ListResponseHeadersPoliciesRequest = {}  # type: ignore[typeddict-item]
        if type is not None:
            input_["type"] = type
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_streaming_distributions(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_streaming_distributions_result.ListStreamingDistributionsResult":
        """<p>List streaming distributions.</p>

        Args:
            marker: <p>The value that you provided for the <code>Marker</code> request parameter.</p>
            max_items: <p>The value that you provided for the <code>MaxItems</code> request parameter.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_streaming_distributions_request.ListStreamingDistributionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_streaming_distributions_result.ListStreamingDistributionsResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_streaming_distributions

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_streaming_distributions.list_streaming_distributions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_streaming_distributions_request.ListStreamingDistributionsRequest = {}  # type: ignore[typeddict-item]
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_streaming_distributions(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "Iterator[aws_sdk_cloudfront.types.streaming_distribution_summary.StreamingDistributionSummary]":
        _token = marker
        while True:
            _response = self.list_streaming_distributions(
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("streaming_distribution_list", "items"))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(
                _response, ("streaming_distribution_list", "next_marker")
            )
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource: "aws_sdk_cloudfront.types.resource_arn.ResourceARN",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.list_tags_for_resource_result.ListTagsForResourceResult":
        r"""<p>List tags for a CloudFront resource. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/tagging.html\">Tagging a distribution</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            resource: <p>An ARN of a CloudFront resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_tags_for_resource_result.ListTagsForResourceResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_tags_for_resource

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource"] = resource

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_trust_stores(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_trust_stores_result.ListTrustStoresResult":
        """<p>Lists trust stores.</p>

        Args:
            marker: <p>Use this field when paginating results to indicate where to begin in your list. The response includes items in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of trust stores that you want returned in the response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_trust_stores_request.ListTrustStoresRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_trust_stores_result.ListTrustStoresResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_trust_stores

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_trust_stores.list_trust_stores(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_trust_stores_request.ListTrustStoresRequest = {}  # type: ignore[typeddict-item]
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_trust_stores(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "Iterator[aws_sdk_cloudfront.types.trust_store_summary.TrustStoreSummary]":
        _token = marker
        while True:
            _response = self.list_trust_stores(
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("trust_store_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    def list_vpc_origins(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        max_items: Optional["aws_sdk_cloudfront.types.integer.integer"] = None,
    ) -> "aws_sdk_cloudfront.types.list_vpc_origins_result.ListVpcOriginsResult":
        """<p>List the CloudFront VPC origins in your account.</p>

        Args:
            marker: <p>The marker associated with the VPC origins list.</p>
            max_items: <p>The maximum number of items included in the list.</p>

        Examples:
            To list VPC origins
            The following command lists VPC origins:

            >>> client.list_vpc_origins()
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.list_vpc_origins_request.ListVpcOriginsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.list_vpc_origins_result.ListVpcOriginsResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_vpc_origins

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.list_vpc_origins.list_vpc_origins(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.list_vpc_origins_request.ListVpcOriginsRequest = {}  # type: ignore[typeddict-item]
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def publish_connection_function(
        self,
        id: "aws_sdk_cloudfront.types.resource_id.ResourceId",
        if_match: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.publish_connection_function_result.PublishConnectionFunctionResult":
        """<p>Publishes a connection function.</p>

        Args:
            id: <p>The connection function ID.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the connection function.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.publish_connection_function_request.PublishConnectionFunctionRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.publish_connection_function_result.PublishConnectionFunctionResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.publish_connection_function

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.publish_connection_function.publish_connection_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.publish_connection_function_request.PublishConnectionFunctionRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def publish_function(
        self,
        name: "aws_sdk_cloudfront.types.function_name.FunctionName",
        if_match: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.publish_function_result.PublishFunctionResult":
        """<p>Publishes a CloudFront function by copying the function code from the <code>DEVELOPMENT</code> stage to <code>LIVE</code>. This automatically updates all cache behaviors that are using this function to use the newly published copy in the <code>LIVE</code> stage.</p> <p>When a function is published to the <code>LIVE</code> stage, you can attach the function to a distribution's cache behavior, using the function's Amazon Resource Name (ARN).</p> <p>To publish a function, you must provide the function's name and version (<code>ETag</code> value). To get these values, you can use <code>ListFunctions</code> and <code>DescribeFunction</code>.</p>

        Args:
            name: <p>The name of the function that you are publishing.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the function that you are publishing, which you can get using <code>DescribeFunction</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.publish_function_request.PublishFunctionRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.publish_function_result.PublishFunctionResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.publish_function

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.publish_function.publish_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.publish_function_request.PublishFunctionRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_resource_policy(
        self,
        resource_arn: "aws_sdk_cloudfront.types.string.string",
        policy_document: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.put_resource_policy_result.PutResourcePolicyResult":
        """<p>Creates a resource control policy for a given CloudFront resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the CloudFront resource for which the policy is being created.</p>
            policy_document: <p>The JSON-formatted resource policy to create.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.put_resource_policy_result.PutResourcePolicyResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.put_resource_policy

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.put_resource_policy.put_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.put_resource_policy_request.PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["policy_document"] = policy_document

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource: "aws_sdk_cloudfront.types.resource_arn.ResourceARN",
        tags: "aws_sdk_cloudfront.types.tags.Tags",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> None:
        r"""<p>Add tags to a CloudFront resource. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/tagging.html\">Tagging a distribution</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            resource: <p>An ARN of a CloudFront resource.</p>
            tags: <p>A complex type that contains zero or more <code>Tag</code> elements.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.tag_resource

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource"] = resource
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def test_connection_function(
        self,
        id: "aws_sdk_cloudfront.types.resource_id.ResourceId",
        if_match: "aws_sdk_cloudfront.types.string.string",
        connection_object: "aws_sdk_cloudfront.types.function_event_object.FunctionEventObject",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        stage: Optional["aws_sdk_cloudfront.types.function_stage.FunctionStage"] = None,
    ) -> "aws_sdk_cloudfront.types.test_connection_function_result.TestConnectionFunctionResult":
        """<p>Tests a connection function.</p>

        Args:
            id: <p>The connection function ID.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the connection function.</p>
            stage: <p>The connection function stage.</p>
            connection_object: <p>The connection object.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.test_connection_function_request.TestConnectionFunctionRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.test_connection_function_result.TestConnectionFunctionResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.test_connection_function

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.test_connection_function.test_connection_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.test_connection_function_request.TestConnectionFunctionRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["if_match"] = if_match
        if stage is not None:
            input_["stage"] = stage
        input_["connection_object"] = connection_object

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def test_function(
        self,
        name: "aws_sdk_cloudfront.types.function_name.FunctionName",
        if_match: "aws_sdk_cloudfront.types.string.string",
        event_object: "aws_sdk_cloudfront.types.function_event_object.FunctionEventObject",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        stage: Optional["aws_sdk_cloudfront.types.function_stage.FunctionStage"] = None,
    ) -> "aws_sdk_cloudfront.types.test_function_result.TestFunctionResult":
        r"""<p>Tests a CloudFront function.</p> <p>To test a function, you provide an <i>event object</i> that represents an HTTP request or response that your CloudFront distribution could receive in production. CloudFront runs the function, passing it the event object that you provided, and returns the function's result (the modified event object) in the response. The response also contains function logs and error messages, if any exist. For more information about testing functions, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/managing-functions.html#test-function\">Testing functions</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>To test a function, you provide the function's name and version (<code>ETag</code> value) along with the event object. To get the function's name and version, you can use <code>ListFunctions</code> and <code>DescribeFunction</code>.</p>

        Args:
            name: <p>The name of the function that you are testing.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the function that you are testing, which you can get using <code>DescribeFunction</code>.</p>
            stage: <p>The stage of the function that you are testing, either <code>DEVELOPMENT</code> or <code>LIVE</code>.</p>
            event_object: <p>The event object to test the function with. For more information about the structure of the event object, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/managing-functions.html#test-function\">Testing functions</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.test_function_request.TestFunctionRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.test_function_result.TestFunctionResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.test_function

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.test_function.test_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.test_function_request.TestFunctionRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["if_match"] = if_match
        if stage is not None:
            input_["stage"] = stage
        input_["event_object"] = event_object

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource: "aws_sdk_cloudfront.types.resource_arn.ResourceARN",
        tag_keys: "aws_sdk_cloudfront.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> None:
        r"""<p>Remove tags from a CloudFront resource. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/tagging.html\">Tagging a distribution</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            resource: <p>An ARN of a CloudFront resource.</p>
            tag_keys: <p>A complex type that contains zero or more <code>Tag</code> key elements.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.untag_resource

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource"] = resource
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_anycast_ip_list(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        if_match: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        ip_address_type: Optional[
            "aws_sdk_cloudfront.types.ip_address_type.IpAddressType"
        ] = None,
        ipam_cidr_configs: Optional[
            "aws_sdk_cloudfront.types.ipam_cidr_config_list.IpamCidrConfigList"
        ] = None,
    ) -> "aws_sdk_cloudfront.types.update_anycast_ip_list_result.UpdateAnycastIpListResult":
        """<p>Updates an Anycast static IP list.</p>

        Args:
            id: <p>The ID of the Anycast static IP list.</p>
            ip_address_type: <p>The IP address type for the Anycast static IP list. You can specify one of the following options:</p> <ul> <li> <p> <code>ipv4</code> only</p> </li> <li> <p> <code>ipv6</code> only</p> </li> <li> <p> <code>dualstack</code> - Allocate a list of both IPv4 and IPv6 addresses</p> </li> </ul>
            ipam_cidr_configs: <p>A list of IPAM CIDR configurations that specify the IP address ranges and IPAM pool settings for updating the Anycast static IP list.</p>
            if_match: <p>The current version (ETag value) of the Anycast static IP list that you are updating.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.update_anycast_ip_list_request.UpdateAnycastIpListRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.update_anycast_ip_list_result.UpdateAnycastIpListResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_anycast_ip_list

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_anycast_ip_list.update_anycast_ip_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.update_anycast_ip_list_request.UpdateAnycastIpListRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if ipam_cidr_configs is not None:
            input_["ipam_cidr_configs"] = ipam_cidr_configs
        input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_cache_policy(
        self,
        cache_policy_config: "aws_sdk_cloudfront.types.cache_policy_config.CachePolicyConfig",
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> "aws_sdk_cloudfront.types.update_cache_policy_result.UpdateCachePolicyResult":
        """<p>Updates a cache policy configuration.</p> <p>When you update a cache policy configuration, all the fields are updated with the values provided in the request. You cannot update some fields independent of others. To update a cache policy configuration:</p> <ol> <li> <p>Use <code>GetCachePolicyConfig</code> to get the current configuration.</p> </li> <li> <p>Locally modify the fields in the cache policy configuration that you want to update.</p> </li> <li> <p>Call <code>UpdateCachePolicy</code> by providing the entire cache policy configuration, including the fields that you modified and those that you didn't.</p> </li> </ol> <important> <p>If your minimum TTL is greater than 0, CloudFront will cache content for at least the duration specified in the cache policy's minimum TTL, even if the <code>Cache-Control: no-cache</code>, <code>no-store</code>, or <code>private</code> directives are present in the origin headers.</p> </important>

        Args:
            cache_policy_config: <p>A cache policy configuration.</p>
            id: <p>The unique identifier for the cache policy that you are updating. The identifier is returned in a cache behavior's <code>CachePolicyId</code> field in the response to <code>GetDistributionConfig</code>.</p>
            if_match: <p>The version of the cache policy that you are updating. The version is returned in the cache policy's <code>ETag</code> field in the response to <code>GetCachePolicyConfig</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.update_cache_policy_request.UpdateCachePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.update_cache_policy_result.UpdateCachePolicyResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_cache_policy

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_cache_policy.update_cache_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.update_cache_policy_request.UpdateCachePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["cache_policy_config"] = cache_policy_config
        input_["id"] = id
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_cloud_front_origin_access_identity(
        self,
        cloud_front_origin_access_identity_config: "aws_sdk_cloudfront.types.cloud_front_origin_access_identity_config.CloudFrontOriginAccessIdentityConfig",
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> "aws_sdk_cloudfront.types.update_cloud_front_origin_access_identity_result.UpdateCloudFrontOriginAccessIdentityResult":
        """<p>Update an origin access identity.</p>

        Args:
            cloud_front_origin_access_identity_config: <p>The identity's configuration information.</p>
            id: <p>The identity's id.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the identity's configuration. For example: <code>E2QWRUHAPOMQZL</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.update_cloud_front_origin_access_identity_request.UpdateCloudFrontOriginAccessIdentityRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.update_cloud_front_origin_access_identity_result.UpdateCloudFrontOriginAccessIdentityResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_cloud_front_origin_access_identity

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_cloud_front_origin_access_identity.update_cloud_front_origin_access_identity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.update_cloud_front_origin_access_identity_request.UpdateCloudFrontOriginAccessIdentityRequest = {}  # type: ignore[typeddict-item]
        input_["cloud_front_origin_access_identity_config"] = (
            cloud_front_origin_access_identity_config
        )
        input_["id"] = id
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_connection_function(
        self,
        id: "aws_sdk_cloudfront.types.resource_id.ResourceId",
        if_match: "aws_sdk_cloudfront.types.string.string",
        connection_function_config: "aws_sdk_cloudfront.types.function_config.FunctionConfig",
        connection_function_code: "aws_sdk_cloudfront.types.function_blob.FunctionBlob",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.update_connection_function_result.UpdateConnectionFunctionResult":
        """<p>Updates a connection function.</p>

        Args:
            id: <p>The connection function ID.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the connection function you are updating.</p>
            connection_function_code: <p>The connection function code.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.update_connection_function_request.UpdateConnectionFunctionRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.update_connection_function_result.UpdateConnectionFunctionResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_connection_function

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_connection_function.update_connection_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.update_connection_function_request.UpdateConnectionFunctionRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["if_match"] = if_match
        input_["connection_function_config"] = connection_function_config
        input_["connection_function_code"] = connection_function_code

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_connection_group(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        if_match: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        ipv6_enabled: Optional["aws_sdk_cloudfront.types.boolean.boolean"] = None,
        anycast_ip_list_id: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        enabled: Optional["aws_sdk_cloudfront.types.boolean.boolean"] = None,
    ) -> "aws_sdk_cloudfront.types.update_connection_group_result.UpdateConnectionGroupResult":
        r"""<p>Updates a connection group.</p>

        Args:
            id: <p>The ID of the connection group.</p>
            ipv6_enabled: <p>Enable IPv6 for the connection group. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesEnableIPv6\">Enable IPv6</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the connection group that you're updating.</p>
            anycast_ip_list_id: <p>The ID of the Anycast static IP list.</p>
            enabled: <p>Whether the connection group is enabled.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.update_connection_group_request.UpdateConnectionGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.update_connection_group_result.UpdateConnectionGroupResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_connection_group

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_connection_group.update_connection_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.update_connection_group_request.UpdateConnectionGroupRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if ipv6_enabled is not None:
            input_["ipv6_enabled"] = ipv6_enabled
        input_["if_match"] = if_match
        if anycast_ip_list_id is not None:
            input_["anycast_ip_list_id"] = anycast_ip_list_id
        if enabled is not None:
            input_["enabled"] = enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_continuous_deployment_policy(
        self,
        continuous_deployment_policy_config: "aws_sdk_cloudfront.types.continuous_deployment_policy_config.ContinuousDeploymentPolicyConfig",
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> "aws_sdk_cloudfront.types.update_continuous_deployment_policy_result.UpdateContinuousDeploymentPolicyResult":
        """<p>Updates a continuous deployment policy. You can update a continuous deployment policy to enable or disable it, to change the percentage of traffic that it sends to the staging distribution, or to change the staging distribution that it sends traffic to.</p> <p>When you update a continuous deployment policy configuration, all the fields are updated with the values that are provided in the request. You cannot update some fields independent of others. To update a continuous deployment policy configuration:</p> <ol> <li> <p>Use <code>GetContinuousDeploymentPolicyConfig</code> to get the current configuration.</p> </li> <li> <p>Locally modify the fields in the continuous deployment policy configuration that you want to update.</p> </li> <li> <p>Use <code>UpdateContinuousDeploymentPolicy</code>, providing the entire continuous deployment policy configuration, including the fields that you modified and those that you didn't.</p> </li> </ol>

        Args:
            continuous_deployment_policy_config: <p>The continuous deployment policy configuration.</p>
            id: <p>The identifier of the continuous deployment policy that you are updating.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the continuous deployment policy that you are updating.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.update_continuous_deployment_policy_request.UpdateContinuousDeploymentPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.update_continuous_deployment_policy_result.UpdateContinuousDeploymentPolicyResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_continuous_deployment_policy

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_continuous_deployment_policy.update_continuous_deployment_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.update_continuous_deployment_policy_request.UpdateContinuousDeploymentPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["continuous_deployment_policy_config"] = (
            continuous_deployment_policy_config
        )
        input_["id"] = id
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_distribution(
        self,
        distribution_config: "aws_sdk_cloudfront.types.distribution_config.DistributionConfig",
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> "aws_sdk_cloudfront.types.update_distribution_result.UpdateDistributionResult":
        """<p>Updates the configuration for a CloudFront distribution.</p> <p>The update process includes getting the current distribution configuration, updating it to make your changes, and then submitting an <code>UpdateDistribution</code> request to make the updates.</p> <p> <b>To update a web distribution using the CloudFront API</b> </p> <ol> <li> <p>Use <code>GetDistributionConfig</code> to get the current configuration, including the version identifier (<code>ETag</code>).</p> </li> <li> <p>Update the distribution configuration that was returned in the response. Note the following important requirements and restrictions:</p> <ul> <li> <p>You must copy the <code>ETag</code> field value from the response. (You'll use it for the <code>IfMatch</code> parameter in your request.) Then, remove the <code>ETag</code> field from the distribution configuration.</p> </li> <li> <p>You can't change the value of <code>CallerReference</code>.</p> </li> </ul> </li> <li> <p>Submit an <code>UpdateDistribution</code> request, providing the updated distribution configuration. The new configuration replaces the existing configuration. The values that you specify in an <code>UpdateDistribution</code> request are not merged into your existing configuration. Make sure to include all fields: the ones that you modified and also the ones that you didn't.</p> </li> </ol>

        Args:
            distribution_config: <p>The distribution's configuration information.</p>
            id: <p>The distribution's id.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the distribution's configuration. For example: <code>E2QWRUHAPOMQZL</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.update_distribution_request.UpdateDistributionRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.update_distribution_result.UpdateDistributionResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_distribution

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_distribution.update_distribution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.update_distribution_request.UpdateDistributionRequest = {}  # type: ignore[typeddict-item]
        input_["distribution_config"] = distribution_config
        input_["id"] = id
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_distribution_tenant(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        if_match: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        distribution_id: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        domains: Optional["aws_sdk_cloudfront.types.domain_list.DomainList"] = None,
        customizations: Optional[
            "aws_sdk_cloudfront.types.customizations.Customizations"
        ] = None,
        parameters: Optional["aws_sdk_cloudfront.types.parameters.Parameters"] = None,
        connection_group_id: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        managed_certificate_request: Optional[
            "aws_sdk_cloudfront.types.managed_certificate_request.ManagedCertificateRequest"
        ] = None,
        enabled: Optional["aws_sdk_cloudfront.types.boolean.boolean"] = None,
    ) -> "aws_sdk_cloudfront.types.update_distribution_tenant_result.UpdateDistributionTenantResult":
        """<p>Updates a distribution tenant.</p>

        Args:
            id: <p>The ID of the distribution tenant.</p>
            distribution_id: <p>The ID for the multi-tenant distribution.</p>
            domains: <p>The domains to update for the distribution tenant. A domain object can contain only a domain property. You must specify at least one domain. Each distribution tenant can have up to 5 domains.</p>
            customizations: <p>Customizations for the distribution tenant. For each distribution tenant, you can specify the geographic restrictions, and the Amazon Resource Names (ARNs) for the ACM certificate and WAF web ACL. These are specific values that you can override or disable from the multi-tenant distribution that was used to create the distribution tenant.</p>
            parameters: <p>A list of parameter values to add to the resource. A parameter is specified as a key-value pair. A valid parameter value must exist for any parameter that is marked as required in the multi-tenant distribution.</p>
            connection_group_id: <p>The ID of the target connection group.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the distribution tenant to update. This value is returned in the response of the <code>GetDistributionTenant</code> API operation.</p>
            managed_certificate_request: <p>An object that contains the CloudFront managed ACM certificate request.</p>
            enabled: <p>Indicates whether the distribution tenant should be updated to an enabled state. If you update the distribution tenant and it's not enabled, the distribution tenant won't serve traffic.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.update_distribution_tenant_request.UpdateDistributionTenantRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.update_distribution_tenant_result.UpdateDistributionTenantResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_distribution_tenant

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_distribution_tenant.update_distribution_tenant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.update_distribution_tenant_request.UpdateDistributionTenantRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if distribution_id is not None:
            input_["distribution_id"] = distribution_id
        if domains is not None:
            input_["domains"] = domains
        if customizations is not None:
            input_["customizations"] = customizations
        if parameters is not None:
            input_["parameters"] = parameters
        if connection_group_id is not None:
            input_["connection_group_id"] = connection_group_id
        input_["if_match"] = if_match
        if managed_certificate_request is not None:
            input_["managed_certificate_request"] = managed_certificate_request
        if enabled is not None:
            input_["enabled"] = enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_distribution_with_staging_config(
        self,
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        staging_distribution_id: Optional[
            "aws_sdk_cloudfront.types.string.string"
        ] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> "aws_sdk_cloudfront.types.update_distribution_with_staging_config_result.UpdateDistributionWithStagingConfigResult":
        r"""<p>Copies the staging distribution's configuration to its corresponding primary distribution. The primary distribution retains its <code>Aliases</code> (also known as alternate domain names or CNAMEs) and <code>ContinuousDeploymentPolicyId</code> value, but otherwise its configuration is overwritten to match the staging distribution.</p> <p>You can use this operation in a continuous deployment workflow after you have tested configuration changes on the staging distribution. After using a continuous deployment policy to move a portion of your domain name's traffic to the staging distribution and verifying that it works as intended, you can use this operation to copy the staging distribution's configuration to the primary distribution. This action will disable the continuous deployment policy and move your domain's traffic back to the primary distribution.</p> <p>This API operation requires the following IAM permissions:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetDistribution.html\">GetDistribution</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateDistribution.html\">UpdateDistribution</a> </p> </li> </ul>

        Args:
            id: <p>The identifier of the primary distribution to which you are copying a staging distribution's configuration.</p>
            staging_distribution_id: <p>The identifier of the staging distribution whose configuration you are copying to the primary distribution.</p>
            if_match: <p>The current versions (<code>ETag</code> values) of both primary and staging distributions. Provide these in the following format:</p> <p> <code>&lt;primary ETag&gt;, &lt;staging ETag&gt;</code> </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.update_distribution_with_staging_config_request.UpdateDistributionWithStagingConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.update_distribution_with_staging_config_result.UpdateDistributionWithStagingConfigResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_distribution_with_staging_config

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_distribution_with_staging_config.update_distribution_with_staging_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.update_distribution_with_staging_config_request.UpdateDistributionWithStagingConfigRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if staging_distribution_id is not None:
            input_["staging_distribution_id"] = staging_distribution_id
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_domain_association(
        self,
        domain: "aws_sdk_cloudfront.types.string.string",
        target_resource: "aws_sdk_cloudfront.types.distribution_resource_id.DistributionResourceId",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> "aws_sdk_cloudfront.types.update_domain_association_result.UpdateDomainAssociationResult":
        r"""<note> <p>We recommend that you use the <code>UpdateDomainAssociation</code> API operation to move a domain association, as it supports both standard distributions and distribution tenants. <a href=\"https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_AssociateAlias.html\">AssociateAlias</a> performs similar checks but only supports standard distributions.</p> </note> <p>Moves a domain from its current standard distribution or distribution tenant to another one.</p> <p>You must first disable the source distribution (standard distribution or distribution tenant) and then separately call this operation to move the domain to another target distribution (standard distribution or distribution tenant).</p> <p>To use this operation, specify the domain and the ID of the target resource (standard distribution or distribution tenant). For more information, including how to set up the target resource, prerequisites that you must complete, and other restrictions, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html#alternate-domain-names-move\">Moving an alternate domain name to a different standard distribution or distribution tenant</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            domain: <p>The domain to update.</p>
            target_resource: <p>The target standard distribution or distribution tenant resource for the domain. You can specify either <code>DistributionId</code> or <code>DistributionTenantId</code>, but not both.</p>
            if_match: <p>The value of the <code>ETag</code> identifier for the standard distribution or distribution tenant that will be associated with the domain.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.update_domain_association_request.UpdateDomainAssociationRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.update_domain_association_result.UpdateDomainAssociationResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_domain_association

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_domain_association.update_domain_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.update_domain_association_request.UpdateDomainAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["domain"] = domain
        input_["target_resource"] = target_resource
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_field_level_encryption_config(
        self,
        field_level_encryption_config: "aws_sdk_cloudfront.types.field_level_encryption_config.FieldLevelEncryptionConfig",
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> "aws_sdk_cloudfront.types.update_field_level_encryption_config_result.UpdateFieldLevelEncryptionConfigResult":
        """<p>Update a field-level encryption configuration.</p>

        Args:
            field_level_encryption_config: <p>Request to update a field-level encryption configuration.</p>
            id: <p>The ID of the configuration you want to update.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the configuration identity to update. For example: <code>E2QWRUHAPOMQZL</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.update_field_level_encryption_config_request.UpdateFieldLevelEncryptionConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.update_field_level_encryption_config_result.UpdateFieldLevelEncryptionConfigResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_field_level_encryption_config

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_field_level_encryption_config.update_field_level_encryption_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.update_field_level_encryption_config_request.UpdateFieldLevelEncryptionConfigRequest = {}  # type: ignore[typeddict-item]
        input_["field_level_encryption_config"] = field_level_encryption_config
        input_["id"] = id
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_field_level_encryption_profile(
        self,
        field_level_encryption_profile_config: "aws_sdk_cloudfront.types.field_level_encryption_profile_config.FieldLevelEncryptionProfileConfig",
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> "aws_sdk_cloudfront.types.update_field_level_encryption_profile_result.UpdateFieldLevelEncryptionProfileResult":
        """<p>Update a field-level encryption profile.</p>

        Args:
            field_level_encryption_profile_config: <p>Request to update a field-level encryption profile.</p>
            id: <p>The ID of the field-level encryption profile request.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the profile identity to update. For example: <code>E2QWRUHAPOMQZL</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.update_field_level_encryption_profile_request.UpdateFieldLevelEncryptionProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.update_field_level_encryption_profile_result.UpdateFieldLevelEncryptionProfileResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_field_level_encryption_profile

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_field_level_encryption_profile.update_field_level_encryption_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.update_field_level_encryption_profile_request.UpdateFieldLevelEncryptionProfileRequest = {}  # type: ignore[typeddict-item]
        input_["field_level_encryption_profile_config"] = (
            field_level_encryption_profile_config
        )
        input_["id"] = id
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_function(
        self,
        name: "aws_sdk_cloudfront.types.function_name.FunctionName",
        if_match: "aws_sdk_cloudfront.types.string.string",
        function_config: "aws_sdk_cloudfront.types.function_config.FunctionConfig",
        function_code: "aws_sdk_cloudfront.types.function_blob.FunctionBlob",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.update_function_result.UpdateFunctionResult":
        r"""<p>Updates a CloudFront function.</p> <p>You can update a function's code or the comment that describes the function. You cannot update a function's name.</p> <p>To update a function, you provide the function's name and version (<code>ETag</code> value) along with the updated function code. To get the name and version, you can use <code>ListFunctions</code> and <code>DescribeFunction</code>.</p>

        Args:
            name: <p>The name of the function that you are updating.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the function that you are updating, which you can get using <code>DescribeFunction</code>.</p>
            function_config: <p>Configuration information about the function.</p>
            function_code: <p>The function code. For more information about writing a CloudFront function, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/writing-function-code.html\">Writing function code for CloudFront Functions</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Examples:
            To update a function
            Use the following command to update a function.

            >>> client.update_function(name='my-function-name', function_config={'Comment': 'my-changed-comment', 'Runtime': 'cloudfront-js-2.0', 'KeyValueStoreAssociations': {'Quantity': 1, 'Items': [{'KeyValueStoreARN': 'arn:aws:cloudfront::123456789012:key-value-store/54947df8-0e9e-4471-a2f9-9af509fb5889'}]}}, function_code='function-code-changed.js', if_match='ETVPDKIKX0DER')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.update_function_request.UpdateFunctionRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.update_function_result.UpdateFunctionResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_function

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_function.update_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.update_function_request.UpdateFunctionRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["if_match"] = if_match
        input_["function_config"] = function_config
        input_["function_code"] = function_code

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_key_group(
        self,
        key_group_config: "aws_sdk_cloudfront.types.key_group_config.KeyGroupConfig",
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> "aws_sdk_cloudfront.types.update_key_group_result.UpdateKeyGroupResult":
        """<p>Updates a key group.</p> <p>When you update a key group, all the fields are updated with the values provided in the request. You cannot update some fields independent of others. To update a key group:</p> <ol> <li> <p>Get the current key group with <code>GetKeyGroup</code> or <code>GetKeyGroupConfig</code>.</p> </li> <li> <p>Locally modify the fields in the key group that you want to update. For example, add or remove public key IDs.</p> </li> <li> <p>Call <code>UpdateKeyGroup</code> with the entire key group object, including the fields that you modified and those that you didn't.</p> </li> </ol>

        Args:
            key_group_config: <p>The key group configuration.</p>
            id: <p>The identifier of the key group that you are updating.</p>
            if_match: <p>The version of the key group that you are updating. The version is the key group's <code>ETag</code> value.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.update_key_group_request.UpdateKeyGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.update_key_group_result.UpdateKeyGroupResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_key_group

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_key_group.update_key_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.update_key_group_request.UpdateKeyGroupRequest = {}  # type: ignore[typeddict-item]
        input_["key_group_config"] = key_group_config
        input_["id"] = id
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_key_value_store(
        self,
        name: "aws_sdk_cloudfront.types.key_value_store_name.KeyValueStoreName",
        comment: "aws_sdk_cloudfront.types.key_value_store_comment.KeyValueStoreComment",
        if_match: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.update_key_value_store_result.UpdateKeyValueStoreResult":
        """<p>Specifies the key value store to update.</p>

        Args:
            name: <p>The name of the key value store to update.</p>
            comment: <p>The comment of the key value store to update.</p>
            if_match: <p>The key value store to update, if a match occurs.</p>

        Examples:
            To update a KeyValueStore
            Use the following command to update a KeyValueStore.

            >>> client.update_key_value_store(name='my-keyvaluestore-name', comment='my-changed-comment', if_match='ETVPDKIKX0DER')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.update_key_value_store_request.UpdateKeyValueStoreRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.update_key_value_store_result.UpdateKeyValueStoreResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_key_value_store

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_key_value_store.update_key_value_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.update_key_value_store_request.UpdateKeyValueStoreRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["comment"] = comment
        input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_origin_access_control(
        self,
        origin_access_control_config: "aws_sdk_cloudfront.types.origin_access_control_config.OriginAccessControlConfig",
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> "aws_sdk_cloudfront.types.update_origin_access_control_result.UpdateOriginAccessControlResult":
        """<p>Updates a CloudFront origin access control.</p>

        Args:
            origin_access_control_config: <p>An origin access control.</p>
            id: <p>The unique identifier of the origin access control that you are updating.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the origin access control that you are updating.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.update_origin_access_control_request.UpdateOriginAccessControlRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.update_origin_access_control_result.UpdateOriginAccessControlResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_origin_access_control

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_origin_access_control.update_origin_access_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.update_origin_access_control_request.UpdateOriginAccessControlRequest = {}  # type: ignore[typeddict-item]
        input_["origin_access_control_config"] = origin_access_control_config
        input_["id"] = id
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_origin_request_policy(
        self,
        origin_request_policy_config: "aws_sdk_cloudfront.types.origin_request_policy_config.OriginRequestPolicyConfig",
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> "aws_sdk_cloudfront.types.update_origin_request_policy_result.UpdateOriginRequestPolicyResult":
        """<p>Updates an origin request policy configuration.</p> <p>When you update an origin request policy configuration, all the fields are updated with the values provided in the request. You cannot update some fields independent of others. To update an origin request policy configuration:</p> <ol> <li> <p>Use <code>GetOriginRequestPolicyConfig</code> to get the current configuration.</p> </li> <li> <p>Locally modify the fields in the origin request policy configuration that you want to update.</p> </li> <li> <p>Call <code>UpdateOriginRequestPolicy</code> by providing the entire origin request policy configuration, including the fields that you modified and those that you didn't.</p> </li> </ol>

        Args:
            origin_request_policy_config: <p>An origin request policy configuration.</p>
            id: <p>The unique identifier for the origin request policy that you are updating. The identifier is returned in a cache behavior's <code>OriginRequestPolicyId</code> field in the response to <code>GetDistributionConfig</code>.</p>
            if_match: <p>The version of the origin request policy that you are updating. The version is returned in the origin request policy's <code>ETag</code> field in the response to <code>GetOriginRequestPolicyConfig</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.update_origin_request_policy_request.UpdateOriginRequestPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.update_origin_request_policy_result.UpdateOriginRequestPolicyResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_origin_request_policy

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_origin_request_policy.update_origin_request_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.update_origin_request_policy_request.UpdateOriginRequestPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["origin_request_policy_config"] = origin_request_policy_config
        input_["id"] = id
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_public_key(
        self,
        public_key_config: "aws_sdk_cloudfront.types.public_key_config.PublicKeyConfig",
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> "aws_sdk_cloudfront.types.update_public_key_result.UpdatePublicKeyResult":
        """<p>Update public key information. Note that the only value you can change is the comment.</p>

        Args:
            public_key_config: <p>A public key configuration.</p>
            id: <p>The identifier of the public key that you are updating.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the public key to update. For example: <code>E2QWRUHAPOMQZL</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.update_public_key_request.UpdatePublicKeyRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.update_public_key_result.UpdatePublicKeyResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_public_key

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_public_key.update_public_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.update_public_key_request.UpdatePublicKeyRequest = {}  # type: ignore[typeddict-item]
        input_["public_key_config"] = public_key_config
        input_["id"] = id
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_realtime_log_config(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        end_points: Optional[
            "aws_sdk_cloudfront.types.end_point_list.EndPointList"
        ] = None,
        fields: Optional["aws_sdk_cloudfront.types.field_list.FieldList"] = None,
        name: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        arn: Optional["aws_sdk_cloudfront.types.string.string"] = None,
        sampling_rate: Optional["aws_sdk_cloudfront.types.long.long"] = None,
    ) -> "aws_sdk_cloudfront.types.update_realtime_log_config_result.UpdateRealtimeLogConfigResult":
        r"""<p>Updates a real-time log configuration.</p> <p>When you update a real-time log configuration, all the parameters are updated with the values provided in the request. You cannot update some parameters independent of others. To update a real-time log configuration:</p> <ol> <li> <p>Call <code>GetRealtimeLogConfig</code> to get the current real-time log configuration.</p> </li> <li> <p>Locally modify the parameters in the real-time log configuration that you want to update.</p> </li> <li> <p>Call this API (<code>UpdateRealtimeLogConfig</code>) by providing the entire real-time log configuration, including the parameters that you modified and those that you didn't.</p> </li> </ol> <p>You cannot update a real-time log configuration's <code>Name</code> or <code>ARN</code>.</p>

        Args:
            end_points: <p>Contains information about the Amazon Kinesis data stream where you are sending real-time log data.</p>
            fields: <p>A list of fields to include in each real-time log record.</p> <p>For more information about fields, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html#understand-real-time-log-config-fields\">Real-time log configuration fields</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>
            name: <p>The name for this real-time log configuration.</p>
            arn: <p>The Amazon Resource Name (ARN) for this real-time log configuration.</p>
            sampling_rate: <p>The sampling rate for this real-time log configuration. The sampling rate determines the percentage of viewer requests that are represented in the real-time log data. You must provide an integer between 1 and 100, inclusive.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.update_realtime_log_config_request.UpdateRealtimeLogConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.update_realtime_log_config_result.UpdateRealtimeLogConfigResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_realtime_log_config

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_realtime_log_config.update_realtime_log_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.update_realtime_log_config_request.UpdateRealtimeLogConfigRequest = {}  # type: ignore[typeddict-item]
        if end_points is not None:
            input_["end_points"] = end_points
        if fields is not None:
            input_["fields"] = fields
        if name is not None:
            input_["name"] = name
        if arn is not None:
            input_["arn"] = arn
        if sampling_rate is not None:
            input_["sampling_rate"] = sampling_rate

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_response_headers_policy(
        self,
        response_headers_policy_config: "aws_sdk_cloudfront.types.response_headers_policy_config.ResponseHeadersPolicyConfig",
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> "aws_sdk_cloudfront.types.update_response_headers_policy_result.UpdateResponseHeadersPolicyResult":
        """<p>Updates a response headers policy.</p> <p>When you update a response headers policy, the entire policy is replaced. You cannot update some policy fields independent of others. To update a response headers policy configuration:</p> <ol> <li> <p>Use <code>GetResponseHeadersPolicyConfig</code> to get the current policy's configuration.</p> </li> <li> <p>Modify the fields in the response headers policy configuration that you want to update.</p> </li> <li> <p>Call <code>UpdateResponseHeadersPolicy</code>, providing the entire response headers policy configuration, including the fields that you modified and those that you didn't.</p> </li> </ol>

        Args:
            response_headers_policy_config: <p>A response headers policy configuration.</p>
            id: <p>The identifier for the response headers policy that you are updating.</p>
            if_match: <p>The version of the response headers policy that you are updating.</p> <p>The version is returned in the cache policy's <code>ETag</code> field in the response to <code>GetResponseHeadersPolicyConfig</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.update_response_headers_policy_request.UpdateResponseHeadersPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.update_response_headers_policy_result.UpdateResponseHeadersPolicyResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_response_headers_policy

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_response_headers_policy.update_response_headers_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.update_response_headers_policy_request.UpdateResponseHeadersPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["response_headers_policy_config"] = response_headers_policy_config
        input_["id"] = id
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_streaming_distribution(
        self,
        streaming_distribution_config: "aws_sdk_cloudfront.types.streaming_distribution_config.StreamingDistributionConfig",
        id: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> "aws_sdk_cloudfront.types.update_streaming_distribution_result.UpdateStreamingDistributionResult":
        """<p>Update a streaming distribution.</p>

        Args:
            streaming_distribution_config: <p>The streaming distribution's configuration information.</p>
            id: <p>The streaming distribution's id.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the streaming distribution's configuration. For example: <code>E2QWRUHAPOMQZL</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.update_streaming_distribution_request.UpdateStreamingDistributionRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.update_streaming_distribution_result.UpdateStreamingDistributionResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_streaming_distribution

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_streaming_distribution.update_streaming_distribution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.update_streaming_distribution_request.UpdateStreamingDistributionRequest = {}  # type: ignore[typeddict-item]
        input_["streaming_distribution_config"] = streaming_distribution_config
        input_["id"] = id
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_trust_store(
        self,
        id: "aws_sdk_cloudfront.types.resource_id.ResourceId",
        if_match: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        ca_certificates_bundle_source: Optional[
            "aws_sdk_cloudfront.types.ca_certificates_bundle_source.CaCertificatesBundleSource"
        ] = None,
        use_client_certificate_ocsp_endpoint: Optional[
            "aws_sdk_cloudfront.types.boolean.boolean"
        ] = None,
    ) -> "aws_sdk_cloudfront.types.update_trust_store_result.UpdateTrustStoreResult":
        """<p>Updates a trust store.</p>

        Args:
            id: <p>The trust store ID.</p>
            ca_certificates_bundle_source: <p>The CA certificates bundle source.</p>
            use_client_certificate_ocsp_endpoint: <p>A Boolean that determines whether to use the CA certificate's OCSP endpoint to check certificate revocation status.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the trust store you are updating.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.update_trust_store_request.UpdateTrustStoreRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.update_trust_store_result.UpdateTrustStoreResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_trust_store

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_trust_store.update_trust_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.update_trust_store_request.UpdateTrustStoreRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if ca_certificates_bundle_source is not None:
            input_["ca_certificates_bundle_source"] = ca_certificates_bundle_source
        if use_client_certificate_ocsp_endpoint is not None:
            input_["use_client_certificate_ocsp_endpoint"] = (
                use_client_certificate_ocsp_endpoint
            )
        input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_vpc_origin(
        self,
        vpc_origin_endpoint_config: "aws_sdk_cloudfront.types.vpc_origin_endpoint_config.VpcOriginEndpointConfig",
        id: "aws_sdk_cloudfront.types.string.string",
        if_match: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "aws_sdk_cloudfront.types.update_vpc_origin_result.UpdateVpcOriginResult":
        """<p>Update an Amazon CloudFront VPC origin in your account.</p>

        Args:
            vpc_origin_endpoint_config: <p>The VPC origin endpoint configuration.</p>
            id: <p>The VPC origin ID.</p>
            if_match: <p>The VPC origin to update, if a match occurs.</p>

        Examples:
            To update a VPC origin
            The following command updates a VPC origin:

            >>> client.update_vpc_origin(vpc_origin_endpoint_config={'Name': 'my-vpcorigin-name', 'Arn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-alb-us-west-2/e6aa5c7d26415c6d', 'HTTPPort': 80, 'HTTPSPort': 443, 'OriginProtocolPolicy': 'match-viewer', 'OriginSslProtocols': {'Quantity': 2, 'Items': ['TLSv1.1', 'TLSv1.2']}}, id='vo_BQwjxxQxjCaBcQLzJUFkDM', if_match='ETVPDKIKX0DER')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.update_vpc_origin_request.UpdateVpcOriginRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.update_vpc_origin_result.UpdateVpcOriginResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_vpc_origin

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.update_vpc_origin.update_vpc_origin(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.update_vpc_origin_request.UpdateVpcOriginRequest = {}  # type: ignore[typeddict-item]
        input_["vpc_origin_endpoint_config"] = vpc_origin_endpoint_config
        input_["id"] = id
        input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def verify_dns_configuration(
        self,
        identifier: "aws_sdk_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        domain: Optional["aws_sdk_cloudfront.types.string.string"] = None,
    ) -> "aws_sdk_cloudfront.types.verify_dns_configuration_result.VerifyDnsConfigurationResult":
        """<p>Verify the DNS configuration for your domain names. This API operation checks whether your domain name points to the correct routing endpoint of the connection group, such as d111111abcdef8.cloudfront.net. You can use this API operation to troubleshoot and resolve DNS configuration issues.</p>

        Args:
            domain: <p>The domain name that you're verifying.</p>
            identifier: <p>The identifier of the distribution tenant. You can specify the ARN, ID, or name of the distribution tenant.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudfront.types.verify_dns_configuration_request.VerifyDnsConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudfront.types.verify_dns_configuration_result.VerifyDnsConfigurationResult"
        ]:
            import aws_sdk_cloudfront._operations.cloudfront2020_05_31.verify_dns_configuration

            output, http_response = (
                aws_sdk_cloudfront._operations.cloudfront2020_05_31.verify_dns_configuration.verify_dns_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudfront.types.verify_dns_configuration_request.VerifyDnsConfigurationRequest = {}  # type: ignore[typeddict-item]
        if domain is not None:
            input_["domain"] = domain
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
