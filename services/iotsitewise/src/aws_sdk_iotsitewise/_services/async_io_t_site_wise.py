"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AWSIoTSiteWise``."""

import time
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_iotsitewise._auth._signers
import aws_sdk_iotsitewise._auth._sigv4
from aws_sdk_iotsitewise._async import anysleep
from aws_sdk_iotsitewise._auth._identity import Credentials
from aws_sdk_iotsitewise._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_iotsitewise._auth._zapros_handler import AuthMiddleware
from aws_sdk_iotsitewise._pagination import resolve_path as _resolve_path
from aws_sdk_iotsitewise._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)
from aws_sdk_iotsitewise.errors import (
    ServiceError,
    WaiterTimeoutError,
)

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.access_policy_summary
    import aws_sdk_iotsitewise.types.action_payload
    import aws_sdk_iotsitewise.types.action_summary
    import aws_sdk_iotsitewise.types.adaptive_ingestion
    import aws_sdk_iotsitewise.types.aggregate_types
    import aws_sdk_iotsitewise.types.aggregated_value
    import aws_sdk_iotsitewise.types.alarms
    import aws_sdk_iotsitewise.types.amazon_resource_name
    import aws_sdk_iotsitewise.types.arn
    import aws_sdk_iotsitewise.types.asset_model_composite_model_definitions
    import aws_sdk_iotsitewise.types.asset_model_composite_model_summary
    import aws_sdk_iotsitewise.types.asset_model_composite_models
    import aws_sdk_iotsitewise.types.asset_model_hierarchies
    import aws_sdk_iotsitewise.types.asset_model_hierarchy_definitions
    import aws_sdk_iotsitewise.types.asset_model_properties
    import aws_sdk_iotsitewise.types.asset_model_property_definitions
    import aws_sdk_iotsitewise.types.asset_model_property_summary
    import aws_sdk_iotsitewise.types.asset_model_summary
    import aws_sdk_iotsitewise.types.asset_model_type
    import aws_sdk_iotsitewise.types.asset_model_version_filter
    import aws_sdk_iotsitewise.types.asset_model_version_type
    import aws_sdk_iotsitewise.types.asset_property_alias
    import aws_sdk_iotsitewise.types.asset_property_summary
    import aws_sdk_iotsitewise.types.asset_property_value
    import aws_sdk_iotsitewise.types.asset_relationship_summary
    import aws_sdk_iotsitewise.types.asset_summary
    import aws_sdk_iotsitewise.types.associate_assets_request
    import aws_sdk_iotsitewise.types.associate_time_series_to_asset_property_request
    import aws_sdk_iotsitewise.types.associated_assets_summary
    import aws_sdk_iotsitewise.types.auth_mode
    import aws_sdk_iotsitewise.types.batch_associate_project_assets_request
    import aws_sdk_iotsitewise.types.batch_associate_project_assets_response
    import aws_sdk_iotsitewise.types.batch_disassociate_project_assets_request
    import aws_sdk_iotsitewise.types.batch_disassociate_project_assets_response
    import aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_entries
    import aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_max_results
    import aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_request
    import aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_response
    import aws_sdk_iotsitewise.types.batch_get_asset_property_value_entries
    import aws_sdk_iotsitewise.types.batch_get_asset_property_value_history_entries
    import aws_sdk_iotsitewise.types.batch_get_asset_property_value_history_max_results
    import aws_sdk_iotsitewise.types.batch_get_asset_property_value_history_request
    import aws_sdk_iotsitewise.types.batch_get_asset_property_value_history_response
    import aws_sdk_iotsitewise.types.batch_get_asset_property_value_request
    import aws_sdk_iotsitewise.types.batch_get_asset_property_value_response
    import aws_sdk_iotsitewise.types.batch_put_asset_property_value_request
    import aws_sdk_iotsitewise.types.batch_put_asset_property_value_response
    import aws_sdk_iotsitewise.types.boolean_value
    import aws_sdk_iotsitewise.types.capability_configuration
    import aws_sdk_iotsitewise.types.capability_namespace
    import aws_sdk_iotsitewise.types.client_token
    import aws_sdk_iotsitewise.types.composition_relationship_summary
    import aws_sdk_iotsitewise.types.computation_model_configuration
    import aws_sdk_iotsitewise.types.computation_model_data_binding
    import aws_sdk_iotsitewise.types.computation_model_data_binding_usage_summary
    import aws_sdk_iotsitewise.types.computation_model_resolve_to_resource_summary
    import aws_sdk_iotsitewise.types.computation_model_summary
    import aws_sdk_iotsitewise.types.computation_model_type
    import aws_sdk_iotsitewise.types.computation_model_version_filter
    import aws_sdk_iotsitewise.types.conversation_id
    import aws_sdk_iotsitewise.types.create_access_policy_request
    import aws_sdk_iotsitewise.types.create_access_policy_response
    import aws_sdk_iotsitewise.types.create_asset_model_composite_model_request
    import aws_sdk_iotsitewise.types.create_asset_model_composite_model_response
    import aws_sdk_iotsitewise.types.create_asset_model_request
    import aws_sdk_iotsitewise.types.create_asset_model_response
    import aws_sdk_iotsitewise.types.create_asset_request
    import aws_sdk_iotsitewise.types.create_asset_response
    import aws_sdk_iotsitewise.types.create_bulk_import_job_request
    import aws_sdk_iotsitewise.types.create_bulk_import_job_response
    import aws_sdk_iotsitewise.types.create_computation_model_request
    import aws_sdk_iotsitewise.types.create_computation_model_response
    import aws_sdk_iotsitewise.types.create_dashboard_request
    import aws_sdk_iotsitewise.types.create_dashboard_response
    import aws_sdk_iotsitewise.types.create_dataset_request
    import aws_sdk_iotsitewise.types.create_dataset_response
    import aws_sdk_iotsitewise.types.create_gateway_request
    import aws_sdk_iotsitewise.types.create_gateway_response
    import aws_sdk_iotsitewise.types.create_portal_request
    import aws_sdk_iotsitewise.types.create_portal_response
    import aws_sdk_iotsitewise.types.create_project_request
    import aws_sdk_iotsitewise.types.create_project_response
    import aws_sdk_iotsitewise.types.custom_id
    import aws_sdk_iotsitewise.types.dashboard_definition
    import aws_sdk_iotsitewise.types.dashboard_summary
    import aws_sdk_iotsitewise.types.data_binding_value_filter
    import aws_sdk_iotsitewise.types.dataset_source
    import aws_sdk_iotsitewise.types.dataset_source_type
    import aws_sdk_iotsitewise.types.dataset_summary
    import aws_sdk_iotsitewise.types.delete_access_policy_request
    import aws_sdk_iotsitewise.types.delete_access_policy_response
    import aws_sdk_iotsitewise.types.delete_asset_model_composite_model_request
    import aws_sdk_iotsitewise.types.delete_asset_model_composite_model_response
    import aws_sdk_iotsitewise.types.delete_asset_model_interface_relationship_request
    import aws_sdk_iotsitewise.types.delete_asset_model_interface_relationship_response
    import aws_sdk_iotsitewise.types.delete_asset_model_request
    import aws_sdk_iotsitewise.types.delete_asset_model_response
    import aws_sdk_iotsitewise.types.delete_asset_request
    import aws_sdk_iotsitewise.types.delete_asset_response
    import aws_sdk_iotsitewise.types.delete_computation_model_request
    import aws_sdk_iotsitewise.types.delete_computation_model_response
    import aws_sdk_iotsitewise.types.delete_dashboard_request
    import aws_sdk_iotsitewise.types.delete_dashboard_response
    import aws_sdk_iotsitewise.types.delete_dataset_request
    import aws_sdk_iotsitewise.types.delete_dataset_response
    import aws_sdk_iotsitewise.types.delete_files_after_import
    import aws_sdk_iotsitewise.types.delete_gateway_request
    import aws_sdk_iotsitewise.types.delete_portal_request
    import aws_sdk_iotsitewise.types.delete_portal_response
    import aws_sdk_iotsitewise.types.delete_project_request
    import aws_sdk_iotsitewise.types.delete_project_response
    import aws_sdk_iotsitewise.types.delete_time_series_request
    import aws_sdk_iotsitewise.types.describe_access_policy_request
    import aws_sdk_iotsitewise.types.describe_access_policy_response
    import aws_sdk_iotsitewise.types.describe_action_request
    import aws_sdk_iotsitewise.types.describe_action_response
    import aws_sdk_iotsitewise.types.describe_asset_composite_model_request
    import aws_sdk_iotsitewise.types.describe_asset_composite_model_response
    import aws_sdk_iotsitewise.types.describe_asset_model_composite_model_request
    import aws_sdk_iotsitewise.types.describe_asset_model_composite_model_response
    import aws_sdk_iotsitewise.types.describe_asset_model_interface_relationship_request
    import aws_sdk_iotsitewise.types.describe_asset_model_interface_relationship_response
    import aws_sdk_iotsitewise.types.describe_asset_model_request
    import aws_sdk_iotsitewise.types.describe_asset_model_response
    import aws_sdk_iotsitewise.types.describe_asset_property_request
    import aws_sdk_iotsitewise.types.describe_asset_property_response
    import aws_sdk_iotsitewise.types.describe_asset_request
    import aws_sdk_iotsitewise.types.describe_asset_response
    import aws_sdk_iotsitewise.types.describe_bulk_import_job_request
    import aws_sdk_iotsitewise.types.describe_bulk_import_job_response
    import aws_sdk_iotsitewise.types.describe_computation_model_execution_summary_request
    import aws_sdk_iotsitewise.types.describe_computation_model_execution_summary_response
    import aws_sdk_iotsitewise.types.describe_computation_model_request
    import aws_sdk_iotsitewise.types.describe_computation_model_response
    import aws_sdk_iotsitewise.types.describe_dashboard_request
    import aws_sdk_iotsitewise.types.describe_dashboard_response
    import aws_sdk_iotsitewise.types.describe_dataset_request
    import aws_sdk_iotsitewise.types.describe_dataset_response
    import aws_sdk_iotsitewise.types.describe_default_encryption_configuration_request
    import aws_sdk_iotsitewise.types.describe_default_encryption_configuration_response
    import aws_sdk_iotsitewise.types.describe_execution_request
    import aws_sdk_iotsitewise.types.describe_execution_response
    import aws_sdk_iotsitewise.types.describe_gateway_capability_configuration_request
    import aws_sdk_iotsitewise.types.describe_gateway_capability_configuration_response
    import aws_sdk_iotsitewise.types.describe_gateway_request
    import aws_sdk_iotsitewise.types.describe_gateway_response
    import aws_sdk_iotsitewise.types.describe_logging_options_request
    import aws_sdk_iotsitewise.types.describe_logging_options_response
    import aws_sdk_iotsitewise.types.describe_portal_request
    import aws_sdk_iotsitewise.types.describe_portal_response
    import aws_sdk_iotsitewise.types.describe_project_request
    import aws_sdk_iotsitewise.types.describe_project_response
    import aws_sdk_iotsitewise.types.describe_storage_configuration_request
    import aws_sdk_iotsitewise.types.describe_storage_configuration_response
    import aws_sdk_iotsitewise.types.describe_time_series_request
    import aws_sdk_iotsitewise.types.describe_time_series_response
    import aws_sdk_iotsitewise.types.description
    import aws_sdk_iotsitewise.types.disallow_ingest_null_na_n
    import aws_sdk_iotsitewise.types.disassociate_assets_request
    import aws_sdk_iotsitewise.types.disassociate_time_series_from_asset_property_request
    import aws_sdk_iotsitewise.types.disassociated_data_storage_state
    import aws_sdk_iotsitewise.types.e_tag
    import aws_sdk_iotsitewise.types.email
    import aws_sdk_iotsitewise.types.encryption_type
    import aws_sdk_iotsitewise.types.error_report_location
    import aws_sdk_iotsitewise.types.exclude_properties
    import aws_sdk_iotsitewise.types.execute_action_request
    import aws_sdk_iotsitewise.types.execute_action_response
    import aws_sdk_iotsitewise.types.execute_query_max_results
    import aws_sdk_iotsitewise.types.execute_query_next_token
    import aws_sdk_iotsitewise.types.execute_query_request
    import aws_sdk_iotsitewise.types.execute_query_response
    import aws_sdk_iotsitewise.types.execution_summary
    import aws_sdk_iotsitewise.types.external_id
    import aws_sdk_iotsitewise.types.files
    import aws_sdk_iotsitewise.types.gateway_name
    import aws_sdk_iotsitewise.types.gateway_platform
    import aws_sdk_iotsitewise.types.gateway_summary
    import aws_sdk_iotsitewise.types.gateway_version
    import aws_sdk_iotsitewise.types.get_asset_property_aggregates_request
    import aws_sdk_iotsitewise.types.get_asset_property_aggregates_response
    import aws_sdk_iotsitewise.types.get_asset_property_value_aggregates_max_results
    import aws_sdk_iotsitewise.types.get_asset_property_value_history_max_results
    import aws_sdk_iotsitewise.types.get_asset_property_value_history_request
    import aws_sdk_iotsitewise.types.get_asset_property_value_history_response
    import aws_sdk_iotsitewise.types.get_asset_property_value_request
    import aws_sdk_iotsitewise.types.get_asset_property_value_response
    import aws_sdk_iotsitewise.types.get_interpolated_asset_property_values_request
    import aws_sdk_iotsitewise.types.get_interpolated_asset_property_values_response
    import aws_sdk_iotsitewise.types.i_ds
    import aws_sdk_iotsitewise.types.iam_arn
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.identity
    import aws_sdk_iotsitewise.types.identity_id
    import aws_sdk_iotsitewise.types.identity_type
    import aws_sdk_iotsitewise.types.image
    import aws_sdk_iotsitewise.types.image_file
    import aws_sdk_iotsitewise.types.interface_relationship_summary
    import aws_sdk_iotsitewise.types.interpolated_asset_property_value
    import aws_sdk_iotsitewise.types.interpolation_type
    import aws_sdk_iotsitewise.types.interval_in_seconds
    import aws_sdk_iotsitewise.types.interval_window_in_seconds
    import aws_sdk_iotsitewise.types.invoke_assistant_request
    import aws_sdk_iotsitewise.types.invoke_assistant_response
    import aws_sdk_iotsitewise.types.job_configuration
    import aws_sdk_iotsitewise.types.job_summary
    import aws_sdk_iotsitewise.types.kms_key_id
    import aws_sdk_iotsitewise.types.list_access_policies_request
    import aws_sdk_iotsitewise.types.list_access_policies_response
    import aws_sdk_iotsitewise.types.list_actions_request
    import aws_sdk_iotsitewise.types.list_actions_response
    import aws_sdk_iotsitewise.types.list_asset_model_composite_models_request
    import aws_sdk_iotsitewise.types.list_asset_model_composite_models_response
    import aws_sdk_iotsitewise.types.list_asset_model_properties_filter
    import aws_sdk_iotsitewise.types.list_asset_model_properties_request
    import aws_sdk_iotsitewise.types.list_asset_model_properties_response
    import aws_sdk_iotsitewise.types.list_asset_models_request
    import aws_sdk_iotsitewise.types.list_asset_models_response
    import aws_sdk_iotsitewise.types.list_asset_models_type_filter
    import aws_sdk_iotsitewise.types.list_asset_properties_filter
    import aws_sdk_iotsitewise.types.list_asset_properties_request
    import aws_sdk_iotsitewise.types.list_asset_properties_response
    import aws_sdk_iotsitewise.types.list_asset_relationships_request
    import aws_sdk_iotsitewise.types.list_asset_relationships_response
    import aws_sdk_iotsitewise.types.list_assets_filter
    import aws_sdk_iotsitewise.types.list_assets_request
    import aws_sdk_iotsitewise.types.list_assets_response
    import aws_sdk_iotsitewise.types.list_associated_assets_request
    import aws_sdk_iotsitewise.types.list_associated_assets_response
    import aws_sdk_iotsitewise.types.list_bulk_import_jobs_filter
    import aws_sdk_iotsitewise.types.list_bulk_import_jobs_request
    import aws_sdk_iotsitewise.types.list_bulk_import_jobs_response
    import aws_sdk_iotsitewise.types.list_composition_relationships_request
    import aws_sdk_iotsitewise.types.list_composition_relationships_response
    import aws_sdk_iotsitewise.types.list_computation_model_data_binding_usages_request
    import aws_sdk_iotsitewise.types.list_computation_model_data_binding_usages_response
    import aws_sdk_iotsitewise.types.list_computation_model_resolve_to_resources_request
    import aws_sdk_iotsitewise.types.list_computation_model_resolve_to_resources_response
    import aws_sdk_iotsitewise.types.list_computation_models_request
    import aws_sdk_iotsitewise.types.list_computation_models_response
    import aws_sdk_iotsitewise.types.list_dashboards_request
    import aws_sdk_iotsitewise.types.list_dashboards_response
    import aws_sdk_iotsitewise.types.list_datasets_request
    import aws_sdk_iotsitewise.types.list_datasets_response
    import aws_sdk_iotsitewise.types.list_executions_request
    import aws_sdk_iotsitewise.types.list_executions_response
    import aws_sdk_iotsitewise.types.list_gateways_request
    import aws_sdk_iotsitewise.types.list_gateways_response
    import aws_sdk_iotsitewise.types.list_interface_relationships_request
    import aws_sdk_iotsitewise.types.list_interface_relationships_response
    import aws_sdk_iotsitewise.types.list_portals_request
    import aws_sdk_iotsitewise.types.list_portals_response
    import aws_sdk_iotsitewise.types.list_project_assets_request
    import aws_sdk_iotsitewise.types.list_project_assets_response
    import aws_sdk_iotsitewise.types.list_projects_request
    import aws_sdk_iotsitewise.types.list_projects_response
    import aws_sdk_iotsitewise.types.list_tags_for_resource_request
    import aws_sdk_iotsitewise.types.list_tags_for_resource_response
    import aws_sdk_iotsitewise.types.list_time_series_request
    import aws_sdk_iotsitewise.types.list_time_series_response
    import aws_sdk_iotsitewise.types.list_time_series_type
    import aws_sdk_iotsitewise.types.logging_options
    import aws_sdk_iotsitewise.types.max_interpolated_results
    import aws_sdk_iotsitewise.types.max_results
    import aws_sdk_iotsitewise.types.message_input
    import aws_sdk_iotsitewise.types.multi_layer_storage
    import aws_sdk_iotsitewise.types.name
    import aws_sdk_iotsitewise.types.next_token
    import aws_sdk_iotsitewise.types.offset_in_nanos
    import aws_sdk_iotsitewise.types.permission
    import aws_sdk_iotsitewise.types.portal_summary
    import aws_sdk_iotsitewise.types.portal_type
    import aws_sdk_iotsitewise.types.portal_type_configuration
    import aws_sdk_iotsitewise.types.project_summary
    import aws_sdk_iotsitewise.types.property_alias
    import aws_sdk_iotsitewise.types.property_mapping_configuration
    import aws_sdk_iotsitewise.types.property_notification_state
    import aws_sdk_iotsitewise.types.property_unit
    import aws_sdk_iotsitewise.types.put_asset_model_interface_relationship_request
    import aws_sdk_iotsitewise.types.put_asset_model_interface_relationship_response
    import aws_sdk_iotsitewise.types.put_asset_property_value_entries
    import aws_sdk_iotsitewise.types.put_default_encryption_configuration_request
    import aws_sdk_iotsitewise.types.put_default_encryption_configuration_response
    import aws_sdk_iotsitewise.types.put_logging_options_request
    import aws_sdk_iotsitewise.types.put_logging_options_response
    import aws_sdk_iotsitewise.types.put_storage_configuration_request
    import aws_sdk_iotsitewise.types.put_storage_configuration_response
    import aws_sdk_iotsitewise.types.qualities
    import aws_sdk_iotsitewise.types.quality
    import aws_sdk_iotsitewise.types.query_statement
    import aws_sdk_iotsitewise.types.resolution
    import aws_sdk_iotsitewise.types.resolve_to
    import aws_sdk_iotsitewise.types.resolve_to_resource_type
    import aws_sdk_iotsitewise.types.resource
    import aws_sdk_iotsitewise.types.resource_type
    import aws_sdk_iotsitewise.types.restricted_description
    import aws_sdk_iotsitewise.types.restricted_name
    import aws_sdk_iotsitewise.types.retention_period
    import aws_sdk_iotsitewise.types.row
    import aws_sdk_iotsitewise.types.select_all
    import aws_sdk_iotsitewise.types.storage_type
    import aws_sdk_iotsitewise.types.tag_key_list
    import aws_sdk_iotsitewise.types.tag_map
    import aws_sdk_iotsitewise.types.tag_resource_request
    import aws_sdk_iotsitewise.types.tag_resource_response
    import aws_sdk_iotsitewise.types.target_resource
    import aws_sdk_iotsitewise.types.target_resource_type
    import aws_sdk_iotsitewise.types.time_in_seconds
    import aws_sdk_iotsitewise.types.time_ordering
    import aws_sdk_iotsitewise.types.time_series_summary
    import aws_sdk_iotsitewise.types.timestamp
    import aws_sdk_iotsitewise.types.traversal_direction
    import aws_sdk_iotsitewise.types.traversal_type
    import aws_sdk_iotsitewise.types.untag_resource_request
    import aws_sdk_iotsitewise.types.untag_resource_response
    import aws_sdk_iotsitewise.types.update_access_policy_request
    import aws_sdk_iotsitewise.types.update_access_policy_response
    import aws_sdk_iotsitewise.types.update_asset_model_composite_model_request
    import aws_sdk_iotsitewise.types.update_asset_model_composite_model_response
    import aws_sdk_iotsitewise.types.update_asset_model_request
    import aws_sdk_iotsitewise.types.update_asset_model_response
    import aws_sdk_iotsitewise.types.update_asset_property_request
    import aws_sdk_iotsitewise.types.update_asset_request
    import aws_sdk_iotsitewise.types.update_asset_response
    import aws_sdk_iotsitewise.types.update_computation_model_request
    import aws_sdk_iotsitewise.types.update_computation_model_response
    import aws_sdk_iotsitewise.types.update_dashboard_request
    import aws_sdk_iotsitewise.types.update_dashboard_response
    import aws_sdk_iotsitewise.types.update_dataset_request
    import aws_sdk_iotsitewise.types.update_dataset_response
    import aws_sdk_iotsitewise.types.update_gateway_capability_configuration_request
    import aws_sdk_iotsitewise.types.update_gateway_capability_configuration_response
    import aws_sdk_iotsitewise.types.update_gateway_request
    import aws_sdk_iotsitewise.types.update_portal_request
    import aws_sdk_iotsitewise.types.update_portal_response
    import aws_sdk_iotsitewise.types.update_project_request
    import aws_sdk_iotsitewise.types.update_project_response
    import aws_sdk_iotsitewise.types.warm_tier_retention_period
    import aws_sdk_iotsitewise.types.warm_tier_state


class AsyncIoTSiteWiseClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


async def ensure_async_iterator(
    it: AsyncIterator[bytes] | bytes,
) -> AsyncIterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        async for chunk in it:
            yield chunk


