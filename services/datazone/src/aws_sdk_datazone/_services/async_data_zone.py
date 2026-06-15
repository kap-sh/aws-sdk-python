"""Generated from Smithy shape ``com.amazonaws.datazone#DataZone``."""

import datetime
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_datazone._auth._signers
import aws_sdk_datazone._auth._sigv4
from aws_sdk_datazone._auth._identity import Credentials
from aws_sdk_datazone._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_datazone._auth._zapros_handler import AuthMiddleware
from aws_sdk_datazone._pagination import resolve_path as _resolve_path
from aws_sdk_datazone._resources.data_zone.asset import AsyncAsset
from aws_sdk_datazone._resources.data_zone.asset_type import AsyncAssetType
from aws_sdk_datazone._resources.data_zone.data_product import AsyncDataProduct
from aws_sdk_datazone._resources.data_zone.data_source import AsyncDataSource
from aws_sdk_datazone._resources.data_zone.data_source_run import AsyncDataSourceRun
from aws_sdk_datazone._resources.data_zone.domain import AsyncDomain
from aws_sdk_datazone._resources.data_zone.domain_unit import AsyncDomainUnit
from aws_sdk_datazone._resources.data_zone.environment_blueprint_configuration import (
    AsyncEnvironmentBlueprintConfiguration,
)
from aws_sdk_datazone._resources.data_zone.form_type import AsyncFormType
from aws_sdk_datazone._resources.data_zone.glossary import AsyncGlossary
from aws_sdk_datazone._resources.data_zone.glossary_term import AsyncGlossaryTerm
from aws_sdk_datazone._resources.data_zone.listing import AsyncListing
from aws_sdk_datazone._resources.data_zone.metadata_generation_run import (
    AsyncMetadataGenerationRun,
)
from aws_sdk_datazone._resources.data_zone.notebook import AsyncNotebook
from aws_sdk_datazone._resources.data_zone.notebook_export import AsyncNotebookExport
from aws_sdk_datazone._resources.data_zone.notebook_run import AsyncNotebookRun
from aws_sdk_datazone._resources.data_zone.rule import AsyncRule
from aws_sdk_datazone._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_datazone.types.accept_choices
    import aws_sdk_datazone.types.accept_predictions_input
    import aws_sdk_datazone.types.accept_predictions_output
    import aws_sdk_datazone.types.accept_rule
    import aws_sdk_datazone.types.accept_subscription_request_input
    import aws_sdk_datazone.types.accept_subscription_request_output
    import aws_sdk_datazone.types.accepted_asset_scopes
    import aws_sdk_datazone.types.account_info
    import aws_sdk_datazone.types.account_pool_id
    import aws_sdk_datazone.types.account_pool_name
    import aws_sdk_datazone.types.account_pool_summary
    import aws_sdk_datazone.types.account_source
    import aws_sdk_datazone.types.action_parameters
    import aws_sdk_datazone.types.add_entity_owner_input
    import aws_sdk_datazone.types.add_entity_owner_output
    import aws_sdk_datazone.types.add_policy_grant_input
    import aws_sdk_datazone.types.add_policy_grant_output
    import aws_sdk_datazone.types.additional_attributes
    import aws_sdk_datazone.types.aggregation_list
    import aws_sdk_datazone.types.applicable_asset_types
    import aws_sdk_datazone.types.asset_filter_configuration
    import aws_sdk_datazone.types.asset_filter_summary
    import aws_sdk_datazone.types.asset_id
    import aws_sdk_datazone.types.asset_identifier
    import aws_sdk_datazone.types.asset_permissions
    import aws_sdk_datazone.types.asset_target_names
    import aws_sdk_datazone.types.associate_environment_role_input
    import aws_sdk_datazone.types.associate_environment_role_output
    import aws_sdk_datazone.types.associate_governed_terms_input
    import aws_sdk_datazone.types.associate_governed_terms_output
    import aws_sdk_datazone.types.attribute_entity_type
    import aws_sdk_datazone.types.attributes
    import aws_sdk_datazone.types.attributes_list
    import aws_sdk_datazone.types.authorized_principal_identifiers
    import aws_sdk_datazone.types.aws_account_id
    import aws_sdk_datazone.types.aws_location
    import aws_sdk_datazone.types.aws_region
    import aws_sdk_datazone.types.batch_get_attributes_metadata_input
    import aws_sdk_datazone.types.batch_get_attributes_metadata_output
    import aws_sdk_datazone.types.batch_put_attributes_metadata_input
    import aws_sdk_datazone.types.batch_put_attributes_metadata_output
    import aws_sdk_datazone.types.cancel_subscription_input
    import aws_sdk_datazone.types.cancel_subscription_output
    import aws_sdk_datazone.types.change_action
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.configurations
    import aws_sdk_datazone.types.connection_id
    import aws_sdk_datazone.types.connection_name
    import aws_sdk_datazone.types.connection_properties_input
    import aws_sdk_datazone.types.connection_properties_patch
    import aws_sdk_datazone.types.connection_scope
    import aws_sdk_datazone.types.connection_summary
    import aws_sdk_datazone.types.connection_type
    import aws_sdk_datazone.types.create_account_pool_input
    import aws_sdk_datazone.types.create_account_pool_output
    import aws_sdk_datazone.types.create_asset_filter_input
    import aws_sdk_datazone.types.create_asset_filter_output
    import aws_sdk_datazone.types.create_connection_input
    import aws_sdk_datazone.types.create_connection_output
    import aws_sdk_datazone.types.create_environment_action_input
    import aws_sdk_datazone.types.create_environment_action_output
    import aws_sdk_datazone.types.create_environment_blueprint_input
    import aws_sdk_datazone.types.create_environment_blueprint_output
    import aws_sdk_datazone.types.create_environment_input
    import aws_sdk_datazone.types.create_environment_output
    import aws_sdk_datazone.types.create_environment_profile_input
    import aws_sdk_datazone.types.create_environment_profile_output
    import aws_sdk_datazone.types.create_group_profile_input
    import aws_sdk_datazone.types.create_group_profile_output
    import aws_sdk_datazone.types.create_listing_change_set_input
    import aws_sdk_datazone.types.create_listing_change_set_output
    import aws_sdk_datazone.types.create_project_input
    import aws_sdk_datazone.types.create_project_membership_input
    import aws_sdk_datazone.types.create_project_membership_output
    import aws_sdk_datazone.types.create_project_output
    import aws_sdk_datazone.types.create_project_profile_input
    import aws_sdk_datazone.types.create_project_profile_output
    import aws_sdk_datazone.types.create_subscription_grant_input
    import aws_sdk_datazone.types.create_subscription_grant_output
    import aws_sdk_datazone.types.create_subscription_request_input
    import aws_sdk_datazone.types.create_subscription_request_output
    import aws_sdk_datazone.types.create_subscription_target_input
    import aws_sdk_datazone.types.create_subscription_target_output
    import aws_sdk_datazone.types.create_user_profile_input
    import aws_sdk_datazone.types.create_user_profile_output
    import aws_sdk_datazone.types.custom_parameter_list
    import aws_sdk_datazone.types.data_asset_activity_status
    import aws_sdk_datazone.types.data_product_id
    import aws_sdk_datazone.types.data_product_revision
    import aws_sdk_datazone.types.data_source_run_activity
    import aws_sdk_datazone.types.data_source_run_id
    import aws_sdk_datazone.types.data_zone_entity_type
    import aws_sdk_datazone.types.decision_comment
    import aws_sdk_datazone.types.delete_account_pool_input
    import aws_sdk_datazone.types.delete_account_pool_output
    import aws_sdk_datazone.types.delete_asset_filter_input
    import aws_sdk_datazone.types.delete_connection_input
    import aws_sdk_datazone.types.delete_connection_output
    import aws_sdk_datazone.types.delete_data_export_configuration_input
    import aws_sdk_datazone.types.delete_data_export_configuration_output
    import aws_sdk_datazone.types.delete_environment_action_input
    import aws_sdk_datazone.types.delete_environment_blueprint_input
    import aws_sdk_datazone.types.delete_environment_input
    import aws_sdk_datazone.types.delete_environment_profile_input
    import aws_sdk_datazone.types.delete_project_input
    import aws_sdk_datazone.types.delete_project_membership_input
    import aws_sdk_datazone.types.delete_project_membership_output
    import aws_sdk_datazone.types.delete_project_output
    import aws_sdk_datazone.types.delete_project_profile_input
    import aws_sdk_datazone.types.delete_project_profile_output
    import aws_sdk_datazone.types.delete_subscription_grant_input
    import aws_sdk_datazone.types.delete_subscription_grant_output
    import aws_sdk_datazone.types.delete_subscription_request_input
    import aws_sdk_datazone.types.delete_subscription_target_input
    import aws_sdk_datazone.types.delete_time_series_data_points_input
    import aws_sdk_datazone.types.delete_time_series_data_points_output
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.disassociate_environment_role_input
    import aws_sdk_datazone.types.disassociate_environment_role_output
    import aws_sdk_datazone.types.disassociate_governed_terms_input
    import aws_sdk_datazone.types.disassociate_governed_terms_output
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.domain_unit_id
    import aws_sdk_datazone.types.edge_direction
    import aws_sdk_datazone.types.encryption_configuration
    import aws_sdk_datazone.types.entity_id
    import aws_sdk_datazone.types.entity_identifier
    import aws_sdk_datazone.types.entity_type
    import aws_sdk_datazone.types.environment_action_summary
    import aws_sdk_datazone.types.environment_blueprint_id
    import aws_sdk_datazone.types.environment_blueprint_name
    import aws_sdk_datazone.types.environment_blueprint_summary
    import aws_sdk_datazone.types.environment_configuration_name
    import aws_sdk_datazone.types.environment_configuration_user_parameters_list
    import aws_sdk_datazone.types.environment_configurations_list
    import aws_sdk_datazone.types.environment_deployment_details
    import aws_sdk_datazone.types.environment_id
    import aws_sdk_datazone.types.environment_parameters_list
    import aws_sdk_datazone.types.environment_profile_id
    import aws_sdk_datazone.types.environment_profile_name
    import aws_sdk_datazone.types.environment_profile_summary
    import aws_sdk_datazone.types.environment_status
    import aws_sdk_datazone.types.environment_summary
    import aws_sdk_datazone.types.failure_cause
    import aws_sdk_datazone.types.filter_clause
    import aws_sdk_datazone.types.filter_id
    import aws_sdk_datazone.types.filter_name
    import aws_sdk_datazone.types.filter_status
    import aws_sdk_datazone.types.get_account_pool_input
    import aws_sdk_datazone.types.get_account_pool_output
    import aws_sdk_datazone.types.get_asset_filter_input
    import aws_sdk_datazone.types.get_asset_filter_output
    import aws_sdk_datazone.types.get_connection_input
    import aws_sdk_datazone.types.get_connection_output
    import aws_sdk_datazone.types.get_data_export_configuration_input
    import aws_sdk_datazone.types.get_data_export_configuration_output
    import aws_sdk_datazone.types.get_environment_action_input
    import aws_sdk_datazone.types.get_environment_action_output
    import aws_sdk_datazone.types.get_environment_blueprint_input
    import aws_sdk_datazone.types.get_environment_blueprint_output
    import aws_sdk_datazone.types.get_environment_credentials_input
    import aws_sdk_datazone.types.get_environment_credentials_output
    import aws_sdk_datazone.types.get_environment_input
    import aws_sdk_datazone.types.get_environment_output
    import aws_sdk_datazone.types.get_environment_profile_input
    import aws_sdk_datazone.types.get_environment_profile_output
    import aws_sdk_datazone.types.get_group_profile_input
    import aws_sdk_datazone.types.get_group_profile_output
    import aws_sdk_datazone.types.get_iam_portal_login_url_input
    import aws_sdk_datazone.types.get_iam_portal_login_url_output
    import aws_sdk_datazone.types.get_job_run_input
    import aws_sdk_datazone.types.get_job_run_output
    import aws_sdk_datazone.types.get_lineage_event_input
    import aws_sdk_datazone.types.get_lineage_event_output
    import aws_sdk_datazone.types.get_lineage_node_input
    import aws_sdk_datazone.types.get_lineage_node_output
    import aws_sdk_datazone.types.get_project_input
    import aws_sdk_datazone.types.get_project_output
    import aws_sdk_datazone.types.get_project_profile_input
    import aws_sdk_datazone.types.get_project_profile_output
    import aws_sdk_datazone.types.get_subscription_grant_input
    import aws_sdk_datazone.types.get_subscription_grant_output
    import aws_sdk_datazone.types.get_subscription_input
    import aws_sdk_datazone.types.get_subscription_output
    import aws_sdk_datazone.types.get_subscription_request_details_input
    import aws_sdk_datazone.types.get_subscription_request_details_output
    import aws_sdk_datazone.types.get_subscription_target_input
    import aws_sdk_datazone.types.get_subscription_target_output
    import aws_sdk_datazone.types.get_time_series_data_point_input
    import aws_sdk_datazone.types.get_time_series_data_point_output
    import aws_sdk_datazone.types.get_user_profile_input
    import aws_sdk_datazone.types.get_user_profile_output
    import aws_sdk_datazone.types.glossary_terms
    import aws_sdk_datazone.types.governed_entity_type
    import aws_sdk_datazone.types.governed_glossary_terms
    import aws_sdk_datazone.types.grant_identifier
    import aws_sdk_datazone.types.granted_entity_input
    import aws_sdk_datazone.types.group_identifier
    import aws_sdk_datazone.types.group_profile_id
    import aws_sdk_datazone.types.group_profile_status
    import aws_sdk_datazone.types.group_profile_summary
    import aws_sdk_datazone.types.group_search_text
    import aws_sdk_datazone.types.group_search_type
    import aws_sdk_datazone.types.iam_principal_arn
    import aws_sdk_datazone.types.iam_role_arn
    import aws_sdk_datazone.types.inventory_search_scope
    import aws_sdk_datazone.types.job_run_status
    import aws_sdk_datazone.types.job_run_summary
    import aws_sdk_datazone.types.lineage_event
    import aws_sdk_datazone.types.lineage_event_identifier
    import aws_sdk_datazone.types.lineage_event_processing_status
    import aws_sdk_datazone.types.lineage_event_summary
    import aws_sdk_datazone.types.lineage_node_identifier
    import aws_sdk_datazone.types.lineage_node_summary
    import aws_sdk_datazone.types.list_account_pools_input
    import aws_sdk_datazone.types.list_account_pools_output
    import aws_sdk_datazone.types.list_accounts_in_account_pool_input
    import aws_sdk_datazone.types.list_accounts_in_account_pool_output
    import aws_sdk_datazone.types.list_asset_filters_input
    import aws_sdk_datazone.types.list_asset_filters_output
    import aws_sdk_datazone.types.list_asset_revisions_input
    import aws_sdk_datazone.types.list_asset_revisions_output
    import aws_sdk_datazone.types.list_connections_input
    import aws_sdk_datazone.types.list_connections_output
    import aws_sdk_datazone.types.list_data_product_revisions_input
    import aws_sdk_datazone.types.list_data_product_revisions_output
    import aws_sdk_datazone.types.list_data_source_run_activities_input
    import aws_sdk_datazone.types.list_data_source_run_activities_output
    import aws_sdk_datazone.types.list_entity_owners_input
    import aws_sdk_datazone.types.list_entity_owners_output
    import aws_sdk_datazone.types.list_environment_actions_input
    import aws_sdk_datazone.types.list_environment_actions_output
    import aws_sdk_datazone.types.list_environment_blueprints_input
    import aws_sdk_datazone.types.list_environment_blueprints_output
    import aws_sdk_datazone.types.list_environment_profiles_input
    import aws_sdk_datazone.types.list_environment_profiles_output
    import aws_sdk_datazone.types.list_environments_input
    import aws_sdk_datazone.types.list_environments_output
    import aws_sdk_datazone.types.list_job_runs_input
    import aws_sdk_datazone.types.list_job_runs_output
    import aws_sdk_datazone.types.list_lineage_events_input
    import aws_sdk_datazone.types.list_lineage_events_output
    import aws_sdk_datazone.types.list_lineage_node_history_input
    import aws_sdk_datazone.types.list_lineage_node_history_output
    import aws_sdk_datazone.types.list_notifications_input
    import aws_sdk_datazone.types.list_notifications_output
    import aws_sdk_datazone.types.list_policy_grants_input
    import aws_sdk_datazone.types.list_policy_grants_output
    import aws_sdk_datazone.types.list_project_memberships_input
    import aws_sdk_datazone.types.list_project_memberships_output
    import aws_sdk_datazone.types.list_project_profiles_input
    import aws_sdk_datazone.types.list_project_profiles_output
    import aws_sdk_datazone.types.list_projects_input
    import aws_sdk_datazone.types.list_projects_output
    import aws_sdk_datazone.types.list_subscription_grants_input
    import aws_sdk_datazone.types.list_subscription_grants_output
    import aws_sdk_datazone.types.list_subscription_requests_input
    import aws_sdk_datazone.types.list_subscription_requests_output
    import aws_sdk_datazone.types.list_subscription_targets_input
    import aws_sdk_datazone.types.list_subscription_targets_output
    import aws_sdk_datazone.types.list_subscriptions_input
    import aws_sdk_datazone.types.list_subscriptions_output
    import aws_sdk_datazone.types.list_tags_for_resource_request
    import aws_sdk_datazone.types.list_tags_for_resource_response
    import aws_sdk_datazone.types.list_time_series_data_points_input
    import aws_sdk_datazone.types.list_time_series_data_points_output
    import aws_sdk_datazone.types.listing_id
    import aws_sdk_datazone.types.managed_policy_type
    import aws_sdk_datazone.types.match_clauses
    import aws_sdk_datazone.types.max_results
    import aws_sdk_datazone.types.max_results_for_list_domains
    import aws_sdk_datazone.types.member
    import aws_sdk_datazone.types.metadata_form_inputs
    import aws_sdk_datazone.types.notebook_name
    import aws_sdk_datazone.types.notification_output
    import aws_sdk_datazone.types.notification_subjects
    import aws_sdk_datazone.types.notification_type
    import aws_sdk_datazone.types.owner_properties
    import aws_sdk_datazone.types.owner_properties_output
    import aws_sdk_datazone.types.pagination_token
    import aws_sdk_datazone.types.policy_grant_detail
    import aws_sdk_datazone.types.policy_grant_member
    import aws_sdk_datazone.types.policy_grant_principal
    import aws_sdk_datazone.types.post_lineage_event_input
    import aws_sdk_datazone.types.post_lineage_event_output
    import aws_sdk_datazone.types.post_time_series_data_points_input
    import aws_sdk_datazone.types.post_time_series_data_points_output
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.project_member
    import aws_sdk_datazone.types.project_membership_assignments
    import aws_sdk_datazone.types.project_name
    import aws_sdk_datazone.types.project_profile_id
    import aws_sdk_datazone.types.project_profile_name
    import aws_sdk_datazone.types.project_profile_summary
    import aws_sdk_datazone.types.project_resource_tag_parameters
    import aws_sdk_datazone.types.project_summary
    import aws_sdk_datazone.types.provisioning_properties
    import aws_sdk_datazone.types.put_data_export_configuration_input
    import aws_sdk_datazone.types.put_data_export_configuration_output
    import aws_sdk_datazone.types.query_graph_input
    import aws_sdk_datazone.types.query_graph_output
    import aws_sdk_datazone.types.reject_choices
    import aws_sdk_datazone.types.reject_predictions_input
    import aws_sdk_datazone.types.reject_predictions_output
    import aws_sdk_datazone.types.reject_rule
    import aws_sdk_datazone.types.reject_subscription_request_input
    import aws_sdk_datazone.types.reject_subscription_request_output
    import aws_sdk_datazone.types.remove_entity_owner_input
    import aws_sdk_datazone.types.remove_entity_owner_output
    import aws_sdk_datazone.types.remove_policy_grant_input
    import aws_sdk_datazone.types.remove_policy_grant_output
    import aws_sdk_datazone.types.request_reason
    import aws_sdk_datazone.types.resolution_strategy
    import aws_sdk_datazone.types.result_item
    import aws_sdk_datazone.types.revision
    import aws_sdk_datazone.types.revoke_subscription_input
    import aws_sdk_datazone.types.revoke_subscription_output
    import aws_sdk_datazone.types.role_arn
    import aws_sdk_datazone.types.run_identifier
    import aws_sdk_datazone.types.search_group_profiles_input
    import aws_sdk_datazone.types.search_group_profiles_output
    import aws_sdk_datazone.types.search_in_list
    import aws_sdk_datazone.types.search_input
    import aws_sdk_datazone.types.search_inventory_result_item
    import aws_sdk_datazone.types.search_listings_input
    import aws_sdk_datazone.types.search_listings_output
    import aws_sdk_datazone.types.search_output
    import aws_sdk_datazone.types.search_output_additional_attributes
    import aws_sdk_datazone.types.search_result_item
    import aws_sdk_datazone.types.search_sort
    import aws_sdk_datazone.types.search_text
    import aws_sdk_datazone.types.search_types_input
    import aws_sdk_datazone.types.search_types_output
    import aws_sdk_datazone.types.search_types_result_item
    import aws_sdk_datazone.types.search_user_profiles_input
    import aws_sdk_datazone.types.search_user_profiles_output
    import aws_sdk_datazone.types.sort_field_account_pool
    import aws_sdk_datazone.types.sort_field_connection
    import aws_sdk_datazone.types.sort_field_project
    import aws_sdk_datazone.types.sort_key
    import aws_sdk_datazone.types.sort_order
    import aws_sdk_datazone.types.source_location
    import aws_sdk_datazone.types.start_notebook_import_input
    import aws_sdk_datazone.types.start_notebook_import_output
    import aws_sdk_datazone.types.status
    import aws_sdk_datazone.types.subscribed_listing_inputs
    import aws_sdk_datazone.types.subscribed_principal_inputs
    import aws_sdk_datazone.types.subscription_grant_creation_mode
    import aws_sdk_datazone.types.subscription_grant_id
    import aws_sdk_datazone.types.subscription_grant_status
    import aws_sdk_datazone.types.subscription_grant_summary
    import aws_sdk_datazone.types.subscription_id
    import aws_sdk_datazone.types.subscription_request_id
    import aws_sdk_datazone.types.subscription_request_status
    import aws_sdk_datazone.types.subscription_request_summary
    import aws_sdk_datazone.types.subscription_status
    import aws_sdk_datazone.types.subscription_summary
    import aws_sdk_datazone.types.subscription_target_forms
    import aws_sdk_datazone.types.subscription_target_id
    import aws_sdk_datazone.types.subscription_target_name
    import aws_sdk_datazone.types.subscription_target_summary
    import aws_sdk_datazone.types.tag_key_list
    import aws_sdk_datazone.types.tag_resource_request
    import aws_sdk_datazone.types.tag_resource_response
    import aws_sdk_datazone.types.tags
    import aws_sdk_datazone.types.target_entity_type
    import aws_sdk_datazone.types.task_status
    import aws_sdk_datazone.types.time_series_data_point_form_input_list
    import aws_sdk_datazone.types.time_series_data_point_identifier
    import aws_sdk_datazone.types.time_series_data_point_summary_form_output
    import aws_sdk_datazone.types.time_series_entity_type
    import aws_sdk_datazone.types.time_series_form_name
    import aws_sdk_datazone.types.types_search_scope
    import aws_sdk_datazone.types.untag_resource_request
    import aws_sdk_datazone.types.untag_resource_response
    import aws_sdk_datazone.types.update_account_pool_input
    import aws_sdk_datazone.types.update_account_pool_output
    import aws_sdk_datazone.types.update_asset_filter_input
    import aws_sdk_datazone.types.update_asset_filter_output
    import aws_sdk_datazone.types.update_connection_input
    import aws_sdk_datazone.types.update_connection_output
    import aws_sdk_datazone.types.update_environment_action_input
    import aws_sdk_datazone.types.update_environment_action_output
    import aws_sdk_datazone.types.update_environment_blueprint_input
    import aws_sdk_datazone.types.update_environment_blueprint_output
    import aws_sdk_datazone.types.update_environment_input
    import aws_sdk_datazone.types.update_environment_output
    import aws_sdk_datazone.types.update_environment_profile_input
    import aws_sdk_datazone.types.update_environment_profile_output
    import aws_sdk_datazone.types.update_group_profile_input
    import aws_sdk_datazone.types.update_group_profile_output
    import aws_sdk_datazone.types.update_project_input
    import aws_sdk_datazone.types.update_project_output
    import aws_sdk_datazone.types.update_project_profile_input
    import aws_sdk_datazone.types.update_project_profile_output
    import aws_sdk_datazone.types.update_root_domain_unit_owner_input
    import aws_sdk_datazone.types.update_root_domain_unit_owner_output
    import aws_sdk_datazone.types.update_subscription_grant_status_input
    import aws_sdk_datazone.types.update_subscription_grant_status_output
    import aws_sdk_datazone.types.update_subscription_request_input
    import aws_sdk_datazone.types.update_subscription_request_output
    import aws_sdk_datazone.types.update_subscription_target_input
    import aws_sdk_datazone.types.update_subscription_target_output
    import aws_sdk_datazone.types.update_user_profile_input
    import aws_sdk_datazone.types.update_user_profile_output
    import aws_sdk_datazone.types.user_designation
    import aws_sdk_datazone.types.user_identifier
    import aws_sdk_datazone.types.user_profile_id
    import aws_sdk_datazone.types.user_profile_status
    import aws_sdk_datazone.types.user_profile_summary
    import aws_sdk_datazone.types.user_profile_type
    import aws_sdk_datazone.types.user_search_text
    import aws_sdk_datazone.types.user_search_type
    import aws_sdk_datazone.types.user_type


class AsyncDataZoneClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
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


class AsyncDataZoneClient:
    """A client for the ``DataZone`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
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
        self._config = AsyncDataZoneClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "region": region,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

        # resources
        self.asset = AsyncAsset(self)
        self.asset_type = AsyncAssetType(self)
        self.data_product = AsyncDataProduct(self)
        self.data_source = AsyncDataSource(self)
        self.data_source_run = AsyncDataSourceRun(self)
        self.domain = AsyncDomain(self)
        self.domain_unit = AsyncDomainUnit(self)
        self.environment_blueprint_configuration = (
            AsyncEnvironmentBlueprintConfiguration(self)
        )
        self.form_type = AsyncFormType(self)
        self.glossary = AsyncGlossary(self)
        self.glossary_term = AsyncGlossaryTerm(self)
        self.listing = AsyncListing(self)
        self.metadata_generation_run = AsyncMetadataGenerationRun(self)
        self.notebook = AsyncNotebook(self)
        self.notebook_export = AsyncNotebookExport(self)
        self.notebook_run = AsyncNotebookRun(self)
        self.rule = AsyncRule(self)

    def operation_options(
        self, config_overrides: Optional[AsyncDataZoneClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncDataZoneClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def accept_predictions(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.asset_identifier.AssetIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        revision: Optional["aws_sdk_datazone.types.revision.Revision"] = None,
        accept_rule: Optional["aws_sdk_datazone.types.accept_rule.AcceptRule"] = None,
        accept_choices: Optional[
            "aws_sdk_datazone.types.accept_choices.AcceptChoices"
        ] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.accept_predictions_output.AcceptPredictionsOutput":
        """<p>Accepts automatically generated business-friendly metadata for your Amazon DataZone assets.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            identifier: <p>The identifier of the asset.</p>
            revision: <p>The revision that is to be made to the asset.</p>
            accept_rule: <p>Specifies the rule (or the conditions) under which a prediction can be accepted.</p>
            accept_choices: <p>Specifies the prediction (aka, the automatically generated piece of metadata) and the target (for example, a column name) that can be accepted.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.accept_predictions_input.AcceptPredictionsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.accept_predictions_output.AcceptPredictionsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.accept_predictions

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.accept_predictions.async_accept_predictions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.accept_predictions_input.AcceptPredictionsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        if revision is not None:
            input_["revision"] = revision
        if accept_rule is not None:
            input_["accept_rule"] = accept_rule
        if accept_choices is not None:
            input_["accept_choices"] = accept_choices
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def accept_subscription_request(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.subscription_request_id.SubscriptionRequestId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        decision_comment: Optional[
            "aws_sdk_datazone.types.decision_comment.DecisionComment"
        ] = None,
        asset_scopes: Optional[
            "aws_sdk_datazone.types.accepted_asset_scopes.AcceptedAssetScopes"
        ] = None,
        asset_permissions: Optional[
            "aws_sdk_datazone.types.asset_permissions.AssetPermissions"
        ] = None,
    ) -> "aws_sdk_datazone.types.accept_subscription_request_output.AcceptSubscriptionRequestOutput":
        """<p>Accepts a subscription request to a specific asset. </p>

        Args:
            domain_identifier: <p>The Amazon DataZone domain where the specified subscription request is being accepted.</p>
            identifier: <p>The unique identifier of the subscription request that is to be accepted.</p>
            decision_comment: <p>A description that specifies the reason for accepting the specified subscription request.</p>
            asset_scopes: <p>The asset scopes of the accept subscription request.</p>
            asset_permissions: <p>The asset permissions of the accept subscription request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.accept_subscription_request_input.AcceptSubscriptionRequestInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.accept_subscription_request_output.AcceptSubscriptionRequestOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.accept_subscription_request

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.accept_subscription_request.async_accept_subscription_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.accept_subscription_request_input.AcceptSubscriptionRequestInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        if decision_comment is not None:
            input_["decision_comment"] = decision_comment
        if asset_scopes is not None:
            input_["asset_scopes"] = asset_scopes
        if asset_permissions is not None:
            input_["asset_permissions"] = asset_permissions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def add_entity_owner(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        entity_type: "aws_sdk_datazone.types.data_zone_entity_type.DataZoneEntityType",
        entity_identifier: str,
        owner: "aws_sdk_datazone.types.owner_properties.OwnerProperties",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.add_entity_owner_output.AddEntityOwnerOutput":
        """<p>Adds the owner of an entity (a domain unit).</p>

        Args:
            domain_identifier: <p>The ID of the domain in which you want to add the entity owner.</p>
            entity_type: <p>The type of an entity.</p>
            entity_identifier: <p>The ID of the entity to which you want to add an owner.</p>
            owner: <p>The owner that you want to add to the entity.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.add_entity_owner_input.AddEntityOwnerInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.add_entity_owner_output.AddEntityOwnerOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.add_entity_owner

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.add_entity_owner.async_add_entity_owner(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.add_entity_owner_input.AddEntityOwnerInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["entity_type"] = entity_type
        input_["entity_identifier"] = entity_identifier
        input_["owner"] = owner
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def add_policy_grant(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        entity_type: "aws_sdk_datazone.types.target_entity_type.TargetEntityType",
        entity_identifier: str,
        policy_type: "aws_sdk_datazone.types.managed_policy_type.ManagedPolicyType",
        principal: "aws_sdk_datazone.types.policy_grant_principal.PolicyGrantPrincipal",
        detail: "aws_sdk_datazone.types.policy_grant_detail.PolicyGrantDetail",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.add_policy_grant_output.AddPolicyGrantOutput":
        """<p>Adds a policy grant (an authorization policy) to a specified entity, including domain units, environment blueprint configurations, or environment profiles.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to add a policy grant.</p>
            entity_type: <p>The type of entity (resource) to which the grant is added.</p>
            entity_identifier: <p>The ID of the entity (resource) to which you want to add a policy grant.</p>
            policy_type: <p>The type of policy that you want to grant.</p>
            principal: <p>The principal to whom the permissions are granted.</p>
            detail: <p>The details of the policy grant.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.add_policy_grant_input.AddPolicyGrantInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.add_policy_grant_output.AddPolicyGrantOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.add_policy_grant

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.add_policy_grant.async_add_policy_grant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.add_policy_grant_input.AddPolicyGrantInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["entity_type"] = entity_type
        input_["entity_identifier"] = entity_identifier
        input_["policy_type"] = policy_type
        input_["principal"] = principal
        input_["detail"] = detail
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_environment_role(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        environment_identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId",
        environment_role_arn: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.associate_environment_role_output.AssociateEnvironmentRoleOutput":
        """<p>Associates the environment role in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the environment role is associated.</p>
            environment_identifier: <p>The ID of the Amazon DataZone environment.</p>
            environment_role_arn: <p>The ARN of the environment role.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.associate_environment_role_input.AssociateEnvironmentRoleInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.associate_environment_role_output.AssociateEnvironmentRoleOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.associate_environment_role

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.associate_environment_role.async_associate_environment_role(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.associate_environment_role_input.AssociateEnvironmentRoleInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["environment_identifier"] = environment_identifier
        input_["environment_role_arn"] = environment_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_governed_terms(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        entity_identifier: "aws_sdk_datazone.types.entity_identifier.EntityIdentifier",
        entity_type: "aws_sdk_datazone.types.governed_entity_type.GovernedEntityType",
        governed_glossary_terms: "aws_sdk_datazone.types.governed_glossary_terms.GovernedGlossaryTerms",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.associate_governed_terms_output.AssociateGovernedTermsOutput":
        """<p>Associates governed terms with an asset.</p>

        Args:
            domain_identifier: <p>The ID of the domain where governed terms are to be associated with an asset.</p>
            entity_identifier: <p>The ID of the asset with which you want to associate a governed term.</p>
            entity_type: <p>The type of the asset with which you want to associate a governed term.</p>
            governed_glossary_terms: <p>The glossary terms in a restricted glossary.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.associate_governed_terms_input.AssociateGovernedTermsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.associate_governed_terms_output.AssociateGovernedTermsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.associate_governed_terms

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.associate_governed_terms.async_associate_governed_terms(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.associate_governed_terms_input.AssociateGovernedTermsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["entity_identifier"] = entity_identifier
        input_["entity_type"] = entity_type
        input_["governed_glossary_terms"] = governed_glossary_terms

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_attributes_metadata(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        entity_type: "aws_sdk_datazone.types.attribute_entity_type.AttributeEntityType",
        entity_identifier: "aws_sdk_datazone.types.entity_id.EntityId",
        attribute_identifiers: "aws_sdk_datazone.types.attributes_list.AttributesList",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        entity_revision: Optional["aws_sdk_datazone.types.revision.Revision"] = None,
    ) -> "aws_sdk_datazone.types.batch_get_attributes_metadata_output.BatchGetAttributesMetadataOutput":
        """<p>Gets the attribute metadata.</p>

        Args:
            domain_identifier: <p>The domain ID where you want to get the attribute metadata.</p>
            entity_type: <p>The entity type for which you want to get attribute metadata.</p>
            entity_identifier: <p>The entity ID for which you want to get attribute metadata.</p>
            entity_revision: <p>The entity revision for which you want to get attribute metadata.</p>
            attribute_identifiers: <p>The attribute identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.batch_get_attributes_metadata_input.BatchGetAttributesMetadataInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.batch_get_attributes_metadata_output.BatchGetAttributesMetadataOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.batch_get_attributes_metadata

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.batch_get_attributes_metadata.async_batch_get_attributes_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.batch_get_attributes_metadata_input.BatchGetAttributesMetadataInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["entity_type"] = entity_type
        input_["entity_identifier"] = entity_identifier
        if entity_revision is not None:
            input_["entity_revision"] = entity_revision
        input_["attribute_identifiers"] = attribute_identifiers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_put_attributes_metadata(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        entity_type: "aws_sdk_datazone.types.attribute_entity_type.AttributeEntityType",
        entity_identifier: "aws_sdk_datazone.types.entity_id.EntityId",
        attributes: "aws_sdk_datazone.types.attributes.Attributes",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.batch_put_attributes_metadata_output.BatchPutAttributesMetadataOutput":
        """<p>Writes the attribute metadata.</p>

        Args:
            domain_identifier: <p>The domain ID where you want to write the attribute metadata.</p>
            entity_type: <p>The entity type for which you want to write the attribute metadata.</p>
            entity_identifier: <p>The entity ID for which you want to write the attribute metadata.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>
            attributes: <p>The attributes of the metadata.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.batch_put_attributes_metadata_input.BatchPutAttributesMetadataInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.batch_put_attributes_metadata_output.BatchPutAttributesMetadataOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.batch_put_attributes_metadata

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.batch_put_attributes_metadata.async_batch_put_attributes_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.batch_put_attributes_metadata_input.BatchPutAttributesMetadataInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["entity_type"] = entity_type
        input_["entity_identifier"] = entity_identifier
        if client_token is not None:
            input_["client_token"] = client_token
        input_["attributes"] = attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_subscription(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.subscription_id.SubscriptionId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.cancel_subscription_output.CancelSubscriptionOutput":
        """<p>Cancels the subscription to the specified asset.</p>

        Args:
            domain_identifier: <p>The unique identifier of the Amazon DataZone domain where the subscription request is being cancelled.</p>
            identifier: <p>The unique identifier of the subscription that is being cancelled.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.cancel_subscription_input.CancelSubscriptionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.cancel_subscription_output.CancelSubscriptionOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.cancel_subscription

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.cancel_subscription.async_cancel_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.cancel_subscription_input.CancelSubscriptionInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_account_pool(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        name: "aws_sdk_datazone.types.account_pool_name.AccountPoolName",
        resolution_strategy: "aws_sdk_datazone.types.resolution_strategy.ResolutionStrategy",
        account_source: "aws_sdk_datazone.types.account_source.AccountSource",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional["aws_sdk_datazone.types.description.Description"] = None,
    ) -> "aws_sdk_datazone.types.create_account_pool_output.CreateAccountPoolOutput":
        """<p>Creates an account pool. </p>

        Args:
            domain_identifier: <p>The ID of the domain where the account pool is created.</p>
            name: <p>The name of the account pool.</p>
            description: <p>The description of the account pool.</p>
            resolution_strategy: <p>The mechanism used to resolve the account selection from the account pool.</p>
            account_source: <p>The source of accounts for the account pool. In the current release, it's either a static list of accounts provided by the customer or a custom Amazon Web Services Lambda handler. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.create_account_pool_input.CreateAccountPoolInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.create_account_pool_output.CreateAccountPoolOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_account_pool

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.create_account_pool.async_create_account_pool(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.create_account_pool_input.CreateAccountPoolInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["resolution_strategy"] = resolution_strategy
        input_["account_source"] = account_source

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_asset_filter(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        asset_identifier: "aws_sdk_datazone.types.asset_id.AssetId",
        name: "aws_sdk_datazone.types.filter_name.FilterName",
        configuration: "aws_sdk_datazone.types.asset_filter_configuration.AssetFilterConfiguration",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional["aws_sdk_datazone.types.description.Description"] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_datazone.types.create_asset_filter_output.CreateAssetFilterOutput":
        """<p>Creates a data asset filter.</p> <p>Asset filters provide a sophisticated way to create controlled views of data assets by selecting specific columns or applying row-level filters. This capability is crucial for organizations that need to share data while maintaining security and privacy controls. For example, your database might be filtered to show only non-PII fields to certain users, or sales data might be filtered by region for different regional teams. Asset filters enable fine-grained access control while maintaining a single source of truth.</p> <p>Prerequisites:</p> <ul> <li> <p>A valid domain (<code>--domain-identifier</code>) must exist. </p> </li> <li> <p>A data asset (<code>--asset-identifier</code>) must already be created under that domain.</p> </li> <li> <p>The asset must have the referenced columns available in its schema for column-based filtering.</p> </li> <li> <p>You cannot specify both (<code>columnConfiguration</code>, <code>rowConfiguration</code>)at the same time.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the domain in which you want to create an asset filter.</p>
            asset_identifier: <p>The ID of the data asset.</p>
            name: <p>The name of the asset filter.</p>
            description: <p>The description of the asset filter.</p>
            configuration: <p>The configuration of the asset filter.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.create_asset_filter_input.CreateAssetFilterInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.create_asset_filter_output.CreateAssetFilterOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_asset_filter

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.create_asset_filter.async_create_asset_filter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.create_asset_filter_input.CreateAssetFilterInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["asset_identifier"] = asset_identifier
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["configuration"] = configuration
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_connection(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        name: "aws_sdk_datazone.types.connection_name.ConnectionName",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        aws_location: Optional[
            "aws_sdk_datazone.types.aws_location.AwsLocation"
        ] = None,
        client_token: Optional[str] = None,
        configurations: Optional[
            "aws_sdk_datazone.types.configurations.Configurations"
        ] = None,
        description: Optional["aws_sdk_datazone.types.description.Description"] = None,
        environment_identifier: Optional[
            "aws_sdk_datazone.types.environment_id.EnvironmentId"
        ] = None,
        props: Optional[
            "aws_sdk_datazone.types.connection_properties_input.ConnectionPropertiesInput"
        ] = None,
        enable_trusted_identity_propagation: Optional[bool] = None,
        scope: Optional[
            "aws_sdk_datazone.types.connection_scope.ConnectionScope"
        ] = None,
    ) -> "aws_sdk_datazone.types.create_connection_output.CreateConnectionOutput":
        """<p>Creates a new connection. In Amazon DataZone, a connection enables you to connect your resources (domains, projects, and environments) to external resources and services.</p>

        Args:
            aws_location: <p>The location where the connection is created.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
            configurations: <p>The configurations of the connection.</p>
            description: <p>A connection description.</p>
            domain_identifier: <p>The ID of the domain where the connection is created.</p>
            environment_identifier: <p>The ID of the environment where the connection is created.</p>
            name: <p>The connection name.</p>
            props: <p>The connection props.</p>
            enable_trusted_identity_propagation: <p>Specifies whether the trusted identity propagation is enabled.</p>
            scope: <p>The scope of the connection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.create_connection_input.CreateConnectionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.create_connection_output.CreateConnectionOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_connection

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.create_connection.async_create_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.create_connection_input.CreateConnectionInput = {}  # type: ignore[typeddict-item]
        if aws_location is not None:
            input_["aws_location"] = aws_location
        if client_token is not None:
            input_["client_token"] = client_token
        if configurations is not None:
            input_["configurations"] = configurations
        if description is not None:
            input_["description"] = description
        input_["domain_identifier"] = domain_identifier
        if environment_identifier is not None:
            input_["environment_identifier"] = environment_identifier
        input_["name"] = name
        if props is not None:
            input_["props"] = props
        if enable_trusted_identity_propagation is not None:
            input_["enable_trusted_identity_propagation"] = (
                enable_trusted_identity_propagation
            )
        if scope is not None:
            input_["scope"] = scope

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_environment(
        self,
        project_identifier: "aws_sdk_datazone.types.project_id.ProjectId",
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        name: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional[str] = None,
        environment_profile_identifier: Optional[
            "aws_sdk_datazone.types.environment_profile_id.EnvironmentProfileId"
        ] = None,
        user_parameters: Optional[
            "aws_sdk_datazone.types.environment_parameters_list.EnvironmentParametersList"
        ] = None,
        glossary_terms: Optional[
            "aws_sdk_datazone.types.glossary_terms.GlossaryTerms"
        ] = None,
        environment_account_identifier: Optional[str] = None,
        environment_account_region: Optional[str] = None,
        environment_blueprint_identifier: Optional[str] = None,
        deployment_order: Optional[int] = None,
        environment_configuration_id: Optional[str] = None,
        environment_configuration_name: Optional[
            "aws_sdk_datazone.types.environment_configuration_name.EnvironmentConfigurationName"
        ] = None,
    ) -> "aws_sdk_datazone.types.create_environment_output.CreateEnvironmentOutput":
        """<p>Create an Amazon DataZone environment.</p>

        Args:
            project_identifier: <p>The identifier of the Amazon DataZone project in which this environment is created.</p>
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which the environment is created.</p>
            description: <p>The description of the Amazon DataZone environment.</p>
            name: <p>The name of the Amazon DataZone environment.</p>
            environment_profile_identifier: <p>The identifier of the environment profile that is used to create this Amazon DataZone environment.</p>
            user_parameters: <p>The user parameters of this Amazon DataZone environment.</p>
            glossary_terms: <p>The glossary terms that can be used in this Amazon DataZone environment.</p>
            environment_account_identifier: <p>The ID of the account in which the environment is being created.</p>
            environment_account_region: <p>The region of the account in which the environment is being created.</p>
            environment_blueprint_identifier: <p>The ID of the blueprint with which the environment is being created.</p>
            deployment_order: <p>The deployment order of the environment.</p>
            environment_configuration_id: <p>The configuration ID of the environment.</p>
            environment_configuration_name: <p>The configuration name of the environment.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.create_environment_input.CreateEnvironmentInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.create_environment_output.CreateEnvironmentOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_environment

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.create_environment.async_create_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.create_environment_input.CreateEnvironmentInput = {}  # type: ignore[typeddict-item]
        input_["project_identifier"] = project_identifier
        input_["domain_identifier"] = domain_identifier
        if description is not None:
            input_["description"] = description
        input_["name"] = name
        if environment_profile_identifier is not None:
            input_["environment_profile_identifier"] = environment_profile_identifier
        if user_parameters is not None:
            input_["user_parameters"] = user_parameters
        if glossary_terms is not None:
            input_["glossary_terms"] = glossary_terms
        if environment_account_identifier is not None:
            input_["environment_account_identifier"] = environment_account_identifier
        if environment_account_region is not None:
            input_["environment_account_region"] = environment_account_region
        if environment_blueprint_identifier is not None:
            input_["environment_blueprint_identifier"] = (
                environment_blueprint_identifier
            )
        if deployment_order is not None:
            input_["deployment_order"] = deployment_order
        if environment_configuration_id is not None:
            input_["environment_configuration_id"] = environment_configuration_id
        if environment_configuration_name is not None:
            input_["environment_configuration_name"] = environment_configuration_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_environment_action(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        environment_identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId",
        name: str,
        parameters: "aws_sdk_datazone.types.action_parameters.ActionParameters",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional[str] = None,
    ) -> "aws_sdk_datazone.types.create_environment_action_output.CreateEnvironmentActionOutput":
        """<p>Creates an action for the environment, for example, creates a console link for an analytics tool that is available in this environment.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the environment action is created.</p>
            environment_identifier: <p>The ID of the environment in which the environment action is created.</p>
            name: <p>The name of the environment action.</p>
            parameters: <p>The parameters of the environment action.</p>
            description: <p>The description of the environment action that is being created in the environment.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.create_environment_action_input.CreateEnvironmentActionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.create_environment_action_output.CreateEnvironmentActionOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_environment_action

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.create_environment_action.async_create_environment_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.create_environment_action_input.CreateEnvironmentActionInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["environment_identifier"] = environment_identifier
        input_["name"] = name
        input_["parameters"] = parameters
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_environment_blueprint(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        name: "aws_sdk_datazone.types.environment_blueprint_name.EnvironmentBlueprintName",
        provisioning_properties: "aws_sdk_datazone.types.provisioning_properties.ProvisioningProperties",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional["aws_sdk_datazone.types.description.Description"] = None,
        user_parameters: Optional[
            "aws_sdk_datazone.types.custom_parameter_list.CustomParameterList"
        ] = None,
    ) -> "aws_sdk_datazone.types.create_environment_blueprint_output.CreateEnvironmentBlueprintOutput":
        """<p>Creates a Amazon DataZone blueprint.</p>

        Args:
            domain_identifier: <p>The identifier of the domain in which this blueprint is created.</p>
            name: <p>The name of this Amazon DataZone blueprint.</p>
            description: <p>The description of the Amazon DataZone blueprint.</p>
            provisioning_properties: <p>The provisioning properties of this Amazon DataZone blueprint.</p>
            user_parameters: <p>The user parameters of this Amazon DataZone blueprint.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.create_environment_blueprint_input.CreateEnvironmentBlueprintInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.create_environment_blueprint_output.CreateEnvironmentBlueprintOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_environment_blueprint

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.create_environment_blueprint.async_create_environment_blueprint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.create_environment_blueprint_input.CreateEnvironmentBlueprintInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["provisioning_properties"] = provisioning_properties
        if user_parameters is not None:
            input_["user_parameters"] = user_parameters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_environment_profile(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        name: "aws_sdk_datazone.types.environment_profile_name.EnvironmentProfileName",
        environment_blueprint_identifier: "aws_sdk_datazone.types.environment_blueprint_id.EnvironmentBlueprintId",
        project_identifier: "aws_sdk_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional["aws_sdk_datazone.types.description.Description"] = None,
        user_parameters: Optional[
            "aws_sdk_datazone.types.environment_parameters_list.EnvironmentParametersList"
        ] = None,
        aws_account_id: Optional[
            "aws_sdk_datazone.types.aws_account_id.AwsAccountId"
        ] = None,
        aws_account_region: Optional[
            "aws_sdk_datazone.types.aws_region.AwsRegion"
        ] = None,
    ) -> "aws_sdk_datazone.types.create_environment_profile_output.CreateEnvironmentProfileOutput":
        """<p>Creates an Amazon DataZone environment profile.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this environment profile is created.</p>
            name: <p>The name of this Amazon DataZone environment profile.</p>
            description: <p>The description of this Amazon DataZone environment profile.</p>
            environment_blueprint_identifier: <p>The ID of the blueprint with which this environment profile is created.</p>
            project_identifier: <p>The identifier of the project in which to create the environment profile.</p>
            user_parameters: <p>The user parameters of this Amazon DataZone environment profile.</p>
            aws_account_id: <p>The Amazon Web Services account in which the Amazon DataZone environment is created.</p>
            aws_account_region: <p>The Amazon Web Services region in which this environment profile is created.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.create_environment_profile_input.CreateEnvironmentProfileInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.create_environment_profile_output.CreateEnvironmentProfileOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_environment_profile

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.create_environment_profile.async_create_environment_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.create_environment_profile_input.CreateEnvironmentProfileInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["environment_blueprint_identifier"] = environment_blueprint_identifier
        input_["project_identifier"] = project_identifier
        if user_parameters is not None:
            input_["user_parameters"] = user_parameters
        if aws_account_id is not None:
            input_["aws_account_id"] = aws_account_id
        if aws_account_region is not None:
            input_["aws_account_region"] = aws_account_region

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_group_profile(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        group_identifier: Optional[
            "aws_sdk_datazone.types.group_identifier.GroupIdentifier"
        ] = None,
        role_principal_arn: Optional[str] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_datazone.types.create_group_profile_output.CreateGroupProfileOutput":
        """<p>Creates a group profile in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which the group profile is created.</p>
            group_identifier: <p>The identifier of the group for which the group profile is created.</p>
            role_principal_arn: <p>The ARN of the IAM role that will be associated with the group profile. This role defines the permissions that group members will assume when accessing Amazon DataZone resources.</p>
            client_token: <p> A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.create_group_profile_input.CreateGroupProfileInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.create_group_profile_output.CreateGroupProfileOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_group_profile

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.create_group_profile.async_create_group_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.create_group_profile_input.CreateGroupProfileInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        if group_identifier is not None:
            input_["group_identifier"] = group_identifier
        if role_principal_arn is not None:
            input_["role_principal_arn"] = role_principal_arn
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_listing_change_set(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        entity_identifier: "aws_sdk_datazone.types.entity_identifier.EntityIdentifier",
        entity_type: "aws_sdk_datazone.types.entity_type.EntityType",
        action: "aws_sdk_datazone.types.change_action.ChangeAction",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        entity_revision: Optional["aws_sdk_datazone.types.revision.Revision"] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.create_listing_change_set_output.CreateListingChangeSetOutput":
        """<p>Publishes a listing (a record of an asset at a given time) or removes a listing from the catalog. </p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain.</p>
            entity_identifier: <p>The ID of the asset.</p>
            entity_type: <p>The type of an entity.</p>
            entity_revision: <p>The revision of an asset.</p>
            action: <p>Specifies whether to publish or unpublish a listing.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.create_listing_change_set_input.CreateListingChangeSetInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.create_listing_change_set_output.CreateListingChangeSetOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_listing_change_set

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.create_listing_change_set.async_create_listing_change_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.create_listing_change_set_input.CreateListingChangeSetInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["entity_identifier"] = entity_identifier
        input_["entity_type"] = entity_type
        if entity_revision is not None:
            input_["entity_revision"] = entity_revision
        input_["action"] = action
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_project(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        name: "aws_sdk_datazone.types.project_name.ProjectName",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional["aws_sdk_datazone.types.description.Description"] = None,
        resource_tags: Optional["aws_sdk_datazone.types.tags.Tags"] = None,
        glossary_terms: Optional[
            "aws_sdk_datazone.types.glossary_terms.GlossaryTerms"
        ] = None,
        domain_unit_id: Optional[
            "aws_sdk_datazone.types.domain_unit_id.DomainUnitId"
        ] = None,
        project_profile_id: Optional[
            "aws_sdk_datazone.types.project_profile_id.ProjectProfileId"
        ] = None,
        user_parameters: Optional[
            "aws_sdk_datazone.types.environment_configuration_user_parameters_list.EnvironmentConfigurationUserParametersList"
        ] = None,
        project_category: Optional[str] = None,
        project_execution_role: Optional[
            "aws_sdk_datazone.types.role_arn.RoleArn"
        ] = None,
        membership_assignments: Optional[
            "aws_sdk_datazone.types.project_membership_assignments.ProjectMembershipAssignments"
        ] = None,
    ) -> "aws_sdk_datazone.types.create_project_output.CreateProjectOutput":
        """<p>Creates an Amazon DataZone project.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this project is created.</p>
            name: <p>The name of the Amazon DataZone project.</p>
            description: <p>The description of the Amazon DataZone project.</p>
            resource_tags: <p>The resource tags of the project.</p>
            glossary_terms: <p>The glossary terms that can be used in this Amazon DataZone project.</p>
            domain_unit_id: <p>The ID of the domain unit. This parameter is not required and if it is not specified, then the project is created at the root domain unit level.</p>
            project_profile_id: <p>The ID of the project profile.</p>
            user_parameters: <p>The user parameters of the project.</p>
            project_category: <p>The category of the project. Set to 'ADMIN' designates this as an administrative project for the Amazon DataZone domain.</p>
            project_execution_role: <p>The default project IAM role that is used to access project resources and run computes such as Glue and Sagemaker.</p>
            membership_assignments: <p>The members to be assigned to the project.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.create_project_input.CreateProjectInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.create_project_output.CreateProjectOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_project

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.create_project.async_create_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.create_project_input.CreateProjectInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags
        if glossary_terms is not None:
            input_["glossary_terms"] = glossary_terms
        if domain_unit_id is not None:
            input_["domain_unit_id"] = domain_unit_id
        if project_profile_id is not None:
            input_["project_profile_id"] = project_profile_id
        if user_parameters is not None:
            input_["user_parameters"] = user_parameters
        if project_category is not None:
            input_["project_category"] = project_category
        if project_execution_role is not None:
            input_["project_execution_role"] = project_execution_role
        if membership_assignments is not None:
            input_["membership_assignments"] = membership_assignments

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_project_membership(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        project_identifier: "aws_sdk_datazone.types.project_id.ProjectId",
        member: "aws_sdk_datazone.types.member.Member",
        designation: "aws_sdk_datazone.types.user_designation.UserDesignation",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.create_project_membership_output.CreateProjectMembershipOutput":
        """<p>Creates a project membership in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which project membership is created.</p>
            project_identifier: <p>The ID of the project for which this project membership was created.</p>
            member: <p>The project member whose project membership was created.</p>
            designation: <p>The designation of the project membership.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.create_project_membership_input.CreateProjectMembershipInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.create_project_membership_output.CreateProjectMembershipOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_project_membership

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.create_project_membership.async_create_project_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.create_project_membership_input.CreateProjectMembershipInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["project_identifier"] = project_identifier
        input_["member"] = member
        input_["designation"] = designation

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_project_profile(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        name: "aws_sdk_datazone.types.project_profile_name.ProjectProfileName",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional["aws_sdk_datazone.types.description.Description"] = None,
        status: Optional["aws_sdk_datazone.types.status.Status"] = None,
        project_resource_tags: Optional[
            "aws_sdk_datazone.types.project_resource_tag_parameters.ProjectResourceTagParameters"
        ] = None,
        allow_custom_project_resource_tags: Optional[bool] = None,
        project_resource_tags_description: Optional[
            "aws_sdk_datazone.types.description.Description"
        ] = None,
        environment_configurations: Optional[
            "aws_sdk_datazone.types.environment_configurations_list.EnvironmentConfigurationsList"
        ] = None,
        domain_unit_identifier: Optional[
            "aws_sdk_datazone.types.domain_unit_id.DomainUnitId"
        ] = None,
    ) -> "aws_sdk_datazone.types.create_project_profile_output.CreateProjectProfileOutput":
        """<p>Creates a project profile.</p>

        Args:
            domain_identifier: <p>A domain ID of the project profile.</p>
            name: <p>Project profile name.</p>
            description: <p>A description of a project profile.</p>
            status: <p>Project profile status.</p>
            project_resource_tags: <p>The resource tags of the project profile.</p>
            allow_custom_project_resource_tags: <p>Specifies whether custom project resource tags are supported.</p>
            project_resource_tags_description: <p>Field viewable through the UI that provides a project user with the allowed resource tag specifications.</p>
            environment_configurations: <p>Environment configurations of the project profile.</p>
            domain_unit_identifier: <p>A domain unit ID of the project profile.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.create_project_profile_input.CreateProjectProfileInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.create_project_profile_output.CreateProjectProfileOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_project_profile

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.create_project_profile.async_create_project_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.create_project_profile_input.CreateProjectProfileInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status
        if project_resource_tags is not None:
            input_["project_resource_tags"] = project_resource_tags
        if allow_custom_project_resource_tags is not None:
            input_["allow_custom_project_resource_tags"] = (
                allow_custom_project_resource_tags
            )
        if project_resource_tags_description is not None:
            input_["project_resource_tags_description"] = (
                project_resource_tags_description
            )
        if environment_configurations is not None:
            input_["environment_configurations"] = environment_configurations
        if domain_unit_identifier is not None:
            input_["domain_unit_identifier"] = domain_unit_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_subscription_grant(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        environment_identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId",
        granted_entity: "aws_sdk_datazone.types.granted_entity_input.GrantedEntityInput",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        subscription_target_identifier: Optional[
            "aws_sdk_datazone.types.subscription_target_id.SubscriptionTargetId"
        ] = None,
        asset_target_names: Optional[
            "aws_sdk_datazone.types.asset_target_names.AssetTargetNames"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_datazone.types.create_subscription_grant_output.CreateSubscriptionGrantOutput":
        """<p>Creates a subsscription grant in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the subscription grant is created.</p>
            environment_identifier: <p>The ID of the environment in which the subscription grant is created.</p>
            subscription_target_identifier: <p>The ID of the subscription target for which the subscription grant is created.</p>
            granted_entity: <p>The entity to which the subscription is to be granted.</p>
            asset_target_names: <p>The names of the assets for which the subscription grant is created.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.create_subscription_grant_input.CreateSubscriptionGrantInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.create_subscription_grant_output.CreateSubscriptionGrantOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_subscription_grant

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.create_subscription_grant.async_create_subscription_grant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.create_subscription_grant_input.CreateSubscriptionGrantInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["environment_identifier"] = environment_identifier
        if subscription_target_identifier is not None:
            input_["subscription_target_identifier"] = subscription_target_identifier
        input_["granted_entity"] = granted_entity
        if asset_target_names is not None:
            input_["asset_target_names"] = asset_target_names
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_subscription_request(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        subscribed_principals: "aws_sdk_datazone.types.subscribed_principal_inputs.SubscribedPrincipalInputs",
        subscribed_listings: "aws_sdk_datazone.types.subscribed_listing_inputs.SubscribedListingInputs",
        request_reason: "aws_sdk_datazone.types.request_reason.RequestReason",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional[str] = None,
        metadata_forms: Optional[
            "aws_sdk_datazone.types.metadata_form_inputs.MetadataFormInputs"
        ] = None,
        asset_permissions: Optional[
            "aws_sdk_datazone.types.asset_permissions.AssetPermissions"
        ] = None,
        asset_scopes: Optional[
            "aws_sdk_datazone.types.accepted_asset_scopes.AcceptedAssetScopes"
        ] = None,
    ) -> "aws_sdk_datazone.types.create_subscription_request_output.CreateSubscriptionRequestOutput":
        """<p>Creates a subscription request in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the subscription request is created.</p>
            subscribed_principals: <p>The Amazon DataZone principals for whom the subscription request is created.</p>
            subscribed_listings: <p>The published asset for which the subscription grant is to be created.</p>
            request_reason: <p>The reason for the subscription request.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
            metadata_forms: <p>The metadata form included in the subscription request.</p>
            asset_permissions: <p>The asset permissions of the subscription request.</p>
            asset_scopes: <p>The asset scopes of the subscription request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.create_subscription_request_input.CreateSubscriptionRequestInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.create_subscription_request_output.CreateSubscriptionRequestOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_subscription_request

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.create_subscription_request.async_create_subscription_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.create_subscription_request_input.CreateSubscriptionRequestInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["subscribed_principals"] = subscribed_principals
        input_["subscribed_listings"] = subscribed_listings
        input_["request_reason"] = request_reason
        if client_token is not None:
            input_["client_token"] = client_token
        if metadata_forms is not None:
            input_["metadata_forms"] = metadata_forms
        if asset_permissions is not None:
            input_["asset_permissions"] = asset_permissions
        if asset_scopes is not None:
            input_["asset_scopes"] = asset_scopes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_subscription_target(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        environment_identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId",
        name: "aws_sdk_datazone.types.subscription_target_name.SubscriptionTargetName",
        type: str,
        subscription_target_config: "aws_sdk_datazone.types.subscription_target_forms.SubscriptionTargetForms",
        authorized_principals: "aws_sdk_datazone.types.authorized_principal_identifiers.AuthorizedPrincipalIdentifiers",
        manage_access_role: "aws_sdk_datazone.types.iam_role_arn.IamRoleArn",
        applicable_asset_types: "aws_sdk_datazone.types.applicable_asset_types.ApplicableAssetTypes",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        provider: Optional[str] = None,
        client_token: Optional[str] = None,
        subscription_grant_creation_mode: Optional[
            "aws_sdk_datazone.types.subscription_grant_creation_mode.SubscriptionGrantCreationMode"
        ] = None,
    ) -> "aws_sdk_datazone.types.create_subscription_target_output.CreateSubscriptionTargetOutput":
        """<p>Creates a subscription target in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which subscription target is created.</p>
            environment_identifier: <p>The ID of the environment in which subscription target is created.</p>
            name: <p>The name of the subscription target.</p>
            type: <p>The type of the subscription target.</p>
            subscription_target_config: <p>The configuration of the subscription target.</p>
            authorized_principals: <p>The authorized principals of the subscription target.</p>
            manage_access_role: <p>The manage access role that is used to create the subscription target.</p>
            applicable_asset_types: <p>The asset types that can be included in the subscription target.</p>
            provider: <p>The provider of the subscription target.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
            subscription_grant_creation_mode: <p> Determines the subscription grant creation mode for this target, defining if grants are auto-created upon subscription approval or managed manually. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.create_subscription_target_input.CreateSubscriptionTargetInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.create_subscription_target_output.CreateSubscriptionTargetOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_subscription_target

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.create_subscription_target.async_create_subscription_target(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.create_subscription_target_input.CreateSubscriptionTargetInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["environment_identifier"] = environment_identifier
        input_["name"] = name
        input_["type"] = type
        input_["subscription_target_config"] = subscription_target_config
        input_["authorized_principals"] = authorized_principals
        input_["manage_access_role"] = manage_access_role
        input_["applicable_asset_types"] = applicable_asset_types
        if provider is not None:
            input_["provider"] = provider
        if client_token is not None:
            input_["client_token"] = client_token
        if subscription_grant_creation_mode is not None:
            input_["subscription_grant_creation_mode"] = (
                subscription_grant_creation_mode
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_user_profile(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        user_identifier: "aws_sdk_datazone.types.user_identifier.UserIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        user_type: Optional["aws_sdk_datazone.types.user_type.UserType"] = None,
        session_name: Optional[str] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_datazone.types.create_user_profile_output.CreateUserProfileOutput":
        """<p>Creates a user profile in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which a user profile is created.</p>
            user_identifier: <p>The identifier of the user for which the user profile is created.</p>
            user_type: <p>The user type of the user for which the user profile is created.</p>
            session_name: <p>The session name for IAM role sessions.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.create_user_profile_input.CreateUserProfileInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.create_user_profile_output.CreateUserProfileOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_user_profile

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.create_user_profile.async_create_user_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.create_user_profile_input.CreateUserProfileInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["user_identifier"] = user_identifier
        if user_type is not None:
            input_["user_type"] = user_type
        if session_name is not None:
            input_["session_name"] = session_name
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_account_pool(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.account_pool_id.AccountPoolId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.delete_account_pool_output.DeleteAccountPoolOutput":
        """<p>Deletes an account pool.</p>

        Args:
            domain_identifier: <p>The ID of the domain where the account pool is deleted.</p>
            identifier: <p>The ID of the account pool to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.delete_account_pool_input.DeleteAccountPoolInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.delete_account_pool_output.DeleteAccountPoolOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.delete_account_pool

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.delete_account_pool.async_delete_account_pool(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.delete_account_pool_input.DeleteAccountPoolInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_asset_filter(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        asset_identifier: "aws_sdk_datazone.types.asset_id.AssetId",
        identifier: "aws_sdk_datazone.types.filter_id.FilterId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> None:
        """<p>Deletes an asset filter.</p> <p>Prerequisites:</p> <ul> <li> <p>The asset filter must exist. </p> </li> <li> <p>The domain and asset must not have been deleted.</p> </li> <li> <p>Ensure the --identifier refers to a valid filter ID.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the domain where you want to delete an asset filter.</p>
            asset_identifier: <p>The ID of the data asset.</p>
            identifier: <p>The ID of the asset filter that you want to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.delete_asset_filter_input.DeleteAssetFilterInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_datazone._operations.data_zone.delete_asset_filter

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.delete_asset_filter.async_delete_asset_filter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.delete_asset_filter_input.DeleteAssetFilterInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["asset_identifier"] = asset_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_connection(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.delete_connection_output.DeleteConnectionOutput":
        """<p>Deletes and connection. In Amazon DataZone, a connection enables you to connect your resources (domains, projects, and environments) to external resources and services.</p>

        Args:
            domain_identifier: <p>The ID of the domain where the connection is deleted.</p>
            identifier: <p>The ID of the connection that is deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.delete_connection_input.DeleteConnectionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.delete_connection_output.DeleteConnectionOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.delete_connection

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.delete_connection.async_delete_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.delete_connection_input.DeleteConnectionInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_data_export_configuration(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.delete_data_export_configuration_output.DeleteDataExportConfigurationOutput":
        """<p>Deletes data export configuration for a domain.</p> <p>This operation does not delete the S3 table created by the PutDataExportConfiguration operation.</p> <p>To temporarily disable export without deleting the configuration, use the PutDataExportConfiguration operation with the <code>--no-enable-export</code> flag instead. This allows you to re-enable export for the same domain using the <code>--enable-export</code> flag without deleting S3 table.</p>

        Args:
            domain_identifier: <p>The domain ID for which you want to delete the data export configuration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.delete_data_export_configuration_input.DeleteDataExportConfigurationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.delete_data_export_configuration_output.DeleteDataExportConfigurationOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.delete_data_export_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.delete_data_export_configuration.async_delete_data_export_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.delete_data_export_configuration_input.DeleteDataExportConfigurationInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_environment(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> None:
        """<p>Deletes an environment in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the environment is deleted.</p>
            identifier: <p>The identifier of the environment that is to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.delete_environment_input.DeleteEnvironmentInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_datazone._operations.data_zone.delete_environment

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.delete_environment.async_delete_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.delete_environment_input.DeleteEnvironmentInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_environment_action(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        environment_identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId",
        identifier: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> None:
        """<p>Deletes an action for the environment, for example, deletes a console link for an analytics tool that is available in this environment.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which an environment action is deleted.</p>
            environment_identifier: <p>The ID of the environment where an environment action is deleted.</p>
            identifier: <p>The ID of the environment action that is deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.delete_environment_action_input.DeleteEnvironmentActionInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_datazone._operations.data_zone.delete_environment_action

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.delete_environment_action.async_delete_environment_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.delete_environment_action_input.DeleteEnvironmentActionInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["environment_identifier"] = environment_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_environment_blueprint(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.environment_blueprint_id.EnvironmentBlueprintId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> None:
        """<p>Deletes a blueprint in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the blueprint is deleted.</p>
            identifier: <p>The ID of the blueprint that is deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.delete_environment_blueprint_input.DeleteEnvironmentBlueprintInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_datazone._operations.data_zone.delete_environment_blueprint

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.delete_environment_blueprint.async_delete_environment_blueprint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.delete_environment_blueprint_input.DeleteEnvironmentBlueprintInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_environment_profile(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.environment_profile_id.EnvironmentProfileId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> None:
        """<p>Deletes an environment profile in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the environment profile is deleted.</p>
            identifier: <p>The ID of the environment profile that is deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.delete_environment_profile_input.DeleteEnvironmentProfileInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_datazone._operations.data_zone.delete_environment_profile

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.delete_environment_profile.async_delete_environment_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.delete_environment_profile_input.DeleteEnvironmentProfileInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_project(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        skip_deletion_check: Optional[bool] = None,
    ) -> "aws_sdk_datazone.types.delete_project_output.DeleteProjectOutput":
        """<p>Deletes a project in Amazon DataZone. </p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the project is deleted.</p>
            identifier: <p>The identifier of the project that is to be deleted.</p>
            skip_deletion_check: <p>Specifies the optional flag to delete all child entities within the project.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.delete_project_input.DeleteProjectInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.delete_project_output.DeleteProjectOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.delete_project

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.delete_project.async_delete_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.delete_project_input.DeleteProjectInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        if skip_deletion_check is not None:
            input_["skip_deletion_check"] = skip_deletion_check

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_project_membership(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        project_identifier: "aws_sdk_datazone.types.project_id.ProjectId",
        member: "aws_sdk_datazone.types.member.Member",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.delete_project_membership_output.DeleteProjectMembershipOutput":
        """<p>Deletes project membership in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain where project membership is deleted.</p>
            project_identifier: <p>The ID of the Amazon DataZone project the membership to which is deleted.</p>
            member: <p>The project member whose project membership is deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.delete_project_membership_input.DeleteProjectMembershipInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.delete_project_membership_output.DeleteProjectMembershipOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.delete_project_membership

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.delete_project_membership.async_delete_project_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.delete_project_membership_input.DeleteProjectMembershipInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["project_identifier"] = project_identifier
        input_["member"] = member

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_project_profile(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.project_profile_id.ProjectProfileId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.delete_project_profile_output.DeleteProjectProfileOutput":
        """<p>Deletes a project profile.</p>

        Args:
            domain_identifier: <p>The ID of the domain where a project profile is deleted.</p>
            identifier: <p>The ID of the project profile that is deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.delete_project_profile_input.DeleteProjectProfileInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.delete_project_profile_output.DeleteProjectProfileOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.delete_project_profile

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.delete_project_profile.async_delete_project_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.delete_project_profile_input.DeleteProjectProfileInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_subscription_grant(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.subscription_grant_id.SubscriptionGrantId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.delete_subscription_grant_output.DeleteSubscriptionGrantOutput":
        """<p>Deletes and subscription grant in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain where the subscription grant is deleted.</p>
            identifier: <p>The ID of the subscription grant that is deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.delete_subscription_grant_input.DeleteSubscriptionGrantInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.delete_subscription_grant_output.DeleteSubscriptionGrantOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.delete_subscription_grant

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.delete_subscription_grant.async_delete_subscription_grant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.delete_subscription_grant_input.DeleteSubscriptionGrantInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_subscription_request(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.subscription_request_id.SubscriptionRequestId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> None:
        """<p>Deletes a subscription request in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the subscription request is deleted.</p>
            identifier: <p>The ID of the subscription request that is deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.delete_subscription_request_input.DeleteSubscriptionRequestInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_datazone._operations.data_zone.delete_subscription_request

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.delete_subscription_request.async_delete_subscription_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.delete_subscription_request_input.DeleteSubscriptionRequestInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_subscription_target(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        environment_identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId",
        identifier: "aws_sdk_datazone.types.subscription_target_id.SubscriptionTargetId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> None:
        """<p>Deletes a subscription target in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the subscription target is deleted.</p>
            environment_identifier: <p>The ID of the Amazon DataZone environment in which the subscription target is deleted.</p>
            identifier: <p>The ID of the subscription target that is deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.delete_subscription_target_input.DeleteSubscriptionTargetInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_datazone._operations.data_zone.delete_subscription_target

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.delete_subscription_target.async_delete_subscription_target(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.delete_subscription_target_input.DeleteSubscriptionTargetInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["environment_identifier"] = environment_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_time_series_data_points(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        entity_identifier: "aws_sdk_datazone.types.entity_identifier.EntityIdentifier",
        entity_type: "aws_sdk_datazone.types.time_series_entity_type.TimeSeriesEntityType",
        form_name: "aws_sdk_datazone.types.time_series_form_name.TimeSeriesFormName",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.delete_time_series_data_points_output.DeleteTimeSeriesDataPointsOutput":
        """<p>Deletes the specified time series form for the specified asset. </p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain that houses the asset for which you want to delete a time series form.</p>
            entity_identifier: <p>The ID of the asset for which you want to delete a time series form.</p>
            entity_type: <p>The type of the asset for which you want to delete a time series form.</p>
            form_name: <p>The name of the time series form that you want to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.delete_time_series_data_points_input.DeleteTimeSeriesDataPointsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.delete_time_series_data_points_output.DeleteTimeSeriesDataPointsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.delete_time_series_data_points

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.delete_time_series_data_points.async_delete_time_series_data_points(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.delete_time_series_data_points_input.DeleteTimeSeriesDataPointsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["entity_identifier"] = entity_identifier
        input_["entity_type"] = entity_type
        input_["form_name"] = form_name
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_environment_role(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        environment_identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId",
        environment_role_arn: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.disassociate_environment_role_output.DisassociateEnvironmentRoleOutput":
        """<p>Disassociates the environment role in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which an environment role is disassociated.</p>
            environment_identifier: <p>The ID of the environment.</p>
            environment_role_arn: <p>The ARN of the environment role.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.disassociate_environment_role_input.DisassociateEnvironmentRoleInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.disassociate_environment_role_output.DisassociateEnvironmentRoleOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.disassociate_environment_role

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.disassociate_environment_role.async_disassociate_environment_role(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.disassociate_environment_role_input.DisassociateEnvironmentRoleInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["environment_identifier"] = environment_identifier
        input_["environment_role_arn"] = environment_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_governed_terms(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        entity_identifier: "aws_sdk_datazone.types.entity_identifier.EntityIdentifier",
        entity_type: "aws_sdk_datazone.types.governed_entity_type.GovernedEntityType",
        governed_glossary_terms: "aws_sdk_datazone.types.governed_glossary_terms.GovernedGlossaryTerms",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.disassociate_governed_terms_output.DisassociateGovernedTermsOutput":
        """<p>Disassociates restricted terms from an asset.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to disassociate restricted terms from an asset.</p>
            entity_identifier: <p>The ID of an asset from which you want to disassociate restricted terms.</p>
            entity_type: <p>The type of the asset from which you want to disassociate restricted terms.</p>
            governed_glossary_terms: <p>The restricted glossary terms that you want to disassociate from an asset.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.disassociate_governed_terms_input.DisassociateGovernedTermsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.disassociate_governed_terms_output.DisassociateGovernedTermsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.disassociate_governed_terms

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.disassociate_governed_terms.async_disassociate_governed_terms(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.disassociate_governed_terms_input.DisassociateGovernedTermsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["entity_identifier"] = entity_identifier
        input_["entity_type"] = entity_type
        input_["governed_glossary_terms"] = governed_glossary_terms

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_account_pool(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.account_pool_id.AccountPoolId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_account_pool_output.GetAccountPoolOutput":
        """<p>Gets the details of the account pool.</p>

        Args:
            domain_identifier: <p>The ID of the domain in which the account pool lives whose details are to be displayed.</p>
            identifier: <p>The ID of the account pool whose details are to be displayed.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_account_pool_input.GetAccountPoolInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_account_pool_output.GetAccountPoolOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_account_pool

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_account_pool.async_get_account_pool(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_account_pool_input.GetAccountPoolInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_asset_filter(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        asset_identifier: "aws_sdk_datazone.types.asset_id.AssetId",
        identifier: "aws_sdk_datazone.types.filter_id.FilterId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_asset_filter_output.GetAssetFilterOutput":
        """<p>Gets an asset filter.</p> <p>Prerequisites:</p> <ul> <li> <p>Domain (<code>--domain-identifier</code>), asset (<code>--asset-identifier</code>), and filter (<code>--identifier</code>) must all exist. </p> </li> <li> <p>The asset filter should not have been deleted.</p> </li> <li> <p>The asset must still exist (since the filter is linked to it).</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the domain where you want to get an asset filter.</p>
            asset_identifier: <p>The ID of the data asset.</p>
            identifier: <p>The ID of the asset filter.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_asset_filter_input.GetAssetFilterInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_asset_filter_output.GetAssetFilterOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_asset_filter

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_asset_filter.async_get_asset_filter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_asset_filter_input.GetAssetFilterInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["asset_identifier"] = asset_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_connection(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        with_secret: Optional[bool] = None,
    ) -> "aws_sdk_datazone.types.get_connection_output.GetConnectionOutput":
        """<p>Gets a connection. In Amazon DataZone, a connection enables you to connect your resources (domains, projects, and environments) to external resources and services.</p>

        Args:
            domain_identifier: <p>The ID of the domain where we get the connection.</p>
            identifier: <p>The connection ID.</p>
            with_secret: <p>Specifies whether a connection has a secret.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_connection_input.GetConnectionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_connection_output.GetConnectionOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_connection

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_connection.async_get_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_connection_input.GetConnectionInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        if with_secret is not None:
            input_["with_secret"] = with_secret

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_data_export_configuration(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_data_export_configuration_output.GetDataExportConfigurationOutput":
        """<p>Gets data export configuration details.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to get the data export configuration details.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_data_export_configuration_input.GetDataExportConfigurationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_data_export_configuration_output.GetDataExportConfigurationOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_data_export_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_data_export_configuration.async_get_data_export_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_data_export_configuration_input.GetDataExportConfigurationInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_environment(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_environment_output.GetEnvironmentOutput":
        """<p>Gets an Amazon DataZone environment.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain where the environment exists.</p>
            identifier: <p>The ID of the Amazon DataZone environment.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_environment_input.GetEnvironmentInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_environment_output.GetEnvironmentOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_environment

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_environment.async_get_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_environment_input.GetEnvironmentInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_environment_action(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        environment_identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId",
        identifier: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_environment_action_output.GetEnvironmentActionOutput":
        """<p>Gets the specified environment action.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the <code>GetEnvironmentAction</code> API is invoked. </p>
            environment_identifier: <p>The environment ID of the environment action.</p>
            identifier: <p>The ID of the environment action</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_environment_action_input.GetEnvironmentActionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_environment_action_output.GetEnvironmentActionOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_environment_action

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_environment_action.async_get_environment_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_environment_action_input.GetEnvironmentActionInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["environment_identifier"] = environment_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_environment_blueprint(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.environment_blueprint_id.EnvironmentBlueprintId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_environment_blueprint_output.GetEnvironmentBlueprintOutput":
        """<p>Gets an Amazon DataZone blueprint.</p>

        Args:
            domain_identifier: <p>The identifier of the domain in which this blueprint exists.</p>
            identifier: <p>The ID of this Amazon DataZone blueprint.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_environment_blueprint_input.GetEnvironmentBlueprintInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_environment_blueprint_output.GetEnvironmentBlueprintOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_environment_blueprint

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_environment_blueprint.async_get_environment_blueprint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_environment_blueprint_input.GetEnvironmentBlueprintInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_environment_credentials(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        environment_identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_environment_credentials_output.GetEnvironmentCredentialsOutput":
        """<p>Gets the credentials of an environment in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this environment and its credentials exist.</p>
            environment_identifier: <p>The ID of the environment whose credentials this operation gets.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_environment_credentials_input.GetEnvironmentCredentialsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_environment_credentials_output.GetEnvironmentCredentialsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_environment_credentials

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_environment_credentials.async_get_environment_credentials(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_environment_credentials_input.GetEnvironmentCredentialsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["environment_identifier"] = environment_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_environment_profile(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.environment_profile_id.EnvironmentProfileId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_environment_profile_output.GetEnvironmentProfileOutput":
        """<p>Gets an evinronment profile in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this environment profile exists.</p>
            identifier: <p>The ID of the environment profile.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_environment_profile_input.GetEnvironmentProfileInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_environment_profile_output.GetEnvironmentProfileOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_environment_profile

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_environment_profile.async_get_environment_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_environment_profile_input.GetEnvironmentProfileInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_group_profile(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        group_identifier: "aws_sdk_datazone.types.group_identifier.GroupIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_group_profile_output.GetGroupProfileOutput":
        """<p>Gets a group profile in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which the group profile exists.</p>
            group_identifier: <p>The identifier of the group profile.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_group_profile_input.GetGroupProfileInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_group_profile_output.GetGroupProfileOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_group_profile

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_group_profile.async_get_group_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_group_profile_input.GetGroupProfileInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["group_identifier"] = group_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_iam_portal_login_url(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_iam_portal_login_url_output.GetIamPortalLoginUrlOutput":
        """<p>Gets the data portal URL for the specified Amazon DataZone domain.</p>

        Args:
            domain_identifier: <p>the ID of the Amazon DataZone domain the data portal of which you want to get.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_iam_portal_login_url_input.GetIamPortalLoginUrlInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_iam_portal_login_url_output.GetIamPortalLoginUrlOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_iam_portal_login_url

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_iam_portal_login_url.async_get_iam_portal_login_url(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_iam_portal_login_url_input.GetIamPortalLoginUrlInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_job_run(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.run_identifier.RunIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_job_run_output.GetJobRunOutput":
        """<p>The details of the job run.</p>

        Args:
            domain_identifier: <p>The ID of the domain.</p>
            identifier: <p>The ID of the job run.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_job_run_input.GetJobRunInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_job_run_output.GetJobRunOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_job_run

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_job_run.async_get_job_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_job_run_input.GetJobRunInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_lineage_event(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.lineage_event_identifier.LineageEventIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_lineage_event_output.GetLineageEventOutput":
        """<p>Describes the lineage event.</p>

        Args:
            domain_identifier: <p>The ID of the domain.</p>
            identifier: <p>The ID of the lineage event.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_lineage_event_input.GetLineageEventInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_lineage_event_output.GetLineageEventOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_lineage_event

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_lineage_event.async_get_lineage_event(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_lineage_event_input.GetLineageEventInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_lineage_node(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.lineage_node_identifier.LineageNodeIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        event_timestamp: Optional[datetime.datetime] = None,
    ) -> "aws_sdk_datazone.types.get_lineage_node_output.GetLineageNodeOutput":
        """<p>Gets the data lineage node.</p>

        Args:
            domain_identifier: <p>The ID of the domain in which you want to get the data lineage node.</p>
            identifier: <p>The ID of the data lineage node that you want to get.</p> <p>Both, a lineage node identifier generated by Amazon DataZone and a <code>sourceIdentifier</code> of the lineage node are supported. If <code>sourceIdentifier</code> is greater than 1800 characters, you can use lineage node identifier generated by Amazon DataZone to get the node details.</p>
            event_timestamp: <p>The event time stamp for which you want to get the data lineage node.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_lineage_node_input.GetLineageNodeInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_lineage_node_output.GetLineageNodeOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_lineage_node

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_lineage_node.async_get_lineage_node(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_lineage_node_input.GetLineageNodeInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        if event_timestamp is not None:
            input_["event_timestamp"] = event_timestamp

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_project(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_project_output.GetProjectOutput":
        """<p>Gets a project in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the project exists.</p>
            identifier: <p>The ID of the project.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_project_input.GetProjectInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_project_output.GetProjectOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_project

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_project.async_get_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_project_input.GetProjectInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_project_profile(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.project_profile_id.ProjectProfileId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_project_profile_output.GetProjectProfileOutput":
        """<p>The details of the project profile.</p>

        Args:
            domain_identifier: <p>The ID of the domain.</p>
            identifier: <p>The ID of the project profile.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_project_profile_input.GetProjectProfileInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_project_profile_output.GetProjectProfileOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_project_profile

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_project_profile.async_get_project_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_project_profile_input.GetProjectProfileInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_subscription(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.subscription_id.SubscriptionId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_subscription_output.GetSubscriptionOutput":
        """<p>Gets a subscription in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the subscription exists.</p>
            identifier: <p>The ID of the subscription.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_subscription_input.GetSubscriptionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_subscription_output.GetSubscriptionOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_subscription

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_subscription.async_get_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_subscription_input.GetSubscriptionInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_subscription_grant(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.subscription_grant_id.SubscriptionGrantId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_subscription_grant_output.GetSubscriptionGrantOutput":
        """<p>Gets the subscription grant in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the subscription grant exists.</p>
            identifier: <p>The ID of the subscription grant.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_subscription_grant_input.GetSubscriptionGrantInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_subscription_grant_output.GetSubscriptionGrantOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_subscription_grant

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_subscription_grant.async_get_subscription_grant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_subscription_grant_input.GetSubscriptionGrantInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_subscription_request_details(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.subscription_request_id.SubscriptionRequestId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_subscription_request_details_output.GetSubscriptionRequestDetailsOutput":
        """<p>Gets the details of the specified subscription request.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which to get the subscription request details.</p>
            identifier: <p>The identifier of the subscription request the details of which to get.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_subscription_request_details_input.GetSubscriptionRequestDetailsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_subscription_request_details_output.GetSubscriptionRequestDetailsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_subscription_request_details

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_subscription_request_details.async_get_subscription_request_details(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_subscription_request_details_input.GetSubscriptionRequestDetailsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_subscription_target(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        environment_identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId",
        identifier: "aws_sdk_datazone.types.subscription_target_id.SubscriptionTargetId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_subscription_target_output.GetSubscriptionTargetOutput":
        """<p>Gets the subscription target in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the subscription target exists.</p>
            environment_identifier: <p>The ID of the environment associated with the subscription target.</p>
            identifier: <p>The ID of the subscription target.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_subscription_target_input.GetSubscriptionTargetInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_subscription_target_output.GetSubscriptionTargetOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_subscription_target

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_subscription_target.async_get_subscription_target(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_subscription_target_input.GetSubscriptionTargetInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["environment_identifier"] = environment_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_time_series_data_point(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        entity_identifier: "aws_sdk_datazone.types.entity_identifier.EntityIdentifier",
        entity_type: "aws_sdk_datazone.types.time_series_entity_type.TimeSeriesEntityType",
        identifier: "aws_sdk_datazone.types.time_series_data_point_identifier.TimeSeriesDataPointIdentifier",
        form_name: "aws_sdk_datazone.types.time_series_form_name.TimeSeriesFormName",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_time_series_data_point_output.GetTimeSeriesDataPointOutput":
        """<p>Gets the existing data point for the asset.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain that houses the asset for which you want to get the data point.</p>
            entity_identifier: <p>The ID of the asset for which you want to get the data point.</p>
            entity_type: <p>The type of the asset for which you want to get the data point.</p>
            identifier: <p>The ID of the data point that you want to get.</p>
            form_name: <p>The name of the time series form that houses the data point that you want to get.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_time_series_data_point_input.GetTimeSeriesDataPointInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_time_series_data_point_output.GetTimeSeriesDataPointOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_time_series_data_point

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_time_series_data_point.async_get_time_series_data_point(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_time_series_data_point_input.GetTimeSeriesDataPointInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["entity_identifier"] = entity_identifier
        input_["entity_type"] = entity_type
        input_["identifier"] = identifier
        input_["form_name"] = form_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_user_profile(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        user_identifier: "aws_sdk_datazone.types.user_identifier.UserIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        type: Optional[
            "aws_sdk_datazone.types.user_profile_type.UserProfileType"
        ] = None,
        session_name: Optional[str] = None,
    ) -> "aws_sdk_datazone.types.get_user_profile_output.GetUserProfileOutput":
        """<p>Gets a user profile in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>the ID of the Amazon DataZone domain the data portal of which you want to get.</p>
            user_identifier: <p>The identifier of the user for which you want to get the user profile.</p>
            type: <p>The type of the user profile.</p>
            session_name: <p>The session name for IAM role sessions.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_user_profile_input.GetUserProfileInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_user_profile_output.GetUserProfileOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_user_profile

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_user_profile.async_get_user_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_user_profile_input.GetUserProfileInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["user_identifier"] = user_identifier
        if type is not None:
            input_["type"] = type
        if session_name is not None:
            input_["session_name"] = session_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_account_pools(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        name: Optional[
            "aws_sdk_datazone.types.account_pool_name.AccountPoolName"
        ] = None,
        sort_by: Optional[
            "aws_sdk_datazone.types.sort_field_account_pool.SortFieldAccountPool"
        ] = None,
        sort_order: Optional["aws_sdk_datazone.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_datazone.types.list_account_pools_output.ListAccountPoolsOutput":
        """<p>Lists existing account pools.</p>

        Args:
            domain_identifier: <p>The ID of the domain where exsting account pools are to be listed.</p>
            name: <p>The name of the account pool to be listed.</p>
            sort_by: <p>The sort by mechanism in which the existing account pools are to be listed.</p>
            sort_order: <p>The sort order in which the existing account pools are to be listed.</p>
            next_token: <p>When the number of account pools is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of account pools, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListAccountPools to list the next set of account pools.</p>
            max_results: <p>The maximum number of account pools to return in a single call to ListAccountPools. When the number of account pools to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListAccountPools to list the next set of account pools.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_account_pools_input.ListAccountPoolsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_account_pools_output.ListAccountPoolsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_account_pools

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_account_pools.async_list_account_pools(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_account_pools_input.ListAccountPoolsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        if name is not None:
            input_["name"] = name
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
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

    async def iter_list_account_pools(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        name: Optional[
            "aws_sdk_datazone.types.account_pool_name.AccountPoolName"
        ] = None,
        sort_by: Optional[
            "aws_sdk_datazone.types.sort_field_account_pool.SortFieldAccountPool"
        ] = None,
        sort_order: Optional["aws_sdk_datazone.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
    ) -> (
        "AsyncIterator[aws_sdk_datazone.types.account_pool_summary.AccountPoolSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.list_account_pools(
                domain_identifier,
                config_overrides=config_overrides,
                name=name,
                sort_by=sort_by,
                sort_order=sort_order,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_accounts_in_account_pool(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.account_pool_id.AccountPoolId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_datazone.types.list_accounts_in_account_pool_output.ListAccountsInAccountPoolOutput":
        """<p>Lists the accounts in the specified account pool.</p>

        Args:
            domain_identifier: <p>The ID of the domain in which the accounts in the specified account pool are to be listed.</p>
            identifier: <p>The ID of the account pool whose accounts are to be listed.</p>
            next_token: <p>When the number of accounts is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of accounts, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListAccountsInAccountPool to list the next set of accounts.</p>
            max_results: <p>The maximum number of accounts to return in a single call to ListAccountsInAccountPool. When the number of accounts to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListAccountsInAccountPool to list the next set of accounts.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_accounts_in_account_pool_input.ListAccountsInAccountPoolInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_accounts_in_account_pool_output.ListAccountsInAccountPoolOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_accounts_in_account_pool

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_accounts_in_account_pool.async_list_accounts_in_account_pool(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_accounts_in_account_pool_input.ListAccountsInAccountPoolInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
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

    async def iter_list_accounts_in_account_pool(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.account_pool_id.AccountPoolId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[aws_sdk_datazone.types.account_info.AccountInfo]":
        _token = next_token
        while True:
            _response = await self.list_accounts_in_account_pool(
                domain_identifier,
                identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_asset_filters(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        asset_identifier: "aws_sdk_datazone.types.asset_id.AssetId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional["aws_sdk_datazone.types.filter_status.FilterStatus"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_datazone.types.list_asset_filters_output.ListAssetFiltersOutput":
        """<p>Lists asset filters.</p> <p>Prerequisites:</p> <ul> <li> <p>A valid domain and asset must exist. </p> </li> <li> <p>The asset must have at least one filter created to return results. </p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the domain where you want to list asset filters.</p>
            asset_identifier: <p>The ID of the data asset.</p>
            status: <p>The status of the asset filter.</p>
            next_token: <p>When the number of asset filters is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of asset filters, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListAssetFilters</code> to list the next set of asset filters.</p>
            max_results: <p>The maximum number of asset filters to return in a single call to <code>ListAssetFilters</code>. When the number of asset filters to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListAssetFilters</code> to list the next set of asset filters.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_asset_filters_input.ListAssetFiltersInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_asset_filters_output.ListAssetFiltersOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_asset_filters

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_asset_filters.async_list_asset_filters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_asset_filters_input.ListAssetFiltersInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["asset_identifier"] = asset_identifier
        if status is not None:
            input_["status"] = status
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

    async def iter_list_asset_filters(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        asset_identifier: "aws_sdk_datazone.types.asset_id.AssetId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional["aws_sdk_datazone.types.filter_status.FilterStatus"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
    ) -> (
        "AsyncIterator[aws_sdk_datazone.types.asset_filter_summary.AssetFilterSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.list_asset_filters(
                domain_identifier,
                asset_identifier,
                config_overrides=config_overrides,
                status=status,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_asset_revisions(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.asset_identifier.AssetIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_datazone.types.list_asset_revisions_output.ListAssetRevisionsOutput":
        """<p>Lists the revisions for the asset.</p> <p>Prerequisites:</p> <ul> <li> <p>The asset must exist in the domain. </p> </li> <li> <p>There must be at least one revision of the asset (which happens automatically after creation).</p> </li> <li> <p>The domain must be valid and active.</p> </li> <li> <p>User must have permissions on the asset and domain.</p> </li> </ul>

        Args:
            domain_identifier: <p>The identifier of the domain.</p>
            identifier: <p>The identifier of the asset.</p>
            next_token: <p>When the number of revisions is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of revisions, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListAssetRevisions</code> to list the next set of revisions.</p>
            max_results: <p>The maximum number of revisions to return in a single call to <code>ListAssetRevisions</code>. When the number of revisions to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListAssetRevisions</code> to list the next set of revisions.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_asset_revisions_input.ListAssetRevisionsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_asset_revisions_output.ListAssetRevisionsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_asset_revisions

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_asset_revisions.async_list_asset_revisions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_asset_revisions_input.ListAssetRevisionsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
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

    async def list_connections(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional[
            "aws_sdk_datazone.types.sort_field_connection.SortFieldConnection"
        ] = None,
        sort_order: Optional["aws_sdk_datazone.types.sort_order.SortOrder"] = None,
        name: Optional["aws_sdk_datazone.types.connection_name.ConnectionName"] = None,
        environment_identifier: Optional[
            "aws_sdk_datazone.types.environment_id.EnvironmentId"
        ] = None,
        project_identifier: Optional[
            "aws_sdk_datazone.types.project_id.ProjectId"
        ] = None,
        type: Optional["aws_sdk_datazone.types.connection_type.ConnectionType"] = None,
        scope: Optional[
            "aws_sdk_datazone.types.connection_scope.ConnectionScope"
        ] = None,
    ) -> "aws_sdk_datazone.types.list_connections_output.ListConnectionsOutput":
        """<p>Lists connections. In Amazon DataZone, a connection enables you to connect your resources (domains, projects, and environments) to external resources and services.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to list connections.</p>
            max_results: <p>The maximum number of connections to return in a single call to ListConnections. When the number of connections to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListConnections to list the next set of connections.</p>
            next_token: <p>When the number of connections is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of connections, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListConnections to list the next set of connections.</p>
            sort_by: <p>Specifies how you want to sort the listed connections.</p>
            sort_order: <p>Specifies the sort order for the listed connections.</p>
            name: <p>The name of the connection.</p>
            environment_identifier: <p>The ID of the environment where you want to list connections.</p>
            project_identifier: <p>The ID of the project where you want to list connections.</p>
            type: <p>The type of connection.</p>
            scope: <p>The scope of the connection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_connections_input.ListConnectionsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_connections_output.ListConnectionsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_connections

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_connections.async_list_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_connections_input.ListConnectionsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if name is not None:
            input_["name"] = name
        if environment_identifier is not None:
            input_["environment_identifier"] = environment_identifier
        if project_identifier is not None:
            input_["project_identifier"] = project_identifier
        if type is not None:
            input_["type"] = type
        if scope is not None:
            input_["scope"] = scope

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_connections(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional[
            "aws_sdk_datazone.types.sort_field_connection.SortFieldConnection"
        ] = None,
        sort_order: Optional["aws_sdk_datazone.types.sort_order.SortOrder"] = None,
        name: Optional["aws_sdk_datazone.types.connection_name.ConnectionName"] = None,
        environment_identifier: Optional[
            "aws_sdk_datazone.types.environment_id.EnvironmentId"
        ] = None,
        project_identifier: Optional[
            "aws_sdk_datazone.types.project_id.ProjectId"
        ] = None,
        type: Optional["aws_sdk_datazone.types.connection_type.ConnectionType"] = None,
        scope: Optional[
            "aws_sdk_datazone.types.connection_scope.ConnectionScope"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_datazone.types.connection_summary.ConnectionSummary]":
        _token = next_token
        while True:
            _response = await self.list_connections(
                domain_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                sort_by=sort_by,
                sort_order=sort_order,
                name=name,
                environment_identifier=environment_identifier,
                project_identifier=project_identifier,
                type=type,
                scope=scope,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_data_product_revisions(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.data_product_id.DataProductId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.list_data_product_revisions_output.ListDataProductRevisionsOutput":
        """<p>Lists data product revisions.</p> <p>Prerequisites:</p> <ul> <li> <p>The data product ID must exist within the domain. </p> </li> <li> <p>User must have view permissions on the data product.</p> </li> <li> <p>The domain must be in a valid and accessible state.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the domain of the data product revisions that you want to list.</p>
            identifier: <p>The ID of the data product revision.</p>
            max_results: <p>The maximum number of asset filters to return in a single call to <code>ListDataProductRevisions</code>. When the number of data product revisions to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListDataProductRevisions</code> to list the next set of data product revisions.</p>
            next_token: <p>When the number of data product revisions is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of data product revisions, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListDataProductRevisions</code> to list the next set of data product revisions.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_data_product_revisions_input.ListDataProductRevisionsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_data_product_revisions_output.ListDataProductRevisionsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_data_product_revisions

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_data_product_revisions.async_list_data_product_revisions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_data_product_revisions_input.ListDataProductRevisionsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_data_product_revisions(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.data_product_id.DataProductId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_datazone.types.data_product_revision.DataProductRevision]":
        _token = next_token
        while True:
            _response = await self.list_data_product_revisions(
                domain_identifier,
                identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_data_source_run_activities(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.data_source_run_id.DataSourceRunId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional[
            "aws_sdk_datazone.types.data_asset_activity_status.DataAssetActivityStatus"
        ] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_datazone.types.list_data_source_run_activities_output.ListDataSourceRunActivitiesOutput":
        """<p>Lists data source run activities.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which to list data source run activities.</p>
            identifier: <p>The identifier of the data source run.</p>
            status: <p>The status of the data source run.</p>
            next_token: <p>When the number of activities is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of activities, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListDataSourceRunActivities</code> to list the next set of activities.</p>
            max_results: <p>The maximum number of activities to return in a single call to <code>ListDataSourceRunActivities</code>. When the number of activities to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListDataSourceRunActivities</code> to list the next set of activities.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_data_source_run_activities_input.ListDataSourceRunActivitiesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_data_source_run_activities_output.ListDataSourceRunActivitiesOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_data_source_run_activities

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_data_source_run_activities.async_list_data_source_run_activities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_data_source_run_activities_input.ListDataSourceRunActivitiesInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        if status is not None:
            input_["status"] = status
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

    async def iter_list_data_source_run_activities(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.data_source_run_id.DataSourceRunId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional[
            "aws_sdk_datazone.types.data_asset_activity_status.DataAssetActivityStatus"
        ] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[aws_sdk_datazone.types.data_source_run_activity.DataSourceRunActivity]":
        _token = next_token
        while True:
            _response = await self.list_data_source_run_activities(
                domain_identifier,
                identifier,
                config_overrides=config_overrides,
                status=status,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_entity_owners(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        entity_type: "aws_sdk_datazone.types.data_zone_entity_type.DataZoneEntityType",
        entity_identifier: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional[
            "aws_sdk_datazone.types.max_results_for_list_domains.MaxResultsForListDomains"
        ] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.list_entity_owners_output.ListEntityOwnersOutput":
        """<p>Lists the entity (domain units) owners.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to list entity owners.</p>
            entity_type: <p>The type of the entity that you want to list.</p>
            entity_identifier: <p>The ID of the entity that you want to list.</p>
            max_results: <p>The maximum number of entities to return in a single call to <code>ListEntityOwners</code>. When the number of entities to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListEntityOwners</code> to list the next set of entities.</p>
            next_token: <p>When the number of entities is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of entities, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListEntityOwners</code> to list the next set of entities.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_entity_owners_input.ListEntityOwnersInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_entity_owners_output.ListEntityOwnersOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_entity_owners

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_entity_owners.async_list_entity_owners(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_entity_owners_input.ListEntityOwnersInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["entity_type"] = entity_type
        input_["entity_identifier"] = entity_identifier
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_entity_owners(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        entity_type: "aws_sdk_datazone.types.data_zone_entity_type.DataZoneEntityType",
        entity_identifier: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional[
            "aws_sdk_datazone.types.max_results_for_list_domains.MaxResultsForListDomains"
        ] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_datazone.types.owner_properties_output.OwnerPropertiesOutput]":
        _token = next_token
        while True:
            _response = await self.list_entity_owners(
                domain_identifier,
                entity_type,
                entity_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("owners",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_environment_actions(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        environment_identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_datazone.types.list_environment_actions_output.ListEnvironmentActionsOutput":
        """<p>Lists existing environment actions.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the environment actions are listed.</p>
            environment_identifier: <p>The ID of the envrironment whose environment actions are listed.</p>
            next_token: <p>When the number of environment actions is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of environment actions, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListEnvironmentActions</code> to list the next set of environment actions.</p>
            max_results: <p>The maximum number of environment actions to return in a single call to <code>ListEnvironmentActions</code>. When the number of environment actions to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListEnvironmentActions</code> to list the next set of environment actions.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_environment_actions_input.ListEnvironmentActionsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_environment_actions_output.ListEnvironmentActionsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_environment_actions

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_environment_actions.async_list_environment_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_environment_actions_input.ListEnvironmentActionsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["environment_identifier"] = environment_identifier
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

    async def iter_list_environment_actions(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        environment_identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[aws_sdk_datazone.types.environment_action_summary.EnvironmentActionSummary]":
        _token = next_token
        while True:
            _response = await self.list_environment_actions(
                domain_identifier,
                environment_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_environment_blueprints(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        name: Optional[
            "aws_sdk_datazone.types.environment_blueprint_name.EnvironmentBlueprintName"
        ] = None,
        managed: Optional[bool] = None,
    ) -> "aws_sdk_datazone.types.list_environment_blueprints_output.ListEnvironmentBlueprintsOutput":
        """<p>Lists blueprints in an Amazon DataZone environment.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            max_results: <p>The maximum number of blueprints to return in a single call to <code>ListEnvironmentBlueprints</code>. When the number of blueprints to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListEnvironmentBlueprints</code> to list the next set of blueprints.</p>
            next_token: <p>When the number of blueprints in the environment is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of blueprints in the environment, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListEnvironmentBlueprints</code>to list the next set of blueprints.</p>
            name: <p>The name of the Amazon DataZone environment.</p>
            managed: <p>Specifies whether the environment blueprint is managed by Amazon DataZone.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_environment_blueprints_input.ListEnvironmentBlueprintsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_environment_blueprints_output.ListEnvironmentBlueprintsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_environment_blueprints

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_environment_blueprints.async_list_environment_blueprints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_environment_blueprints_input.ListEnvironmentBlueprintsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if name is not None:
            input_["name"] = name
        if managed is not None:
            input_["managed"] = managed

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_environment_blueprints(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        name: Optional[
            "aws_sdk_datazone.types.environment_blueprint_name.EnvironmentBlueprintName"
        ] = None,
        managed: Optional[bool] = None,
    ) -> "AsyncIterator[aws_sdk_datazone.types.environment_blueprint_summary.EnvironmentBlueprintSummary]":
        _token = next_token
        while True:
            _response = await self.list_environment_blueprints(
                domain_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                name=name,
                managed=managed,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_environment_profiles(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        aws_account_id: Optional[
            "aws_sdk_datazone.types.aws_account_id.AwsAccountId"
        ] = None,
        aws_account_region: Optional[
            "aws_sdk_datazone.types.aws_region.AwsRegion"
        ] = None,
        environment_blueprint_identifier: Optional[
            "aws_sdk_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
        ] = None,
        project_identifier: Optional[
            "aws_sdk_datazone.types.project_id.ProjectId"
        ] = None,
        name: Optional[
            "aws_sdk_datazone.types.environment_profile_name.EnvironmentProfileName"
        ] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_datazone.types.list_environment_profiles_output.ListEnvironmentProfilesOutput":
        """<p>Lists Amazon DataZone environment profiles.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            aws_account_id: <p>The identifier of the Amazon Web Services account where you want to list environment profiles.</p>
            aws_account_region: <p>The Amazon Web Services region where you want to list environment profiles.</p>
            environment_blueprint_identifier: <p>The identifier of the blueprint that was used to create the environment profiles that you want to list.</p>
            project_identifier: <p>The identifier of the Amazon DataZone project.</p>
            name: <p/>
            next_token: <p>When the number of environment profiles is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of environment profiles, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListEnvironmentProfiles</code> to list the next set of environment profiles.</p>
            max_results: <p>The maximum number of environment profiles to return in a single call to <code>ListEnvironmentProfiles</code>. When the number of environment profiles to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListEnvironmentProfiles</code> to list the next set of environment profiles.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_environment_profiles_input.ListEnvironmentProfilesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_environment_profiles_output.ListEnvironmentProfilesOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_environment_profiles

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_environment_profiles.async_list_environment_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_environment_profiles_input.ListEnvironmentProfilesInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        if aws_account_id is not None:
            input_["aws_account_id"] = aws_account_id
        if aws_account_region is not None:
            input_["aws_account_region"] = aws_account_region
        if environment_blueprint_identifier is not None:
            input_["environment_blueprint_identifier"] = (
                environment_blueprint_identifier
            )
        if project_identifier is not None:
            input_["project_identifier"] = project_identifier
        if name is not None:
            input_["name"] = name
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

    async def iter_list_environment_profiles(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        aws_account_id: Optional[
            "aws_sdk_datazone.types.aws_account_id.AwsAccountId"
        ] = None,
        aws_account_region: Optional[
            "aws_sdk_datazone.types.aws_region.AwsRegion"
        ] = None,
        environment_blueprint_identifier: Optional[
            "aws_sdk_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
        ] = None,
        project_identifier: Optional[
            "aws_sdk_datazone.types.project_id.ProjectId"
        ] = None,
        name: Optional[
            "aws_sdk_datazone.types.environment_profile_name.EnvironmentProfileName"
        ] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[aws_sdk_datazone.types.environment_profile_summary.EnvironmentProfileSummary]":
        _token = next_token
        while True:
            _response = await self.list_environment_profiles(
                domain_identifier,
                config_overrides=config_overrides,
                aws_account_id=aws_account_id,
                aws_account_region=aws_account_region,
                environment_blueprint_identifier=environment_blueprint_identifier,
                project_identifier=project_identifier,
                name=name,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_environments(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        project_identifier: "aws_sdk_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        aws_account_id: Optional[
            "aws_sdk_datazone.types.aws_account_id.AwsAccountId"
        ] = None,
        status: Optional[
            "aws_sdk_datazone.types.environment_status.EnvironmentStatus"
        ] = None,
        aws_account_region: Optional[
            "aws_sdk_datazone.types.aws_region.AwsRegion"
        ] = None,
        environment_profile_identifier: Optional[
            "aws_sdk_datazone.types.environment_profile_id.EnvironmentProfileId"
        ] = None,
        environment_blueprint_identifier: Optional[
            "aws_sdk_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
        ] = None,
        provider: Optional[str] = None,
        name: Optional[str] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.list_environments_output.ListEnvironmentsOutput":
        """<p>Lists Amazon DataZone environments.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            aws_account_id: <p>The identifier of the Amazon Web Services account where you want to list environments.</p>
            status: <p>The status of the environments that you want to list.</p>
            aws_account_region: <p>The Amazon Web Services region where you want to list environments.</p>
            project_identifier: <p>The identifier of the Amazon DataZone project.</p>
            environment_profile_identifier: <p>The identifier of the environment profile.</p>
            environment_blueprint_identifier: <p>The identifier of the Amazon DataZone blueprint.</p>
            provider: <p>The provider of the environment.</p>
            name: <p>The name of the environment.</p>
            max_results: <p>The maximum number of environments to return in a single call to <code>ListEnvironments</code>. When the number of environments to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListEnvironments</code> to list the next set of environments.</p>
            next_token: <p>When the number of environments is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of environments, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListEnvironments</code> to list the next set of environments.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_environments_input.ListEnvironmentsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_environments_output.ListEnvironmentsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_environments

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_environments.async_list_environments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_environments_input.ListEnvironmentsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        if aws_account_id is not None:
            input_["aws_account_id"] = aws_account_id
        if status is not None:
            input_["status"] = status
        if aws_account_region is not None:
            input_["aws_account_region"] = aws_account_region
        input_["project_identifier"] = project_identifier
        if environment_profile_identifier is not None:
            input_["environment_profile_identifier"] = environment_profile_identifier
        if environment_blueprint_identifier is not None:
            input_["environment_blueprint_identifier"] = (
                environment_blueprint_identifier
            )
        if provider is not None:
            input_["provider"] = provider
        if name is not None:
            input_["name"] = name
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_environments(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        project_identifier: "aws_sdk_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        aws_account_id: Optional[
            "aws_sdk_datazone.types.aws_account_id.AwsAccountId"
        ] = None,
        status: Optional[
            "aws_sdk_datazone.types.environment_status.EnvironmentStatus"
        ] = None,
        aws_account_region: Optional[
            "aws_sdk_datazone.types.aws_region.AwsRegion"
        ] = None,
        environment_profile_identifier: Optional[
            "aws_sdk_datazone.types.environment_profile_id.EnvironmentProfileId"
        ] = None,
        environment_blueprint_identifier: Optional[
            "aws_sdk_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
        ] = None,
        provider: Optional[str] = None,
        name: Optional[str] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_datazone.types.environment_summary.EnvironmentSummary]":
        _token = next_token
        while True:
            _response = await self.list_environments(
                domain_identifier,
                project_identifier,
                config_overrides=config_overrides,
                aws_account_id=aws_account_id,
                status=status,
                aws_account_region=aws_account_region,
                environment_profile_identifier=environment_profile_identifier,
                environment_blueprint_identifier=environment_blueprint_identifier,
                provider=provider,
                name=name,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_job_runs(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        job_identifier: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional["aws_sdk_datazone.types.job_run_status.JobRunStatus"] = None,
        sort_order: Optional["aws_sdk_datazone.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_datazone.types.list_job_runs_output.ListJobRunsOutput":
        """<p>Lists job runs.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to list job runs.</p>
            job_identifier: <p>The ID of the job run.</p>
            status: <p>The status of a job run.</p>
            sort_order: <p>Specifies the order in which job runs are to be sorted.</p>
            next_token: <p>When the number of job runs is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of job runs, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListJobRuns to list the next set of job runs.</p>
            max_results: <p>The maximum number of job runs to return in a single call to ListJobRuns. When the number of job runs to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListJobRuns to list the next set of job runs.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_job_runs_input.ListJobRunsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_job_runs_output.ListJobRunsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_job_runs

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_job_runs.async_list_job_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_job_runs_input.ListJobRunsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["job_identifier"] = job_identifier
        if status is not None:
            input_["status"] = status
        if sort_order is not None:
            input_["sort_order"] = sort_order
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

    async def iter_list_job_runs(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        job_identifier: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional["aws_sdk_datazone.types.job_run_status.JobRunStatus"] = None,
        sort_order: Optional["aws_sdk_datazone.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[aws_sdk_datazone.types.job_run_summary.JobRunSummary]":
        _token = next_token
        while True:
            _response = await self.list_job_runs(
                domain_identifier,
                job_identifier,
                config_overrides=config_overrides,
                status=status,
                sort_order=sort_order,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_lineage_events(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        timestamp_after: Optional[datetime.datetime] = None,
        timestamp_before: Optional[datetime.datetime] = None,
        processing_status: Optional[
            "aws_sdk_datazone.types.lineage_event_processing_status.LineageEventProcessingStatus"
        ] = None,
        sort_order: Optional["aws_sdk_datazone.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.list_lineage_events_output.ListLineageEventsOutput":
        """<p>Lists lineage events.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to list lineage events.</p>
            max_results: <p>The maximum number of lineage events to return in a single call to ListLineageEvents. When the number of lineage events to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListLineageEvents to list the next set of lineage events.</p>
            timestamp_after: <p>The after timestamp of a lineage event.</p>
            timestamp_before: <p>The before timestamp of a lineage event.</p>
            processing_status: <p>The processing status of a lineage event.</p>
            sort_order: <p>The sort order of the lineage events.</p>
            next_token: <p>When the number of lineage events is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of lineage events, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListLineageEvents to list the next set of lineage events.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_lineage_events_input.ListLineageEventsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_lineage_events_output.ListLineageEventsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_lineage_events

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_lineage_events.async_list_lineage_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_lineage_events_input.ListLineageEventsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        if max_results is not None:
            input_["max_results"] = max_results
        if timestamp_after is not None:
            input_["timestamp_after"] = timestamp_after
        if timestamp_before is not None:
            input_["timestamp_before"] = timestamp_before
        if processing_status is not None:
            input_["processing_status"] = processing_status
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_lineage_events(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        timestamp_after: Optional[datetime.datetime] = None,
        timestamp_before: Optional[datetime.datetime] = None,
        processing_status: Optional[
            "aws_sdk_datazone.types.lineage_event_processing_status.LineageEventProcessingStatus"
        ] = None,
        sort_order: Optional["aws_sdk_datazone.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_datazone.types.lineage_event_summary.LineageEventSummary]":
        _token = next_token
        while True:
            _response = await self.list_lineage_events(
                domain_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                timestamp_after=timestamp_after,
                timestamp_before=timestamp_before,
                processing_status=processing_status,
                sort_order=sort_order,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_lineage_node_history(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.lineage_node_identifier.LineageNodeIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        direction: Optional[
            "aws_sdk_datazone.types.edge_direction.EdgeDirection"
        ] = None,
        event_timestamp_gte: Optional[datetime.datetime] = None,
        event_timestamp_lte: Optional[datetime.datetime] = None,
        sort_order: Optional["aws_sdk_datazone.types.sort_order.SortOrder"] = None,
    ) -> "aws_sdk_datazone.types.list_lineage_node_history_output.ListLineageNodeHistoryOutput":
        """<p>Lists the history of the specified data lineage node.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to list the history of the specified data lineage node.</p>
            max_results: <p>The maximum number of history items to return in a single call to ListLineageNodeHistory. When the number of memberships to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListLineageNodeHistory to list the next set of items.</p>
            next_token: <p>When the number of history items is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of items, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListLineageNodeHistory to list the next set of items.</p>
            identifier: <p>The ID of the data lineage node whose history you want to list.</p>
            direction: <p>The direction of the data lineage node refers to the lineage node having neighbors in that direction. For example, if direction is <code>UPSTREAM</code>, the <code>ListLineageNodeHistory</code> API responds with historical versions with upstream neighbors only.</p>
            event_timestamp_gte: <p>Specifies whether the action is to return data lineage node history from the time after the event timestamp.</p>
            event_timestamp_lte: <p>Specifies whether the action is to return data lineage node history from the time prior of the event timestamp.</p>
            sort_order: <p>The order by which you want data lineage node history to be sorted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_lineage_node_history_input.ListLineageNodeHistoryInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_lineage_node_history_output.ListLineageNodeHistoryOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_lineage_node_history

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_lineage_node_history.async_list_lineage_node_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_lineage_node_history_input.ListLineageNodeHistoryInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["identifier"] = identifier
        if direction is not None:
            input_["direction"] = direction
        if event_timestamp_gte is not None:
            input_["event_timestamp_gte"] = event_timestamp_gte
        if event_timestamp_lte is not None:
            input_["event_timestamp_lte"] = event_timestamp_lte
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_lineage_node_history(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.lineage_node_identifier.LineageNodeIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        direction: Optional[
            "aws_sdk_datazone.types.edge_direction.EdgeDirection"
        ] = None,
        event_timestamp_gte: Optional[datetime.datetime] = None,
        event_timestamp_lte: Optional[datetime.datetime] = None,
        sort_order: Optional["aws_sdk_datazone.types.sort_order.SortOrder"] = None,
    ) -> (
        "AsyncIterator[aws_sdk_datazone.types.lineage_node_summary.LineageNodeSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.list_lineage_node_history(
                domain_identifier,
                identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                direction=direction,
                event_timestamp_gte=event_timestamp_gte,
                event_timestamp_lte=event_timestamp_lte,
                sort_order=sort_order,
            )
            _page = _resolve_path(_response, ("nodes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_notifications(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        type: "aws_sdk_datazone.types.notification_type.NotificationType",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        after_timestamp: Optional[datetime.datetime] = None,
        before_timestamp: Optional[datetime.datetime] = None,
        subjects: Optional[
            "aws_sdk_datazone.types.notification_subjects.NotificationSubjects"
        ] = None,
        task_status: Optional["aws_sdk_datazone.types.task_status.TaskStatus"] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.list_notifications_output.ListNotificationsOutput":
        """<p>Lists all Amazon DataZone notifications.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            type: <p>The type of notifications.</p>
            after_timestamp: <p>The time after which you want to list notifications.</p>
            before_timestamp: <p>The time before which you want to list notifications.</p>
            subjects: <p>The subjects of notifications.</p>
            task_status: <p>The task status of notifications.</p>
            max_results: <p>The maximum number of notifications to return in a single call to <code>ListNotifications</code>. When the number of notifications to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListNotifications</code> to list the next set of notifications.</p>
            next_token: <p>When the number of notifications is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of notifications, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListNotifications</code> to list the next set of notifications.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_notifications_input.ListNotificationsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_notifications_output.ListNotificationsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_notifications

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_notifications.async_list_notifications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_notifications_input.ListNotificationsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["type"] = type
        if after_timestamp is not None:
            input_["after_timestamp"] = after_timestamp
        if before_timestamp is not None:
            input_["before_timestamp"] = before_timestamp
        if subjects is not None:
            input_["subjects"] = subjects
        if task_status is not None:
            input_["task_status"] = task_status
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_notifications(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        type: "aws_sdk_datazone.types.notification_type.NotificationType",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        after_timestamp: Optional[datetime.datetime] = None,
        before_timestamp: Optional[datetime.datetime] = None,
        subjects: Optional[
            "aws_sdk_datazone.types.notification_subjects.NotificationSubjects"
        ] = None,
        task_status: Optional["aws_sdk_datazone.types.task_status.TaskStatus"] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_datazone.types.notification_output.NotificationOutput]":
        _token = next_token
        while True:
            _response = await self.list_notifications(
                domain_identifier,
                type,
                config_overrides=config_overrides,
                after_timestamp=after_timestamp,
                before_timestamp=before_timestamp,
                subjects=subjects,
                task_status=task_status,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("notifications",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_policy_grants(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        entity_type: "aws_sdk_datazone.types.target_entity_type.TargetEntityType",
        entity_identifier: str,
        policy_type: "aws_sdk_datazone.types.managed_policy_type.ManagedPolicyType",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional[
            "aws_sdk_datazone.types.max_results_for_list_domains.MaxResultsForListDomains"
        ] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.list_policy_grants_output.ListPolicyGrantsOutput":
        """<p>Lists policy grants.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to list policy grants.</p>
            entity_type: <p>The type of entity for which you want to list policy grants.</p>
            entity_identifier: <p>The ID of the entity for which you want to list policy grants.</p>
            policy_type: <p>The type of policy that you want to list.</p>
            max_results: <p>The maximum number of grants to return in a single call to <code>ListPolicyGrants</code>. When the number of grants to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListPolicyGrants</code> to list the next set of grants.</p>
            next_token: <p>When the number of grants is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of grants, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListPolicyGrants</code> to list the next set of grants.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_policy_grants_input.ListPolicyGrantsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_policy_grants_output.ListPolicyGrantsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_policy_grants

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_policy_grants.async_list_policy_grants(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_policy_grants_input.ListPolicyGrantsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["entity_type"] = entity_type
        input_["entity_identifier"] = entity_identifier
        input_["policy_type"] = policy_type
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_policy_grants(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        entity_type: "aws_sdk_datazone.types.target_entity_type.TargetEntityType",
        entity_identifier: str,
        policy_type: "aws_sdk_datazone.types.managed_policy_type.ManagedPolicyType",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional[
            "aws_sdk_datazone.types.max_results_for_list_domains.MaxResultsForListDomains"
        ] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_datazone.types.policy_grant_member.PolicyGrantMember]":
        _token = next_token
        while True:
            _response = await self.list_policy_grants(
                domain_identifier,
                entity_type,
                entity_identifier,
                policy_type,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("grant_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_project_memberships(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        project_identifier: "aws_sdk_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        sort_by: Optional[
            "aws_sdk_datazone.types.sort_field_project.SortFieldProject"
        ] = None,
        sort_order: Optional["aws_sdk_datazone.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_datazone.types.list_project_memberships_output.ListProjectMembershipsOutput":
        """<p>Lists all members of the specified project.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which you want to list project memberships.</p>
            project_identifier: <p>The identifier of the project whose memberships you want to list.</p>
            sort_by: <p>The method by which you want to sort the project memberships.</p>
            sort_order: <p>The sort order of the project memberships.</p>
            next_token: <p>When the number of memberships is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of memberships, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListProjectMemberships</code> to list the next set of memberships.</p>
            max_results: <p>The maximum number of memberships to return in a single call to <code>ListProjectMemberships</code>. When the number of memberships to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListProjectMemberships</code> to list the next set of memberships.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_project_memberships_input.ListProjectMembershipsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_project_memberships_output.ListProjectMembershipsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_project_memberships

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_project_memberships.async_list_project_memberships(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_project_memberships_input.ListProjectMembershipsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["project_identifier"] = project_identifier
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
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

    async def iter_list_project_memberships(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        project_identifier: "aws_sdk_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        sort_by: Optional[
            "aws_sdk_datazone.types.sort_field_project.SortFieldProject"
        ] = None,
        sort_order: Optional["aws_sdk_datazone.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[aws_sdk_datazone.types.project_member.ProjectMember]":
        _token = next_token
        while True:
            _response = await self.list_project_memberships(
                domain_identifier,
                project_identifier,
                config_overrides=config_overrides,
                sort_by=sort_by,
                sort_order=sort_order,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("members",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_project_profiles(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        name: Optional[
            "aws_sdk_datazone.types.project_profile_name.ProjectProfileName"
        ] = None,
        sort_by: Optional[
            "aws_sdk_datazone.types.sort_field_project.SortFieldProject"
        ] = None,
        sort_order: Optional["aws_sdk_datazone.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
    ) -> (
        "aws_sdk_datazone.types.list_project_profiles_output.ListProjectProfilesOutput"
    ):
        """<p>Lists project profiles.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to list project profiles.</p>
            name: <p>The name of a project profile.</p>
            sort_by: <p>Specifies by what to sort project profiles.</p>
            sort_order: <p>Specifies the sort order of the project profiles.</p>
            next_token: <p>When the number of project profiles is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of project profiles, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListProjectProfiles to list the next set of project profiles.</p>
            max_results: <p>The maximum number of project profiles to return in a single call to ListProjectProfiles. When the number of project profiles to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListProjectProfiles to list the next set of project profiles.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_project_profiles_input.ListProjectProfilesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_project_profiles_output.ListProjectProfilesOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_project_profiles

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_project_profiles.async_list_project_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_project_profiles_input.ListProjectProfilesInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        if name is not None:
            input_["name"] = name
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
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

    async def iter_list_project_profiles(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        name: Optional[
            "aws_sdk_datazone.types.project_profile_name.ProjectProfileName"
        ] = None,
        sort_by: Optional[
            "aws_sdk_datazone.types.sort_field_project.SortFieldProject"
        ] = None,
        sort_order: Optional["aws_sdk_datazone.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[aws_sdk_datazone.types.project_profile_summary.ProjectProfileSummary]":
        _token = next_token
        while True:
            _response = await self.list_project_profiles(
                domain_identifier,
                config_overrides=config_overrides,
                name=name,
                sort_by=sort_by,
                sort_order=sort_order,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_projects(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        user_identifier: Optional[str] = None,
        group_identifier: Optional[str] = None,
        name: Optional["aws_sdk_datazone.types.project_name.ProjectName"] = None,
        project_category: Optional[str] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_datazone.types.list_projects_output.ListProjectsOutput":
        """<p>Lists Amazon DataZone projects.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            user_identifier: <p>The identifier of the Amazon DataZone user.</p>
            group_identifier: <p>The identifier of a group.</p>
            name: <p>The name of the project.</p>
            project_category: <p>A parameter to filter projects by their category.</p>
            next_token: <p>When the number of projects is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of projects, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListProjects</code> to list the next set of projects.</p>
            max_results: <p>The maximum number of projects to return in a single call to <code>ListProjects</code>. When the number of projects to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListProjects</code> to list the next set of projects.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_projects_input.ListProjectsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_projects_output.ListProjectsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_projects

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_projects.async_list_projects(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_projects_input.ListProjectsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        if user_identifier is not None:
            input_["user_identifier"] = user_identifier
        if group_identifier is not None:
            input_["group_identifier"] = group_identifier
        if name is not None:
            input_["name"] = name
        if project_category is not None:
            input_["project_category"] = project_category
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
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        user_identifier: Optional[str] = None,
        group_identifier: Optional[str] = None,
        name: Optional["aws_sdk_datazone.types.project_name.ProjectName"] = None,
        project_category: Optional[str] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[aws_sdk_datazone.types.project_summary.ProjectSummary]":
        _token = next_token
        while True:
            _response = await self.list_projects(
                domain_identifier,
                config_overrides=config_overrides,
                user_identifier=user_identifier,
                group_identifier=group_identifier,
                name=name,
                project_category=project_category,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_subscription_grants(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        environment_id: Optional[
            "aws_sdk_datazone.types.environment_id.EnvironmentId"
        ] = None,
        subscription_target_id: Optional[
            "aws_sdk_datazone.types.subscription_target_id.SubscriptionTargetId"
        ] = None,
        subscribed_listing_id: Optional[
            "aws_sdk_datazone.types.listing_id.ListingId"
        ] = None,
        subscription_id: Optional[
            "aws_sdk_datazone.types.subscription_id.SubscriptionId"
        ] = None,
        owning_project_id: Optional[
            "aws_sdk_datazone.types.project_id.ProjectId"
        ] = None,
        owning_iam_principal_arn: Optional[
            "aws_sdk_datazone.types.iam_principal_arn.IamPrincipalArn"
        ] = None,
        owning_user_id: Optional[
            "aws_sdk_datazone.types.user_profile_id.UserProfileId"
        ] = None,
        owning_group_id: Optional[
            "aws_sdk_datazone.types.group_profile_id.GroupProfileId"
        ] = None,
        sort_by: Optional["aws_sdk_datazone.types.sort_key.SortKey"] = None,
        sort_order: Optional["aws_sdk_datazone.types.sort_order.SortOrder"] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.list_subscription_grants_output.ListSubscriptionGrantsOutput":
        """<p>Lists subscription grants.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            environment_id: <p>The identifier of the Amazon DataZone environment.</p>
            subscription_target_id: <p>The identifier of the subscription target.</p>
            subscribed_listing_id: <p>The identifier of the subscribed listing.</p>
            subscription_id: <p>The identifier of the subscription.</p>
            owning_project_id: <p>The ID of the owning project of the subscription grants.</p>
            owning_iam_principal_arn: <p>The ARN of the owning IAM principal.</p>
            owning_user_id: <p>The ID of the owning user.</p>
            owning_group_id: <p>The ID of the owning group.</p>
            sort_by: <p>Specifies the way of sorting the results of this action.</p>
            sort_order: <p>Specifies the sort order of this action.</p>
            max_results: <p>The maximum number of subscription grants to return in a single call to <code>ListSubscriptionGrants</code>. When the number of subscription grants to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListSubscriptionGrants</code> to list the next set of subscription grants.</p>
            next_token: <p>When the number of subscription grants is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of subscription grants, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListSubscriptionGrants</code> to list the next set of subscription grants.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_subscription_grants_input.ListSubscriptionGrantsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_subscription_grants_output.ListSubscriptionGrantsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_subscription_grants

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_subscription_grants.async_list_subscription_grants(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_subscription_grants_input.ListSubscriptionGrantsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        if environment_id is not None:
            input_["environment_id"] = environment_id
        if subscription_target_id is not None:
            input_["subscription_target_id"] = subscription_target_id
        if subscribed_listing_id is not None:
            input_["subscribed_listing_id"] = subscribed_listing_id
        if subscription_id is not None:
            input_["subscription_id"] = subscription_id
        if owning_project_id is not None:
            input_["owning_project_id"] = owning_project_id
        if owning_iam_principal_arn is not None:
            input_["owning_iam_principal_arn"] = owning_iam_principal_arn
        if owning_user_id is not None:
            input_["owning_user_id"] = owning_user_id
        if owning_group_id is not None:
            input_["owning_group_id"] = owning_group_id
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_subscription_grants(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        environment_id: Optional[
            "aws_sdk_datazone.types.environment_id.EnvironmentId"
        ] = None,
        subscription_target_id: Optional[
            "aws_sdk_datazone.types.subscription_target_id.SubscriptionTargetId"
        ] = None,
        subscribed_listing_id: Optional[
            "aws_sdk_datazone.types.listing_id.ListingId"
        ] = None,
        subscription_id: Optional[
            "aws_sdk_datazone.types.subscription_id.SubscriptionId"
        ] = None,
        owning_project_id: Optional[
            "aws_sdk_datazone.types.project_id.ProjectId"
        ] = None,
        owning_iam_principal_arn: Optional[
            "aws_sdk_datazone.types.iam_principal_arn.IamPrincipalArn"
        ] = None,
        owning_user_id: Optional[
            "aws_sdk_datazone.types.user_profile_id.UserProfileId"
        ] = None,
        owning_group_id: Optional[
            "aws_sdk_datazone.types.group_profile_id.GroupProfileId"
        ] = None,
        sort_by: Optional["aws_sdk_datazone.types.sort_key.SortKey"] = None,
        sort_order: Optional["aws_sdk_datazone.types.sort_order.SortOrder"] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_datazone.types.subscription_grant_summary.SubscriptionGrantSummary]":
        _token = next_token
        while True:
            _response = await self.list_subscription_grants(
                domain_identifier,
                config_overrides=config_overrides,
                environment_id=environment_id,
                subscription_target_id=subscription_target_id,
                subscribed_listing_id=subscribed_listing_id,
                subscription_id=subscription_id,
                owning_project_id=owning_project_id,
                owning_iam_principal_arn=owning_iam_principal_arn,
                owning_user_id=owning_user_id,
                owning_group_id=owning_group_id,
                sort_by=sort_by,
                sort_order=sort_order,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_subscription_requests(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional[
            "aws_sdk_datazone.types.subscription_request_status.SubscriptionRequestStatus"
        ] = None,
        subscribed_listing_id: Optional[
            "aws_sdk_datazone.types.listing_id.ListingId"
        ] = None,
        owning_project_id: Optional[
            "aws_sdk_datazone.types.project_id.ProjectId"
        ] = None,
        owning_iam_principal_arn: Optional[
            "aws_sdk_datazone.types.iam_principal_arn.IamPrincipalArn"
        ] = None,
        approver_project_id: Optional[
            "aws_sdk_datazone.types.project_id.ProjectId"
        ] = None,
        owning_user_id: Optional[
            "aws_sdk_datazone.types.user_profile_id.UserProfileId"
        ] = None,
        owning_group_id: Optional[
            "aws_sdk_datazone.types.group_profile_id.GroupProfileId"
        ] = None,
        sort_by: Optional["aws_sdk_datazone.types.sort_key.SortKey"] = None,
        sort_order: Optional["aws_sdk_datazone.types.sort_order.SortOrder"] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.list_subscription_requests_output.ListSubscriptionRequestsOutput":
        """<p>Lists Amazon DataZone subscription requests.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            status: <p>Specifies the status of the subscription requests.</p> <note> <p>This is not a required parameter, but if not specified, by default, Amazon DataZone returns only <code>PENDING</code> subscription requests. </p> </note>
            subscribed_listing_id: <p>The identifier of the subscribed listing.</p>
            owning_project_id: <p>The identifier of the project for the subscription requests.</p>
            owning_iam_principal_arn: <p>The ARN of the owning IAM principal.</p>
            approver_project_id: <p>The identifier of the subscription request approver's project.</p>
            owning_user_id: <p>The ID of the owning user.</p>
            owning_group_id: <p>The ID of the owning group.</p>
            sort_by: <p>Specifies the way to sort the results of this action.</p>
            sort_order: <p>Specifies the sort order for the results of this action.</p>
            max_results: <p>The maximum number of subscription requests to return in a single call to <code>ListSubscriptionRequests</code>. When the number of subscription requests to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListSubscriptionRequests</code> to list the next set of subscription requests.</p>
            next_token: <p>When the number of subscription requests is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of subscription requests, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListSubscriptionRequests</code> to list the next set of subscription requests.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_subscription_requests_input.ListSubscriptionRequestsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_subscription_requests_output.ListSubscriptionRequestsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_subscription_requests

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_subscription_requests.async_list_subscription_requests(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_subscription_requests_input.ListSubscriptionRequestsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        if status is not None:
            input_["status"] = status
        if subscribed_listing_id is not None:
            input_["subscribed_listing_id"] = subscribed_listing_id
        if owning_project_id is not None:
            input_["owning_project_id"] = owning_project_id
        if owning_iam_principal_arn is not None:
            input_["owning_iam_principal_arn"] = owning_iam_principal_arn
        if approver_project_id is not None:
            input_["approver_project_id"] = approver_project_id
        if owning_user_id is not None:
            input_["owning_user_id"] = owning_user_id
        if owning_group_id is not None:
            input_["owning_group_id"] = owning_group_id
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_subscription_requests(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional[
            "aws_sdk_datazone.types.subscription_request_status.SubscriptionRequestStatus"
        ] = None,
        subscribed_listing_id: Optional[
            "aws_sdk_datazone.types.listing_id.ListingId"
        ] = None,
        owning_project_id: Optional[
            "aws_sdk_datazone.types.project_id.ProjectId"
        ] = None,
        owning_iam_principal_arn: Optional[
            "aws_sdk_datazone.types.iam_principal_arn.IamPrincipalArn"
        ] = None,
        approver_project_id: Optional[
            "aws_sdk_datazone.types.project_id.ProjectId"
        ] = None,
        owning_user_id: Optional[
            "aws_sdk_datazone.types.user_profile_id.UserProfileId"
        ] = None,
        owning_group_id: Optional[
            "aws_sdk_datazone.types.group_profile_id.GroupProfileId"
        ] = None,
        sort_by: Optional["aws_sdk_datazone.types.sort_key.SortKey"] = None,
        sort_order: Optional["aws_sdk_datazone.types.sort_order.SortOrder"] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_datazone.types.subscription_request_summary.SubscriptionRequestSummary]":
        _token = next_token
        while True:
            _response = await self.list_subscription_requests(
                domain_identifier,
                config_overrides=config_overrides,
                status=status,
                subscribed_listing_id=subscribed_listing_id,
                owning_project_id=owning_project_id,
                owning_iam_principal_arn=owning_iam_principal_arn,
                approver_project_id=approver_project_id,
                owning_user_id=owning_user_id,
                owning_group_id=owning_group_id,
                sort_by=sort_by,
                sort_order=sort_order,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_subscriptions(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        subscription_request_identifier: Optional[
            "aws_sdk_datazone.types.subscription_request_id.SubscriptionRequestId"
        ] = None,
        status: Optional[
            "aws_sdk_datazone.types.subscription_status.SubscriptionStatus"
        ] = None,
        subscribed_listing_id: Optional[
            "aws_sdk_datazone.types.listing_id.ListingId"
        ] = None,
        owning_project_id: Optional[
            "aws_sdk_datazone.types.project_id.ProjectId"
        ] = None,
        owning_iam_principal_arn: Optional[
            "aws_sdk_datazone.types.iam_principal_arn.IamPrincipalArn"
        ] = None,
        owning_user_id: Optional[
            "aws_sdk_datazone.types.user_profile_id.UserProfileId"
        ] = None,
        owning_group_id: Optional[
            "aws_sdk_datazone.types.group_profile_id.GroupProfileId"
        ] = None,
        approver_project_id: Optional[
            "aws_sdk_datazone.types.project_id.ProjectId"
        ] = None,
        sort_by: Optional["aws_sdk_datazone.types.sort_key.SortKey"] = None,
        sort_order: Optional["aws_sdk_datazone.types.sort_order.SortOrder"] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.list_subscriptions_output.ListSubscriptionsOutput":
        """<p>Lists subscriptions in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            subscription_request_identifier: <p>The identifier of the subscription request for the subscriptions that you want to list.</p>
            status: <p>The status of the subscriptions that you want to list.</p> <note> <p>This is not a required parameter, but if not provided, by default, Amazon DataZone returns only <code>APPROVED</code> subscriptions. </p> </note>
            subscribed_listing_id: <p>The identifier of the subscribed listing for the subscriptions that you want to list.</p>
            owning_project_id: <p>The identifier of the owning project.</p>
            owning_iam_principal_arn: <p>The ARN of the owning IAM principal.</p>
            owning_user_id: <p>The ID of the owning user.</p>
            owning_group_id: <p>The ID of the owning group.</p>
            approver_project_id: <p>The identifier of the project for the subscription's approver.</p>
            sort_by: <p>Specifies the way in which the results of this action are to be sorted.</p>
            sort_order: <p>Specifies the sort order for the results of this action.</p>
            max_results: <p>The maximum number of subscriptions to return in a single call to <code>ListSubscriptions</code>. When the number of subscriptions to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListSubscriptions</code> to list the next set of Subscriptions. </p>
            next_token: <p>When the number of subscriptions is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of subscriptions, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListSubscriptions</code> to list the next set of subscriptions.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_subscriptions_input.ListSubscriptionsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_subscriptions_output.ListSubscriptionsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_subscriptions

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_subscriptions.async_list_subscriptions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_subscriptions_input.ListSubscriptionsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        if subscription_request_identifier is not None:
            input_["subscription_request_identifier"] = subscription_request_identifier
        if status is not None:
            input_["status"] = status
        if subscribed_listing_id is not None:
            input_["subscribed_listing_id"] = subscribed_listing_id
        if owning_project_id is not None:
            input_["owning_project_id"] = owning_project_id
        if owning_iam_principal_arn is not None:
            input_["owning_iam_principal_arn"] = owning_iam_principal_arn
        if owning_user_id is not None:
            input_["owning_user_id"] = owning_user_id
        if owning_group_id is not None:
            input_["owning_group_id"] = owning_group_id
        if approver_project_id is not None:
            input_["approver_project_id"] = approver_project_id
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_subscriptions(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        subscription_request_identifier: Optional[
            "aws_sdk_datazone.types.subscription_request_id.SubscriptionRequestId"
        ] = None,
        status: Optional[
            "aws_sdk_datazone.types.subscription_status.SubscriptionStatus"
        ] = None,
        subscribed_listing_id: Optional[
            "aws_sdk_datazone.types.listing_id.ListingId"
        ] = None,
        owning_project_id: Optional[
            "aws_sdk_datazone.types.project_id.ProjectId"
        ] = None,
        owning_iam_principal_arn: Optional[
            "aws_sdk_datazone.types.iam_principal_arn.IamPrincipalArn"
        ] = None,
        owning_user_id: Optional[
            "aws_sdk_datazone.types.user_profile_id.UserProfileId"
        ] = None,
        owning_group_id: Optional[
            "aws_sdk_datazone.types.group_profile_id.GroupProfileId"
        ] = None,
        approver_project_id: Optional[
            "aws_sdk_datazone.types.project_id.ProjectId"
        ] = None,
        sort_by: Optional["aws_sdk_datazone.types.sort_key.SortKey"] = None,
        sort_order: Optional["aws_sdk_datazone.types.sort_order.SortOrder"] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> (
        "AsyncIterator[aws_sdk_datazone.types.subscription_summary.SubscriptionSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.list_subscriptions(
                domain_identifier,
                config_overrides=config_overrides,
                subscription_request_identifier=subscription_request_identifier,
                status=status,
                subscribed_listing_id=subscribed_listing_id,
                owning_project_id=owning_project_id,
                owning_iam_principal_arn=owning_iam_principal_arn,
                owning_user_id=owning_user_id,
                owning_group_id=owning_group_id,
                approver_project_id=approver_project_id,
                sort_by=sort_by,
                sort_order=sort_order,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_subscription_targets(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        environment_identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        sort_by: Optional["aws_sdk_datazone.types.sort_key.SortKey"] = None,
        sort_order: Optional["aws_sdk_datazone.types.sort_order.SortOrder"] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.list_subscription_targets_output.ListSubscriptionTargetsOutput":
        """<p>Lists subscription targets in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain where you want to list subscription targets.</p>
            environment_identifier: <p>The identifier of the environment where you want to list subscription targets.</p>
            sort_by: <p>Specifies the way in which the results of this action are to be sorted.</p>
            sort_order: <p>Specifies the sort order for the results of this action.</p>
            max_results: <p>The maximum number of subscription targets to return in a single call to <code>ListSubscriptionTargets</code>. When the number of subscription targets to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListSubscriptionTargets</code> to list the next set of subscription targets. </p>
            next_token: <p>When the number of subscription targets is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of subscription targets, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListSubscriptionTargets</code> to list the next set of subscription targets.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_subscription_targets_input.ListSubscriptionTargetsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_subscription_targets_output.ListSubscriptionTargetsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_subscription_targets

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_subscription_targets.async_list_subscription_targets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_subscription_targets_input.ListSubscriptionTargetsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["environment_identifier"] = environment_identifier
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_subscription_targets(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        environment_identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        sort_by: Optional["aws_sdk_datazone.types.sort_key.SortKey"] = None,
        sort_order: Optional["aws_sdk_datazone.types.sort_order.SortOrder"] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_datazone.types.subscription_target_summary.SubscriptionTargetSummary]":
        _token = next_token
        while True:
            _response = await self.list_subscription_targets(
                domain_identifier,
                environment_identifier,
                config_overrides=config_overrides,
                sort_by=sort_by,
                sort_order=sort_order,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists tags for the specified resource in Amazon DataZone.</p>

        Args:
            resource_arn: <p>The ARN of the resource whose tags you want to list.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_time_series_data_points(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        entity_identifier: "aws_sdk_datazone.types.entity_identifier.EntityIdentifier",
        entity_type: "aws_sdk_datazone.types.time_series_entity_type.TimeSeriesEntityType",
        form_name: "aws_sdk_datazone.types.time_series_form_name.TimeSeriesFormName",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        started_at: Optional[datetime.datetime] = None,
        ended_at: Optional[datetime.datetime] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_datazone.types.list_time_series_data_points_output.ListTimeSeriesDataPointsOutput":
        """<p>Lists time series data points.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain that houses the assets for which you want to list time series data points.</p>
            entity_identifier: <p>The ID of the asset for which you want to list data points.</p>
            entity_type: <p>The type of the asset for which you want to list data points.</p>
            form_name: <p>The name of the time series data points form.</p>
            started_at: <p>The timestamp at which the data points that you want to list started.</p>
            ended_at: <p>The timestamp at which the data points that you wanted to list ended.</p>
            next_token: <p>When the number of data points is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of data points, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListTimeSeriesDataPoints to list the next set of data points.</p>
            max_results: <p>The maximum number of data points to return in a single call to ListTimeSeriesDataPoints. When the number of data points to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListTimeSeriesDataPoints to list the next set of data points.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_time_series_data_points_input.ListTimeSeriesDataPointsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_time_series_data_points_output.ListTimeSeriesDataPointsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_time_series_data_points

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_time_series_data_points.async_list_time_series_data_points(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_time_series_data_points_input.ListTimeSeriesDataPointsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["entity_identifier"] = entity_identifier
        input_["entity_type"] = entity_type
        input_["form_name"] = form_name
        if started_at is not None:
            input_["started_at"] = started_at
        if ended_at is not None:
            input_["ended_at"] = ended_at
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

    async def iter_list_time_series_data_points(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        entity_identifier: "aws_sdk_datazone.types.entity_identifier.EntityIdentifier",
        entity_type: "aws_sdk_datazone.types.time_series_entity_type.TimeSeriesEntityType",
        form_name: "aws_sdk_datazone.types.time_series_form_name.TimeSeriesFormName",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        started_at: Optional[datetime.datetime] = None,
        ended_at: Optional[datetime.datetime] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[aws_sdk_datazone.types.time_series_data_point_summary_form_output.TimeSeriesDataPointSummaryFormOutput]":
        _token = next_token
        while True:
            _response = await self.list_time_series_data_points(
                domain_identifier,
                entity_identifier,
                entity_type,
                form_name,
                config_overrides=config_overrides,
                started_at=started_at,
                ended_at=ended_at,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def post_lineage_event(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        event: "aws_sdk_datazone.types.lineage_event.LineageEvent",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.post_lineage_event_output.PostLineageEventOutput":
        """<p>Posts a data lineage event.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to post a data lineage event.</p>
            event: <p>The data lineage event that you want to post. Only open-lineage run event are supported as events. </p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.post_lineage_event_input.PostLineageEventInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.post_lineage_event_output.PostLineageEventOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.post_lineage_event

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.post_lineage_event.async_post_lineage_event(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.post_lineage_event_input.PostLineageEventInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["event"] = event
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def post_time_series_data_points(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        entity_identifier: "aws_sdk_datazone.types.entity_identifier.EntityIdentifier",
        entity_type: "aws_sdk_datazone.types.time_series_entity_type.TimeSeriesEntityType",
        forms: "aws_sdk_datazone.types.time_series_data_point_form_input_list.TimeSeriesDataPointFormInputList",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.post_time_series_data_points_output.PostTimeSeriesDataPointsOutput":
        """<p>Posts time series data points to Amazon DataZone for the specified asset.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which you want to post time series data points.</p>
            entity_identifier: <p>The ID of the asset for which you want to post time series data points.</p>
            entity_type: <p>The type of the asset for which you want to post data points.</p>
            forms: <p>The forms that contain the data points that you want to post.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.post_time_series_data_points_input.PostTimeSeriesDataPointsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.post_time_series_data_points_output.PostTimeSeriesDataPointsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.post_time_series_data_points

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.post_time_series_data_points.async_post_time_series_data_points(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.post_time_series_data_points_input.PostTimeSeriesDataPointsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["entity_identifier"] = entity_identifier
        input_["entity_type"] = entity_type
        input_["forms"] = forms
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_data_export_configuration(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        enable_export: bool,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        encryption_configuration: Optional[
            "aws_sdk_datazone.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.put_data_export_configuration_output.PutDataExportConfigurationOutput":
        r"""<p>Creates data export configuration details.</p> <p>If you want to temporarily disable export and later re-enable it for the same domain, use the <code>--no-enable-export</code> flag to disable and the <code>--enable-export</code> flag to re-enable. This preserves the configuration and allows you to re-enable export without deleting S3 table.</p> <note> <p>You can enable asset metadata export for only one domain per account per Region. To enable export for a different domain, complete the following steps:</p> <ol> <li> <p>Delete the export configuration for the currently enabled domain using the DeleteDataExportConfiguration operation.</p> </li> <li> <p>Delete the asset S3 table under the aws-sagemaker-catalog S3 table bucket. We recommend backing up the S3 table before deletion.</p> </li> <li> <p>Call the PutDataExportConfiguration API to enable export for the new domain.</p> </li> </ol> </note>

        Args:
            domain_identifier: <p>The domain ID for which you want to create data export configuration details.</p>
            enable_export: <p>Specifies that the export is to be enabled as part of creating data export configuration details.</p>
            encryption_configuration: <p>The encryption configuration as part of creating data export configuration details.</p> <p>The KMS key provided here as part of encryptionConfiguration must have the required permissions as described in <a href=\"https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/sagemaker-unified-studio-export-asset-metadata-kms-permissions.html\">KMS permissions for exporting asset metadata in Amazon SageMaker Unified Studio</a>.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.put_data_export_configuration_input.PutDataExportConfigurationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.put_data_export_configuration_output.PutDataExportConfigurationOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.put_data_export_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.put_data_export_configuration.async_put_data_export_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.put_data_export_configuration_input.PutDataExportConfigurationInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["enable_export"] = enable_export
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def query_graph(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        match: "aws_sdk_datazone.types.match_clauses.MatchClauses",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        additional_attributes: Optional[
            "aws_sdk_datazone.types.additional_attributes.AdditionalAttributes"
        ] = None,
    ) -> "aws_sdk_datazone.types.query_graph_output.QueryGraphOutput":
        """<p>Queries entities in the graph store.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            match: <p>List of query match clauses.</p>
            max_results: <p>The maximum number of entities to return in a single call to <code>QueryGraph</code>. When the number of entities to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>QueryGraph</code> to list the next set of entities.</p>
            next_token: <p>When the number of entities is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of entities, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>QueryGraph</code> to list the next set of entities.</p>
            additional_attributes: <p>Additional details on the queried entity that can be requested in the response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.query_graph_input.QueryGraphInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.query_graph_output.QueryGraphOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.query_graph

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.query_graph.async_query_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.query_graph_input.QueryGraphInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["match"] = match
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if additional_attributes is not None:
            input_["additional_attributes"] = additional_attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_query_graph(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        match: "aws_sdk_datazone.types.match_clauses.MatchClauses",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        additional_attributes: Optional[
            "aws_sdk_datazone.types.additional_attributes.AdditionalAttributes"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_datazone.types.result_item.ResultItem]":
        _token = next_token
        while True:
            _response = await self.query_graph(
                domain_identifier,
                match,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                additional_attributes=additional_attributes,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def reject_predictions(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.asset_identifier.AssetIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        revision: Optional["aws_sdk_datazone.types.revision.Revision"] = None,
        reject_rule: Optional["aws_sdk_datazone.types.reject_rule.RejectRule"] = None,
        reject_choices: Optional[
            "aws_sdk_datazone.types.reject_choices.RejectChoices"
        ] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.reject_predictions_output.RejectPredictionsOutput":
        """<p>Rejects automatically generated business-friendly metadata for your Amazon DataZone assets.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            identifier: <p>The identifier of the prediction.</p>
            revision: <p>The revision that is to be made to the asset.</p>
            reject_rule: <p>Specifies the rule (or the conditions) under which a prediction can be rejected.</p>
            reject_choices: <p>Specifies the prediction (aka, the automatically generated piece of metadata) and the target (for example, a column name) that can be rejected.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.reject_predictions_input.RejectPredictionsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.reject_predictions_output.RejectPredictionsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.reject_predictions

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.reject_predictions.async_reject_predictions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.reject_predictions_input.RejectPredictionsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        if revision is not None:
            input_["revision"] = revision
        if reject_rule is not None:
            input_["reject_rule"] = reject_rule
        if reject_choices is not None:
            input_["reject_choices"] = reject_choices
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def reject_subscription_request(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.subscription_request_id.SubscriptionRequestId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        decision_comment: Optional[
            "aws_sdk_datazone.types.decision_comment.DecisionComment"
        ] = None,
    ) -> "aws_sdk_datazone.types.reject_subscription_request_output.RejectSubscriptionRequestOutput":
        """<p>Rejects the specified subscription request.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which the subscription request was rejected.</p>
            identifier: <p>The identifier of the subscription request that was rejected.</p>
            decision_comment: <p>The decision comment of the rejected subscription request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.reject_subscription_request_input.RejectSubscriptionRequestInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.reject_subscription_request_output.RejectSubscriptionRequestOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.reject_subscription_request

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.reject_subscription_request.async_reject_subscription_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.reject_subscription_request_input.RejectSubscriptionRequestInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        if decision_comment is not None:
            input_["decision_comment"] = decision_comment

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def remove_entity_owner(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        entity_type: "aws_sdk_datazone.types.data_zone_entity_type.DataZoneEntityType",
        entity_identifier: str,
        owner: "aws_sdk_datazone.types.owner_properties.OwnerProperties",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.remove_entity_owner_output.RemoveEntityOwnerOutput":
        """<p>Removes an owner from an entity.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to remove an owner from an entity.</p>
            entity_type: <p>The type of the entity from which you want to remove an owner.</p>
            entity_identifier: <p>The ID of the entity from which you want to remove an owner.</p>
            owner: <p>The owner that you want to remove from an entity.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.remove_entity_owner_input.RemoveEntityOwnerInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.remove_entity_owner_output.RemoveEntityOwnerOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.remove_entity_owner

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.remove_entity_owner.async_remove_entity_owner(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.remove_entity_owner_input.RemoveEntityOwnerInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["entity_type"] = entity_type
        input_["entity_identifier"] = entity_identifier
        input_["owner"] = owner
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def remove_policy_grant(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        entity_type: "aws_sdk_datazone.types.target_entity_type.TargetEntityType",
        entity_identifier: str,
        policy_type: "aws_sdk_datazone.types.managed_policy_type.ManagedPolicyType",
        principal: "aws_sdk_datazone.types.policy_grant_principal.PolicyGrantPrincipal",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        grant_identifier: Optional[
            "aws_sdk_datazone.types.grant_identifier.GrantIdentifier"
        ] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.remove_policy_grant_output.RemovePolicyGrantOutput":
        """<p>Removes a policy grant.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to remove a policy grant.</p>
            entity_type: <p>The type of the entity from which you want to remove a policy grant.</p>
            entity_identifier: <p>The ID of the entity from which you want to remove a policy grant.</p>
            policy_type: <p>The type of the policy that you want to remove.</p>
            principal: <p>The principal from which you want to remove a policy grant.</p>
            grant_identifier: <p>The ID of the policy grant that is to be removed from a specified entity.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.remove_policy_grant_input.RemovePolicyGrantInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.remove_policy_grant_output.RemovePolicyGrantOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.remove_policy_grant

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.remove_policy_grant.async_remove_policy_grant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.remove_policy_grant_input.RemovePolicyGrantInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["entity_type"] = entity_type
        input_["entity_identifier"] = entity_identifier
        input_["policy_type"] = policy_type
        input_["principal"] = principal
        if grant_identifier is not None:
            input_["grant_identifier"] = grant_identifier
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def revoke_subscription(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.subscription_id.SubscriptionId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        retain_permissions: Optional[bool] = None,
    ) -> "aws_sdk_datazone.types.revoke_subscription_output.RevokeSubscriptionOutput":
        """<p>Revokes a specified subscription in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain where you want to revoke a subscription.</p>
            identifier: <p>The identifier of the revoked subscription.</p>
            retain_permissions: <p>Specifies whether permissions are retained when the subscription is revoked.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.revoke_subscription_input.RevokeSubscriptionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.revoke_subscription_output.RevokeSubscriptionOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.revoke_subscription

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.revoke_subscription.async_revoke_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.revoke_subscription_input.RevokeSubscriptionInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        if retain_permissions is not None:
            input_["retain_permissions"] = retain_permissions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def search(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        search_scope: "aws_sdk_datazone.types.inventory_search_scope.InventorySearchScope",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        owning_project_identifier: Optional[
            "aws_sdk_datazone.types.project_id.ProjectId"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        search_text: Optional["aws_sdk_datazone.types.search_text.SearchText"] = None,
        search_in: Optional[
            "aws_sdk_datazone.types.search_in_list.SearchInList"
        ] = None,
        filters: Optional["aws_sdk_datazone.types.filter_clause.FilterClause"] = None,
        sort: Optional["aws_sdk_datazone.types.search_sort.SearchSort"] = None,
        additional_attributes: Optional[
            "aws_sdk_datazone.types.search_output_additional_attributes.SearchOutputAdditionalAttributes"
        ] = None,
    ) -> "aws_sdk_datazone.types.search_output.SearchOutput":
        r"""<p>Searches for assets in Amazon DataZone.</p> <p>Search in Amazon DataZone is a powerful capability that enables users to discover and explore data assets, glossary terms, and data products across their organization. It provides both basic and advanced search functionality, allowing users to find resources based on names, descriptions, metadata, and other attributes. Search can be scoped to specific types of resources (like assets, glossary terms, or data products) and can be filtered using various criteria such as creation date, owner, or status. The search functionality is essential for making the wealth of data resources in an organization discoverable and usable, helping users find the right data for their needs quickly and efficiently.</p> <p>Many search commands in Amazon DataZone are paginated, including <code>search</code> and <code>search-types</code>. When the result set is large, Amazon DataZone returns a <code>nextToken</code> in the response. This token can be used to retrieve the next page of results. </p> <p>Prerequisites:</p> <ul> <li> <p>The --domain-identifier must refer to an existing Amazon DataZone domain. </p> </li> <li> <p>--search-scope must be one of: ASSET, GLOSSARY_TERM, DATA_PRODUCT, or GLOSSARY.</p> </li> <li> <p>The user must have search permissions in the specified domain.</p> </li> <li> <p>If using --filters, ensure that the JSON is well-formed and that each filter includes valid attribute and value keys. </p> </li> <li> <p>For paginated results, be prepared to use --next-token to fetch additional pages.</p> </li> </ul> <p>To run a standard free-text search, the <code>searchText</code> parameter must be supplied. By default, all searchable fields are indexed for semantic search and will return semantic matches for SearchListings queries. To prevent semantic search indexing for a custom form attribute, see the <a href=\"https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateFormType.html\">CreateFormType API documentation</a>. To run a lexical search query, enclose the query with double quotes (\"\"). This will disable semantic search even for fields that have semantic search enabled and will only return results that contain the keywords wrapped by double quotes (order of tokens in the query is not enforced). Free-text search is supported for all attributes annotated with @amazon.datazone#searchable.</p> <p>To run a filtered search, provide filter clause using the <code>filters</code> parameter. To filter on glossary terms, use the special attribute <code>__DataZoneGlossaryTerms</code>. To filter on an indexed numeric attribute (i.e., a numeric attribute annotated with <code>@amazon.datazone#sortable</code>), provide a filter using the <code>intValue</code> parameter. The filters parameter can also be used to run more advanced free-text searches that target specific attributes (attributes must be annotated with <code>@amazon.datazone#searchable</code> for free-text search). Create/update timestamp filtering is supported using the special <code>creationTime</code>/<code>lastUpdatedTime</code> attributes. Filter types can be mixed and matched to power complex queries.</p> <p> To find out whether an attribute has been annotated and indexed for a given search type, use the GetFormType API to retrieve the form containing the attribute.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            owning_project_identifier: <p>The identifier of the owning project specified for the search.</p>
            max_results: <p>The maximum number of results to return in a single call to <code>Search</code>. When the number of results to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>Search</code> to list the next set of results.</p>
            next_token: <p>When the number of results is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of results, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>Search</code> to list the next set of results.</p>
            search_scope: <p>The scope of the search.</p>
            search_text: <p>Specifies the text for which to search.</p>
            search_in: <p>The details of the search.</p>
            filters: <p>Specifies the search filters.</p>
            sort: <p>Specifies the way in which the search results are to be sorted.</p>
            additional_attributes: <p>Specifies additional attributes for the <code>Search</code> action.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.search_input.SearchInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.search_output.SearchOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.search

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.search.async_search(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.search_input.SearchInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        if owning_project_identifier is not None:
            input_["owning_project_identifier"] = owning_project_identifier
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["search_scope"] = search_scope
        if search_text is not None:
            input_["search_text"] = search_text
        if search_in is not None:
            input_["search_in"] = search_in
        if filters is not None:
            input_["filters"] = filters
        if sort is not None:
            input_["sort"] = sort
        if additional_attributes is not None:
            input_["additional_attributes"] = additional_attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_search(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        search_scope: "aws_sdk_datazone.types.inventory_search_scope.InventorySearchScope",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        owning_project_identifier: Optional[
            "aws_sdk_datazone.types.project_id.ProjectId"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        search_text: Optional["aws_sdk_datazone.types.search_text.SearchText"] = None,
        search_in: Optional[
            "aws_sdk_datazone.types.search_in_list.SearchInList"
        ] = None,
        filters: Optional["aws_sdk_datazone.types.filter_clause.FilterClause"] = None,
        sort: Optional["aws_sdk_datazone.types.search_sort.SearchSort"] = None,
        additional_attributes: Optional[
            "aws_sdk_datazone.types.search_output_additional_attributes.SearchOutputAdditionalAttributes"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_datazone.types.search_inventory_result_item.SearchInventoryResultItem]":
        _token = next_token
        while True:
            _response = await self.search(
                domain_identifier,
                search_scope,
                config_overrides=config_overrides,
                owning_project_identifier=owning_project_identifier,
                max_results=max_results,
                next_token=_token,
                search_text=search_text,
                search_in=search_in,
                filters=filters,
                sort=sort,
                additional_attributes=additional_attributes,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def search_group_profiles(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        group_type: "aws_sdk_datazone.types.group_search_type.GroupSearchType",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        search_text: Optional[
            "aws_sdk_datazone.types.group_search_text.GroupSearchText"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> (
        "aws_sdk_datazone.types.search_group_profiles_output.SearchGroupProfilesOutput"
    ):
        """<p>Searches group profiles in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which you want to search group profiles.</p>
            group_type: <p>The group type for which to search.</p>
            search_text: <p>Specifies the text for which to search.</p>
            max_results: <p>The maximum number of results to return in a single call to <code>SearchGroupProfiles</code>. When the number of results to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>SearchGroupProfiles</code> to list the next set of results. </p>
            next_token: <p>When the number of results is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of results, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>SearchGroupProfiles</code> to list the next set of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.search_group_profiles_input.SearchGroupProfilesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.search_group_profiles_output.SearchGroupProfilesOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.search_group_profiles

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.search_group_profiles.async_search_group_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.search_group_profiles_input.SearchGroupProfilesInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["group_type"] = group_type
        if search_text is not None:
            input_["search_text"] = search_text
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_search_group_profiles(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        group_type: "aws_sdk_datazone.types.group_search_type.GroupSearchType",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        search_text: Optional[
            "aws_sdk_datazone.types.group_search_text.GroupSearchText"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_datazone.types.group_profile_summary.GroupProfileSummary]":
        _token = next_token
        while True:
            _response = await self.search_group_profiles(
                domain_identifier,
                group_type,
                config_overrides=config_overrides,
                search_text=search_text,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def search_listings(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        search_text: Optional[str] = None,
        search_in: Optional[
            "aws_sdk_datazone.types.search_in_list.SearchInList"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        filters: Optional["aws_sdk_datazone.types.filter_clause.FilterClause"] = None,
        aggregations: Optional[
            "aws_sdk_datazone.types.aggregation_list.AggregationList"
        ] = None,
        sort: Optional["aws_sdk_datazone.types.search_sort.SearchSort"] = None,
        additional_attributes: Optional[
            "aws_sdk_datazone.types.search_output_additional_attributes.SearchOutputAdditionalAttributes"
        ] = None,
    ) -> "aws_sdk_datazone.types.search_listings_output.SearchListingsOutput":
        r"""<p>Searches listings in Amazon DataZone.</p> <p>SearchListings is a powerful capability that enables users to discover and explore published assets and data products across their organization. It provides both basic and advanced search functionality, allowing users to find resources based on names, descriptions, metadata, and other attributes. SearchListings also supports filtering using various criteria such as creation date, owner, or status. This API is essential for making the wealth of data resources in an organization discoverable and usable, helping users find the right data for their needs quickly and efficiently.</p> <p>SearchListings returns results in a paginated format. When the result set is large, the response will include a nextToken, which can be used to retrieve the next page of results.</p> <p>The SearchListings API gives users flexibility in specifying what kind of search is run.</p> <p>To run a standard free-text search, the <code>searchText</code> parameter must be supplied. By default, all searchable fields are indexed for semantic search and will return semantic matches for SearchListings queries. To prevent semantic search indexing for a custom form attribute, see the <a href=\"https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateFormType.html\">CreateFormType API documentation</a>. To run a lexical search query, enclose the query with double quotes (\"\"). This will disable semantic search even for fields that have semantic search enabled and will only return results that contain the keywords wrapped by double quotes (order of tokens in the query is not enforced). Free-text search is supported for all attributes annotated with @amazon.datazone#searchable.</p> <p>To run a filtered search, provide filter clause using the <code>filters</code> parameter. To filter on glossary terms, use the special attribute <code>__DataZoneGlossaryTerms</code>. To filter on an indexed numeric attribute (i.e., a numeric attribute annotated with <code>@amazon.datazone#sortable</code>), provide a filter using the <code>intValue</code> parameter. The filters parameter can also be used to run more advanced free-text searches that target specific attributes (attributes must be annotated with <code>@amazon.datazone#searchable</code> for free-text search). Create/update timestamp filtering is supported using the special <code>creationTime</code>/<code>lastUpdatedTime</code> attributes. Filter types can be mixed and matched to power complex queries.</p> <p> To find out whether an attribute has been annotated and indexed for a given search type, use the GetFormType API to retrieve the form containing the attribute.</p>

        Args:
            domain_identifier: <p>The identifier of the domain in which to search listings.</p>
            search_text: <p>Specifies the text for which to search.</p>
            search_in: <p>The details of the search.</p>
            max_results: <p>The maximum number of results to return in a single call to <code>SearchListings</code>. When the number of results to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>SearchListings</code> to list the next set of results. </p>
            next_token: <p>When the number of results is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of results, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>SearchListings</code> to list the next set of results.</p>
            filters: <p>Specifies the filters for the search of listings.</p>
            aggregations: <p>Enables you to specify one or more attributes to compute and return counts grouped by field values.</p>
            sort: <p>Specifies the way for sorting the search results.</p>
            additional_attributes: <p>Specifies additional attributes for the search.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.search_listings_input.SearchListingsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.search_listings_output.SearchListingsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.search_listings

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.search_listings.async_search_listings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.search_listings_input.SearchListingsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        if search_text is not None:
            input_["search_text"] = search_text
        if search_in is not None:
            input_["search_in"] = search_in
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters
        if aggregations is not None:
            input_["aggregations"] = aggregations
        if sort is not None:
            input_["sort"] = sort
        if additional_attributes is not None:
            input_["additional_attributes"] = additional_attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_search_listings(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        search_text: Optional[str] = None,
        search_in: Optional[
            "aws_sdk_datazone.types.search_in_list.SearchInList"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        filters: Optional["aws_sdk_datazone.types.filter_clause.FilterClause"] = None,
        aggregations: Optional[
            "aws_sdk_datazone.types.aggregation_list.AggregationList"
        ] = None,
        sort: Optional["aws_sdk_datazone.types.search_sort.SearchSort"] = None,
        additional_attributes: Optional[
            "aws_sdk_datazone.types.search_output_additional_attributes.SearchOutputAdditionalAttributes"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_datazone.types.search_result_item.SearchResultItem]":
        _token = next_token
        while True:
            _response = await self.search_listings(
                domain_identifier,
                config_overrides=config_overrides,
                search_text=search_text,
                search_in=search_in,
                max_results=max_results,
                next_token=_token,
                filters=filters,
                aggregations=aggregations,
                sort=sort,
                additional_attributes=additional_attributes,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def search_types(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        search_scope: "aws_sdk_datazone.types.types_search_scope.TypesSearchScope",
        managed: bool,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        search_text: Optional["aws_sdk_datazone.types.search_text.SearchText"] = None,
        search_in: Optional[
            "aws_sdk_datazone.types.search_in_list.SearchInList"
        ] = None,
        filters: Optional["aws_sdk_datazone.types.filter_clause.FilterClause"] = None,
        sort: Optional["aws_sdk_datazone.types.search_sort.SearchSort"] = None,
    ) -> "aws_sdk_datazone.types.search_types_output.SearchTypesOutput":
        """<p>Searches for types in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>The --domain-identifier must refer to an existing Amazon DataZone domain. </p> </li> <li> <p>--search-scope must be one of the valid values including: ASSET_TYPE, GLOSSARY_TERM_TYPE, DATA_PRODUCT_TYPE.</p> </li> <li> <p>The --managed flag must be present without a value.</p> </li> <li> <p>The user must have permissions for form or asset types in the domain.</p> </li> <li> <p>If using --filters, ensure that the JSON is valid.</p> </li> <li> <p>Filters contain correct structure (attribute, value, operator).</p> </li> </ul>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which to invoke the <code>SearchTypes</code> action.</p>
            max_results: <p>The maximum number of results to return in a single call to <code>SearchTypes</code>. When the number of results to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>SearchTypes</code> to list the next set of results. </p>
            next_token: <p>When the number of results is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of results, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>SearchTypes</code> to list the next set of results.</p>
            search_scope: <p>Specifies the scope of the search for types.</p>
            search_text: <p>Specifies the text for which to search.</p>
            search_in: <p>The details of the search.</p>
            filters: <p>The filters for the <code>SearchTypes</code> action.</p>
            sort: <p>The specifies the way to sort the <code>SearchTypes</code> results.</p>
            managed: <p>Specifies whether the search is managed.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.search_types_input.SearchTypesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.search_types_output.SearchTypesOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.search_types

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.search_types.async_search_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.search_types_input.SearchTypesInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["search_scope"] = search_scope
        if search_text is not None:
            input_["search_text"] = search_text
        if search_in is not None:
            input_["search_in"] = search_in
        if filters is not None:
            input_["filters"] = filters
        if sort is not None:
            input_["sort"] = sort
        input_["managed"] = managed

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_search_types(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        search_scope: "aws_sdk_datazone.types.types_search_scope.TypesSearchScope",
        managed: bool,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        search_text: Optional["aws_sdk_datazone.types.search_text.SearchText"] = None,
        search_in: Optional[
            "aws_sdk_datazone.types.search_in_list.SearchInList"
        ] = None,
        filters: Optional["aws_sdk_datazone.types.filter_clause.FilterClause"] = None,
        sort: Optional["aws_sdk_datazone.types.search_sort.SearchSort"] = None,
    ) -> "AsyncIterator[aws_sdk_datazone.types.search_types_result_item.SearchTypesResultItem]":
        _token = next_token
        while True:
            _response = await self.search_types(
                domain_identifier,
                search_scope,
                managed,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                search_text=search_text,
                search_in=search_in,
                filters=filters,
                sort=sort,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def search_user_profiles(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        user_type: "aws_sdk_datazone.types.user_search_type.UserSearchType",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        search_text: Optional[
            "aws_sdk_datazone.types.user_search_text.UserSearchText"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.search_user_profiles_output.SearchUserProfilesOutput":
        """<p>Searches user profiles in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which you want to search user profiles.</p>
            user_type: <p>Specifies the user type for the <code>SearchUserProfiles</code> action.</p>
            search_text: <p>Specifies the text for which to search.</p>
            max_results: <p>The maximum number of results to return in a single call to <code>SearchUserProfiles</code>. When the number of results to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>SearchUserProfiles</code> to list the next set of results. </p>
            next_token: <p>When the number of results is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of results, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>SearchUserProfiles</code> to list the next set of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.search_user_profiles_input.SearchUserProfilesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.search_user_profiles_output.SearchUserProfilesOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.search_user_profiles

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.search_user_profiles.async_search_user_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.search_user_profiles_input.SearchUserProfilesInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["user_type"] = user_type
        if search_text is not None:
            input_["search_text"] = search_text
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_search_user_profiles(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        user_type: "aws_sdk_datazone.types.user_search_type.UserSearchType",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        search_text: Optional[
            "aws_sdk_datazone.types.user_search_text.UserSearchText"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> (
        "AsyncIterator[aws_sdk_datazone.types.user_profile_summary.UserProfileSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.search_user_profiles(
                domain_identifier,
                user_type,
                config_overrides=config_overrides,
                search_text=search_text,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_notebook_import(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        owning_project_identifier: "aws_sdk_datazone.types.project_id.ProjectId",
        source_location: "aws_sdk_datazone.types.source_location.SourceLocation",
        name: "aws_sdk_datazone.types.notebook_name.NotebookName",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional["aws_sdk_datazone.types.description.Description"] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> (
        "aws_sdk_datazone.types.start_notebook_import_output.StartNotebookImportOutput"
    ):
        """<p>Starts a notebook import in Amazon SageMaker Unified Studio. This operation imports a notebook from an Amazon Simple Storage Service location into a project.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which to import the notebook.</p>
            owning_project_identifier: <p>The identifier of the project that will own the imported notebook.</p>
            source_location: <p>The source location of the notebook to import. This specifies the Amazon Simple Storage Service URI of the notebook file.</p>
            name: <p>The name of the imported notebook. The name must be between 1 and 256 characters.</p>
            description: <p>The description of the imported notebook.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.start_notebook_import_input.StartNotebookImportInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.start_notebook_import_output.StartNotebookImportOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.start_notebook_import

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.start_notebook_import.async_start_notebook_import(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.start_notebook_import_input.StartNotebookImportInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["owning_project_identifier"] = owning_project_identifier
        input_["source_location"] = source_location
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: str,
        tags: "aws_sdk_datazone.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.tag_resource_response.TagResourceResponse":
        """<p>Tags a resource in Amazon DataZone.</p>

        Args:
            resource_arn: <p>The ARN of the resource to be tagged in Amazon DataZone.</p>
            tags: <p>Specifies the tags for the <code>TagResource</code> action.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_datazone._operations.data_zone.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: str,
        tag_keys: "aws_sdk_datazone.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.untag_resource_response.UntagResourceResponse":
        """<p>Untags a resource in Amazon DataZone.</p>

        Args:
            resource_arn: <p>The ARN of the resource to be untagged in Amazon DataZone.</p>
            tag_keys: <p>Specifies the tag keys for the <code>UntagResource</code> action.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_datazone._operations.data_zone.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_account_pool(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.account_pool_id.AccountPoolId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        name: Optional[
            "aws_sdk_datazone.types.account_pool_name.AccountPoolName"
        ] = None,
        description: Optional["aws_sdk_datazone.types.description.Description"] = None,
        resolution_strategy: Optional[
            "aws_sdk_datazone.types.resolution_strategy.ResolutionStrategy"
        ] = None,
        account_source: Optional[
            "aws_sdk_datazone.types.account_source.AccountSource"
        ] = None,
    ) -> "aws_sdk_datazone.types.update_account_pool_output.UpdateAccountPoolOutput":
        """<p>Updates the account pool.</p>

        Args:
            domain_identifier: <p>The domain ID where the account pool that is to be updated lives.</p>
            identifier: <p>The ID of the account pool that is to be updated.</p>
            name: <p>The name of the account pool that is to be updated.</p>
            description: <p>The description of the account pool that is to be udpated.</p>
            resolution_strategy: <p>The mechanism used to resolve the account selection from the account pool.</p>
            account_source: <p>The source of accounts for the account pool. In the current release, it's either a static list of accounts provided by the customer or a custom Amazon Web Services Lambda handler. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.update_account_pool_input.UpdateAccountPoolInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.update_account_pool_output.UpdateAccountPoolOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.update_account_pool

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.update_account_pool.async_update_account_pool(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.update_account_pool_input.UpdateAccountPoolInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if resolution_strategy is not None:
            input_["resolution_strategy"] = resolution_strategy
        if account_source is not None:
            input_["account_source"] = account_source

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_asset_filter(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        asset_identifier: "aws_sdk_datazone.types.asset_id.AssetId",
        identifier: "aws_sdk_datazone.types.filter_id.FilterId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        name: Optional[str] = None,
        description: Optional["aws_sdk_datazone.types.description.Description"] = None,
        configuration: Optional[
            "aws_sdk_datazone.types.asset_filter_configuration.AssetFilterConfiguration"
        ] = None,
    ) -> "aws_sdk_datazone.types.update_asset_filter_output.UpdateAssetFilterOutput":
        """<p>Updates an asset filter.</p> <p>Prerequisites:</p> <ul> <li> <p>The domain, asset, and asset filter identifier must all exist. </p> </li> <li> <p>The asset must contain the columns being referenced in the update.</p> </li> <li> <p>If applying a row filter, ensure the column referenced in the expression exists in the asset schema.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the domain where you want to update an asset filter.</p>
            asset_identifier: <p>The ID of the data asset.</p>
            identifier: <p>The ID of the asset filter.</p>
            name: <p>The name of the asset filter.</p>
            description: <p>The description of the asset filter.</p>
            configuration: <p>The configuration of the asset filter.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.update_asset_filter_input.UpdateAssetFilterInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.update_asset_filter_output.UpdateAssetFilterOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.update_asset_filter

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.update_asset_filter.async_update_asset_filter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.update_asset_filter_input.UpdateAssetFilterInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["asset_identifier"] = asset_identifier
        input_["identifier"] = identifier
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if configuration is not None:
            input_["configuration"] = configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_connection(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        configurations: Optional[
            "aws_sdk_datazone.types.configurations.Configurations"
        ] = None,
        description: Optional["aws_sdk_datazone.types.description.Description"] = None,
        aws_location: Optional[
            "aws_sdk_datazone.types.aws_location.AwsLocation"
        ] = None,
        props: Optional[
            "aws_sdk_datazone.types.connection_properties_patch.ConnectionPropertiesPatch"
        ] = None,
    ) -> "aws_sdk_datazone.types.update_connection_output.UpdateConnectionOutput":
        """<p>Updates a connection. In Amazon DataZone, a connection enables you to connect your resources (domains, projects, and environments) to external resources and services.</p>

        Args:
            configurations: <p>The configurations of the connection.</p>
            domain_identifier: <p>The ID of the domain where a connection is to be updated.</p>
            identifier: <p>The ID of the connection to be updated.</p>
            description: <p>The description of a connection.</p>
            aws_location: <p>The location where a connection is to be updated.</p>
            props: <p>The connection props.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.update_connection_input.UpdateConnectionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.update_connection_output.UpdateConnectionOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.update_connection

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.update_connection.async_update_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.update_connection_input.UpdateConnectionInput = {}  # type: ignore[typeddict-item]
        if configurations is not None:
            input_["configurations"] = configurations
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        if description is not None:
            input_["description"] = description
        if aws_location is not None:
            input_["aws_location"] = aws_location
        if props is not None:
            input_["props"] = props

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_environment(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        glossary_terms: Optional[
            "aws_sdk_datazone.types.glossary_terms.GlossaryTerms"
        ] = None,
        blueprint_version: Optional[str] = None,
        user_parameters: Optional[
            "aws_sdk_datazone.types.environment_parameters_list.EnvironmentParametersList"
        ] = None,
        environment_configuration_name: Optional[
            "aws_sdk_datazone.types.environment_configuration_name.EnvironmentConfigurationName"
        ] = None,
    ) -> "aws_sdk_datazone.types.update_environment_output.UpdateEnvironmentOutput":
        """<p>Updates the specified environment in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the domain in which the environment is to be updated.</p>
            identifier: <p>The identifier of the environment that is to be updated.</p>
            name: <p>The name to be updated as part of the <code>UpdateEnvironment</code> action.</p>
            description: <p>The description to be updated as part of the <code>UpdateEnvironment</code> action.</p>
            glossary_terms: <p>The glossary terms to be updated as part of the <code>UpdateEnvironment</code> action.</p>
            blueprint_version: <p>The blueprint version to which the environment should be updated. You can only specify the following string for this parameter: <code>latest</code>.</p>
            user_parameters: <p>The user parameters of the environment.</p>
            environment_configuration_name: <p>The configuration name of the environment.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.update_environment_input.UpdateEnvironmentInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.update_environment_output.UpdateEnvironmentOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.update_environment

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.update_environment.async_update_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.update_environment_input.UpdateEnvironmentInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if glossary_terms is not None:
            input_["glossary_terms"] = glossary_terms
        if blueprint_version is not None:
            input_["blueprint_version"] = blueprint_version
        if user_parameters is not None:
            input_["user_parameters"] = user_parameters
        if environment_configuration_name is not None:
            input_["environment_configuration_name"] = environment_configuration_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_environment_action(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        environment_identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId",
        identifier: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        parameters: Optional[
            "aws_sdk_datazone.types.action_parameters.ActionParameters"
        ] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> "aws_sdk_datazone.types.update_environment_action_output.UpdateEnvironmentActionOutput":
        """<p>Updates an environment action.</p>

        Args:
            domain_identifier: <p>The domain ID of the environment action.</p>
            environment_identifier: <p>The environment ID of the environment action.</p>
            identifier: <p>The ID of the environment action.</p>
            parameters: <p>The parameters of the environment action.</p>
            name: <p>The name of the environment action.</p>
            description: <p>The description of the environment action.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.update_environment_action_input.UpdateEnvironmentActionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.update_environment_action_output.UpdateEnvironmentActionOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.update_environment_action

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.update_environment_action.async_update_environment_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.update_environment_action_input.UpdateEnvironmentActionInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["environment_identifier"] = environment_identifier
        input_["identifier"] = identifier
        if parameters is not None:
            input_["parameters"] = parameters
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_environment_blueprint(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.environment_blueprint_id.EnvironmentBlueprintId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional[str] = None,
        provisioning_properties: Optional[
            "aws_sdk_datazone.types.provisioning_properties.ProvisioningProperties"
        ] = None,
        user_parameters: Optional[
            "aws_sdk_datazone.types.custom_parameter_list.CustomParameterList"
        ] = None,
    ) -> "aws_sdk_datazone.types.update_environment_blueprint_output.UpdateEnvironmentBlueprintOutput":
        """<p>Updates an environment blueprint in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which an environment blueprint is to be updated.</p>
            identifier: <p>The identifier of the environment blueprint to be updated.</p>
            description: <p>The description to be updated as part of the <code>UpdateEnvironmentBlueprint</code> action.</p>
            provisioning_properties: <p>The provisioning properties to be updated as part of the <code>UpdateEnvironmentBlueprint</code> action.</p>
            user_parameters: <p>The user parameters to be updated as part of the <code>UpdateEnvironmentBlueprint</code> action.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.update_environment_blueprint_input.UpdateEnvironmentBlueprintInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.update_environment_blueprint_output.UpdateEnvironmentBlueprintOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.update_environment_blueprint

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.update_environment_blueprint.async_update_environment_blueprint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.update_environment_blueprint_input.UpdateEnvironmentBlueprintInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        if description is not None:
            input_["description"] = description
        if provisioning_properties is not None:
            input_["provisioning_properties"] = provisioning_properties
        if user_parameters is not None:
            input_["user_parameters"] = user_parameters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_environment_profile(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.environment_profile_id.EnvironmentProfileId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        name: Optional[
            "aws_sdk_datazone.types.environment_profile_name.EnvironmentProfileName"
        ] = None,
        description: Optional[str] = None,
        user_parameters: Optional[
            "aws_sdk_datazone.types.environment_parameters_list.EnvironmentParametersList"
        ] = None,
        aws_account_id: Optional[
            "aws_sdk_datazone.types.aws_account_id.AwsAccountId"
        ] = None,
        aws_account_region: Optional[
            "aws_sdk_datazone.types.aws_region.AwsRegion"
        ] = None,
    ) -> "aws_sdk_datazone.types.update_environment_profile_output.UpdateEnvironmentProfileOutput":
        """<p>Updates the specified environment profile in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which an environment profile is to be updated.</p>
            identifier: <p>The identifier of the environment profile that is to be updated.</p>
            name: <p>The name to be updated as part of the <code>UpdateEnvironmentProfile</code> action.</p>
            description: <p>The description to be updated as part of the <code>UpdateEnvironmentProfile</code> action.</p>
            user_parameters: <p>The user parameters to be updated as part of the <code>UpdateEnvironmentProfile</code> action.</p>
            aws_account_id: <p>The Amazon Web Services account in which a specified environment profile is to be udpated.</p>
            aws_account_region: <p>The Amazon Web Services Region in which a specified environment profile is to be updated.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.update_environment_profile_input.UpdateEnvironmentProfileInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.update_environment_profile_output.UpdateEnvironmentProfileOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.update_environment_profile

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.update_environment_profile.async_update_environment_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.update_environment_profile_input.UpdateEnvironmentProfileInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if user_parameters is not None:
            input_["user_parameters"] = user_parameters
        if aws_account_id is not None:
            input_["aws_account_id"] = aws_account_id
        if aws_account_region is not None:
            input_["aws_account_region"] = aws_account_region

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_group_profile(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        group_identifier: "aws_sdk_datazone.types.group_identifier.GroupIdentifier",
        status: "aws_sdk_datazone.types.group_profile_status.GroupProfileStatus",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.update_group_profile_output.UpdateGroupProfileOutput":
        """<p>Updates the specified group profile in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which a group profile is updated.</p>
            group_identifier: <p>The identifier of the group profile that is updated.</p>
            status: <p>The status of the group profile that is updated.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.update_group_profile_input.UpdateGroupProfileInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.update_group_profile_output.UpdateGroupProfileOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.update_group_profile

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.update_group_profile.async_update_group_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.update_group_profile_input.UpdateGroupProfileInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["group_identifier"] = group_identifier
        input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_project(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        name: Optional["aws_sdk_datazone.types.project_name.ProjectName"] = None,
        description: Optional["aws_sdk_datazone.types.description.Description"] = None,
        resource_tags: Optional["aws_sdk_datazone.types.tags.Tags"] = None,
        glossary_terms: Optional[
            "aws_sdk_datazone.types.glossary_terms.GlossaryTerms"
        ] = None,
        domain_unit_id: Optional[
            "aws_sdk_datazone.types.domain_unit_id.DomainUnitId"
        ] = None,
        environment_deployment_details: Optional[
            "aws_sdk_datazone.types.environment_deployment_details.EnvironmentDeploymentDetails"
        ] = None,
        user_parameters: Optional[
            "aws_sdk_datazone.types.environment_configuration_user_parameters_list.EnvironmentConfigurationUserParametersList"
        ] = None,
        project_profile_version: Optional[str] = None,
    ) -> "aws_sdk_datazone.types.update_project_output.UpdateProjectOutput":
        """<p>Updates the specified project in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain where a project is being updated.</p>
            identifier: <p>The identifier of the project that is to be updated.</p>
            name: <p>The name to be updated as part of the <code>UpdateProject</code> action.</p>
            description: <p>The description to be updated as part of the <code>UpdateProject</code> action.</p>
            resource_tags: <p>The resource tags of the project.</p>
            glossary_terms: <p>The glossary terms to be updated as part of the <code>UpdateProject</code> action.</p>
            domain_unit_id: <p>The ID of the domain unit.</p>
            environment_deployment_details: <p>The environment deployment details of the project.</p>
            user_parameters: <p>The user parameters of the project.</p>
            project_profile_version: <p>The project profile version to which the project should be updated. You can only specify the following string for this parameter: <code>latest</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.update_project_input.UpdateProjectInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.update_project_output.UpdateProjectOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.update_project

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.update_project.async_update_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.update_project_input.UpdateProjectInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags
        if glossary_terms is not None:
            input_["glossary_terms"] = glossary_terms
        if domain_unit_id is not None:
            input_["domain_unit_id"] = domain_unit_id
        if environment_deployment_details is not None:
            input_["environment_deployment_details"] = environment_deployment_details
        if user_parameters is not None:
            input_["user_parameters"] = user_parameters
        if project_profile_version is not None:
            input_["project_profile_version"] = project_profile_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_project_profile(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.project_profile_id.ProjectProfileId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        name: Optional[
            "aws_sdk_datazone.types.project_profile_name.ProjectProfileName"
        ] = None,
        description: Optional["aws_sdk_datazone.types.description.Description"] = None,
        status: Optional["aws_sdk_datazone.types.status.Status"] = None,
        project_resource_tags: Optional[
            "aws_sdk_datazone.types.project_resource_tag_parameters.ProjectResourceTagParameters"
        ] = None,
        allow_custom_project_resource_tags: Optional[bool] = None,
        project_resource_tags_description: Optional[
            "aws_sdk_datazone.types.description.Description"
        ] = None,
        environment_configurations: Optional[
            "aws_sdk_datazone.types.environment_configurations_list.EnvironmentConfigurationsList"
        ] = None,
        domain_unit_identifier: Optional[
            "aws_sdk_datazone.types.domain_unit_id.DomainUnitId"
        ] = None,
    ) -> "aws_sdk_datazone.types.update_project_profile_output.UpdateProjectProfileOutput":
        """<p>Updates a project profile.</p>

        Args:
            domain_identifier: <p>The ID of the domain where a project profile is to be updated.</p>
            identifier: <p>The ID of a project profile that is to be updated.</p>
            name: <p>The name of a project profile.</p>
            description: <p>The description of a project profile.</p>
            status: <p>The status of a project profile.</p>
            project_resource_tags: <p>The resource tags of the project profile.</p>
            allow_custom_project_resource_tags: <p>Specifies whether custom project resource tags are supported.</p>
            project_resource_tags_description: <p>Field viewable through the UI that provides a project user with the allowed resource tag specifications.</p>
            environment_configurations: <p>The environment configurations of a project profile.</p>
            domain_unit_identifier: <p>The ID of the domain unit where a project profile is to be updated.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.update_project_profile_input.UpdateProjectProfileInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.update_project_profile_output.UpdateProjectProfileOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.update_project_profile

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.update_project_profile.async_update_project_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.update_project_profile_input.UpdateProjectProfileInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status
        if project_resource_tags is not None:
            input_["project_resource_tags"] = project_resource_tags
        if allow_custom_project_resource_tags is not None:
            input_["allow_custom_project_resource_tags"] = (
                allow_custom_project_resource_tags
            )
        if project_resource_tags_description is not None:
            input_["project_resource_tags_description"] = (
                project_resource_tags_description
            )
        if environment_configurations is not None:
            input_["environment_configurations"] = environment_configurations
        if domain_unit_identifier is not None:
            input_["domain_unit_identifier"] = domain_unit_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_root_domain_unit_owner(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        current_owner: "aws_sdk_datazone.types.user_identifier.UserIdentifier",
        new_owner: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.update_root_domain_unit_owner_output.UpdateRootDomainUnitOwnerOutput":
        """<p>Updates the owner of the root domain unit.</p>

        Args:
            domain_identifier: <p>The ID of the domain where the root domain unit owner is to be updated.</p>
            current_owner: <p>The current owner of the root domain unit.</p>
            new_owner: <p>The new owner of the root domain unit.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.update_root_domain_unit_owner_input.UpdateRootDomainUnitOwnerInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.update_root_domain_unit_owner_output.UpdateRootDomainUnitOwnerOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.update_root_domain_unit_owner

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.update_root_domain_unit_owner.async_update_root_domain_unit_owner(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.update_root_domain_unit_owner_input.UpdateRootDomainUnitOwnerInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["current_owner"] = current_owner
        input_["new_owner"] = new_owner
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_subscription_grant_status(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.subscription_grant_id.SubscriptionGrantId",
        asset_identifier: "aws_sdk_datazone.types.asset_id.AssetId",
        status: "aws_sdk_datazone.types.subscription_grant_status.SubscriptionGrantStatus",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        failure_cause: Optional[
            "aws_sdk_datazone.types.failure_cause.FailureCause"
        ] = None,
        target_name: Optional[str] = None,
    ) -> "aws_sdk_datazone.types.update_subscription_grant_status_output.UpdateSubscriptionGrantStatusOutput":
        """<p>Updates the status of the specified subscription grant status in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which a subscription grant status is to be updated.</p>
            identifier: <p>The identifier of the subscription grant the status of which is to be updated.</p>
            asset_identifier: <p>The identifier of the asset the subscription grant status of which is to be updated.</p>
            status: <p>The status to be updated as part of the <code>UpdateSubscriptionGrantStatus</code> action.</p>
            failure_cause: <p>Specifies the error message that is returned if the operation cannot be successfully completed.</p>
            target_name: <p>The target name to be updated as part of the <code>UpdateSubscriptionGrantStatus</code> action.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.update_subscription_grant_status_input.UpdateSubscriptionGrantStatusInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.update_subscription_grant_status_output.UpdateSubscriptionGrantStatusOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.update_subscription_grant_status

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.update_subscription_grant_status.async_update_subscription_grant_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.update_subscription_grant_status_input.UpdateSubscriptionGrantStatusInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        input_["asset_identifier"] = asset_identifier
        input_["status"] = status
        if failure_cause is not None:
            input_["failure_cause"] = failure_cause
        if target_name is not None:
            input_["target_name"] = target_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_subscription_request(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.subscription_request_id.SubscriptionRequestId",
        request_reason: "aws_sdk_datazone.types.request_reason.RequestReason",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.update_subscription_request_output.UpdateSubscriptionRequestOutput":
        """<p>Updates a specified subscription request in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which a subscription request is to be updated.</p>
            identifier: <p>The identifier of the subscription request that is to be updated.</p>
            request_reason: <p>The reason for the <code>UpdateSubscriptionRequest</code> action.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.update_subscription_request_input.UpdateSubscriptionRequestInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.update_subscription_request_output.UpdateSubscriptionRequestOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.update_subscription_request

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.update_subscription_request.async_update_subscription_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.update_subscription_request_input.UpdateSubscriptionRequestInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        input_["request_reason"] = request_reason

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_subscription_target(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        environment_identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId",
        identifier: "aws_sdk_datazone.types.subscription_target_id.SubscriptionTargetId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        name: Optional[
            "aws_sdk_datazone.types.subscription_target_name.SubscriptionTargetName"
        ] = None,
        authorized_principals: Optional[
            "aws_sdk_datazone.types.authorized_principal_identifiers.AuthorizedPrincipalIdentifiers"
        ] = None,
        applicable_asset_types: Optional[
            "aws_sdk_datazone.types.applicable_asset_types.ApplicableAssetTypes"
        ] = None,
        subscription_target_config: Optional[
            "aws_sdk_datazone.types.subscription_target_forms.SubscriptionTargetForms"
        ] = None,
        manage_access_role: Optional[
            "aws_sdk_datazone.types.iam_role_arn.IamRoleArn"
        ] = None,
        provider: Optional[str] = None,
        subscription_grant_creation_mode: Optional[
            "aws_sdk_datazone.types.subscription_grant_creation_mode.SubscriptionGrantCreationMode"
        ] = None,
    ) -> "aws_sdk_datazone.types.update_subscription_target_output.UpdateSubscriptionTargetOutput":
        """<p>Updates the specified subscription target in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which a subscription target is to be updated.</p>
            environment_identifier: <p>The identifier of the environment in which a subscription target is to be updated.</p>
            identifier: <p>Identifier of the subscription target that is to be updated.</p>
            name: <p>The name to be updated as part of the <code>UpdateSubscriptionTarget</code> action.</p>
            authorized_principals: <p>The authorized principals to be updated as part of the <code>UpdateSubscriptionTarget</code> action.</p>
            applicable_asset_types: <p>The applicable asset types to be updated as part of the <code>UpdateSubscriptionTarget</code> action.</p>
            subscription_target_config: <p>The configuration to be updated as part of the <code>UpdateSubscriptionTarget</code> action.</p>
            manage_access_role: <p>The manage access role to be updated as part of the <code>UpdateSubscriptionTarget</code> action.</p>
            provider: <p>The provider to be updated as part of the <code>UpdateSubscriptionTarget</code> action.</p>
            subscription_grant_creation_mode: <p> Determines the subscription grant creation mode for this target, defining if grants are auto-created upon subscription approval or managed manually. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.update_subscription_target_input.UpdateSubscriptionTargetInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.update_subscription_target_output.UpdateSubscriptionTargetOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.update_subscription_target

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.update_subscription_target.async_update_subscription_target(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.update_subscription_target_input.UpdateSubscriptionTargetInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["environment_identifier"] = environment_identifier
        input_["identifier"] = identifier
        if name is not None:
            input_["name"] = name
        if authorized_principals is not None:
            input_["authorized_principals"] = authorized_principals
        if applicable_asset_types is not None:
            input_["applicable_asset_types"] = applicable_asset_types
        if subscription_target_config is not None:
            input_["subscription_target_config"] = subscription_target_config
        if manage_access_role is not None:
            input_["manage_access_role"] = manage_access_role
        if provider is not None:
            input_["provider"] = provider
        if subscription_grant_creation_mode is not None:
            input_["subscription_grant_creation_mode"] = (
                subscription_grant_creation_mode
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_user_profile(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        user_identifier: "aws_sdk_datazone.types.user_identifier.UserIdentifier",
        status: "aws_sdk_datazone.types.user_profile_status.UserProfileStatus",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        type: Optional[
            "aws_sdk_datazone.types.user_profile_type.UserProfileType"
        ] = None,
        session_name: Optional[str] = None,
    ) -> "aws_sdk_datazone.types.update_user_profile_output.UpdateUserProfileOutput":
        """<p>Updates the specified user profile in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which a user profile is updated.</p>
            user_identifier: <p>The identifier of the user whose user profile is to be updated.</p>
            type: <p>The type of the user profile that are to be updated.</p>
            status: <p>The status of the user profile that are to be updated.</p>
            session_name: <p>The session name for IAM role sessions.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.update_user_profile_input.UpdateUserProfileInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.update_user_profile_output.UpdateUserProfileOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.update_user_profile

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.update_user_profile.async_update_user_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.update_user_profile_input.UpdateUserProfileInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["user_identifier"] = user_identifier
        if type is not None:
            input_["type"] = type
        input_["status"] = status
        if session_name is not None:
            input_["session_name"] = session_name

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