class AsyncIoTSiteWiseClient:
    """A client for the ``IoTSiteWise`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self._config = AsyncIoTSiteWiseClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncIoTSiteWiseClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self._config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def associate_assets(
        self,
        asset_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        hierarchy_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        child_asset_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> None:
        """<p>Associates a child asset with the given parent asset through a hierarchy defined in the parent asset's model. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/add-associated-assets.html\">Associating assets</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Args:
            asset_id: <p>The ID of the parent asset. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            hierarchy_id: <p>The ID of a hierarchy in the parent asset's model. (This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.) Hierarchies allow different groupings of assets to be formed that all come from the same asset model. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html\">Asset hierarchies</a> in the <i>IoT SiteWise User Guide</i>.</p>
            child_asset_id: <p>The ID of the child asset to be associated. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.associate_assets_request.AssociateAssetsRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.associate_assets

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.associate_assets.async_associate_assets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.associate_assets_request.AssociateAssetsRequest = {}  # type: ignore[typeddict-item]
        input_["asset_id"] = asset_id
        input_["hierarchy_id"] = hierarchy_id
        input_["child_asset_id"] = child_asset_id
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_time_series_to_asset_property(
        self,
        alias: "aws_sdk_iotsitewise.types.property_alias.PropertyAlias",
        asset_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        property_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> None:
        """<p>Associates a time series (data stream) with an asset property.</p>

        Args:
            alias: <p>The alias that identifies the time series.</p>
            asset_id: <p>The ID of the asset in which the asset property was created. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            property_id: <p>The ID of the asset property. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.associate_time_series_to_asset_property_request.AssociateTimeSeriesToAssetPropertyRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.associate_time_series_to_asset_property

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.associate_time_series_to_asset_property.async_associate_time_series_to_asset_property(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.associate_time_series_to_asset_property_request.AssociateTimeSeriesToAssetPropertyRequest = {}  # type: ignore[typeddict-item]
        input_["alias"] = alias
        input_["asset_id"] = asset_id
        input_["property_id"] = property_id
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_associate_project_assets(
        self,
        project_id: "aws_sdk_iotsitewise.types.id.ID",
        asset_ids: "aws_sdk_iotsitewise.types.i_ds.IDs",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.batch_associate_project_assets_response.BatchAssociateProjectAssetsResponse":
        """<p>Associates a group (batch) of assets with an IoT SiteWise Monitor project.</p>

        Args:
            project_id: <p>The ID of the project to which to associate the assets.</p>
            asset_ids: <p>The IDs of the assets to be associated to the project.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.batch_associate_project_assets_request.BatchAssociateProjectAssetsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.batch_associate_project_assets_response.BatchAssociateProjectAssetsResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.batch_associate_project_assets

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.batch_associate_project_assets.async_batch_associate_project_assets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.batch_associate_project_assets_request.BatchAssociateProjectAssetsRequest = {}  # type: ignore[typeddict-item]
        input_["project_id"] = project_id
        input_["asset_ids"] = asset_ids
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_disassociate_project_assets(
        self,
        project_id: "aws_sdk_iotsitewise.types.id.ID",
        asset_ids: "aws_sdk_iotsitewise.types.i_ds.IDs",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.batch_disassociate_project_assets_response.BatchDisassociateProjectAssetsResponse":
        """<p>Disassociates a group (batch) of assets from an IoT SiteWise Monitor project.</p>

        Args:
            project_id: <p>The ID of the project from which to disassociate the assets.</p>
            asset_ids: <p>The IDs of the assets to be disassociated from the project.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.batch_disassociate_project_assets_request.BatchDisassociateProjectAssetsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.batch_disassociate_project_assets_response.BatchDisassociateProjectAssetsResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.batch_disassociate_project_assets

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.batch_disassociate_project_assets.async_batch_disassociate_project_assets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.batch_disassociate_project_assets_request.BatchDisassociateProjectAssetsRequest = {}  # type: ignore[typeddict-item]
        input_["project_id"] = project_id
        input_["asset_ids"] = asset_ids
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_asset_property_aggregates(
        self,
        entries: "aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_entries.BatchGetAssetPropertyAggregatesEntries",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_max_results.BatchGetAssetPropertyAggregatesMaxResults"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_response.BatchGetAssetPropertyAggregatesResponse":
        """<p>Gets aggregated values (for example, average, minimum, and maximum) for one or more asset properties. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#aggregates\">Querying aggregates</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Args:
            entries: <p>The list of asset property aggregate entries for the batch get request. You can specify up to 16 entries per request.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request. A result set is returned in the two cases, whichever occurs first.</p> <ul> <li> <p>The size of the result set is equal to 1 MB.</p> </li> <li> <p>The number of data points in the result set is equal to the value of <code>maxResults</code>. The maximum value of <code>maxResults</code> is 4000.</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_request.BatchGetAssetPropertyAggregatesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_response.BatchGetAssetPropertyAggregatesResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.batch_get_asset_property_aggregates

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.batch_get_asset_property_aggregates.async_batch_get_asset_property_aggregates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.batch_get_asset_property_aggregates_request.BatchGetAssetPropertyAggregatesRequest = {}  # type: ignore[typeddict-item]
        input_["entries"] = entries
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_asset_property_value(
        self,
        entries: "aws_sdk_iotsitewise.types.batch_get_asset_property_value_entries.BatchGetAssetPropertyValueEntries",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_iotsitewise.types.batch_get_asset_property_value_response.BatchGetAssetPropertyValueResponse":
        """<p>Gets the current value for one or more asset properties. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#current-values\">Querying current values</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Args:
            entries: <p>The list of asset property value entries for the batch get request. You can specify up to 128 entries per request.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.batch_get_asset_property_value_request.BatchGetAssetPropertyValueRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.batch_get_asset_property_value_response.BatchGetAssetPropertyValueResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.batch_get_asset_property_value

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.batch_get_asset_property_value.async_batch_get_asset_property_value(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.batch_get_asset_property_value_request.BatchGetAssetPropertyValueRequest = {}  # type: ignore[typeddict-item]
        input_["entries"] = entries
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_asset_property_value_history(
        self,
        entries: "aws_sdk_iotsitewise.types.batch_get_asset_property_value_history_entries.BatchGetAssetPropertyValueHistoryEntries",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.batch_get_asset_property_value_history_max_results.BatchGetAssetPropertyValueHistoryMaxResults"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.batch_get_asset_property_value_history_response.BatchGetAssetPropertyValueHistoryResponse":
        """<p>Gets the historical values for one or more asset properties. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#historical-values\">Querying historical values</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Args:
            entries: <p>The list of asset property historical value entries for the batch get request. You can specify up to 16 entries per request.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request. A result set is returned in the two cases, whichever occurs first.</p> <ul> <li> <p>The size of the result set is equal to 4 MB.</p> </li> <li> <p>The number of data points in the result set is equal to the value of <code>maxResults</code>. The maximum value of <code>maxResults</code> is 20000.</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.batch_get_asset_property_value_history_request.BatchGetAssetPropertyValueHistoryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.batch_get_asset_property_value_history_response.BatchGetAssetPropertyValueHistoryResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.batch_get_asset_property_value_history

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.batch_get_asset_property_value_history.async_batch_get_asset_property_value_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.batch_get_asset_property_value_history_request.BatchGetAssetPropertyValueHistoryRequest = {}  # type: ignore[typeddict-item]
        input_["entries"] = entries
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_put_asset_property_value(
        self,
        entries: "aws_sdk_iotsitewise.types.put_asset_property_value_entries.PutAssetPropertyValueEntries",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        enable_partial_entry_processing: Optional[
            "aws_sdk_iotsitewise.types.boolean_value.BooleanValue"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.batch_put_asset_property_value_response.BatchPutAssetPropertyValueResponse":
        """<p>Sends a list of asset property values to IoT SiteWise. Each value is a timestamp-quality-value (TQV) data point. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/ingest-api.html\">Ingesting data using the API</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>To identify an asset property, you must specify one of the following:</p> <ul> <li> <p>The <code>assetId</code> and <code>propertyId</code> of an asset property.</p> </li> <li> <p>A <code>propertyAlias</code>, which is a data stream alias (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). To define an asset property's alias, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html\">UpdateAssetProperty</a>.</p> </li> </ul> <important> <p>With respect to Unix epoch time, IoT SiteWise accepts only TQVs that have a timestamp of no more than 7 days in the past and no more than 10 minutes in the future. IoT SiteWise rejects timestamps outside of the inclusive range of [-7 days, +10 minutes] and returns a <code>TimestampOutOfRangeException</code> error.</p> <p>For each asset property, IoT SiteWise overwrites TQVs with duplicate timestamps unless the newer TQV has a different quality. For example, if you store a TQV <code>{T1, GOOD, V1}</code>, then storing <code>{T1, GOOD, V2}</code> replaces the existing TQV.</p> </important> <p>IoT SiteWise authorizes access to each <code>BatchPutAssetPropertyValue</code> entry individually. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-batchputassetpropertyvalue-action\">BatchPutAssetPropertyValue authorization</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Args:
            enable_partial_entry_processing: <p>This setting enables partial ingestion at entry-level. If set to <code>true</code>, we ingest all TQVs not resulting in an error. If set to <code>false</code>, an invalid TQV fails ingestion of the entire entry that contains it.</p>
            entries: <p>The list of asset property value entries for the batch put request. You can specify up to 10 entries per request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.batch_put_asset_property_value_request.BatchPutAssetPropertyValueRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.batch_put_asset_property_value_response.BatchPutAssetPropertyValueResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.batch_put_asset_property_value

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.batch_put_asset_property_value.async_batch_put_asset_property_value(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.batch_put_asset_property_value_request.BatchPutAssetPropertyValueRequest = {}  # type: ignore[typeddict-item]
        if enable_partial_entry_processing is not None:
            input_["enable_partial_entry_processing"] = enable_partial_entry_processing
        input_["entries"] = entries

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_access_policy(
        self,
        access_policy_identity: "aws_sdk_iotsitewise.types.identity.Identity",
        access_policy_resource: "aws_sdk_iotsitewise.types.resource.Resource",
        access_policy_permission: "aws_sdk_iotsitewise.types.permission.Permission",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_iotsitewise.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_iotsitewise.types.create_access_policy_response.CreateAccessPolicyResponse":
        """<p>Creates an access policy that grants the specified identity (IAM Identity Center user, IAM Identity Center group, or IAM user) access to the specified IoT SiteWise Monitor portal or project resource.</p> <note> <p>Support for access policies that use an SSO Group as the identity is not supported at this time.</p> </note>

        Args:
            access_policy_identity: <p>The identity for this access policy. Choose an IAM Identity Center user, an IAM Identity Center group, or an IAM user.</p>
            access_policy_resource: <p>The IoT SiteWise Monitor resource for this access policy. Choose either a portal or a project.</p>
            access_policy_permission: <p>The permission level for this access policy. Note that a project <code>ADMINISTRATOR</code> is also known as a project owner.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            tags: <p>A list of key-value pairs that contain metadata for the access policy. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html\">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.create_access_policy_request.CreateAccessPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.create_access_policy_response.CreateAccessPolicyResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.create_access_policy

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.create_access_policy.async_create_access_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.create_access_policy_request.CreateAccessPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["access_policy_identity"] = access_policy_identity
        input_["access_policy_resource"] = access_policy_resource
        input_["access_policy_permission"] = access_policy_permission
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_asset(
        self,
        asset_name: "aws_sdk_iotsitewise.types.name.Name",
        asset_model_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_id: Optional["aws_sdk_iotsitewise.types.id.ID"] = None,
        asset_external_id: Optional[
            "aws_sdk_iotsitewise.types.external_id.ExternalId"
        ] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_iotsitewise.types.tag_map.TagMap"] = None,
        asset_description: Optional[
            "aws_sdk_iotsitewise.types.description.Description"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.create_asset_response.CreateAssetResponse":
        """<p>Creates an asset from an existing asset model. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-assets.html\">Creating assets</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Args:
            asset_name: <p>A friendly name for the asset.</p>
            asset_model_id: <p>The ID of the asset model from which to create the asset. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            asset_id: <p>The ID to assign to the asset, if desired. IoT SiteWise automatically generates a unique ID for you, so this parameter is never required. However, if you prefer to supply your own ID instead, you can specify it here in UUID format. If you specify your own ID, it must be globally unique.</p>
            asset_external_id: <p>An external ID to assign to the asset. The external ID must be unique within your Amazon Web Services account. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids\">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            tags: <p>A list of key-value pairs that contain metadata for the asset. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html\">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>
            asset_description: <p>A description for the asset.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.create_asset_request.CreateAssetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.create_asset_response.CreateAssetResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.create_asset

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.create_asset.async_create_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.create_asset_request.CreateAssetRequest = {}  # type: ignore[typeddict-item]
        input_["asset_name"] = asset_name
        input_["asset_model_id"] = asset_model_id
        if asset_id is not None:
            input_["asset_id"] = asset_id
        if asset_external_id is not None:
            input_["asset_external_id"] = asset_external_id
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if asset_description is not None:
            input_["asset_description"] = asset_description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_asset_model(
        self,
        asset_model_name: "aws_sdk_iotsitewise.types.name.Name",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_model_type: Optional[
            "aws_sdk_iotsitewise.types.asset_model_type.AssetModelType"
        ] = None,
        asset_model_id: Optional["aws_sdk_iotsitewise.types.id.ID"] = None,
        asset_model_external_id: Optional[
            "aws_sdk_iotsitewise.types.external_id.ExternalId"
        ] = None,
        asset_model_description: Optional[
            "aws_sdk_iotsitewise.types.description.Description"
        ] = None,
        asset_model_properties: Optional[
            "aws_sdk_iotsitewise.types.asset_model_property_definitions.AssetModelPropertyDefinitions"
        ] = None,
        asset_model_hierarchies: Optional[
            "aws_sdk_iotsitewise.types.asset_model_hierarchy_definitions.AssetModelHierarchyDefinitions"
        ] = None,
        asset_model_composite_models: Optional[
            "aws_sdk_iotsitewise.types.asset_model_composite_model_definitions.AssetModelCompositeModelDefinitions"
        ] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_iotsitewise.types.tag_map.TagMap"] = None,
    ) -> (
        "aws_sdk_iotsitewise.types.create_asset_model_response.CreateAssetModelResponse"
    ):
        """<p>Creates an asset model from specified property and hierarchy definitions. You create assets from asset models. With asset models, you can easily create assets of the same type that have standardized definitions. Each asset created from a model inherits the asset model's property and hierarchy definitions. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/define-models.html\">Defining asset models</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>You can create three types of asset models, <code>ASSET_MODEL</code>, <code>COMPONENT_MODEL</code>, or an <code>INTERFACE</code>.</p> <ul> <li> <p> <b>ASSET_MODEL</b> – (default) An asset model that you can use to create assets. Can't be included as a component in another asset model.</p> </li> <li> <p> <b>COMPONENT_MODEL</b> – A reusable component that you can include in the composite models of other asset models. You can't create assets directly from this type of asset model. </p> </li> <li> <p> <b>INTERFACE</b> – An interface is a type of model that defines a standard structure that can be applied to different asset models.</p> </li> </ul>

        Args:
            asset_model_name: <p>A unique name for the asset model.</p>
            asset_model_type: <p>The type of asset model.</p> <ul> <li> <p> <b>ASSET_MODEL</b> – (default) An asset model that you can use to create assets. Can't be included as a component in another asset model.</p> </li> <li> <p> <b>COMPONENT_MODEL</b> – A reusable component that you can include in the composite models of other asset models. You can't create assets directly from this type of asset model. </p> </li> </ul>
            asset_model_id: <p>The ID to assign to the asset model, if desired. IoT SiteWise automatically generates a unique ID for you, so this parameter is never required. However, if you prefer to supply your own ID instead, you can specify it here in UUID format. If you specify your own ID, it must be globally unique.</p>
            asset_model_external_id: <p>An external ID to assign to the asset model. The external ID must be unique within your Amazon Web Services account. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids\">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            asset_model_description: <p>A description for the asset model.</p>
            asset_model_properties: <p>The property definitions of the asset model. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-properties.html\">Asset properties</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>You can specify up to 200 properties per asset model. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html\">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            asset_model_hierarchies: <p>The hierarchy definitions of the asset model. Each hierarchy specifies an asset model whose assets can be children of any other assets created from this asset model. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html\">Asset hierarchies</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>You can specify up to 10 hierarchies per asset model. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html\">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            asset_model_composite_models: <p>The composite models that are part of this asset model. It groups properties (such as attributes, measurements, transforms, and metrics) and child composite models that model parts of your industrial equipment. Each composite model has a type that defines the properties that the composite model supports. Use composite models to define alarms on this asset model.</p> <note> <p>When creating custom composite models, you need to use <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModelCompositeModel.html\">CreateAssetModelCompositeModel</a>. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-custom-composite-models.html\">Creating custom composite models (Components)</a> in the <i>IoT SiteWise User Guide</i>.</p> </note>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            tags: <p>A list of key-value pairs that contain metadata for the asset model. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html\">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.create_asset_model_request.CreateAssetModelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.create_asset_model_response.CreateAssetModelResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.create_asset_model

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.create_asset_model.async_create_asset_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.create_asset_model_request.CreateAssetModelRequest = {}  # type: ignore[typeddict-item]
        input_["asset_model_name"] = asset_model_name
        if asset_model_type is not None:
            input_["asset_model_type"] = asset_model_type
        if asset_model_id is not None:
            input_["asset_model_id"] = asset_model_id
        if asset_model_external_id is not None:
            input_["asset_model_external_id"] = asset_model_external_id
        if asset_model_description is not None:
            input_["asset_model_description"] = asset_model_description
        if asset_model_properties is not None:
            input_["asset_model_properties"] = asset_model_properties
        if asset_model_hierarchies is not None:
            input_["asset_model_hierarchies"] = asset_model_hierarchies
        if asset_model_composite_models is not None:
            input_["asset_model_composite_models"] = asset_model_composite_models
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_asset_model_composite_model(
        self,
        asset_model_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        asset_model_composite_model_name: "aws_sdk_iotsitewise.types.name.Name",
        asset_model_composite_model_type: "aws_sdk_iotsitewise.types.name.Name",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_model_composite_model_external_id: Optional[
            "aws_sdk_iotsitewise.types.external_id.ExternalId"
        ] = None,
        parent_asset_model_composite_model_id: Optional[
            "aws_sdk_iotsitewise.types.custom_id.CustomID"
        ] = None,
        asset_model_composite_model_id: Optional[
            "aws_sdk_iotsitewise.types.id.ID"
        ] = None,
        asset_model_composite_model_description: Optional[
            "aws_sdk_iotsitewise.types.description.Description"
        ] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
        composed_asset_model_id: Optional[
            "aws_sdk_iotsitewise.types.custom_id.CustomID"
        ] = None,
        asset_model_composite_model_properties: Optional[
            "aws_sdk_iotsitewise.types.asset_model_property_definitions.AssetModelPropertyDefinitions"
        ] = None,
        if_match: Optional["aws_sdk_iotsitewise.types.e_tag.ETag"] = None,
        if_none_match: Optional[
            "aws_sdk_iotsitewise.types.select_all.SelectAll"
        ] = None,
        match_for_version_type: Optional[
            "aws_sdk_iotsitewise.types.asset_model_version_type.AssetModelVersionType"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.create_asset_model_composite_model_response.CreateAssetModelCompositeModelResponse":
        """<p>Creates a custom composite model from specified property and hierarchy definitions. There are two types of custom composite models, <code>inline</code> and <code>component-model-based</code>. </p> <p>Use component-model-based custom composite models to define standard, reusable components. A component-model-based custom composite model consists of a name, a description, and the ID of the component model it references. A component-model-based custom composite model has no properties of its own; its referenced component model provides its associated properties to any created assets. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/custom-composite-models.html\">Custom composite models (Components)</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>Use inline custom composite models to organize the properties of an asset model. The properties of inline custom composite models are local to the asset model where they are included and can't be used to create multiple assets.</p> <p>To create a component-model-based model, specify the <code>composedAssetModelId</code> of an existing asset model with <code>assetModelType</code> of <code>COMPONENT_MODEL</code>.</p> <p>To create an inline model, specify the <code>assetModelCompositeModelProperties</code> and don't include an <code>composedAssetModelId</code>.</p>

        Args:
            asset_model_id: <p>The ID of the asset model this composite model is a part of.</p>
            asset_model_composite_model_external_id: <p>An external ID to assign to the composite model.</p> <p>If the composite model is a derived composite model, or one nested inside a component model, you can only set the external ID using <code>UpdateAssetModelCompositeModel</code> and specifying the derived ID of the model or property from the created model it's a part of.</p>
            parent_asset_model_composite_model_id: <p>The ID of the parent composite model in this asset model relationship.</p>
            asset_model_composite_model_id: <p>The ID of the composite model. IoT SiteWise automatically generates a unique ID for you, so this parameter is never required. However, if you prefer to supply your own ID instead, you can specify it here in UUID format. If you specify your own ID, it must be globally unique.</p>
            asset_model_composite_model_description: <p>A description for the composite model.</p>
            asset_model_composite_model_name: <p>A unique name for the composite model.</p>
            asset_model_composite_model_type: <p>The composite model type. Valid values are <code>AWS/ALARM</code>, <code>CUSTOM</code>, or <code> AWS/L4E_ANOMALY</code>.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            composed_asset_model_id: <p>The ID of a component model which is reused to create this composite model.</p>
            asset_model_composite_model_properties: <p>The property definitions of the composite model. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/custom-composite-models.html#inline-composite-models\"> Inline custom composite models</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>You can specify up to 200 properties per composite model. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html\">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            if_match: <p>The expected current entity tag (ETag) for the asset model’s latest or active version (specified using <code>matchForVersionType</code>). The create request is rejected if the tag does not match the latest or active version's current entity tag. See <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/opt-locking-for-model.html\">Optimistic locking for asset model writes</a> in the <i>IoT SiteWise User Guide</i>.</p>
            if_none_match: <p>Accepts <b>*</b> to reject the create request if an active version (specified using <code>matchForVersionType</code> as <code>ACTIVE</code>) already exists for the asset model.</p>
            match_for_version_type: <p>Specifies the asset model version type (<code>LATEST</code> or <code>ACTIVE</code>) used in conjunction with <code>If-Match</code> or <code>If-None-Match</code> headers to determine the target ETag for the create operation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.create_asset_model_composite_model_request.CreateAssetModelCompositeModelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.create_asset_model_composite_model_response.CreateAssetModelCompositeModelResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.create_asset_model_composite_model

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.create_asset_model_composite_model.async_create_asset_model_composite_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.create_asset_model_composite_model_request.CreateAssetModelCompositeModelRequest = {}  # type: ignore[typeddict-item]
        input_["asset_model_id"] = asset_model_id
        if asset_model_composite_model_external_id is not None:
            input_["asset_model_composite_model_external_id"] = (
                asset_model_composite_model_external_id
            )
        if parent_asset_model_composite_model_id is not None:
            input_["parent_asset_model_composite_model_id"] = (
                parent_asset_model_composite_model_id
            )
        if asset_model_composite_model_id is not None:
            input_["asset_model_composite_model_id"] = asset_model_composite_model_id
        if asset_model_composite_model_description is not None:
            input_["asset_model_composite_model_description"] = (
                asset_model_composite_model_description
            )
        input_["asset_model_composite_model_name"] = asset_model_composite_model_name
        input_["asset_model_composite_model_type"] = asset_model_composite_model_type
        if client_token is not None:
            input_["client_token"] = client_token
        if composed_asset_model_id is not None:
            input_["composed_asset_model_id"] = composed_asset_model_id
        if asset_model_composite_model_properties is not None:
            input_["asset_model_composite_model_properties"] = (
                asset_model_composite_model_properties
            )
        if if_match is not None:
            input_["if_match"] = if_match
        if if_none_match is not None:
            input_["if_none_match"] = if_none_match
        if match_for_version_type is not None:
            input_["match_for_version_type"] = match_for_version_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_bulk_import_job(
        self,
        job_name: "aws_sdk_iotsitewise.types.name.Name",
        job_role_arn: "aws_sdk_iotsitewise.types.arn.ARN",
        files: "aws_sdk_iotsitewise.types.files.Files",
        error_report_location: "aws_sdk_iotsitewise.types.error_report_location.ErrorReportLocation",
        job_configuration: "aws_sdk_iotsitewise.types.job_configuration.JobConfiguration",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        adaptive_ingestion: Optional[
            "aws_sdk_iotsitewise.types.adaptive_ingestion.AdaptiveIngestion"
        ] = None,
        delete_files_after_import: Optional[
            "aws_sdk_iotsitewise.types.delete_files_after_import.DeleteFilesAfterImport"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.create_bulk_import_job_response.CreateBulkImportJobResponse":
        """<p>Defines a job to ingest data to IoT SiteWise from Amazon S3. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/CreateBulkImportJob.html\">Create a bulk import job (CLI)</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <important> <p>Before you create a bulk import job, you must enable IoT SiteWise warm tier or IoT SiteWise cold tier. For more information about how to configure storage settings, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PutStorageConfiguration.html\">PutStorageConfiguration</a>.</p> <p>Bulk import is designed to store historical data to IoT SiteWise.</p> <ul> <li> <p>Newly ingested data in the hot tier triggers notifications and computations.</p> </li> <li> <p>After data moves from the hot tier to the warm or cold tier based on retention settings, it does not trigger computations or notifications.</p> </li> <li> <p>Data older than 7 days does not trigger computations or notifications.</p> </li> </ul> </important>

        Args:
            job_name: <p>The unique name that helps identify the job request.</p>
            job_role_arn: <p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the IAM role that allows IoT SiteWise to read Amazon S3 data.</p>
            files: <p>The files in the specified Amazon S3 bucket that contain your data.</p>
            error_report_location: <p>The Amazon S3 destination where errors associated with the job creation request are saved.</p>
            job_configuration: <p>Contains the configuration information of a job, such as the file format used to save data in Amazon S3.</p>
            adaptive_ingestion: <p>If set to true, ingest new data into IoT SiteWise storage. Measurements with notifications, metrics and transforms are computed. If set to false, historical data is ingested into IoT SiteWise as is.</p>
            delete_files_after_import: <p>If set to true, your data files is deleted from S3, after ingestion into IoT SiteWise storage.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.create_bulk_import_job_request.CreateBulkImportJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.create_bulk_import_job_response.CreateBulkImportJobResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.create_bulk_import_job

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.create_bulk_import_job.async_create_bulk_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.create_bulk_import_job_request.CreateBulkImportJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_name"] = job_name
        input_["job_role_arn"] = job_role_arn
        input_["files"] = files
        input_["error_report_location"] = error_report_location
        input_["job_configuration"] = job_configuration
        if adaptive_ingestion is not None:
            input_["adaptive_ingestion"] = adaptive_ingestion
        if delete_files_after_import is not None:
            input_["delete_files_after_import"] = delete_files_after_import

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_computation_model(
        self,
        computation_model_name: "aws_sdk_iotsitewise.types.restricted_name.RestrictedName",
        computation_model_configuration: "aws_sdk_iotsitewise.types.computation_model_configuration.ComputationModelConfiguration",
        computation_model_data_binding: "aws_sdk_iotsitewise.types.computation_model_data_binding.ComputationModelDataBinding",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        computation_model_description: Optional[
            "aws_sdk_iotsitewise.types.restricted_description.RestrictedDescription"
        ] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_iotsitewise.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_iotsitewise.types.create_computation_model_response.CreateComputationModelResponse":
        """<p>Create a computation model with a configuration and data binding.</p>

        Args:
            computation_model_name: <p>The name of the computation model.</p>
            computation_model_description: <p>The description of the computation model.</p>
            computation_model_configuration: <p>The configuration for the computation model.</p>
            computation_model_data_binding: <p>The data binding for the computation model. Key is a variable name defined in configuration. Value is a <code>ComputationModelDataBindingValue</code> referenced by the variable.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            tags: <p>A list of key-value pairs that contain metadata for the asset. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html\">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.create_computation_model_request.CreateComputationModelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.create_computation_model_response.CreateComputationModelResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.create_computation_model

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.create_computation_model.async_create_computation_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.create_computation_model_request.CreateComputationModelRequest = {}  # type: ignore[typeddict-item]
        input_["computation_model_name"] = computation_model_name
        if computation_model_description is not None:
            input_["computation_model_description"] = computation_model_description
        input_["computation_model_configuration"] = computation_model_configuration
        input_["computation_model_data_binding"] = computation_model_data_binding
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_dashboard(
        self,
        project_id: "aws_sdk_iotsitewise.types.id.ID",
        dashboard_name: "aws_sdk_iotsitewise.types.name.Name",
        dashboard_definition: "aws_sdk_iotsitewise.types.dashboard_definition.DashboardDefinition",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        dashboard_description: Optional[
            "aws_sdk_iotsitewise.types.description.Description"
        ] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_iotsitewise.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_iotsitewise.types.create_dashboard_response.CreateDashboardResponse":
        """<p>Creates a dashboard in an IoT SiteWise Monitor project.</p>

        Args:
            project_id: <p>The ID of the project in which to create the dashboard.</p>
            dashboard_name: <p>A friendly name for the dashboard.</p>
            dashboard_description: <p>A description for the dashboard.</p>
            dashboard_definition: <p>The dashboard definition specified in a JSON literal.</p> <ul> <li> <p>IoT SiteWise Monitor (Classic) see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboards-using-aws-cli.html\">Create dashboards (CLI)</a> </p> </li> <li> <p>IoT SiteWise Monitor (AI-aware) see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboards-ai-dashboard-cli.html\">Create dashboards (CLI)</a> </p> </li> </ul> <p>in the <i>IoT SiteWise User Guide</i> </p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            tags: <p>A list of key-value pairs that contain metadata for the dashboard. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html\">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.create_dashboard_request.CreateDashboardRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.create_dashboard_response.CreateDashboardResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.create_dashboard

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.create_dashboard.async_create_dashboard(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.create_dashboard_request.CreateDashboardRequest = {}  # type: ignore[typeddict-item]
        input_["project_id"] = project_id
        input_["dashboard_name"] = dashboard_name
        if dashboard_description is not None:
            input_["dashboard_description"] = dashboard_description
        input_["dashboard_definition"] = dashboard_definition
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_dataset(
        self,
        dataset_name: "aws_sdk_iotsitewise.types.restricted_name.RestrictedName",
        dataset_source: "aws_sdk_iotsitewise.types.dataset_source.DatasetSource",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        dataset_id: Optional["aws_sdk_iotsitewise.types.id.ID"] = None,
        dataset_description: Optional[
            "aws_sdk_iotsitewise.types.restricted_description.RestrictedDescription"
        ] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_iotsitewise.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_iotsitewise.types.create_dataset_response.CreateDatasetResponse":
        """<p>Creates a dataset to connect an external datasource.</p>

        Args:
            dataset_id: <p>The ID of the dataset.</p>
            dataset_name: <p>The name of the dataset.</p>
            dataset_description: <p>A description about the dataset, and its functionality.</p>
            dataset_source: <p>The data source for the dataset.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            tags: <p>A list of key-value pairs that contain metadata for the access policy. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html\">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.create_dataset_request.CreateDatasetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.create_dataset_response.CreateDatasetResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.create_dataset

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.create_dataset.async_create_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.create_dataset_request.CreateDatasetRequest = {}  # type: ignore[typeddict-item]
        if dataset_id is not None:
            input_["dataset_id"] = dataset_id
        input_["dataset_name"] = dataset_name
        if dataset_description is not None:
            input_["dataset_description"] = dataset_description
        input_["dataset_source"] = dataset_source
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_gateway(
        self,
        gateway_name: "aws_sdk_iotsitewise.types.gateway_name.GatewayName",
        gateway_platform: "aws_sdk_iotsitewise.types.gateway_platform.GatewayPlatform",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        gateway_version: Optional[
            "aws_sdk_iotsitewise.types.gateway_version.GatewayVersion"
        ] = None,
        tags: Optional["aws_sdk_iotsitewise.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_iotsitewise.types.create_gateway_response.CreateGatewayResponse":
        """<p>Creates a gateway, which is a virtual or edge device that delivers industrial data streams from local servers to IoT SiteWise. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateway-connector.html\">Ingesting data using a gateway</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Args:
            gateway_name: <p>A unique name for the gateway.</p>
            gateway_platform: <p>The gateway's platform. You can only specify one platform in a gateway.</p>
            gateway_version: <p>The version of the gateway to create. Specify <code>3</code> to create an MQTT-enabled, V3 gateway and <code>2</code> to create a Classic streams, V2 gateway. If not specified, the default is <code>2</code> (Classic streams, V2 gateway).</p> <note> <p>When creating a V3 gateway (<code>gatewayVersion=3</code>) with the <code>GreengrassV2</code> platform, you must also specify the <code>coreDeviceOperatingSystem</code> parameter.</p> </note> <p> We recommend creating an MQTT-enabled gateway for self-hosted gateways and Siemens Industrial Edge gateways. For more information on gateway versions, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateways.html\">Use Amazon Web Services IoT SiteWise Edge Edge gateways</a>.</p>
            tags: <p>A list of key-value pairs that contain metadata for the gateway. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html\">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.create_gateway_request.CreateGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.create_gateway_response.CreateGatewayResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.create_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.create_gateway.async_create_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.create_gateway_request.CreateGatewayRequest = {}  # type: ignore[typeddict-item]
        input_["gateway_name"] = gateway_name
        input_["gateway_platform"] = gateway_platform
        if gateway_version is not None:
            input_["gateway_version"] = gateway_version
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_portal(
        self,
        portal_name: "aws_sdk_iotsitewise.types.name.Name",
        portal_contact_email: "aws_sdk_iotsitewise.types.email.Email",
        role_arn: "aws_sdk_iotsitewise.types.iam_arn.IamArn",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        portal_description: Optional[
            "aws_sdk_iotsitewise.types.description.Description"
        ] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
        portal_logo_image_file: Optional[
            "aws_sdk_iotsitewise.types.image_file.ImageFile"
        ] = None,
        tags: Optional["aws_sdk_iotsitewise.types.tag_map.TagMap"] = None,
        portal_auth_mode: Optional[
            "aws_sdk_iotsitewise.types.auth_mode.AuthMode"
        ] = None,
        notification_sender_email: Optional[
            "aws_sdk_iotsitewise.types.email.Email"
        ] = None,
        alarms: Optional["aws_sdk_iotsitewise.types.alarms.Alarms"] = None,
        portal_type: Optional[
            "aws_sdk_iotsitewise.types.portal_type.PortalType"
        ] = None,
        portal_type_configuration: Optional[
            "aws_sdk_iotsitewise.types.portal_type_configuration.PortalTypeConfiguration"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.create_portal_response.CreatePortalResponse":
        """<p>Creates a portal, which can contain projects and dashboards. IoT SiteWise Monitor uses IAM Identity Center or IAM to authenticate portal users and manage user permissions.</p> <note> <p>Before you can sign in to a new portal, you must add at least one identity to that portal. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/administer-portals.html#portal-change-admins\">Adding or removing portal administrators</a> in the <i>IoT SiteWise User Guide</i>.</p> </note>

        Args:
            portal_name: <p>A friendly name for the portal.</p>
            portal_description: <p>A description for the portal.</p>
            portal_contact_email: <p>The Amazon Web Services administrator's contact email address.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            portal_logo_image_file: <p>A logo image to display in the portal. Upload a square, high-resolution image. The image is displayed on a dark background.</p>
            role_arn: <p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of a service role that allows the portal's users to access your IoT SiteWise resources on your behalf. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-service-role.html\">Using service roles for IoT SiteWise Monitor</a> in the <i>IoT SiteWise User Guide</i>.</p>
            tags: <p>A list of key-value pairs that contain metadata for the portal. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html\">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>
            portal_auth_mode: <p>The service to use to authenticate users to the portal. Choose from the following options:</p> <ul> <li> <p> <code>SSO</code> – The portal uses IAM Identity Center to authenticate users and manage user permissions. Before you can create a portal that uses IAM Identity Center, you must enable IAM Identity Center. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-get-started.html#mon-gs-sso\">Enabling IAM Identity Center</a> in the <i>IoT SiteWise User Guide</i>. This option is only available in Amazon Web Services Regions other than the China Regions.</p> </li> <li> <p> <code>IAM</code> – The portal uses Identity and Access Management to authenticate users and manage user permissions.</p> </li> </ul> <p>You can't change this value after you create a portal.</p> <p>Default: <code>SSO</code> </p>
            notification_sender_email: <p>The email address that sends alarm notifications.</p> <important> <p>If you use the <a href=\"https://docs.aws.amazon.com/iotevents/latest/developerguide/lambda-support.html\">IoT Events managed Lambda function</a> to manage your emails, you must <a href=\"https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-email-addresses.html\">verify the sender email address in Amazon SES</a>.</p> </important>
            alarms: <p>Contains the configuration information of an alarm created in an IoT SiteWise Monitor portal. You can use the alarm to monitor an asset property and get notified when the asset property value is outside a specified range. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/appguide/monitor-alarms.html\">Monitoring with alarms</a> in the <i>IoT SiteWise Application Guide</i>.</p>
            portal_type: <p>Define the type of portal. The value for IoT SiteWise Monitor (Classic) is <code>SITEWISE_PORTAL_V1</code>. The value for IoT SiteWise Monitor (AI-aware) is <code>SITEWISE_PORTAL_V2</code>.</p>
            portal_type_configuration: <p>The configuration entry associated with the specific portal type. The value for IoT SiteWise Monitor (Classic) is <code>SITEWISE_PORTAL_V1</code>. The value for IoT SiteWise Monitor (AI-aware) is <code>SITEWISE_PORTAL_V2</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.create_portal_request.CreatePortalRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.create_portal_response.CreatePortalResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.create_portal

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.create_portal.async_create_portal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.create_portal_request.CreatePortalRequest = {}  # type: ignore[typeddict-item]
        input_["portal_name"] = portal_name
        if portal_description is not None:
            input_["portal_description"] = portal_description
        input_["portal_contact_email"] = portal_contact_email
        if client_token is not None:
            input_["client_token"] = client_token
        if portal_logo_image_file is not None:
            input_["portal_logo_image_file"] = portal_logo_image_file
        input_["role_arn"] = role_arn
        if tags is not None:
            input_["tags"] = tags
        if portal_auth_mode is not None:
            input_["portal_auth_mode"] = portal_auth_mode
        if notification_sender_email is not None:
            input_["notification_sender_email"] = notification_sender_email
        if alarms is not None:
            input_["alarms"] = alarms
        if portal_type is not None:
            input_["portal_type"] = portal_type
        if portal_type_configuration is not None:
            input_["portal_type_configuration"] = portal_type_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_project(
        self,
        portal_id: "aws_sdk_iotsitewise.types.id.ID",
        project_name: "aws_sdk_iotsitewise.types.name.Name",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        project_description: Optional[
            "aws_sdk_iotsitewise.types.description.Description"
        ] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_iotsitewise.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_iotsitewise.types.create_project_response.CreateProjectResponse":
        """<p>Creates a project in the specified portal.</p> <note> <p>Make sure that the project name and description don't contain confidential information.</p> </note>

        Args:
            portal_id: <p>The ID of the portal in which to create the project.</p>
            project_name: <p>A friendly name for the project.</p>
            project_description: <p>A description for the project.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            tags: <p>A list of key-value pairs that contain metadata for the project. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html\">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.create_project_request.CreateProjectRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.create_project_response.CreateProjectResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.create_project

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.create_project.async_create_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.create_project_request.CreateProjectRequest = {}  # type: ignore[typeddict-item]
        input_["portal_id"] = portal_id
        input_["project_name"] = project_name
        if project_description is not None:
            input_["project_description"] = project_description
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_access_policy(
        self,
        access_policy_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.delete_access_policy_response.DeleteAccessPolicyResponse":
        """<p>Deletes an access policy that grants the specified identity access to the specified IoT SiteWise Monitor resource. You can use this operation to revoke access to an IoT SiteWise Monitor resource.</p>

        Args:
            access_policy_id: <p>The ID of the access policy to be deleted.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.delete_access_policy_request.DeleteAccessPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.delete_access_policy_response.DeleteAccessPolicyResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.delete_access_policy

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.delete_access_policy.async_delete_access_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.delete_access_policy_request.DeleteAccessPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["access_policy_id"] = access_policy_id
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_asset(
        self,
        asset_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.delete_asset_response.DeleteAssetResponse":
        """<p>Deletes an asset. This action can't be undone. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/delete-assets-and-models.html\">Deleting assets and models</a> in the <i>IoT SiteWise User Guide</i>.</p> <note> <p>You can't delete an asset that's associated to another asset. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DisassociateAssets.html\">DisassociateAssets</a>.</p> </note>

        Args:
            asset_id: <p>The ID of the asset to delete. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.delete_asset_request.DeleteAssetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.delete_asset_response.DeleteAssetResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.delete_asset

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.delete_asset.async_delete_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.delete_asset_request.DeleteAssetRequest = {}  # type: ignore[typeddict-item]
        input_["asset_id"] = asset_id
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_asset_model(
        self,
        asset_model_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
        if_match: Optional["aws_sdk_iotsitewise.types.e_tag.ETag"] = None,
        if_none_match: Optional[
            "aws_sdk_iotsitewise.types.select_all.SelectAll"
        ] = None,
        match_for_version_type: Optional[
            "aws_sdk_iotsitewise.types.asset_model_version_type.AssetModelVersionType"
        ] = None,
    ) -> (
        "aws_sdk_iotsitewise.types.delete_asset_model_response.DeleteAssetModelResponse"
    ):
        """<p>Deletes an asset model. This action can't be undone. You must delete all assets created from an asset model before you can delete the model. Also, you can't delete an asset model if a parent asset model exists that contains a property formula expression that depends on the asset model that you want to delete. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/delete-assets-and-models.html\">Deleting assets and models</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Args:
            asset_model_id: <p>The ID of the asset model to delete. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            if_match: <p>The expected current entity tag (ETag) for the asset model’s latest or active version (specified using <code>matchForVersionType</code>). The delete request is rejected if the tag does not match the latest or active version's current entity tag. See <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/opt-locking-for-model.html\">Optimistic locking for asset model writes</a> in the <i>IoT SiteWise User Guide</i>.</p>
            if_none_match: <p>Accepts <b>*</b> to reject the delete request if an active version (specified using <code>matchForVersionType</code> as <code>ACTIVE</code>) already exists for the asset model.</p>
            match_for_version_type: <p>Specifies the asset model version type (<code>LATEST</code> or <code>ACTIVE</code>) used in conjunction with <code>If-Match</code> or <code>If-None-Match</code> headers to determine the target ETag for the delete operation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.delete_asset_model_request.DeleteAssetModelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.delete_asset_model_response.DeleteAssetModelResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.delete_asset_model

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.delete_asset_model.async_delete_asset_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.delete_asset_model_request.DeleteAssetModelRequest = {}  # type: ignore[typeddict-item]
        input_["asset_model_id"] = asset_model_id
        if client_token is not None:
            input_["client_token"] = client_token
        if if_match is not None:
            input_["if_match"] = if_match
        if if_none_match is not None:
            input_["if_none_match"] = if_none_match
        if match_for_version_type is not None:
            input_["match_for_version_type"] = match_for_version_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_asset_model_composite_model(
        self,
        asset_model_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        asset_model_composite_model_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
        if_match: Optional["aws_sdk_iotsitewise.types.e_tag.ETag"] = None,
        if_none_match: Optional[
            "aws_sdk_iotsitewise.types.select_all.SelectAll"
        ] = None,
        match_for_version_type: Optional[
            "aws_sdk_iotsitewise.types.asset_model_version_type.AssetModelVersionType"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.delete_asset_model_composite_model_response.DeleteAssetModelCompositeModelResponse":
        """<p>Deletes a composite model. This action can't be undone. You must delete all assets created from a composite model before you can delete the model. Also, you can't delete a composite model if a parent asset model exists that contains a property formula expression that depends on the asset model that you want to delete. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/delete-assets-and-models.html\">Deleting assets and models</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Args:
            asset_model_id: <p>The ID of the asset model, in UUID format.</p>
            asset_model_composite_model_id: <p>The ID of a composite model on this asset model.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            if_match: <p>The expected current entity tag (ETag) for the asset model’s latest or active version (specified using <code>matchForVersionType</code>). The delete request is rejected if the tag does not match the latest or active version's current entity tag. See <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/opt-locking-for-model.html\">Optimistic locking for asset model writes</a> in the <i>IoT SiteWise User Guide</i>.</p>
            if_none_match: <p>Accepts <b>*</b> to reject the delete request if an active version (specified using <code>matchForVersionType</code> as <code>ACTIVE</code>) already exists for the asset model.</p>
            match_for_version_type: <p>Specifies the asset model version type (<code>LATEST</code> or <code>ACTIVE</code>) used in conjunction with <code>If-Match</code> or <code>If-None-Match</code> headers to determine the target ETag for the delete operation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.delete_asset_model_composite_model_request.DeleteAssetModelCompositeModelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.delete_asset_model_composite_model_response.DeleteAssetModelCompositeModelResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.delete_asset_model_composite_model

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.delete_asset_model_composite_model.async_delete_asset_model_composite_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.delete_asset_model_composite_model_request.DeleteAssetModelCompositeModelRequest = {}  # type: ignore[typeddict-item]
        input_["asset_model_id"] = asset_model_id
        input_["asset_model_composite_model_id"] = asset_model_composite_model_id
        if client_token is not None:
            input_["client_token"] = client_token
        if if_match is not None:
            input_["if_match"] = if_match
        if if_none_match is not None:
            input_["if_none_match"] = if_none_match
        if match_for_version_type is not None:
            input_["match_for_version_type"] = match_for_version_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_asset_model_interface_relationship(
        self,
        asset_model_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        interface_asset_model_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.delete_asset_model_interface_relationship_response.DeleteAssetModelInterfaceRelationshipResponse":
        """<p>Deletes an interface relationship between an asset model and an interface asset model.</p>

        Args:
            asset_model_id: <p>The ID of the asset model. This can be either the actual ID in UUID format, or else externalId: followed by the external ID.</p>
            interface_asset_model_id: <p>The ID of the interface asset model. This can be either the actual ID in UUID format, or else externalId: followed by the external ID.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.delete_asset_model_interface_relationship_request.DeleteAssetModelInterfaceRelationshipRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.delete_asset_model_interface_relationship_response.DeleteAssetModelInterfaceRelationshipResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.delete_asset_model_interface_relationship

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.delete_asset_model_interface_relationship.async_delete_asset_model_interface_relationship(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.delete_asset_model_interface_relationship_request.DeleteAssetModelInterfaceRelationshipRequest = {}  # type: ignore[typeddict-item]
        input_["asset_model_id"] = asset_model_id
        input_["interface_asset_model_id"] = interface_asset_model_id
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_computation_model(
        self,
        computation_model_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.delete_computation_model_response.DeleteComputationModelResponse":
        """<p>Deletes a computation model. This action can't be undone.</p>

        Args:
            computation_model_id: <p>The ID of the computation model.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.delete_computation_model_request.DeleteComputationModelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.delete_computation_model_response.DeleteComputationModelResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.delete_computation_model

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.delete_computation_model.async_delete_computation_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.delete_computation_model_request.DeleteComputationModelRequest = {}  # type: ignore[typeddict-item]
        input_["computation_model_id"] = computation_model_id
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_dashboard(
        self,
        dashboard_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.delete_dashboard_response.DeleteDashboardResponse":
        """<p>Deletes a dashboard from IoT SiteWise Monitor.</p>

        Args:
            dashboard_id: <p>The ID of the dashboard to delete.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.delete_dashboard_request.DeleteDashboardRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.delete_dashboard_response.DeleteDashboardResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.delete_dashboard

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.delete_dashboard.async_delete_dashboard(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.delete_dashboard_request.DeleteDashboardRequest = {}  # type: ignore[typeddict-item]
        input_["dashboard_id"] = dashboard_id
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_dataset(
        self,
        dataset_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.delete_dataset_response.DeleteDatasetResponse":
        """<p>Deletes a dataset. This cannot be undone.</p>

        Args:
            dataset_id: <p>The ID of the dataset.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.delete_dataset_request.DeleteDatasetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.delete_dataset_response.DeleteDatasetResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.delete_dataset

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.delete_dataset.async_delete_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.delete_dataset_request.DeleteDatasetRequest = {}  # type: ignore[typeddict-item]
        input_["dataset_id"] = dataset_id
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_gateway(
        self,
        gateway_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> None:
        """<p>Deletes a gateway from IoT SiteWise. When you delete a gateway, some of the gateway's files remain in your gateway's file system.</p>

        Args:
            gateway_id: <p>The ID of the gateway to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.delete_gateway_request.DeleteGatewayRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.delete_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.delete_gateway.async_delete_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.delete_gateway_request.DeleteGatewayRequest = {}  # type: ignore[typeddict-item]
        input_["gateway_id"] = gateway_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_portal(
        self,
        portal_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.delete_portal_response.DeletePortalResponse":
        """<p>Deletes a portal from IoT SiteWise Monitor.</p>

        Args:
            portal_id: <p>The ID of the portal to delete.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.delete_portal_request.DeletePortalRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.delete_portal_response.DeletePortalResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.delete_portal

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.delete_portal.async_delete_portal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.delete_portal_request.DeletePortalRequest = {}  # type: ignore[typeddict-item]
        input_["portal_id"] = portal_id
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_project(
        self,
        project_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.delete_project_response.DeleteProjectResponse":
        """<p>Deletes a project from IoT SiteWise Monitor.</p>

        Args:
            project_id: <p>The ID of the project.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.delete_project_request.DeleteProjectRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.delete_project_response.DeleteProjectResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.delete_project

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.delete_project.async_delete_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.delete_project_request.DeleteProjectRequest = {}  # type: ignore[typeddict-item]
        input_["project_id"] = project_id
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_time_series(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        alias: Optional[
            "aws_sdk_iotsitewise.types.property_alias.PropertyAlias"
        ] = None,
        asset_id: Optional["aws_sdk_iotsitewise.types.custom_id.CustomID"] = None,
        property_id: Optional["aws_sdk_iotsitewise.types.custom_id.CustomID"] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> None:
        """<p>Deletes a time series (data stream). If you delete a time series that's associated with an asset property, the asset property still exists, but the time series will no longer be associated with this asset property.</p> <p>To identify a time series, do one of the following:</p> <ul> <li> <p>If the time series isn't associated with an asset property, specify the <code>alias</code> of the time series.</p> </li> <li> <p>If the time series is associated with an asset property, specify one of the following: </p> <ul> <li> <p>The <code>alias</code> of the time series.</p> </li> <li> <p>The <code>assetId</code> and <code>propertyId</code> that identifies the asset property.</p> </li> </ul> </li> </ul>

        Args:
            alias: <p>The alias that identifies the time series.</p>
            asset_id: <p>The ID of the asset in which the asset property was created. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            property_id: <p>The ID of the asset property. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.delete_time_series_request.DeleteTimeSeriesRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.delete_time_series

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.delete_time_series.async_delete_time_series(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.delete_time_series_request.DeleteTimeSeriesRequest = {}  # type: ignore[typeddict-item]
        if alias is not None:
            input_["alias"] = alias
        if asset_id is not None:
            input_["asset_id"] = asset_id
        if property_id is not None:
            input_["property_id"] = property_id
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_access_policy(
        self,
        access_policy_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "aws_sdk_iotsitewise.types.describe_access_policy_response.DescribeAccessPolicyResponse":
        """<p>Describes an access policy, which specifies an identity's access to an IoT SiteWise Monitor portal or project.</p>

        Args:
            access_policy_id: <p>The ID of the access policy.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.describe_access_policy_request.DescribeAccessPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.describe_access_policy_response.DescribeAccessPolicyResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_access_policy

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_access_policy.async_describe_access_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.describe_access_policy_request.DescribeAccessPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["access_policy_id"] = access_policy_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_action(
        self,
        action_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "aws_sdk_iotsitewise.types.describe_action_response.DescribeActionResponse":
        """<p>Retrieves information about an action.</p>

        Args:
            action_id: <p>The ID of the action.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.describe_action_request.DescribeActionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.describe_action_response.DescribeActionResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_action

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_action.async_describe_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.describe_action_request.DescribeActionRequest = {}  # type: ignore[typeddict-item]
        input_["action_id"] = action_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_asset(
        self,
        asset_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        exclude_properties: Optional[
            "aws_sdk_iotsitewise.types.exclude_properties.ExcludeProperties"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.describe_asset_response.DescribeAssetResponse":
        """<p>Retrieves information about an asset.</p>

        Args:
            asset_id: <p>The ID of the asset. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            exclude_properties: <p> Whether or not to exclude asset properties from the response. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.describe_asset_request.DescribeAssetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.describe_asset_response.DescribeAssetResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_asset

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_asset.async_describe_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.describe_asset_request.DescribeAssetRequest = {}  # type: ignore[typeddict-item]
        input_["asset_id"] = asset_id
        if exclude_properties is not None:
            input_["exclude_properties"] = exclude_properties

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def wait_asset_not_exists(
        self,
        asset_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        *,
        max_wait_time: float,
        min_delay: float = 3,
        max_delay: float = 120,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        exclude_properties: Optional[
            "aws_sdk_iotsitewise.types.exclude_properties.ExcludeProperties"
        ] = None,
    ) -> ServiceError:
        """Wait for asset_not_exists.

        Args:
            asset_id: <p>The ID of the asset. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            max_wait_time: Maximum total seconds to wait before raising WaiterTimeoutError.
            min_delay: Minimum seconds between operation attempts (spec default 2).
            max_delay: Maximum seconds between operation attempts (spec default 120).
            exclude_properties: <p> Whether or not to exclude asset properties from the response. </p>
        """
        start = time.monotonic()
        attempt = 0
        while True:
            op_output: "aws_sdk_iotsitewise.types.describe_asset_response.DescribeAssetResponse | None" = None
            op_error: ServiceError | None = None
            try:
                op_output = await self.describe_asset(  # noqa: F841
                    asset_id,
                    config_overrides=config_overrides,
                    exclude_properties=exclude_properties,
                )
            except ServiceError as e:
                op_error = e
            if op_error is not None and op_error.code == "ResourceNotFoundException":
                return op_error

            elapsed = time.monotonic() - start
            remaining = max_wait_time - elapsed
            if remaining <= 0:
                raise WaiterTimeoutError("asset_not_exists", max_wait_time)
            delay = min(max_delay, min_delay * (2**attempt))
            delay = min(delay, remaining)
            await anysleep(delay)
            attempt += 1

    async def describe_asset_composite_model(
        self,
        asset_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        asset_composite_model_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "aws_sdk_iotsitewise.types.describe_asset_composite_model_response.DescribeAssetCompositeModelResponse":
        """<p>Retrieves information about an asset composite model (also known as an asset component). An <code>AssetCompositeModel</code> is an instance of an <code>AssetModelCompositeModel</code>. If you want to see information about the model this is based on, call <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetModelCompositeModel.html\">DescribeAssetModelCompositeModel</a>.</p>

        Args:
            asset_id: <p>The ID of the asset. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            asset_composite_model_id: <p>The ID of a composite model on this asset. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.describe_asset_composite_model_request.DescribeAssetCompositeModelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.describe_asset_composite_model_response.DescribeAssetCompositeModelResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_asset_composite_model

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_asset_composite_model.async_describe_asset_composite_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.describe_asset_composite_model_request.DescribeAssetCompositeModelRequest = {}  # type: ignore[typeddict-item]
        input_["asset_id"] = asset_id
        input_["asset_composite_model_id"] = asset_composite_model_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_asset_model(
        self,
        asset_model_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        exclude_properties: Optional[
            "aws_sdk_iotsitewise.types.exclude_properties.ExcludeProperties"
        ] = None,
        asset_model_version: Optional[
            "aws_sdk_iotsitewise.types.asset_model_version_filter.AssetModelVersionFilter"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.describe_asset_model_response.DescribeAssetModelResponse":
        """<p>Retrieves information about an asset model. This includes details about the asset model's properties, hierarchies, composite models, and any interface relationships if the asset model implements interfaces.</p>

        Args:
            asset_model_id: <p>The ID of the asset model. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            exclude_properties: <p> Whether or not to exclude asset model properties from the response. </p>
            asset_model_version: <p>The version alias that specifies the latest or active version of the asset model. The details are returned in the response. The default value is <code>LATEST</code>. See <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/model-active-version.html\"> Asset model versions</a> in the <i>IoT SiteWise User Guide</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.describe_asset_model_request.DescribeAssetModelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.describe_asset_model_response.DescribeAssetModelResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_asset_model

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_asset_model.async_describe_asset_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.describe_asset_model_request.DescribeAssetModelRequest = {}  # type: ignore[typeddict-item]
        input_["asset_model_id"] = asset_model_id
        if exclude_properties is not None:
            input_["exclude_properties"] = exclude_properties
        if asset_model_version is not None:
            input_["asset_model_version"] = asset_model_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def wait_asset_model_not_exists(
        self,
        asset_model_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        *,
        max_wait_time: float,
        min_delay: float = 3,
        max_delay: float = 120,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        exclude_properties: Optional[
            "aws_sdk_iotsitewise.types.exclude_properties.ExcludeProperties"
        ] = None,
        asset_model_version: Optional[
            "aws_sdk_iotsitewise.types.asset_model_version_filter.AssetModelVersionFilter"
        ] = None,
    ) -> ServiceError:
        """Wait for asset_model_not_exists.

        Args:
            asset_model_id: <p>The ID of the asset model. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            max_wait_time: Maximum total seconds to wait before raising WaiterTimeoutError.
            min_delay: Minimum seconds between operation attempts (spec default 2).
            max_delay: Maximum seconds between operation attempts (spec default 120).
            exclude_properties: <p> Whether or not to exclude asset model properties from the response. </p>
            asset_model_version: <p>The version alias that specifies the latest or active version of the asset model. The details are returned in the response. The default value is <code>LATEST</code>. See <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/model-active-version.html\"> Asset model versions</a> in the <i>IoT SiteWise User Guide</i>.</p>
        """
        start = time.monotonic()
        attempt = 0
        while True:
            op_output: "aws_sdk_iotsitewise.types.describe_asset_model_response.DescribeAssetModelResponse | None" = None
            op_error: ServiceError | None = None
            try:
                op_output = await self.describe_asset_model(  # noqa: F841
                    asset_model_id,
                    config_overrides=config_overrides,
                    exclude_properties=exclude_properties,
                    asset_model_version=asset_model_version,
                )
            except ServiceError as e:
                op_error = e
            if op_error is not None and op_error.code == "ResourceNotFoundException":
                return op_error

            elapsed = time.monotonic() - start
            remaining = max_wait_time - elapsed
            if remaining <= 0:
                raise WaiterTimeoutError("asset_model_not_exists", max_wait_time)
            delay = min(max_delay, min_delay * (2**attempt))
            delay = min(delay, remaining)
            await anysleep(delay)
            attempt += 1

    async def describe_asset_model_composite_model(
        self,
        asset_model_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        asset_model_composite_model_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_model_version: Optional[
            "aws_sdk_iotsitewise.types.asset_model_version_filter.AssetModelVersionFilter"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.describe_asset_model_composite_model_response.DescribeAssetModelCompositeModelResponse":
        """<p>Retrieves information about an asset model composite model (also known as an asset model component). For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/custom-composite-models.html\">Custom composite models (Components)</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Args:
            asset_model_id: <p>The ID of the asset model. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            asset_model_composite_model_id: <p>The ID of a composite model on this asset model. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            asset_model_version: <p>The version alias that specifies the latest or active version of the asset model. The details are returned in the response. The default value is <code>LATEST</code>. See <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/model-active-version.html\"> Asset model versions</a> in the <i>IoT SiteWise User Guide</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.describe_asset_model_composite_model_request.DescribeAssetModelCompositeModelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.describe_asset_model_composite_model_response.DescribeAssetModelCompositeModelResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_asset_model_composite_model

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_asset_model_composite_model.async_describe_asset_model_composite_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.describe_asset_model_composite_model_request.DescribeAssetModelCompositeModelRequest = {}  # type: ignore[typeddict-item]
        input_["asset_model_id"] = asset_model_id
        input_["asset_model_composite_model_id"] = asset_model_composite_model_id
        if asset_model_version is not None:
            input_["asset_model_version"] = asset_model_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_asset_model_interface_relationship(
        self,
        asset_model_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        interface_asset_model_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "aws_sdk_iotsitewise.types.describe_asset_model_interface_relationship_response.DescribeAssetModelInterfaceRelationshipResponse":
        """<p>Retrieves information about an interface relationship between an asset model and an interface asset model.</p>

        Args:
            asset_model_id: <p>The ID of the asset model. This can be either the actual ID in UUID format, or else externalId: followed by the external ID.</p>
            interface_asset_model_id: <p>The ID of the interface asset model. This can be either the actual ID in UUID format, or else externalId: followed by the external ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.describe_asset_model_interface_relationship_request.DescribeAssetModelInterfaceRelationshipRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.describe_asset_model_interface_relationship_response.DescribeAssetModelInterfaceRelationshipResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_asset_model_interface_relationship

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_asset_model_interface_relationship.async_describe_asset_model_interface_relationship(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.describe_asset_model_interface_relationship_request.DescribeAssetModelInterfaceRelationshipRequest = {}  # type: ignore[typeddict-item]
        input_["asset_model_id"] = asset_model_id
        input_["interface_asset_model_id"] = interface_asset_model_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_asset_property(
        self,
        asset_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        property_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "aws_sdk_iotsitewise.types.describe_asset_property_response.DescribeAssetPropertyResponse":
        """<p>Retrieves information about an asset property.</p> <note> <p>When you call this operation for an attribute property, this response includes the default attribute value that you define in the asset model. If you update the default value in the model, this operation's response includes the new default value.</p> </note> <p>This operation doesn't return the value of the asset property. To get the value of an asset property, use <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GetAssetPropertyValue.html\">GetAssetPropertyValue</a>.</p>

        Args:
            asset_id: <p>The ID of the asset. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            property_id: <p>The ID of the asset property. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.describe_asset_property_request.DescribeAssetPropertyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.describe_asset_property_response.DescribeAssetPropertyResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_asset_property

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_asset_property.async_describe_asset_property(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.describe_asset_property_request.DescribeAssetPropertyRequest = {}  # type: ignore[typeddict-item]
        input_["asset_id"] = asset_id
        input_["property_id"] = property_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_bulk_import_job(
        self,
        job_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "aws_sdk_iotsitewise.types.describe_bulk_import_job_response.DescribeBulkImportJobResponse":
        """<p>Retrieves information about a bulk import job request. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/DescribeBulkImportJob.html\">Describe a bulk import job (CLI)</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p>

        Args:
            job_id: <p>The ID of the job.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.describe_bulk_import_job_request.DescribeBulkImportJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.describe_bulk_import_job_response.DescribeBulkImportJobResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_bulk_import_job

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_bulk_import_job.async_describe_bulk_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.describe_bulk_import_job_request.DescribeBulkImportJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_computation_model(
        self,
        computation_model_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        computation_model_version: Optional[
            "aws_sdk_iotsitewise.types.computation_model_version_filter.ComputationModelVersionFilter"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.describe_computation_model_response.DescribeComputationModelResponse":
        """<p>Retrieves information about a computation model.</p>

        Args:
            computation_model_id: <p>The ID of the computation model.</p>
            computation_model_version: <p>The version of the computation model.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.describe_computation_model_request.DescribeComputationModelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.describe_computation_model_response.DescribeComputationModelResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_computation_model

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_computation_model.async_describe_computation_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.describe_computation_model_request.DescribeComputationModelRequest = {}  # type: ignore[typeddict-item]
        input_["computation_model_id"] = computation_model_id
        if computation_model_version is not None:
            input_["computation_model_version"] = computation_model_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_computation_model_execution_summary(
        self,
        computation_model_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        resolve_to_resource_type: Optional[
            "aws_sdk_iotsitewise.types.resolve_to_resource_type.ResolveToResourceType"
        ] = None,
        resolve_to_resource_id: Optional["aws_sdk_iotsitewise.types.id.ID"] = None,
    ) -> "aws_sdk_iotsitewise.types.describe_computation_model_execution_summary_response.DescribeComputationModelExecutionSummaryResponse":
        """<p>Retrieves information about the execution summary of a computation model.</p>

        Args:
            computation_model_id: <p>The ID of the computation model.</p>
            resolve_to_resource_type: <p>The type of the resolved resource.</p>
            resolve_to_resource_id: <p>The ID of the resolved resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.describe_computation_model_execution_summary_request.DescribeComputationModelExecutionSummaryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.describe_computation_model_execution_summary_response.DescribeComputationModelExecutionSummaryResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_computation_model_execution_summary

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_computation_model_execution_summary.async_describe_computation_model_execution_summary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.describe_computation_model_execution_summary_request.DescribeComputationModelExecutionSummaryRequest = {}  # type: ignore[typeddict-item]
        input_["computation_model_id"] = computation_model_id
        if resolve_to_resource_type is not None:
            input_["resolve_to_resource_type"] = resolve_to_resource_type
        if resolve_to_resource_id is not None:
            input_["resolve_to_resource_id"] = resolve_to_resource_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_dashboard(
        self,
        dashboard_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "aws_sdk_iotsitewise.types.describe_dashboard_response.DescribeDashboardResponse":
        """<p>Retrieves information about a dashboard.</p>

        Args:
            dashboard_id: <p>The ID of the dashboard.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.describe_dashboard_request.DescribeDashboardRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.describe_dashboard_response.DescribeDashboardResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_dashboard

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_dashboard.async_describe_dashboard(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.describe_dashboard_request.DescribeDashboardRequest = {}  # type: ignore[typeddict-item]
        input_["dashboard_id"] = dashboard_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_dataset(
        self,
        dataset_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "aws_sdk_iotsitewise.types.describe_dataset_response.DescribeDatasetResponse":
        """<p>Retrieves information about a dataset.</p>

        Args:
            dataset_id: <p>The ID of the dataset.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.describe_dataset_request.DescribeDatasetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.describe_dataset_response.DescribeDatasetResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_dataset

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_dataset.async_describe_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.describe_dataset_request.DescribeDatasetRequest = {}  # type: ignore[typeddict-item]
        input_["dataset_id"] = dataset_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_default_encryption_configuration(
        self, *, config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None
    ) -> "aws_sdk_iotsitewise.types.describe_default_encryption_configuration_response.DescribeDefaultEncryptionConfigurationResponse":
        """<p>Retrieves information about the default encryption configuration for the Amazon Web Services account in the default or specified Region. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/key-management.html\">Key management</a> in the <i>IoT SiteWise User Guide</i>.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.describe_default_encryption_configuration_request.DescribeDefaultEncryptionConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.describe_default_encryption_configuration_response.DescribeDefaultEncryptionConfigurationResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_default_encryption_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_default_encryption_configuration.async_describe_default_encryption_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.describe_default_encryption_configuration_request.DescribeDefaultEncryptionConfigurationRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_execution(
        self,
        execution_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "aws_sdk_iotsitewise.types.describe_execution_response.DescribeExecutionResponse":
        """<p>Retrieves information about the execution.</p>

        Args:
            execution_id: <p>The ID of the execution.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.describe_execution_request.DescribeExecutionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.describe_execution_response.DescribeExecutionResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_execution

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_execution.async_describe_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.describe_execution_request.DescribeExecutionRequest = {}  # type: ignore[typeddict-item]
        input_["execution_id"] = execution_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_gateway(
        self,
        gateway_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "aws_sdk_iotsitewise.types.describe_gateway_response.DescribeGatewayResponse":
        """<p>Retrieves information about a gateway.</p>

        Args:
            gateway_id: <p>The ID of the gateway device.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.describe_gateway_request.DescribeGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.describe_gateway_response.DescribeGatewayResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_gateway.async_describe_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.describe_gateway_request.DescribeGatewayRequest = {}  # type: ignore[typeddict-item]
        input_["gateway_id"] = gateway_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_gateway_capability_configuration(
        self,
        gateway_id: "aws_sdk_iotsitewise.types.id.ID",
        capability_namespace: "aws_sdk_iotsitewise.types.capability_namespace.CapabilityNamespace",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "aws_sdk_iotsitewise.types.describe_gateway_capability_configuration_response.DescribeGatewayCapabilityConfigurationResponse":
        """<p>Each gateway capability defines data sources for a gateway. This is the namespace of the gateway capability.</p> <p>. The namespace follows the format <code>service:capability:version</code>, where:</p> <ul> <li> <p> <code>service</code> - The service providing the capability, or <code>iotsitewise</code>.</p> </li> <li> <p> <code>capability</code> - The specific capability type. Options include: <code>opcuacollector</code> for the OPC UA data source collector, or <code>publisher</code> for data publisher capability.</p> </li> <li> <p> <code>version</code> - The version number of the capability. Option include <code>2</code> for Classic streams, V2 gateways, and <code>3</code> for MQTT-enabled, V3 gateways.</p> </li> </ul> <p>After updating a capability configuration, the sync status becomes <code>OUT_OF_SYNC</code> until the gateway processes the configuration.Use <code>DescribeGatewayCapabilityConfiguration</code> to check the sync status and verify the configuration was applied.</p> <p>A gateway can have multiple capability configurations with different namespaces.</p>

        Args:
            gateway_id: <p>The ID of the gateway that defines the capability configuration.</p>
            capability_namespace: <p>The namespace of the capability configuration. For example, if you configure OPC UA sources for an MQTT-enabled gateway, your OPC-UA capability configuration has the namespace <code>iotsitewise:opcuacollector:3</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.describe_gateway_capability_configuration_request.DescribeGatewayCapabilityConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.describe_gateway_capability_configuration_response.DescribeGatewayCapabilityConfigurationResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_gateway_capability_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_gateway_capability_configuration.async_describe_gateway_capability_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.describe_gateway_capability_configuration_request.DescribeGatewayCapabilityConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["gateway_id"] = gateway_id
        input_["capability_namespace"] = capability_namespace

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_logging_options(
        self, *, config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None
    ) -> "aws_sdk_iotsitewise.types.describe_logging_options_response.DescribeLoggingOptionsResponse":
        """<p>Retrieves the current IoT SiteWise logging options.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.describe_logging_options_request.DescribeLoggingOptionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.describe_logging_options_response.DescribeLoggingOptionsResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_logging_options

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_logging_options.async_describe_logging_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.describe_logging_options_request.DescribeLoggingOptionsRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_portal(
        self,
        portal_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "aws_sdk_iotsitewise.types.describe_portal_response.DescribePortalResponse":
        """<p>Retrieves information about a portal.</p>

        Args:
            portal_id: <p>The ID of the portal.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.describe_portal_request.DescribePortalRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.describe_portal_response.DescribePortalResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_portal

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_portal.async_describe_portal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.describe_portal_request.DescribePortalRequest = {}  # type: ignore[typeddict-item]
        input_["portal_id"] = portal_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def wait_portal_not_exists(
        self,
        portal_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        max_wait_time: float,
        min_delay: float = 3,
        max_delay: float = 120,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> ServiceError:
        """Wait for portal_not_exists.

        Args:
            portal_id: <p>The ID of the portal.</p>
            max_wait_time: Maximum total seconds to wait before raising WaiterTimeoutError.
            min_delay: Minimum seconds between operation attempts (spec default 2).
            max_delay: Maximum seconds between operation attempts (spec default 120).
        """
        start = time.monotonic()
        attempt = 0
        while True:
            op_output: "aws_sdk_iotsitewise.types.describe_portal_response.DescribePortalResponse | None" = None
            op_error: ServiceError | None = None
            try:
                op_output = await self.describe_portal(  # noqa: F841
                    portal_id, config_overrides=config_overrides
                )
            except ServiceError as e:
                op_error = e
            if op_error is not None and op_error.code == "ResourceNotFoundException":
                return op_error

            elapsed = time.monotonic() - start
            remaining = max_wait_time - elapsed
            if remaining <= 0:
                raise WaiterTimeoutError("portal_not_exists", max_wait_time)
            delay = min(max_delay, min_delay * (2**attempt))
            delay = min(delay, remaining)
            await anysleep(delay)
            attempt += 1

    async def describe_project(
        self,
        project_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "aws_sdk_iotsitewise.types.describe_project_response.DescribeProjectResponse":
        """<p>Retrieves information about a project.</p>

        Args:
            project_id: <p>The ID of the project.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.describe_project_request.DescribeProjectRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.describe_project_response.DescribeProjectResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_project

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_project.async_describe_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.describe_project_request.DescribeProjectRequest = {}  # type: ignore[typeddict-item]
        input_["project_id"] = project_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_storage_configuration(
        self, *, config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None
    ) -> "aws_sdk_iotsitewise.types.describe_storage_configuration_response.DescribeStorageConfigurationResponse":
        """<p>Retrieves information about the storage configuration for IoT SiteWise.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.describe_storage_configuration_request.DescribeStorageConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.describe_storage_configuration_response.DescribeStorageConfigurationResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_storage_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_storage_configuration.async_describe_storage_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.describe_storage_configuration_request.DescribeStorageConfigurationRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_time_series(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        alias: Optional[
            "aws_sdk_iotsitewise.types.property_alias.PropertyAlias"
        ] = None,
        asset_id: Optional["aws_sdk_iotsitewise.types.custom_id.CustomID"] = None,
        property_id: Optional["aws_sdk_iotsitewise.types.custom_id.CustomID"] = None,
    ) -> "aws_sdk_iotsitewise.types.describe_time_series_response.DescribeTimeSeriesResponse":
        """<p>Retrieves information about a time series (data stream).</p> <p>To identify a time series, do one of the following:</p> <ul> <li> <p>If the time series isn't associated with an asset property, specify the <code>alias</code> of the time series.</p> </li> <li> <p>If the time series is associated with an asset property, specify one of the following: </p> <ul> <li> <p>The <code>alias</code> of the time series.</p> </li> <li> <p>The <code>assetId</code> and <code>propertyId</code> that identifies the asset property.</p> </li> </ul> </li> </ul>

        Args:
            alias: <p>The alias that identifies the time series.</p>
            asset_id: <p>The ID of the asset in which the asset property was created. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            property_id: <p>The ID of the asset property. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.describe_time_series_request.DescribeTimeSeriesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.describe_time_series_response.DescribeTimeSeriesResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_time_series

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.describe_time_series.async_describe_time_series(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.describe_time_series_request.DescribeTimeSeriesRequest = {}  # type: ignore[typeddict-item]
        if alias is not None:
            input_["alias"] = alias
        if asset_id is not None:
            input_["asset_id"] = asset_id
        if property_id is not None:
            input_["property_id"] = property_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_assets(
        self,
        asset_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        hierarchy_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        child_asset_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> None:
        """<p>Disassociates a child asset from the given parent asset through a hierarchy defined in the parent asset's model.</p>

        Args:
            asset_id: <p>The ID of the parent asset from which to disassociate the child asset. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            hierarchy_id: <p>The ID of a hierarchy in the parent asset's model. (This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.) Hierarchies allow different groupings of assets to be formed that all come from the same asset model. You can use the hierarchy ID to identify the correct asset to disassociate. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html\">Asset hierarchies</a> in the <i>IoT SiteWise User Guide</i>.</p>
            child_asset_id: <p>The ID of the child asset to disassociate. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.disassociate_assets_request.DisassociateAssetsRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.disassociate_assets

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.disassociate_assets.async_disassociate_assets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.disassociate_assets_request.DisassociateAssetsRequest = {}  # type: ignore[typeddict-item]
        input_["asset_id"] = asset_id
        input_["hierarchy_id"] = hierarchy_id
        input_["child_asset_id"] = child_asset_id
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_time_series_from_asset_property(
        self,
        alias: "aws_sdk_iotsitewise.types.property_alias.PropertyAlias",
        asset_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        property_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> None:
        """<p>Disassociates a time series (data stream) from an asset property.</p>

        Args:
            alias: <p>The alias that identifies the time series.</p>
            asset_id: <p>The ID of the asset in which the asset property was created. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            property_id: <p>The ID of the asset property. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.disassociate_time_series_from_asset_property_request.DisassociateTimeSeriesFromAssetPropertyRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.disassociate_time_series_from_asset_property

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.disassociate_time_series_from_asset_property.async_disassociate_time_series_from_asset_property(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.disassociate_time_series_from_asset_property_request.DisassociateTimeSeriesFromAssetPropertyRequest = {}  # type: ignore[typeddict-item]
        input_["alias"] = alias
        input_["asset_id"] = asset_id
        input_["property_id"] = property_id
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def execute_action(
        self,
        target_resource: "aws_sdk_iotsitewise.types.target_resource.TargetResource",
        action_definition_id: "aws_sdk_iotsitewise.types.id.ID",
        action_payload: "aws_sdk_iotsitewise.types.action_payload.ActionPayload",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
        resolve_to: Optional["aws_sdk_iotsitewise.types.resolve_to.ResolveTo"] = None,
    ) -> "aws_sdk_iotsitewise.types.execute_action_response.ExecuteActionResponse":
        """<p>Executes an action on a target resource.</p>

        Args:
            target_resource: <p>The resource the action will be taken on.</p>
            action_definition_id: <p>The ID of the action definition.</p>
            action_payload: <p>The JSON payload of the action.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            resolve_to: <p>The detailed resource this action resolves to.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.execute_action_request.ExecuteActionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.execute_action_response.ExecuteActionResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.execute_action

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.execute_action.async_execute_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.execute_action_request.ExecuteActionRequest = {}  # type: ignore[typeddict-item]
        input_["target_resource"] = target_resource
        input_["action_definition_id"] = action_definition_id
        input_["action_payload"] = action_payload
        if client_token is not None:
            input_["client_token"] = client_token
        if resolve_to is not None:
            input_["resolve_to"] = resolve_to

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def execute_query(
        self,
        query_statement: "aws_sdk_iotsitewise.types.query_statement.QueryStatement",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional[
            "aws_sdk_iotsitewise.types.execute_query_next_token.ExecuteQueryNextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.execute_query_max_results.ExecuteQueryMaxResults"
        ] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.execute_query_response.ExecuteQueryResponse":
        """<p>Run SQL queries to retrieve metadata and time-series data from asset models, assets, measurements, metrics, transforms, and aggregates.</p>

        Args:
            query_statement: <p>The IoT SiteWise query statement.</p>
            next_token: <p>The string that specifies the next page of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p> <ul> <li> <p>Minimum is 1</p> </li> <li> <p>Maximum is 20000</p> </li> <li> <p>Default is 20000</p> </li> </ul>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.execute_query_request.ExecuteQueryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.execute_query_response.ExecuteQueryResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.execute_query

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.execute_query.async_execute_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.execute_query_request.ExecuteQueryRequest = {}  # type: ignore[typeddict-item]
        input_["query_statement"] = query_statement
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_execute_query(
        self,
        query_statement: "aws_sdk_iotsitewise.types.query_statement.QueryStatement",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional[
            "aws_sdk_iotsitewise.types.execute_query_next_token.ExecuteQueryNextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.execute_query_max_results.ExecuteQueryMaxResults"
        ] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_iotsitewise.types.row.Row]":
        _token = next_token
        while True:
            _response = await self.execute_query(
                query_statement,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                client_token=client_token,
            )
            _page = _resolve_path(_response, ("rows",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_asset_property_aggregates(
        self,
        aggregate_types: "aws_sdk_iotsitewise.types.aggregate_types.AggregateTypes",
        resolution: "aws_sdk_iotsitewise.types.resolution.Resolution",
        start_date: "aws_sdk_iotsitewise.types.timestamp.Timestamp",
        end_date: "aws_sdk_iotsitewise.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_id: Optional["aws_sdk_iotsitewise.types.id.ID"] = None,
        property_id: Optional["aws_sdk_iotsitewise.types.id.ID"] = None,
        property_alias: Optional[
            "aws_sdk_iotsitewise.types.asset_property_alias.AssetPropertyAlias"
        ] = None,
        qualities: Optional["aws_sdk_iotsitewise.types.qualities.Qualities"] = None,
        time_ordering: Optional[
            "aws_sdk_iotsitewise.types.time_ordering.TimeOrdering"
        ] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.get_asset_property_value_aggregates_max_results.GetAssetPropertyValueAggregatesMaxResults"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.get_asset_property_aggregates_response.GetAssetPropertyAggregatesResponse":
        """<p>Gets aggregated values for an asset property. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#aggregates\">Querying aggregates</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>To identify an asset property, you must specify one of the following:</p> <ul> <li> <p>The <code>assetId</code> and <code>propertyId</code> of an asset property.</p> </li> <li> <p>A <code>propertyAlias</code>, which is a data stream alias (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). To define an asset property's alias, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html\">UpdateAssetProperty</a>.</p> </li> </ul>

        Args:
            asset_id: <p>The ID of the asset, in UUID format.</p>
            property_id: <p>The ID of the asset property, in UUID format.</p>
            property_alias: <p>The alias that identifies the property, such as an OPC-UA server data stream path (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\">Mapping industrial data streams to asset properties</a> in the <i>IoT SiteWise User Guide</i>.</p>
            aggregate_types: <p>The data aggregating function.</p>
            resolution: <p>The time interval over which to aggregate data.</p>
            qualities: <p>The quality by which to filter asset data.</p>
            start_date: <p>The exclusive start of the range from which to query historical data, expressed in seconds in Unix epoch time.</p>
            end_date: <p>The inclusive end of the range from which to query historical data, expressed in seconds in Unix epoch time.</p>
            time_ordering: <p>The chronological sorting order of the requested information.</p> <p>Default: <code>ASCENDING</code> </p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request. A result set is returned in the two cases, whichever occurs first.</p> <ul> <li> <p>The size of the result set is equal to 1 MB.</p> </li> <li> <p>The number of data points in the result set is equal to the value of <code>maxResults</code>. The maximum value of <code>maxResults</code> is 2500.</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.get_asset_property_aggregates_request.GetAssetPropertyAggregatesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.get_asset_property_aggregates_response.GetAssetPropertyAggregatesResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.get_asset_property_aggregates

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.get_asset_property_aggregates.async_get_asset_property_aggregates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.get_asset_property_aggregates_request.GetAssetPropertyAggregatesRequest = {}  # type: ignore[typeddict-item]
        if asset_id is not None:
            input_["asset_id"] = asset_id
        if property_id is not None:
            input_["property_id"] = property_id
        if property_alias is not None:
            input_["property_alias"] = property_alias
        input_["aggregate_types"] = aggregate_types
        input_["resolution"] = resolution
        if qualities is not None:
            input_["qualities"] = qualities
        input_["start_date"] = start_date
        input_["end_date"] = end_date
        if time_ordering is not None:
            input_["time_ordering"] = time_ordering
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_get_asset_property_aggregates(
        self,
        aggregate_types: "aws_sdk_iotsitewise.types.aggregate_types.AggregateTypes",
        resolution: "aws_sdk_iotsitewise.types.resolution.Resolution",
        start_date: "aws_sdk_iotsitewise.types.timestamp.Timestamp",
        end_date: "aws_sdk_iotsitewise.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_id: Optional["aws_sdk_iotsitewise.types.id.ID"] = None,
        property_id: Optional["aws_sdk_iotsitewise.types.id.ID"] = None,
        property_alias: Optional[
            "aws_sdk_iotsitewise.types.asset_property_alias.AssetPropertyAlias"
        ] = None,
        qualities: Optional["aws_sdk_iotsitewise.types.qualities.Qualities"] = None,
        time_ordering: Optional[
            "aws_sdk_iotsitewise.types.time_ordering.TimeOrdering"
        ] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.get_asset_property_value_aggregates_max_results.GetAssetPropertyValueAggregatesMaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_iotsitewise.types.aggregated_value.AggregatedValue]":
        _token = next_token
        while True:
            _response = await self.get_asset_property_aggregates(
                aggregate_types,
                resolution,
                start_date,
                end_date,
                config_overrides=config_overrides,
                asset_id=asset_id,
                property_id=property_id,
                property_alias=property_alias,
                qualities=qualities,
                time_ordering=time_ordering,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("aggregated_values",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_asset_property_value(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_id: Optional["aws_sdk_iotsitewise.types.id.ID"] = None,
        property_id: Optional["aws_sdk_iotsitewise.types.id.ID"] = None,
        property_alias: Optional[
            "aws_sdk_iotsitewise.types.asset_property_alias.AssetPropertyAlias"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.get_asset_property_value_response.GetAssetPropertyValueResponse":
        """<p>Gets an asset property's current value. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#current-values\">Querying current values</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>To identify an asset property, you must specify one of the following:</p> <ul> <li> <p>The <code>assetId</code> and <code>propertyId</code> of an asset property.</p> </li> <li> <p>A <code>propertyAlias</code>, which is a data stream alias (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). To define an asset property's alias, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html\">UpdateAssetProperty</a>.</p> </li> </ul>

        Args:
            asset_id: <p>The ID of the asset, in UUID format.</p>
            property_id: <p>The ID of the asset property, in UUID format.</p>
            property_alias: <p>The alias that identifies the property, such as an OPC-UA server data stream path (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\">Mapping industrial data streams to asset properties</a> in the <i>IoT SiteWise User Guide</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.get_asset_property_value_request.GetAssetPropertyValueRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.get_asset_property_value_response.GetAssetPropertyValueResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.get_asset_property_value

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.get_asset_property_value.async_get_asset_property_value(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.get_asset_property_value_request.GetAssetPropertyValueRequest = {}  # type: ignore[typeddict-item]
        if asset_id is not None:
            input_["asset_id"] = asset_id
        if property_id is not None:
            input_["property_id"] = property_id
        if property_alias is not None:
            input_["property_alias"] = property_alias

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_asset_property_value_history(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_id: Optional["aws_sdk_iotsitewise.types.id.ID"] = None,
        property_id: Optional["aws_sdk_iotsitewise.types.id.ID"] = None,
        property_alias: Optional[
            "aws_sdk_iotsitewise.types.asset_property_alias.AssetPropertyAlias"
        ] = None,
        start_date: Optional["aws_sdk_iotsitewise.types.timestamp.Timestamp"] = None,
        end_date: Optional["aws_sdk_iotsitewise.types.timestamp.Timestamp"] = None,
        qualities: Optional["aws_sdk_iotsitewise.types.qualities.Qualities"] = None,
        time_ordering: Optional[
            "aws_sdk_iotsitewise.types.time_ordering.TimeOrdering"
        ] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.get_asset_property_value_history_max_results.GetAssetPropertyValueHistoryMaxResults"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.get_asset_property_value_history_response.GetAssetPropertyValueHistoryResponse":
        """<p>Gets the history of an asset property's values. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#historical-values\">Querying historical values</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>To identify an asset property, you must specify one of the following:</p> <ul> <li> <p>The <code>assetId</code> and <code>propertyId</code> of an asset property.</p> </li> <li> <p>A <code>propertyAlias</code>, which is a data stream alias (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). To define an asset property's alias, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html\">UpdateAssetProperty</a>.</p> </li> </ul>

        Args:
            asset_id: <p>The ID of the asset, in UUID format.</p>
            property_id: <p>The ID of the asset property, in UUID format.</p>
            property_alias: <p>The alias that identifies the property, such as an OPC-UA server data stream path (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\">Mapping industrial data streams to asset properties</a> in the <i>IoT SiteWise User Guide</i>.</p>
            start_date: <p>The exclusive start of the range from which to query historical data, expressed in seconds in Unix epoch time.</p>
            end_date: <p>The inclusive end of the range from which to query historical data, expressed in seconds in Unix epoch time.</p>
            qualities: <p>The quality by which to filter asset data.</p>
            time_ordering: <p>The chronological sorting order of the requested information.</p> <p>Default: <code>ASCENDING</code> </p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request. A result set is returned in the two cases, whichever occurs first.</p> <ul> <li> <p>The size of the result set is equal to 4 MB.</p> </li> <li> <p>The number of data points in the result set is equal to the value of <code>maxResults</code>. The maximum value of <code>maxResults</code> is 20000.</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.get_asset_property_value_history_request.GetAssetPropertyValueHistoryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.get_asset_property_value_history_response.GetAssetPropertyValueHistoryResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.get_asset_property_value_history

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.get_asset_property_value_history.async_get_asset_property_value_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.get_asset_property_value_history_request.GetAssetPropertyValueHistoryRequest = {}  # type: ignore[typeddict-item]
        if asset_id is not None:
            input_["asset_id"] = asset_id
        if property_id is not None:
            input_["property_id"] = property_id
        if property_alias is not None:
            input_["property_alias"] = property_alias
        if start_date is not None:
            input_["start_date"] = start_date
        if end_date is not None:
            input_["end_date"] = end_date
        if qualities is not None:
            input_["qualities"] = qualities
        if time_ordering is not None:
            input_["time_ordering"] = time_ordering
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_get_asset_property_value_history(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_id: Optional["aws_sdk_iotsitewise.types.id.ID"] = None,
        property_id: Optional["aws_sdk_iotsitewise.types.id.ID"] = None,
        property_alias: Optional[
            "aws_sdk_iotsitewise.types.asset_property_alias.AssetPropertyAlias"
        ] = None,
        start_date: Optional["aws_sdk_iotsitewise.types.timestamp.Timestamp"] = None,
        end_date: Optional["aws_sdk_iotsitewise.types.timestamp.Timestamp"] = None,
        qualities: Optional["aws_sdk_iotsitewise.types.qualities.Qualities"] = None,
        time_ordering: Optional[
            "aws_sdk_iotsitewise.types.time_ordering.TimeOrdering"
        ] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.get_asset_property_value_history_max_results.GetAssetPropertyValueHistoryMaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_iotsitewise.types.asset_property_value.AssetPropertyValue]":
        _token = next_token
        while True:
            _response = await self.get_asset_property_value_history(
                config_overrides=config_overrides,
                asset_id=asset_id,
                property_id=property_id,
                property_alias=property_alias,
                start_date=start_date,
                end_date=end_date,
                qualities=qualities,
                time_ordering=time_ordering,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("asset_property_value_history",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_interpolated_asset_property_values(
        self,
        start_time_in_seconds: "aws_sdk_iotsitewise.types.time_in_seconds.TimeInSeconds",
        end_time_in_seconds: "aws_sdk_iotsitewise.types.time_in_seconds.TimeInSeconds",
        quality: "aws_sdk_iotsitewise.types.quality.Quality",
        interval_in_seconds: "aws_sdk_iotsitewise.types.interval_in_seconds.IntervalInSeconds",
        type: "aws_sdk_iotsitewise.types.interpolation_type.InterpolationType",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_id: Optional["aws_sdk_iotsitewise.types.id.ID"] = None,
        property_id: Optional["aws_sdk_iotsitewise.types.id.ID"] = None,
        property_alias: Optional[
            "aws_sdk_iotsitewise.types.asset_property_alias.AssetPropertyAlias"
        ] = None,
        start_time_offset_in_nanos: Optional[
            "aws_sdk_iotsitewise.types.offset_in_nanos.OffsetInNanos"
        ] = None,
        end_time_offset_in_nanos: Optional[
            "aws_sdk_iotsitewise.types.offset_in_nanos.OffsetInNanos"
        ] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_interpolated_results.MaxInterpolatedResults"
        ] = None,
        interval_window_in_seconds: Optional[
            "aws_sdk_iotsitewise.types.interval_window_in_seconds.IntervalWindowInSeconds"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.get_interpolated_asset_property_values_response.GetInterpolatedAssetPropertyValuesResponse":
        """<p>Get interpolated values for an asset property for a specified time interval, during a period of time. If your time series is missing data points during the specified time interval, you can use interpolation to estimate the missing data.</p> <p>For example, you can use this operation to return the interpolated temperature values for a wind turbine every 24 hours over a duration of 7 days.</p> <p>To identify an asset property, you must specify one of the following:</p> <ul> <li> <p>The <code>assetId</code> and <code>propertyId</code> of an asset property.</p> </li> <li> <p>A <code>propertyAlias</code>, which is a data stream alias (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). To define an asset property's alias, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html\">UpdateAssetProperty</a>.</p> </li> </ul>

        Args:
            asset_id: <p>The ID of the asset, in UUID format.</p>
            property_id: <p>The ID of the asset property, in UUID format.</p>
            property_alias: <p>The alias that identifies the property, such as an OPC-UA server data stream path (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\">Mapping industrial data streams to asset properties</a> in the <i>IoT SiteWise User Guide</i>.</p>
            start_time_in_seconds: <p>The exclusive start of the range from which to interpolate data, expressed in seconds in Unix epoch time.</p>
            start_time_offset_in_nanos: <p>The nanosecond offset converted from <code>startTimeInSeconds</code>.</p>
            end_time_in_seconds: <p>The inclusive end of the range from which to interpolate data, expressed in seconds in Unix epoch time.</p>
            end_time_offset_in_nanos: <p>The nanosecond offset converted from <code>endTimeInSeconds</code>.</p>
            quality: <p>The quality of the asset property value. You can use this parameter as a filter to choose only the asset property values that have a specific quality.</p>
            interval_in_seconds: <p>The time interval in seconds over which to interpolate data. Each interval starts when the previous one ends.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request. If not specified, the default value is 10.</p>
            type: <p>The interpolation type.</p> <p>Valid values: <code>LINEAR_INTERPOLATION | LOCF_INTERPOLATION</code> </p> <ul> <li> <p> <code>LINEAR_INTERPOLATION</code> – Estimates missing data using <a href=\"https://en.wikipedia.org/wiki/Linear_interpolation\">linear interpolation</a>.</p> <p>For example, you can use this operation to return the interpolated temperature values for a wind turbine every 24 hours over a duration of 7 days. If the interpolation starts July 1, 2021, at 9 AM, IoT SiteWise returns the first interpolated value on July 2, 2021, at 9 AM, the second interpolated value on July 3, 2021, at 9 AM, and so on.</p> </li> <li> <p> <code>LOCF_INTERPOLATION</code> – Estimates missing data using last observation carried forward interpolation</p> <p>If no data point is found for an interval, IoT SiteWise returns the last observed data point for the previous interval and carries forward this interpolated value until a new data point is found.</p> <p>For example, you can get the state of an on-off valve every 24 hours over a duration of 7 days. If the interpolation starts July 1, 2021, at 9 AM, IoT SiteWise returns the last observed data point between July 1, 2021, at 9 AM and July 2, 2021, at 9 AM as the first interpolated value. If a data point isn't found after 9 AM on July 2, 2021, IoT SiteWise uses the same interpolated value for the rest of the days.</p> </li> </ul>
            interval_window_in_seconds: <p>The query interval for the window, in seconds. IoT SiteWise computes each interpolated value by using data points from the timestamp of each interval, minus the window to the timestamp of each interval plus the window. If not specified, the window ranges between the start time minus the interval and the end time plus the interval.</p> <note> <ul> <li> <p>If you specify a value for the <code>intervalWindowInSeconds</code> parameter, the value for the <code>type</code> parameter must be <code>LINEAR_INTERPOLATION</code>.</p> </li> <li> <p>If a data point isn't found during the specified query window, IoT SiteWise won't return an interpolated value for the interval. This indicates that there's a gap in the ingested data points.</p> </li> </ul> </note> <p>For example, you can get the interpolated temperature values for a wind turbine every 24 hours over a duration of 7 days. If the interpolation starts on July 1, 2021, at 9 AM with a window of 2 hours, IoT SiteWise uses the data points from 7 AM (9 AM minus 2 hours) to 11 AM (9 AM plus 2 hours) on July 2, 2021 to compute the first interpolated value. Next, IoT SiteWise uses the data points from 7 AM (9 AM minus 2 hours) to 11 AM (9 AM plus 2 hours) on July 3, 2021 to compute the second interpolated value, and so on. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.get_interpolated_asset_property_values_request.GetInterpolatedAssetPropertyValuesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.get_interpolated_asset_property_values_response.GetInterpolatedAssetPropertyValuesResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.get_interpolated_asset_property_values

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.get_interpolated_asset_property_values.async_get_interpolated_asset_property_values(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.get_interpolated_asset_property_values_request.GetInterpolatedAssetPropertyValuesRequest = {}  # type: ignore[typeddict-item]
        if asset_id is not None:
            input_["asset_id"] = asset_id
        if property_id is not None:
            input_["property_id"] = property_id
        if property_alias is not None:
            input_["property_alias"] = property_alias
        input_["start_time_in_seconds"] = start_time_in_seconds
        if start_time_offset_in_nanos is not None:
            input_["start_time_offset_in_nanos"] = start_time_offset_in_nanos
        input_["end_time_in_seconds"] = end_time_in_seconds
        if end_time_offset_in_nanos is not None:
            input_["end_time_offset_in_nanos"] = end_time_offset_in_nanos
        input_["quality"] = quality
        input_["interval_in_seconds"] = interval_in_seconds
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        input_["type"] = type
        if interval_window_in_seconds is not None:
            input_["interval_window_in_seconds"] = interval_window_in_seconds

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_get_interpolated_asset_property_values(
        self,
        start_time_in_seconds: "aws_sdk_iotsitewise.types.time_in_seconds.TimeInSeconds",
        end_time_in_seconds: "aws_sdk_iotsitewise.types.time_in_seconds.TimeInSeconds",
        quality: "aws_sdk_iotsitewise.types.quality.Quality",
        interval_in_seconds: "aws_sdk_iotsitewise.types.interval_in_seconds.IntervalInSeconds",
        type: "aws_sdk_iotsitewise.types.interpolation_type.InterpolationType",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_id: Optional["aws_sdk_iotsitewise.types.id.ID"] = None,
        property_id: Optional["aws_sdk_iotsitewise.types.id.ID"] = None,
        property_alias: Optional[
            "aws_sdk_iotsitewise.types.asset_property_alias.AssetPropertyAlias"
        ] = None,
        start_time_offset_in_nanos: Optional[
            "aws_sdk_iotsitewise.types.offset_in_nanos.OffsetInNanos"
        ] = None,
        end_time_offset_in_nanos: Optional[
            "aws_sdk_iotsitewise.types.offset_in_nanos.OffsetInNanos"
        ] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_interpolated_results.MaxInterpolatedResults"
        ] = None,
        interval_window_in_seconds: Optional[
            "aws_sdk_iotsitewise.types.interval_window_in_seconds.IntervalWindowInSeconds"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_iotsitewise.types.interpolated_asset_property_value.InterpolatedAssetPropertyValue]":
        _token = next_token
        while True:
            _response = await self.get_interpolated_asset_property_values(
                start_time_in_seconds,
                end_time_in_seconds,
                quality,
                interval_in_seconds,
                type,
                config_overrides=config_overrides,
                asset_id=asset_id,
                property_id=property_id,
                property_alias=property_alias,
                start_time_offset_in_nanos=start_time_offset_in_nanos,
                end_time_offset_in_nanos=end_time_offset_in_nanos,
                next_token=_token,
                max_results=max_results,
                interval_window_in_seconds=interval_window_in_seconds,
            )
            _page = _resolve_path(_response, ("interpolated_asset_property_values",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def invoke_assistant(
        self,
        message: "aws_sdk_iotsitewise.types.message_input.MessageInput",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        conversation_id: Optional[
            "aws_sdk_iotsitewise.types.conversation_id.ConversationId"
        ] = None,
        enable_trace: Optional[bool] = None,
    ) -> "aws_sdk_iotsitewise.types.invoke_assistant_response.InvokeAssistantResponse":
        """<p>Invokes SiteWise Assistant to start or continue a conversation.</p>

        Args:
            conversation_id: <p>The ID assigned to a conversation. IoT SiteWise automatically generates a unique ID for you, and this parameter is never required. However, if you prefer to have your own ID, you must specify it here in UUID format. If you specify your own ID, it must be globally unique.</p>
            message: <p>A text message sent to the SiteWise Assistant by the user.</p>
            enable_trace: <p>Specifies if to turn trace on or not. It is used to track the SiteWise Assistant's reasoning, and data access process.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.invoke_assistant_request.InvokeAssistantRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.invoke_assistant_response.InvokeAssistantResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.invoke_assistant

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.invoke_assistant.async_invoke_assistant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.invoke_assistant_request.InvokeAssistantRequest = {}  # type: ignore[typeddict-item]
        if conversation_id is not None:
            input_["conversation_id"] = conversation_id
        input_["message"] = message
        if enable_trace is not None:
            input_["enable_trace"] = enable_trace

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_access_policies(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        identity_type: Optional[
            "aws_sdk_iotsitewise.types.identity_type.IdentityType"
        ] = None,
        identity_id: Optional[
            "aws_sdk_iotsitewise.types.identity_id.IdentityId"
        ] = None,
        resource_type: Optional[
            "aws_sdk_iotsitewise.types.resource_type.ResourceType"
        ] = None,
        resource_id: Optional["aws_sdk_iotsitewise.types.id.ID"] = None,
        iam_arn: Optional["aws_sdk_iotsitewise.types.iam_arn.IamArn"] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.list_access_policies_response.ListAccessPoliciesResponse":
        """<p>Retrieves a paginated list of access policies for an identity (an IAM Identity Center user, an IAM Identity Center group, or an IAM user) or an IoT SiteWise Monitor resource (a portal or project).</p>

        Args:
            identity_type: <p>The type of identity (IAM Identity Center user, IAM Identity Center group, or IAM user). This parameter is required if you specify <code>identityId</code>.</p>
            identity_id: <p>The ID of the identity. This parameter is required if you specify <code>USER</code> or <code>GROUP</code> for <code>identityType</code>.</p>
            resource_type: <p>The type of resource (portal or project). This parameter is required if you specify <code>resourceId</code>.</p>
            resource_id: <p>The ID of the resource. This parameter is required if you specify <code>resourceType</code>.</p>
            iam_arn: <p>The ARN of the IAM user. For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html\">IAM ARNs</a> in the <i>IAM User Guide</i>. This parameter is required if you specify <code>IAM</code> for <code>identityType</code>.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.list_access_policies_request.ListAccessPoliciesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.list_access_policies_response.ListAccessPoliciesResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_access_policies

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_access_policies.async_list_access_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.list_access_policies_request.ListAccessPoliciesRequest = {}  # type: ignore[typeddict-item]
        if identity_type is not None:
            input_["identity_type"] = identity_type
        if identity_id is not None:
            input_["identity_id"] = identity_id
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if resource_id is not None:
            input_["resource_id"] = resource_id
        if iam_arn is not None:
            input_["iam_arn"] = iam_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_access_policies(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        identity_type: Optional[
            "aws_sdk_iotsitewise.types.identity_type.IdentityType"
        ] = None,
        identity_id: Optional[
            "aws_sdk_iotsitewise.types.identity_id.IdentityId"
        ] = None,
        resource_type: Optional[
            "aws_sdk_iotsitewise.types.resource_type.ResourceType"
        ] = None,
        resource_id: Optional["aws_sdk_iotsitewise.types.id.ID"] = None,
        iam_arn: Optional["aws_sdk_iotsitewise.types.iam_arn.IamArn"] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_iotsitewise.types.access_policy_summary.AccessPolicySummary]":
        _token = next_token
        while True:
            _response = await self.list_access_policies(
                config_overrides=config_overrides,
                identity_type=identity_type,
                identity_id=identity_id,
                resource_type=resource_type,
                resource_id=resource_id,
                iam_arn=iam_arn,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("access_policy_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_actions(
        self,
        target_resource_type: "aws_sdk_iotsitewise.types.target_resource_type.TargetResourceType",
        target_resource_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
        resolve_to_resource_type: Optional[
            "aws_sdk_iotsitewise.types.resolve_to_resource_type.ResolveToResourceType"
        ] = None,
        resolve_to_resource_id: Optional["aws_sdk_iotsitewise.types.id.ID"] = None,
    ) -> "aws_sdk_iotsitewise.types.list_actions_response.ListActionsResponse":
        """<p>Retrieves a paginated list of actions for a specific target resource.</p>

        Args:
            target_resource_type: <p>The type of resource.</p>
            target_resource_id: <p>The ID of the target resource.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p>
            resolve_to_resource_type: <p>The type of the resolved resource.</p>
            resolve_to_resource_id: <p>The ID of the resolved resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.list_actions_request.ListActionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.list_actions_response.ListActionsResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_actions

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_actions.async_list_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.list_actions_request.ListActionsRequest = {}  # type: ignore[typeddict-item]
        input_["target_resource_type"] = target_resource_type
        input_["target_resource_id"] = target_resource_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if resolve_to_resource_type is not None:
            input_["resolve_to_resource_type"] = resolve_to_resource_type
        if resolve_to_resource_id is not None:
            input_["resolve_to_resource_id"] = resolve_to_resource_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_actions(
        self,
        target_resource_type: "aws_sdk_iotsitewise.types.target_resource_type.TargetResourceType",
        target_resource_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
        resolve_to_resource_type: Optional[
            "aws_sdk_iotsitewise.types.resolve_to_resource_type.ResolveToResourceType"
        ] = None,
        resolve_to_resource_id: Optional["aws_sdk_iotsitewise.types.id.ID"] = None,
    ) -> "AsyncIterator[aws_sdk_iotsitewise.types.action_summary.ActionSummary]":
        _token = next_token
        while True:
            _response = await self.list_actions(
                target_resource_type,
                target_resource_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                resolve_to_resource_type=resolve_to_resource_type,
                resolve_to_resource_id=resolve_to_resource_id,
            )
            _page = _resolve_path(_response, ("action_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_asset_model_composite_models(
        self,
        asset_model_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
        asset_model_version: Optional[
            "aws_sdk_iotsitewise.types.asset_model_version_filter.AssetModelVersionFilter"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.list_asset_model_composite_models_response.ListAssetModelCompositeModelsResponse":
        """<p>Retrieves a paginated list of composite models associated with the asset model</p>

        Args:
            asset_model_id: <p>The ID of the asset model. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
            asset_model_version: <p>The version alias that specifies the latest or active version of the asset model. The details are returned in the response. The default value is <code>LATEST</code>. See <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/model-active-version.html\"> Asset model versions</a> in the <i>IoT SiteWise User Guide</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.list_asset_model_composite_models_request.ListAssetModelCompositeModelsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.list_asset_model_composite_models_response.ListAssetModelCompositeModelsResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_asset_model_composite_models

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_asset_model_composite_models.async_list_asset_model_composite_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.list_asset_model_composite_models_request.ListAssetModelCompositeModelsRequest = {}  # type: ignore[typeddict-item]
        input_["asset_model_id"] = asset_model_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if asset_model_version is not None:
            input_["asset_model_version"] = asset_model_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_asset_model_composite_models(
        self,
        asset_model_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
        asset_model_version: Optional[
            "aws_sdk_iotsitewise.types.asset_model_version_filter.AssetModelVersionFilter"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_iotsitewise.types.asset_model_composite_model_summary.AssetModelCompositeModelSummary]":
        _token = next_token
        while True:
            _response = await self.list_asset_model_composite_models(
                asset_model_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                asset_model_version=asset_model_version,
            )
            _page = _resolve_path(_response, ("asset_model_composite_model_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_asset_model_properties(
        self,
        asset_model_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
        filter: Optional[
            "aws_sdk_iotsitewise.types.list_asset_model_properties_filter.ListAssetModelPropertiesFilter"
        ] = None,
        asset_model_version: Optional[
            "aws_sdk_iotsitewise.types.asset_model_version_filter.AssetModelVersionFilter"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.list_asset_model_properties_response.ListAssetModelPropertiesResponse":
        """<p>Retrieves a paginated list of properties associated with an asset model. If you update properties associated with the model before you finish listing all the properties, you need to start all over again.</p>

        Args:
            asset_model_id: <p>The ID of the asset model. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request. If not specified, the default value is 50.</p>
            filter: <p> Filters the requested list of asset model properties. You can choose one of the following options:</p> <ul> <li> <p> <code>ALL</code> – The list includes all asset model properties for a given asset model ID. </p> </li> <li> <p> <code>BASE</code> – The list includes only base asset model properties for a given asset model ID. </p> </li> </ul> <p>Default: <code>BASE</code> </p>
            asset_model_version: <p>The version alias that specifies the latest or active version of the asset model. The details are returned in the response. The default value is <code>LATEST</code>. See <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/model-active-version.html\"> Asset model versions</a> in the <i>IoT SiteWise User Guide</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.list_asset_model_properties_request.ListAssetModelPropertiesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.list_asset_model_properties_response.ListAssetModelPropertiesResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_asset_model_properties

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_asset_model_properties.async_list_asset_model_properties(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.list_asset_model_properties_request.ListAssetModelPropertiesRequest = {}  # type: ignore[typeddict-item]
        input_["asset_model_id"] = asset_model_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter
        if asset_model_version is not None:
            input_["asset_model_version"] = asset_model_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_asset_model_properties(
        self,
        asset_model_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
        filter: Optional[
            "aws_sdk_iotsitewise.types.list_asset_model_properties_filter.ListAssetModelPropertiesFilter"
        ] = None,
        asset_model_version: Optional[
            "aws_sdk_iotsitewise.types.asset_model_version_filter.AssetModelVersionFilter"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_iotsitewise.types.asset_model_property_summary.AssetModelPropertySummary]":
        _token = next_token
        while True:
            _response = await self.list_asset_model_properties(
                asset_model_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filter=filter,
                asset_model_version=asset_model_version,
            )
            _page = _resolve_path(_response, ("asset_model_property_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_asset_models(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_model_types: Optional[
            "aws_sdk_iotsitewise.types.list_asset_models_type_filter.ListAssetModelsTypeFilter"
        ] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
        asset_model_version: Optional[
            "aws_sdk_iotsitewise.types.asset_model_version_filter.AssetModelVersionFilter"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.list_asset_models_response.ListAssetModelsResponse":
        """<p>Retrieves a paginated list of summaries of all asset models.</p>

        Args:
            asset_model_types: <p>The type of asset model. If you don't provide an <code>assetModelTypes</code>, all types of asset models are returned.</p> <ul> <li> <p> <b>ASSET_MODEL</b> – An asset model that you can use to create assets. Can't be included as a component in another asset model.</p> </li> <li> <p> <b>COMPONENT_MODEL</b> – A reusable component that you can include in the composite models of other asset models. You can't create assets directly from this type of asset model. </p> </li> <li> <p> <b>INTERFACE</b> – An interface is a type of model that defines a standard structure that can be applied to different asset models.</p> </li> </ul>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
            asset_model_version: <p>The version alias that specifies the latest or active version of the asset model. The details are returned in the response. The default value is <code>LATEST</code>. See <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/model-active-version.html\"> Asset model versions</a> in the <i>IoT SiteWise User Guide</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.list_asset_models_request.ListAssetModelsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.list_asset_models_response.ListAssetModelsResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_asset_models

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_asset_models.async_list_asset_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.list_asset_models_request.ListAssetModelsRequest = {}  # type: ignore[typeddict-item]
        if asset_model_types is not None:
            input_["asset_model_types"] = asset_model_types
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if asset_model_version is not None:
            input_["asset_model_version"] = asset_model_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_asset_models(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_model_types: Optional[
            "aws_sdk_iotsitewise.types.list_asset_models_type_filter.ListAssetModelsTypeFilter"
        ] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
        asset_model_version: Optional[
            "aws_sdk_iotsitewise.types.asset_model_version_filter.AssetModelVersionFilter"
        ] = None,
    ) -> (
        "AsyncIterator[aws_sdk_iotsitewise.types.asset_model_summary.AssetModelSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.list_asset_models(
                config_overrides=config_overrides,
                asset_model_types=asset_model_types,
                next_token=_token,
                max_results=max_results,
                asset_model_version=asset_model_version,
            )
            _page = _resolve_path(_response, ("asset_model_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_asset_properties(
        self,
        asset_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
        filter: Optional[
            "aws_sdk_iotsitewise.types.list_asset_properties_filter.ListAssetPropertiesFilter"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.list_asset_properties_response.ListAssetPropertiesResponse":
        """<p>Retrieves a paginated list of properties associated with an asset. If you update properties associated with the model before you finish listing all the properties, you need to start all over again.</p>

        Args:
            asset_id: <p>The ID of the asset. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request. If not specified, the default value is 50.</p>
            filter: <p> Filters the requested list of asset properties. You can choose one of the following options:</p> <ul> <li> <p> <code>ALL</code> – The list includes all asset properties for a given asset model ID. </p> </li> <li> <p> <code>BASE</code> – The list includes only base asset properties for a given asset model ID. </p> </li> </ul> <p>Default: <code>BASE</code> </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.list_asset_properties_request.ListAssetPropertiesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.list_asset_properties_response.ListAssetPropertiesResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_asset_properties

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_asset_properties.async_list_asset_properties(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.list_asset_properties_request.ListAssetPropertiesRequest = {}  # type: ignore[typeddict-item]
        input_["asset_id"] = asset_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_asset_properties(
        self,
        asset_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
        filter: Optional[
            "aws_sdk_iotsitewise.types.list_asset_properties_filter.ListAssetPropertiesFilter"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_iotsitewise.types.asset_property_summary.AssetPropertySummary]":
        _token = next_token
        while True:
            _response = await self.list_asset_properties(
                asset_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filter=filter,
            )
            _page = _resolve_path(_response, ("asset_property_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_asset_relationships(
        self,
        asset_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        traversal_type: "aws_sdk_iotsitewise.types.traversal_type.TraversalType",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.list_asset_relationships_response.ListAssetRelationshipsResponse":
        """<p>Retrieves a paginated list of asset relationships for an asset. You can use this operation to identify an asset's root asset and all associated assets between that asset and its root.</p>

        Args:
            asset_id: <p>The ID of the asset. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            traversal_type: <p>The type of traversal to use to identify asset relationships. Choose the following option:</p> <ul> <li> <p> <code>PATH_TO_ROOT</code> – Identify the asset's parent assets up to the root asset. The asset that you specify in <code>assetId</code> is the first result in the list of <code>assetRelationshipSummaries</code>, and the root asset is the last result.</p> </li> </ul>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.list_asset_relationships_request.ListAssetRelationshipsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.list_asset_relationships_response.ListAssetRelationshipsResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_asset_relationships

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_asset_relationships.async_list_asset_relationships(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.list_asset_relationships_request.ListAssetRelationshipsRequest = {}  # type: ignore[typeddict-item]
        input_["asset_id"] = asset_id
        input_["traversal_type"] = traversal_type
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_asset_relationships(
        self,
        asset_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        traversal_type: "aws_sdk_iotsitewise.types.traversal_type.TraversalType",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_iotsitewise.types.asset_relationship_summary.AssetRelationshipSummary]":
        _token = next_token
        while True:
            _response = await self.list_asset_relationships(
                asset_id,
                traversal_type,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("asset_relationship_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_assets(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
        asset_model_id: Optional["aws_sdk_iotsitewise.types.custom_id.CustomID"] = None,
        filter: Optional[
            "aws_sdk_iotsitewise.types.list_assets_filter.ListAssetsFilter"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.list_assets_response.ListAssetsResponse":
        """<p>Retrieves a paginated list of asset summaries.</p> <p>You can use this operation to do the following:</p> <ul> <li> <p>List assets based on a specific asset model.</p> </li> <li> <p>List top-level assets.</p> </li> </ul> <p>You can't use this operation to list all assets. To retrieve summaries for all of your assets, use <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAssetModels.html\">ListAssetModels</a> to get all of your asset model IDs. Then, use ListAssets to get all assets for each asset model.</p>

        Args:
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
            asset_model_id: <p>The ID of the asset model by which to filter the list of assets. This parameter is required if you choose <code>ALL</code> for <code>filter</code>. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            filter: <p>The filter for the requested list of assets. Choose one of the following options:</p> <ul> <li> <p> <code>ALL</code> – The list includes all assets for a given asset model ID. The <code>assetModelId</code> parameter is required if you filter by <code>ALL</code>.</p> </li> <li> <p> <code>TOP_LEVEL</code> – The list includes only top-level assets in the asset hierarchy tree.</p> </li> </ul> <p>Default: <code>ALL</code> </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.list_assets_request.ListAssetsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.list_assets_response.ListAssetsResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_assets

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_assets.async_list_assets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.list_assets_request.ListAssetsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if asset_model_id is not None:
            input_["asset_model_id"] = asset_model_id
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_assets(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
        asset_model_id: Optional["aws_sdk_iotsitewise.types.custom_id.CustomID"] = None,
        filter: Optional[
            "aws_sdk_iotsitewise.types.list_assets_filter.ListAssetsFilter"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_iotsitewise.types.asset_summary.AssetSummary]":
        _token = next_token
        while True:
            _response = await self.list_assets(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                asset_model_id=asset_model_id,
                filter=filter,
            )
            _page = _resolve_path(_response, ("asset_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_associated_assets(
        self,
        asset_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        hierarchy_id: Optional["aws_sdk_iotsitewise.types.custom_id.CustomID"] = None,
        traversal_direction: Optional[
            "aws_sdk_iotsitewise.types.traversal_direction.TraversalDirection"
        ] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.list_associated_assets_response.ListAssociatedAssetsResponse":
        """<p>Retrieves a paginated list of associated assets.</p> <p>You can use this operation to do the following:</p> <ul> <li> <p> <code>CHILD</code> - List all child assets associated to the asset.</p> </li> <li> <p> <code>PARENT</code> - List the asset's parent asset.</p> </li> </ul>

        Args:
            asset_id: <p>The ID of the asset to query. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            hierarchy_id: <p>(Optional) If you don't provide a <code>hierarchyId</code>, all the immediate assets in the <code>traversalDirection</code> will be returned. </p> <p> The ID of the hierarchy by which child assets are associated to the asset. (This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.)</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html\">Asset hierarchies</a> in the <i>IoT SiteWise User Guide</i>.</p>
            traversal_direction: <p>The direction to list associated assets. Choose one of the following options:</p> <ul> <li> <p> <code>CHILD</code> – The list includes all child assets associated to the asset.</p> </li> <li> <p> <code>PARENT</code> – The list includes the asset's parent asset.</p> </li> </ul> <p>Default: <code>CHILD</code> </p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.list_associated_assets_request.ListAssociatedAssetsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.list_associated_assets_response.ListAssociatedAssetsResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_associated_assets

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_associated_assets.async_list_associated_assets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.list_associated_assets_request.ListAssociatedAssetsRequest = {}  # type: ignore[typeddict-item]
        input_["asset_id"] = asset_id
        if hierarchy_id is not None:
            input_["hierarchy_id"] = hierarchy_id
        if traversal_direction is not None:
            input_["traversal_direction"] = traversal_direction
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_associated_assets(
        self,
        asset_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        hierarchy_id: Optional["aws_sdk_iotsitewise.types.custom_id.CustomID"] = None,
        traversal_direction: Optional[
            "aws_sdk_iotsitewise.types.traversal_direction.TraversalDirection"
        ] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_iotsitewise.types.associated_assets_summary.AssociatedAssetsSummary]":
        _token = next_token
        while True:
            _response = await self.list_associated_assets(
                asset_id,
                config_overrides=config_overrides,
                hierarchy_id=hierarchy_id,
                traversal_direction=traversal_direction,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("asset_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_bulk_import_jobs(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
        filter: Optional[
            "aws_sdk_iotsitewise.types.list_bulk_import_jobs_filter.ListBulkImportJobsFilter"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.list_bulk_import_jobs_response.ListBulkImportJobsResponse":
        """<p>Retrieves a paginated list of bulk import job requests. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/ListBulkImportJobs.html\">List bulk import jobs (CLI)</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Args:
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p>
            filter: <p>You can use a filter to select the bulk import jobs that you want to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.list_bulk_import_jobs_request.ListBulkImportJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.list_bulk_import_jobs_response.ListBulkImportJobsResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_bulk_import_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_bulk_import_jobs.async_list_bulk_import_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.list_bulk_import_jobs_request.ListBulkImportJobsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_bulk_import_jobs(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
        filter: Optional[
            "aws_sdk_iotsitewise.types.list_bulk_import_jobs_filter.ListBulkImportJobsFilter"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_iotsitewise.types.job_summary.JobSummary]":
        _token = next_token
        while True:
            _response = await self.list_bulk_import_jobs(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filter=filter,
            )
            _page = _resolve_path(_response, ("job_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_composition_relationships(
        self,
        asset_model_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.list_composition_relationships_response.ListCompositionRelationshipsResponse":
        """<p>Retrieves a paginated list of composition relationships for an asset model of type <code>COMPONENT_MODEL</code>.</p>

        Args:
            asset_model_id: <p>The ID of the asset model. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.list_composition_relationships_request.ListCompositionRelationshipsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.list_composition_relationships_response.ListCompositionRelationshipsResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_composition_relationships

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_composition_relationships.async_list_composition_relationships(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.list_composition_relationships_request.ListCompositionRelationshipsRequest = {}  # type: ignore[typeddict-item]
        input_["asset_model_id"] = asset_model_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_composition_relationships(
        self,
        asset_model_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_iotsitewise.types.composition_relationship_summary.CompositionRelationshipSummary]":
        _token = next_token
        while True:
            _response = await self.list_composition_relationships(
                asset_model_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("composition_relationship_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_computation_model_data_binding_usages(
        self,
        data_binding_value_filter: "aws_sdk_iotsitewise.types.data_binding_value_filter.DataBindingValueFilter",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.list_computation_model_data_binding_usages_response.ListComputationModelDataBindingUsagesResponse":
        """<p> Lists all data binding usages for computation models. This allows to identify where specific data bindings are being utilized across the computation models. This track dependencies between data sources and computation models. </p>

        Args:
            data_binding_value_filter: <p>A filter used to limit the returned data binding usages based on specific data binding values. You can filter by asset, asset model, asset property, or asset model property to find all computation models using these specific data sources.</p>
            next_token: <p>The token used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results returned for each paginated request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.list_computation_model_data_binding_usages_request.ListComputationModelDataBindingUsagesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.list_computation_model_data_binding_usages_response.ListComputationModelDataBindingUsagesResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_computation_model_data_binding_usages

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_computation_model_data_binding_usages.async_list_computation_model_data_binding_usages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.list_computation_model_data_binding_usages_request.ListComputationModelDataBindingUsagesRequest = {}  # type: ignore[typeddict-item]
        input_["data_binding_value_filter"] = data_binding_value_filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_computation_model_data_binding_usages(
        self,
        data_binding_value_filter: "aws_sdk_iotsitewise.types.data_binding_value_filter.DataBindingValueFilter",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_iotsitewise.types.computation_model_data_binding_usage_summary.ComputationModelDataBindingUsageSummary]":
        _token = next_token
        while True:
            _response = await self.list_computation_model_data_binding_usages(
                data_binding_value_filter,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("data_binding_usage_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_computation_model_resolve_to_resources(
        self,
        computation_model_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.list_computation_model_resolve_to_resources_response.ListComputationModelResolveToResourcesResponse":
        """<p>Lists all distinct resources that are resolved from the executed actions of the computation model.</p>

        Args:
            computation_model_id: <p>The ID of the computation model for which to list resolved resources.</p>
            next_token: <p>The token used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results returned for each paginated request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.list_computation_model_resolve_to_resources_request.ListComputationModelResolveToResourcesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.list_computation_model_resolve_to_resources_response.ListComputationModelResolveToResourcesResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_computation_model_resolve_to_resources

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_computation_model_resolve_to_resources.async_list_computation_model_resolve_to_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.list_computation_model_resolve_to_resources_request.ListComputationModelResolveToResourcesRequest = {}  # type: ignore[typeddict-item]
        input_["computation_model_id"] = computation_model_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_computation_model_resolve_to_resources(
        self,
        computation_model_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_iotsitewise.types.computation_model_resolve_to_resource_summary.ComputationModelResolveToResourceSummary]":
        _token = next_token
        while True:
            _response = await self.list_computation_model_resolve_to_resources(
                computation_model_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(
                _response, ("computation_model_resolve_to_resource_summaries",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_computation_models(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        computation_model_type: Optional[
            "aws_sdk_iotsitewise.types.computation_model_type.ComputationModelType"
        ] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.list_computation_models_response.ListComputationModelsResponse":
        """<p>Retrieves a paginated list of summaries of all computation models.</p>

        Args:
            computation_model_type: <p>The type of computation model. If a <code>computationModelType</code> is not provided, all types of computation models are returned.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.list_computation_models_request.ListComputationModelsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.list_computation_models_response.ListComputationModelsResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_computation_models

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_computation_models.async_list_computation_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.list_computation_models_request.ListComputationModelsRequest = {}  # type: ignore[typeddict-item]
        if computation_model_type is not None:
            input_["computation_model_type"] = computation_model_type
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_computation_models(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        computation_model_type: Optional[
            "aws_sdk_iotsitewise.types.computation_model_type.ComputationModelType"
        ] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_iotsitewise.types.computation_model_summary.ComputationModelSummary]":
        _token = next_token
        while True:
            _response = await self.list_computation_models(
                config_overrides=config_overrides,
                computation_model_type=computation_model_type,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("computation_model_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_dashboards(
        self,
        project_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.list_dashboards_response.ListDashboardsResponse":
        """<p>Retrieves a paginated list of dashboards for an IoT SiteWise Monitor project.</p>

        Args:
            project_id: <p>The ID of the project.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.list_dashboards_request.ListDashboardsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.list_dashboards_response.ListDashboardsResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_dashboards

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_dashboards.async_list_dashboards(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.list_dashboards_request.ListDashboardsRequest = {}  # type: ignore[typeddict-item]
        input_["project_id"] = project_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_dashboards(
        self,
        project_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_iotsitewise.types.dashboard_summary.DashboardSummary]":
        _token = next_token
        while True:
            _response = await self.list_dashboards(
                project_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("dashboard_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_datasets(
        self,
        source_type: "aws_sdk_iotsitewise.types.dataset_source_type.DatasetSourceType",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.list_datasets_response.ListDatasetsResponse":
        """<p>Retrieves a paginated list of datasets for a specific target resource.</p>

        Args:
            source_type: <p>The type of data source for the dataset.</p>
            next_token: <p>The token for the next set of results, or null if there are no additional results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.list_datasets_request.ListDatasetsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.list_datasets_response.ListDatasetsResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_datasets

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_datasets.async_list_datasets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.list_datasets_request.ListDatasetsRequest = {}  # type: ignore[typeddict-item]
        input_["source_type"] = source_type
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_datasets(
        self,
        source_type: "aws_sdk_iotsitewise.types.dataset_source_type.DatasetSourceType",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_iotsitewise.types.dataset_summary.DatasetSummary]":
        _token = next_token
        while True:
            _response = await self.list_datasets(
                source_type,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("dataset_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_executions(
        self,
        target_resource_type: "aws_sdk_iotsitewise.types.target_resource_type.TargetResourceType",
        target_resource_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        resolve_to_resource_type: Optional[
            "aws_sdk_iotsitewise.types.resolve_to_resource_type.ResolveToResourceType"
        ] = None,
        resolve_to_resource_id: Optional["aws_sdk_iotsitewise.types.id.ID"] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
        action_type: Optional["aws_sdk_iotsitewise.types.name.Name"] = None,
    ) -> "aws_sdk_iotsitewise.types.list_executions_response.ListExecutionsResponse":
        """<p>Retrieves a paginated list of summaries of all executions.</p>

        Args:
            target_resource_type: <p>The type of the target resource.</p>
            target_resource_id: <p>The ID of the target resource.</p>
            resolve_to_resource_type: <p>The type of the resolved resource.</p>
            resolve_to_resource_id: <p>The ID of the resolved resource.</p>
            next_token: <p>The token used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results returned for each paginated request.</p>
            action_type: <p>The type of action exectued.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.list_executions_request.ListExecutionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.list_executions_response.ListExecutionsResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_executions

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_executions.async_list_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.list_executions_request.ListExecutionsRequest = {}  # type: ignore[typeddict-item]
        input_["target_resource_type"] = target_resource_type
        input_["target_resource_id"] = target_resource_id
        if resolve_to_resource_type is not None:
            input_["resolve_to_resource_type"] = resolve_to_resource_type
        if resolve_to_resource_id is not None:
            input_["resolve_to_resource_id"] = resolve_to_resource_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if action_type is not None:
            input_["action_type"] = action_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_executions(
        self,
        target_resource_type: "aws_sdk_iotsitewise.types.target_resource_type.TargetResourceType",
        target_resource_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        resolve_to_resource_type: Optional[
            "aws_sdk_iotsitewise.types.resolve_to_resource_type.ResolveToResourceType"
        ] = None,
        resolve_to_resource_id: Optional["aws_sdk_iotsitewise.types.id.ID"] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
        action_type: Optional["aws_sdk_iotsitewise.types.name.Name"] = None,
    ) -> "AsyncIterator[aws_sdk_iotsitewise.types.execution_summary.ExecutionSummary]":
        _token = next_token
        while True:
            _response = await self.list_executions(
                target_resource_type,
                target_resource_id,
                config_overrides=config_overrides,
                resolve_to_resource_type=resolve_to_resource_type,
                resolve_to_resource_id=resolve_to_resource_id,
                next_token=_token,
                max_results=max_results,
                action_type=action_type,
            )
            _page = _resolve_path(_response, ("execution_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_gateways(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.list_gateways_response.ListGatewaysResponse":
        """<p>Retrieves a paginated list of gateways.</p>

        Args:
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.list_gateways_request.ListGatewaysRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.list_gateways_response.ListGatewaysResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_gateways

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_gateways.async_list_gateways(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.list_gateways_request.ListGatewaysRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_gateways(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_iotsitewise.types.gateway_summary.GatewaySummary]":
        _token = next_token
        while True:
            _response = await self.list_gateways(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("gateway_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_interface_relationships(
        self,
        interface_asset_model_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.list_interface_relationships_response.ListInterfaceRelationshipsResponse":
        """<p>Retrieves a paginated list of asset models that have a specific interface asset model applied to them.</p>

        Args:
            interface_asset_model_id: <p>The ID of the interface asset model. This can be either the actual ID in UUID format, or else externalId: followed by the external ID.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request. Default: 50</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.list_interface_relationships_request.ListInterfaceRelationshipsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.list_interface_relationships_response.ListInterfaceRelationshipsResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_interface_relationships

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_interface_relationships.async_list_interface_relationships(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.list_interface_relationships_request.ListInterfaceRelationshipsRequest = {}  # type: ignore[typeddict-item]
        input_["interface_asset_model_id"] = interface_asset_model_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_interface_relationships(
        self,
        interface_asset_model_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_iotsitewise.types.interface_relationship_summary.InterfaceRelationshipSummary]":
        _token = next_token
        while True:
            _response = await self.list_interface_relationships(
                interface_asset_model_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("interface_relationship_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_portals(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.list_portals_response.ListPortalsResponse":
        """<p>Retrieves a paginated list of IoT SiteWise Monitor portals.</p>

        Args:
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.list_portals_request.ListPortalsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.list_portals_response.ListPortalsResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_portals

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_portals.async_list_portals(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.list_portals_request.ListPortalsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_portals(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_iotsitewise.types.portal_summary.PortalSummary]":
        _token = next_token
        while True:
            _response = await self.list_portals(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("portal_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_project_assets(
        self,
        project_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.list_project_assets_response.ListProjectAssetsResponse":
        """<p>Retrieves a paginated list of assets associated with an IoT SiteWise Monitor project.</p>

        Args:
            project_id: <p>The ID of the project.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.list_project_assets_request.ListProjectAssetsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.list_project_assets_response.ListProjectAssetsResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_project_assets

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_project_assets.async_list_project_assets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.list_project_assets_request.ListProjectAssetsRequest = {}  # type: ignore[typeddict-item]
        input_["project_id"] = project_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_project_assets(
        self,
        project_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_iotsitewise.types.id.ID]":
        _token = next_token
        while True:
            _response = await self.list_project_assets(
                project_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("asset_ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_projects(
        self,
        portal_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.list_projects_response.ListProjectsResponse":
        """<p>Retrieves a paginated list of projects for an IoT SiteWise Monitor portal.</p>

        Args:
            portal_id: <p>The ID of the portal.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.list_projects_request.ListProjectsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.list_projects_response.ListProjectsResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_projects

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_projects.async_list_projects(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.list_projects_request.ListProjectsRequest = {}  # type: ignore[typeddict-item]
        input_["portal_id"] = portal_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_projects(
        self,
        portal_id: "aws_sdk_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_iotsitewise.types.project_summary.ProjectSummary]":
        _token = next_token
        while True:
            _response = await self.list_projects(
                portal_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("project_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_iotsitewise.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "aws_sdk_iotsitewise.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieves the list of tags for an IoT SiteWise resource.</p>

        Args:
            resource_arn: <p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_time_series(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
        asset_id: Optional["aws_sdk_iotsitewise.types.custom_id.CustomID"] = None,
        alias_prefix: Optional[
            "aws_sdk_iotsitewise.types.property_alias.PropertyAlias"
        ] = None,
        time_series_type: Optional[
            "aws_sdk_iotsitewise.types.list_time_series_type.ListTimeSeriesType"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.list_time_series_response.ListTimeSeriesResponse":
        """<p>Retrieves a paginated list of time series (data streams).</p>

        Args:
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p>
            asset_id: <p>The ID of the asset in which the asset property was created. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            alias_prefix: <p>The alias prefix of the time series.</p>
            time_series_type: <p>The type of the time series. The time series type can be one of the following values:</p> <ul> <li> <p> <code>ASSOCIATED</code> – The time series is associated with an asset property.</p> </li> <li> <p> <code>DISASSOCIATED</code> – The time series isn't associated with any asset property.</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.list_time_series_request.ListTimeSeriesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.list_time_series_response.ListTimeSeriesResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_time_series

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.list_time_series.async_list_time_series(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.list_time_series_request.ListTimeSeriesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if asset_id is not None:
            input_["asset_id"] = asset_id
        if alias_prefix is not None:
            input_["alias_prefix"] = alias_prefix
        if time_series_type is not None:
            input_["time_series_type"] = time_series_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_time_series(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotsitewise.types.max_results.MaxResults"
        ] = None,
        asset_id: Optional["aws_sdk_iotsitewise.types.custom_id.CustomID"] = None,
        alias_prefix: Optional[
            "aws_sdk_iotsitewise.types.property_alias.PropertyAlias"
        ] = None,
        time_series_type: Optional[
            "aws_sdk_iotsitewise.types.list_time_series_type.ListTimeSeriesType"
        ] = None,
    ) -> (
        "AsyncIterator[aws_sdk_iotsitewise.types.time_series_summary.TimeSeriesSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.list_time_series(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                asset_id=asset_id,
                alias_prefix=alias_prefix,
                time_series_type=time_series_type,
            )
            _page = _resolve_path(_response, ("time_series_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_asset_model_interface_relationship(
        self,
        asset_model_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        interface_asset_model_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        property_mapping_configuration: "aws_sdk_iotsitewise.types.property_mapping_configuration.PropertyMappingConfiguration",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.put_asset_model_interface_relationship_response.PutAssetModelInterfaceRelationshipResponse":
        """<p>Creates or updates an interface relationship between an asset model and an interface asset model. This operation applies an interface to an asset model.</p>

        Args:
            asset_model_id: <p>The ID of the asset model. This can be either the actual ID in UUID format, or else externalId: followed by the external ID.</p>
            interface_asset_model_id: <p>The ID of the interface asset model. This can be either the actual ID in UUID format, or else externalId: followed by the external ID.</p>
            property_mapping_configuration: <p>The configuration for mapping properties from the interface asset model to the asset model where the interface is applied. This configuration controls how properties are matched and created during the interface application process.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.put_asset_model_interface_relationship_request.PutAssetModelInterfaceRelationshipRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.put_asset_model_interface_relationship_response.PutAssetModelInterfaceRelationshipResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.put_asset_model_interface_relationship

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.put_asset_model_interface_relationship.async_put_asset_model_interface_relationship(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.put_asset_model_interface_relationship_request.PutAssetModelInterfaceRelationshipRequest = {}  # type: ignore[typeddict-item]
        input_["asset_model_id"] = asset_model_id
        input_["interface_asset_model_id"] = interface_asset_model_id
        input_["property_mapping_configuration"] = property_mapping_configuration
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_default_encryption_configuration(
        self,
        encryption_type: "aws_sdk_iotsitewise.types.encryption_type.EncryptionType",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        kms_key_id: Optional["aws_sdk_iotsitewise.types.kms_key_id.KmsKeyId"] = None,
    ) -> "aws_sdk_iotsitewise.types.put_default_encryption_configuration_response.PutDefaultEncryptionConfigurationResponse":
        """<p>Sets the default encryption configuration for the Amazon Web Services account. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/key-management.html\">Key management</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Args:
            encryption_type: <p>The type of encryption used for the encryption configuration.</p>
            kms_key_id: <p>The Key ID of the customer managed key used for KMS encryption. This is required if you use <code>KMS_BASED_ENCRYPTION</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.put_default_encryption_configuration_request.PutDefaultEncryptionConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.put_default_encryption_configuration_response.PutDefaultEncryptionConfigurationResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.put_default_encryption_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.put_default_encryption_configuration.async_put_default_encryption_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.put_default_encryption_configuration_request.PutDefaultEncryptionConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["encryption_type"] = encryption_type
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_logging_options(
        self,
        logging_options: "aws_sdk_iotsitewise.types.logging_options.LoggingOptions",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "aws_sdk_iotsitewise.types.put_logging_options_response.PutLoggingOptionsResponse":
        """<p>Sets logging options for IoT SiteWise.</p>

        Args:
            logging_options: <p>The logging options to set.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.put_logging_options_request.PutLoggingOptionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.put_logging_options_response.PutLoggingOptionsResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.put_logging_options

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.put_logging_options.async_put_logging_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.put_logging_options_request.PutLoggingOptionsRequest = {}  # type: ignore[typeddict-item]
        input_["logging_options"] = logging_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_storage_configuration(
        self,
        storage_type: "aws_sdk_iotsitewise.types.storage_type.StorageType",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        multi_layer_storage: Optional[
            "aws_sdk_iotsitewise.types.multi_layer_storage.MultiLayerStorage"
        ] = None,
        disassociated_data_storage: Optional[
            "aws_sdk_iotsitewise.types.disassociated_data_storage_state.DisassociatedDataStorageState"
        ] = None,
        retention_period: Optional[
            "aws_sdk_iotsitewise.types.retention_period.RetentionPeriod"
        ] = None,
        warm_tier: Optional[
            "aws_sdk_iotsitewise.types.warm_tier_state.WarmTierState"
        ] = None,
        warm_tier_retention_period: Optional[
            "aws_sdk_iotsitewise.types.warm_tier_retention_period.WarmTierRetentionPeriod"
        ] = None,
        disallow_ingest_null_na_n: Optional[
            "aws_sdk_iotsitewise.types.disallow_ingest_null_na_n.DisallowIngestNullNaN"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.put_storage_configuration_response.PutStorageConfigurationResponse":
        """<p>Configures storage settings for IoT SiteWise.</p>

        Args:
            storage_type: <p>The storage tier that you specified for your data. The <code>storageType</code> parameter can be one of the following values:</p> <ul> <li> <p> <code>SITEWISE_DEFAULT_STORAGE</code> – IoT SiteWise saves your data into the hot tier. The hot tier is a service-managed database.</p> </li> <li> <p> <code>MULTI_LAYER_STORAGE</code> – IoT SiteWise saves your data in both the cold tier and the hot tier. The cold tier is a customer-managed Amazon S3 bucket.</p> </li> </ul>
            multi_layer_storage: <p>Identifies a storage destination. If you specified <code>MULTI_LAYER_STORAGE</code> for the storage type, you must specify a <code>MultiLayerStorage</code> object.</p>
            disassociated_data_storage: <p>Contains the storage configuration for time series (data streams) that aren't associated with asset properties. The <code>disassociatedDataStorage</code> can be one of the following values:</p> <ul> <li> <p> <code>ENABLED</code> – IoT SiteWise accepts time series that aren't associated with asset properties.</p> <important> <p>After the <code>disassociatedDataStorage</code> is enabled, you can't disable it.</p> </important> </li> <li> <p> <code>DISABLED</code> – IoT SiteWise doesn't accept time series (data streams) that aren't associated with asset properties.</p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/data-streams.html\">Data streams</a> in the <i>IoT SiteWise User Guide</i>.</p>
            warm_tier: <p>A service managed storage tier optimized for analytical queries. It stores periodically uploaded, buffered and historical data ingested with the CreaeBulkImportJob API.</p>
            warm_tier_retention_period: <p>Set this period to specify how long your data is stored in the warm tier before it is deleted. You can set this only if cold tier is enabled.</p>
            disallow_ingest_null_na_n: <p>Describes the configuration for ingesting NULL and NaN data. By default the feature is allowed. The feature is disallowed if the value is <code>true</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.put_storage_configuration_request.PutStorageConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.put_storage_configuration_response.PutStorageConfigurationResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.put_storage_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.put_storage_configuration.async_put_storage_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.put_storage_configuration_request.PutStorageConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["storage_type"] = storage_type
        if multi_layer_storage is not None:
            input_["multi_layer_storage"] = multi_layer_storage
        if disassociated_data_storage is not None:
            input_["disassociated_data_storage"] = disassociated_data_storage
        if retention_period is not None:
            input_["retention_period"] = retention_period
        if warm_tier is not None:
            input_["warm_tier"] = warm_tier
        if warm_tier_retention_period is not None:
            input_["warm_tier_retention_period"] = warm_tier_retention_period
        if disallow_ingest_null_na_n is not None:
            input_["disallow_ingest_null_na_n"] = disallow_ingest_null_na_n

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_iotsitewise.types.amazon_resource_name.AmazonResourceName",
        tags: "aws_sdk_iotsitewise.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "aws_sdk_iotsitewise.types.tag_resource_response.TagResourceResponse":
        """<p>Adds tags to an IoT SiteWise resource. If a tag already exists for the resource, this operation updates the tag's value.</p>

        Args:
            resource_arn: <p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the resource to tag.</p>
            tags: <p>A list of key-value pairs that contain metadata for the resource. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html\">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_iotsitewise.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "aws_sdk_iotsitewise.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "aws_sdk_iotsitewise.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag from an IoT SiteWise resource.</p>

        Args:
            resource_arn: <p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the resource to untag.</p>
            tag_keys: <p>A list of keys for tags to remove from the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_access_policy(
        self,
        access_policy_id: "aws_sdk_iotsitewise.types.id.ID",
        access_policy_identity: "aws_sdk_iotsitewise.types.identity.Identity",
        access_policy_resource: "aws_sdk_iotsitewise.types.resource.Resource",
        access_policy_permission: "aws_sdk_iotsitewise.types.permission.Permission",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.update_access_policy_response.UpdateAccessPolicyResponse":
        """<p>Updates an existing access policy that specifies an identity's access to an IoT SiteWise Monitor portal or project resource.</p>

        Args:
            access_policy_id: <p>The ID of the access policy.</p>
            access_policy_identity: <p>The identity for this access policy. Choose an IAM Identity Center user, an IAM Identity Center group, or an IAM user.</p>
            access_policy_resource: <p>The IoT SiteWise Monitor resource for this access policy. Choose either a portal or a project.</p>
            access_policy_permission: <p>The permission level for this access policy. Note that a project <code>ADMINISTRATOR</code> is also known as a project owner.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.update_access_policy_request.UpdateAccessPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.update_access_policy_response.UpdateAccessPolicyResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.update_access_policy

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.update_access_policy.async_update_access_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.update_access_policy_request.UpdateAccessPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["access_policy_id"] = access_policy_id
        input_["access_policy_identity"] = access_policy_identity
        input_["access_policy_resource"] = access_policy_resource
        input_["access_policy_permission"] = access_policy_permission
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_asset(
        self,
        asset_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        asset_name: "aws_sdk_iotsitewise.types.name.Name",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_external_id: Optional[
            "aws_sdk_iotsitewise.types.external_id.ExternalId"
        ] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
        asset_description: Optional[
            "aws_sdk_iotsitewise.types.description.Description"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.update_asset_response.UpdateAssetResponse":
        """<p>Updates an asset's name. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-assets-and-models.html\">Updating assets and models</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Args:
            asset_id: <p>The ID of the asset to update. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            asset_external_id: <p>An external ID to assign to the asset. The asset must not already have an external ID. The external ID must be unique within your Amazon Web Services account. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids\">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            asset_name: <p>A friendly name for the asset.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            asset_description: <p>A description for the asset.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.update_asset_request.UpdateAssetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.update_asset_response.UpdateAssetResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.update_asset

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.update_asset.async_update_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.update_asset_request.UpdateAssetRequest = {}  # type: ignore[typeddict-item]
        input_["asset_id"] = asset_id
        if asset_external_id is not None:
            input_["asset_external_id"] = asset_external_id
        input_["asset_name"] = asset_name
        if client_token is not None:
            input_["client_token"] = client_token
        if asset_description is not None:
            input_["asset_description"] = asset_description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_asset_model(
        self,
        asset_model_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        asset_model_name: "aws_sdk_iotsitewise.types.name.Name",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_model_external_id: Optional[
            "aws_sdk_iotsitewise.types.external_id.ExternalId"
        ] = None,
        asset_model_description: Optional[
            "aws_sdk_iotsitewise.types.description.Description"
        ] = None,
        asset_model_properties: Optional[
            "aws_sdk_iotsitewise.types.asset_model_properties.AssetModelProperties"
        ] = None,
        asset_model_hierarchies: Optional[
            "aws_sdk_iotsitewise.types.asset_model_hierarchies.AssetModelHierarchies"
        ] = None,
        asset_model_composite_models: Optional[
            "aws_sdk_iotsitewise.types.asset_model_composite_models.AssetModelCompositeModels"
        ] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
        if_match: Optional["aws_sdk_iotsitewise.types.e_tag.ETag"] = None,
        if_none_match: Optional[
            "aws_sdk_iotsitewise.types.select_all.SelectAll"
        ] = None,
        match_for_version_type: Optional[
            "aws_sdk_iotsitewise.types.asset_model_version_type.AssetModelVersionType"
        ] = None,
    ) -> (
        "aws_sdk_iotsitewise.types.update_asset_model_response.UpdateAssetModelResponse"
    ):
        """<p>Updates an asset model and all of the assets that were created from the model. Each asset created from the model inherits the updated asset model's property and hierarchy definitions. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-assets-and-models.html\">Updating assets and models</a> in the <i>IoT SiteWise User Guide</i>.</p> <important> <p>If you remove a property from an asset model, IoT SiteWise deletes all previous data for that property. You can’t change the type or data type of an existing property.</p> <p>To replace an existing asset model property with a new one with the same <code>name</code>, do the following:</p> <ol> <li> <p>Submit an <code>UpdateAssetModel</code> request with the entire existing property removed.</p> </li> <li> <p>Submit a second <code>UpdateAssetModel</code> request that includes the new property. The new asset property will have the same <code>name</code> as the previous one and IoT SiteWise will generate a new unique <code>id</code>.</p> </li> </ol> </important>

        Args:
            asset_model_id: <p>The ID of the asset model to update. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            asset_model_external_id: <p>An external ID to assign to the asset model. The asset model must not already have an external ID. The external ID must be unique within your Amazon Web Services account. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids\">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            asset_model_name: <p>A unique name for the asset model.</p>
            asset_model_description: <p>A description for the asset model.</p>
            asset_model_properties: <p>The updated property definitions of the asset model. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-properties.html\">Asset properties</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>You can specify up to 200 properties per asset model. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html\">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            asset_model_hierarchies: <p>The updated hierarchy definitions of the asset model. Each hierarchy specifies an asset model whose assets can be children of any other assets created from this asset model. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html\">Asset hierarchies</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>You can specify up to 10 hierarchies per asset model. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html\">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            asset_model_composite_models: <p>The composite models that are part of this asset model. It groups properties (such as attributes, measurements, transforms, and metrics) and child composite models that model parts of your industrial equipment. Each composite model has a type that defines the properties that the composite model supports. Use composite models to define alarms on this asset model.</p> <note> <p>When creating custom composite models, you need to use <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModelCompositeModel.html\">CreateAssetModelCompositeModel</a>. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-custom-composite-models.html\">Creating custom composite models (Components)</a> in the <i>IoT SiteWise User Guide</i>.</p> </note>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            if_match: <p>The expected current entity tag (ETag) for the asset model’s latest or active version (specified using <code>matchForVersionType</code>). The update request is rejected if the tag does not match the latest or active version's current entity tag. See <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/opt-locking-for-model.html\">Optimistic locking for asset model writes</a> in the <i>IoT SiteWise User Guide</i>.</p>
            if_none_match: <p>Accepts <b>*</b> to reject the update request if an active version (specified using <code>matchForVersionType</code> as <code>ACTIVE</code>) already exists for the asset model.</p>
            match_for_version_type: <p>Specifies the asset model version type (<code>LATEST</code> or <code>ACTIVE</code>) used in conjunction with <code>If-Match</code> or <code>If-None-Match</code> headers to determine the target ETag for the update operation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.update_asset_model_request.UpdateAssetModelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.update_asset_model_response.UpdateAssetModelResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.update_asset_model

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.update_asset_model.async_update_asset_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.update_asset_model_request.UpdateAssetModelRequest = {}  # type: ignore[typeddict-item]
        input_["asset_model_id"] = asset_model_id
        if asset_model_external_id is not None:
            input_["asset_model_external_id"] = asset_model_external_id
        input_["asset_model_name"] = asset_model_name
        if asset_model_description is not None:
            input_["asset_model_description"] = asset_model_description
        if asset_model_properties is not None:
            input_["asset_model_properties"] = asset_model_properties
        if asset_model_hierarchies is not None:
            input_["asset_model_hierarchies"] = asset_model_hierarchies
        if asset_model_composite_models is not None:
            input_["asset_model_composite_models"] = asset_model_composite_models
        if client_token is not None:
            input_["client_token"] = client_token
        if if_match is not None:
            input_["if_match"] = if_match
        if if_none_match is not None:
            input_["if_none_match"] = if_none_match
        if match_for_version_type is not None:
            input_["match_for_version_type"] = match_for_version_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_asset_model_composite_model(
        self,
        asset_model_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        asset_model_composite_model_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        asset_model_composite_model_name: "aws_sdk_iotsitewise.types.name.Name",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_model_composite_model_external_id: Optional[
            "aws_sdk_iotsitewise.types.external_id.ExternalId"
        ] = None,
        asset_model_composite_model_description: Optional[
            "aws_sdk_iotsitewise.types.description.Description"
        ] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
        asset_model_composite_model_properties: Optional[
            "aws_sdk_iotsitewise.types.asset_model_properties.AssetModelProperties"
        ] = None,
        if_match: Optional["aws_sdk_iotsitewise.types.e_tag.ETag"] = None,
        if_none_match: Optional[
            "aws_sdk_iotsitewise.types.select_all.SelectAll"
        ] = None,
        match_for_version_type: Optional[
            "aws_sdk_iotsitewise.types.asset_model_version_type.AssetModelVersionType"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.update_asset_model_composite_model_response.UpdateAssetModelCompositeModelResponse":
        """<p>Updates a composite model and all of the assets that were created from the model. Each asset created from the model inherits the updated asset model's property and hierarchy definitions. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-assets-and-models.html\">Updating assets and models</a> in the <i>IoT SiteWise User Guide</i>.</p> <important> <p>If you remove a property from a composite asset model, IoT SiteWise deletes all previous data for that property. You can’t change the type or data type of an existing property.</p> <p>To replace an existing composite asset model property with a new one with the same <code>name</code>, do the following:</p> <ol> <li> <p>Submit an <code>UpdateAssetModelCompositeModel</code> request with the entire existing property removed.</p> </li> <li> <p>Submit a second <code>UpdateAssetModelCompositeModel</code> request that includes the new property. The new asset property will have the same <code>name</code> as the previous one and IoT SiteWise will generate a new unique <code>id</code>.</p> </li> </ol> </important>

        Args:
            asset_model_id: <p>The ID of the asset model, in UUID format.</p>
            asset_model_composite_model_id: <p>The ID of a composite model on this asset model.</p>
            asset_model_composite_model_external_id: <p>An external ID to assign to the asset model. You can only set the external ID of the asset model if it wasn't set when it was created, or you're setting it to the exact same thing as when it was created.</p>
            asset_model_composite_model_description: <p>A description for the composite model.</p>
            asset_model_composite_model_name: <p>A unique name for the composite model.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            asset_model_composite_model_properties: <p>The property definitions of the composite model. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/custom-composite-models.html#inline-composite-models\"> Inline custom composite models</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>You can specify up to 200 properties per composite model. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html\">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            if_match: <p>The expected current entity tag (ETag) for the asset model’s latest or active version (specified using <code>matchForVersionType</code>). The update request is rejected if the tag does not match the latest or active version's current entity tag. See <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/opt-locking-for-model.html\">Optimistic locking for asset model writes</a> in the <i>IoT SiteWise User Guide</i>.</p>
            if_none_match: <p>Accepts <b>*</b> to reject the update request if an active version (specified using <code>matchForVersionType</code> as <code>ACTIVE</code>) already exists for the asset model.</p>
            match_for_version_type: <p>Specifies the asset model version type (<code>LATEST</code> or <code>ACTIVE</code>) used in conjunction with <code>If-Match</code> or <code>If-None-Match</code> headers to determine the target ETag for the update operation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.update_asset_model_composite_model_request.UpdateAssetModelCompositeModelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.update_asset_model_composite_model_response.UpdateAssetModelCompositeModelResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.update_asset_model_composite_model

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.update_asset_model_composite_model.async_update_asset_model_composite_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.update_asset_model_composite_model_request.UpdateAssetModelCompositeModelRequest = {}  # type: ignore[typeddict-item]
        input_["asset_model_id"] = asset_model_id
        input_["asset_model_composite_model_id"] = asset_model_composite_model_id
        if asset_model_composite_model_external_id is not None:
            input_["asset_model_composite_model_external_id"] = (
                asset_model_composite_model_external_id
            )
        if asset_model_composite_model_description is not None:
            input_["asset_model_composite_model_description"] = (
                asset_model_composite_model_description
            )
        input_["asset_model_composite_model_name"] = asset_model_composite_model_name
        if client_token is not None:
            input_["client_token"] = client_token
        if asset_model_composite_model_properties is not None:
            input_["asset_model_composite_model_properties"] = (
                asset_model_composite_model_properties
            )
        if if_match is not None:
            input_["if_match"] = if_match
        if if_none_match is not None:
            input_["if_none_match"] = if_none_match
        if match_for_version_type is not None:
            input_["match_for_version_type"] = match_for_version_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_asset_property(
        self,
        asset_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        property_id: "aws_sdk_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        property_alias: Optional[
            "aws_sdk_iotsitewise.types.property_alias.PropertyAlias"
        ] = None,
        property_notification_state: Optional[
            "aws_sdk_iotsitewise.types.property_notification_state.PropertyNotificationState"
        ] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
        property_unit: Optional[
            "aws_sdk_iotsitewise.types.property_unit.PropertyUnit"
        ] = None,
    ) -> None:
        """<p>Updates an asset property's alias and notification state.</p> <important> <p>This operation overwrites the property's existing alias and notification state. To keep your existing property's alias or notification state, you must include the existing values in the UpdateAssetProperty request. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetProperty.html\">DescribeAssetProperty</a>.</p> </important>

        Args:
            asset_id: <p>The ID of the asset to be updated. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            property_id: <p>The ID of the asset property to be updated. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            property_alias: <p>The alias that identifies the property, such as an OPC-UA server data stream path (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\">Mapping industrial data streams to asset properties</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>If you omit this parameter, the alias is removed from the property.</p>
            property_notification_state: <p>The MQTT notification state (enabled or disabled) for this asset property. When the notification state is enabled, IoT SiteWise publishes property value updates to a unique MQTT topic. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/interact-with-other-services.html\">Interacting with other services</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>If you omit this parameter, the notification state is set to <code>DISABLED</code>.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            property_unit: <p>The unit of measure (such as Newtons or RPM) of the asset property. If you don't specify a value for this parameter, the service uses the value of the <code>assetModelProperty</code> in the asset model.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.update_asset_property_request.UpdateAssetPropertyRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.update_asset_property

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.update_asset_property.async_update_asset_property(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.update_asset_property_request.UpdateAssetPropertyRequest = {}  # type: ignore[typeddict-item]
        input_["asset_id"] = asset_id
        input_["property_id"] = property_id
        if property_alias is not None:
            input_["property_alias"] = property_alias
        if property_notification_state is not None:
            input_["property_notification_state"] = property_notification_state
        if client_token is not None:
            input_["client_token"] = client_token
        if property_unit is not None:
            input_["property_unit"] = property_unit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_computation_model(
        self,
        computation_model_id: "aws_sdk_iotsitewise.types.id.ID",
        computation_model_name: "aws_sdk_iotsitewise.types.restricted_name.RestrictedName",
        computation_model_configuration: "aws_sdk_iotsitewise.types.computation_model_configuration.ComputationModelConfiguration",
        computation_model_data_binding: "aws_sdk_iotsitewise.types.computation_model_data_binding.ComputationModelDataBinding",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        computation_model_description: Optional[
            "aws_sdk_iotsitewise.types.restricted_description.RestrictedDescription"
        ] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.update_computation_model_response.UpdateComputationModelResponse":
        """<p>Updates the computation model.</p>

        Args:
            computation_model_id: <p>The ID of the computation model.</p>
            computation_model_name: <p>The name of the computation model.</p>
            computation_model_description: <p>The description of the computation model.</p>
            computation_model_configuration: <p>The configuration for the computation model.</p>
            computation_model_data_binding: <p>The data binding for the computation model. Key is a variable name defined in configuration. Value is a <code>ComputationModelDataBindingValue</code> referenced by the variable.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.update_computation_model_request.UpdateComputationModelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.update_computation_model_response.UpdateComputationModelResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.update_computation_model

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.update_computation_model.async_update_computation_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.update_computation_model_request.UpdateComputationModelRequest = {}  # type: ignore[typeddict-item]
        input_["computation_model_id"] = computation_model_id
        input_["computation_model_name"] = computation_model_name
        if computation_model_description is not None:
            input_["computation_model_description"] = computation_model_description
        input_["computation_model_configuration"] = computation_model_configuration
        input_["computation_model_data_binding"] = computation_model_data_binding
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_dashboard(
        self,
        dashboard_id: "aws_sdk_iotsitewise.types.id.ID",
        dashboard_name: "aws_sdk_iotsitewise.types.name.Name",
        dashboard_definition: "aws_sdk_iotsitewise.types.dashboard_definition.DashboardDefinition",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        dashboard_description: Optional[
            "aws_sdk_iotsitewise.types.description.Description"
        ] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.update_dashboard_response.UpdateDashboardResponse":
        """<p>Updates an IoT SiteWise Monitor dashboard.</p>

        Args:
            dashboard_id: <p>The ID of the dashboard to update.</p>
            dashboard_name: <p>A new friendly name for the dashboard.</p>
            dashboard_description: <p>A new description for the dashboard.</p>
            dashboard_definition: <p>The new dashboard definition, as specified in a JSON literal.</p> <ul> <li> <p>IoT SiteWise Monitor (Classic) see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboards-using-aws-cli.html\">Create dashboards (CLI)</a> </p> </li> <li> <p>IoT SiteWise Monitor (AI-aware) see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboards-ai-dashboard-cli.html\">Create dashboards (CLI)</a> </p> </li> </ul> <p>in the <i>IoT SiteWise User Guide</i> </p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.update_dashboard_request.UpdateDashboardRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.update_dashboard_response.UpdateDashboardResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.update_dashboard

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.update_dashboard.async_update_dashboard(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.update_dashboard_request.UpdateDashboardRequest = {}  # type: ignore[typeddict-item]
        input_["dashboard_id"] = dashboard_id
        input_["dashboard_name"] = dashboard_name
        if dashboard_description is not None:
            input_["dashboard_description"] = dashboard_description
        input_["dashboard_definition"] = dashboard_definition
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_dataset(
        self,
        dataset_id: "aws_sdk_iotsitewise.types.id.ID",
        dataset_name: "aws_sdk_iotsitewise.types.restricted_name.RestrictedName",
        dataset_source: "aws_sdk_iotsitewise.types.dataset_source.DatasetSource",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        dataset_description: Optional[
            "aws_sdk_iotsitewise.types.restricted_description.RestrictedDescription"
        ] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.update_dataset_response.UpdateDatasetResponse":
        """<p>Updates a dataset.</p>

        Args:
            dataset_id: <p>The ID of the dataset.</p>
            dataset_name: <p>The name of the dataset.</p>
            dataset_description: <p>A description about the dataset, and its functionality.</p>
            dataset_source: <p>The data source for the dataset.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.update_dataset_request.UpdateDatasetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.update_dataset_response.UpdateDatasetResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.update_dataset

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.update_dataset.async_update_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.update_dataset_request.UpdateDatasetRequest = {}  # type: ignore[typeddict-item]
        input_["dataset_id"] = dataset_id
        input_["dataset_name"] = dataset_name
        if dataset_description is not None:
            input_["dataset_description"] = dataset_description
        input_["dataset_source"] = dataset_source
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_gateway(
        self,
        gateway_id: "aws_sdk_iotsitewise.types.id.ID",
        gateway_name: "aws_sdk_iotsitewise.types.gateway_name.GatewayName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> None:
        """<p>Updates a gateway's name.</p>

        Args:
            gateway_id: <p>The ID of the gateway to update.</p>
            gateway_name: <p>A unique name for the gateway.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.update_gateway_request.UpdateGatewayRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.update_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.update_gateway.async_update_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.update_gateway_request.UpdateGatewayRequest = {}  # type: ignore[typeddict-item]
        input_["gateway_id"] = gateway_id
        input_["gateway_name"] = gateway_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_gateway_capability_configuration(
        self,
        gateway_id: "aws_sdk_iotsitewise.types.id.ID",
        capability_namespace: "aws_sdk_iotsitewise.types.capability_namespace.CapabilityNamespace",
        capability_configuration: "aws_sdk_iotsitewise.types.capability_configuration.CapabilityConfiguration",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "aws_sdk_iotsitewise.types.update_gateway_capability_configuration_response.UpdateGatewayCapabilityConfigurationResponse":
        """<p>Updates a gateway capability configuration or defines a new capability configuration. Each gateway capability defines data sources for a gateway.</p> <p>Important workflow notes:</p> <p>Each gateway capability defines data sources for a gateway. This is the namespace of the gateway capability.</p> <p>. The namespace follows the format <code>service:capability:version</code>, where:</p> <ul> <li> <p> <code>service</code> - The service providing the capability, or <code>iotsitewise</code>.</p> </li> <li> <p> <code>capability</code> - The specific capability type. Options include: <code>opcuacollector</code> for the OPC UA data source collector, or <code>publisher</code> for data publisher capability.</p> </li> <li> <p> <code>version</code> - The version number of the capability. Option include <code>2</code> for Classic streams, V2 gateways, and <code>3</code> for MQTT-enabled, V3 gateways.</p> </li> </ul> <p>After updating a capability configuration, the sync status becomes <code>OUT_OF_SYNC</code> until the gateway processes the configuration.Use <code>DescribeGatewayCapabilityConfiguration</code> to check the sync status and verify the configuration was applied.</p> <p>A gateway can have multiple capability configurations with different namespaces.</p>

        Args:
            gateway_id: <p>The ID of the gateway to be updated.</p>
            capability_namespace: <p>The namespace of the gateway capability configuration to be updated. For example, if you configure OPC UA sources for an MQTT-enabled gateway, your OPC-UA capability configuration has the namespace <code>iotsitewise:opcuacollector:3</code>.</p>
            capability_configuration: <p>The JSON document that defines the configuration for the gateway capability. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/configure-sources.html#configure-source-cli\">Configuring data sources (CLI)</a> in the <i>IoT SiteWise User Guide</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.update_gateway_capability_configuration_request.UpdateGatewayCapabilityConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.update_gateway_capability_configuration_response.UpdateGatewayCapabilityConfigurationResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.update_gateway_capability_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.update_gateway_capability_configuration.async_update_gateway_capability_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.update_gateway_capability_configuration_request.UpdateGatewayCapabilityConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["gateway_id"] = gateway_id
        input_["capability_namespace"] = capability_namespace
        input_["capability_configuration"] = capability_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_portal(
        self,
        portal_id: "aws_sdk_iotsitewise.types.id.ID",
        portal_name: "aws_sdk_iotsitewise.types.name.Name",
        portal_contact_email: "aws_sdk_iotsitewise.types.email.Email",
        role_arn: "aws_sdk_iotsitewise.types.iam_arn.IamArn",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        portal_description: Optional[
            "aws_sdk_iotsitewise.types.description.Description"
        ] = None,
        portal_logo_image: Optional["aws_sdk_iotsitewise.types.image.Image"] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
        notification_sender_email: Optional[
            "aws_sdk_iotsitewise.types.email.Email"
        ] = None,
        alarms: Optional["aws_sdk_iotsitewise.types.alarms.Alarms"] = None,
        portal_type: Optional[
            "aws_sdk_iotsitewise.types.portal_type.PortalType"
        ] = None,
        portal_type_configuration: Optional[
            "aws_sdk_iotsitewise.types.portal_type_configuration.PortalTypeConfiguration"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.update_portal_response.UpdatePortalResponse":
        """<p>Updates an IoT SiteWise Monitor portal.</p>

        Args:
            portal_id: <p>The ID of the portal to update.</p>
            portal_name: <p>A new friendly name for the portal.</p>
            portal_description: <p>A new description for the portal.</p>
            portal_contact_email: <p>The Amazon Web Services administrator's contact email address.</p>
            role_arn: <p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of a service role that allows the portal's users to access your IoT SiteWise resources on your behalf. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-service-role.html\">Using service roles for IoT SiteWise Monitor</a> in the <i>IoT SiteWise User Guide</i>.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            notification_sender_email: <p>The email address that sends alarm notifications.</p>
            alarms: <p>Contains the configuration information of an alarm created in an IoT SiteWise Monitor portal. You can use the alarm to monitor an asset property and get notified when the asset property value is outside a specified range. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/appguide/monitor-alarms.html\">Monitoring with alarms</a> in the <i>IoT SiteWise Application Guide</i>.</p>
            portal_type: <p>Define the type of portal. The value for IoT SiteWise Monitor (Classic) is <code>SITEWISE_PORTAL_V1</code>. The value for IoT SiteWise Monitor (AI-aware) is <code>SITEWISE_PORTAL_V2</code>.</p>
            portal_type_configuration: <p>The configuration entry associated with the specific portal type. The value for IoT SiteWise Monitor (Classic) is <code>SITEWISE_PORTAL_V1</code>. The value for IoT SiteWise Monitor (AI-aware) is <code>SITEWISE_PORTAL_V2</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.update_portal_request.UpdatePortalRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.update_portal_response.UpdatePortalResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.update_portal

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.update_portal.async_update_portal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.update_portal_request.UpdatePortalRequest = {}  # type: ignore[typeddict-item]
        input_["portal_id"] = portal_id
        input_["portal_name"] = portal_name
        if portal_description is not None:
            input_["portal_description"] = portal_description
        input_["portal_contact_email"] = portal_contact_email
        if portal_logo_image is not None:
            input_["portal_logo_image"] = portal_logo_image
        input_["role_arn"] = role_arn
        if client_token is not None:
            input_["client_token"] = client_token
        if notification_sender_email is not None:
            input_["notification_sender_email"] = notification_sender_email
        if alarms is not None:
            input_["alarms"] = alarms
        if portal_type is not None:
            input_["portal_type"] = portal_type
        if portal_type_configuration is not None:
            input_["portal_type_configuration"] = portal_type_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_project(
        self,
        project_id: "aws_sdk_iotsitewise.types.id.ID",
        project_name: "aws_sdk_iotsitewise.types.name.Name",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        project_description: Optional[
            "aws_sdk_iotsitewise.types.description.Description"
        ] = None,
        client_token: Optional[
            "aws_sdk_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_iotsitewise.types.update_project_response.UpdateProjectResponse":
        """<p>Updates an IoT SiteWise Monitor project.</p>

        Args:
            project_id: <p>The ID of the project to update.</p>
            project_name: <p>A new friendly name for the project.</p>
            project_description: <p>A new description for the project.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotsitewise.types.update_project_request.UpdateProjectRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotsitewise.types.update_project_response.UpdateProjectResponse"
        ]:
            import aws_sdk_iotsitewise._operations.aws_io_t_site_wise.update_project

            (
                output,
                http_response,
            ) = await aws_sdk_iotsitewise._operations.aws_io_t_site_wise.update_project.async_update_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsitewise.types.update_project_request.UpdateProjectRequest = {}  # type: ignore[typeddict-item]
        input_["project_id"] = project_id
        input_["project_name"] = project_name
        if project_description is not None:
            input_["project_description"] = project_description
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
