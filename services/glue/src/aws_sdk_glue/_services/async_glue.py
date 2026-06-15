"""Generated from Smithy shape ``com.amazonaws.glue#AWSGlue``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_glue._auth._signers
import aws_sdk_glue._auth._sigv4
from aws_sdk_glue._auth._identity import Credentials
from aws_sdk_glue._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_glue._auth._zapros_handler import AuthMiddleware
from aws_sdk_glue._pagination import resolve_path as _resolve_path
from aws_sdk_glue._services._aws_config import aaws_config
from aws_sdk_glue._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_glue.types.action_list
    import aws_sdk_glue.types.additional_plan_options_map
    import aws_sdk_glue.types.api_version
    import aws_sdk_glue.types.arn_string
    import aws_sdk_glue.types.audit_context
    import aws_sdk_glue.types.auth_token_string
    import aws_sdk_glue.types.batch_create_partition_request
    import aws_sdk_glue.types.batch_create_partition_response
    import aws_sdk_glue.types.batch_delete_connection_request
    import aws_sdk_glue.types.batch_delete_connection_response
    import aws_sdk_glue.types.batch_delete_partition_request
    import aws_sdk_glue.types.batch_delete_partition_response
    import aws_sdk_glue.types.batch_delete_partition_value_list
    import aws_sdk_glue.types.batch_delete_table_name_list
    import aws_sdk_glue.types.batch_delete_table_request
    import aws_sdk_glue.types.batch_delete_table_response
    import aws_sdk_glue.types.batch_delete_table_version_list
    import aws_sdk_glue.types.batch_delete_table_version_request
    import aws_sdk_glue.types.batch_delete_table_version_response
    import aws_sdk_glue.types.batch_get_blueprint_names
    import aws_sdk_glue.types.batch_get_blueprints_request
    import aws_sdk_glue.types.batch_get_blueprints_response
    import aws_sdk_glue.types.batch_get_crawlers_request
    import aws_sdk_glue.types.batch_get_crawlers_response
    import aws_sdk_glue.types.batch_get_custom_entity_types_request
    import aws_sdk_glue.types.batch_get_custom_entity_types_response
    import aws_sdk_glue.types.batch_get_data_quality_result_request
    import aws_sdk_glue.types.batch_get_data_quality_result_response
    import aws_sdk_glue.types.batch_get_dev_endpoints_request
    import aws_sdk_glue.types.batch_get_dev_endpoints_response
    import aws_sdk_glue.types.batch_get_jobs_request
    import aws_sdk_glue.types.batch_get_jobs_response
    import aws_sdk_glue.types.batch_get_partition_request
    import aws_sdk_glue.types.batch_get_partition_response
    import aws_sdk_glue.types.batch_get_partition_value_list
    import aws_sdk_glue.types.batch_get_table_optimizer_entries
    import aws_sdk_glue.types.batch_get_table_optimizer_request
    import aws_sdk_glue.types.batch_get_table_optimizer_response
    import aws_sdk_glue.types.batch_get_triggers_request
    import aws_sdk_glue.types.batch_get_triggers_response
    import aws_sdk_glue.types.batch_get_workflows_request
    import aws_sdk_glue.types.batch_get_workflows_response
    import aws_sdk_glue.types.batch_put_data_quality_statistic_annotation_request
    import aws_sdk_glue.types.batch_put_data_quality_statistic_annotation_response
    import aws_sdk_glue.types.batch_stop_job_run_job_run_id_list
    import aws_sdk_glue.types.batch_stop_job_run_request
    import aws_sdk_glue.types.batch_stop_job_run_response
    import aws_sdk_glue.types.batch_update_partition_request
    import aws_sdk_glue.types.batch_update_partition_request_entry_list
    import aws_sdk_glue.types.batch_update_partition_response
    import aws_sdk_glue.types.blueprint_parameters
    import aws_sdk_glue.types.boolean
    import aws_sdk_glue.types.boolean_nullable
    import aws_sdk_glue.types.boolean_value
    import aws_sdk_glue.types.bounded_partition_value_list
    import aws_sdk_glue.types.cancel_data_quality_rule_recommendation_run_request
    import aws_sdk_glue.types.cancel_data_quality_rule_recommendation_run_response
    import aws_sdk_glue.types.cancel_data_quality_ruleset_evaluation_run_request
    import aws_sdk_glue.types.cancel_data_quality_ruleset_evaluation_run_response
    import aws_sdk_glue.types.cancel_ml_task_run_request
    import aws_sdk_glue.types.cancel_ml_task_run_response
    import aws_sdk_glue.types.cancel_statement_request
    import aws_sdk_glue.types.cancel_statement_response
    import aws_sdk_glue.types.catalog_entries
    import aws_sdk_glue.types.catalog_entry
    import aws_sdk_glue.types.catalog_getter_page_size
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.catalog_input
    import aws_sdk_glue.types.catalog_name_string
    import aws_sdk_glue.types.check_schema_version_validity_input
    import aws_sdk_glue.types.check_schema_version_validity_response
    import aws_sdk_glue.types.classifier_name_list
    import aws_sdk_glue.types.code_gen_configuration_nodes
    import aws_sdk_glue.types.column_name_list
    import aws_sdk_glue.types.commit_id_string
    import aws_sdk_glue.types.compatibility
    import aws_sdk_glue.types.compute_environment
    import aws_sdk_glue.types.connection_input
    import aws_sdk_glue.types.connection_options
    import aws_sdk_glue.types.connection_properties_configuration
    import aws_sdk_glue.types.connection_type_brief
    import aws_sdk_glue.types.connections_list
    import aws_sdk_glue.types.connector_authentication_configuration
    import aws_sdk_glue.types.context_words
    import aws_sdk_glue.types.crawler_configuration
    import aws_sdk_glue.types.crawler_name_list
    import aws_sdk_glue.types.crawler_security_configuration
    import aws_sdk_glue.types.crawler_targets
    import aws_sdk_glue.types.crawls_filter_list
    import aws_sdk_glue.types.create_blueprint_request
    import aws_sdk_glue.types.create_blueprint_response
    import aws_sdk_glue.types.create_catalog_request
    import aws_sdk_glue.types.create_catalog_response
    import aws_sdk_glue.types.create_classifier_request
    import aws_sdk_glue.types.create_classifier_response
    import aws_sdk_glue.types.create_column_statistics_task_settings_request
    import aws_sdk_glue.types.create_column_statistics_task_settings_response
    import aws_sdk_glue.types.create_connection_request
    import aws_sdk_glue.types.create_connection_response
    import aws_sdk_glue.types.create_crawler_request
    import aws_sdk_glue.types.create_crawler_response
    import aws_sdk_glue.types.create_csv_classifier_request
    import aws_sdk_glue.types.create_custom_entity_type_request
    import aws_sdk_glue.types.create_custom_entity_type_response
    import aws_sdk_glue.types.create_data_quality_ruleset_request
    import aws_sdk_glue.types.create_data_quality_ruleset_response
    import aws_sdk_glue.types.create_database_request
    import aws_sdk_glue.types.create_database_response
    import aws_sdk_glue.types.create_dev_endpoint_request
    import aws_sdk_glue.types.create_dev_endpoint_response
    import aws_sdk_glue.types.create_glue_identity_center_configuration_request
    import aws_sdk_glue.types.create_glue_identity_center_configuration_response
    import aws_sdk_glue.types.create_grok_classifier_request
    import aws_sdk_glue.types.create_integration_request
    import aws_sdk_glue.types.create_integration_resource_property_request
    import aws_sdk_glue.types.create_integration_resource_property_response
    import aws_sdk_glue.types.create_integration_response
    import aws_sdk_glue.types.create_integration_table_properties_request
    import aws_sdk_glue.types.create_integration_table_properties_response
    import aws_sdk_glue.types.create_job_request
    import aws_sdk_glue.types.create_job_response
    import aws_sdk_glue.types.create_json_classifier_request
    import aws_sdk_glue.types.create_ml_transform_request
    import aws_sdk_glue.types.create_ml_transform_response
    import aws_sdk_glue.types.create_partition_index_request
    import aws_sdk_glue.types.create_partition_index_response
    import aws_sdk_glue.types.create_partition_request
    import aws_sdk_glue.types.create_partition_response
    import aws_sdk_glue.types.create_registry_input
    import aws_sdk_glue.types.create_registry_response
    import aws_sdk_glue.types.create_schema_input
    import aws_sdk_glue.types.create_schema_response
    import aws_sdk_glue.types.create_script_request
    import aws_sdk_glue.types.create_script_response
    import aws_sdk_glue.types.create_security_configuration_request
    import aws_sdk_glue.types.create_security_configuration_response
    import aws_sdk_glue.types.create_session_request
    import aws_sdk_glue.types.create_session_response
    import aws_sdk_glue.types.create_table_optimizer_request
    import aws_sdk_glue.types.create_table_optimizer_response
    import aws_sdk_glue.types.create_table_request
    import aws_sdk_glue.types.create_table_response
    import aws_sdk_glue.types.create_trigger_request
    import aws_sdk_glue.types.create_trigger_response
    import aws_sdk_glue.types.create_usage_profile_request
    import aws_sdk_glue.types.create_usage_profile_response
    import aws_sdk_glue.types.create_user_defined_function_request
    import aws_sdk_glue.types.create_user_defined_function_response
    import aws_sdk_glue.types.create_workflow_request
    import aws_sdk_glue.types.create_workflow_response
    import aws_sdk_glue.types.create_xml_classifier_request
    import aws_sdk_glue.types.cron_expression
    import aws_sdk_glue.types.custom_entity_type_names
    import aws_sdk_glue.types.dag_edges
    import aws_sdk_glue.types.dag_nodes
    import aws_sdk_glue.types.data_catalog_encryption_settings
    import aws_sdk_glue.types.data_format
    import aws_sdk_glue.types.data_quality_evaluation_run_additional_run_options
    import aws_sdk_glue.types.data_quality_result_filter_criteria
    import aws_sdk_glue.types.data_quality_result_ids
    import aws_sdk_glue.types.data_quality_rule_recommendation_run_filter
    import aws_sdk_glue.types.data_quality_ruleset_evaluation_run_filter
    import aws_sdk_glue.types.data_quality_ruleset_filter_criteria
    import aws_sdk_glue.types.data_quality_ruleset_string
    import aws_sdk_glue.types.data_quality_target_table
    import aws_sdk_glue.types.data_source
    import aws_sdk_glue.types.data_source_map
    import aws_sdk_glue.types.database_attributes_list
    import aws_sdk_glue.types.database_input
    import aws_sdk_glue.types.database_name
    import aws_sdk_glue.types.delete_blueprint_request
    import aws_sdk_glue.types.delete_blueprint_response
    import aws_sdk_glue.types.delete_catalog_request
    import aws_sdk_glue.types.delete_catalog_response
    import aws_sdk_glue.types.delete_classifier_request
    import aws_sdk_glue.types.delete_classifier_response
    import aws_sdk_glue.types.delete_column_statistics_for_partition_request
    import aws_sdk_glue.types.delete_column_statistics_for_partition_response
    import aws_sdk_glue.types.delete_column_statistics_for_table_request
    import aws_sdk_glue.types.delete_column_statistics_for_table_response
    import aws_sdk_glue.types.delete_column_statistics_task_settings_request
    import aws_sdk_glue.types.delete_column_statistics_task_settings_response
    import aws_sdk_glue.types.delete_connection_name_list
    import aws_sdk_glue.types.delete_connection_request
    import aws_sdk_glue.types.delete_connection_response
    import aws_sdk_glue.types.delete_connection_type_request
    import aws_sdk_glue.types.delete_connection_type_response
    import aws_sdk_glue.types.delete_crawler_request
    import aws_sdk_glue.types.delete_crawler_response
    import aws_sdk_glue.types.delete_custom_entity_type_request
    import aws_sdk_glue.types.delete_custom_entity_type_response
    import aws_sdk_glue.types.delete_data_quality_ruleset_request
    import aws_sdk_glue.types.delete_data_quality_ruleset_response
    import aws_sdk_glue.types.delete_database_request
    import aws_sdk_glue.types.delete_database_response
    import aws_sdk_glue.types.delete_dev_endpoint_request
    import aws_sdk_glue.types.delete_dev_endpoint_response
    import aws_sdk_glue.types.delete_glue_identity_center_configuration_request
    import aws_sdk_glue.types.delete_glue_identity_center_configuration_response
    import aws_sdk_glue.types.delete_integration_request
    import aws_sdk_glue.types.delete_integration_resource_property_request
    import aws_sdk_glue.types.delete_integration_resource_property_response
    import aws_sdk_glue.types.delete_integration_response
    import aws_sdk_glue.types.delete_integration_table_properties_request
    import aws_sdk_glue.types.delete_integration_table_properties_response
    import aws_sdk_glue.types.delete_job_request
    import aws_sdk_glue.types.delete_job_response
    import aws_sdk_glue.types.delete_ml_transform_request
    import aws_sdk_glue.types.delete_ml_transform_response
    import aws_sdk_glue.types.delete_partition_index_request
    import aws_sdk_glue.types.delete_partition_index_response
    import aws_sdk_glue.types.delete_partition_request
    import aws_sdk_glue.types.delete_partition_response
    import aws_sdk_glue.types.delete_registry_input
    import aws_sdk_glue.types.delete_registry_response
    import aws_sdk_glue.types.delete_resource_policy_request
    import aws_sdk_glue.types.delete_resource_policy_response
    import aws_sdk_glue.types.delete_schema_input
    import aws_sdk_glue.types.delete_schema_response
    import aws_sdk_glue.types.delete_schema_versions_input
    import aws_sdk_glue.types.delete_schema_versions_response
    import aws_sdk_glue.types.delete_security_configuration_request
    import aws_sdk_glue.types.delete_security_configuration_response
    import aws_sdk_glue.types.delete_session_request
    import aws_sdk_glue.types.delete_session_response
    import aws_sdk_glue.types.delete_table_optimizer_request
    import aws_sdk_glue.types.delete_table_optimizer_response
    import aws_sdk_glue.types.delete_table_request
    import aws_sdk_glue.types.delete_table_response
    import aws_sdk_glue.types.delete_table_version_request
    import aws_sdk_glue.types.delete_table_version_response
    import aws_sdk_glue.types.delete_trigger_request
    import aws_sdk_glue.types.delete_trigger_response
    import aws_sdk_glue.types.delete_usage_profile_request
    import aws_sdk_glue.types.delete_usage_profile_response
    import aws_sdk_glue.types.delete_user_defined_function_request
    import aws_sdk_glue.types.delete_user_defined_function_response
    import aws_sdk_glue.types.delete_workflow_request
    import aws_sdk_glue.types.delete_workflow_response
    import aws_sdk_glue.types.describe_connection_type_request
    import aws_sdk_glue.types.describe_connection_type_response
    import aws_sdk_glue.types.describe_entity_request
    import aws_sdk_glue.types.describe_entity_response
    import aws_sdk_glue.types.describe_inbound_integrations_request
    import aws_sdk_glue.types.describe_inbound_integrations_response
    import aws_sdk_glue.types.describe_integrations_request
    import aws_sdk_glue.types.describe_integrations_response
    import aws_sdk_glue.types.description
    import aws_sdk_glue.types.description_string
    import aws_sdk_glue.types.description_string_removable
    import aws_sdk_glue.types.dev_endpoint_custom_libraries
    import aws_sdk_glue.types.dev_endpoint_names
    import aws_sdk_glue.types.enable_hybrid_values
    import aws_sdk_glue.types.encryption_configuration
    import aws_sdk_glue.types.entity
    import aws_sdk_glue.types.entity_name
    import aws_sdk_glue.types.event_batching_condition
    import aws_sdk_glue.types.execution_class
    import aws_sdk_glue.types.execution_property
    import aws_sdk_glue.types.exist_condition
    import aws_sdk_glue.types.field
    import aws_sdk_glue.types.filter_predicate
    import aws_sdk_glue.types.filter_string
    import aws_sdk_glue.types.function_type
    import aws_sdk_glue.types.generic512_char_string
    import aws_sdk_glue.types.generic_map
    import aws_sdk_glue.types.generic_string
    import aws_sdk_glue.types.get_blueprint_request
    import aws_sdk_glue.types.get_blueprint_response
    import aws_sdk_glue.types.get_blueprint_run_request
    import aws_sdk_glue.types.get_blueprint_run_response
    import aws_sdk_glue.types.get_blueprint_runs_request
    import aws_sdk_glue.types.get_blueprint_runs_response
    import aws_sdk_glue.types.get_catalog_import_status_request
    import aws_sdk_glue.types.get_catalog_import_status_response
    import aws_sdk_glue.types.get_catalog_request
    import aws_sdk_glue.types.get_catalog_response
    import aws_sdk_glue.types.get_catalogs_request
    import aws_sdk_glue.types.get_catalogs_response
    import aws_sdk_glue.types.get_classifier_request
    import aws_sdk_glue.types.get_classifier_response
    import aws_sdk_glue.types.get_classifiers_request
    import aws_sdk_glue.types.get_classifiers_response
    import aws_sdk_glue.types.get_column_names_list
    import aws_sdk_glue.types.get_column_statistics_for_partition_request
    import aws_sdk_glue.types.get_column_statistics_for_partition_response
    import aws_sdk_glue.types.get_column_statistics_for_table_request
    import aws_sdk_glue.types.get_column_statistics_for_table_response
    import aws_sdk_glue.types.get_column_statistics_task_run_request
    import aws_sdk_glue.types.get_column_statistics_task_run_response
    import aws_sdk_glue.types.get_column_statistics_task_runs_request
    import aws_sdk_glue.types.get_column_statistics_task_runs_response
    import aws_sdk_glue.types.get_column_statistics_task_settings_request
    import aws_sdk_glue.types.get_column_statistics_task_settings_response
    import aws_sdk_glue.types.get_connection_request
    import aws_sdk_glue.types.get_connection_response
    import aws_sdk_glue.types.get_connections_filter
    import aws_sdk_glue.types.get_connections_request
    import aws_sdk_glue.types.get_connections_response
    import aws_sdk_glue.types.get_crawler_metrics_request
    import aws_sdk_glue.types.get_crawler_metrics_response
    import aws_sdk_glue.types.get_crawler_request
    import aws_sdk_glue.types.get_crawler_response
    import aws_sdk_glue.types.get_crawlers_request
    import aws_sdk_glue.types.get_crawlers_response
    import aws_sdk_glue.types.get_custom_entity_type_request
    import aws_sdk_glue.types.get_custom_entity_type_response
    import aws_sdk_glue.types.get_dashboard_url_request
    import aws_sdk_glue.types.get_dashboard_url_response
    import aws_sdk_glue.types.get_data_catalog_encryption_settings_request
    import aws_sdk_glue.types.get_data_catalog_encryption_settings_response
    import aws_sdk_glue.types.get_data_quality_model_request
    import aws_sdk_glue.types.get_data_quality_model_response
    import aws_sdk_glue.types.get_data_quality_model_result_request
    import aws_sdk_glue.types.get_data_quality_model_result_response
    import aws_sdk_glue.types.get_data_quality_result_request
    import aws_sdk_glue.types.get_data_quality_result_response
    import aws_sdk_glue.types.get_data_quality_rule_recommendation_run_request
    import aws_sdk_glue.types.get_data_quality_rule_recommendation_run_response
    import aws_sdk_glue.types.get_data_quality_ruleset_evaluation_run_request
    import aws_sdk_glue.types.get_data_quality_ruleset_evaluation_run_response
    import aws_sdk_glue.types.get_data_quality_ruleset_request
    import aws_sdk_glue.types.get_data_quality_ruleset_response
    import aws_sdk_glue.types.get_database_request
    import aws_sdk_glue.types.get_database_response
    import aws_sdk_glue.types.get_databases_request
    import aws_sdk_glue.types.get_databases_response
    import aws_sdk_glue.types.get_dataflow_graph_request
    import aws_sdk_glue.types.get_dataflow_graph_response
    import aws_sdk_glue.types.get_dev_endpoint_request
    import aws_sdk_glue.types.get_dev_endpoint_response
    import aws_sdk_glue.types.get_dev_endpoints_request
    import aws_sdk_glue.types.get_dev_endpoints_response
    import aws_sdk_glue.types.get_entity_records_request
    import aws_sdk_glue.types.get_entity_records_response
    import aws_sdk_glue.types.get_glue_identity_center_configuration_request
    import aws_sdk_glue.types.get_glue_identity_center_configuration_response
    import aws_sdk_glue.types.get_integration_resource_property_request
    import aws_sdk_glue.types.get_integration_resource_property_response
    import aws_sdk_glue.types.get_integration_table_properties_request
    import aws_sdk_glue.types.get_integration_table_properties_response
    import aws_sdk_glue.types.get_job_bookmark_request
    import aws_sdk_glue.types.get_job_bookmark_response
    import aws_sdk_glue.types.get_job_request
    import aws_sdk_glue.types.get_job_response
    import aws_sdk_glue.types.get_job_run_request
    import aws_sdk_glue.types.get_job_run_response
    import aws_sdk_glue.types.get_job_runs_request
    import aws_sdk_glue.types.get_job_runs_response
    import aws_sdk_glue.types.get_jobs_request
    import aws_sdk_glue.types.get_jobs_response
    import aws_sdk_glue.types.get_mapping_request
    import aws_sdk_glue.types.get_mapping_response
    import aws_sdk_glue.types.get_materialized_view_refresh_task_run_request
    import aws_sdk_glue.types.get_materialized_view_refresh_task_run_response
    import aws_sdk_glue.types.get_ml_task_run_request
    import aws_sdk_glue.types.get_ml_task_run_response
    import aws_sdk_glue.types.get_ml_task_runs_request
    import aws_sdk_glue.types.get_ml_task_runs_response
    import aws_sdk_glue.types.get_ml_transform_request
    import aws_sdk_glue.types.get_ml_transform_response
    import aws_sdk_glue.types.get_ml_transforms_request
    import aws_sdk_glue.types.get_ml_transforms_response
    import aws_sdk_glue.types.get_partition_indexes_request
    import aws_sdk_glue.types.get_partition_indexes_response
    import aws_sdk_glue.types.get_partition_request
    import aws_sdk_glue.types.get_partition_response
    import aws_sdk_glue.types.get_partitions_request
    import aws_sdk_glue.types.get_partitions_response
    import aws_sdk_glue.types.get_plan_request
    import aws_sdk_glue.types.get_plan_response
    import aws_sdk_glue.types.get_registry_input
    import aws_sdk_glue.types.get_registry_response
    import aws_sdk_glue.types.get_resource_policies_request
    import aws_sdk_glue.types.get_resource_policies_response
    import aws_sdk_glue.types.get_resource_policy_request
    import aws_sdk_glue.types.get_resource_policy_response
    import aws_sdk_glue.types.get_schema_by_definition_input
    import aws_sdk_glue.types.get_schema_by_definition_response
    import aws_sdk_glue.types.get_schema_input
    import aws_sdk_glue.types.get_schema_response
    import aws_sdk_glue.types.get_schema_version_input
    import aws_sdk_glue.types.get_schema_version_response
    import aws_sdk_glue.types.get_schema_versions_diff_input
    import aws_sdk_glue.types.get_schema_versions_diff_response
    import aws_sdk_glue.types.get_security_configuration_request
    import aws_sdk_glue.types.get_security_configuration_response
    import aws_sdk_glue.types.get_security_configurations_request
    import aws_sdk_glue.types.get_security_configurations_response
    import aws_sdk_glue.types.get_session_endpoint_request
    import aws_sdk_glue.types.get_session_endpoint_response
    import aws_sdk_glue.types.get_session_request
    import aws_sdk_glue.types.get_session_response
    import aws_sdk_glue.types.get_statement_request
    import aws_sdk_glue.types.get_statement_response
    import aws_sdk_glue.types.get_table_optimizer_request
    import aws_sdk_glue.types.get_table_optimizer_response
    import aws_sdk_glue.types.get_table_request
    import aws_sdk_glue.types.get_table_response
    import aws_sdk_glue.types.get_table_version_request
    import aws_sdk_glue.types.get_table_version_response
    import aws_sdk_glue.types.get_table_versions_request
    import aws_sdk_glue.types.get_table_versions_response
    import aws_sdk_glue.types.get_tables_request
    import aws_sdk_glue.types.get_tables_response
    import aws_sdk_glue.types.get_tags_request
    import aws_sdk_glue.types.get_tags_response
    import aws_sdk_glue.types.get_trigger_request
    import aws_sdk_glue.types.get_trigger_response
    import aws_sdk_glue.types.get_triggers_request
    import aws_sdk_glue.types.get_triggers_response
    import aws_sdk_glue.types.get_unfiltered_partition_metadata_request
    import aws_sdk_glue.types.get_unfiltered_partition_metadata_response
    import aws_sdk_glue.types.get_unfiltered_partitions_metadata_request
    import aws_sdk_glue.types.get_unfiltered_partitions_metadata_response
    import aws_sdk_glue.types.get_unfiltered_table_metadata_request
    import aws_sdk_glue.types.get_unfiltered_table_metadata_response
    import aws_sdk_glue.types.get_usage_profile_request
    import aws_sdk_glue.types.get_usage_profile_response
    import aws_sdk_glue.types.get_user_defined_function_request
    import aws_sdk_glue.types.get_user_defined_function_response
    import aws_sdk_glue.types.get_user_defined_functions_request
    import aws_sdk_glue.types.get_user_defined_functions_response
    import aws_sdk_glue.types.get_workflow_request
    import aws_sdk_glue.types.get_workflow_response
    import aws_sdk_glue.types.get_workflow_run_properties_request
    import aws_sdk_glue.types.get_workflow_run_properties_response
    import aws_sdk_glue.types.get_workflow_run_request
    import aws_sdk_glue.types.get_workflow_run_response
    import aws_sdk_glue.types.get_workflow_runs_request
    import aws_sdk_glue.types.get_workflow_runs_response
    import aws_sdk_glue.types.glue_policy
    import aws_sdk_glue.types.glue_resource_arn
    import aws_sdk_glue.types.glue_resource_type
    import aws_sdk_glue.types.glue_tables
    import aws_sdk_glue.types.glue_version_string
    import aws_sdk_glue.types.hash_string
    import aws_sdk_glue.types.id_string
    import aws_sdk_glue.types.identity_center_instance_arn
    import aws_sdk_glue.types.identity_center_scopes_list
    import aws_sdk_glue.types.import_catalog_to_glue_request
    import aws_sdk_glue.types.import_catalog_to_glue_response
    import aws_sdk_glue.types.inclusion_annotation_list
    import aws_sdk_glue.types.inclusion_annotation_value
    import aws_sdk_glue.types.integer_value
    import aws_sdk_glue.types.integration_additional_encryption_context_map
    import aws_sdk_glue.types.integration_config
    import aws_sdk_glue.types.integration_description
    import aws_sdk_glue.types.integration_filter_list
    import aws_sdk_glue.types.integration_integer
    import aws_sdk_glue.types.integration_resource_property_filter_list
    import aws_sdk_glue.types.integration_tags_list
    import aws_sdk_glue.types.integration_type
    import aws_sdk_glue.types.job
    import aws_sdk_glue.types.job_command
    import aws_sdk_glue.types.job_mode
    import aws_sdk_glue.types.job_name
    import aws_sdk_glue.types.job_name_list
    import aws_sdk_glue.types.job_run
    import aws_sdk_glue.types.job_update
    import aws_sdk_glue.types.lake_formation_configuration
    import aws_sdk_glue.types.language
    import aws_sdk_glue.types.limit
    import aws_sdk_glue.types.lineage_configuration
    import aws_sdk_glue.types.list_blueprints_request
    import aws_sdk_glue.types.list_blueprints_response
    import aws_sdk_glue.types.list_column_statistics_task_runs_request
    import aws_sdk_glue.types.list_column_statistics_task_runs_response
    import aws_sdk_glue.types.list_connection_types_request
    import aws_sdk_glue.types.list_connection_types_response
    import aws_sdk_glue.types.list_crawlers_request
    import aws_sdk_glue.types.list_crawlers_response
    import aws_sdk_glue.types.list_crawls_request
    import aws_sdk_glue.types.list_crawls_response
    import aws_sdk_glue.types.list_custom_entity_types_request
    import aws_sdk_glue.types.list_custom_entity_types_response
    import aws_sdk_glue.types.list_data_quality_results_request
    import aws_sdk_glue.types.list_data_quality_results_response
    import aws_sdk_glue.types.list_data_quality_rule_recommendation_runs_request
    import aws_sdk_glue.types.list_data_quality_rule_recommendation_runs_response
    import aws_sdk_glue.types.list_data_quality_ruleset_evaluation_runs_request
    import aws_sdk_glue.types.list_data_quality_ruleset_evaluation_runs_response
    import aws_sdk_glue.types.list_data_quality_rulesets_request
    import aws_sdk_glue.types.list_data_quality_rulesets_response
    import aws_sdk_glue.types.list_data_quality_statistic_annotations_request
    import aws_sdk_glue.types.list_data_quality_statistic_annotations_response
    import aws_sdk_glue.types.list_data_quality_statistics_request
    import aws_sdk_glue.types.list_data_quality_statistics_response
    import aws_sdk_glue.types.list_dev_endpoints_request
    import aws_sdk_glue.types.list_dev_endpoints_response
    import aws_sdk_glue.types.list_entities_request
    import aws_sdk_glue.types.list_entities_response
    import aws_sdk_glue.types.list_integration_resource_properties_request
    import aws_sdk_glue.types.list_integration_resource_properties_response
    import aws_sdk_glue.types.list_jobs_request
    import aws_sdk_glue.types.list_jobs_response
    import aws_sdk_glue.types.list_materialized_view_refresh_task_runs_request
    import aws_sdk_glue.types.list_materialized_view_refresh_task_runs_response
    import aws_sdk_glue.types.list_ml_transforms_request
    import aws_sdk_glue.types.list_ml_transforms_response
    import aws_sdk_glue.types.list_registries_input
    import aws_sdk_glue.types.list_registries_response
    import aws_sdk_glue.types.list_schema_versions_input
    import aws_sdk_glue.types.list_schema_versions_response
    import aws_sdk_glue.types.list_schemas_input
    import aws_sdk_glue.types.list_schemas_response
    import aws_sdk_glue.types.list_sessions_request
    import aws_sdk_glue.types.list_sessions_response
    import aws_sdk_glue.types.list_statements_request
    import aws_sdk_glue.types.list_statements_response
    import aws_sdk_glue.types.list_table_optimizer_runs_request
    import aws_sdk_glue.types.list_table_optimizer_runs_response
    import aws_sdk_glue.types.list_table_optimizer_runs_token
    import aws_sdk_glue.types.list_triggers_request
    import aws_sdk_glue.types.list_triggers_response
    import aws_sdk_glue.types.list_usage_profiles_request
    import aws_sdk_glue.types.list_usage_profiles_response
    import aws_sdk_glue.types.list_workflows_request
    import aws_sdk_glue.types.list_workflows_response
    import aws_sdk_glue.types.location
    import aws_sdk_glue.types.maintenance_window
    import aws_sdk_glue.types.map_value
    import aws_sdk_glue.types.mapping_list
    import aws_sdk_glue.types.materialized_view_refresh_task_run
    import aws_sdk_glue.types.max_list_table_optimizer_runs_token_results
    import aws_sdk_glue.types.max_results
    import aws_sdk_glue.types.max_results_number
    import aws_sdk_glue.types.max_retries
    import aws_sdk_glue.types.metadata_key_value_pair
    import aws_sdk_glue.types.metadata_list
    import aws_sdk_glue.types.modify_integration_request
    import aws_sdk_glue.types.modify_integration_response
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.next_token
    import aws_sdk_glue.types.node_id_list
    import aws_sdk_glue.types.notification_property
    import aws_sdk_glue.types.nullable_boolean
    import aws_sdk_glue.types.nullable_double
    import aws_sdk_glue.types.nullable_integer
    import aws_sdk_glue.types.open_table_format_input
    import aws_sdk_glue.types.orchestration_arguments_map
    import aws_sdk_glue.types.orchestration_iam_role_arn
    import aws_sdk_glue.types.orchestration_name_string
    import aws_sdk_glue.types.orchestration_page_size25
    import aws_sdk_glue.types.orchestration_page_size200
    import aws_sdk_glue.types.orchestration_policy_json_string
    import aws_sdk_glue.types.orchestration_role_arn
    import aws_sdk_glue.types.orchestration_s3_location
    import aws_sdk_glue.types.orchestration_statement_code_string
    import aws_sdk_glue.types.orchestration_token
    import aws_sdk_glue.types.page_size
    import aws_sdk_glue.types.pagination_token
    import aws_sdk_glue.types.partition_index
    import aws_sdk_glue.types.partition_index_descriptor
    import aws_sdk_glue.types.partition_index_list
    import aws_sdk_glue.types.partition_input
    import aws_sdk_glue.types.partition_input_list
    import aws_sdk_glue.types.permission_list
    import aws_sdk_glue.types.permission_type_list
    import aws_sdk_glue.types.policy_json_string
    import aws_sdk_glue.types.predicate
    import aws_sdk_glue.types.predicate_string
    import aws_sdk_glue.types.profile_configuration
    import aws_sdk_glue.types.public_keys_list
    import aws_sdk_glue.types.put_data_catalog_encryption_settings_request
    import aws_sdk_glue.types.put_data_catalog_encryption_settings_response
    import aws_sdk_glue.types.put_data_quality_profile_annotation_request
    import aws_sdk_glue.types.put_data_quality_profile_annotation_response
    import aws_sdk_glue.types.put_resource_policy_request
    import aws_sdk_glue.types.put_resource_policy_response
    import aws_sdk_glue.types.put_schema_version_metadata_input
    import aws_sdk_glue.types.put_schema_version_metadata_response
    import aws_sdk_glue.types.put_workflow_run_properties_request
    import aws_sdk_glue.types.put_workflow_run_properties_response
    import aws_sdk_glue.types.python_script
    import aws_sdk_glue.types.query_schema_version_metadata_input
    import aws_sdk_glue.types.query_schema_version_metadata_max_results
    import aws_sdk_glue.types.query_schema_version_metadata_response
    import aws_sdk_glue.types.query_session_context
    import aws_sdk_glue.types.recrawl_policy
    import aws_sdk_glue.types.register_connection_type_request
    import aws_sdk_glue.types.register_connection_type_response
    import aws_sdk_glue.types.register_schema_version_input
    import aws_sdk_glue.types.register_schema_version_response
    import aws_sdk_glue.types.registry_id
    import aws_sdk_glue.types.registry_list_item
    import aws_sdk_glue.types.remove_schema_version_metadata_input
    import aws_sdk_glue.types.remove_schema_version_metadata_response
    import aws_sdk_glue.types.replace_boolean
    import aws_sdk_glue.types.reset_job_bookmark_request
    import aws_sdk_glue.types.reset_job_bookmark_response
    import aws_sdk_glue.types.resource_share_type
    import aws_sdk_glue.types.rest_configuration
    import aws_sdk_glue.types.resume_workflow_run_request
    import aws_sdk_glue.types.resume_workflow_run_response
    import aws_sdk_glue.types.role
    import aws_sdk_glue.types.role_arn
    import aws_sdk_glue.types.role_string
    import aws_sdk_glue.types.ruleset_names
    import aws_sdk_glue.types.run_id
    import aws_sdk_glue.types.run_statement_request
    import aws_sdk_glue.types.run_statement_response
    import aws_sdk_glue.types.sample_size_percentage
    import aws_sdk_glue.types.schema_change_policy
    import aws_sdk_glue.types.schema_definition_string
    import aws_sdk_glue.types.schema_diff_type
    import aws_sdk_glue.types.schema_id
    import aws_sdk_glue.types.schema_list_item
    import aws_sdk_glue.types.schema_registry_name_string
    import aws_sdk_glue.types.schema_registry_token_string
    import aws_sdk_glue.types.schema_version_id_string
    import aws_sdk_glue.types.schema_version_list_item
    import aws_sdk_glue.types.schema_version_number
    import aws_sdk_glue.types.search_property_predicates
    import aws_sdk_glue.types.search_tables_request
    import aws_sdk_glue.types.search_tables_response
    import aws_sdk_glue.types.security_configuration
    import aws_sdk_glue.types.segment
    import aws_sdk_glue.types.selected_fields
    import aws_sdk_glue.types.session_command
    import aws_sdk_glue.types.session_type
    import aws_sdk_glue.types.sort_criteria
    import aws_sdk_glue.types.source_control_auth_strategy
    import aws_sdk_glue.types.source_control_details
    import aws_sdk_glue.types.source_control_provider
    import aws_sdk_glue.types.source_processing_properties
    import aws_sdk_glue.types.source_table_config
    import aws_sdk_glue.types.start_blueprint_run_request
    import aws_sdk_glue.types.start_blueprint_run_response
    import aws_sdk_glue.types.start_column_statistics_task_run_request
    import aws_sdk_glue.types.start_column_statistics_task_run_response
    import aws_sdk_glue.types.start_column_statistics_task_run_schedule_request
    import aws_sdk_glue.types.start_column_statistics_task_run_schedule_response
    import aws_sdk_glue.types.start_crawler_request
    import aws_sdk_glue.types.start_crawler_response
    import aws_sdk_glue.types.start_crawler_schedule_request
    import aws_sdk_glue.types.start_crawler_schedule_response
    import aws_sdk_glue.types.start_data_quality_rule_recommendation_run_request
    import aws_sdk_glue.types.start_data_quality_rule_recommendation_run_response
    import aws_sdk_glue.types.start_data_quality_ruleset_evaluation_run_request
    import aws_sdk_glue.types.start_data_quality_ruleset_evaluation_run_response
    import aws_sdk_glue.types.start_export_labels_task_run_request
    import aws_sdk_glue.types.start_export_labels_task_run_response
    import aws_sdk_glue.types.start_import_labels_task_run_request
    import aws_sdk_glue.types.start_import_labels_task_run_response
    import aws_sdk_glue.types.start_job_run_request
    import aws_sdk_glue.types.start_job_run_response
    import aws_sdk_glue.types.start_materialized_view_refresh_task_run_request
    import aws_sdk_glue.types.start_materialized_view_refresh_task_run_response
    import aws_sdk_glue.types.start_ml_evaluation_task_run_request
    import aws_sdk_glue.types.start_ml_evaluation_task_run_response
    import aws_sdk_glue.types.start_ml_labeling_set_generation_task_run_request
    import aws_sdk_glue.types.start_ml_labeling_set_generation_task_run_response
    import aws_sdk_glue.types.start_trigger_request
    import aws_sdk_glue.types.start_trigger_response
    import aws_sdk_glue.types.start_workflow_run_request
    import aws_sdk_glue.types.start_workflow_run_response
    import aws_sdk_glue.types.stop_column_statistics_task_run_request
    import aws_sdk_glue.types.stop_column_statistics_task_run_response
    import aws_sdk_glue.types.stop_column_statistics_task_run_schedule_request
    import aws_sdk_glue.types.stop_column_statistics_task_run_schedule_response
    import aws_sdk_glue.types.stop_crawler_request
    import aws_sdk_glue.types.stop_crawler_response
    import aws_sdk_glue.types.stop_crawler_schedule_request
    import aws_sdk_glue.types.stop_crawler_schedule_response
    import aws_sdk_glue.types.stop_materialized_view_refresh_task_run_request
    import aws_sdk_glue.types.stop_materialized_view_refresh_task_run_response
    import aws_sdk_glue.types.stop_session_request
    import aws_sdk_glue.types.stop_session_response
    import aws_sdk_glue.types.stop_trigger_request
    import aws_sdk_glue.types.stop_trigger_response
    import aws_sdk_glue.types.stop_workflow_run_request
    import aws_sdk_glue.types.stop_workflow_run_response
    import aws_sdk_glue.types.string128
    import aws_sdk_glue.types.string512
    import aws_sdk_glue.types.string1024
    import aws_sdk_glue.types.string2048
    import aws_sdk_glue.types.string_list
    import aws_sdk_glue.types.supported_dialect
    import aws_sdk_glue.types.table_attributes_list
    import aws_sdk_glue.types.table_input
    import aws_sdk_glue.types.table_optimizer_configuration
    import aws_sdk_glue.types.table_optimizer_run
    import aws_sdk_glue.types.table_optimizer_type
    import aws_sdk_glue.types.table_prefix
    import aws_sdk_glue.types.tag_keys_list
    import aws_sdk_glue.types.tag_resource_request
    import aws_sdk_glue.types.tag_resource_response
    import aws_sdk_glue.types.tags_map
    import aws_sdk_glue.types.target_processing_properties
    import aws_sdk_glue.types.target_table_config
    import aws_sdk_glue.types.task_run_filter_criteria
    import aws_sdk_glue.types.task_run_sort_criteria
    import aws_sdk_glue.types.test_connection_input
    import aws_sdk_glue.types.test_connection_request
    import aws_sdk_glue.types.test_connection_response
    import aws_sdk_glue.types.timeout
    import aws_sdk_glue.types.timestamp
    import aws_sdk_glue.types.timestamp_filter
    import aws_sdk_glue.types.token
    import aws_sdk_glue.types.transaction_id_string
    import aws_sdk_glue.types.transform_encryption
    import aws_sdk_glue.types.transform_filter_criteria
    import aws_sdk_glue.types.transform_parameters
    import aws_sdk_glue.types.transform_sort_criteria
    import aws_sdk_glue.types.trigger
    import aws_sdk_glue.types.trigger_name_list
    import aws_sdk_glue.types.trigger_type
    import aws_sdk_glue.types.trigger_update
    import aws_sdk_glue.types.untag_resource_request
    import aws_sdk_glue.types.untag_resource_response
    import aws_sdk_glue.types.update_blueprint_request
    import aws_sdk_glue.types.update_blueprint_response
    import aws_sdk_glue.types.update_catalog_request
    import aws_sdk_glue.types.update_catalog_response
    import aws_sdk_glue.types.update_classifier_request
    import aws_sdk_glue.types.update_classifier_response
    import aws_sdk_glue.types.update_column_statistics_for_partition_request
    import aws_sdk_glue.types.update_column_statistics_for_partition_response
    import aws_sdk_glue.types.update_column_statistics_for_table_request
    import aws_sdk_glue.types.update_column_statistics_for_table_response
    import aws_sdk_glue.types.update_column_statistics_list
    import aws_sdk_glue.types.update_column_statistics_task_settings_request
    import aws_sdk_glue.types.update_column_statistics_task_settings_response
    import aws_sdk_glue.types.update_connection_request
    import aws_sdk_glue.types.update_connection_response
    import aws_sdk_glue.types.update_crawler_request
    import aws_sdk_glue.types.update_crawler_response
    import aws_sdk_glue.types.update_crawler_schedule_request
    import aws_sdk_glue.types.update_crawler_schedule_response
    import aws_sdk_glue.types.update_csv_classifier_request
    import aws_sdk_glue.types.update_data_quality_ruleset_request
    import aws_sdk_glue.types.update_data_quality_ruleset_response
    import aws_sdk_glue.types.update_database_request
    import aws_sdk_glue.types.update_database_response
    import aws_sdk_glue.types.update_dev_endpoint_request
    import aws_sdk_glue.types.update_dev_endpoint_response
    import aws_sdk_glue.types.update_glue_identity_center_configuration_request
    import aws_sdk_glue.types.update_glue_identity_center_configuration_response
    import aws_sdk_glue.types.update_grok_classifier_request
    import aws_sdk_glue.types.update_integration_resource_property_request
    import aws_sdk_glue.types.update_integration_resource_property_response
    import aws_sdk_glue.types.update_integration_table_properties_request
    import aws_sdk_glue.types.update_integration_table_properties_response
    import aws_sdk_glue.types.update_job_from_source_control_request
    import aws_sdk_glue.types.update_job_from_source_control_response
    import aws_sdk_glue.types.update_job_request
    import aws_sdk_glue.types.update_job_response
    import aws_sdk_glue.types.update_json_classifier_request
    import aws_sdk_glue.types.update_ml_transform_request
    import aws_sdk_glue.types.update_ml_transform_response
    import aws_sdk_glue.types.update_open_table_format_input
    import aws_sdk_glue.types.update_partition_request
    import aws_sdk_glue.types.update_partition_response
    import aws_sdk_glue.types.update_registry_input
    import aws_sdk_glue.types.update_registry_response
    import aws_sdk_glue.types.update_schema_input
    import aws_sdk_glue.types.update_schema_response
    import aws_sdk_glue.types.update_source_control_from_job_request
    import aws_sdk_glue.types.update_source_control_from_job_response
    import aws_sdk_glue.types.update_table_optimizer_request
    import aws_sdk_glue.types.update_table_optimizer_response
    import aws_sdk_glue.types.update_table_request
    import aws_sdk_glue.types.update_table_response
    import aws_sdk_glue.types.update_trigger_request
    import aws_sdk_glue.types.update_trigger_response
    import aws_sdk_glue.types.update_usage_profile_request
    import aws_sdk_glue.types.update_usage_profile_response
    import aws_sdk_glue.types.update_user_defined_function_request
    import aws_sdk_glue.types.update_user_defined_function_response
    import aws_sdk_glue.types.update_workflow_request
    import aws_sdk_glue.types.update_workflow_response
    import aws_sdk_glue.types.update_xml_classifier_request
    import aws_sdk_glue.types.uri_string
    import aws_sdk_glue.types.usage_profile_definition
    import aws_sdk_glue.types.user_defined_function_input
    import aws_sdk_glue.types.uui_dv4
    import aws_sdk_glue.types.value_string
    import aws_sdk_glue.types.value_string_list
    import aws_sdk_glue.types.version_string
    import aws_sdk_glue.types.versions_string
    import aws_sdk_glue.types.view_update_action
    import aws_sdk_glue.types.worker_type
    import aws_sdk_glue.types.workflow_description_string
    import aws_sdk_glue.types.workflow_names
    import aws_sdk_glue.types.workflow_run
    import aws_sdk_glue.types.workflow_run_properties


class AsyncGlueClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


class AsyncGlueClient:
    """A client for the ``Glue`` service.

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
        self._config = AsyncGlueClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncGlueClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncGlueClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
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

    async def batch_create_partition(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        partition_input_list: "aws_sdk_glue.types.partition_input_list.PartitionInputList",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.batch_create_partition_response.BatchCreatePartitionResponse":
        """<p>Creates one or more partitions in a batch operation.</p>

        Args:
            catalog_id: <p>The ID of the catalog in which the partition is to be created. Currently, this should be the Amazon Web Services account ID.</p>
            database_name: <p>The name of the metadata database in which the partition is to be created.</p>
            table_name: <p>The name of the metadata table in which the partition is to be created.</p>
            partition_input_list: <p>A list of <code>PartitionInput</code> structures that define the partitions to be created.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.batch_create_partition_request.BatchCreatePartitionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.batch_create_partition_response.BatchCreatePartitionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.batch_create_partition

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.batch_create_partition.async_batch_create_partition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.batch_create_partition_request.BatchCreatePartitionRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        input_["partition_input_list"] = partition_input_list

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_delete_connection(
        self,
        connection_name_list: "aws_sdk_glue.types.delete_connection_name_list.DeleteConnectionNameList",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.batch_delete_connection_response.BatchDeleteConnectionResponse":
        """<p>Deletes a list of connection definitions from the Data Catalog.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog in which the connections reside. If none is provided, the Amazon Web Services account ID is used by default.</p>
            connection_name_list: <p>A list of names of the connections to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.batch_delete_connection_request.BatchDeleteConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.batch_delete_connection_response.BatchDeleteConnectionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.batch_delete_connection

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.batch_delete_connection.async_batch_delete_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.batch_delete_connection_request.BatchDeleteConnectionRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["connection_name_list"] = connection_name_list

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_delete_partition(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        partitions_to_delete: "aws_sdk_glue.types.batch_delete_partition_value_list.BatchDeletePartitionValueList",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.batch_delete_partition_response.BatchDeletePartitionResponse":
        """<p>Deletes one or more partitions in a batch operation.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog where the partition to be deleted resides. If none is provided, the Amazon Web Services account ID is used by default.</p>
            database_name: <p>The name of the catalog database in which the table in question resides.</p>
            table_name: <p>The name of the table that contains the partitions to be deleted.</p>
            partitions_to_delete: <p>A list of <code>PartitionInput</code> structures that define the partitions to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.batch_delete_partition_request.BatchDeletePartitionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.batch_delete_partition_response.BatchDeletePartitionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.batch_delete_partition

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.batch_delete_partition.async_batch_delete_partition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.batch_delete_partition_request.BatchDeletePartitionRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        input_["partitions_to_delete"] = partitions_to_delete

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_delete_table(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        tables_to_delete: "aws_sdk_glue.types.batch_delete_table_name_list.BatchDeleteTableNameList",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
        transaction_id: Optional[
            "aws_sdk_glue.types.transaction_id_string.TransactionIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.batch_delete_table_response.BatchDeleteTableResponse":
        r"""<p>Deletes multiple tables at once.</p> <note> <p>After completing this operation, you no longer have access to the table versions and partitions that belong to the deleted table. Glue deletes these \"orphaned\" resources asynchronously in a timely manner, at the discretion of the service.</p> <p>To ensure the immediate deletion of all related resources, before calling <code>BatchDeleteTable</code>, use <code>DeleteTableVersion</code> or <code>BatchDeleteTableVersion</code>, and <code>DeletePartition</code> or <code>BatchDeletePartition</code>, to delete any resources that belong to the table.</p> </note>

        Args:
            catalog_id: <p>The ID of the Data Catalog where the table resides. If none is provided, the Amazon Web Services account ID is used by default.</p>
            database_name: <p>The name of the catalog database in which the tables to delete reside. For Hive compatibility, this name is entirely lowercase.</p>
            tables_to_delete: <p>A list of the table to delete.</p>
            transaction_id: <p>The transaction ID at which to delete the table contents.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.batch_delete_table_request.BatchDeleteTableRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.batch_delete_table_response.BatchDeleteTableResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.batch_delete_table

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.batch_delete_table.async_batch_delete_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.batch_delete_table_request.BatchDeleteTableRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["tables_to_delete"] = tables_to_delete
        if transaction_id is not None:
            input_["transaction_id"] = transaction_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_delete_table_version(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        version_ids: "aws_sdk_glue.types.batch_delete_table_version_list.BatchDeleteTableVersionList",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.batch_delete_table_version_response.BatchDeleteTableVersionResponse":
        """<p>Deletes a specified batch of versions of a table.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog where the tables reside. If none is provided, the Amazon Web Services account ID is used by default.</p>
            database_name: <p>The database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase.</p>
            table_name: <p>The name of the table. For Hive compatibility, this name is entirely lowercase.</p>
            version_ids: <p>A list of the IDs of versions to be deleted. A <code>VersionId</code> is a string representation of an integer. Each version is incremented by 1.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.batch_delete_table_version_request.BatchDeleteTableVersionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.batch_delete_table_version_response.BatchDeleteTableVersionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.batch_delete_table_version

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.batch_delete_table_version.async_batch_delete_table_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.batch_delete_table_version_request.BatchDeleteTableVersionRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        input_["version_ids"] = version_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_blueprints(
        self,
        names: "aws_sdk_glue.types.batch_get_blueprint_names.BatchGetBlueprintNames",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        include_blueprint: Optional[
            "aws_sdk_glue.types.nullable_boolean.NullableBoolean"
        ] = None,
        include_parameter_spec: Optional[
            "aws_sdk_glue.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "aws_sdk_glue.types.batch_get_blueprints_response.BatchGetBlueprintsResponse":
        """<p>Retrieves information about a list of blueprints.</p>

        Args:
            names: <p>A list of blueprint names.</p>
            include_blueprint: <p>Specifies whether or not to include the blueprint in the response.</p>
            include_parameter_spec: <p>Specifies whether or not to include the parameters, as a JSON string, for the blueprint in the response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.batch_get_blueprints_request.BatchGetBlueprintsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.batch_get_blueprints_response.BatchGetBlueprintsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.batch_get_blueprints

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.batch_get_blueprints.async_batch_get_blueprints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.batch_get_blueprints_request.BatchGetBlueprintsRequest = {}  # type: ignore[typeddict-item]
        input_["names"] = names
        if include_blueprint is not None:
            input_["include_blueprint"] = include_blueprint
        if include_parameter_spec is not None:
            input_["include_parameter_spec"] = include_parameter_spec

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_crawlers(
        self,
        crawler_names: "aws_sdk_glue.types.crawler_name_list.CrawlerNameList",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.batch_get_crawlers_response.BatchGetCrawlersResponse":
        """<p>Returns a list of resource metadata for a given list of crawler names. After calling the <code>ListCrawlers</code> operation, you can call this operation to access the data to which you have been granted permissions. This operation supports all IAM permissions, including permission conditions that uses tags.</p>

        Args:
            crawler_names: <p>A list of crawler names, which might be the names returned from the <code>ListCrawlers</code> operation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.batch_get_crawlers_request.BatchGetCrawlersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.batch_get_crawlers_response.BatchGetCrawlersResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.batch_get_crawlers

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.batch_get_crawlers.async_batch_get_crawlers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.batch_get_crawlers_request.BatchGetCrawlersRequest = {}  # type: ignore[typeddict-item]
        input_["crawler_names"] = crawler_names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_custom_entity_types(
        self,
        names: "aws_sdk_glue.types.custom_entity_type_names.CustomEntityTypeNames",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.batch_get_custom_entity_types_response.BatchGetCustomEntityTypesResponse":
        """<p>Retrieves the details for the custom patterns specified by a list of names.</p>

        Args:
            names: <p>A list of names of the custom patterns that you want to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.batch_get_custom_entity_types_request.BatchGetCustomEntityTypesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.batch_get_custom_entity_types_response.BatchGetCustomEntityTypesResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.batch_get_custom_entity_types

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.batch_get_custom_entity_types.async_batch_get_custom_entity_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.batch_get_custom_entity_types_request.BatchGetCustomEntityTypesRequest = {}  # type: ignore[typeddict-item]
        input_["names"] = names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_data_quality_result(
        self,
        result_ids: "aws_sdk_glue.types.data_quality_result_ids.DataQualityResultIds",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.batch_get_data_quality_result_response.BatchGetDataQualityResultResponse":
        """<p>Retrieves a list of data quality results for the specified result IDs.</p>

        Args:
            result_ids: <p>A list of unique result IDs for the data quality results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.batch_get_data_quality_result_request.BatchGetDataQualityResultRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.batch_get_data_quality_result_response.BatchGetDataQualityResultResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.batch_get_data_quality_result

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.batch_get_data_quality_result.async_batch_get_data_quality_result(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.batch_get_data_quality_result_request.BatchGetDataQualityResultRequest = {}  # type: ignore[typeddict-item]
        input_["result_ids"] = result_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_dev_endpoints(
        self,
        dev_endpoint_names: "aws_sdk_glue.types.dev_endpoint_names.DevEndpointNames",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.batch_get_dev_endpoints_response.BatchGetDevEndpointsResponse":
        """<p>Returns a list of resource metadata for a given list of development endpoint names. After calling the <code>ListDevEndpoints</code> operation, you can call this operation to access the data to which you have been granted permissions. This operation supports all IAM permissions, including permission conditions that uses tags.</p>

        Args:
            dev_endpoint_names: <p>The list of <code>DevEndpoint</code> names, which might be the names returned from the <code>ListDevEndpoint</code> operation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.batch_get_dev_endpoints_request.BatchGetDevEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.batch_get_dev_endpoints_response.BatchGetDevEndpointsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.batch_get_dev_endpoints

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.batch_get_dev_endpoints.async_batch_get_dev_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.batch_get_dev_endpoints_request.BatchGetDevEndpointsRequest = {}  # type: ignore[typeddict-item]
        input_["dev_endpoint_names"] = dev_endpoint_names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_jobs(
        self,
        job_names: "aws_sdk_glue.types.job_name_list.JobNameList",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.batch_get_jobs_response.BatchGetJobsResponse":
        """<p>Returns a list of resource metadata for a given list of job names. After calling the <code>ListJobs</code> operation, you can call this operation to access the data to which you have been granted permissions. This operation supports all IAM permissions, including permission conditions that uses tags. </p>

        Args:
            job_names: <p>A list of job names, which might be the names returned from the <code>ListJobs</code> operation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.batch_get_jobs_request.BatchGetJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.batch_get_jobs_response.BatchGetJobsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.batch_get_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.batch_get_jobs.async_batch_get_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.batch_get_jobs_request.BatchGetJobsRequest = {}  # type: ignore[typeddict-item]
        input_["job_names"] = job_names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_partition(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        partitions_to_get: "aws_sdk_glue.types.batch_get_partition_value_list.BatchGetPartitionValueList",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
        audit_context: Optional["aws_sdk_glue.types.audit_context.AuditContext"] = None,
        query_session_context: Optional[
            "aws_sdk_glue.types.query_session_context.QuerySessionContext"
        ] = None,
    ) -> "aws_sdk_glue.types.batch_get_partition_response.BatchGetPartitionResponse":
        """<p>Retrieves partitions in a batch request.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog where the partitions in question reside. If none is supplied, the Amazon Web Services account ID is used by default.</p>
            database_name: <p>The name of the catalog database where the partitions reside.</p>
            table_name: <p>The name of the partitions' table.</p>
            partitions_to_get: <p>A list of partition values identifying the partitions to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.batch_get_partition_request.BatchGetPartitionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.batch_get_partition_response.BatchGetPartitionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.batch_get_partition

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.batch_get_partition.async_batch_get_partition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.batch_get_partition_request.BatchGetPartitionRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        input_["partitions_to_get"] = partitions_to_get
        if audit_context is not None:
            input_["audit_context"] = audit_context
        if query_session_context is not None:
            input_["query_session_context"] = query_session_context

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_table_optimizer(
        self,
        entries: "aws_sdk_glue.types.batch_get_table_optimizer_entries.BatchGetTableOptimizerEntries",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.batch_get_table_optimizer_response.BatchGetTableOptimizerResponse":
        """<p>Returns the configuration for the specified table optimizers.</p>

        Args:
            entries: <p>A list of <code>BatchGetTableOptimizerEntry</code> objects specifying the table optimizers to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.batch_get_table_optimizer_request.BatchGetTableOptimizerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.batch_get_table_optimizer_response.BatchGetTableOptimizerResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.batch_get_table_optimizer

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.batch_get_table_optimizer.async_batch_get_table_optimizer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.batch_get_table_optimizer_request.BatchGetTableOptimizerRequest = {}  # type: ignore[typeddict-item]
        input_["entries"] = entries

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_triggers(
        self,
        trigger_names: "aws_sdk_glue.types.trigger_name_list.TriggerNameList",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.batch_get_triggers_response.BatchGetTriggersResponse":
        """<p>Returns a list of resource metadata for a given list of trigger names. After calling the <code>ListTriggers</code> operation, you can call this operation to access the data to which you have been granted permissions. This operation supports all IAM permissions, including permission conditions that uses tags.</p>

        Args:
            trigger_names: <p>A list of trigger names, which may be the names returned from the <code>ListTriggers</code> operation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.batch_get_triggers_request.BatchGetTriggersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.batch_get_triggers_response.BatchGetTriggersResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.batch_get_triggers

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.batch_get_triggers.async_batch_get_triggers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.batch_get_triggers_request.BatchGetTriggersRequest = {}  # type: ignore[typeddict-item]
        input_["trigger_names"] = trigger_names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_workflows(
        self,
        names: "aws_sdk_glue.types.workflow_names.WorkflowNames",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        include_graph: Optional[
            "aws_sdk_glue.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "aws_sdk_glue.types.batch_get_workflows_response.BatchGetWorkflowsResponse":
        """<p>Returns a list of resource metadata for a given list of workflow names. After calling the <code>ListWorkflows</code> operation, you can call this operation to access the data to which you have been granted permissions. This operation supports all IAM permissions, including permission conditions that uses tags.</p>

        Args:
            names: <p>A list of workflow names, which may be the names returned from the <code>ListWorkflows</code> operation.</p>
            include_graph: <p>Specifies whether to include a graph when returning the workflow resource metadata.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.batch_get_workflows_request.BatchGetWorkflowsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.batch_get_workflows_response.BatchGetWorkflowsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.batch_get_workflows

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.batch_get_workflows.async_batch_get_workflows(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.batch_get_workflows_request.BatchGetWorkflowsRequest = {}  # type: ignore[typeddict-item]
        input_["names"] = names
        if include_graph is not None:
            input_["include_graph"] = include_graph

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_put_data_quality_statistic_annotation(
        self,
        inclusion_annotations: "aws_sdk_glue.types.inclusion_annotation_list.InclusionAnnotationList",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        client_token: Optional["aws_sdk_glue.types.hash_string.HashString"] = None,
    ) -> "aws_sdk_glue.types.batch_put_data_quality_statistic_annotation_response.BatchPutDataQualityStatisticAnnotationResponse":
        """<p>Annotate datapoints over time for a specific data quality statistic. The API requires both profileID and statisticID as part of the InclusionAnnotation input. The API only works for a single statisticId across multiple profiles.</p>

        Args:
            inclusion_annotations: <p>A list of <code>DatapointInclusionAnnotation</code>'s. The InclusionAnnotations must contain a profileId and statisticId. If there are multiple InclusionAnnotations, the list must refer to a single statisticId across multiple profileIds.</p>
            client_token: <p>Client Token.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.batch_put_data_quality_statistic_annotation_request.BatchPutDataQualityStatisticAnnotationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.batch_put_data_quality_statistic_annotation_response.BatchPutDataQualityStatisticAnnotationResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.batch_put_data_quality_statistic_annotation

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.batch_put_data_quality_statistic_annotation.async_batch_put_data_quality_statistic_annotation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.batch_put_data_quality_statistic_annotation_request.BatchPutDataQualityStatisticAnnotationRequest = {}  # type: ignore[typeddict-item]
        input_["inclusion_annotations"] = inclusion_annotations
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_stop_job_run(
        self,
        job_name: "aws_sdk_glue.types.name_string.NameString",
        job_run_ids: "aws_sdk_glue.types.batch_stop_job_run_job_run_id_list.BatchStopJobRunJobRunIdList",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.batch_stop_job_run_response.BatchStopJobRunResponse":
        """<p>Stops one or more job runs for a specified job definition.</p>

        Args:
            job_name: <p>The name of the job definition for which to stop job runs.</p>
            job_run_ids: <p>A list of the <code>JobRunIds</code> that should be stopped for that job definition.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.batch_stop_job_run_request.BatchStopJobRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.batch_stop_job_run_response.BatchStopJobRunResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.batch_stop_job_run

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.batch_stop_job_run.async_batch_stop_job_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.batch_stop_job_run_request.BatchStopJobRunRequest = {}  # type: ignore[typeddict-item]
        input_["job_name"] = job_name
        input_["job_run_ids"] = job_run_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_update_partition(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        entries: "aws_sdk_glue.types.batch_update_partition_request_entry_list.BatchUpdatePartitionRequestEntryList",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.batch_update_partition_response.BatchUpdatePartitionResponse":
        """<p>Updates one or more partitions in a batch operation.</p>

        Args:
            catalog_id: <p>The ID of the catalog in which the partition is to be updated. Currently, this should be the Amazon Web Services account ID.</p>
            database_name: <p>The name of the metadata database in which the partition is to be updated.</p>
            table_name: <p>The name of the metadata table in which the partition is to be updated.</p>
            entries: <p>A list of up to 100 <code>BatchUpdatePartitionRequestEntry</code> objects to update.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.batch_update_partition_request.BatchUpdatePartitionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.batch_update_partition_response.BatchUpdatePartitionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.batch_update_partition

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.batch_update_partition.async_batch_update_partition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.batch_update_partition_request.BatchUpdatePartitionRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        input_["entries"] = entries

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_data_quality_rule_recommendation_run(
        self,
        run_id: "aws_sdk_glue.types.hash_string.HashString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.cancel_data_quality_rule_recommendation_run_response.CancelDataQualityRuleRecommendationRunResponse":
        """<p>Cancels the specified recommendation run that was being used to generate rules.</p>

        Args:
            run_id: <p>The unique run identifier associated with this run.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.cancel_data_quality_rule_recommendation_run_request.CancelDataQualityRuleRecommendationRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.cancel_data_quality_rule_recommendation_run_response.CancelDataQualityRuleRecommendationRunResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.cancel_data_quality_rule_recommendation_run

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.cancel_data_quality_rule_recommendation_run.async_cancel_data_quality_rule_recommendation_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.cancel_data_quality_rule_recommendation_run_request.CancelDataQualityRuleRecommendationRunRequest = {}  # type: ignore[typeddict-item]
        input_["run_id"] = run_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_data_quality_ruleset_evaluation_run(
        self,
        run_id: "aws_sdk_glue.types.hash_string.HashString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.cancel_data_quality_ruleset_evaluation_run_response.CancelDataQualityRulesetEvaluationRunResponse":
        """<p>Cancels a run where a ruleset is being evaluated against a data source.</p>

        Args:
            run_id: <p>The unique run identifier associated with this run.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.cancel_data_quality_ruleset_evaluation_run_request.CancelDataQualityRulesetEvaluationRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.cancel_data_quality_ruleset_evaluation_run_response.CancelDataQualityRulesetEvaluationRunResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.cancel_data_quality_ruleset_evaluation_run

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.cancel_data_quality_ruleset_evaluation_run.async_cancel_data_quality_ruleset_evaluation_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.cancel_data_quality_ruleset_evaluation_run_request.CancelDataQualityRulesetEvaluationRunRequest = {}  # type: ignore[typeddict-item]
        input_["run_id"] = run_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_ml_task_run(
        self,
        transform_id: "aws_sdk_glue.types.hash_string.HashString",
        task_run_id: "aws_sdk_glue.types.hash_string.HashString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.cancel_ml_task_run_response.CancelMLTaskRunResponse":
        """<p>Cancels (stops) a task run. Machine learning task runs are asynchronous tasks that Glue runs on your behalf as part of various machine learning workflows. You can cancel a machine learning task run at any time by calling <code>CancelMLTaskRun</code> with a task run's parent transform's <code>TransformID</code> and the task run's <code>TaskRunId</code>. </p>

        Args:
            transform_id: <p>The unique identifier of the machine learning transform.</p>
            task_run_id: <p>A unique identifier for the task run.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.cancel_ml_task_run_request.CancelMLTaskRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.cancel_ml_task_run_response.CancelMLTaskRunResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.cancel_ml_task_run

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.cancel_ml_task_run.async_cancel_ml_task_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.cancel_ml_task_run_request.CancelMLTaskRunRequest = {}  # type: ignore[typeddict-item]
        input_["transform_id"] = transform_id
        input_["task_run_id"] = task_run_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_statement(
        self,
        session_id: "aws_sdk_glue.types.name_string.NameString",
        id: "aws_sdk_glue.types.integer_value.IntegerValue",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        request_origin: Optional[
            "aws_sdk_glue.types.orchestration_name_string.OrchestrationNameString"
        ] = None,
    ) -> "aws_sdk_glue.types.cancel_statement_response.CancelStatementResponse":
        """<p>Cancels the statement.</p>

        Args:
            session_id: <p>The Session ID of the statement to be cancelled.</p>
            id: <p>The ID of the statement to be cancelled.</p>
            request_origin: <p>The origin of the request to cancel the statement.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.cancel_statement_request.CancelStatementRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.cancel_statement_response.CancelStatementResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.cancel_statement

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.cancel_statement.async_cancel_statement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.cancel_statement_request.CancelStatementRequest = {}  # type: ignore[typeddict-item]
        input_["session_id"] = session_id
        input_["id"] = id
        if request_origin is not None:
            input_["request_origin"] = request_origin

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def check_schema_version_validity(
        self,
        data_format: "aws_sdk_glue.types.data_format.DataFormat",
        schema_definition: "aws_sdk_glue.types.schema_definition_string.SchemaDefinitionString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.check_schema_version_validity_response.CheckSchemaVersionValidityResponse":
        """<p>Validates the supplied schema. This call has no side effects, it simply validates using the supplied schema using <code>DataFormat</code> as the format. Since it does not take a schema set name, no compatibility checks are performed.</p>

        Args:
            data_format: <p>The data format of the schema definition. Currently <code>AVRO</code>, <code>JSON</code> and <code>PROTOBUF</code> are supported.</p>
            schema_definition: <p>The definition of the schema that has to be validated.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.check_schema_version_validity_input.CheckSchemaVersionValidityInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.check_schema_version_validity_response.CheckSchemaVersionValidityResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.check_schema_version_validity

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.check_schema_version_validity.async_check_schema_version_validity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.check_schema_version_validity_input.CheckSchemaVersionValidityInput = {}  # type: ignore[typeddict-item]
        input_["data_format"] = data_format
        input_["schema_definition"] = schema_definition

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_blueprint(
        self,
        name: "aws_sdk_glue.types.orchestration_name_string.OrchestrationNameString",
        blueprint_location: "aws_sdk_glue.types.orchestration_s3_location.OrchestrationS3Location",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        description: Optional[
            "aws_sdk_glue.types.generic512_char_string.Generic512CharString"
        ] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_glue.types.create_blueprint_response.CreateBlueprintResponse":
        """<p>Registers a blueprint with Glue.</p>

        Args:
            name: <p>The name of the blueprint.</p>
            description: <p>A description of the blueprint.</p>
            blueprint_location: <p>Specifies a path in Amazon S3 where the blueprint is published.</p>
            tags: <p>The tags to be applied to this blueprint.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.create_blueprint_request.CreateBlueprintRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.create_blueprint_response.CreateBlueprintResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.create_blueprint

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.create_blueprint.async_create_blueprint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.create_blueprint_request.CreateBlueprintRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["blueprint_location"] = blueprint_location
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_catalog(
        self,
        name: "aws_sdk_glue.types.catalog_name_string.CatalogNameString",
        catalog_input: "aws_sdk_glue.types.catalog_input.CatalogInput",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_glue.types.create_catalog_response.CreateCatalogResponse":
        """<p>Creates a new catalog in the Glue Data Catalog.</p>

        Args:
            name: <p>The name of the catalog to create.</p>
            catalog_input: <p>A <code>CatalogInput</code> object that defines the metadata for the catalog.</p>
            tags: <p>A map array of key-value pairs, not more than 50 pairs. Each key is a UTF-8 string, not less than 1 or more than 128 bytes long. Each value is a UTF-8 string, not more than 256 bytes long. The tags you assign to the catalog.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.create_catalog_request.CreateCatalogRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.create_catalog_response.CreateCatalogResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.create_catalog

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.create_catalog.async_create_catalog(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.create_catalog_request.CreateCatalogRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["catalog_input"] = catalog_input
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_classifier(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        grok_classifier: Optional[
            "aws_sdk_glue.types.create_grok_classifier_request.CreateGrokClassifierRequest"
        ] = None,
        xml_classifier: Optional[
            "aws_sdk_glue.types.create_xml_classifier_request.CreateXMLClassifierRequest"
        ] = None,
        json_classifier: Optional[
            "aws_sdk_glue.types.create_json_classifier_request.CreateJsonClassifierRequest"
        ] = None,
        csv_classifier: Optional[
            "aws_sdk_glue.types.create_csv_classifier_request.CreateCsvClassifierRequest"
        ] = None,
    ) -> "aws_sdk_glue.types.create_classifier_response.CreateClassifierResponse":
        """<p>Creates a classifier in the user's account. This can be a <code>GrokClassifier</code>, an <code>XMLClassifier</code>, a <code>JsonClassifier</code>, or a <code>CsvClassifier</code>, depending on which field of the request is present.</p>

        Args:
            grok_classifier: <p>A <code>GrokClassifier</code> object specifying the classifier to create.</p>
            xml_classifier: <p>An <code>XMLClassifier</code> object specifying the classifier to create.</p>
            json_classifier: <p>A <code>JsonClassifier</code> object specifying the classifier to create.</p>
            csv_classifier: <p>A <code>CsvClassifier</code> object specifying the classifier to create.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.create_classifier_request.CreateClassifierRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.create_classifier_response.CreateClassifierResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.create_classifier

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.create_classifier.async_create_classifier(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.create_classifier_request.CreateClassifierRequest = {}  # type: ignore[typeddict-item]
        if grok_classifier is not None:
            input_["grok_classifier"] = grok_classifier
        if xml_classifier is not None:
            input_["xml_classifier"] = xml_classifier
        if json_classifier is not None:
            input_["json_classifier"] = json_classifier
        if csv_classifier is not None:
            input_["csv_classifier"] = csv_classifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_column_statistics_task_settings(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        role: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        schedule: Optional["aws_sdk_glue.types.cron_expression.CronExpression"] = None,
        column_name_list: Optional[
            "aws_sdk_glue.types.column_name_list.ColumnNameList"
        ] = None,
        sample_size: Optional[
            "aws_sdk_glue.types.sample_size_percentage.SampleSizePercentage"
        ] = None,
        catalog_id: Optional["aws_sdk_glue.types.name_string.NameString"] = None,
        security_configuration: Optional[
            "aws_sdk_glue.types.name_string.NameString"
        ] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_glue.types.create_column_statistics_task_settings_response.CreateColumnStatisticsTaskSettingsResponse":
        """<p>Creates settings for a column statistics task.</p>

        Args:
            database_name: <p>The name of the database where the table resides.</p>
            table_name: <p>The name of the table for which to generate column statistics.</p>
            role: <p>The role used for running the column statistics.</p>
            schedule: <p>A schedule for running the column statistics, specified in CRON syntax.</p>
            column_name_list: <p>A list of column names for which to run statistics.</p>
            sample_size: <p>The percentage of data to sample.</p>
            catalog_id: <p>The ID of the Data Catalog in which the database resides.</p>
            security_configuration: <p>Name of the security configuration that is used to encrypt CloudWatch logs.</p>
            tags: <p>A map of tags.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.create_column_statistics_task_settings_request.CreateColumnStatisticsTaskSettingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.create_column_statistics_task_settings_response.CreateColumnStatisticsTaskSettingsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.create_column_statistics_task_settings

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.create_column_statistics_task_settings.async_create_column_statistics_task_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.create_column_statistics_task_settings_request.CreateColumnStatisticsTaskSettingsRequest = {}  # type: ignore[typeddict-item]
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        input_["role"] = role
        if schedule is not None:
            input_["schedule"] = schedule
        if column_name_list is not None:
            input_["column_name_list"] = column_name_list
        if sample_size is not None:
            input_["sample_size"] = sample_size
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        if security_configuration is not None:
            input_["security_configuration"] = security_configuration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_connection(
        self,
        connection_input: "aws_sdk_glue.types.connection_input.ConnectionInput",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_glue.types.create_connection_response.CreateConnectionResponse":
        """<p>Creates a connection definition in the Data Catalog.</p> <p>Connections used for creating federated resources require the IAM <code>glue:PassConnection</code> permission.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog in which to create the connection. If none is provided, the Amazon Web Services account ID is used by default.</p>
            connection_input: <p>A <code>ConnectionInput</code> object defining the connection to create.</p>
            tags: <p>The tags you assign to the connection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.create_connection_request.CreateConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.create_connection_response.CreateConnectionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.create_connection

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.create_connection.async_create_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.create_connection_request.CreateConnectionRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["connection_input"] = connection_input
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_crawler(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        role: "aws_sdk_glue.types.role.Role",
        targets: "aws_sdk_glue.types.crawler_targets.CrawlerTargets",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        database_name: Optional["aws_sdk_glue.types.database_name.DatabaseName"] = None,
        description: Optional[
            "aws_sdk_glue.types.description_string.DescriptionString"
        ] = None,
        schedule: Optional["aws_sdk_glue.types.cron_expression.CronExpression"] = None,
        classifiers: Optional[
            "aws_sdk_glue.types.classifier_name_list.ClassifierNameList"
        ] = None,
        table_prefix: Optional["aws_sdk_glue.types.table_prefix.TablePrefix"] = None,
        schema_change_policy: Optional[
            "aws_sdk_glue.types.schema_change_policy.SchemaChangePolicy"
        ] = None,
        recrawl_policy: Optional[
            "aws_sdk_glue.types.recrawl_policy.RecrawlPolicy"
        ] = None,
        lineage_configuration: Optional[
            "aws_sdk_glue.types.lineage_configuration.LineageConfiguration"
        ] = None,
        lake_formation_configuration: Optional[
            "aws_sdk_glue.types.lake_formation_configuration.LakeFormationConfiguration"
        ] = None,
        configuration: Optional[
            "aws_sdk_glue.types.crawler_configuration.CrawlerConfiguration"
        ] = None,
        crawler_security_configuration: Optional[
            "aws_sdk_glue.types.crawler_security_configuration.CrawlerSecurityConfiguration"
        ] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_glue.types.create_crawler_response.CreateCrawlerResponse":
        r"""<p>Creates a new crawler with specified targets, role, configuration, and optional schedule. At least one crawl target must be specified, in the <code>s3Targets</code> field, the <code>jdbcTargets</code> field, or the <code>DynamoDBTargets</code> field.</p>

        Args:
            name: <p>Name of the new crawler.</p>
            role: <p>The IAM role or Amazon Resource Name (ARN) of an IAM role used by the new crawler to access customer resources.</p>
            database_name: <p>The Glue database where results are written, such as: <code>arn:aws:daylight:us-east-1::database/sometable/*</code>.</p>
            description: <p>A description of the new crawler.</p>
            targets: <p>A list of collection of targets to crawl.</p>
            schedule: <p>A <code>cron</code> expression used to specify the schedule (see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html\">Time-Based Schedules for Jobs and Crawlers</a>. For example, to run something every day at 12:15 UTC, you would specify: <code>cron(15 12 * * ? *)</code>.</p>
            classifiers: <p>A list of custom classifiers that the user has registered. By default, all built-in classifiers are included in a crawl, but these custom classifiers always override the default classifiers for a given classification.</p>
            table_prefix: <p>The table prefix used for catalog tables that are created.</p>
            schema_change_policy: <p>The policy for the crawler's update and deletion behavior.</p>
            recrawl_policy: <p>A policy that specifies whether to crawl the entire dataset again, or to crawl only folders that were added since the last crawler run.</p>
            lineage_configuration: <p>Specifies data lineage configuration settings for the crawler.</p>
            lake_formation_configuration: <p>Specifies Lake Formation configuration settings for the crawler.</p>
            configuration: <p>Crawler configuration information. This versioned JSON string allows users to specify aspects of a crawler's behavior. For more information, see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/crawler-configuration.html\">Setting crawler configuration options</a>.</p>
            crawler_security_configuration: <p>The name of the <code>SecurityConfiguration</code> structure to be used by this crawler.</p>
            tags: <p>The tags to use with this crawler request. You may use tags to limit access to the crawler. For more information about tags in Glue, see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html\">Amazon Web Services Tags in Glue</a> in the developer guide.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.create_crawler_request.CreateCrawlerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.create_crawler_response.CreateCrawlerResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.create_crawler

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.create_crawler.async_create_crawler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.create_crawler_request.CreateCrawlerRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["role"] = role
        if database_name is not None:
            input_["database_name"] = database_name
        if description is not None:
            input_["description"] = description
        input_["targets"] = targets
        if schedule is not None:
            input_["schedule"] = schedule
        if classifiers is not None:
            input_["classifiers"] = classifiers
        if table_prefix is not None:
            input_["table_prefix"] = table_prefix
        if schema_change_policy is not None:
            input_["schema_change_policy"] = schema_change_policy
        if recrawl_policy is not None:
            input_["recrawl_policy"] = recrawl_policy
        if lineage_configuration is not None:
            input_["lineage_configuration"] = lineage_configuration
        if lake_formation_configuration is not None:
            input_["lake_formation_configuration"] = lake_formation_configuration
        if configuration is not None:
            input_["configuration"] = configuration
        if crawler_security_configuration is not None:
            input_["crawler_security_configuration"] = crawler_security_configuration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_custom_entity_type(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        regex_string: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        context_words: Optional["aws_sdk_glue.types.context_words.ContextWords"] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_glue.types.create_custom_entity_type_response.CreateCustomEntityTypeResponse":
        """<p>Creates a custom pattern that is used to detect sensitive data across the columns and rows of your structured data.</p> <p>Each custom pattern you create specifies a regular expression and an optional list of context words. If no context words are passed only a regular expression is checked.</p>

        Args:
            name: <p>A name for the custom pattern that allows it to be retrieved or deleted later. This name must be unique per Amazon Web Services account.</p>
            regex_string: <p>A regular expression string that is used for detecting sensitive data in a custom pattern.</p>
            context_words: <p>A list of context words. If none of these context words are found within the vicinity of the regular expression the data will not be detected as sensitive data.</p> <p>If no context words are passed only a regular expression is checked.</p>
            tags: <p>A list of tags applied to the custom entity type.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.create_custom_entity_type_request.CreateCustomEntityTypeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.create_custom_entity_type_response.CreateCustomEntityTypeResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.create_custom_entity_type

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.create_custom_entity_type.async_create_custom_entity_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.create_custom_entity_type_request.CreateCustomEntityTypeRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["regex_string"] = regex_string
        if context_words is not None:
            input_["context_words"] = context_words
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_database(
        self,
        database_input: "aws_sdk_glue.types.database_input.DatabaseInput",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_glue.types.create_database_response.CreateDatabaseResponse":
        """<p>Creates a new database in a Data Catalog.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog in which to create the database. If none is provided, the Amazon Web Services account ID is used by default.</p>
            database_input: <p>The metadata for the database.</p>
            tags: <p>The tags you assign to the database.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.create_database_request.CreateDatabaseRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.create_database_response.CreateDatabaseResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.create_database

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.create_database.async_create_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.create_database_request.CreateDatabaseRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_input"] = database_input
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_data_quality_ruleset(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        ruleset: "aws_sdk_glue.types.data_quality_ruleset_string.DataQualityRulesetString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        description: Optional[
            "aws_sdk_glue.types.description_string.DescriptionString"
        ] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
        target_table: Optional[
            "aws_sdk_glue.types.data_quality_target_table.DataQualityTargetTable"
        ] = None,
        data_quality_security_configuration: Optional[
            "aws_sdk_glue.types.name_string.NameString"
        ] = None,
        client_token: Optional["aws_sdk_glue.types.hash_string.HashString"] = None,
    ) -> "aws_sdk_glue.types.create_data_quality_ruleset_response.CreateDataQualityRulesetResponse":
        """<p>Creates a data quality ruleset with DQDL rules applied to a specified Glue table.</p> <p>You create the ruleset using the Data Quality Definition Language (DQDL). For more information, see the Glue developer guide.</p>

        Args:
            name: <p>A unique name for the data quality ruleset.</p>
            description: <p>A description of the data quality ruleset.</p>
            ruleset: <p>A Data Quality Definition Language (DQDL) ruleset. For more information, see the Glue developer guide.</p>
            tags: <p>A list of tags applied to the data quality ruleset.</p>
            target_table: <p>A target table associated with the data quality ruleset.</p>
            data_quality_security_configuration: <p>The name of the security configuration created with the data quality encryption option.</p>
            client_token: <p>Used for idempotency and is recommended to be set to a random ID (such as a UUID) to avoid creating or starting multiple instances of the same resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.create_data_quality_ruleset_request.CreateDataQualityRulesetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.create_data_quality_ruleset_response.CreateDataQualityRulesetResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.create_data_quality_ruleset

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.create_data_quality_ruleset.async_create_data_quality_ruleset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.create_data_quality_ruleset_request.CreateDataQualityRulesetRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["ruleset"] = ruleset
        if tags is not None:
            input_["tags"] = tags
        if target_table is not None:
            input_["target_table"] = target_table
        if data_quality_security_configuration is not None:
            input_["data_quality_security_configuration"] = (
                data_quality_security_configuration
            )
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_dev_endpoint(
        self,
        endpoint_name: "aws_sdk_glue.types.generic_string.GenericString",
        role_arn: "aws_sdk_glue.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        security_group_ids: Optional[
            "aws_sdk_glue.types.string_list.StringList"
        ] = None,
        subnet_id: Optional["aws_sdk_glue.types.generic_string.GenericString"] = None,
        public_key: Optional["aws_sdk_glue.types.generic_string.GenericString"] = None,
        public_keys: Optional[
            "aws_sdk_glue.types.public_keys_list.PublicKeysList"
        ] = None,
        number_of_nodes: Optional[
            "aws_sdk_glue.types.integer_value.IntegerValue"
        ] = None,
        worker_type: Optional["aws_sdk_glue.types.worker_type.WorkerType"] = None,
        glue_version: Optional[
            "aws_sdk_glue.types.glue_version_string.GlueVersionString"
        ] = None,
        number_of_workers: Optional[
            "aws_sdk_glue.types.nullable_integer.NullableInteger"
        ] = None,
        extra_python_libs_s3_path: Optional[
            "aws_sdk_glue.types.generic_string.GenericString"
        ] = None,
        extra_jars_s3_path: Optional[
            "aws_sdk_glue.types.generic_string.GenericString"
        ] = None,
        security_configuration: Optional[
            "aws_sdk_glue.types.name_string.NameString"
        ] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
        arguments: Optional["aws_sdk_glue.types.map_value.MapValue"] = None,
    ) -> "aws_sdk_glue.types.create_dev_endpoint_response.CreateDevEndpointResponse":
        r"""<p>Creates a new development endpoint.</p>

        Args:
            endpoint_name: <p>The name to be assigned to the new <code>DevEndpoint</code>.</p>
            role_arn: <p>The IAM role for the <code>DevEndpoint</code>.</p>
            security_group_ids: <p>Security group IDs for the security groups to be used by the new <code>DevEndpoint</code>.</p>
            subnet_id: <p>The subnet ID for the new <code>DevEndpoint</code> to use.</p>
            public_key: <p>The public key to be used by this <code>DevEndpoint</code> for authentication. This attribute is provided for backward compatibility because the recommended attribute to use is public keys.</p>
            public_keys: <p>A list of public keys to be used by the development endpoints for authentication. The use of this attribute is preferred over a single public key because the public keys allow you to have a different private key per client.</p> <note> <p>If you previously created an endpoint with a public key, you must remove that key to be able to set a list of public keys. Call the <code>UpdateDevEndpoint</code> API with the public key content in the <code>deletePublicKeys</code> attribute, and the list of new keys in the <code>addPublicKeys</code> attribute.</p> </note>
            number_of_nodes: <p>The number of Glue Data Processing Units (DPUs) to allocate to this <code>DevEndpoint</code>.</p>
            worker_type: <p>The type of predefined worker that is allocated to the development endpoint. Accepts a value of Standard, G.1X, or G.2X.</p> <ul> <li> <p>For the <code>Standard</code> worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.</p> </li> <li> <p>For the <code>G.1X</code> worker type, each worker maps to 1 DPU (4 vCPU, 16 GB of memory, 64 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.</p> </li> <li> <p>For the <code>G.2X</code> worker type, each worker maps to 2 DPU (8 vCPU, 32 GB of memory, 128 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.</p> </li> </ul> <p>Known issue: when a development endpoint is created with the <code>G.2X</code> <code>WorkerType</code> configuration, the Spark drivers for the development endpoint will run on 4 vCPU, 16 GB of memory, and a 64 GB disk. </p>
            glue_version: <p>Glue version determines the versions of Apache Spark and Python that Glue supports. The Python version indicates the version supported for running your ETL scripts on development endpoints. </p> <p>For more information about the available Glue versions and corresponding Spark and Python versions, see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/add-job.html\">Glue version</a> in the developer guide.</p> <p>Development endpoints that are created without specifying a Glue version default to Glue 0.9.</p> <p>You can specify a version of Python support for development endpoints by using the <code>Arguments</code> parameter in the <code>CreateDevEndpoint</code> or <code>UpdateDevEndpoint</code> APIs. If no arguments are provided, the version defaults to Python 2.</p>
            number_of_workers: <p>The number of workers of a defined <code>workerType</code> that are allocated to the development endpoint.</p> <p>The maximum number of workers you can define are 299 for <code>G.1X</code>, and 149 for <code>G.2X</code>. </p>
            extra_python_libs_s3_path: <p>The paths to one or more Python libraries in an Amazon S3 bucket that should be loaded in your <code>DevEndpoint</code>. Multiple values must be complete paths separated by a comma.</p> <note> <p>You can only use pure Python libraries with a <code>DevEndpoint</code>. Libraries that rely on C extensions, such as the <a href=\"http://pandas.pydata.org/\">pandas</a> Python data analysis library, are not yet supported.</p> </note>
            extra_jars_s3_path: <p>The path to one or more Java <code>.jar</code> files in an S3 bucket that should be loaded in your <code>DevEndpoint</code>.</p>
            security_configuration: <p>The name of the <code>SecurityConfiguration</code> structure to be used with this <code>DevEndpoint</code>.</p>
            tags: <p>The tags to use with this DevEndpoint. You may use tags to limit access to the DevEndpoint. For more information about tags in Glue, see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html\">Amazon Web Services Tags in Glue</a> in the developer guide.</p>
            arguments: <p>A map of arguments used to configure the <code>DevEndpoint</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.create_dev_endpoint_request.CreateDevEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.create_dev_endpoint_response.CreateDevEndpointResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.create_dev_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.create_dev_endpoint.async_create_dev_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.create_dev_endpoint_request.CreateDevEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["endpoint_name"] = endpoint_name
        input_["role_arn"] = role_arn
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if subnet_id is not None:
            input_["subnet_id"] = subnet_id
        if public_key is not None:
            input_["public_key"] = public_key
        if public_keys is not None:
            input_["public_keys"] = public_keys
        if number_of_nodes is not None:
            input_["number_of_nodes"] = number_of_nodes
        if worker_type is not None:
            input_["worker_type"] = worker_type
        if glue_version is not None:
            input_["glue_version"] = glue_version
        if number_of_workers is not None:
            input_["number_of_workers"] = number_of_workers
        if extra_python_libs_s3_path is not None:
            input_["extra_python_libs_s3_path"] = extra_python_libs_s3_path
        if extra_jars_s3_path is not None:
            input_["extra_jars_s3_path"] = extra_jars_s3_path
        if security_configuration is not None:
            input_["security_configuration"] = security_configuration
        if tags is not None:
            input_["tags"] = tags
        if arguments is not None:
            input_["arguments"] = arguments

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_glue_identity_center_configuration(
        self,
        instance_arn: "aws_sdk_glue.types.identity_center_instance_arn.IdentityCenterInstanceArn",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        scopes: Optional[
            "aws_sdk_glue.types.identity_center_scopes_list.IdentityCenterScopesList"
        ] = None,
        user_background_sessions_enabled: Optional[
            "aws_sdk_glue.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "aws_sdk_glue.types.create_glue_identity_center_configuration_response.CreateGlueIdentityCenterConfigurationResponse":
        """<p>Creates a new Glue Identity Center configuration to enable integration between Glue and Amazon Web Services IAM Identity Center for authentication and authorization.</p>

        Args:
            instance_arn: <p>The Amazon Resource Name (ARN) of the Identity Center instance to be associated with the Glue configuration.</p>
            scopes: <p>A list of Identity Center scopes that define the permissions and access levels for the Glue configuration.</p>
            user_background_sessions_enabled: <p>Specifies whether users can run background sessions when using Identity Center authentication with Glue services.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.create_glue_identity_center_configuration_request.CreateGlueIdentityCenterConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.create_glue_identity_center_configuration_response.CreateGlueIdentityCenterConfigurationResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.create_glue_identity_center_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.create_glue_identity_center_configuration.async_create_glue_identity_center_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.create_glue_identity_center_configuration_request.CreateGlueIdentityCenterConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["instance_arn"] = instance_arn
        if scopes is not None:
            input_["scopes"] = scopes
        if user_background_sessions_enabled is not None:
            input_["user_background_sessions_enabled"] = (
                user_background_sessions_enabled
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_integration(
        self,
        integration_name: "aws_sdk_glue.types.string128.String128",
        source_arn: "aws_sdk_glue.types.string512.String512",
        target_arn: "aws_sdk_glue.types.string512.String512",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        description: Optional[
            "aws_sdk_glue.types.integration_description.IntegrationDescription"
        ] = None,
        data_filter: Optional["aws_sdk_glue.types.string2048.String2048"] = None,
        kms_key_id: Optional["aws_sdk_glue.types.string2048.String2048"] = None,
        additional_encryption_context: Optional[
            "aws_sdk_glue.types.integration_additional_encryption_context_map.IntegrationAdditionalEncryptionContextMap"
        ] = None,
        tags: Optional[
            "aws_sdk_glue.types.integration_tags_list.IntegrationTagsList"
        ] = None,
        integration_config: Optional[
            "aws_sdk_glue.types.integration_config.IntegrationConfig"
        ] = None,
    ) -> "aws_sdk_glue.types.create_integration_response.CreateIntegrationResponse":
        """<p>Creates a Zero-ETL integration in the caller's account between two resources with Amazon Resource Names (ARNs): the <code>SourceArn</code> and <code>TargetArn</code>.</p>

        Args:
            integration_name: <p>A unique name for an integration in Glue.</p>
            source_arn: <p>The ARN of the source resource for the integration.</p>
            target_arn: <p>The ARN of the target resource for the integration.</p>
            description: <p>A description of the integration.</p>
            data_filter: <p>Selects source tables for the integration using Maxwell filter syntax.</p>
            kms_key_id: <p>The ARN of a KMS key used for encrypting the channel.</p>
            additional_encryption_context: <p>An optional set of non-secret key–value pairs that contains additional contextual information for encryption. This can only be provided if <code>KMSKeyId</code> is provided.</p>
            tags: <p>Metadata assigned to the resource consisting of a list of key-value pairs.</p>
            integration_config: <p>The configuration settings.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.create_integration_request.CreateIntegrationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.create_integration_response.CreateIntegrationResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.create_integration

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.create_integration.async_create_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.create_integration_request.CreateIntegrationRequest = {}  # type: ignore[typeddict-item]
        input_["integration_name"] = integration_name
        input_["source_arn"] = source_arn
        input_["target_arn"] = target_arn
        if description is not None:
            input_["description"] = description
        if data_filter is not None:
            input_["data_filter"] = data_filter
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if additional_encryption_context is not None:
            input_["additional_encryption_context"] = additional_encryption_context
        if tags is not None:
            input_["tags"] = tags
        if integration_config is not None:
            input_["integration_config"] = integration_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_integration_resource_property(
        self,
        resource_arn: "aws_sdk_glue.types.string512.String512",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        source_processing_properties: Optional[
            "aws_sdk_glue.types.source_processing_properties.SourceProcessingProperties"
        ] = None,
        target_processing_properties: Optional[
            "aws_sdk_glue.types.target_processing_properties.TargetProcessingProperties"
        ] = None,
        tags: Optional[
            "aws_sdk_glue.types.integration_tags_list.IntegrationTagsList"
        ] = None,
    ) -> "aws_sdk_glue.types.create_integration_resource_property_response.CreateIntegrationResourcePropertyResponse":
        """<p>This API can be used for setting up the <code>ResourceProperty</code> of the Glue connection (for the source) or Glue database ARN (for the target). These properties can include the role to access the connection or database. To set both source and target properties the same API needs to be invoked with the Glue connection ARN as <code>ResourceArn</code> with <code>SourceProcessingProperties</code> and the Glue database ARN as <code>ResourceArn</code> with <code>TargetProcessingProperties</code> respectively.</p>

        Args:
            resource_arn: <p>The connection ARN of the source, or the database ARN of the target.</p>
            source_processing_properties: <p>The resource properties associated with the integration source.</p>
            target_processing_properties: <p>The resource properties associated with the integration target.</p>
            tags: <p>Metadata assigned to the resource consisting of a list of key-value pairs.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.create_integration_resource_property_request.CreateIntegrationResourcePropertyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.create_integration_resource_property_response.CreateIntegrationResourcePropertyResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.create_integration_resource_property

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.create_integration_resource_property.async_create_integration_resource_property(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.create_integration_resource_property_request.CreateIntegrationResourcePropertyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        if source_processing_properties is not None:
            input_["source_processing_properties"] = source_processing_properties
        if target_processing_properties is not None:
            input_["target_processing_properties"] = target_processing_properties
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_integration_table_properties(
        self,
        resource_arn: "aws_sdk_glue.types.string512.String512",
        table_name: "aws_sdk_glue.types.string128.String128",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        source_table_config: Optional[
            "aws_sdk_glue.types.source_table_config.SourceTableConfig"
        ] = None,
        target_table_config: Optional[
            "aws_sdk_glue.types.target_table_config.TargetTableConfig"
        ] = None,
    ) -> "aws_sdk_glue.types.create_integration_table_properties_response.CreateIntegrationTablePropertiesResponse":
        """<p>This API is used to provide optional override properties for the the tables that need to be replicated. These properties can include properties for filtering and partitioning for the source and target tables. To set both source and target properties the same API need to be invoked with the Glue connection ARN as <code>ResourceArn</code> with <code>SourceTableConfig</code>, and the Glue database ARN as <code>ResourceArn</code> with <code>TargetTableConfig</code> respectively.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the target table for which to create integration table properties. Currently, this API only supports creating integration table properties for target tables, and the provided ARN should be the ARN of the target table in the Glue Data Catalog. Support for creating integration table properties for source connections (using the connection ARN) is not yet implemented and will be added in a future release. </p>
            table_name: <p>The name of the table to be replicated.</p>
            source_table_config: <p>A structure for the source table configuration. See the <code>SourceTableConfig</code> structure to see list of supported source properties.</p>
            target_table_config: <p>A structure for the target table configuration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.create_integration_table_properties_request.CreateIntegrationTablePropertiesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.create_integration_table_properties_response.CreateIntegrationTablePropertiesResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.create_integration_table_properties

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.create_integration_table_properties.async_create_integration_table_properties(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.create_integration_table_properties_request.CreateIntegrationTablePropertiesRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["table_name"] = table_name
        if source_table_config is not None:
            input_["source_table_config"] = source_table_config
        if target_table_config is not None:
            input_["target_table_config"] = target_table_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_job(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        role: "aws_sdk_glue.types.role_string.RoleString",
        command: "aws_sdk_glue.types.job_command.JobCommand",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        job_mode: Optional["aws_sdk_glue.types.job_mode.JobMode"] = None,
        job_run_queuing_enabled: Optional[
            "aws_sdk_glue.types.nullable_boolean.NullableBoolean"
        ] = None,
        description: Optional[
            "aws_sdk_glue.types.description_string.DescriptionString"
        ] = None,
        log_uri: Optional["aws_sdk_glue.types.uri_string.UriString"] = None,
        execution_property: Optional[
            "aws_sdk_glue.types.execution_property.ExecutionProperty"
        ] = None,
        default_arguments: Optional["aws_sdk_glue.types.generic_map.GenericMap"] = None,
        non_overridable_arguments: Optional[
            "aws_sdk_glue.types.generic_map.GenericMap"
        ] = None,
        connections: Optional[
            "aws_sdk_glue.types.connections_list.ConnectionsList"
        ] = None,
        max_retries: Optional["aws_sdk_glue.types.max_retries.MaxRetries"] = None,
        allocated_capacity: Optional[
            "aws_sdk_glue.types.integer_value.IntegerValue"
        ] = None,
        timeout: Optional["aws_sdk_glue.types.timeout.Timeout"] = None,
        max_capacity: Optional[
            "aws_sdk_glue.types.nullable_double.NullableDouble"
        ] = None,
        security_configuration: Optional[
            "aws_sdk_glue.types.name_string.NameString"
        ] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
        notification_property: Optional[
            "aws_sdk_glue.types.notification_property.NotificationProperty"
        ] = None,
        glue_version: Optional[
            "aws_sdk_glue.types.glue_version_string.GlueVersionString"
        ] = None,
        number_of_workers: Optional[
            "aws_sdk_glue.types.nullable_integer.NullableInteger"
        ] = None,
        worker_type: Optional["aws_sdk_glue.types.worker_type.WorkerType"] = None,
        code_gen_configuration_nodes: Optional[
            "aws_sdk_glue.types.code_gen_configuration_nodes.CodeGenConfigurationNodes"
        ] = None,
        execution_class: Optional[
            "aws_sdk_glue.types.execution_class.ExecutionClass"
        ] = None,
        source_control_details: Optional[
            "aws_sdk_glue.types.source_control_details.SourceControlDetails"
        ] = None,
        maintenance_window: Optional[
            "aws_sdk_glue.types.maintenance_window.MaintenanceWindow"
        ] = None,
    ) -> "aws_sdk_glue.types.create_job_response.CreateJobResponse":
        r"""<p>Creates a new job definition.</p>

        Args:
            name: <p>The name you assign to this job definition. It must be unique in your account.</p>
            job_mode: <p>A mode that describes how a job was created. Valid values are:</p> <ul> <li> <p> <code>SCRIPT</code> - The job was created using the Glue Studio script editor.</p> </li> <li> <p> <code>VISUAL</code> - The job was created using the Glue Studio visual editor.</p> </li> <li> <p> <code>NOTEBOOK</code> - The job was created using an interactive sessions notebook.</p> </li> </ul> <p>When the <code>JobMode</code> field is missing or null, <code>SCRIPT</code> is assigned as the default value.</p>
            job_run_queuing_enabled: <p>Specifies whether job run queuing is enabled for the job runs for this job.</p> <p>A value of true means job run queuing is enabled for the job runs. If false or not populated, the job runs will not be considered for queueing.</p> <p>If this field does not match the value set in the job run, then the value from the job run field will be used.</p>
            description: <p>Description of the job being defined.</p>
            log_uri: <p>This field is reserved for future use.</p>
            role: <p>The name or Amazon Resource Name (ARN) of the IAM role associated with this job.</p>
            execution_property: <p>An <code>ExecutionProperty</code> specifying the maximum number of concurrent runs allowed for this job.</p>
            command: <p>The <code>JobCommand</code> that runs this job.</p>
            default_arguments: <p>The default arguments for every run of this job, specified as name-value pairs.</p> <p>You can specify arguments here that your own job-execution script consumes, as well as arguments that Glue itself consumes.</p> <p>Job arguments may be logged. Do not pass plaintext secrets as arguments. Retrieve secrets from a Glue Connection, Secrets Manager or other secret management mechanism if you intend to keep them within the Job. </p> <p>For information about how to specify and consume your own Job arguments, see the <a href=\"https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html\">Calling Glue APIs in Python</a> topic in the developer guide.</p> <p>For information about the arguments you can provide to this field when configuring Spark jobs, see the <a href=\"https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html\">Special Parameters Used by Glue</a> topic in the developer guide.</p> <p>For information about the arguments you can provide to this field when configuring Ray jobs, see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/author-job-ray-job-parameters.html\">Using job parameters in Ray jobs</a> in the developer guide.</p>
            non_overridable_arguments: <p>Arguments for this job that are not overridden when providing job arguments in a job run, specified as name-value pairs.</p>
            connections: <p>The connections used for this job.</p>
            max_retries: <p>The maximum number of times to retry this job if it fails.</p>
            allocated_capacity: <p>This parameter is deprecated. Use <code>MaxCapacity</code> instead.</p> <p>The number of Glue data processing units (DPUs) to allocate to this Job. You can allocate a minimum of 2 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the <a href=\"https://aws.amazon.com/glue/pricing/\">Glue pricing page</a>.</p>
            timeout: <p>The job timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters <code>TIMEOUT</code> status.</p> <p>Jobs must have timeout values less than 7 days or 10080 minutes. Otherwise, the jobs will throw an exception.</p> <p>When the value is left blank, the timeout is defaulted to 2,880 minutes for Glue version 4.0 and earlier, or 480 minutes for Glue version 5.0 and later.</p> <p>Any existing Glue jobs that had a timeout value greater than 7 days will be defaulted to 7 days. For instance if you have specified a timeout of 20 days for a batch job, it will be stopped on the 7th day.</p> <p>For streaming jobs, if you have set up a maintenance window, it will be restarted during the maintenance window after 7 days.</p>
            max_capacity: <p>For Glue version 1.0 or earlier jobs, using the standard worker type, the number of Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the <a href=\"https://aws.amazon.com/glue/pricing/\"> Glue pricing page</a>.</p> <p>For Glue version 2.0+ jobs, you cannot specify a <code>Maximum capacity</code>. Instead, you should specify a <code>Worker type</code> and the <code>Number of workers</code>.</p> <p>Do not set <code>MaxCapacity</code> if using <code>WorkerType</code> and <code>NumberOfWorkers</code>.</p> <p>The value that can be allocated for <code>MaxCapacity</code> depends on whether you are running a Python shell job, an Apache Spark ETL job, or an Apache Spark streaming ETL job:</p> <ul> <li> <p>When you specify a Python shell job (<code>JobCommand.Name</code>=\"pythonshell\"), you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.</p> </li> <li> <p>When you specify an Apache Spark ETL job (<code>JobCommand.Name</code>=\"glueetl\") or Apache Spark streaming ETL job (<code>JobCommand.Name</code>=\"gluestreaming\"), you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.</p> </li> </ul>
            security_configuration: <p>The name of the <code>SecurityConfiguration</code> structure to be used with this job.</p>
            tags: <p>The tags to use with this job. You may use tags to limit access to the job. For more information about tags in Glue, see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html\">Amazon Web Services Tags in Glue</a> in the developer guide.</p>
            notification_property: <p>Specifies configuration properties of a job notification.</p>
            glue_version: <p>In Spark jobs, <code>GlueVersion</code> determines the versions of Apache Spark and Python that Glue available in a job. The Python version indicates the version supported for jobs of type Spark. </p> <p>Ray jobs should set <code>GlueVersion</code> to <code>4.0</code> or greater. However, the versions of Ray, Python and additional libraries available in your Ray job are determined by the <code>Runtime</code> parameter of the Job command.</p> <p>For more information about the available Glue versions and corresponding Spark and Python versions, see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/add-job.html\">Glue version</a> in the developer guide.</p> <p>Jobs that are created without specifying a Glue version default to Glue 5.1.</p>
            number_of_workers: <p>The number of workers of a defined <code>workerType</code> that are allocated when a job runs.</p>
            worker_type: <p>The type of predefined worker that is allocated when a job runs. Accepts a value of G.1X, G.2X, G.4X, G.8X or G.025X for Spark jobs. Accepts the value Z.2X for Ray jobs.</p> <ul> <li> <p>For the <code>G.1X</code> worker type, each worker maps to 1 DPU (4 vCPUs, 16 GB of memory) with 94GB disk, and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs.</p> </li> <li> <p>For the <code>G.2X</code> worker type, each worker maps to 2 DPU (8 vCPUs, 32 GB of memory) with 138GB disk, and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs.</p> </li> <li> <p>For the <code>G.4X</code> worker type, each worker maps to 4 DPU (16 vCPUs, 64 GB of memory) with 256GB disk, and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for Glue version 3.0 or later Spark ETL jobs in the following Amazon Web Services Regions: US East (Ohio), US East (N. Virginia), US West (N. California), US West (Oregon), Asia Pacific (Mumbai), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Spain), Europe (Stockholm), and South America (São Paulo).</p> </li> <li> <p>For the <code>G.8X</code> worker type, each worker maps to 8 DPU (32 vCPUs, 128 GB of memory) with 512GB disk, and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for Glue version 3.0 or later Spark ETL jobs, in the same Amazon Web Services Regions as supported for the <code>G.4X</code> worker type.</p> </li> <li> <p>For the <code>G.025X</code> worker type, each worker maps to 0.25 DPU (2 vCPUs, 4 GB of memory) with 84GB disk, and provides 1 executor per worker. We recommend this worker type for low volume streaming jobs. This worker type is only available for Glue version 3.0 or later streaming jobs.</p> </li> <li> <p>For the <code>Z.2X</code> worker type, each worker maps to 2 M-DPU (8vCPUs, 64 GB of memory) with 128 GB disk, and provides up to 8 Ray workers based on the autoscaler.</p> </li> </ul>
            code_gen_configuration_nodes: <p>The representation of a directed acyclic graph on which both the Glue Studio visual component and Glue Studio code generation is based.</p>
            execution_class: <p>Indicates whether the job is run with a standard or flexible execution class. The standard execution-class is ideal for time-sensitive workloads that require fast job startup and dedicated resources.</p> <p>The flexible execution class is appropriate for time-insensitive jobs whose start and completion times may vary. </p> <p>Only jobs with Glue version 3.0 and above and command type <code>glueetl</code> will be allowed to set <code>ExecutionClass</code> to <code>FLEX</code>. The flexible execution class is available for Spark jobs.</p>
            source_control_details: <p>The details for a source control configuration for a job, allowing synchronization of job artifacts to or from a remote repository.</p>
            maintenance_window: <p>This field specifies a day of the week and hour for a maintenance window for streaming jobs. Glue periodically performs maintenance activities. During these maintenance windows, Glue will need to restart your streaming jobs.</p> <p>Glue will restart the job within 3 hours of the specified maintenance window. For instance, if you set up the maintenance window for Monday at 10:00AM GMT, your jobs will be restarted between 10:00AM GMT to 1:00PM GMT.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.create_job_request.CreateJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.create_job_response.CreateJobResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.create_job

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.create_job.async_create_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.create_job_request.CreateJobRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if job_mode is not None:
            input_["job_mode"] = job_mode
        if job_run_queuing_enabled is not None:
            input_["job_run_queuing_enabled"] = job_run_queuing_enabled
        if description is not None:
            input_["description"] = description
        if log_uri is not None:
            input_["log_uri"] = log_uri
        input_["role"] = role
        if execution_property is not None:
            input_["execution_property"] = execution_property
        input_["command"] = command
        if default_arguments is not None:
            input_["default_arguments"] = default_arguments
        if non_overridable_arguments is not None:
            input_["non_overridable_arguments"] = non_overridable_arguments
        if connections is not None:
            input_["connections"] = connections
        if max_retries is not None:
            input_["max_retries"] = max_retries
        if allocated_capacity is not None:
            input_["allocated_capacity"] = allocated_capacity
        if timeout is not None:
            input_["timeout"] = timeout
        if max_capacity is not None:
            input_["max_capacity"] = max_capacity
        if security_configuration is not None:
            input_["security_configuration"] = security_configuration
        if tags is not None:
            input_["tags"] = tags
        if notification_property is not None:
            input_["notification_property"] = notification_property
        if glue_version is not None:
            input_["glue_version"] = glue_version
        if number_of_workers is not None:
            input_["number_of_workers"] = number_of_workers
        if worker_type is not None:
            input_["worker_type"] = worker_type
        if code_gen_configuration_nodes is not None:
            input_["code_gen_configuration_nodes"] = code_gen_configuration_nodes
        if execution_class is not None:
            input_["execution_class"] = execution_class
        if source_control_details is not None:
            input_["source_control_details"] = source_control_details
        if maintenance_window is not None:
            input_["maintenance_window"] = maintenance_window

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_ml_transform(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        input_record_tables: "aws_sdk_glue.types.glue_tables.GlueTables",
        parameters: "aws_sdk_glue.types.transform_parameters.TransformParameters",
        role: "aws_sdk_glue.types.role_string.RoleString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        description: Optional[
            "aws_sdk_glue.types.description_string.DescriptionString"
        ] = None,
        glue_version: Optional[
            "aws_sdk_glue.types.glue_version_string.GlueVersionString"
        ] = None,
        max_capacity: Optional[
            "aws_sdk_glue.types.nullable_double.NullableDouble"
        ] = None,
        worker_type: Optional["aws_sdk_glue.types.worker_type.WorkerType"] = None,
        number_of_workers: Optional[
            "aws_sdk_glue.types.nullable_integer.NullableInteger"
        ] = None,
        timeout: Optional["aws_sdk_glue.types.timeout.Timeout"] = None,
        max_retries: Optional[
            "aws_sdk_glue.types.nullable_integer.NullableInteger"
        ] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
        transform_encryption: Optional[
            "aws_sdk_glue.types.transform_encryption.TransformEncryption"
        ] = None,
    ) -> "aws_sdk_glue.types.create_ml_transform_response.CreateMLTransformResponse":
        r"""<p>Creates an Glue machine learning transform. This operation creates the transform and all the necessary parameters to train it.</p> <p>Call this operation as the first step in the process of using a machine learning transform (such as the <code>FindMatches</code> transform) for deduplicating data. You can provide an optional <code>Description</code>, in addition to the parameters that you want to use for your algorithm.</p> <p>You must also specify certain parameters for the tasks that Glue runs on your behalf as part of learning from your data and creating a high-quality machine learning transform. These parameters include <code>Role</code>, and optionally, <code>AllocatedCapacity</code>, <code>Timeout</code>, and <code>MaxRetries</code>. For more information, see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-job.html\">Jobs</a>.</p>

        Args:
            name: <p>The unique name that you give the transform when you create it.</p>
            description: <p>A description of the machine learning transform that is being defined. The default is an empty string.</p>
            input_record_tables: <p>A list of Glue table definitions used by the transform.</p>
            parameters: <p>The algorithmic parameters that are specific to the transform type used. Conditionally dependent on the transform type.</p>
            role: <p>The name or Amazon Resource Name (ARN) of the IAM role with the required permissions. The required permissions include both Glue service role permissions to Glue resources, and Amazon S3 permissions required by the transform. </p> <ul> <li> <p>This role needs Glue service role permissions to allow access to resources in Glue. See <a href=\"https://docs.aws.amazon.com/glue/latest/dg/attach-policy-iam-user.html\">Attach a Policy to IAM Users That Access Glue</a>.</p> </li> <li> <p>This role needs permission to your Amazon Simple Storage Service (Amazon S3) sources, targets, temporary directory, scripts, and any libraries used by the task run for this transform.</p> </li> </ul>
            glue_version: <p>This value determines which version of Glue this machine learning transform is compatible with. Glue 1.0 is recommended for most customers. If the value is not set, the Glue compatibility defaults to Glue 0.9. For more information, see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/release-notes.html#release-notes-versions\">Glue Versions</a> in the developer guide.</p>
            max_capacity: <p>The number of Glue data processing units (DPUs) that are allocated to task runs for this transform. You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the <a href=\"https://aws.amazon.com/glue/pricing/\">Glue pricing page</a>. </p> <p> <code>MaxCapacity</code> is a mutually exclusive option with <code>NumberOfWorkers</code> and <code>WorkerType</code>.</p> <ul> <li> <p>If either <code>NumberOfWorkers</code> or <code>WorkerType</code> is set, then <code>MaxCapacity</code> cannot be set.</p> </li> <li> <p>If <code>MaxCapacity</code> is set then neither <code>NumberOfWorkers</code> or <code>WorkerType</code> can be set.</p> </li> <li> <p>If <code>WorkerType</code> is set, then <code>NumberOfWorkers</code> is required (and vice versa).</p> </li> <li> <p> <code>MaxCapacity</code> and <code>NumberOfWorkers</code> must both be at least 1.</p> </li> </ul> <p>When the <code>WorkerType</code> field is set to a value other than <code>Standard</code>, the <code>MaxCapacity</code> field is set automatically and becomes read-only.</p> <p>When the <code>WorkerType</code> field is set to a value other than <code>Standard</code>, the <code>MaxCapacity</code> field is set automatically and becomes read-only.</p>
            worker_type: <p>The type of predefined worker that is allocated when this task runs. Accepts a value of Standard, G.1X, or G.2X.</p> <ul> <li> <p>For the <code>Standard</code> worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.</p> </li> <li> <p>For the <code>G.1X</code> worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk, and 1 executor per worker.</p> </li> <li> <p>For the <code>G.2X</code> worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB disk, and 1 executor per worker.</p> </li> </ul> <p> <code>MaxCapacity</code> is a mutually exclusive option with <code>NumberOfWorkers</code> and <code>WorkerType</code>.</p> <ul> <li> <p>If either <code>NumberOfWorkers</code> or <code>WorkerType</code> is set, then <code>MaxCapacity</code> cannot be set.</p> </li> <li> <p>If <code>MaxCapacity</code> is set then neither <code>NumberOfWorkers</code> or <code>WorkerType</code> can be set.</p> </li> <li> <p>If <code>WorkerType</code> is set, then <code>NumberOfWorkers</code> is required (and vice versa).</p> </li> <li> <p> <code>MaxCapacity</code> and <code>NumberOfWorkers</code> must both be at least 1.</p> </li> </ul>
            number_of_workers: <p>The number of workers of a defined <code>workerType</code> that are allocated when this task runs.</p> <p>If <code>WorkerType</code> is set, then <code>NumberOfWorkers</code> is required (and vice versa).</p>
            timeout: <p>The timeout of the task run for this transform in minutes. This is the maximum time that a task run for this transform can consume resources before it is terminated and enters <code>TIMEOUT</code> status. The default is 2,880 minutes (48 hours).</p>
            max_retries: <p>The maximum number of times to retry a task for this transform after a task run fails.</p>
            tags: <p>The tags to use with this machine learning transform. You may use tags to limit access to the machine learning transform. For more information about tags in Glue, see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html\">Amazon Web Services Tags in Glue</a> in the developer guide.</p>
            transform_encryption: <p>The encryption-at-rest settings of the transform that apply to accessing user data. Machine learning transforms can access user data encrypted in Amazon S3 using KMS.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.create_ml_transform_request.CreateMLTransformRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.create_ml_transform_response.CreateMLTransformResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.create_ml_transform

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.create_ml_transform.async_create_ml_transform(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.create_ml_transform_request.CreateMLTransformRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["input_record_tables"] = input_record_tables
        input_["parameters"] = parameters
        input_["role"] = role
        if glue_version is not None:
            input_["glue_version"] = glue_version
        if max_capacity is not None:
            input_["max_capacity"] = max_capacity
        if worker_type is not None:
            input_["worker_type"] = worker_type
        if number_of_workers is not None:
            input_["number_of_workers"] = number_of_workers
        if timeout is not None:
            input_["timeout"] = timeout
        if max_retries is not None:
            input_["max_retries"] = max_retries
        if tags is not None:
            input_["tags"] = tags
        if transform_encryption is not None:
            input_["transform_encryption"] = transform_encryption

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_partition(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        partition_input: "aws_sdk_glue.types.partition_input.PartitionInput",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.create_partition_response.CreatePartitionResponse":
        """<p>Creates a new partition.</p>

        Args:
            catalog_id: <p>The Amazon Web Services account ID of the catalog in which the partition is to be created.</p>
            database_name: <p>The name of the metadata database in which the partition is to be created.</p>
            table_name: <p>The name of the metadata table in which the partition is to be created.</p>
            partition_input: <p>A <code>PartitionInput</code> structure defining the partition to be created.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.create_partition_request.CreatePartitionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.create_partition_response.CreatePartitionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.create_partition

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.create_partition.async_create_partition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.create_partition_request.CreatePartitionRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        input_["partition_input"] = partition_input

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_partition_index(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        partition_index: "aws_sdk_glue.types.partition_index.PartitionIndex",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.create_partition_index_response.CreatePartitionIndexResponse":
        """<p>Creates a specified partition index in an existing table.</p>

        Args:
            catalog_id: <p>The catalog ID where the table resides.</p>
            database_name: <p>Specifies the name of a database in which you want to create a partition index.</p>
            table_name: <p>Specifies the name of a table in which you want to create a partition index.</p>
            partition_index: <p>Specifies a <code>PartitionIndex</code> structure to create a partition index in an existing table.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.create_partition_index_request.CreatePartitionIndexRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.create_partition_index_response.CreatePartitionIndexResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.create_partition_index

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.create_partition_index.async_create_partition_index(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.create_partition_index_request.CreatePartitionIndexRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        input_["partition_index"] = partition_index

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_registry(
        self,
        registry_name: "aws_sdk_glue.types.schema_registry_name_string.SchemaRegistryNameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        description: Optional[
            "aws_sdk_glue.types.description_string.DescriptionString"
        ] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_glue.types.create_registry_response.CreateRegistryResponse":
        """<p>Creates a new registry which may be used to hold a collection of schemas.</p>

        Args:
            registry_name: <p>Name of the registry to be created of max length of 255, and may only contain letters, numbers, hyphen, underscore, dollar sign, or hash mark. No whitespace.</p>
            description: <p>A description of the registry. If description is not provided, there will not be any default value for this.</p>
            tags: <p>Amazon Web Services tags that contain a key value pair and may be searched by console, command line, or API.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.create_registry_input.CreateRegistryInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.create_registry_response.CreateRegistryResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.create_registry

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.create_registry.async_create_registry(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.create_registry_input.CreateRegistryInput = {}  # type: ignore[typeddict-item]
        input_["registry_name"] = registry_name
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_schema(
        self,
        schema_name: "aws_sdk_glue.types.schema_registry_name_string.SchemaRegistryNameString",
        data_format: "aws_sdk_glue.types.data_format.DataFormat",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        registry_id: Optional["aws_sdk_glue.types.registry_id.RegistryId"] = None,
        compatibility: Optional[
            "aws_sdk_glue.types.compatibility.Compatibility"
        ] = None,
        description: Optional[
            "aws_sdk_glue.types.description_string.DescriptionString"
        ] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
        schema_definition: Optional[
            "aws_sdk_glue.types.schema_definition_string.SchemaDefinitionString"
        ] = None,
    ) -> "aws_sdk_glue.types.create_schema_response.CreateSchemaResponse":
        r"""<p>Creates a new schema set and registers the schema definition. Returns an error if the schema set already exists without actually registering the version.</p> <p>When the schema set is created, a version checkpoint will be set to the first version. Compatibility mode \"DISABLED\" restricts any additional schema versions from being added after the first schema version. For all other compatibility modes, validation of compatibility settings will be applied only from the second version onwards when the <code>RegisterSchemaVersion</code> API is used.</p> <p>When this API is called without a <code>RegistryId</code>, this will create an entry for a \"default-registry\" in the registry database tables, if it is not already present.</p>

        Args:
            registry_id: <p> This is a wrapper shape to contain the registry identity fields. If this is not provided, the default registry will be used. The ARN format for the same will be: <code>arn:aws:glue:us-east-2:<customer id>:registry/default-registry:random-5-letter-id</code>.</p>
            schema_name: <p>Name of the schema to be created of max length of 255, and may only contain letters, numbers, hyphen, underscore, dollar sign, or hash mark. No whitespace.</p>
            data_format: <p>The data format of the schema definition. Currently <code>AVRO</code>, <code>JSON</code> and <code>PROTOBUF</code> are supported.</p>
            compatibility: <p>The compatibility mode of the schema. The possible values are:</p> <ul> <li> <p> <i>NONE</i>: No compatibility mode applies. You can use this choice in development scenarios or if you do not know the compatibility mode that you want to apply to schemas. Any new version added will be accepted without undergoing a compatibility check.</p> </li> <li> <p> <i>DISABLED</i>: This compatibility choice prevents versioning for a particular schema. You can use this choice to prevent future versioning of a schema.</p> </li> <li> <p> <i>BACKWARD</i>: This compatibility choice is recommended as it allows data receivers to read both the current and one previous schema version. This means that for instance, a new schema version cannot drop data fields or change the type of these fields, so they can't be read by readers using the previous version.</p> </li> <li> <p> <i>BACKWARD_ALL</i>: This compatibility choice allows data receivers to read both the current and all previous schema versions. You can use this choice when you need to delete fields or add optional fields, and check compatibility against all previous schema versions. </p> </li> <li> <p> <i>FORWARD</i>: This compatibility choice allows data receivers to read both the current and one next schema version, but not necessarily later versions. You can use this choice when you need to add fields or delete optional fields, but only check compatibility against the last schema version.</p> </li> <li> <p> <i>FORWARD_ALL</i>: This compatibility choice allows data receivers to read written by producers of any new registered schema. You can use this choice when you need to add fields or delete optional fields, and check compatibility against all previous schema versions.</p> </li> <li> <p> <i>FULL</i>: This compatibility choice allows data receivers to read data written by producers using the previous or next version of the schema, but not necessarily earlier or later versions. You can use this choice when you need to add or remove optional fields, but only check compatibility against the last schema version.</p> </li> <li> <p> <i>FULL_ALL</i>: This compatibility choice allows data receivers to read data written by producers using all previous schema versions. You can use this choice when you need to add or remove optional fields, and check compatibility against all previous schema versions.</p> </li> </ul>
            description: <p>An optional description of the schema. If description is not provided, there will not be any automatic default value for this.</p>
            tags: <p>Amazon Web Services tags that contain a key value pair and may be searched by console, command line, or API. If specified, follows the Amazon Web Services tags-on-create pattern.</p>
            schema_definition: <p>The schema definition using the <code>DataFormat</code> setting for <code>SchemaName</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.create_schema_input.CreateSchemaInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.create_schema_response.CreateSchemaResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.create_schema

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.create_schema.async_create_schema(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.create_schema_input.CreateSchemaInput = {}  # type: ignore[typeddict-item]
        if registry_id is not None:
            input_["registry_id"] = registry_id
        input_["schema_name"] = schema_name
        input_["data_format"] = data_format
        if compatibility is not None:
            input_["compatibility"] = compatibility
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if schema_definition is not None:
            input_["schema_definition"] = schema_definition

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_script(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        dag_nodes: Optional["aws_sdk_glue.types.dag_nodes.DagNodes"] = None,
        dag_edges: Optional["aws_sdk_glue.types.dag_edges.DagEdges"] = None,
        language: Optional["aws_sdk_glue.types.language.Language"] = None,
    ) -> "aws_sdk_glue.types.create_script_response.CreateScriptResponse":
        """<p>Transforms a directed acyclic graph (DAG) into code.</p>

        Args:
            dag_nodes: <p>A list of the nodes in the DAG.</p>
            dag_edges: <p>A list of the edges in the DAG.</p>
            language: <p>The programming language of the resulting code from the DAG.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.create_script_request.CreateScriptRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.create_script_response.CreateScriptResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.create_script

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.create_script.async_create_script(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.create_script_request.CreateScriptRequest = {}  # type: ignore[typeddict-item]
        if dag_nodes is not None:
            input_["dag_nodes"] = dag_nodes
        if dag_edges is not None:
            input_["dag_edges"] = dag_edges
        if language is not None:
            input_["language"] = language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_security_configuration(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        encryption_configuration: "aws_sdk_glue.types.encryption_configuration.EncryptionConfiguration",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.create_security_configuration_response.CreateSecurityConfigurationResponse":
        r"""<p>Creates a new security configuration. A security configuration is a set of security properties that can be used by Glue. You can use a security configuration to encrypt data at rest. For information about using security configurations in Glue, see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/encryption-security-configuration.html\">Encrypting Data Written by Crawlers, Jobs, and Development Endpoints</a>.</p>

        Args:
            name: <p>The name for the new security configuration.</p>
            encryption_configuration: <p>The encryption configuration for the new security configuration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.create_security_configuration_request.CreateSecurityConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.create_security_configuration_response.CreateSecurityConfigurationResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.create_security_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.create_security_configuration.async_create_security_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.create_security_configuration_request.CreateSecurityConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["encryption_configuration"] = encryption_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_session(
        self,
        id: "aws_sdk_glue.types.name_string.NameString",
        role: "aws_sdk_glue.types.orchestration_role_arn.OrchestrationRoleArn",
        command: "aws_sdk_glue.types.session_command.SessionCommand",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        description: Optional[
            "aws_sdk_glue.types.description_string.DescriptionString"
        ] = None,
        timeout: Optional["aws_sdk_glue.types.timeout.Timeout"] = None,
        idle_timeout: Optional["aws_sdk_glue.types.timeout.Timeout"] = None,
        default_arguments: Optional[
            "aws_sdk_glue.types.orchestration_arguments_map.OrchestrationArgumentsMap"
        ] = None,
        connections: Optional[
            "aws_sdk_glue.types.connections_list.ConnectionsList"
        ] = None,
        max_capacity: Optional[
            "aws_sdk_glue.types.nullable_double.NullableDouble"
        ] = None,
        number_of_workers: Optional[
            "aws_sdk_glue.types.nullable_integer.NullableInteger"
        ] = None,
        worker_type: Optional["aws_sdk_glue.types.worker_type.WorkerType"] = None,
        security_configuration: Optional[
            "aws_sdk_glue.types.name_string.NameString"
        ] = None,
        glue_version: Optional[
            "aws_sdk_glue.types.glue_version_string.GlueVersionString"
        ] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
        request_origin: Optional[
            "aws_sdk_glue.types.orchestration_name_string.OrchestrationNameString"
        ] = None,
        session_type: Optional["aws_sdk_glue.types.session_type.SessionType"] = None,
    ) -> "aws_sdk_glue.types.create_session_response.CreateSessionResponse":
        """<p>Creates a new session.</p>

        Args:
            id: <p>The ID of the session request. </p>
            description: <p>The description of the session. </p>
            role: <p>The IAM Role ARN </p>
            command: <p>The <code>SessionCommand</code> that runs the job. </p>
            timeout: <p> The number of minutes before session times out. Default for Spark ETL jobs is 48 hours (2880 minutes). Consult the documentation for other job types. </p>
            idle_timeout: <p> The number of minutes when idle before session times out. Default for Spark ETL jobs is value of Timeout. Consult the documentation for other job types. </p>
            default_arguments: <p>A map array of key-value pairs. Max is 75 pairs. </p>
            connections: <p>The number of connections to use for the session. </p>
            max_capacity: <p>The number of Glue data processing units (DPUs) that can be allocated when the job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB memory. </p>
            number_of_workers: <p>The number of workers of a defined <code>WorkerType</code> to use for the session. </p>
            worker_type: <p>The type of predefined worker that is allocated when a job runs. Accepts a value of G.1X, G.2X, G.4X, or G.8X for Spark jobs. Accepts the value Z.2X for Ray notebooks.</p> <ul> <li> <p>For the <code>G.1X</code> worker type, each worker maps to 1 DPU (4 vCPUs, 16 GB of memory) with 94GB disk, and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs.</p> </li> <li> <p>For the <code>G.2X</code> worker type, each worker maps to 2 DPU (8 vCPUs, 32 GB of memory) with 138GB disk, and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs.</p> </li> <li> <p>For the <code>G.4X</code> worker type, each worker maps to 4 DPU (16 vCPUs, 64 GB of memory) with 256GB disk, and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for Glue version 3.0 or later Spark ETL jobs in the following Amazon Web Services Regions: US East (Ohio), US East (N. Virginia), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central), Europe (Frankfurt), Europe (Ireland), and Europe (Stockholm).</p> </li> <li> <p>For the <code>G.8X</code> worker type, each worker maps to 8 DPU (32 vCPUs, 128 GB of memory) with 512GB disk, and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for Glue version 3.0 or later Spark ETL jobs, in the same Amazon Web Services Regions as supported for the <code>G.4X</code> worker type.</p> </li> <li> <p>For the <code>Z.2X</code> worker type, each worker maps to 2 M-DPU (8vCPUs, 64 GB of memory) with 128 GB disk, and provides up to 8 Ray workers based on the autoscaler.</p> </li> </ul>
            security_configuration: <p>The name of the SecurityConfiguration structure to be used with the session </p>
            glue_version: <p>The Glue version determines the versions of Apache Spark and Python that Glue supports. The GlueVersion must be greater than 2.0. </p>
            tags: <p>The map of key value pairs (tags) belonging to the session.</p>
            request_origin: <p>The origin of the request. </p>
            session_type: <p>The type of session to create.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.create_session_request.CreateSessionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.create_session_response.CreateSessionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.create_session

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.create_session.async_create_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.create_session_request.CreateSessionRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if description is not None:
            input_["description"] = description
        input_["role"] = role
        input_["command"] = command
        if timeout is not None:
            input_["timeout"] = timeout
        if idle_timeout is not None:
            input_["idle_timeout"] = idle_timeout
        if default_arguments is not None:
            input_["default_arguments"] = default_arguments
        if connections is not None:
            input_["connections"] = connections
        if max_capacity is not None:
            input_["max_capacity"] = max_capacity
        if number_of_workers is not None:
            input_["number_of_workers"] = number_of_workers
        if worker_type is not None:
            input_["worker_type"] = worker_type
        if security_configuration is not None:
            input_["security_configuration"] = security_configuration
        if glue_version is not None:
            input_["glue_version"] = glue_version
        if tags is not None:
            input_["tags"] = tags
        if request_origin is not None:
            input_["request_origin"] = request_origin
        if session_type is not None:
            input_["session_type"] = session_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_table(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
        name: Optional["aws_sdk_glue.types.name_string.NameString"] = None,
        table_input: Optional["aws_sdk_glue.types.table_input.TableInput"] = None,
        partition_indexes: Optional[
            "aws_sdk_glue.types.partition_index_list.PartitionIndexList"
        ] = None,
        transaction_id: Optional[
            "aws_sdk_glue.types.transaction_id_string.TransactionIdString"
        ] = None,
        open_table_format_input: Optional[
            "aws_sdk_glue.types.open_table_format_input.OpenTableFormatInput"
        ] = None,
    ) -> "aws_sdk_glue.types.create_table_response.CreateTableResponse":
        """<p>Creates a new table definition in the Data Catalog.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog in which to create the <code>Table</code>. If none is supplied, the Amazon Web Services account ID is used by default.</p>
            database_name: <p>The catalog database in which to create the new table. For Hive compatibility, this name is entirely lowercase.</p>
            name: <p>The unique identifier for the table within the specified database that will be created in the Glue Data Catalog.</p>
            table_input: <p>The <code>TableInput</code> object that defines the metadata table to create in the catalog.</p>
            partition_indexes: <p>A list of partition indexes, <code>PartitionIndex</code> structures, to create in the table.</p>
            transaction_id: <p>The ID of the transaction.</p>
            open_table_format_input: <p>Specifies an <code>OpenTableFormatInput</code> structure when creating an open format table.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.create_table_request.CreateTableRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.create_table_response.CreateTableResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.create_table

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.create_table.async_create_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.create_table_request.CreateTableRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        if name is not None:
            input_["name"] = name
        if table_input is not None:
            input_["table_input"] = table_input
        if partition_indexes is not None:
            input_["partition_indexes"] = partition_indexes
        if transaction_id is not None:
            input_["transaction_id"] = transaction_id
        if open_table_format_input is not None:
            input_["open_table_format_input"] = open_table_format_input

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_table_optimizer(
        self,
        catalog_id: "aws_sdk_glue.types.catalog_id_string.CatalogIdString",
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        type: "aws_sdk_glue.types.table_optimizer_type.TableOptimizerType",
        table_optimizer_configuration: "aws_sdk_glue.types.table_optimizer_configuration.TableOptimizerConfiguration",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.create_table_optimizer_response.CreateTableOptimizerResponse":
        """<p>Creates a new table optimizer for a specific function. </p>

        Args:
            catalog_id: <p>The Catalog ID of the table.</p>
            database_name: <p>The name of the database in the catalog in which the table resides.</p>
            table_name: <p>The name of the table.</p>
            type: <p>The type of table optimizer.</p>
            table_optimizer_configuration: <p>A <code>TableOptimizerConfiguration</code> object representing the configuration of a table optimizer.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.create_table_optimizer_request.CreateTableOptimizerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.create_table_optimizer_response.CreateTableOptimizerResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.create_table_optimizer

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.create_table_optimizer.async_create_table_optimizer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.create_table_optimizer_request.CreateTableOptimizerRequest = {}  # type: ignore[typeddict-item]
        input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        input_["type"] = type
        input_["table_optimizer_configuration"] = table_optimizer_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_trigger(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        type: "aws_sdk_glue.types.trigger_type.TriggerType",
        actions: "aws_sdk_glue.types.action_list.ActionList",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        workflow_name: Optional["aws_sdk_glue.types.name_string.NameString"] = None,
        schedule: Optional["aws_sdk_glue.types.generic_string.GenericString"] = None,
        predicate: Optional["aws_sdk_glue.types.predicate.Predicate"] = None,
        description: Optional[
            "aws_sdk_glue.types.description_string.DescriptionString"
        ] = None,
        start_on_creation: Optional[
            "aws_sdk_glue.types.boolean_value.BooleanValue"
        ] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
        event_batching_condition: Optional[
            "aws_sdk_glue.types.event_batching_condition.EventBatchingCondition"
        ] = None,
    ) -> "aws_sdk_glue.types.create_trigger_response.CreateTriggerResponse":
        r"""<p>Creates a new trigger.</p> <p>Job arguments may be logged. Do not pass plaintext secrets as arguments. Retrieve secrets from a Glue Connection, Amazon Web Services Secrets Manager or other secret management mechanism if you intend to keep them within the Job.</p>

        Args:
            name: <p>The name of the trigger.</p>
            workflow_name: <p>The name of the workflow associated with the trigger.</p>
            type: <p>The type of the new trigger.</p>
            schedule: <p>A <code>cron</code> expression used to specify the schedule (see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html\">Time-Based Schedules for Jobs and Crawlers</a>. For example, to run something every day at 12:15 UTC, you would specify: <code>cron(15 12 * * ? *)</code>.</p> <p>This field is required when the trigger type is SCHEDULED.</p>
            predicate: <p>A predicate to specify when the new trigger should fire.</p> <p>This field is required when the trigger type is <code>CONDITIONAL</code>.</p>
            actions: <p>The actions initiated by this trigger when it fires.</p>
            description: <p>A description of the new trigger.</p>
            start_on_creation: <p>Set to <code>true</code> to start <code>SCHEDULED</code> and <code>CONDITIONAL</code> triggers when created. True is not supported for <code>ON_DEMAND</code> triggers.</p>
            tags: <p>The tags to use with this trigger. You may use tags to limit access to the trigger. For more information about tags in Glue, see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html\">Amazon Web Services Tags in Glue</a> in the developer guide. </p>
            event_batching_condition: <p>Batch condition that must be met (specified number of events received or batch time window expired) before EventBridge event trigger fires.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.create_trigger_request.CreateTriggerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.create_trigger_response.CreateTriggerResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.create_trigger

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.create_trigger.async_create_trigger(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.create_trigger_request.CreateTriggerRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if workflow_name is not None:
            input_["workflow_name"] = workflow_name
        input_["type"] = type
        if schedule is not None:
            input_["schedule"] = schedule
        if predicate is not None:
            input_["predicate"] = predicate
        input_["actions"] = actions
        if description is not None:
            input_["description"] = description
        if start_on_creation is not None:
            input_["start_on_creation"] = start_on_creation
        if tags is not None:
            input_["tags"] = tags
        if event_batching_condition is not None:
            input_["event_batching_condition"] = event_batching_condition

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_usage_profile(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        configuration: "aws_sdk_glue.types.profile_configuration.ProfileConfiguration",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        description: Optional[
            "aws_sdk_glue.types.description_string.DescriptionString"
        ] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_glue.types.create_usage_profile_response.CreateUsageProfileResponse":
        """<p>Creates an Glue usage profile.</p>

        Args:
            name: <p>The name of the usage profile.</p>
            description: <p>A description of the usage profile.</p>
            configuration: <p>A <code>ProfileConfiguration</code> object specifying the job and session values for the profile.</p>
            tags: <p>A list of tags applied to the usage profile.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.create_usage_profile_request.CreateUsageProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.create_usage_profile_response.CreateUsageProfileResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.create_usage_profile

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.create_usage_profile.async_create_usage_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.create_usage_profile_request.CreateUsageProfileRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["configuration"] = configuration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_user_defined_function(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        function_input: "aws_sdk_glue.types.user_defined_function_input.UserDefinedFunctionInput",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.create_user_defined_function_response.CreateUserDefinedFunctionResponse":
        """<p>Creates a new function definition in the Data Catalog.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog in which to create the function. If none is provided, the Amazon Web Services account ID is used by default.</p>
            database_name: <p>The name of the catalog database in which to create the function.</p>
            function_input: <p>A <code>FunctionInput</code> object that defines the function to create in the Data Catalog.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.create_user_defined_function_request.CreateUserDefinedFunctionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.create_user_defined_function_response.CreateUserDefinedFunctionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.create_user_defined_function

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.create_user_defined_function.async_create_user_defined_function(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.create_user_defined_function_request.CreateUserDefinedFunctionRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["function_input"] = function_input

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_workflow(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        description: Optional[
            "aws_sdk_glue.types.workflow_description_string.WorkflowDescriptionString"
        ] = None,
        default_run_properties: Optional[
            "aws_sdk_glue.types.workflow_run_properties.WorkflowRunProperties"
        ] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
        max_concurrent_runs: Optional[
            "aws_sdk_glue.types.nullable_integer.NullableInteger"
        ] = None,
    ) -> "aws_sdk_glue.types.create_workflow_response.CreateWorkflowResponse":
        """<p>Creates a new workflow.</p>

        Args:
            name: <p>The name to be assigned to the workflow. It should be unique within your account.</p>
            description: <p>A description of the workflow.</p>
            default_run_properties: <p>A collection of properties to be used as part of each execution of the workflow.</p> <p>Run properties may be logged. Do not pass plaintext secrets as properties. Retrieve secrets from a Glue Connection, Amazon Web Services Secrets Manager or other secret management mechanism if you intend to use them within the workflow run.</p>
            tags: <p>The tags to be used with this workflow.</p>
            max_concurrent_runs: <p>You can use this parameter to prevent unwanted multiple updates to data, to control costs, or in some cases, to prevent exceeding the maximum number of concurrent runs of any of the component jobs. If you leave this parameter blank, there is no limit to the number of concurrent workflow runs.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.create_workflow_request.CreateWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.create_workflow_response.CreateWorkflowResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.create_workflow

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.create_workflow.async_create_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.create_workflow_request.CreateWorkflowRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if default_run_properties is not None:
            input_["default_run_properties"] = default_run_properties
        if tags is not None:
            input_["tags"] = tags
        if max_concurrent_runs is not None:
            input_["max_concurrent_runs"] = max_concurrent_runs

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_blueprint(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.delete_blueprint_response.DeleteBlueprintResponse":
        """<p>Deletes an existing blueprint.</p>

        Args:
            name: <p>The name of the blueprint to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_blueprint_request.DeleteBlueprintRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_blueprint_response.DeleteBlueprintResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_blueprint

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_blueprint.async_delete_blueprint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_blueprint_request.DeleteBlueprintRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_catalog(
        self,
        catalog_id: "aws_sdk_glue.types.catalog_id_string.CatalogIdString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.delete_catalog_response.DeleteCatalogResponse":
        r"""<p>Removes the specified catalog from the Glue Data Catalog.</p> <p>After completing this operation, you no longer have access to the databases, tables (and all table versions and partitions that might belong to the tables) and the user-defined functions in the deleted catalog. Glue deletes these \"orphaned\" resources asynchronously in a timely manner, at the discretion of the service.</p> <p>To ensure the immediate deletion of all related resources before calling the <code>DeleteCatalog</code> operation, use <code>DeleteTableVersion</code> (or <code>BatchDeleteTableVersion</code>), <code>DeletePartition</code> (or <code>BatchDeletePartition</code>), <code>DeleteTable</code> (or <code>BatchDeleteTable</code>), <code>DeleteUserDefinedFunction</code> and <code>DeleteDatabase</code> to delete any resources that belong to the catalog.</p>

        Args:
            catalog_id: <p>The ID of the catalog.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_catalog_request.DeleteCatalogRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_catalog_response.DeleteCatalogResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_catalog

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_catalog.async_delete_catalog(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_catalog_request.DeleteCatalogRequest = {}  # type: ignore[typeddict-item]
        input_["catalog_id"] = catalog_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_classifier(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.delete_classifier_response.DeleteClassifierResponse":
        """<p>Removes a classifier from the Data Catalog.</p>

        Args:
            name: <p>Name of the classifier to remove.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_classifier_request.DeleteClassifierRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_classifier_response.DeleteClassifierResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_classifier

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_classifier.async_delete_classifier(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_classifier_request.DeleteClassifierRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_column_statistics_for_partition(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        partition_values: "aws_sdk_glue.types.value_string_list.ValueStringList",
        column_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.delete_column_statistics_for_partition_response.DeleteColumnStatisticsForPartitionResponse":
        """<p>Delete the partition column statistics of a column.</p> <p>The Identity and Access Management (IAM) permission required for this operation is <code>DeletePartition</code>.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog where the partitions in question reside. If none is supplied, the Amazon Web Services account ID is used by default.</p>
            database_name: <p>The name of the catalog database where the partitions reside.</p>
            table_name: <p>The name of the partitions' table.</p>
            partition_values: <p>A list of partition values identifying the partition.</p>
            column_name: <p>Name of the column.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_column_statistics_for_partition_request.DeleteColumnStatisticsForPartitionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_column_statistics_for_partition_response.DeleteColumnStatisticsForPartitionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_column_statistics_for_partition

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_column_statistics_for_partition.async_delete_column_statistics_for_partition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_column_statistics_for_partition_request.DeleteColumnStatisticsForPartitionRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        input_["partition_values"] = partition_values
        input_["column_name"] = column_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_column_statistics_for_table(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        column_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.delete_column_statistics_for_table_response.DeleteColumnStatisticsForTableResponse":
        """<p>Retrieves table statistics of columns.</p> <p>The Identity and Access Management (IAM) permission required for this operation is <code>DeleteTable</code>.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog where the partitions in question reside. If none is supplied, the Amazon Web Services account ID is used by default.</p>
            database_name: <p>The name of the catalog database where the partitions reside.</p>
            table_name: <p>The name of the partitions' table.</p>
            column_name: <p>The name of the column.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_column_statistics_for_table_request.DeleteColumnStatisticsForTableRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_column_statistics_for_table_response.DeleteColumnStatisticsForTableResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_column_statistics_for_table

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_column_statistics_for_table.async_delete_column_statistics_for_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_column_statistics_for_table_request.DeleteColumnStatisticsForTableRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        input_["column_name"] = column_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_column_statistics_task_settings(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.delete_column_statistics_task_settings_response.DeleteColumnStatisticsTaskSettingsResponse":
        """<p>Deletes settings for a column statistics task.</p>

        Args:
            database_name: <p>The name of the database where the table resides.</p>
            table_name: <p>The name of the table for which to delete column statistics.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_column_statistics_task_settings_request.DeleteColumnStatisticsTaskSettingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_column_statistics_task_settings_response.DeleteColumnStatisticsTaskSettingsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_column_statistics_task_settings

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_column_statistics_task_settings.async_delete_column_statistics_task_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_column_statistics_task_settings_request.DeleteColumnStatisticsTaskSettingsRequest = {}  # type: ignore[typeddict-item]
        input_["database_name"] = database_name
        input_["table_name"] = table_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_connection(
        self,
        connection_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.delete_connection_response.DeleteConnectionResponse":
        """<p>Deletes a connection from the Data Catalog.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog in which the connection resides. If none is provided, the Amazon Web Services account ID is used by default.</p>
            connection_name: <p>The name of the connection to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_connection_request.DeleteConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_connection_response.DeleteConnectionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_connection

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_connection.async_delete_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_connection_request.DeleteConnectionRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["connection_name"] = connection_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_connection_type(
        self,
        connection_type: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.delete_connection_type_response.DeleteConnectionTypeResponse":
        """<p>Deletes a custom connection type in Glue.</p> <p>The connection type must exist and be registered before it can be deleted. This operation supports cleanup of connection type resources and helps maintain proper lifecycle management of custom connection types.</p>

        Args:
            connection_type: <p>The name of the connection type to delete. Must reference an existing registered connection type.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_connection_type_request.DeleteConnectionTypeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_connection_type_response.DeleteConnectionTypeResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_connection_type

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_connection_type.async_delete_connection_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_connection_type_request.DeleteConnectionTypeRequest = {}  # type: ignore[typeddict-item]
        input_["connection_type"] = connection_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_crawler(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.delete_crawler_response.DeleteCrawlerResponse":
        """<p>Removes a specified crawler from the Glue Data Catalog, unless the crawler state is <code>RUNNING</code>.</p>

        Args:
            name: <p>The name of the crawler to remove.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_crawler_request.DeleteCrawlerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_crawler_response.DeleteCrawlerResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_crawler

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_crawler.async_delete_crawler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_crawler_request.DeleteCrawlerRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_custom_entity_type(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.delete_custom_entity_type_response.DeleteCustomEntityTypeResponse":
        """<p>Deletes a custom pattern by specifying its name.</p>

        Args:
            name: <p>The name of the custom pattern that you want to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_custom_entity_type_request.DeleteCustomEntityTypeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_custom_entity_type_response.DeleteCustomEntityTypeResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_custom_entity_type

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_custom_entity_type.async_delete_custom_entity_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_custom_entity_type_request.DeleteCustomEntityTypeRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_database(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.delete_database_response.DeleteDatabaseResponse":
        r"""<p>Removes a specified database from a Data Catalog.</p> <note> <p>After completing this operation, you no longer have access to the tables (and all table versions and partitions that might belong to the tables) and the user-defined functions in the deleted database. Glue deletes these \"orphaned\" resources asynchronously in a timely manner, at the discretion of the service.</p> <p>To ensure the immediate deletion of all related resources, before calling <code>DeleteDatabase</code>, use <code>DeleteTableVersion</code> or <code>BatchDeleteTableVersion</code>, <code>DeletePartition</code> or <code>BatchDeletePartition</code>, <code>DeleteUserDefinedFunction</code>, and <code>DeleteTable</code> or <code>BatchDeleteTable</code>, to delete any resources that belong to the database.</p> </note>

        Args:
            catalog_id: <p>The ID of the Data Catalog in which the database resides. If none is provided, the Amazon Web Services account ID is used by default.</p>
            name: <p>The name of the database to delete. For Hive compatibility, this must be all lowercase.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_database_request.DeleteDatabaseRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_database_response.DeleteDatabaseResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_database

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_database.async_delete_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_database_request.DeleteDatabaseRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_data_quality_ruleset(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.delete_data_quality_ruleset_response.DeleteDataQualityRulesetResponse":
        """<p>Deletes a data quality ruleset.</p>

        Args:
            name: <p>A name for the data quality ruleset.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_data_quality_ruleset_request.DeleteDataQualityRulesetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_data_quality_ruleset_response.DeleteDataQualityRulesetResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_data_quality_ruleset

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_data_quality_ruleset.async_delete_data_quality_ruleset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_data_quality_ruleset_request.DeleteDataQualityRulesetRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_dev_endpoint(
        self,
        endpoint_name: "aws_sdk_glue.types.generic_string.GenericString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.delete_dev_endpoint_response.DeleteDevEndpointResponse":
        """<p>Deletes a specified development endpoint.</p>

        Args:
            endpoint_name: <p>The name of the <code>DevEndpoint</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_dev_endpoint_request.DeleteDevEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_dev_endpoint_response.DeleteDevEndpointResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_dev_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_dev_endpoint.async_delete_dev_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_dev_endpoint_request.DeleteDevEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["endpoint_name"] = endpoint_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_glue_identity_center_configuration(
        self, *, config_overrides: Optional[AsyncGlueClientConfig] = None
    ) -> "aws_sdk_glue.types.delete_glue_identity_center_configuration_response.DeleteGlueIdentityCenterConfigurationResponse":
        """<p>Deletes the existing Glue Identity Center configuration, removing the integration between Glue and Amazon Web Services IAM Identity Center.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_glue_identity_center_configuration_request.DeleteGlueIdentityCenterConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_glue_identity_center_configuration_response.DeleteGlueIdentityCenterConfigurationResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_glue_identity_center_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_glue_identity_center_configuration.async_delete_glue_identity_center_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_glue_identity_center_configuration_request.DeleteGlueIdentityCenterConfigurationRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_integration(
        self,
        integration_identifier: "aws_sdk_glue.types.string128.String128",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.delete_integration_response.DeleteIntegrationResponse":
        """<p>Deletes the specified Zero-ETL integration.</p>

        Args:
            integration_identifier: <p>The Amazon Resource Name (ARN) for the integration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_integration_request.DeleteIntegrationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_integration_response.DeleteIntegrationResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_integration

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_integration.async_delete_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_integration_request.DeleteIntegrationRequest = {}  # type: ignore[typeddict-item]
        input_["integration_identifier"] = integration_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_integration_resource_property(
        self,
        resource_arn: "aws_sdk_glue.types.string512.String512",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.delete_integration_resource_property_response.DeleteIntegrationResourcePropertyResponse":
        """<p>This API is used for deleting the <code>ResourceProperty</code> of the Glue connection (for the source) or Glue database ARN (for the target).</p>

        Args:
            resource_arn: <p>The connection ARN of the source, or the database ARN of the target.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_integration_resource_property_request.DeleteIntegrationResourcePropertyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_integration_resource_property_response.DeleteIntegrationResourcePropertyResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_integration_resource_property

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_integration_resource_property.async_delete_integration_resource_property(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_integration_resource_property_request.DeleteIntegrationResourcePropertyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_integration_table_properties(
        self,
        resource_arn: "aws_sdk_glue.types.string512.String512",
        table_name: "aws_sdk_glue.types.string128.String128",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.delete_integration_table_properties_response.DeleteIntegrationTablePropertiesResponse":
        """<p>Deletes the table properties that have been created for the tables that need to be replicated.</p>

        Args:
            resource_arn: <p>The connection ARN of the source, or the database ARN of the target.</p>
            table_name: <p>The name of the table to be replicated.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_integration_table_properties_request.DeleteIntegrationTablePropertiesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_integration_table_properties_response.DeleteIntegrationTablePropertiesResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_integration_table_properties

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_integration_table_properties.async_delete_integration_table_properties(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_integration_table_properties_request.DeleteIntegrationTablePropertiesRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["table_name"] = table_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_job(
        self,
        job_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.delete_job_response.DeleteJobResponse":
        """<p>Deletes a specified job definition. If the job definition is not found, no exception is thrown.</p>

        Args:
            job_name: <p>The name of the job definition to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_job_request.DeleteJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_job_response.DeleteJobResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_job

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_job.async_delete_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_job_request.DeleteJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_name"] = job_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_ml_transform(
        self,
        transform_id: "aws_sdk_glue.types.hash_string.HashString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.delete_ml_transform_response.DeleteMLTransformResponse":
        """<p>Deletes an Glue machine learning transform. Machine learning transforms are a special type of transform that use machine learning to learn the details of the transformation to be performed by learning from examples provided by humans. These transformations are then saved by Glue. If you no longer need a transform, you can delete it by calling <code>DeleteMLTransforms</code>. However, any Glue jobs that still reference the deleted transform will no longer succeed.</p>

        Args:
            transform_id: <p>The unique identifier of the transform to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_ml_transform_request.DeleteMLTransformRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_ml_transform_response.DeleteMLTransformResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_ml_transform

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_ml_transform.async_delete_ml_transform(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_ml_transform_request.DeleteMLTransformRequest = {}  # type: ignore[typeddict-item]
        input_["transform_id"] = transform_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_partition(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        partition_values: "aws_sdk_glue.types.value_string_list.ValueStringList",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.delete_partition_response.DeletePartitionResponse":
        """<p>Deletes a specified partition.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog where the partition to be deleted resides. If none is provided, the Amazon Web Services account ID is used by default.</p>
            database_name: <p>The name of the catalog database in which the table in question resides.</p>
            table_name: <p>The name of the table that contains the partition to be deleted.</p>
            partition_values: <p>The values that define the partition.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_partition_request.DeletePartitionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_partition_response.DeletePartitionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_partition

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_partition.async_delete_partition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_partition_request.DeletePartitionRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        input_["partition_values"] = partition_values

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_partition_index(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        index_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.delete_partition_index_response.DeletePartitionIndexResponse":
        """<p>Deletes a specified partition index from an existing table.</p>

        Args:
            catalog_id: <p>The catalog ID where the table resides.</p>
            database_name: <p>Specifies the name of a database from which you want to delete a partition index.</p>
            table_name: <p>Specifies the name of a table from which you want to delete a partition index.</p>
            index_name: <p>The name of the partition index to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_partition_index_request.DeletePartitionIndexRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_partition_index_response.DeletePartitionIndexResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_partition_index

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_partition_index.async_delete_partition_index(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_partition_index_request.DeletePartitionIndexRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        input_["index_name"] = index_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_registry(
        self,
        registry_id: "aws_sdk_glue.types.registry_id.RegistryId",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.delete_registry_response.DeleteRegistryResponse":
        """<p>Delete the entire registry including schema and all of its versions. To get the status of the delete operation, you can call the <code>GetRegistry</code> API after the asynchronous call. Deleting a registry will deactivate all online operations for the registry such as the <code>UpdateRegistry</code>, <code>CreateSchema</code>, <code>UpdateSchema</code>, and <code>RegisterSchemaVersion</code> APIs. </p>

        Args:
            registry_id: <p>This is a wrapper structure that may contain the registry name and Amazon Resource Name (ARN).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_registry_input.DeleteRegistryInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_registry_response.DeleteRegistryResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_registry

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_registry.async_delete_registry(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_registry_input.DeleteRegistryInput = {}  # type: ignore[typeddict-item]
        input_["registry_id"] = registry_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_resource_policy(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        policy_hash_condition: Optional[
            "aws_sdk_glue.types.hash_string.HashString"
        ] = None,
        resource_arn: Optional[
            "aws_sdk_glue.types.glue_resource_arn.GlueResourceArn"
        ] = None,
    ) -> "aws_sdk_glue.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """<p>Deletes a specified policy.</p>

        Args:
            policy_hash_condition: <p>The hash value returned when this policy was set.</p>
            resource_arn: <p>The ARN of the Glue resource for the resource policy to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_resource_policy.async_delete_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        if policy_hash_condition is not None:
            input_["policy_hash_condition"] = policy_hash_condition
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_schema(
        self,
        schema_id: "aws_sdk_glue.types.schema_id.SchemaId",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.delete_schema_response.DeleteSchemaResponse":
        """<p>Deletes the entire schema set, including the schema set and all of its versions. To get the status of the delete operation, you can call <code>GetSchema</code> API after the asynchronous call. Deleting a registry will deactivate all online operations for the schema, such as the <code>GetSchemaByDefinition</code>, and <code>RegisterSchemaVersion</code> APIs.</p>

        Args:
            schema_id: <p>This is a wrapper structure that may contain the schema name and Amazon Resource Name (ARN).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_schema_input.DeleteSchemaInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_schema_response.DeleteSchemaResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_schema

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_schema.async_delete_schema(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_schema_input.DeleteSchemaInput = {}  # type: ignore[typeddict-item]
        input_["schema_id"] = schema_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_schema_versions(
        self,
        schema_id: "aws_sdk_glue.types.schema_id.SchemaId",
        versions: "aws_sdk_glue.types.versions_string.VersionsString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.delete_schema_versions_response.DeleteSchemaVersionsResponse":
        """<p>Remove versions from the specified schema. A version number or range may be supplied. If the compatibility mode forbids deleting of a version that is necessary, such as BACKWARDS_FULL, an error is returned. Calling the <code>GetSchemaVersions</code> API after this call will list the status of the deleted versions.</p> <p>When the range of version numbers contain check pointed version, the API will return a 409 conflict and will not proceed with the deletion. You have to remove the checkpoint first using the <code>DeleteSchemaCheckpoint</code> API before using this API.</p> <p>You cannot use the <code>DeleteSchemaVersions</code> API to delete the first schema version in the schema set. The first schema version can only be deleted by the <code>DeleteSchema</code> API. This operation will also delete the attached <code>SchemaVersionMetadata</code> under the schema versions. Hard deletes will be enforced on the database.</p> <p>If the compatibility mode forbids deleting of a version that is necessary, such as BACKWARDS_FULL, an error is returned.</p>

        Args:
            schema_id: <p>This is a wrapper structure that may contain the schema name and Amazon Resource Name (ARN).</p>
            versions: <p>A version range may be supplied which may be of the format:</p> <ul> <li> <p>a single version number, 5</p> </li> <li> <p>a range, 5-8 : deletes versions 5, 6, 7, 8</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_schema_versions_input.DeleteSchemaVersionsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_schema_versions_response.DeleteSchemaVersionsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_schema_versions

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_schema_versions.async_delete_schema_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_schema_versions_input.DeleteSchemaVersionsInput = {}  # type: ignore[typeddict-item]
        input_["schema_id"] = schema_id
        input_["versions"] = versions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_security_configuration(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.delete_security_configuration_response.DeleteSecurityConfigurationResponse":
        """<p>Deletes a specified security configuration.</p>

        Args:
            name: <p>The name of the security configuration to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_security_configuration_request.DeleteSecurityConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_security_configuration_response.DeleteSecurityConfigurationResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_security_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_security_configuration.async_delete_security_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_security_configuration_request.DeleteSecurityConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_session(
        self,
        id: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        request_origin: Optional[
            "aws_sdk_glue.types.orchestration_name_string.OrchestrationNameString"
        ] = None,
    ) -> "aws_sdk_glue.types.delete_session_response.DeleteSessionResponse":
        """<p>Deletes the session.</p>

        Args:
            id: <p>The ID of the session to be deleted.</p>
            request_origin: <p>The name of the origin of the delete session request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_session_request.DeleteSessionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_session_response.DeleteSessionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_session

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_session.async_delete_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_session_request.DeleteSessionRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if request_origin is not None:
            input_["request_origin"] = request_origin

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_table(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
        transaction_id: Optional[
            "aws_sdk_glue.types.transaction_id_string.TransactionIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.delete_table_response.DeleteTableResponse":
        r"""<p>Removes a table definition from the Data Catalog.</p> <note> <p>After completing this operation, you no longer have access to the table versions and partitions that belong to the deleted table. Glue deletes these \"orphaned\" resources asynchronously in a timely manner, at the discretion of the service.</p> <p>To ensure the immediate deletion of all related resources, before calling <code>DeleteTable</code>, use <code>DeleteTableVersion</code> or <code>BatchDeleteTableVersion</code>, and <code>DeletePartition</code> or <code>BatchDeletePartition</code>, to delete any resources that belong to the table.</p> </note>

        Args:
            catalog_id: <p>The ID of the Data Catalog where the table resides. If none is provided, the Amazon Web Services account ID is used by default.</p>
            database_name: <p>The name of the catalog database in which the table resides. For Hive compatibility, this name is entirely lowercase.</p>
            name: <p>The name of the table to be deleted. For Hive compatibility, this name is entirely lowercase.</p>
            transaction_id: <p>The transaction ID at which to delete the table contents.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_table_request.DeleteTableRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_table_response.DeleteTableResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_table

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_table.async_delete_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_table_request.DeleteTableRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["name"] = name
        if transaction_id is not None:
            input_["transaction_id"] = transaction_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_table_optimizer(
        self,
        catalog_id: "aws_sdk_glue.types.catalog_id_string.CatalogIdString",
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        type: "aws_sdk_glue.types.table_optimizer_type.TableOptimizerType",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.delete_table_optimizer_response.DeleteTableOptimizerResponse":
        """<p>Deletes an optimizer and all associated metadata for a table. The optimization will no longer be performed on the table.</p>

        Args:
            catalog_id: <p>The Catalog ID of the table.</p>
            database_name: <p>The name of the database in the catalog in which the table resides.</p>
            table_name: <p>The name of the table.</p>
            type: <p>The type of table optimizer.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_table_optimizer_request.DeleteTableOptimizerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_table_optimizer_response.DeleteTableOptimizerResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_table_optimizer

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_table_optimizer.async_delete_table_optimizer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_table_optimizer_request.DeleteTableOptimizerRequest = {}  # type: ignore[typeddict-item]
        input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        input_["type"] = type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_table_version(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        version_id: "aws_sdk_glue.types.version_string.VersionString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.delete_table_version_response.DeleteTableVersionResponse":
        """<p>Deletes a specified version of a table.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog where the tables reside. If none is provided, the Amazon Web Services account ID is used by default.</p>
            database_name: <p>The database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase.</p>
            table_name: <p>The name of the table. For Hive compatibility, this name is entirely lowercase.</p>
            version_id: <p>The ID of the table version to be deleted. A <code>VersionID</code> is a string representation of an integer. Each version is incremented by 1.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_table_version_request.DeleteTableVersionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_table_version_response.DeleteTableVersionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_table_version

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_table_version.async_delete_table_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_table_version_request.DeleteTableVersionRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        input_["version_id"] = version_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_trigger(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.delete_trigger_response.DeleteTriggerResponse":
        """<p>Deletes a specified trigger. If the trigger is not found, no exception is thrown.</p>

        Args:
            name: <p>The name of the trigger to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_trigger_request.DeleteTriggerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_trigger_response.DeleteTriggerResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_trigger

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_trigger.async_delete_trigger(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_trigger_request.DeleteTriggerRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_usage_profile(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.delete_usage_profile_response.DeleteUsageProfileResponse":
        """<p>Deletes the Glue specified usage profile.</p>

        Args:
            name: <p>The name of the usage profile to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_usage_profile_request.DeleteUsageProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_usage_profile_response.DeleteUsageProfileResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_usage_profile

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_usage_profile.async_delete_usage_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_usage_profile_request.DeleteUsageProfileRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_user_defined_function(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        function_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.delete_user_defined_function_response.DeleteUserDefinedFunctionResponse":
        """<p>Deletes an existing function definition from the Data Catalog.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog where the function to be deleted is located. If none is supplied, the Amazon Web Services account ID is used by default.</p>
            database_name: <p>The name of the catalog database where the function is located.</p>
            function_name: <p>The name of the function definition to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_user_defined_function_request.DeleteUserDefinedFunctionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_user_defined_function_response.DeleteUserDefinedFunctionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_user_defined_function

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_user_defined_function.async_delete_user_defined_function(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_user_defined_function_request.DeleteUserDefinedFunctionRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["function_name"] = function_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_workflow(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.delete_workflow_response.DeleteWorkflowResponse":
        """<p>Deletes a workflow.</p>

        Args:
            name: <p>Name of the workflow to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.delete_workflow_request.DeleteWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.delete_workflow_response.DeleteWorkflowResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.delete_workflow

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.delete_workflow.async_delete_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.delete_workflow_request.DeleteWorkflowRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_connection_type(
        self,
        connection_type: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.describe_connection_type_response.DescribeConnectionTypeResponse":
        """<p>The <code>DescribeConnectionType</code> API provides full details of the supported options for a given connection type in Glue. The response includes authentication configuration details that show supported authentication types and properties, and RestConfiguration for custom REST-based connection types registered via <code>RegisterConnectionType</code>.</p> <p>See also: <code>ListConnectionTypes</code>, <code>RegisterConnectionType</code>, <code>DeleteConnectionType</code> </p>

        Args:
            connection_type: <p>The name of the connection type to be described.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.describe_connection_type_request.DescribeConnectionTypeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.describe_connection_type_response.DescribeConnectionTypeResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.describe_connection_type

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.describe_connection_type.async_describe_connection_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.describe_connection_type_request.DescribeConnectionTypeRequest = {}  # type: ignore[typeddict-item]
        input_["connection_type"] = connection_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_entity(
        self,
        connection_name: "aws_sdk_glue.types.name_string.NameString",
        entity_name: "aws_sdk_glue.types.entity_name.EntityName",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
        next_token: Optional["aws_sdk_glue.types.next_token.NextToken"] = None,
        data_store_api_version: Optional[
            "aws_sdk_glue.types.api_version.ApiVersion"
        ] = None,
    ) -> "aws_sdk_glue.types.describe_entity_response.DescribeEntityResponse":
        """<p>Provides details regarding the entity used with the connection type, with a description of the data model for each field in the selected entity.</p> <p> The response includes all the fields which make up the entity.</p>

        Args:
            connection_name: <p>The name of the connection that contains the connection type credentials.</p>
            catalog_id: <p>The catalog ID of the catalog that contains the connection. This can be null, By default, the Amazon Web Services Account ID is the catalog ID.</p>
            entity_name: <p>The name of the entity that you want to describe from the connection type.</p>
            next_token: <p>A continuation token, included if this is a continuation call.</p>
            data_store_api_version: <p>The version of the API used for the data store.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.describe_entity_request.DescribeEntityRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.describe_entity_response.DescribeEntityResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.describe_entity

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.describe_entity.async_describe_entity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.describe_entity_request.DescribeEntityRequest = {}  # type: ignore[typeddict-item]
        input_["connection_name"] = connection_name
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["entity_name"] = entity_name
        if next_token is not None:
            input_["next_token"] = next_token
        if data_store_api_version is not None:
            input_["data_store_api_version"] = data_store_api_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_describe_entity(
        self,
        connection_name: "aws_sdk_glue.types.name_string.NameString",
        entity_name: "aws_sdk_glue.types.entity_name.EntityName",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
        next_token: Optional["aws_sdk_glue.types.next_token.NextToken"] = None,
        data_store_api_version: Optional[
            "aws_sdk_glue.types.api_version.ApiVersion"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_glue.types.field.Field]":
        _token = next_token
        while True:
            _response = await self.describe_entity(
                connection_name,
                entity_name,
                config_overrides=config_overrides,
                catalog_id=catalog_id,
                next_token=_token,
                data_store_api_version=data_store_api_version,
            )
            _page = _resolve_path(_response, ("fields",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_inbound_integrations(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        integration_arn: Optional["aws_sdk_glue.types.string128.String128"] = None,
        marker: Optional["aws_sdk_glue.types.string128.String128"] = None,
        max_records: Optional[
            "aws_sdk_glue.types.integration_integer.IntegrationInteger"
        ] = None,
        target_arn: Optional["aws_sdk_glue.types.string512.String512"] = None,
    ) -> "aws_sdk_glue.types.describe_inbound_integrations_response.DescribeInboundIntegrationsResponse":
        """<p>Returns a list of inbound integrations for the specified integration.</p>

        Args:
            integration_arn: <p>The Amazon Resource Name (ARN) of the integration.</p>
            marker: <p>A token to specify where to start paginating. This is the marker from a previously truncated response.</p>
            max_records: <p>The total number of items to return in the output.</p>
            target_arn: <p>The Amazon Resource Name (ARN) of the target resource in the integration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.describe_inbound_integrations_request.DescribeInboundIntegrationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.describe_inbound_integrations_response.DescribeInboundIntegrationsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.describe_inbound_integrations

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.describe_inbound_integrations.async_describe_inbound_integrations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.describe_inbound_integrations_request.DescribeInboundIntegrationsRequest = {}  # type: ignore[typeddict-item]
        if integration_arn is not None:
            input_["integration_arn"] = integration_arn
        if marker is not None:
            input_["marker"] = marker
        if max_records is not None:
            input_["max_records"] = max_records
        if target_arn is not None:
            input_["target_arn"] = target_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_integrations(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        integration_identifier: Optional[
            "aws_sdk_glue.types.string128.String128"
        ] = None,
        marker: Optional["aws_sdk_glue.types.string128.String128"] = None,
        max_records: Optional[
            "aws_sdk_glue.types.integration_integer.IntegrationInteger"
        ] = None,
        filters: Optional[
            "aws_sdk_glue.types.integration_filter_list.IntegrationFilterList"
        ] = None,
    ) -> (
        "aws_sdk_glue.types.describe_integrations_response.DescribeIntegrationsResponse"
    ):
        r"""<p>The API is used to retrieve a list of integrations.</p>

        Args:
            integration_identifier: <p>The Amazon Resource Name (ARN) for the integration.</p>
            marker: <p>A value that indicates the starting point for the next set of response records in a subsequent request.</p>
            max_records: <p>The total number of items to return in the output.</p>
            filters: <p>A list of key and values, to filter down the results. Supported keys are \"Status\", \"IntegrationName\", and \"SourceArn\". IntegrationName is limited to only one value.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.describe_integrations_request.DescribeIntegrationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.describe_integrations_response.DescribeIntegrationsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.describe_integrations

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.describe_integrations.async_describe_integrations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.describe_integrations_request.DescribeIntegrationsRequest = {}  # type: ignore[typeddict-item]
        if integration_identifier is not None:
            input_["integration_identifier"] = integration_identifier
        if marker is not None:
            input_["marker"] = marker
        if max_records is not None:
            input_["max_records"] = max_records
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_blueprint(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        include_blueprint: Optional[
            "aws_sdk_glue.types.nullable_boolean.NullableBoolean"
        ] = None,
        include_parameter_spec: Optional[
            "aws_sdk_glue.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "aws_sdk_glue.types.get_blueprint_response.GetBlueprintResponse":
        """<p>Retrieves the details of a blueprint.</p>

        Args:
            name: <p>The name of the blueprint.</p>
            include_blueprint: <p>Specifies whether or not to include the blueprint in the response.</p>
            include_parameter_spec: <p>Specifies whether or not to include the parameter specification.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_blueprint_request.GetBlueprintRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_blueprint_response.GetBlueprintResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_blueprint

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_blueprint.async_get_blueprint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_blueprint_request.GetBlueprintRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if include_blueprint is not None:
            input_["include_blueprint"] = include_blueprint
        if include_parameter_spec is not None:
            input_["include_parameter_spec"] = include_parameter_spec

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_blueprint_run(
        self,
        blueprint_name: "aws_sdk_glue.types.orchestration_name_string.OrchestrationNameString",
        run_id: "aws_sdk_glue.types.id_string.IdString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.get_blueprint_run_response.GetBlueprintRunResponse":
        """<p>Retrieves the details of a blueprint run.</p>

        Args:
            blueprint_name: <p>The name of the blueprint.</p>
            run_id: <p>The run ID for the blueprint run you want to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_blueprint_run_request.GetBlueprintRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_blueprint_run_response.GetBlueprintRunResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_blueprint_run

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_blueprint_run.async_get_blueprint_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_blueprint_run_request.GetBlueprintRunRequest = {}  # type: ignore[typeddict-item]
        input_["blueprint_name"] = blueprint_name
        input_["run_id"] = run_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_blueprint_runs(
        self,
        blueprint_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        next_token: Optional["aws_sdk_glue.types.generic_string.GenericString"] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
    ) -> "aws_sdk_glue.types.get_blueprint_runs_response.GetBlueprintRunsResponse":
        """<p>Retrieves the details of blueprint runs for a specified blueprint.</p>

        Args:
            blueprint_name: <p>The name of the blueprint.</p>
            next_token: <p>A continuation token, if this is a continuation request.</p>
            max_results: <p>The maximum size of a list to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_blueprint_runs_request.GetBlueprintRunsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_blueprint_runs_response.GetBlueprintRunsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_blueprint_runs

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_blueprint_runs.async_get_blueprint_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_blueprint_runs_request.GetBlueprintRunsRequest = {}  # type: ignore[typeddict-item]
        input_["blueprint_name"] = blueprint_name
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

    async def get_catalog(
        self,
        catalog_id: "aws_sdk_glue.types.catalog_id_string.CatalogIdString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.get_catalog_response.GetCatalogResponse":
        """<p>The name of the Catalog to retrieve. This should be all lowercase.</p>

        Args:
            catalog_id: <p>The ID of the parent catalog in which the catalog resides. If none is provided, the Amazon Web Services Account Number is used by default.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_catalog_request.GetCatalogRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_catalog_response.GetCatalogResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_catalog

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_catalog.async_get_catalog(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_catalog_request.GetCatalogRequest = {}  # type: ignore[typeddict-item]
        input_["catalog_id"] = catalog_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_catalog_import_status(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.get_catalog_import_status_response.GetCatalogImportStatusResponse":
        """<p>Retrieves the status of a migration operation.</p>

        Args:
            catalog_id: <p>The ID of the catalog to migrate. Currently, this should be the Amazon Web Services account ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_catalog_import_status_request.GetCatalogImportStatusRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_catalog_import_status_response.GetCatalogImportStatusResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_catalog_import_status

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_catalog_import_status.async_get_catalog_import_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_catalog_import_status_request.GetCatalogImportStatusRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_catalogs(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        parent_catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
        next_token: Optional["aws_sdk_glue.types.token.Token"] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
        recursive: Optional["aws_sdk_glue.types.boolean.Boolean"] = None,
        include_root: Optional[
            "aws_sdk_glue.types.nullable_boolean.NullableBoolean"
        ] = None,
        has_databases: Optional[
            "aws_sdk_glue.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "aws_sdk_glue.types.get_catalogs_response.GetCatalogsResponse":
        """<p>Retrieves all catalogs defined in a catalog in the Glue Data Catalog. For a Redshift-federated catalog use case, this operation returns the list of catalogs mapped to Redshift databases in the Redshift namespace catalog.</p>

        Args:
            parent_catalog_id: <p>The ID of the parent catalog in which the catalog resides. If none is provided, the Amazon Web Services Account Number is used by default.</p>
            next_token: <p>A continuation token, if this is a continuation call.</p>
            max_results: <p>The maximum number of catalogs to return in one response.</p>
            recursive: <p>Whether to list all catalogs across the catalog hierarchy, starting from the <code>ParentCatalogId</code>. Defaults to <code>false</code> . When <code>true</code>, all catalog objects in the <code>ParentCatalogID</code> hierarchy are enumerated in the response.</p>
            include_root: <p>Whether to list the default catalog in the account and region in the response. Defaults to <code>false</code>. When <code>true</code> and <code>ParentCatalogId = NULL | Amazon Web Services Account ID</code>, all catalogs and the default catalog are enumerated in the response.</p> <p>When the <code>ParentCatalogId</code> is not equal to null, and this attribute is passed as <code>false</code> or <code>true</code>, an <code>InvalidInputException</code> is thrown.</p>
            has_databases: <p>When <code>true</code>, the response only includes catalogs that can contain databases. Some catalogs are organizational containers that hold only other catalogs, not databases. When this parameter is set to <code>true</code>, those container-only catalogs are excluded, and only catalogs capable of containing databases are returned. Defaults to <code>false</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_catalogs_request.GetCatalogsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_catalogs_response.GetCatalogsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_catalogs

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_catalogs.async_get_catalogs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_catalogs_request.GetCatalogsRequest = {}  # type: ignore[typeddict-item]
        if parent_catalog_id is not None:
            input_["parent_catalog_id"] = parent_catalog_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if recursive is not None:
            input_["recursive"] = recursive
        if include_root is not None:
            input_["include_root"] = include_root
        if has_databases is not None:
            input_["has_databases"] = has_databases

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_classifier(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.get_classifier_response.GetClassifierResponse":
        """<p>Retrieve a classifier by name.</p>

        Args:
            name: <p>Name of the classifier to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_classifier_request.GetClassifierRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_classifier_response.GetClassifierResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_classifier

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_classifier.async_get_classifier(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_classifier_request.GetClassifierRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_classifiers(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
        next_token: Optional["aws_sdk_glue.types.token.Token"] = None,
    ) -> "aws_sdk_glue.types.get_classifiers_response.GetClassifiersResponse":
        """<p>Lists all classifier objects in the Data Catalog.</p>

        Args:
            max_results: <p>The size of the list to return (optional).</p>
            next_token: <p>An optional continuation token.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_classifiers_request.GetClassifiersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_classifiers_response.GetClassifiersResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_classifiers

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_classifiers.async_get_classifiers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_classifiers_request.GetClassifiersRequest = {}  # type: ignore[typeddict-item]
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

    async def get_column_statistics_for_partition(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        partition_values: "aws_sdk_glue.types.value_string_list.ValueStringList",
        column_names: "aws_sdk_glue.types.get_column_names_list.GetColumnNamesList",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.get_column_statistics_for_partition_response.GetColumnStatisticsForPartitionResponse":
        """<p>Retrieves partition statistics of columns.</p> <p>The Identity and Access Management (IAM) permission required for this operation is <code>GetPartition</code>.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog where the partitions in question reside. If none is supplied, the Amazon Web Services account ID is used by default.</p>
            database_name: <p>The name of the catalog database where the partitions reside.</p>
            table_name: <p>The name of the partitions' table.</p>
            partition_values: <p>A list of partition values identifying the partition.</p>
            column_names: <p>A list of the column names.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_column_statistics_for_partition_request.GetColumnStatisticsForPartitionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_column_statistics_for_partition_response.GetColumnStatisticsForPartitionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_column_statistics_for_partition

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_column_statistics_for_partition.async_get_column_statistics_for_partition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_column_statistics_for_partition_request.GetColumnStatisticsForPartitionRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        input_["partition_values"] = partition_values
        input_["column_names"] = column_names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_column_statistics_for_table(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        column_names: "aws_sdk_glue.types.get_column_names_list.GetColumnNamesList",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.get_column_statistics_for_table_response.GetColumnStatisticsForTableResponse":
        """<p>Retrieves table statistics of columns.</p> <p>The Identity and Access Management (IAM) permission required for this operation is <code>GetTable</code>.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog where the partitions in question reside. If none is supplied, the Amazon Web Services account ID is used by default.</p>
            database_name: <p>The name of the catalog database where the partitions reside.</p>
            table_name: <p>The name of the partitions' table.</p>
            column_names: <p>A list of the column names.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_column_statistics_for_table_request.GetColumnStatisticsForTableRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_column_statistics_for_table_response.GetColumnStatisticsForTableResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_column_statistics_for_table

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_column_statistics_for_table.async_get_column_statistics_for_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_column_statistics_for_table_request.GetColumnStatisticsForTableRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        input_["column_names"] = column_names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_column_statistics_task_run(
        self,
        column_statistics_task_run_id: "aws_sdk_glue.types.hash_string.HashString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.get_column_statistics_task_run_response.GetColumnStatisticsTaskRunResponse":
        """<p>Get the associated metadata/information for a task run, given a task run ID.</p>

        Args:
            column_statistics_task_run_id: <p>The identifier for the particular column statistics task run.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_column_statistics_task_run_request.GetColumnStatisticsTaskRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_column_statistics_task_run_response.GetColumnStatisticsTaskRunResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_column_statistics_task_run

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_column_statistics_task_run.async_get_column_statistics_task_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_column_statistics_task_run_request.GetColumnStatisticsTaskRunRequest = {}  # type: ignore[typeddict-item]
        input_["column_statistics_task_run_id"] = column_statistics_task_run_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_column_statistics_task_runs(
        self,
        database_name: "aws_sdk_glue.types.database_name.DatabaseName",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
        next_token: Optional["aws_sdk_glue.types.token.Token"] = None,
    ) -> "aws_sdk_glue.types.get_column_statistics_task_runs_response.GetColumnStatisticsTaskRunsResponse":
        """<p>Retrieves information about all runs associated with the specified table.</p>

        Args:
            database_name: <p>The name of the database where the table resides.</p>
            table_name: <p>The name of the table.</p>
            max_results: <p>The maximum size of the response.</p>
            next_token: <p>A continuation token, if this is a continuation call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_column_statistics_task_runs_request.GetColumnStatisticsTaskRunsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_column_statistics_task_runs_response.GetColumnStatisticsTaskRunsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_column_statistics_task_runs

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_column_statistics_task_runs.async_get_column_statistics_task_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_column_statistics_task_runs_request.GetColumnStatisticsTaskRunsRequest = {}  # type: ignore[typeddict-item]
        input_["database_name"] = database_name
        input_["table_name"] = table_name
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

    async def get_column_statistics_task_settings(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.get_column_statistics_task_settings_response.GetColumnStatisticsTaskSettingsResponse":
        """<p>Gets settings for a column statistics task.</p>

        Args:
            database_name: <p>The name of the database where the table resides.</p>
            table_name: <p>The name of the table for which to retrieve column statistics.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_column_statistics_task_settings_request.GetColumnStatisticsTaskSettingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_column_statistics_task_settings_response.GetColumnStatisticsTaskSettingsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_column_statistics_task_settings

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_column_statistics_task_settings.async_get_column_statistics_task_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_column_statistics_task_settings_request.GetColumnStatisticsTaskSettingsRequest = {}  # type: ignore[typeddict-item]
        input_["database_name"] = database_name
        input_["table_name"] = table_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_connection(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
        hide_password: Optional["aws_sdk_glue.types.boolean.Boolean"] = None,
        apply_override_for_compute_environment: Optional[
            "aws_sdk_glue.types.compute_environment.ComputeEnvironment"
        ] = None,
    ) -> "aws_sdk_glue.types.get_connection_response.GetConnectionResponse":
        """<p>Retrieves a connection definition from the Data Catalog.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog in which the connection resides. If none is provided, the Amazon Web Services account ID is used by default.</p>
            name: <p>The name of the connection definition to retrieve.</p>
            hide_password: <p>Allows you to retrieve the connection metadata without returning the password. For instance, the Glue console uses this flag to retrieve the connection, and does not display the password. Set this parameter when the caller might not have permission to use the KMS key to decrypt the password, but it does have permission to access the rest of the connection properties.</p>
            apply_override_for_compute_environment: <p>For connections that may be used in multiple services, specifies returning properties for the specified compute environment.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_connection_request.GetConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_connection_response.GetConnectionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_connection

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_connection.async_get_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_connection_request.GetConnectionRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["name"] = name
        if hide_password is not None:
            input_["hide_password"] = hide_password
        if apply_override_for_compute_environment is not None:
            input_["apply_override_for_compute_environment"] = (
                apply_override_for_compute_environment
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_connections(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
        filter: Optional[
            "aws_sdk_glue.types.get_connections_filter.GetConnectionsFilter"
        ] = None,
        hide_password: Optional["aws_sdk_glue.types.boolean.Boolean"] = None,
        next_token: Optional["aws_sdk_glue.types.token.Token"] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
    ) -> "aws_sdk_glue.types.get_connections_response.GetConnectionsResponse":
        """<p>Retrieves a list of connection definitions from the Data Catalog.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog in which the connections reside. If none is provided, the Amazon Web Services account ID is used by default.</p>
            filter: <p>A filter that controls which connections are returned.</p>
            hide_password: <p>Allows you to retrieve the connection metadata without returning the password. For instance, the Glue console uses this flag to retrieve the connection, and does not display the password. Set this parameter when the caller might not have permission to use the KMS key to decrypt the password, but it does have permission to access the rest of the connection properties.</p>
            next_token: <p>A continuation token, if this is a continuation call.</p>
            max_results: <p>The maximum number of connections to return in one response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_connections_request.GetConnectionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_connections_response.GetConnectionsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_connections

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_connections.async_get_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_connections_request.GetConnectionsRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        if filter is not None:
            input_["filter"] = filter
        if hide_password is not None:
            input_["hide_password"] = hide_password
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

    async def get_crawler(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.get_crawler_response.GetCrawlerResponse":
        """<p>Retrieves metadata for a specified crawler.</p>

        Args:
            name: <p>The name of the crawler to retrieve metadata for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_crawler_request.GetCrawlerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_crawler_response.GetCrawlerResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_crawler

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_crawler.async_get_crawler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_crawler_request.GetCrawlerRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_crawler_metrics(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        crawler_name_list: Optional[
            "aws_sdk_glue.types.crawler_name_list.CrawlerNameList"
        ] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
        next_token: Optional["aws_sdk_glue.types.token.Token"] = None,
    ) -> "aws_sdk_glue.types.get_crawler_metrics_response.GetCrawlerMetricsResponse":
        """<p>Retrieves metrics about specified crawlers.</p>

        Args:
            crawler_name_list: <p>A list of the names of crawlers about which to retrieve metrics.</p>
            max_results: <p>The maximum size of a list to return.</p>
            next_token: <p>A continuation token, if this is a continuation call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_crawler_metrics_request.GetCrawlerMetricsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_crawler_metrics_response.GetCrawlerMetricsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_crawler_metrics

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_crawler_metrics.async_get_crawler_metrics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_crawler_metrics_request.GetCrawlerMetricsRequest = {}  # type: ignore[typeddict-item]
        if crawler_name_list is not None:
            input_["crawler_name_list"] = crawler_name_list
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

    async def get_crawlers(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
        next_token: Optional["aws_sdk_glue.types.token.Token"] = None,
    ) -> "aws_sdk_glue.types.get_crawlers_response.GetCrawlersResponse":
        """<p>Retrieves metadata for all crawlers defined in the customer account.</p>

        Args:
            max_results: <p>The number of crawlers to return on each call.</p>
            next_token: <p>A continuation token, if this is a continuation request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_crawlers_request.GetCrawlersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_crawlers_response.GetCrawlersResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_crawlers

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_crawlers.async_get_crawlers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_crawlers_request.GetCrawlersRequest = {}  # type: ignore[typeddict-item]
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

    async def get_custom_entity_type(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> (
        "aws_sdk_glue.types.get_custom_entity_type_response.GetCustomEntityTypeResponse"
    ):
        """<p>Retrieves the details of a custom pattern by specifying its name.</p>

        Args:
            name: <p>The name of the custom pattern that you want to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_custom_entity_type_request.GetCustomEntityTypeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_custom_entity_type_response.GetCustomEntityTypeResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_custom_entity_type

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_custom_entity_type.async_get_custom_entity_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_custom_entity_type_request.GetCustomEntityTypeRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_dashboard_url(
        self,
        resource_id: "aws_sdk_glue.types.name_string.NameString",
        resource_type: "aws_sdk_glue.types.glue_resource_type.GlueResourceType",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        request_origin: Optional[
            "aws_sdk_glue.types.orchestration_name_string.OrchestrationNameString"
        ] = None,
    ) -> "aws_sdk_glue.types.get_dashboard_url_response.GetDashboardUrlResponse":
        """<p>Retrieves the URL for the Spark monitoring dashboard for a Glue resource.</p>

        Args:
            resource_id: <p>The unique identifier of the resource for which to retrieve the dashboard URL.</p>
            resource_type: <p>The type of the resource. Valid values are <code>SESSION</code> and <code>JOB</code>.</p>
            request_origin: <p>The origin of the request. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_dashboard_url_request.GetDashboardUrlRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_dashboard_url_response.GetDashboardUrlResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_dashboard_url

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_dashboard_url.async_get_dashboard_url(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_dashboard_url_request.GetDashboardUrlRequest = {}  # type: ignore[typeddict-item]
        input_["resource_id"] = resource_id
        input_["resource_type"] = resource_type
        if request_origin is not None:
            input_["request_origin"] = request_origin

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_database(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.get_database_response.GetDatabaseResponse":
        """<p>Retrieves the definition of a specified database.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog in which the database resides. If none is provided, the Amazon Web Services account ID is used by default.</p>
            name: <p>The name of the database to retrieve. For Hive compatibility, this should be all lowercase.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_database_request.GetDatabaseRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_database_response.GetDatabaseResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_database

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_database.async_get_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_database_request.GetDatabaseRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_databases(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
        next_token: Optional["aws_sdk_glue.types.token.Token"] = None,
        max_results: Optional[
            "aws_sdk_glue.types.catalog_getter_page_size.CatalogGetterPageSize"
        ] = None,
        resource_share_type: Optional[
            "aws_sdk_glue.types.resource_share_type.ResourceShareType"
        ] = None,
        attributes_to_get: Optional[
            "aws_sdk_glue.types.database_attributes_list.DatabaseAttributesList"
        ] = None,
    ) -> "aws_sdk_glue.types.get_databases_response.GetDatabasesResponse":
        """<p>Retrieves all databases defined in a given Data Catalog.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog from which to retrieve <code>Databases</code>. If none is provided, the Amazon Web Services account ID is used by default.</p>
            next_token: <p>A continuation token, if this is a continuation call.</p>
            max_results: <p>The maximum number of databases to return in one response.</p>
            resource_share_type: <p>Allows you to specify that you want to list the databases shared with your account. The allowable values are <code>FEDERATED</code>, <code>FOREIGN</code> or <code>ALL</code>. </p> <ul> <li> <p>If set to <code>FEDERATED</code>, will list the federated databases (referencing an external entity) shared with your account.</p> </li> <li> <p>If set to <code>FOREIGN</code>, will list the databases shared with your account. </p> </li> <li> <p>If set to <code>ALL</code>, will list the databases shared with your account, as well as the databases in yor local account. </p> </li> </ul>
            attributes_to_get: <p>Specifies the database fields returned by the <code>GetDatabases</code> call. This parameter doesn’t accept an empty list. The request must include the <code>NAME</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_databases_request.GetDatabasesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_databases_response.GetDatabasesResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_databases

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_databases.async_get_databases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_databases_request.GetDatabasesRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if resource_share_type is not None:
            input_["resource_share_type"] = resource_share_type
        if attributes_to_get is not None:
            input_["attributes_to_get"] = attributes_to_get

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_data_catalog_encryption_settings(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.get_data_catalog_encryption_settings_response.GetDataCatalogEncryptionSettingsResponse":
        """<p>Retrieves the security configuration for a specified catalog.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog to retrieve the security configuration for. If none is provided, the Amazon Web Services account ID is used by default.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_data_catalog_encryption_settings_request.GetDataCatalogEncryptionSettingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_data_catalog_encryption_settings_response.GetDataCatalogEncryptionSettingsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_data_catalog_encryption_settings

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_data_catalog_encryption_settings.async_get_data_catalog_encryption_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_data_catalog_encryption_settings_request.GetDataCatalogEncryptionSettingsRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_dataflow_graph(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        python_script: Optional["aws_sdk_glue.types.python_script.PythonScript"] = None,
    ) -> "aws_sdk_glue.types.get_dataflow_graph_response.GetDataflowGraphResponse":
        """<p>Transforms a Python script into a directed acyclic graph (DAG). </p>

        Args:
            python_script: <p>The Python script to transform.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_dataflow_graph_request.GetDataflowGraphRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_dataflow_graph_response.GetDataflowGraphResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_dataflow_graph

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_dataflow_graph.async_get_dataflow_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_dataflow_graph_request.GetDataflowGraphRequest = {}  # type: ignore[typeddict-item]
        if python_script is not None:
            input_["python_script"] = python_script

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_data_quality_model(
        self,
        profile_id: "aws_sdk_glue.types.hash_string.HashString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        statistic_id: Optional["aws_sdk_glue.types.hash_string.HashString"] = None,
    ) -> (
        "aws_sdk_glue.types.get_data_quality_model_response.GetDataQualityModelResponse"
    ):
        """<p>Retrieve the training status of the model along with more information (CompletedOn, StartedOn, FailureReason).</p>

        Args:
            statistic_id: <p>The Statistic ID.</p>
            profile_id: <p>The Profile ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_data_quality_model_request.GetDataQualityModelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_data_quality_model_response.GetDataQualityModelResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_data_quality_model

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_data_quality_model.async_get_data_quality_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_data_quality_model_request.GetDataQualityModelRequest = {}  # type: ignore[typeddict-item]
        if statistic_id is not None:
            input_["statistic_id"] = statistic_id
        input_["profile_id"] = profile_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_data_quality_model_result(
        self,
        statistic_id: "aws_sdk_glue.types.hash_string.HashString",
        profile_id: "aws_sdk_glue.types.hash_string.HashString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.get_data_quality_model_result_response.GetDataQualityModelResultResponse":
        """<p>Retrieve a statistic's predictions for a given Profile ID.</p>

        Args:
            statistic_id: <p>The Statistic ID.</p>
            profile_id: <p>The Profile ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_data_quality_model_result_request.GetDataQualityModelResultRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_data_quality_model_result_response.GetDataQualityModelResultResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_data_quality_model_result

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_data_quality_model_result.async_get_data_quality_model_result(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_data_quality_model_result_request.GetDataQualityModelResultRequest = {}  # type: ignore[typeddict-item]
        input_["statistic_id"] = statistic_id
        input_["profile_id"] = profile_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_data_quality_result(
        self,
        result_id: "aws_sdk_glue.types.hash_string.HashString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.get_data_quality_result_response.GetDataQualityResultResponse":
        """<p>Retrieves the result of a data quality rule evaluation.</p>

        Args:
            result_id: <p>A unique result ID for the data quality result.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_data_quality_result_request.GetDataQualityResultRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_data_quality_result_response.GetDataQualityResultResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_data_quality_result

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_data_quality_result.async_get_data_quality_result(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_data_quality_result_request.GetDataQualityResultRequest = {}  # type: ignore[typeddict-item]
        input_["result_id"] = result_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_data_quality_rule_recommendation_run(
        self,
        run_id: "aws_sdk_glue.types.hash_string.HashString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.get_data_quality_rule_recommendation_run_response.GetDataQualityRuleRecommendationRunResponse":
        """<p>Gets the specified recommendation run that was used to generate rules.</p>

        Args:
            run_id: <p>The unique run identifier associated with this run.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_data_quality_rule_recommendation_run_request.GetDataQualityRuleRecommendationRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_data_quality_rule_recommendation_run_response.GetDataQualityRuleRecommendationRunResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_data_quality_rule_recommendation_run

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_data_quality_rule_recommendation_run.async_get_data_quality_rule_recommendation_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_data_quality_rule_recommendation_run_request.GetDataQualityRuleRecommendationRunRequest = {}  # type: ignore[typeddict-item]
        input_["run_id"] = run_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_data_quality_ruleset(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.get_data_quality_ruleset_response.GetDataQualityRulesetResponse":
        """<p>Returns an existing ruleset by identifier or name.</p>

        Args:
            name: <p>The name of the ruleset.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_data_quality_ruleset_request.GetDataQualityRulesetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_data_quality_ruleset_response.GetDataQualityRulesetResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_data_quality_ruleset

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_data_quality_ruleset.async_get_data_quality_ruleset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_data_quality_ruleset_request.GetDataQualityRulesetRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_data_quality_ruleset_evaluation_run(
        self,
        run_id: "aws_sdk_glue.types.hash_string.HashString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.get_data_quality_ruleset_evaluation_run_response.GetDataQualityRulesetEvaluationRunResponse":
        """<p>Retrieves a specific run where a ruleset is evaluated against a data source.</p>

        Args:
            run_id: <p>The unique run identifier associated with this run.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_data_quality_ruleset_evaluation_run_request.GetDataQualityRulesetEvaluationRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_data_quality_ruleset_evaluation_run_response.GetDataQualityRulesetEvaluationRunResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_data_quality_ruleset_evaluation_run

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_data_quality_ruleset_evaluation_run.async_get_data_quality_ruleset_evaluation_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_data_quality_ruleset_evaluation_run_request.GetDataQualityRulesetEvaluationRunRequest = {}  # type: ignore[typeddict-item]
        input_["run_id"] = run_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_dev_endpoint(
        self,
        endpoint_name: "aws_sdk_glue.types.generic_string.GenericString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.get_dev_endpoint_response.GetDevEndpointResponse":
        """<p>Retrieves information about a specified development endpoint.</p> <note> <p>When you create a development endpoint in a virtual private cloud (VPC), Glue returns only a private IP address, and the public IP address field is not populated. When you create a non-VPC development endpoint, Glue returns only a public IP address.</p> </note>

        Args:
            endpoint_name: <p>Name of the <code>DevEndpoint</code> to retrieve information for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_dev_endpoint_request.GetDevEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_dev_endpoint_response.GetDevEndpointResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_dev_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_dev_endpoint.async_get_dev_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_dev_endpoint_request.GetDevEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["endpoint_name"] = endpoint_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_dev_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
        next_token: Optional["aws_sdk_glue.types.generic_string.GenericString"] = None,
    ) -> "aws_sdk_glue.types.get_dev_endpoints_response.GetDevEndpointsResponse":
        """<p>Retrieves all the development endpoints in this Amazon Web Services account.</p> <note> <p>When you create a development endpoint in a virtual private cloud (VPC), Glue returns only a private IP address and the public IP address field is not populated. When you create a non-VPC development endpoint, Glue returns only a public IP address.</p> </note>

        Args:
            max_results: <p>The maximum size of information to return.</p>
            next_token: <p>A continuation token, if this is a continuation call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_dev_endpoints_request.GetDevEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_dev_endpoints_response.GetDevEndpointsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_dev_endpoints

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_dev_endpoints.async_get_dev_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_dev_endpoints_request.GetDevEndpointsRequest = {}  # type: ignore[typeddict-item]
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

    async def get_entity_records(
        self,
        entity_name: "aws_sdk_glue.types.entity_name.EntityName",
        limit: "aws_sdk_glue.types.limit.Limit",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        connection_name: Optional["aws_sdk_glue.types.name_string.NameString"] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
        next_token: Optional["aws_sdk_glue.types.next_token.NextToken"] = None,
        data_store_api_version: Optional[
            "aws_sdk_glue.types.api_version.ApiVersion"
        ] = None,
        connection_options: Optional[
            "aws_sdk_glue.types.connection_options.ConnectionOptions"
        ] = None,
        filter_predicate: Optional[
            "aws_sdk_glue.types.filter_predicate.FilterPredicate"
        ] = None,
        order_by: Optional[str] = None,
        selected_fields: Optional[
            "aws_sdk_glue.types.selected_fields.SelectedFields"
        ] = None,
    ) -> "aws_sdk_glue.types.get_entity_records_response.GetEntityRecordsResponse":
        """<p>This API is used to query preview data from a given connection type or from a native Amazon S3 based Glue Data Catalog.</p> <p>Returns records as an array of JSON blobs. Each record is formatted using Jackson JsonNode based on the field type defined by the <code>DescribeEntity</code> API.</p> <p>Spark connectors generate schemas according to the same data type mapping as in the <code>DescribeEntity</code> API. Spark connectors convert data to the appropriate data types matching the schema when returning rows.</p>

        Args:
            connection_name: <p>The name of the connection that contains the connection type credentials.</p>
            catalog_id: <p>The catalog ID of the catalog that contains the connection. This can be null, By default, the Amazon Web Services Account ID is the catalog ID.</p>
            entity_name: <p>Name of the entity that we want to query the preview data from the given connection type.</p>
            next_token: <p>A continuation token, included if this is a continuation call.</p>
            data_store_api_version: <p>The API version of the SaaS connector.</p>
            connection_options: <p>Connector options that are required to query the data.</p>
            filter_predicate: <p>A filter predicate that you can apply in the query request.</p>
            limit: <p>Limits the number of records fetched with the request.</p>
            order_by: <p>A parameter that orders the response preview data.</p>
            selected_fields: <p> List of fields that we want to fetch as part of preview data.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_entity_records_request.GetEntityRecordsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_entity_records_response.GetEntityRecordsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_entity_records

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_entity_records.async_get_entity_records(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_entity_records_request.GetEntityRecordsRequest = {}  # type: ignore[typeddict-item]
        if connection_name is not None:
            input_["connection_name"] = connection_name
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["entity_name"] = entity_name
        if next_token is not None:
            input_["next_token"] = next_token
        if data_store_api_version is not None:
            input_["data_store_api_version"] = data_store_api_version
        if connection_options is not None:
            input_["connection_options"] = connection_options
        if filter_predicate is not None:
            input_["filter_predicate"] = filter_predicate
        input_["limit"] = limit
        if order_by is not None:
            input_["order_by"] = order_by
        if selected_fields is not None:
            input_["selected_fields"] = selected_fields

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_glue_identity_center_configuration(
        self, *, config_overrides: Optional[AsyncGlueClientConfig] = None
    ) -> "aws_sdk_glue.types.get_glue_identity_center_configuration_response.GetGlueIdentityCenterConfigurationResponse":
        """<p>Retrieves the current Glue Identity Center configuration details, including the associated Identity Center instance and application information.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_glue_identity_center_configuration_request.GetGlueIdentityCenterConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_glue_identity_center_configuration_response.GetGlueIdentityCenterConfigurationResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_glue_identity_center_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_glue_identity_center_configuration.async_get_glue_identity_center_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_glue_identity_center_configuration_request.GetGlueIdentityCenterConfigurationRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_integration_resource_property(
        self,
        resource_arn: "aws_sdk_glue.types.string512.String512",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.get_integration_resource_property_response.GetIntegrationResourcePropertyResponse":
        """<p>This API is used for fetching the <code>ResourceProperty</code> of the Glue connection (for the source) or Glue database ARN (for the target)</p>

        Args:
            resource_arn: <p>The connection ARN of the source, or the database ARN of the target.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_integration_resource_property_request.GetIntegrationResourcePropertyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_integration_resource_property_response.GetIntegrationResourcePropertyResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_integration_resource_property

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_integration_resource_property.async_get_integration_resource_property(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_integration_resource_property_request.GetIntegrationResourcePropertyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_integration_table_properties(
        self,
        resource_arn: "aws_sdk_glue.types.string512.String512",
        table_name: "aws_sdk_glue.types.string128.String128",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.get_integration_table_properties_response.GetIntegrationTablePropertiesResponse":
        """<p>This API is used to retrieve optional override properties for the tables that need to be replicated. These properties can include properties for filtering and partition for source and target tables.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the target table for which to retrieve integration table properties. Currently, this API only supports retrieving properties for target tables, and the provided ARN should be the ARN of the target table in the Glue Data Catalog. Support for retrieving integration table properties for source connections (using the connection ARN) is not yet implemented and will be added in a future release. </p>
            table_name: <p>The name of the table to be replicated.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_integration_table_properties_request.GetIntegrationTablePropertiesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_integration_table_properties_response.GetIntegrationTablePropertiesResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_integration_table_properties

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_integration_table_properties.async_get_integration_table_properties(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_integration_table_properties_request.GetIntegrationTablePropertiesRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["table_name"] = table_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_job(
        self,
        job_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.get_job_response.GetJobResponse":
        """<p>Retrieves an existing job definition.</p>

        Args:
            job_name: <p>The name of the job definition to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_job_request.GetJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_job_response.GetJobResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_job

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_job.async_get_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_job_request.GetJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_name"] = job_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_job_bookmark(
        self,
        job_name: "aws_sdk_glue.types.job_name.JobName",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        run_id: Optional["aws_sdk_glue.types.run_id.RunId"] = None,
    ) -> "aws_sdk_glue.types.get_job_bookmark_response.GetJobBookmarkResponse":
        r"""<p>Returns information on a job bookmark entry.</p> <p>For more information about enabling and using job bookmarks, see:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/glue/latest/dg/monitor-continuations.html\">Tracking processed data using job bookmarks</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html\">Job parameters used by Glue</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-job.html#aws-glue-api-jobs-job-Job\">Job structure</a> </p> </li> </ul>

        Args:
            job_name: <p>The name of the job in question.</p>
            run_id: <p>The unique run identifier associated with this job run.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_job_bookmark_request.GetJobBookmarkRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_job_bookmark_response.GetJobBookmarkResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_job_bookmark

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_job_bookmark.async_get_job_bookmark(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_job_bookmark_request.GetJobBookmarkRequest = {}  # type: ignore[typeddict-item]
        input_["job_name"] = job_name
        if run_id is not None:
            input_["run_id"] = run_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_job_run(
        self,
        job_name: "aws_sdk_glue.types.name_string.NameString",
        run_id: "aws_sdk_glue.types.id_string.IdString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        predecessors_included: Optional[
            "aws_sdk_glue.types.boolean_value.BooleanValue"
        ] = None,
    ) -> "aws_sdk_glue.types.get_job_run_response.GetJobRunResponse":
        """<p>Retrieves the metadata for a given job run. Job run history is accessible for 365 days for your workflow and job run.</p>

        Args:
            job_name: <p>Name of the job definition being run.</p>
            run_id: <p>The ID of the job run.</p>
            predecessors_included: <p>True if a list of predecessor runs should be returned.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_job_run_request.GetJobRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_job_run_response.GetJobRunResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_job_run

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_job_run.async_get_job_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_job_run_request.GetJobRunRequest = {}  # type: ignore[typeddict-item]
        input_["job_name"] = job_name
        input_["run_id"] = run_id
        if predecessors_included is not None:
            input_["predecessors_included"] = predecessors_included

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_job_runs(
        self,
        job_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        next_token: Optional["aws_sdk_glue.types.generic_string.GenericString"] = None,
        max_results: Optional[
            "aws_sdk_glue.types.orchestration_page_size200.OrchestrationPageSize200"
        ] = None,
    ) -> "aws_sdk_glue.types.get_job_runs_response.GetJobRunsResponse":
        """<p>Retrieves metadata for all runs of a given job definition.</p> <p> <code>GetJobRuns</code> returns the job runs in chronological order, with the newest jobs returned first.</p>

        Args:
            job_name: <p>The name of the job definition for which to retrieve all job runs.</p>
            next_token: <p>A continuation token, if this is a continuation call.</p>
            max_results: <p>The maximum size of the response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_job_runs_request.GetJobRunsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_job_runs_response.GetJobRunsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_job_runs

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_job_runs.async_get_job_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_job_runs_request.GetJobRunsRequest = {}  # type: ignore[typeddict-item]
        input_["job_name"] = job_name
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

    async def iter_get_job_runs(
        self,
        job_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        next_token: Optional["aws_sdk_glue.types.generic_string.GenericString"] = None,
        max_results: Optional[
            "aws_sdk_glue.types.orchestration_page_size200.OrchestrationPageSize200"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_glue.types.job_run.JobRun]":
        _token = next_token
        while True:
            _response = await self.get_job_runs(
                job_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("job_runs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_jobs(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        next_token: Optional["aws_sdk_glue.types.generic_string.GenericString"] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
    ) -> "aws_sdk_glue.types.get_jobs_response.GetJobsResponse":
        """<p>Retrieves all current job definitions.</p>

        Args:
            next_token: <p>A continuation token, if this is a continuation call.</p>
            max_results: <p>The maximum size of the response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_jobs_request.GetJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_jobs_response.GetJobsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_jobs.async_get_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_jobs_request.GetJobsRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_get_jobs(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        next_token: Optional["aws_sdk_glue.types.generic_string.GenericString"] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
    ) -> "AsyncIterator[aws_sdk_glue.types.job.Job]":
        _token = next_token
        while True:
            _response = await self.get_jobs(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_mapping(
        self,
        source: "aws_sdk_glue.types.catalog_entry.CatalogEntry",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        sinks: Optional["aws_sdk_glue.types.catalog_entries.CatalogEntries"] = None,
        location: Optional["aws_sdk_glue.types.location.Location"] = None,
    ) -> "aws_sdk_glue.types.get_mapping_response.GetMappingResponse":
        """<p>Creates mappings.</p>

        Args:
            source: <p>Specifies the source table.</p>
            sinks: <p>A list of target tables.</p>
            location: <p>Parameters for the mapping.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_mapping_request.GetMappingRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_mapping_response.GetMappingResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_mapping

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_mapping.async_get_mapping(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_mapping_request.GetMappingRequest = {}  # type: ignore[typeddict-item]
        input_["source"] = source
        if sinks is not None:
            input_["sinks"] = sinks
        if location is not None:
            input_["location"] = location

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_materialized_view_refresh_task_run(
        self,
        catalog_id: "aws_sdk_glue.types.name_string.NameString",
        materialized_view_refresh_task_run_id: "aws_sdk_glue.types.uui_dv4.UUIDv4",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.get_materialized_view_refresh_task_run_response.GetMaterializedViewRefreshTaskRunResponse":
        """<p>Get the associated metadata/information for a task run, given a task run ID.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog where the table resides. If none is supplied, the account ID is used by default.</p>
            materialized_view_refresh_task_run_id: <p>The identifier for the particular materialized view refresh task run.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_materialized_view_refresh_task_run_request.GetMaterializedViewRefreshTaskRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_materialized_view_refresh_task_run_response.GetMaterializedViewRefreshTaskRunResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_materialized_view_refresh_task_run

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_materialized_view_refresh_task_run.async_get_materialized_view_refresh_task_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_materialized_view_refresh_task_run_request.GetMaterializedViewRefreshTaskRunRequest = {}  # type: ignore[typeddict-item]
        input_["catalog_id"] = catalog_id
        input_["materialized_view_refresh_task_run_id"] = (
            materialized_view_refresh_task_run_id
        )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_ml_task_run(
        self,
        transform_id: "aws_sdk_glue.types.hash_string.HashString",
        task_run_id: "aws_sdk_glue.types.hash_string.HashString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.get_ml_task_run_response.GetMLTaskRunResponse":
        """<p>Gets details for a specific task run on a machine learning transform. Machine learning task runs are asynchronous tasks that Glue runs on your behalf as part of various machine learning workflows. You can check the stats of any task run by calling <code>GetMLTaskRun</code> with the <code>TaskRunID</code> and its parent transform's <code>TransformID</code>.</p>

        Args:
            transform_id: <p>The unique identifier of the machine learning transform.</p>
            task_run_id: <p>The unique identifier of the task run.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_ml_task_run_request.GetMLTaskRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_ml_task_run_response.GetMLTaskRunResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_ml_task_run

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_ml_task_run.async_get_ml_task_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_ml_task_run_request.GetMLTaskRunRequest = {}  # type: ignore[typeddict-item]
        input_["transform_id"] = transform_id
        input_["task_run_id"] = task_run_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_ml_task_runs(
        self,
        transform_id: "aws_sdk_glue.types.hash_string.HashString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        next_token: Optional[
            "aws_sdk_glue.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
        filter: Optional[
            "aws_sdk_glue.types.task_run_filter_criteria.TaskRunFilterCriteria"
        ] = None,
        sort: Optional[
            "aws_sdk_glue.types.task_run_sort_criteria.TaskRunSortCriteria"
        ] = None,
    ) -> "aws_sdk_glue.types.get_ml_task_runs_response.GetMLTaskRunsResponse":
        """<p>Gets a list of runs for a machine learning transform. Machine learning task runs are asynchronous tasks that Glue runs on your behalf as part of various machine learning workflows. You can get a sortable, filterable list of machine learning task runs by calling <code>GetMLTaskRuns</code> with their parent transform's <code>TransformID</code> and other optional parameters as documented in this section.</p> <p>This operation returns a list of historic runs and must be paginated.</p>

        Args:
            transform_id: <p>The unique identifier of the machine learning transform.</p>
            next_token: <p>A token for pagination of the results. The default is empty.</p>
            max_results: <p>The maximum number of results to return. </p>
            filter: <p>The filter criteria, in the <code>TaskRunFilterCriteria</code> structure, for the task run.</p>
            sort: <p>The sorting criteria, in the <code>TaskRunSortCriteria</code> structure, for the task run.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_ml_task_runs_request.GetMLTaskRunsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_ml_task_runs_response.GetMLTaskRunsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_ml_task_runs

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_ml_task_runs.async_get_ml_task_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_ml_task_runs_request.GetMLTaskRunsRequest = {}  # type: ignore[typeddict-item]
        input_["transform_id"] = transform_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter
        if sort is not None:
            input_["sort"] = sort

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_ml_transform(
        self,
        transform_id: "aws_sdk_glue.types.hash_string.HashString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.get_ml_transform_response.GetMLTransformResponse":
        """<p>Gets an Glue machine learning transform artifact and all its corresponding metadata. Machine learning transforms are a special type of transform that use machine learning to learn the details of the transformation to be performed by learning from examples provided by humans. These transformations are then saved by Glue. You can retrieve their metadata by calling <code>GetMLTransform</code>.</p>

        Args:
            transform_id: <p>The unique identifier of the transform, generated at the time that the transform was created.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_ml_transform_request.GetMLTransformRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_ml_transform_response.GetMLTransformResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_ml_transform

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_ml_transform.async_get_ml_transform(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_ml_transform_request.GetMLTransformRequest = {}  # type: ignore[typeddict-item]
        input_["transform_id"] = transform_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_ml_transforms(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        next_token: Optional[
            "aws_sdk_glue.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
        filter: Optional[
            "aws_sdk_glue.types.transform_filter_criteria.TransformFilterCriteria"
        ] = None,
        sort: Optional[
            "aws_sdk_glue.types.transform_sort_criteria.TransformSortCriteria"
        ] = None,
    ) -> "aws_sdk_glue.types.get_ml_transforms_response.GetMLTransformsResponse":
        """<p>Gets a sortable, filterable list of existing Glue machine learning transforms. Machine learning transforms are a special type of transform that use machine learning to learn the details of the transformation to be performed by learning from examples provided by humans. These transformations are then saved by Glue, and you can retrieve their metadata by calling <code>GetMLTransforms</code>.</p>

        Args:
            next_token: <p>A paginated token to offset the results.</p>
            max_results: <p>The maximum number of results to return.</p>
            filter: <p>The filter transformation criteria.</p>
            sort: <p>The sorting criteria.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_ml_transforms_request.GetMLTransformsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_ml_transforms_response.GetMLTransformsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_ml_transforms

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_ml_transforms.async_get_ml_transforms(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_ml_transforms_request.GetMLTransformsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter
        if sort is not None:
            input_["sort"] = sort

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_partition(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        partition_values: "aws_sdk_glue.types.value_string_list.ValueStringList",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
        audit_context: Optional["aws_sdk_glue.types.audit_context.AuditContext"] = None,
    ) -> "aws_sdk_glue.types.get_partition_response.GetPartitionResponse":
        """<p>Retrieves information about a specified partition.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog where the partition in question resides. If none is provided, the Amazon Web Services account ID is used by default.</p>
            database_name: <p>The name of the catalog database where the partition resides.</p>
            table_name: <p>The name of the partition's table.</p>
            partition_values: <p>The values that define the partition.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_partition_request.GetPartitionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_partition_response.GetPartitionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_partition

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_partition.async_get_partition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_partition_request.GetPartitionRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        input_["partition_values"] = partition_values
        if audit_context is not None:
            input_["audit_context"] = audit_context

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_partition_indexes(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
        next_token: Optional["aws_sdk_glue.types.token.Token"] = None,
    ) -> (
        "aws_sdk_glue.types.get_partition_indexes_response.GetPartitionIndexesResponse"
    ):
        """<p>Retrieves the partition indexes associated with a table.</p>

        Args:
            catalog_id: <p>The catalog ID where the table resides.</p>
            database_name: <p>Specifies the name of a database from which you want to retrieve partition indexes.</p>
            table_name: <p>Specifies the name of a table for which you want to retrieve the partition indexes.</p>
            next_token: <p>A continuation token, included if this is a continuation call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_partition_indexes_request.GetPartitionIndexesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_partition_indexes_response.GetPartitionIndexesResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_partition_indexes

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_partition_indexes.async_get_partition_indexes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_partition_indexes_request.GetPartitionIndexesRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_get_partition_indexes(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
        next_token: Optional["aws_sdk_glue.types.token.Token"] = None,
    ) -> "AsyncIterator[aws_sdk_glue.types.partition_index_descriptor.PartitionIndexDescriptor]":
        _token = next_token
        while True:
            _response = await self.get_partition_indexes(
                database_name,
                table_name,
                config_overrides=config_overrides,
                catalog_id=catalog_id,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("partition_index_descriptor_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_partitions(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
        expression: Optional[
            "aws_sdk_glue.types.predicate_string.PredicateString"
        ] = None,
        next_token: Optional["aws_sdk_glue.types.token.Token"] = None,
        segment: Optional["aws_sdk_glue.types.segment.Segment"] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
        exclude_column_schema: Optional[
            "aws_sdk_glue.types.boolean_nullable.BooleanNullable"
        ] = None,
        transaction_id: Optional[
            "aws_sdk_glue.types.transaction_id_string.TransactionIdString"
        ] = None,
        query_as_of_time: Optional["aws_sdk_glue.types.timestamp.Timestamp"] = None,
        audit_context: Optional["aws_sdk_glue.types.audit_context.AuditContext"] = None,
    ) -> "aws_sdk_glue.types.get_partitions_response.GetPartitionsResponse":
        r"""<p>Retrieves information about the partitions in a table.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog where the partitions in question reside. If none is provided, the Amazon Web Services account ID is used by default.</p>
            database_name: <p>The name of the catalog database where the partitions reside.</p>
            table_name: <p>The name of the partitions' table.</p>
            expression: <p>An expression that filters the partitions to be returned.</p> <p>The expression uses SQL syntax similar to the SQL <code>WHERE</code> filter clause. The SQL statement parser <a href=\"http://jsqlparser.sourceforge.net/home.php\">JSQLParser</a> parses the expression. </p> <p> <i>Operators</i>: The following are the operators that you can use in the <code>Expression</code> API call:</p> <dl> <dt>=</dt> <dd> <p>Checks whether the values of the two operands are equal; if yes, then the condition becomes true.</p> <p>Example: Assume 'variable a' holds 10 and 'variable b' holds 20. </p> <p>(a = b) is not true.</p> </dd> <dt>< ></dt> <dd> <p>Checks whether the values of two operands are equal; if the values are not equal, then the condition becomes true.</p> <p>Example: (a < > b) is true.</p> </dd> <dt>></dt> <dd> <p>Checks whether the value of the left operand is greater than the value of the right operand; if yes, then the condition becomes true.</p> <p>Example: (a > b) is not true.</p> </dd> <dt><</dt> <dd> <p>Checks whether the value of the left operand is less than the value of the right operand; if yes, then the condition becomes true.</p> <p>Example: (a < b) is true.</p> </dd> <dt>>=</dt> <dd> <p>Checks whether the value of the left operand is greater than or equal to the value of the right operand; if yes, then the condition becomes true.</p> <p>Example: (a >= b) is not true.</p> </dd> <dt><=</dt> <dd> <p>Checks whether the value of the left operand is less than or equal to the value of the right operand; if yes, then the condition becomes true.</p> <p>Example: (a <= b) is true.</p> </dd> <dt>AND, OR, IN, BETWEEN, LIKE, NOT, IS NULL</dt> <dd> <p>Logical operators.</p> </dd> </dl> <p> <i>Supported Partition Key Types</i>: The following are the supported partition keys.</p> <ul> <li> <p> <code>string</code> </p> </li> <li> <p> <code>date</code> </p> </li> <li> <p> <code>timestamp</code> </p> </li> <li> <p> <code>int</code> </p> </li> <li> <p> <code>bigint</code> </p> </li> <li> <p> <code>long</code> </p> </li> <li> <p> <code>tinyint</code> </p> </li> <li> <p> <code>smallint</code> </p> </li> <li> <p> <code>decimal</code> </p> </li> </ul> <p>If an type is encountered that is not valid, an exception is thrown. </p> <p>The following list shows the valid operators on each type. When you define a crawler, the <code>partitionKey</code> type is created as a <code>STRING</code>, to be compatible with the catalog partitions. </p> <p> <i>Sample API Call</i>: </p>
            next_token: <p>A continuation token, if this is not the first call to retrieve these partitions.</p>
            segment: <p>The segment of the table's partitions to scan in this request.</p>
            max_results: <p>The maximum number of partitions to return in a single response.</p>
            exclude_column_schema: <p>When true, specifies not returning the partition column schema. Useful when you are interested only in other partition attributes such as partition values or location. This approach avoids the problem of a large response by not returning duplicate data.</p>
            transaction_id: <p>The transaction ID at which to read the partition contents.</p>
            query_as_of_time: <p>The time as of when to read the partition contents. If not set, the most recent transaction commit time will be used. Cannot be specified along with <code>TransactionId</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_partitions_request.GetPartitionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_partitions_response.GetPartitionsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_partitions

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_partitions.async_get_partitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_partitions_request.GetPartitionsRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        if expression is not None:
            input_["expression"] = expression
        if next_token is not None:
            input_["next_token"] = next_token
        if segment is not None:
            input_["segment"] = segment
        if max_results is not None:
            input_["max_results"] = max_results
        if exclude_column_schema is not None:
            input_["exclude_column_schema"] = exclude_column_schema
        if transaction_id is not None:
            input_["transaction_id"] = transaction_id
        if query_as_of_time is not None:
            input_["query_as_of_time"] = query_as_of_time
        if audit_context is not None:
            input_["audit_context"] = audit_context

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_plan(
        self,
        mapping: "aws_sdk_glue.types.mapping_list.MappingList",
        source: "aws_sdk_glue.types.catalog_entry.CatalogEntry",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        sinks: Optional["aws_sdk_glue.types.catalog_entries.CatalogEntries"] = None,
        location: Optional["aws_sdk_glue.types.location.Location"] = None,
        language: Optional["aws_sdk_glue.types.language.Language"] = None,
        additional_plan_options_map: Optional[
            "aws_sdk_glue.types.additional_plan_options_map.AdditionalPlanOptionsMap"
        ] = None,
    ) -> "aws_sdk_glue.types.get_plan_response.GetPlanResponse":
        r"""<p>Gets code to perform a specified mapping.</p>

        Args:
            mapping: <p>The list of mappings from a source table to target tables.</p>
            source: <p>The source table.</p>
            sinks: <p>The target tables.</p>
            location: <p>The parameters for the mapping.</p>
            language: <p>The programming language of the code to perform the mapping.</p>
            additional_plan_options_map: <p>A map to hold additional optional key-value parameters.</p> <p>Currently, these key-value pairs are supported:</p> <ul> <li> <p> <code>inferSchema</code> — Specifies whether to set <code>inferSchema</code> to true or false for the default script generated by an Glue job. For example, to set <code>inferSchema</code> to true, pass the following key value pair:</p> <p> <code>--additional-plan-options-map '{\"inferSchema\":\"true\"}'</code> </p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_plan_request.GetPlanRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_plan_response.GetPlanResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_plan

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_plan.async_get_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_plan_request.GetPlanRequest = {}  # type: ignore[typeddict-item]
        input_["mapping"] = mapping
        input_["source"] = source
        if sinks is not None:
            input_["sinks"] = sinks
        if location is not None:
            input_["location"] = location
        if language is not None:
            input_["language"] = language
        if additional_plan_options_map is not None:
            input_["additional_plan_options_map"] = additional_plan_options_map

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_registry(
        self,
        registry_id: "aws_sdk_glue.types.registry_id.RegistryId",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.get_registry_response.GetRegistryResponse":
        """<p>Describes the specified registry in detail.</p>

        Args:
            registry_id: <p>This is a wrapper structure that may contain the registry name and Amazon Resource Name (ARN).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_registry_input.GetRegistryInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_registry_response.GetRegistryResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_registry

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_registry.async_get_registry(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_registry_input.GetRegistryInput = {}  # type: ignore[typeddict-item]
        input_["registry_id"] = registry_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_resource_policies(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        next_token: Optional["aws_sdk_glue.types.token.Token"] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
    ) -> (
        "aws_sdk_glue.types.get_resource_policies_response.GetResourcePoliciesResponse"
    ):
        """<p>Retrieves the resource policies set on individual resources by Resource Access Manager during cross-account permission grants. Also retrieves the Data Catalog resource policy.</p> <p>If you enabled metadata encryption in Data Catalog settings, and you do not have permission on the KMS key, the operation can't return the Data Catalog resource policy.</p>

        Args:
            next_token: <p>A continuation token, if this is a continuation request.</p>
            max_results: <p>The maximum size of a list to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_resource_policies_request.GetResourcePoliciesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_resource_policies_response.GetResourcePoliciesResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_resource_policies

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_resource_policies.async_get_resource_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_resource_policies_request.GetResourcePoliciesRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_get_resource_policies(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        next_token: Optional["aws_sdk_glue.types.token.Token"] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
    ) -> "AsyncIterator[aws_sdk_glue.types.glue_policy.GluePolicy]":
        _token = next_token
        while True:
            _response = await self.get_resource_policies(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("get_resource_policies_response_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_resource_policy(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        resource_arn: Optional[
            "aws_sdk_glue.types.glue_resource_arn.GlueResourceArn"
        ] = None,
    ) -> "aws_sdk_glue.types.get_resource_policy_response.GetResourcePolicyResponse":
        r"""<p>Retrieves a specified resource policy.</p>

        Args:
            resource_arn: <p>The ARN of the Glue resource for which to retrieve the resource policy. If not supplied, the Data Catalog resource policy is returned. Use <code>GetResourcePolicies</code> to view all existing resource policies. For more information see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html\">Specifying Glue Resource ARNs</a>. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_resource_policy.async_get_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_resource_policy_request.GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_schema(
        self,
        schema_id: "aws_sdk_glue.types.schema_id.SchemaId",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.get_schema_response.GetSchemaResponse":
        """<p>Describes the specified schema in detail.</p>

        Args:
            schema_id: <p>This is a wrapper structure to contain schema identity fields. The structure contains:</p> <ul> <li> <p>SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. Either <code>SchemaArn</code> or <code>SchemaName</code> and <code>RegistryName</code> has to be provided.</p> </li> <li> <p>SchemaId$SchemaName: The name of the schema. Either <code>SchemaArn</code> or <code>SchemaName</code> and <code>RegistryName</code> has to be provided.</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_schema_input.GetSchemaInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_schema_response.GetSchemaResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_schema

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_schema.async_get_schema(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_schema_input.GetSchemaInput = {}  # type: ignore[typeddict-item]
        input_["schema_id"] = schema_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_schema_by_definition(
        self,
        schema_id: "aws_sdk_glue.types.schema_id.SchemaId",
        schema_definition: "aws_sdk_glue.types.schema_definition_string.SchemaDefinitionString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.get_schema_by_definition_response.GetSchemaByDefinitionResponse":
        """<p>Retrieves a schema by the <code>SchemaDefinition</code>. The schema definition is sent to the Schema Registry, canonicalized, and hashed. If the hash is matched within the scope of the <code>SchemaName</code> or ARN (or the default registry, if none is supplied), that schema’s metadata is returned. Otherwise, a 404 or NotFound error is returned. Schema versions in <code>Deleted</code> statuses will not be included in the results.</p>

        Args:
            schema_id: <p>This is a wrapper structure to contain schema identity fields. The structure contains:</p> <ul> <li> <p>SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. One of <code>SchemaArn</code> or <code>SchemaName</code> has to be provided.</p> </li> <li> <p>SchemaId$SchemaName: The name of the schema. One of <code>SchemaArn</code> or <code>SchemaName</code> has to be provided.</p> </li> </ul>
            schema_definition: <p>The definition of the schema for which schema details are required.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_schema_by_definition_input.GetSchemaByDefinitionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_schema_by_definition_response.GetSchemaByDefinitionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_schema_by_definition

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_schema_by_definition.async_get_schema_by_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_schema_by_definition_input.GetSchemaByDefinitionInput = {}  # type: ignore[typeddict-item]
        input_["schema_id"] = schema_id
        input_["schema_definition"] = schema_definition

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_schema_version(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        schema_id: Optional["aws_sdk_glue.types.schema_id.SchemaId"] = None,
        schema_version_id: Optional[
            "aws_sdk_glue.types.schema_version_id_string.SchemaVersionIdString"
        ] = None,
        schema_version_number: Optional[
            "aws_sdk_glue.types.schema_version_number.SchemaVersionNumber"
        ] = None,
    ) -> "aws_sdk_glue.types.get_schema_version_response.GetSchemaVersionResponse":
        """<p>Get the specified schema by its unique ID assigned when a version of the schema is created or registered. Schema versions in Deleted status will not be included in the results.</p>

        Args:
            schema_id: <p>This is a wrapper structure to contain schema identity fields. The structure contains:</p> <ul> <li> <p>SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. Either <code>SchemaArn</code> or <code>SchemaName</code> and <code>RegistryName</code> has to be provided.</p> </li> <li> <p>SchemaId$SchemaName: The name of the schema. Either <code>SchemaArn</code> or <code>SchemaName</code> and <code>RegistryName</code> has to be provided.</p> </li> </ul>
            schema_version_id: <p>The <code>SchemaVersionId</code> of the schema version. This field is required for fetching by schema ID. Either this or the <code>SchemaId</code> wrapper has to be provided.</p>
            schema_version_number: <p>The version number of the schema.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_schema_version_input.GetSchemaVersionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_schema_version_response.GetSchemaVersionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_schema_version

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_schema_version.async_get_schema_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_schema_version_input.GetSchemaVersionInput = {}  # type: ignore[typeddict-item]
        if schema_id is not None:
            input_["schema_id"] = schema_id
        if schema_version_id is not None:
            input_["schema_version_id"] = schema_version_id
        if schema_version_number is not None:
            input_["schema_version_number"] = schema_version_number

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_schema_versions_diff(
        self,
        schema_id: "aws_sdk_glue.types.schema_id.SchemaId",
        first_schema_version_number: "aws_sdk_glue.types.schema_version_number.SchemaVersionNumber",
        second_schema_version_number: "aws_sdk_glue.types.schema_version_number.SchemaVersionNumber",
        schema_diff_type: "aws_sdk_glue.types.schema_diff_type.SchemaDiffType",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.get_schema_versions_diff_response.GetSchemaVersionsDiffResponse":
        """<p>Fetches the schema version difference in the specified difference type between two stored schema versions in the Schema Registry.</p> <p>This API allows you to compare two schema versions between two schema definitions under the same schema.</p>

        Args:
            schema_id: <p>This is a wrapper structure to contain schema identity fields. The structure contains:</p> <ul> <li> <p>SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. One of <code>SchemaArn</code> or <code>SchemaName</code> has to be provided.</p> </li> <li> <p>SchemaId$SchemaName: The name of the schema. One of <code>SchemaArn</code> or <code>SchemaName</code> has to be provided.</p> </li> </ul>
            first_schema_version_number: <p>The first of the two schema versions to be compared.</p>
            second_schema_version_number: <p>The second of the two schema versions to be compared.</p>
            schema_diff_type: <p>Refers to <code>SYNTAX_DIFF</code>, which is the currently supported diff type.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_schema_versions_diff_input.GetSchemaVersionsDiffInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_schema_versions_diff_response.GetSchemaVersionsDiffResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_schema_versions_diff

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_schema_versions_diff.async_get_schema_versions_diff(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_schema_versions_diff_input.GetSchemaVersionsDiffInput = {}  # type: ignore[typeddict-item]
        input_["schema_id"] = schema_id
        input_["first_schema_version_number"] = first_schema_version_number
        input_["second_schema_version_number"] = second_schema_version_number
        input_["schema_diff_type"] = schema_diff_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_security_configuration(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.get_security_configuration_response.GetSecurityConfigurationResponse":
        """<p>Retrieves a specified security configuration.</p>

        Args:
            name: <p>The name of the security configuration to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_security_configuration_request.GetSecurityConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_security_configuration_response.GetSecurityConfigurationResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_security_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_security_configuration.async_get_security_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_security_configuration_request.GetSecurityConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_security_configurations(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
        next_token: Optional["aws_sdk_glue.types.generic_string.GenericString"] = None,
    ) -> "aws_sdk_glue.types.get_security_configurations_response.GetSecurityConfigurationsResponse":
        """<p>Retrieves a list of all security configurations.</p>

        Args:
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A continuation token, if this is a continuation call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_security_configurations_request.GetSecurityConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_security_configurations_response.GetSecurityConfigurationsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_security_configurations

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_security_configurations.async_get_security_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_security_configurations_request.GetSecurityConfigurationsRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_get_security_configurations(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
        next_token: Optional["aws_sdk_glue.types.generic_string.GenericString"] = None,
    ) -> (
        "AsyncIterator[aws_sdk_glue.types.security_configuration.SecurityConfiguration]"
    ):
        _token = next_token
        while True:
            _response = await self.get_security_configurations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("security_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_session(
        self,
        id: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        request_origin: Optional[
            "aws_sdk_glue.types.orchestration_name_string.OrchestrationNameString"
        ] = None,
    ) -> "aws_sdk_glue.types.get_session_response.GetSessionResponse":
        """<p>Retrieves the session.</p>

        Args:
            id: <p>The ID of the session. </p>
            request_origin: <p>The origin of the request. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_session_request.GetSessionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_session_response.GetSessionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_session

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_session.async_get_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_session_request.GetSessionRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if request_origin is not None:
            input_["request_origin"] = request_origin

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_session_endpoint(
        self,
        session_id: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.get_session_endpoint_response.GetSessionEndpointResponse":
        """<p>Returns the Spark Connect endpoint URL and authentication token for an interactive session.</p>

        Args:
            session_id: <p>The unique identifier of the interactive session.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_session_endpoint_request.GetSessionEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_session_endpoint_response.GetSessionEndpointResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_session_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_session_endpoint.async_get_session_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_session_endpoint_request.GetSessionEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["session_id"] = session_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_statement(
        self,
        session_id: "aws_sdk_glue.types.name_string.NameString",
        id: "aws_sdk_glue.types.integer_value.IntegerValue",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        request_origin: Optional[
            "aws_sdk_glue.types.orchestration_name_string.OrchestrationNameString"
        ] = None,
    ) -> "aws_sdk_glue.types.get_statement_response.GetStatementResponse":
        """<p>Retrieves the statement.</p>

        Args:
            session_id: <p>The Session ID of the statement.</p>
            id: <p>The Id of the statement.</p>
            request_origin: <p>The origin of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_statement_request.GetStatementRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_statement_response.GetStatementResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_statement

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_statement.async_get_statement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_statement_request.GetStatementRequest = {}  # type: ignore[typeddict-item]
        input_["session_id"] = session_id
        input_["id"] = id
        if request_origin is not None:
            input_["request_origin"] = request_origin

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_table(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
        transaction_id: Optional[
            "aws_sdk_glue.types.transaction_id_string.TransactionIdString"
        ] = None,
        query_as_of_time: Optional["aws_sdk_glue.types.timestamp.Timestamp"] = None,
        audit_context: Optional["aws_sdk_glue.types.audit_context.AuditContext"] = None,
        include_status_details: Optional[
            "aws_sdk_glue.types.boolean_nullable.BooleanNullable"
        ] = None,
    ) -> "aws_sdk_glue.types.get_table_response.GetTableResponse":
        r"""<p>Retrieves the <code>Table</code> definition in a Data Catalog for a specified table.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog where the table resides. If none is provided, the Amazon Web Services account ID is used by default.</p>
            database_name: <p>The name of the database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase.</p>
            name: <p>The name of the table for which to retrieve the definition. For Hive compatibility, this name is entirely lowercase.</p>
            transaction_id: <p>The transaction ID at which to read the table contents. </p>
            query_as_of_time: <p>The time as of when to read the table contents. If not set, the most recent transaction commit time will be used. Cannot be specified along with <code>TransactionId</code>.</p>
            audit_context: <p>A structure containing the Lake Formation <a href=\"https://docs.aws.amazon.com/glue/latest/webapi/API_AuditContext.html\">audit context</a>.</p>
            include_status_details: <p>Specifies whether to include status details related to a request to create or update an Glue Data Catalog view.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_table_request.GetTableRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_table_response.GetTableResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_table

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_table.async_get_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_table_request.GetTableRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["name"] = name
        if transaction_id is not None:
            input_["transaction_id"] = transaction_id
        if query_as_of_time is not None:
            input_["query_as_of_time"] = query_as_of_time
        if audit_context is not None:
            input_["audit_context"] = audit_context
        if include_status_details is not None:
            input_["include_status_details"] = include_status_details

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_table_optimizer(
        self,
        catalog_id: "aws_sdk_glue.types.catalog_id_string.CatalogIdString",
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        type: "aws_sdk_glue.types.table_optimizer_type.TableOptimizerType",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.get_table_optimizer_response.GetTableOptimizerResponse":
        """<p>Returns the configuration of all optimizers associated with a specified table.</p>

        Args:
            catalog_id: <p>The Catalog ID of the table.</p>
            database_name: <p>The name of the database in the catalog in which the table resides.</p>
            table_name: <p>The name of the table.</p>
            type: <p>The type of table optimizer.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_table_optimizer_request.GetTableOptimizerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_table_optimizer_response.GetTableOptimizerResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_table_optimizer

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_table_optimizer.async_get_table_optimizer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_table_optimizer_request.GetTableOptimizerRequest = {}  # type: ignore[typeddict-item]
        input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        input_["type"] = type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_tables(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
        expression: Optional["aws_sdk_glue.types.filter_string.FilterString"] = None,
        next_token: Optional["aws_sdk_glue.types.token.Token"] = None,
        max_results: Optional[
            "aws_sdk_glue.types.catalog_getter_page_size.CatalogGetterPageSize"
        ] = None,
        transaction_id: Optional[
            "aws_sdk_glue.types.transaction_id_string.TransactionIdString"
        ] = None,
        query_as_of_time: Optional["aws_sdk_glue.types.timestamp.Timestamp"] = None,
        audit_context: Optional["aws_sdk_glue.types.audit_context.AuditContext"] = None,
        include_status_details: Optional[
            "aws_sdk_glue.types.boolean_nullable.BooleanNullable"
        ] = None,
        attributes_to_get: Optional[
            "aws_sdk_glue.types.table_attributes_list.TableAttributesList"
        ] = None,
    ) -> "aws_sdk_glue.types.get_tables_response.GetTablesResponse":
        r"""<p>Retrieves the definitions of some or all of the tables in a given <code>Database</code>.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog where the tables reside. If none is provided, the Amazon Web Services account ID is used by default.</p>
            database_name: <p>The database in the catalog whose tables to list. For Hive compatibility, this name is entirely lowercase.</p>
            expression: <p>A regular expression pattern. If present, only those tables whose names match the pattern are returned.</p>
            next_token: <p>A continuation token, included if this is a continuation call.</p>
            max_results: <p>The maximum number of tables to return in a single response.</p>
            transaction_id: <p>The transaction ID at which to read the table contents.</p>
            query_as_of_time: <p>The time as of when to read the table contents. If not set, the most recent transaction commit time will be used. Cannot be specified along with <code>TransactionId</code>.</p>
            audit_context: <p>A structure containing the Lake Formation <a href=\"https://docs.aws.amazon.com/glue/latest/webapi/API_AuditContext.html\">audit context</a>.</p>
            include_status_details: <p>Specifies whether to include status details related to a request to create or update an Glue Data Catalog view.</p>
            attributes_to_get: <p> Specifies the table fields returned by the <code>GetTables</code> call. This parameter doesn’t accept an empty list. The request must include <code>NAME</code>.</p> <p>The following are the valid combinations of values:</p> <ul> <li> <p> <code>NAME</code> - Names of all tables in the database.</p> </li> <li> <p> <code>NAME</code>, <code>TABLE_TYPE</code> - Names of all tables and the table types.</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_tables_request.GetTablesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_tables_response.GetTablesResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_tables

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_tables.async_get_tables(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_tables_request.GetTablesRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        if expression is not None:
            input_["expression"] = expression
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if transaction_id is not None:
            input_["transaction_id"] = transaction_id
        if query_as_of_time is not None:
            input_["query_as_of_time"] = query_as_of_time
        if audit_context is not None:
            input_["audit_context"] = audit_context
        if include_status_details is not None:
            input_["include_status_details"] = include_status_details
        if attributes_to_get is not None:
            input_["attributes_to_get"] = attributes_to_get

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_table_version(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
        version_id: Optional["aws_sdk_glue.types.version_string.VersionString"] = None,
        audit_context: Optional["aws_sdk_glue.types.audit_context.AuditContext"] = None,
    ) -> "aws_sdk_glue.types.get_table_version_response.GetTableVersionResponse":
        """<p>Retrieves a specified version of a table.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog where the tables reside. If none is provided, the Amazon Web Services account ID is used by default.</p>
            database_name: <p>The database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase.</p>
            table_name: <p>The name of the table. For Hive compatibility, this name is entirely lowercase.</p>
            version_id: <p>The ID value of the table version to be retrieved. A <code>VersionID</code> is a string representation of an integer. Each version is incremented by 1. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_table_version_request.GetTableVersionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_table_version_response.GetTableVersionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_table_version

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_table_version.async_get_table_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_table_version_request.GetTableVersionRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        if version_id is not None:
            input_["version_id"] = version_id
        if audit_context is not None:
            input_["audit_context"] = audit_context

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_table_versions(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
        next_token: Optional["aws_sdk_glue.types.token.Token"] = None,
        max_results: Optional[
            "aws_sdk_glue.types.catalog_getter_page_size.CatalogGetterPageSize"
        ] = None,
        audit_context: Optional["aws_sdk_glue.types.audit_context.AuditContext"] = None,
    ) -> "aws_sdk_glue.types.get_table_versions_response.GetTableVersionsResponse":
        """<p>Retrieves a list of strings that identify available versions of a specified table.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog where the tables reside. If none is provided, the Amazon Web Services account ID is used by default.</p>
            database_name: <p>The database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase.</p>
            table_name: <p>The name of the table. For Hive compatibility, this name is entirely lowercase.</p>
            next_token: <p>A continuation token, if this is not the first call.</p>
            max_results: <p>The maximum number of table versions to return in one response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_table_versions_request.GetTableVersionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_table_versions_response.GetTableVersionsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_table_versions

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_table_versions.async_get_table_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_table_versions_request.GetTableVersionsRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if audit_context is not None:
            input_["audit_context"] = audit_context

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_tags(
        self,
        resource_arn: "aws_sdk_glue.types.glue_resource_arn.GlueResourceArn",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.get_tags_response.GetTagsResponse":
        """<p>Retrieves a list of tags associated with a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which to retrieve tags.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_tags_request.GetTagsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_tags_response.GetTagsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_tags

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_tags.async_get_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_tags_request.GetTagsRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_trigger(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.get_trigger_response.GetTriggerResponse":
        """<p>Retrieves the definition of a trigger.</p>

        Args:
            name: <p>The name of the trigger to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_trigger_request.GetTriggerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_trigger_response.GetTriggerResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_trigger

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_trigger.async_get_trigger(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_trigger_request.GetTriggerRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_triggers(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        next_token: Optional["aws_sdk_glue.types.generic_string.GenericString"] = None,
        dependent_job_name: Optional[
            "aws_sdk_glue.types.name_string.NameString"
        ] = None,
        max_results: Optional[
            "aws_sdk_glue.types.orchestration_page_size200.OrchestrationPageSize200"
        ] = None,
    ) -> "aws_sdk_glue.types.get_triggers_response.GetTriggersResponse":
        """<p>Gets all the triggers associated with a job.</p>

        Args:
            next_token: <p>A continuation token, if this is a continuation call.</p>
            dependent_job_name: <p>The name of the job to retrieve triggers for. The trigger that can start this job is returned, and if there is no such trigger, all triggers are returned.</p>
            max_results: <p>The maximum size of the response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_triggers_request.GetTriggersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_triggers_response.GetTriggersResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_triggers

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_triggers.async_get_triggers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_triggers_request.GetTriggersRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if dependent_job_name is not None:
            input_["dependent_job_name"] = dependent_job_name
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_get_triggers(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        next_token: Optional["aws_sdk_glue.types.generic_string.GenericString"] = None,
        dependent_job_name: Optional[
            "aws_sdk_glue.types.name_string.NameString"
        ] = None,
        max_results: Optional[
            "aws_sdk_glue.types.orchestration_page_size200.OrchestrationPageSize200"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_glue.types.trigger.Trigger]":
        _token = next_token
        while True:
            _response = await self.get_triggers(
                config_overrides=config_overrides,
                next_token=_token,
                dependent_job_name=dependent_job_name,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("triggers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_unfiltered_partition_metadata(
        self,
        catalog_id: "aws_sdk_glue.types.catalog_id_string.CatalogIdString",
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        partition_values: "aws_sdk_glue.types.value_string_list.ValueStringList",
        supported_permission_types: "aws_sdk_glue.types.permission_type_list.PermissionTypeList",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        region: Optional["aws_sdk_glue.types.value_string.ValueString"] = None,
        audit_context: Optional["aws_sdk_glue.types.audit_context.AuditContext"] = None,
        query_session_context: Optional[
            "aws_sdk_glue.types.query_session_context.QuerySessionContext"
        ] = None,
    ) -> "aws_sdk_glue.types.get_unfiltered_partition_metadata_response.GetUnfilteredPartitionMetadataResponse":
        """<p>Retrieves partition metadata from the Data Catalog that contains unfiltered metadata.</p> <p>For IAM authorization, the public IAM action associated with this API is <code>glue:GetPartition</code>.</p>

        Args:
            region: <p>Specified only if the base tables belong to a different Amazon Web Services Region.</p>
            catalog_id: <p>The catalog ID where the partition resides.</p>
            database_name: <p>(Required) Specifies the name of a database that contains the partition.</p>
            table_name: <p>(Required) Specifies the name of a table that contains the partition.</p>
            partition_values: <p>(Required) A list of partition key values.</p>
            audit_context: <p>A structure containing Lake Formation audit context information.</p>
            supported_permission_types: <p>(Required) A list of supported permission types. </p>
            query_session_context: <p>A structure used as a protocol between query engines and Lake Formation or Glue. Contains both a Lake Formation generated authorization identifier and information from the request's authorization context.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_unfiltered_partition_metadata_request.GetUnfilteredPartitionMetadataRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_unfiltered_partition_metadata_response.GetUnfilteredPartitionMetadataResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_unfiltered_partition_metadata

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_unfiltered_partition_metadata.async_get_unfiltered_partition_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_unfiltered_partition_metadata_request.GetUnfilteredPartitionMetadataRequest = {}  # type: ignore[typeddict-item]
        if region is not None:
            input_["region"] = region
        input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        input_["partition_values"] = partition_values
        if audit_context is not None:
            input_["audit_context"] = audit_context
        input_["supported_permission_types"] = supported_permission_types
        if query_session_context is not None:
            input_["query_session_context"] = query_session_context

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_unfiltered_partitions_metadata(
        self,
        catalog_id: "aws_sdk_glue.types.catalog_id_string.CatalogIdString",
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        supported_permission_types: "aws_sdk_glue.types.permission_type_list.PermissionTypeList",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        region: Optional["aws_sdk_glue.types.value_string.ValueString"] = None,
        expression: Optional[
            "aws_sdk_glue.types.predicate_string.PredicateString"
        ] = None,
        audit_context: Optional["aws_sdk_glue.types.audit_context.AuditContext"] = None,
        next_token: Optional["aws_sdk_glue.types.token.Token"] = None,
        segment: Optional["aws_sdk_glue.types.segment.Segment"] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
        query_session_context: Optional[
            "aws_sdk_glue.types.query_session_context.QuerySessionContext"
        ] = None,
    ) -> "aws_sdk_glue.types.get_unfiltered_partitions_metadata_response.GetUnfilteredPartitionsMetadataResponse":
        r"""<p>Retrieves partition metadata from the Data Catalog that contains unfiltered metadata.</p> <p>For IAM authorization, the public IAM action associated with this API is <code>glue:GetPartitions</code>.</p>

        Args:
            region: <p>Specified only if the base tables belong to a different Amazon Web Services Region.</p>
            catalog_id: <p>The ID of the Data Catalog where the partitions in question reside. If none is provided, the AWS account ID is used by default. </p>
            database_name: <p>The name of the catalog database where the partitions reside.</p>
            table_name: <p>The name of the table that contains the partition.</p>
            expression: <p>An expression that filters the partitions to be returned.</p> <p>The expression uses SQL syntax similar to the SQL <code>WHERE</code> filter clause. The SQL statement parser <a href=\"http://jsqlparser.sourceforge.net/home.php\">JSQLParser</a> parses the expression. </p> <p> <i>Operators</i>: The following are the operators that you can use in the <code>Expression</code> API call:</p> <dl> <dt>=</dt> <dd> <p>Checks whether the values of the two operands are equal; if yes, then the condition becomes true.</p> <p>Example: Assume 'variable a' holds 10 and 'variable b' holds 20. </p> <p>(a = b) is not true.</p> </dd> <dt>< ></dt> <dd> <p>Checks whether the values of two operands are equal; if the values are not equal, then the condition becomes true.</p> <p>Example: (a < > b) is true.</p> </dd> <dt>></dt> <dd> <p>Checks whether the value of the left operand is greater than the value of the right operand; if yes, then the condition becomes true.</p> <p>Example: (a > b) is not true.</p> </dd> <dt><</dt> <dd> <p>Checks whether the value of the left operand is less than the value of the right operand; if yes, then the condition becomes true.</p> <p>Example: (a < b) is true.</p> </dd> <dt>>=</dt> <dd> <p>Checks whether the value of the left operand is greater than or equal to the value of the right operand; if yes, then the condition becomes true.</p> <p>Example: (a >= b) is not true.</p> </dd> <dt><=</dt> <dd> <p>Checks whether the value of the left operand is less than or equal to the value of the right operand; if yes, then the condition becomes true.</p> <p>Example: (a <= b) is true.</p> </dd> <dt>AND, OR, IN, BETWEEN, LIKE, NOT, IS NULL</dt> <dd> <p>Logical operators.</p> </dd> </dl> <p> <i>Supported Partition Key Types</i>: The following are the supported partition keys.</p> <ul> <li> <p> <code>string</code> </p> </li> <li> <p> <code>date</code> </p> </li> <li> <p> <code>timestamp</code> </p> </li> <li> <p> <code>int</code> </p> </li> <li> <p> <code>bigint</code> </p> </li> <li> <p> <code>long</code> </p> </li> <li> <p> <code>tinyint</code> </p> </li> <li> <p> <code>smallint</code> </p> </li> <li> <p> <code>decimal</code> </p> </li> </ul> <p>If an type is encountered that is not valid, an exception is thrown. </p>
            audit_context: <p>A structure containing Lake Formation audit context information.</p>
            supported_permission_types: <p>A list of supported permission types. </p>
            next_token: <p>A continuation token, if this is not the first call to retrieve these partitions.</p>
            segment: <p>The segment of the table's partitions to scan in this request.</p>
            max_results: <p>The maximum number of partitions to return in a single response.</p>
            query_session_context: <p>A structure used as a protocol between query engines and Lake Formation or Glue. Contains both a Lake Formation generated authorization identifier and information from the request's authorization context.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_unfiltered_partitions_metadata_request.GetUnfilteredPartitionsMetadataRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_unfiltered_partitions_metadata_response.GetUnfilteredPartitionsMetadataResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_unfiltered_partitions_metadata

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_unfiltered_partitions_metadata.async_get_unfiltered_partitions_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_unfiltered_partitions_metadata_request.GetUnfilteredPartitionsMetadataRequest = {}  # type: ignore[typeddict-item]
        if region is not None:
            input_["region"] = region
        input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        if expression is not None:
            input_["expression"] = expression
        if audit_context is not None:
            input_["audit_context"] = audit_context
        input_["supported_permission_types"] = supported_permission_types
        if next_token is not None:
            input_["next_token"] = next_token
        if segment is not None:
            input_["segment"] = segment
        if max_results is not None:
            input_["max_results"] = max_results
        if query_session_context is not None:
            input_["query_session_context"] = query_session_context

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_unfiltered_table_metadata(
        self,
        catalog_id: "aws_sdk_glue.types.catalog_id_string.CatalogIdString",
        database_name: "aws_sdk_glue.types.name_string.NameString",
        name: "aws_sdk_glue.types.name_string.NameString",
        supported_permission_types: "aws_sdk_glue.types.permission_type_list.PermissionTypeList",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        region: Optional["aws_sdk_glue.types.value_string.ValueString"] = None,
        audit_context: Optional["aws_sdk_glue.types.audit_context.AuditContext"] = None,
        parent_resource_arn: Optional["aws_sdk_glue.types.arn_string.ArnString"] = None,
        root_resource_arn: Optional["aws_sdk_glue.types.arn_string.ArnString"] = None,
        supported_dialect: Optional[
            "aws_sdk_glue.types.supported_dialect.SupportedDialect"
        ] = None,
        permissions: Optional[
            "aws_sdk_glue.types.permission_list.PermissionList"
        ] = None,
        query_session_context: Optional[
            "aws_sdk_glue.types.query_session_context.QuerySessionContext"
        ] = None,
    ) -> "aws_sdk_glue.types.get_unfiltered_table_metadata_response.GetUnfilteredTableMetadataResponse":
        """<p>Allows a third-party analytical engine to retrieve unfiltered table metadata from the Data Catalog.</p> <p>For IAM authorization, the public IAM action associated with this API is <code>glue:GetTable</code>.</p>

        Args:
            region: <p>Specified only if the base tables belong to a different Amazon Web Services Region.</p>
            catalog_id: <p>The catalog ID where the table resides.</p>
            database_name: <p>(Required) Specifies the name of a database that contains the table.</p>
            name: <p>(Required) Specifies the name of a table for which you are requesting metadata.</p>
            audit_context: <p>A structure containing Lake Formation audit context information.</p>
            supported_permission_types: <p>Indicates the level of filtering a third-party analytical engine is capable of enforcing when calling the <code>GetUnfilteredTableMetadata</code> API operation. Accepted values are:</p> <ul> <li> <p> <code>COLUMN_PERMISSION</code> - Column permissions ensure that users can access only specific columns in the table. If there are particular columns contain sensitive data, data lake administrators can define column filters that exclude access to specific columns.</p> </li> <li> <p> <code>CELL_FILTER_PERMISSION</code> - Cell-level filtering combines column filtering (include or exclude columns) and row filter expressions to restrict access to individual elements in the table.</p> </li> <li> <p> <code>NESTED_PERMISSION</code> - Nested permissions combines cell-level filtering and nested column filtering to restrict access to columns and/or nested columns in specific rows based on row filter expressions.</p> </li> <li> <p> <code>NESTED_CELL_PERMISSION</code> - Nested cell permissions combines nested permission with nested cell-level filtering. This allows different subsets of nested columns to be restricted based on an array of row filter expressions. </p> </li> </ul> <p>Note: Each of these permission types follows a hierarchical order where each subsequent permission type includes all permission of the previous type.</p> <p>Important: If you provide a supported permission type that doesn't match the user's level of permissions on the table, then Lake Formation raises an exception. For example, if the third-party engine calling the <code>GetUnfilteredTableMetadata</code> operation can enforce only column-level filtering, and the user has nested cell filtering applied on the table, Lake Formation throws an exception, and will not return unfiltered table metadata and data access credentials.</p>
            parent_resource_arn: <p>The resource ARN of the view.</p>
            root_resource_arn: <p>The resource ARN of the root view in a chain of nested views.</p>
            supported_dialect: <p>A structure specifying the dialect and dialect version used by the query engine.</p>
            permissions: <p>The Lake Formation data permissions of the caller on the table. Used to authorize the call when no view context is found.</p>
            query_session_context: <p>A structure used as a protocol between query engines and Lake Formation or Glue. Contains both a Lake Formation generated authorization identifier and information from the request's authorization context.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_unfiltered_table_metadata_request.GetUnfilteredTableMetadataRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_unfiltered_table_metadata_response.GetUnfilteredTableMetadataResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_unfiltered_table_metadata

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_unfiltered_table_metadata.async_get_unfiltered_table_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_unfiltered_table_metadata_request.GetUnfilteredTableMetadataRequest = {}  # type: ignore[typeddict-item]
        if region is not None:
            input_["region"] = region
        input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["name"] = name
        if audit_context is not None:
            input_["audit_context"] = audit_context
        input_["supported_permission_types"] = supported_permission_types
        if parent_resource_arn is not None:
            input_["parent_resource_arn"] = parent_resource_arn
        if root_resource_arn is not None:
            input_["root_resource_arn"] = root_resource_arn
        if supported_dialect is not None:
            input_["supported_dialect"] = supported_dialect
        if permissions is not None:
            input_["permissions"] = permissions
        if query_session_context is not None:
            input_["query_session_context"] = query_session_context

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_usage_profile(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.get_usage_profile_response.GetUsageProfileResponse":
        """<p>Retrieves information about the specified Glue usage profile.</p>

        Args:
            name: <p>The name of the usage profile to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_usage_profile_request.GetUsageProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_usage_profile_response.GetUsageProfileResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_usage_profile

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_usage_profile.async_get_usage_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_usage_profile_request.GetUsageProfileRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_user_defined_function(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        function_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.get_user_defined_function_response.GetUserDefinedFunctionResponse":
        """<p>Retrieves a specified function definition from the Data Catalog.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog where the function to be retrieved is located. If none is provided, the Amazon Web Services account ID is used by default.</p>
            database_name: <p>The name of the catalog database where the function is located.</p>
            function_name: <p>The name of the function.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_user_defined_function_request.GetUserDefinedFunctionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_user_defined_function_response.GetUserDefinedFunctionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_user_defined_function

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_user_defined_function.async_get_user_defined_function(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_user_defined_function_request.GetUserDefinedFunctionRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["function_name"] = function_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_user_defined_functions(
        self,
        pattern: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
        database_name: Optional["aws_sdk_glue.types.name_string.NameString"] = None,
        function_type: Optional["aws_sdk_glue.types.function_type.FunctionType"] = None,
        next_token: Optional["aws_sdk_glue.types.token.Token"] = None,
        max_results: Optional[
            "aws_sdk_glue.types.catalog_getter_page_size.CatalogGetterPageSize"
        ] = None,
    ) -> "aws_sdk_glue.types.get_user_defined_functions_response.GetUserDefinedFunctionsResponse":
        """<p>Retrieves multiple function definitions from the Data Catalog.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog where the functions to be retrieved are located. If none is provided, the Amazon Web Services account ID is used by default.</p>
            database_name: <p>The name of the catalog database where the functions are located. If none is provided, functions from all the databases across the catalog will be returned.</p>
            pattern: <p>An optional function-name pattern string that filters the function definitions returned.</p>
            function_type: <p>An optional function-type pattern string that filters the function definitions returned from Amazon Redshift Federated Permissions Catalog.</p> <p>Specify a value of <code>REGULAR_FUNCTION</code> or <code>STORED_PROCEDURE</code>. The <code>STORED_PROCEDURE</code> function type is only compatible with Amazon Redshift Federated Permissions Catalog. </p>
            next_token: <p>A continuation token, if this is a continuation call.</p>
            max_results: <p>The maximum number of functions to return in one response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_user_defined_functions_request.GetUserDefinedFunctionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_user_defined_functions_response.GetUserDefinedFunctionsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_user_defined_functions

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_user_defined_functions.async_get_user_defined_functions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_user_defined_functions_request.GetUserDefinedFunctionsRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        if database_name is not None:
            input_["database_name"] = database_name
        input_["pattern"] = pattern
        if function_type is not None:
            input_["function_type"] = function_type
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

    async def get_workflow(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        include_graph: Optional[
            "aws_sdk_glue.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "aws_sdk_glue.types.get_workflow_response.GetWorkflowResponse":
        """<p>Retrieves resource metadata for a workflow.</p>

        Args:
            name: <p>The name of the workflow to retrieve.</p>
            include_graph: <p>Specifies whether to include a graph when returning the workflow resource metadata.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_workflow_request.GetWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_workflow_response.GetWorkflowResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_workflow

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_workflow.async_get_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_workflow_request.GetWorkflowRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if include_graph is not None:
            input_["include_graph"] = include_graph

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_workflow_run(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        run_id: "aws_sdk_glue.types.id_string.IdString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        include_graph: Optional[
            "aws_sdk_glue.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "aws_sdk_glue.types.get_workflow_run_response.GetWorkflowRunResponse":
        """<p>Retrieves the metadata for a given workflow run. Job run history is accessible for 90 days for your workflow and job run.</p>

        Args:
            name: <p>Name of the workflow being run.</p>
            run_id: <p>The ID of the workflow run.</p>
            include_graph: <p>Specifies whether to include the workflow graph in response or not.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_workflow_run_request.GetWorkflowRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_workflow_run_response.GetWorkflowRunResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_workflow_run

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_workflow_run.async_get_workflow_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_workflow_run_request.GetWorkflowRunRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["run_id"] = run_id
        if include_graph is not None:
            input_["include_graph"] = include_graph

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_workflow_run_properties(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        run_id: "aws_sdk_glue.types.id_string.IdString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.get_workflow_run_properties_response.GetWorkflowRunPropertiesResponse":
        """<p>Retrieves the workflow run properties which were set during the run.</p>

        Args:
            name: <p>Name of the workflow which was run.</p>
            run_id: <p>The ID of the workflow run whose run properties should be returned.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_workflow_run_properties_request.GetWorkflowRunPropertiesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_workflow_run_properties_response.GetWorkflowRunPropertiesResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_workflow_run_properties

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_workflow_run_properties.async_get_workflow_run_properties(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_workflow_run_properties_request.GetWorkflowRunPropertiesRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["run_id"] = run_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_workflow_runs(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        include_graph: Optional[
            "aws_sdk_glue.types.nullable_boolean.NullableBoolean"
        ] = None,
        next_token: Optional["aws_sdk_glue.types.generic_string.GenericString"] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
    ) -> "aws_sdk_glue.types.get_workflow_runs_response.GetWorkflowRunsResponse":
        """<p>Retrieves metadata for all runs of a given workflow.</p>

        Args:
            name: <p>Name of the workflow whose metadata of runs should be returned.</p>
            include_graph: <p>Specifies whether to include the workflow graph in response or not.</p>
            next_token: <p>The maximum size of the response.</p>
            max_results: <p>The maximum number of workflow runs to be included in the response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.get_workflow_runs_request.GetWorkflowRunsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.get_workflow_runs_response.GetWorkflowRunsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.get_workflow_runs

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.get_workflow_runs.async_get_workflow_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.get_workflow_runs_request.GetWorkflowRunsRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if include_graph is not None:
            input_["include_graph"] = include_graph
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

    async def iter_get_workflow_runs(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        include_graph: Optional[
            "aws_sdk_glue.types.nullable_boolean.NullableBoolean"
        ] = None,
        next_token: Optional["aws_sdk_glue.types.generic_string.GenericString"] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
    ) -> "AsyncIterator[aws_sdk_glue.types.workflow_run.WorkflowRun]":
        _token = next_token
        while True:
            _response = await self.get_workflow_runs(
                name,
                config_overrides=config_overrides,
                include_graph=include_graph,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("runs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def import_catalog_to_glue(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> (
        "aws_sdk_glue.types.import_catalog_to_glue_response.ImportCatalogToGlueResponse"
    ):
        """<p>Imports an existing Amazon Athena Data Catalog to Glue.</p>

        Args:
            catalog_id: <p>The ID of the catalog to import. Currently, this should be the Amazon Web Services account ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.import_catalog_to_glue_request.ImportCatalogToGlueRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.import_catalog_to_glue_response.ImportCatalogToGlueResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.import_catalog_to_glue

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.import_catalog_to_glue.async_import_catalog_to_glue(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.import_catalog_to_glue_request.ImportCatalogToGlueRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_blueprints(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        next_token: Optional["aws_sdk_glue.types.generic_string.GenericString"] = None,
        max_results: Optional[
            "aws_sdk_glue.types.orchestration_page_size25.OrchestrationPageSize25"
        ] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_glue.types.list_blueprints_response.ListBlueprintsResponse":
        """<p>Lists all the blueprint names in an account.</p>

        Args:
            next_token: <p>A continuation token, if this is a continuation request.</p>
            max_results: <p>The maximum size of a list to return.</p>
            tags: <p>Filters the list by an Amazon Web Services resource tag.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.list_blueprints_request.ListBlueprintsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.list_blueprints_response.ListBlueprintsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.list_blueprints

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.list_blueprints.async_list_blueprints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.list_blueprints_request.ListBlueprintsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_blueprints(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        next_token: Optional["aws_sdk_glue.types.generic_string.GenericString"] = None,
        max_results: Optional[
            "aws_sdk_glue.types.orchestration_page_size25.OrchestrationPageSize25"
        ] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
    ) -> "AsyncIterator[aws_sdk_glue.types.orchestration_name_string.OrchestrationNameString]":
        _token = next_token
        while True:
            _response = await self.list_blueprints(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                tags=tags,
            )
            _page = _resolve_path(_response, ("blueprints",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_column_statistics_task_runs(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
        next_token: Optional["aws_sdk_glue.types.token.Token"] = None,
    ) -> "aws_sdk_glue.types.list_column_statistics_task_runs_response.ListColumnStatisticsTaskRunsResponse":
        """<p>List all task runs for a particular account.</p>

        Args:
            max_results: <p>The maximum size of the response.</p>
            next_token: <p>A continuation token, if this is a continuation call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.list_column_statistics_task_runs_request.ListColumnStatisticsTaskRunsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.list_column_statistics_task_runs_response.ListColumnStatisticsTaskRunsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.list_column_statistics_task_runs

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.list_column_statistics_task_runs.async_list_column_statistics_task_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.list_column_statistics_task_runs_request.ListColumnStatisticsTaskRunsRequest = {}  # type: ignore[typeddict-item]
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

    async def list_connection_types(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        max_results: Optional["aws_sdk_glue.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_glue.types.next_token.NextToken"] = None,
    ) -> (
        "aws_sdk_glue.types.list_connection_types_response.ListConnectionTypesResponse"
    ):
        """<p>The <code>ListConnectionTypes</code> API provides a discovery mechanism to learn available connection types in Glue. The response contains a list of connection types with high-level details of what is supported for each connection type, including both built-in connection types and custom connection types registered via <code>RegisterConnectionType</code>. The connection types listed are the set of supported options for the <code>ConnectionType</code> value in the <code>CreateConnection</code> API.</p> <p>See also: <code>DescribeConnectionType</code>, <code>RegisterConnectionType</code>, <code>DeleteConnectionType</code> </p>

        Args:
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A continuation token, if this is a continuation call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.list_connection_types_request.ListConnectionTypesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.list_connection_types_response.ListConnectionTypesResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.list_connection_types

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.list_connection_types.async_list_connection_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.list_connection_types_request.ListConnectionTypesRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_list_connection_types(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        max_results: Optional["aws_sdk_glue.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_glue.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_glue.types.connection_type_brief.ConnectionTypeBrief]":
        _token = next_token
        while True:
            _response = await self.list_connection_types(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("connection_types",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_crawlers(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
        next_token: Optional["aws_sdk_glue.types.token.Token"] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_glue.types.list_crawlers_response.ListCrawlersResponse":
        """<p>Retrieves the names of all crawler resources in this Amazon Web Services account, or the resources with the specified tag. This operation allows you to see which resources are available in your account, and their names.</p> <p>This operation takes the optional <code>Tags</code> field, which you can use as a filter on the response so that tagged resources can be retrieved as a group. If you choose to use tags filtering, only resources with the tag are retrieved.</p>

        Args:
            max_results: <p>The maximum size of a list to return.</p>
            next_token: <p>A continuation token, if this is a continuation request.</p>
            tags: <p>Specifies to return only these tagged resources.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.list_crawlers_request.ListCrawlersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.list_crawlers_response.ListCrawlersResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.list_crawlers

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.list_crawlers.async_list_crawlers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.list_crawlers_request.ListCrawlersRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_crawls(
        self,
        crawler_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
        filters: Optional[
            "aws_sdk_glue.types.crawls_filter_list.CrawlsFilterList"
        ] = None,
        next_token: Optional["aws_sdk_glue.types.token.Token"] = None,
    ) -> "aws_sdk_glue.types.list_crawls_response.ListCrawlsResponse":
        """<p>Returns all the crawls of a specified crawler. Returns only the crawls that have occurred since the launch date of the crawler history feature, and only retains up to 12 months of crawls. Older crawls will not be returned.</p> <p>You may use this API to:</p> <ul> <li> <p>Retrive all the crawls of a specified crawler.</p> </li> <li> <p>Retrieve all the crawls of a specified crawler within a limited count.</p> </li> <li> <p>Retrieve all the crawls of a specified crawler in a specific time range.</p> </li> <li> <p>Retrieve all the crawls of a specified crawler with a particular state, crawl ID, or DPU hour value.</p> </li> </ul>

        Args:
            crawler_name: <p>The name of the crawler whose runs you want to retrieve.</p>
            max_results: <p>The maximum number of results to return. The default is 20, and maximum is 100.</p>
            filters: <p>Filters the crawls by the criteria you specify in a list of <code>CrawlsFilter</code> objects.</p>
            next_token: <p>A continuation token, if this is a continuation call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.list_crawls_request.ListCrawlsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.list_crawls_response.ListCrawlsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.list_crawls

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.list_crawls.async_list_crawls(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.list_crawls_request.ListCrawlsRequest = {}  # type: ignore[typeddict-item]
        input_["crawler_name"] = crawler_name
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_custom_entity_types(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        next_token: Optional[
            "aws_sdk_glue.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_glue.types.list_custom_entity_types_response.ListCustomEntityTypesResponse":
        """<p>Lists all the custom patterns that have been created.</p>

        Args:
            next_token: <p>A paginated token to offset the results.</p>
            max_results: <p>The maximum number of results to return.</p>
            tags: <p>A list of key-value pair tags.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.list_custom_entity_types_request.ListCustomEntityTypesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.list_custom_entity_types_response.ListCustomEntityTypesResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.list_custom_entity_types

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.list_custom_entity_types.async_list_custom_entity_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.list_custom_entity_types_request.ListCustomEntityTypesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_data_quality_results(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        filter: Optional[
            "aws_sdk_glue.types.data_quality_result_filter_criteria.DataQualityResultFilterCriteria"
        ] = None,
        next_token: Optional[
            "aws_sdk_glue.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
    ) -> "aws_sdk_glue.types.list_data_quality_results_response.ListDataQualityResultsResponse":
        """<p>Returns all data quality execution results for your account.</p>

        Args:
            filter: <p>The filter criteria.</p>
            next_token: <p>A paginated token to offset the results.</p>
            max_results: <p>The maximum number of results to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.list_data_quality_results_request.ListDataQualityResultsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.list_data_quality_results_response.ListDataQualityResultsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.list_data_quality_results

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.list_data_quality_results.async_list_data_quality_results(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.list_data_quality_results_request.ListDataQualityResultsRequest = {}  # type: ignore[typeddict-item]
        if filter is not None:
            input_["filter"] = filter
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

    async def list_data_quality_rule_recommendation_runs(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        filter: Optional[
            "aws_sdk_glue.types.data_quality_rule_recommendation_run_filter.DataQualityRuleRecommendationRunFilter"
        ] = None,
        next_token: Optional[
            "aws_sdk_glue.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
    ) -> "aws_sdk_glue.types.list_data_quality_rule_recommendation_runs_response.ListDataQualityRuleRecommendationRunsResponse":
        """<p>Lists the recommendation runs meeting the filter criteria.</p>

        Args:
            filter: <p>The filter criteria.</p>
            next_token: <p>A paginated token to offset the results.</p>
            max_results: <p>The maximum number of results to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.list_data_quality_rule_recommendation_runs_request.ListDataQualityRuleRecommendationRunsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.list_data_quality_rule_recommendation_runs_response.ListDataQualityRuleRecommendationRunsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.list_data_quality_rule_recommendation_runs

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.list_data_quality_rule_recommendation_runs.async_list_data_quality_rule_recommendation_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.list_data_quality_rule_recommendation_runs_request.ListDataQualityRuleRecommendationRunsRequest = {}  # type: ignore[typeddict-item]
        if filter is not None:
            input_["filter"] = filter
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

    async def list_data_quality_ruleset_evaluation_runs(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        filter: Optional[
            "aws_sdk_glue.types.data_quality_ruleset_evaluation_run_filter.DataQualityRulesetEvaluationRunFilter"
        ] = None,
        next_token: Optional[
            "aws_sdk_glue.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
    ) -> "aws_sdk_glue.types.list_data_quality_ruleset_evaluation_runs_response.ListDataQualityRulesetEvaluationRunsResponse":
        """<p>Lists all the runs meeting the filter criteria, where a ruleset is evaluated against a data source.</p>

        Args:
            filter: <p>The filter criteria.</p>
            next_token: <p>A paginated token to offset the results.</p>
            max_results: <p>The maximum number of results to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.list_data_quality_ruleset_evaluation_runs_request.ListDataQualityRulesetEvaluationRunsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.list_data_quality_ruleset_evaluation_runs_response.ListDataQualityRulesetEvaluationRunsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.list_data_quality_ruleset_evaluation_runs

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.list_data_quality_ruleset_evaluation_runs.async_list_data_quality_ruleset_evaluation_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.list_data_quality_ruleset_evaluation_runs_request.ListDataQualityRulesetEvaluationRunsRequest = {}  # type: ignore[typeddict-item]
        if filter is not None:
            input_["filter"] = filter
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

    async def list_data_quality_rulesets(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        next_token: Optional[
            "aws_sdk_glue.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
        filter: Optional[
            "aws_sdk_glue.types.data_quality_ruleset_filter_criteria.DataQualityRulesetFilterCriteria"
        ] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_glue.types.list_data_quality_rulesets_response.ListDataQualityRulesetsResponse":
        """<p>Returns a paginated list of rulesets for the specified list of Glue tables.</p>

        Args:
            next_token: <p>A paginated token to offset the results.</p>
            max_results: <p>The maximum number of results to return.</p>
            filter: <p>The filter criteria. </p>
            tags: <p>A list of key-value pair tags.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.list_data_quality_rulesets_request.ListDataQualityRulesetsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.list_data_quality_rulesets_response.ListDataQualityRulesetsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.list_data_quality_rulesets

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.list_data_quality_rulesets.async_list_data_quality_rulesets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.list_data_quality_rulesets_request.ListDataQualityRulesetsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_data_quality_statistic_annotations(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        statistic_id: Optional["aws_sdk_glue.types.hash_string.HashString"] = None,
        profile_id: Optional["aws_sdk_glue.types.hash_string.HashString"] = None,
        timestamp_filter: Optional[
            "aws_sdk_glue.types.timestamp_filter.TimestampFilter"
        ] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
        next_token: Optional[
            "aws_sdk_glue.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_glue.types.list_data_quality_statistic_annotations_response.ListDataQualityStatisticAnnotationsResponse":
        """<p>Retrieve annotations for a data quality statistic.</p>

        Args:
            statistic_id: <p>The Statistic ID.</p>
            profile_id: <p>The Profile ID.</p>
            timestamp_filter: <p>A timestamp filter.</p>
            max_results: <p>The maximum number of results to return in this request.</p>
            next_token: <p>A pagination token to retrieve the next set of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.list_data_quality_statistic_annotations_request.ListDataQualityStatisticAnnotationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.list_data_quality_statistic_annotations_response.ListDataQualityStatisticAnnotationsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.list_data_quality_statistic_annotations

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.list_data_quality_statistic_annotations.async_list_data_quality_statistic_annotations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.list_data_quality_statistic_annotations_request.ListDataQualityStatisticAnnotationsRequest = {}  # type: ignore[typeddict-item]
        if statistic_id is not None:
            input_["statistic_id"] = statistic_id
        if profile_id is not None:
            input_["profile_id"] = profile_id
        if timestamp_filter is not None:
            input_["timestamp_filter"] = timestamp_filter
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

    async def list_data_quality_statistics(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        statistic_id: Optional["aws_sdk_glue.types.hash_string.HashString"] = None,
        profile_id: Optional["aws_sdk_glue.types.hash_string.HashString"] = None,
        timestamp_filter: Optional[
            "aws_sdk_glue.types.timestamp_filter.TimestampFilter"
        ] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
        next_token: Optional[
            "aws_sdk_glue.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_glue.types.list_data_quality_statistics_response.ListDataQualityStatisticsResponse":
        """<p>Retrieves a list of data quality statistics.</p>

        Args:
            statistic_id: <p>The Statistic ID.</p>
            profile_id: <p>The Profile ID.</p>
            timestamp_filter: <p>A timestamp filter.</p>
            max_results: <p>The maximum number of results to return in this request.</p>
            next_token: <p>A pagination token to request the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.list_data_quality_statistics_request.ListDataQualityStatisticsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.list_data_quality_statistics_response.ListDataQualityStatisticsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.list_data_quality_statistics

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.list_data_quality_statistics.async_list_data_quality_statistics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.list_data_quality_statistics_request.ListDataQualityStatisticsRequest = {}  # type: ignore[typeddict-item]
        if statistic_id is not None:
            input_["statistic_id"] = statistic_id
        if profile_id is not None:
            input_["profile_id"] = profile_id
        if timestamp_filter is not None:
            input_["timestamp_filter"] = timestamp_filter
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

    async def list_dev_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        next_token: Optional["aws_sdk_glue.types.generic_string.GenericString"] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_glue.types.list_dev_endpoints_response.ListDevEndpointsResponse":
        """<p>Retrieves the names of all <code>DevEndpoint</code> resources in this Amazon Web Services account, or the resources with the specified tag. This operation allows you to see which resources are available in your account, and their names.</p> <p>This operation takes the optional <code>Tags</code> field, which you can use as a filter on the response so that tagged resources can be retrieved as a group. If you choose to use tags filtering, only resources with the tag are retrieved.</p>

        Args:
            next_token: <p>A continuation token, if this is a continuation request.</p>
            max_results: <p>The maximum size of a list to return.</p>
            tags: <p>Specifies to return only these tagged resources.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.list_dev_endpoints_request.ListDevEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.list_dev_endpoints_response.ListDevEndpointsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.list_dev_endpoints

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.list_dev_endpoints.async_list_dev_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.list_dev_endpoints_request.ListDevEndpointsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_entities(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        connection_name: Optional["aws_sdk_glue.types.name_string.NameString"] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
        parent_entity_name: Optional[
            "aws_sdk_glue.types.entity_name.EntityName"
        ] = None,
        next_token: Optional["aws_sdk_glue.types.next_token.NextToken"] = None,
        data_store_api_version: Optional[
            "aws_sdk_glue.types.api_version.ApiVersion"
        ] = None,
    ) -> "aws_sdk_glue.types.list_entities_response.ListEntitiesResponse":
        """<p>Returns the available entities supported by the connection type. </p>

        Args:
            connection_name: <p>A name for the connection that has required credentials to query any connection type.</p>
            catalog_id: <p>The catalog ID of the catalog that contains the connection. This can be null, By default, the Amazon Web Services Account ID is the catalog ID.</p>
            parent_entity_name: <p>Name of the parent entity for which you want to list the children. This parameter takes a fully-qualified path of the entity in order to list the child entities.</p>
            next_token: <p>A continuation token, included if this is a continuation call.</p>
            data_store_api_version: <p>The API version of the SaaS connector.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.list_entities_request.ListEntitiesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.list_entities_response.ListEntitiesResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.list_entities

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.list_entities.async_list_entities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.list_entities_request.ListEntitiesRequest = {}  # type: ignore[typeddict-item]
        if connection_name is not None:
            input_["connection_name"] = connection_name
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        if parent_entity_name is not None:
            input_["parent_entity_name"] = parent_entity_name
        if next_token is not None:
            input_["next_token"] = next_token
        if data_store_api_version is not None:
            input_["data_store_api_version"] = data_store_api_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_entities(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        connection_name: Optional["aws_sdk_glue.types.name_string.NameString"] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
        parent_entity_name: Optional[
            "aws_sdk_glue.types.entity_name.EntityName"
        ] = None,
        next_token: Optional["aws_sdk_glue.types.next_token.NextToken"] = None,
        data_store_api_version: Optional[
            "aws_sdk_glue.types.api_version.ApiVersion"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_glue.types.entity.Entity]":
        _token = next_token
        while True:
            _response = await self.list_entities(
                config_overrides=config_overrides,
                connection_name=connection_name,
                catalog_id=catalog_id,
                parent_entity_name=parent_entity_name,
                next_token=_token,
                data_store_api_version=data_store_api_version,
            )
            _page = _resolve_path(_response, ("entities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_integration_resource_properties(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        marker: Optional["aws_sdk_glue.types.string1024.String1024"] = None,
        filters: Optional[
            "aws_sdk_glue.types.integration_resource_property_filter_list.IntegrationResourcePropertyFilterList"
        ] = None,
        max_records: Optional[
            "aws_sdk_glue.types.integration_integer.IntegrationInteger"
        ] = None,
    ) -> "aws_sdk_glue.types.list_integration_resource_properties_response.ListIntegrationResourcePropertiesResponse":
        """<p>List integration resource properties for a single customer. It supports the filters, maxRecords and markers.</p>

        Args:
            marker: <p>This is the pagination token for next page, initial value is <code>null</code>.</p>
            filters: <p>A list of filters, supported filter Key is <code>SourceArn</code> and <code>TargetArn</code>.</p>
            max_records: <p>This is total number of items to be evaluated.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.list_integration_resource_properties_request.ListIntegrationResourcePropertiesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.list_integration_resource_properties_response.ListIntegrationResourcePropertiesResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.list_integration_resource_properties

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.list_integration_resource_properties.async_list_integration_resource_properties(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.list_integration_resource_properties_request.ListIntegrationResourcePropertiesRequest = {}  # type: ignore[typeddict-item]
        if marker is not None:
            input_["marker"] = marker
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_jobs(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        next_token: Optional["aws_sdk_glue.types.generic_string.GenericString"] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_glue.types.list_jobs_response.ListJobsResponse":
        """<p>Retrieves the names of all job resources in this Amazon Web Services account, or the resources with the specified tag. This operation allows you to see which resources are available in your account, and their names.</p> <p>This operation takes the optional <code>Tags</code> field, which you can use as a filter on the response so that tagged resources can be retrieved as a group. If you choose to use tags filtering, only resources with the tag are retrieved.</p>

        Args:
            next_token: <p>A continuation token, if this is a continuation request.</p>
            max_results: <p>The maximum size of a list to return.</p>
            tags: <p>Specifies to return only these tagged resources.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.list_jobs_request.ListJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.list_jobs_response.ListJobsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.list_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.list_jobs.async_list_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.list_jobs_request.ListJobsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_jobs(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        next_token: Optional["aws_sdk_glue.types.generic_string.GenericString"] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
    ) -> "AsyncIterator[aws_sdk_glue.types.name_string.NameString]":
        _token = next_token
        while True:
            _response = await self.list_jobs(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                tags=tags,
            )
            _page = _resolve_path(_response, ("job_names",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_materialized_view_refresh_task_runs(
        self,
        catalog_id: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        database_name: Optional["aws_sdk_glue.types.name_string.NameString"] = None,
        table_name: Optional["aws_sdk_glue.types.name_string.NameString"] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
        next_token: Optional["aws_sdk_glue.types.token.Token"] = None,
    ) -> "aws_sdk_glue.types.list_materialized_view_refresh_task_runs_response.ListMaterializedViewRefreshTaskRunsResponse":
        """<p>List all task runs for a particular account.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog where the table resides. If none is supplied, the account ID is used by default.</p>
            database_name: <p>The database where the table resides.</p>
            table_name: <p>The name of the table for which statistics is generated.</p>
            max_results: <p>The maximum size of the response.</p>
            next_token: <p>A continuation token, if this is a continuation call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.list_materialized_view_refresh_task_runs_request.ListMaterializedViewRefreshTaskRunsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.list_materialized_view_refresh_task_runs_response.ListMaterializedViewRefreshTaskRunsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.list_materialized_view_refresh_task_runs

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.list_materialized_view_refresh_task_runs.async_list_materialized_view_refresh_task_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.list_materialized_view_refresh_task_runs_request.ListMaterializedViewRefreshTaskRunsRequest = {}  # type: ignore[typeddict-item]
        input_["catalog_id"] = catalog_id
        if database_name is not None:
            input_["database_name"] = database_name
        if table_name is not None:
            input_["table_name"] = table_name
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

    async def iter_list_materialized_view_refresh_task_runs(
        self,
        catalog_id: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        database_name: Optional["aws_sdk_glue.types.name_string.NameString"] = None,
        table_name: Optional["aws_sdk_glue.types.name_string.NameString"] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
        next_token: Optional["aws_sdk_glue.types.token.Token"] = None,
    ) -> "AsyncIterator[aws_sdk_glue.types.materialized_view_refresh_task_run.MaterializedViewRefreshTaskRun]":
        _token = next_token
        while True:
            _response = await self.list_materialized_view_refresh_task_runs(
                catalog_id,
                config_overrides=config_overrides,
                database_name=database_name,
                table_name=table_name,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("materialized_view_refresh_task_runs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_ml_transforms(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        next_token: Optional[
            "aws_sdk_glue.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
        filter: Optional[
            "aws_sdk_glue.types.transform_filter_criteria.TransformFilterCriteria"
        ] = None,
        sort: Optional[
            "aws_sdk_glue.types.transform_sort_criteria.TransformSortCriteria"
        ] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_glue.types.list_ml_transforms_response.ListMLTransformsResponse":
        """<p> Retrieves a sortable, filterable list of existing Glue machine learning transforms in this Amazon Web Services account, or the resources with the specified tag. This operation takes the optional <code>Tags</code> field, which you can use as a filter of the responses so that tagged resources can be retrieved as a group. If you choose to use tag filtering, only resources with the tags are retrieved. </p>

        Args:
            next_token: <p>A continuation token, if this is a continuation request.</p>
            max_results: <p>The maximum size of a list to return.</p>
            filter: <p>A <code>TransformFilterCriteria</code> used to filter the machine learning transforms.</p>
            sort: <p>A <code>TransformSortCriteria</code> used to sort the machine learning transforms.</p>
            tags: <p>Specifies to return only these tagged resources.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.list_ml_transforms_request.ListMLTransformsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.list_ml_transforms_response.ListMLTransformsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.list_ml_transforms

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.list_ml_transforms.async_list_ml_transforms(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.list_ml_transforms_request.ListMLTransformsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter
        if sort is not None:
            input_["sort"] = sort
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_registries(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        max_results: Optional[
            "aws_sdk_glue.types.max_results_number.MaxResultsNumber"
        ] = None,
        next_token: Optional[
            "aws_sdk_glue.types.schema_registry_token_string.SchemaRegistryTokenString"
        ] = None,
    ) -> "aws_sdk_glue.types.list_registries_response.ListRegistriesResponse":
        """<p>Returns a list of registries that you have created, with minimal registry information. Registries in the <code>Deleting</code> status will not be included in the results. Empty results will be returned if there are no registries available.</p>

        Args:
            max_results: <p>Maximum number of results required per page. If the value is not supplied, this will be defaulted to 25 per page.</p>
            next_token: <p>A continuation token, if this is a continuation call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.list_registries_input.ListRegistriesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.list_registries_response.ListRegistriesResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.list_registries

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.list_registries.async_list_registries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.list_registries_input.ListRegistriesInput = {}  # type: ignore[typeddict-item]
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

    async def iter_list_registries(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        max_results: Optional[
            "aws_sdk_glue.types.max_results_number.MaxResultsNumber"
        ] = None,
        next_token: Optional[
            "aws_sdk_glue.types.schema_registry_token_string.SchemaRegistryTokenString"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_glue.types.registry_list_item.RegistryListItem]":
        _token = next_token
        while True:
            _response = await self.list_registries(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("registries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_schemas(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        registry_id: Optional["aws_sdk_glue.types.registry_id.RegistryId"] = None,
        max_results: Optional[
            "aws_sdk_glue.types.max_results_number.MaxResultsNumber"
        ] = None,
        next_token: Optional[
            "aws_sdk_glue.types.schema_registry_token_string.SchemaRegistryTokenString"
        ] = None,
    ) -> "aws_sdk_glue.types.list_schemas_response.ListSchemasResponse":
        """<p>Returns a list of schemas with minimal details. Schemas in Deleting status will not be included in the results. Empty results will be returned if there are no schemas available.</p> <p>When the <code>RegistryId</code> is not provided, all the schemas across registries will be part of the API response.</p>

        Args:
            registry_id: <p>A wrapper structure that may contain the registry name and Amazon Resource Name (ARN).</p>
            max_results: <p>Maximum number of results required per page. If the value is not supplied, this will be defaulted to 25 per page.</p>
            next_token: <p>A continuation token, if this is a continuation call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.list_schemas_input.ListSchemasInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.list_schemas_response.ListSchemasResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.list_schemas

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.list_schemas.async_list_schemas(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.list_schemas_input.ListSchemasInput = {}  # type: ignore[typeddict-item]
        if registry_id is not None:
            input_["registry_id"] = registry_id
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

    async def iter_list_schemas(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        registry_id: Optional["aws_sdk_glue.types.registry_id.RegistryId"] = None,
        max_results: Optional[
            "aws_sdk_glue.types.max_results_number.MaxResultsNumber"
        ] = None,
        next_token: Optional[
            "aws_sdk_glue.types.schema_registry_token_string.SchemaRegistryTokenString"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_glue.types.schema_list_item.SchemaListItem]":
        _token = next_token
        while True:
            _response = await self.list_schemas(
                config_overrides=config_overrides,
                registry_id=registry_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("schemas",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_schema_versions(
        self,
        schema_id: "aws_sdk_glue.types.schema_id.SchemaId",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        max_results: Optional[
            "aws_sdk_glue.types.max_results_number.MaxResultsNumber"
        ] = None,
        next_token: Optional[
            "aws_sdk_glue.types.schema_registry_token_string.SchemaRegistryTokenString"
        ] = None,
    ) -> "aws_sdk_glue.types.list_schema_versions_response.ListSchemaVersionsResponse":
        """<p>Returns a list of schema versions that you have created, with minimal information. Schema versions in Deleted status will not be included in the results. Empty results will be returned if there are no schema versions available.</p>

        Args:
            schema_id: <p>This is a wrapper structure to contain schema identity fields. The structure contains:</p> <ul> <li> <p>SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. Either <code>SchemaArn</code> or <code>SchemaName</code> and <code>RegistryName</code> has to be provided.</p> </li> <li> <p>SchemaId$SchemaName: The name of the schema. Either <code>SchemaArn</code> or <code>SchemaName</code> and <code>RegistryName</code> has to be provided.</p> </li> </ul>
            max_results: <p>Maximum number of results required per page. If the value is not supplied, this will be defaulted to 25 per page.</p>
            next_token: <p>A continuation token, if this is a continuation call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.list_schema_versions_input.ListSchemaVersionsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.list_schema_versions_response.ListSchemaVersionsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.list_schema_versions

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.list_schema_versions.async_list_schema_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.list_schema_versions_input.ListSchemaVersionsInput = {}  # type: ignore[typeddict-item]
        input_["schema_id"] = schema_id
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

    async def iter_list_schema_versions(
        self,
        schema_id: "aws_sdk_glue.types.schema_id.SchemaId",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        max_results: Optional[
            "aws_sdk_glue.types.max_results_number.MaxResultsNumber"
        ] = None,
        next_token: Optional[
            "aws_sdk_glue.types.schema_registry_token_string.SchemaRegistryTokenString"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_glue.types.schema_version_list_item.SchemaVersionListItem]":
        _token = next_token
        while True:
            _response = await self.list_schema_versions(
                schema_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("schemas",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_sessions(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        next_token: Optional[
            "aws_sdk_glue.types.orchestration_token.OrchestrationToken"
        ] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
        request_origin: Optional[
            "aws_sdk_glue.types.orchestration_name_string.OrchestrationNameString"
        ] = None,
    ) -> "aws_sdk_glue.types.list_sessions_response.ListSessionsResponse":
        """<p>Retrieve a list of sessions.</p>

        Args:
            next_token: <p>The token for the next set of results, or null if there are no more result. </p>
            max_results: <p>The maximum number of results. </p>
            tags: <p>Tags belonging to the session. </p>
            request_origin: <p>The origin of the request. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.list_sessions_request.ListSessionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.list_sessions_response.ListSessionsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.list_sessions

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.list_sessions.async_list_sessions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.list_sessions_request.ListSessionsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if tags is not None:
            input_["tags"] = tags
        if request_origin is not None:
            input_["request_origin"] = request_origin

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_statements(
        self,
        session_id: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        request_origin: Optional[
            "aws_sdk_glue.types.orchestration_name_string.OrchestrationNameString"
        ] = None,
        next_token: Optional[
            "aws_sdk_glue.types.orchestration_token.OrchestrationToken"
        ] = None,
    ) -> "aws_sdk_glue.types.list_statements_response.ListStatementsResponse":
        """<p>Lists statements for the session.</p>

        Args:
            session_id: <p>The Session ID of the statements.</p>
            request_origin: <p>The origin of the request to list statements.</p>
            next_token: <p>A continuation token, if this is a continuation call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.list_statements_request.ListStatementsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.list_statements_response.ListStatementsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.list_statements

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.list_statements.async_list_statements(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.list_statements_request.ListStatementsRequest = {}  # type: ignore[typeddict-item]
        input_["session_id"] = session_id
        if request_origin is not None:
            input_["request_origin"] = request_origin
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_table_optimizer_runs(
        self,
        catalog_id: "aws_sdk_glue.types.catalog_id_string.CatalogIdString",
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        type: "aws_sdk_glue.types.table_optimizer_type.TableOptimizerType",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        max_results: Optional[
            "aws_sdk_glue.types.max_list_table_optimizer_runs_token_results.MaxListTableOptimizerRunsTokenResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_glue.types.list_table_optimizer_runs_token.ListTableOptimizerRunsToken"
        ] = None,
    ) -> "aws_sdk_glue.types.list_table_optimizer_runs_response.ListTableOptimizerRunsResponse":
        """<p>Lists the history of previous optimizer runs for a specific table.</p>

        Args:
            catalog_id: <p>The Catalog ID of the table.</p>
            database_name: <p>The name of the database in the catalog in which the table resides.</p>
            table_name: <p>The name of the table.</p>
            type: <p>The type of table optimizer.</p>
            max_results: <p>The maximum number of optimizer runs to return on each call.</p>
            next_token: <p>A continuation token, if this is a continuation call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.list_table_optimizer_runs_request.ListTableOptimizerRunsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.list_table_optimizer_runs_response.ListTableOptimizerRunsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.list_table_optimizer_runs

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.list_table_optimizer_runs.async_list_table_optimizer_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.list_table_optimizer_runs_request.ListTableOptimizerRunsRequest = {}  # type: ignore[typeddict-item]
        input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        input_["type"] = type
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

    async def iter_list_table_optimizer_runs(
        self,
        catalog_id: "aws_sdk_glue.types.catalog_id_string.CatalogIdString",
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        type: "aws_sdk_glue.types.table_optimizer_type.TableOptimizerType",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        max_results: Optional[
            "aws_sdk_glue.types.max_list_table_optimizer_runs_token_results.MaxListTableOptimizerRunsTokenResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_glue.types.list_table_optimizer_runs_token.ListTableOptimizerRunsToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_glue.types.table_optimizer_run.TableOptimizerRun]":
        _token = next_token
        while True:
            _response = await self.list_table_optimizer_runs(
                catalog_id,
                database_name,
                table_name,
                type,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("table_optimizer_runs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_triggers(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        next_token: Optional["aws_sdk_glue.types.generic_string.GenericString"] = None,
        dependent_job_name: Optional[
            "aws_sdk_glue.types.name_string.NameString"
        ] = None,
        max_results: Optional[
            "aws_sdk_glue.types.orchestration_page_size200.OrchestrationPageSize200"
        ] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_glue.types.list_triggers_response.ListTriggersResponse":
        """<p>Retrieves the names of all trigger resources in this Amazon Web Services account, or the resources with the specified tag. This operation allows you to see which resources are available in your account, and their names.</p> <p>This operation takes the optional <code>Tags</code> field, which you can use as a filter on the response so that tagged resources can be retrieved as a group. If you choose to use tags filtering, only resources with the tag are retrieved.</p>

        Args:
            next_token: <p>A continuation token, if this is a continuation request.</p>
            dependent_job_name: <p> The name of the job for which to retrieve triggers. The trigger that can start this job is returned. If there is no such trigger, all triggers are returned.</p>
            max_results: <p>The maximum size of a list to return.</p>
            tags: <p>Specifies to return only these tagged resources.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.list_triggers_request.ListTriggersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.list_triggers_response.ListTriggersResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.list_triggers

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.list_triggers.async_list_triggers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.list_triggers_request.ListTriggersRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if dependent_job_name is not None:
            input_["dependent_job_name"] = dependent_job_name
        if max_results is not None:
            input_["max_results"] = max_results
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_triggers(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        next_token: Optional["aws_sdk_glue.types.generic_string.GenericString"] = None,
        dependent_job_name: Optional[
            "aws_sdk_glue.types.name_string.NameString"
        ] = None,
        max_results: Optional[
            "aws_sdk_glue.types.orchestration_page_size200.OrchestrationPageSize200"
        ] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
    ) -> "AsyncIterator[aws_sdk_glue.types.name_string.NameString]":
        _token = next_token
        while True:
            _response = await self.list_triggers(
                config_overrides=config_overrides,
                next_token=_token,
                dependent_job_name=dependent_job_name,
                max_results=max_results,
                tags=tags,
            )
            _page = _resolve_path(_response, ("trigger_names",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_usage_profiles(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        next_token: Optional[
            "aws_sdk_glue.types.orchestration_token.OrchestrationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_glue.types.orchestration_page_size200.OrchestrationPageSize200"
        ] = None,
    ) -> "aws_sdk_glue.types.list_usage_profiles_response.ListUsageProfilesResponse":
        """<p>List all the Glue usage profiles.</p>

        Args:
            next_token: <p>A continuation token, included if this is a continuation call.</p>
            max_results: <p>The maximum number of usage profiles to return in a single response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.list_usage_profiles_request.ListUsageProfilesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.list_usage_profiles_response.ListUsageProfilesResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.list_usage_profiles

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.list_usage_profiles.async_list_usage_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.list_usage_profiles_request.ListUsageProfilesRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_list_usage_profiles(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        next_token: Optional[
            "aws_sdk_glue.types.orchestration_token.OrchestrationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_glue.types.orchestration_page_size200.OrchestrationPageSize200"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_glue.types.usage_profile_definition.UsageProfileDefinition]":
        _token = next_token
        while True:
            _response = await self.list_usage_profiles(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("profiles",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_workflows(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        next_token: Optional["aws_sdk_glue.types.generic_string.GenericString"] = None,
        max_results: Optional[
            "aws_sdk_glue.types.orchestration_page_size25.OrchestrationPageSize25"
        ] = None,
    ) -> "aws_sdk_glue.types.list_workflows_response.ListWorkflowsResponse":
        """<p>Lists names of workflows created in the account.</p>

        Args:
            next_token: <p>A continuation token, if this is a continuation request.</p>
            max_results: <p>The maximum size of a list to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.list_workflows_request.ListWorkflowsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.list_workflows_response.ListWorkflowsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.list_workflows

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.list_workflows.async_list_workflows(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.list_workflows_request.ListWorkflowsRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_list_workflows(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        next_token: Optional["aws_sdk_glue.types.generic_string.GenericString"] = None,
        max_results: Optional[
            "aws_sdk_glue.types.orchestration_page_size25.OrchestrationPageSize25"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_glue.types.name_string.NameString]":
        _token = next_token
        while True:
            _response = await self.list_workflows(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("workflows",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def modify_integration(
        self,
        integration_identifier: "aws_sdk_glue.types.string128.String128",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        description: Optional[
            "aws_sdk_glue.types.integration_description.IntegrationDescription"
        ] = None,
        data_filter: Optional["aws_sdk_glue.types.string2048.String2048"] = None,
        integration_config: Optional[
            "aws_sdk_glue.types.integration_config.IntegrationConfig"
        ] = None,
        integration_name: Optional["aws_sdk_glue.types.string128.String128"] = None,
    ) -> "aws_sdk_glue.types.modify_integration_response.ModifyIntegrationResponse":
        """<p>Modifies a Zero-ETL integration in the caller's account.</p>

        Args:
            integration_identifier: <p>The Amazon Resource Name (ARN) for the integration.</p>
            description: <p>A description of the integration.</p>
            data_filter: <p>Selects source tables for the integration using Maxwell filter syntax.</p>
            integration_config: <p>The configuration settings for the integration. Currently, only the RefreshInterval can be modified. </p>
            integration_name: <p>A unique name for an integration in Glue.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.modify_integration_request.ModifyIntegrationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.modify_integration_response.ModifyIntegrationResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.modify_integration

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.modify_integration.async_modify_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.modify_integration_request.ModifyIntegrationRequest = {}  # type: ignore[typeddict-item]
        input_["integration_identifier"] = integration_identifier
        if description is not None:
            input_["description"] = description
        if data_filter is not None:
            input_["data_filter"] = data_filter
        if integration_config is not None:
            input_["integration_config"] = integration_config
        if integration_name is not None:
            input_["integration_name"] = integration_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_data_catalog_encryption_settings(
        self,
        data_catalog_encryption_settings: "aws_sdk_glue.types.data_catalog_encryption_settings.DataCatalogEncryptionSettings",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.put_data_catalog_encryption_settings_response.PutDataCatalogEncryptionSettingsResponse":
        """<p>Sets the security configuration for a specified catalog. After the configuration has been set, the specified encryption is applied to every catalog write thereafter.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog to set the security configuration for. If none is provided, the Amazon Web Services account ID is used by default.</p>
            data_catalog_encryption_settings: <p>The security configuration to set.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.put_data_catalog_encryption_settings_request.PutDataCatalogEncryptionSettingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.put_data_catalog_encryption_settings_response.PutDataCatalogEncryptionSettingsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.put_data_catalog_encryption_settings

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.put_data_catalog_encryption_settings.async_put_data_catalog_encryption_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.put_data_catalog_encryption_settings_request.PutDataCatalogEncryptionSettingsRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["data_catalog_encryption_settings"] = data_catalog_encryption_settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_data_quality_profile_annotation(
        self,
        profile_id: "aws_sdk_glue.types.hash_string.HashString",
        inclusion_annotation: "aws_sdk_glue.types.inclusion_annotation_value.InclusionAnnotationValue",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.put_data_quality_profile_annotation_response.PutDataQualityProfileAnnotationResponse":
        """<p>Annotate all datapoints for a Profile.</p>

        Args:
            profile_id: <p>The ID of the data quality monitoring profile to annotate.</p>
            inclusion_annotation: <p>The inclusion annotation value to apply to the profile.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.put_data_quality_profile_annotation_request.PutDataQualityProfileAnnotationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.put_data_quality_profile_annotation_response.PutDataQualityProfileAnnotationResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.put_data_quality_profile_annotation

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.put_data_quality_profile_annotation.async_put_data_quality_profile_annotation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.put_data_quality_profile_annotation_request.PutDataQualityProfileAnnotationRequest = {}  # type: ignore[typeddict-item]
        input_["profile_id"] = profile_id
        input_["inclusion_annotation"] = inclusion_annotation

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_resource_policy(
        self,
        policy_in_json: "aws_sdk_glue.types.policy_json_string.PolicyJsonString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        resource_arn: Optional[
            "aws_sdk_glue.types.glue_resource_arn.GlueResourceArn"
        ] = None,
        policy_hash_condition: Optional[
            "aws_sdk_glue.types.hash_string.HashString"
        ] = None,
        policy_exists_condition: Optional[
            "aws_sdk_glue.types.exist_condition.ExistCondition"
        ] = None,
        enable_hybrid: Optional[
            "aws_sdk_glue.types.enable_hybrid_values.EnableHybridValues"
        ] = None,
    ) -> "aws_sdk_glue.types.put_resource_policy_response.PutResourcePolicyResponse":
        """<p>Sets the Data Catalog resource policy for access control.</p>

        Args:
            policy_in_json: <p>Contains the policy document to set, in JSON format.</p>
            resource_arn: <p>Do not use. For internal use only.</p>
            policy_hash_condition: <p>The hash value returned when the previous policy was set using <code>PutResourcePolicy</code>. Its purpose is to prevent concurrent modifications of a policy. Do not use this parameter if no previous policy has been set.</p>
            policy_exists_condition: <p>A value of <code>MUST_EXIST</code> is used to update a policy. A value of <code>NOT_EXIST</code> is used to create a new policy. If a value of <code>NONE</code> or a null value is used, the call does not depend on the existence of a policy.</p>
            enable_hybrid: <p>If <code>'TRUE'</code>, indicates that you are using both methods to grant cross-account access to Data Catalog resources:</p> <ul> <li> <p>By directly updating the resource policy with <code>PutResourePolicy</code> </p> </li> <li> <p>By using the <b>Grant permissions</b> command on the Amazon Web Services Management Console.</p> </li> </ul> <p>Must be set to <code>'TRUE'</code> if you have already used the Management Console to grant cross-account access, otherwise the call fails. Default is 'FALSE'.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.put_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.put_resource_policy.async_put_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.put_resource_policy_request.PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["policy_in_json"] = policy_in_json
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
        if policy_hash_condition is not None:
            input_["policy_hash_condition"] = policy_hash_condition
        if policy_exists_condition is not None:
            input_["policy_exists_condition"] = policy_exists_condition
        if enable_hybrid is not None:
            input_["enable_hybrid"] = enable_hybrid

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_schema_version_metadata(
        self,
        metadata_key_value: "aws_sdk_glue.types.metadata_key_value_pair.MetadataKeyValuePair",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        schema_id: Optional["aws_sdk_glue.types.schema_id.SchemaId"] = None,
        schema_version_number: Optional[
            "aws_sdk_glue.types.schema_version_number.SchemaVersionNumber"
        ] = None,
        schema_version_id: Optional[
            "aws_sdk_glue.types.schema_version_id_string.SchemaVersionIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.put_schema_version_metadata_response.PutSchemaVersionMetadataResponse":
        """<p>Puts the metadata key value pair for a specified schema version ID. A maximum of 10 key value pairs will be allowed per schema version. They can be added over one or more calls.</p>

        Args:
            schema_id: <p>The unique ID for the schema.</p>
            schema_version_number: <p>The version number of the schema.</p>
            schema_version_id: <p>The unique version ID of the schema version.</p>
            metadata_key_value: <p>The metadata key's corresponding value.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.put_schema_version_metadata_input.PutSchemaVersionMetadataInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.put_schema_version_metadata_response.PutSchemaVersionMetadataResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.put_schema_version_metadata

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.put_schema_version_metadata.async_put_schema_version_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.put_schema_version_metadata_input.PutSchemaVersionMetadataInput = {}  # type: ignore[typeddict-item]
        if schema_id is not None:
            input_["schema_id"] = schema_id
        if schema_version_number is not None:
            input_["schema_version_number"] = schema_version_number
        if schema_version_id is not None:
            input_["schema_version_id"] = schema_version_id
        input_["metadata_key_value"] = metadata_key_value

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_workflow_run_properties(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        run_id: "aws_sdk_glue.types.id_string.IdString",
        run_properties: "aws_sdk_glue.types.workflow_run_properties.WorkflowRunProperties",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.put_workflow_run_properties_response.PutWorkflowRunPropertiesResponse":
        """<p>Puts the specified workflow run properties for the given workflow run. If a property already exists for the specified run, then it overrides the value otherwise adds the property to existing properties.</p>

        Args:
            name: <p>Name of the workflow which was run.</p>
            run_id: <p>The ID of the workflow run for which the run properties should be updated.</p>
            run_properties: <p>The properties to put for the specified run.</p> <p>Run properties may be logged. Do not pass plaintext secrets as properties. Retrieve secrets from a Glue Connection, Amazon Web Services Secrets Manager or other secret management mechanism if you intend to use them within the workflow run.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.put_workflow_run_properties_request.PutWorkflowRunPropertiesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.put_workflow_run_properties_response.PutWorkflowRunPropertiesResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.put_workflow_run_properties

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.put_workflow_run_properties.async_put_workflow_run_properties(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.put_workflow_run_properties_request.PutWorkflowRunPropertiesRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["run_id"] = run_id
        input_["run_properties"] = run_properties

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def query_schema_version_metadata(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        schema_id: Optional["aws_sdk_glue.types.schema_id.SchemaId"] = None,
        schema_version_number: Optional[
            "aws_sdk_glue.types.schema_version_number.SchemaVersionNumber"
        ] = None,
        schema_version_id: Optional[
            "aws_sdk_glue.types.schema_version_id_string.SchemaVersionIdString"
        ] = None,
        metadata_list: Optional["aws_sdk_glue.types.metadata_list.MetadataList"] = None,
        max_results: Optional[
            "aws_sdk_glue.types.query_schema_version_metadata_max_results.QuerySchemaVersionMetadataMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_glue.types.schema_registry_token_string.SchemaRegistryTokenString"
        ] = None,
    ) -> "aws_sdk_glue.types.query_schema_version_metadata_response.QuerySchemaVersionMetadataResponse":
        """<p>Queries for the schema version metadata information. </p>

        Args:
            schema_id: <p>A wrapper structure that may contain the schema name and Amazon Resource Name (ARN).</p>
            schema_version_number: <p>The version number of the schema.</p>
            schema_version_id: <p>The unique version ID of the schema version.</p>
            metadata_list: <p>Search key-value pairs for metadata, if they are not provided all the metadata information will be fetched.</p>
            max_results: <p>Maximum number of results required per page. If the value is not supplied, this will be defaulted to 25 per page.</p>
            next_token: <p>A continuation token, if this is a continuation call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.query_schema_version_metadata_input.QuerySchemaVersionMetadataInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.query_schema_version_metadata_response.QuerySchemaVersionMetadataResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.query_schema_version_metadata

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.query_schema_version_metadata.async_query_schema_version_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.query_schema_version_metadata_input.QuerySchemaVersionMetadataInput = {}  # type: ignore[typeddict-item]
        if schema_id is not None:
            input_["schema_id"] = schema_id
        if schema_version_number is not None:
            input_["schema_version_number"] = schema_version_number
        if schema_version_id is not None:
            input_["schema_version_id"] = schema_version_id
        if metadata_list is not None:
            input_["metadata_list"] = metadata_list
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

    async def register_connection_type(
        self,
        connection_type: "aws_sdk_glue.types.name_string.NameString",
        integration_type: "aws_sdk_glue.types.integration_type.IntegrationType",
        connection_properties: "aws_sdk_glue.types.connection_properties_configuration.ConnectionPropertiesConfiguration",
        connector_authentication_configuration: "aws_sdk_glue.types.connector_authentication_configuration.ConnectorAuthenticationConfiguration",
        rest_configuration: "aws_sdk_glue.types.rest_configuration.RestConfiguration",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        description: Optional["aws_sdk_glue.types.description.Description"] = None,
        tags: Optional["aws_sdk_glue.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_glue.types.register_connection_type_response.RegisterConnectionTypeResponse":
        r"""<p>Registers a custom connection type in Glue based on the configuration provided. This operation enables customers to configure custom connectors for any data source with REST-based APIs, eliminating the need for building custom Lambda connectors.</p> <p>The registered connection type stores details about how requests and responses are interpreted by REST sources, including connection properties, authentication configuration, and REST configuration with entity definitions. Once registered, customers can create connections using this connection type and work with them the same way as natively supported Glue connectors.</p> <p>Supports multiple authentication types including Basic, OAuth2 (Client Credentials, JWT Bearer, Authorization Code), and Custom Auth configurations.</p>

        Args:
            connection_type: <p>The name of the connection type. Must be between 1 and 255 characters and must be prefixed with \"REST-\" to indicate it is a REST-based connector.</p>
            integration_type: <p>The integration type for the connection. Currently only \"REST\" protocol is supported.</p>
            description: <p>A description of the connection type. Can be up to 2048 characters and provides details about the purpose and functionality of the connection type.</p>
            connection_properties: <p>Defines the base URL and additional request parameters needed during connection creation for this connection type.</p>
            connector_authentication_configuration: <p>Defines the supported authentication types and required properties for this connection type, including Basic, OAuth2, and Custom authentication methods.</p>
            rest_configuration: <p>Defines the HTTP request and response configuration, validation endpoint, and entity configurations for REST API interactions.</p>
            tags: <p>The tags you assign to the connection type.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.register_connection_type_request.RegisterConnectionTypeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.register_connection_type_response.RegisterConnectionTypeResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.register_connection_type

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.register_connection_type.async_register_connection_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.register_connection_type_request.RegisterConnectionTypeRequest = {}  # type: ignore[typeddict-item]
        input_["connection_type"] = connection_type
        input_["integration_type"] = integration_type
        if description is not None:
            input_["description"] = description
        input_["connection_properties"] = connection_properties
        input_["connector_authentication_configuration"] = (
            connector_authentication_configuration
        )
        input_["rest_configuration"] = rest_configuration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def register_schema_version(
        self,
        schema_id: "aws_sdk_glue.types.schema_id.SchemaId",
        schema_definition: "aws_sdk_glue.types.schema_definition_string.SchemaDefinitionString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.register_schema_version_response.RegisterSchemaVersionResponse":
        """<p>Adds a new version to the existing schema. Returns an error if new version of schema does not meet the compatibility requirements of the schema set. This API will not create a new schema set and will return a 404 error if the schema set is not already present in the Schema Registry.</p> <p>If this is the first schema definition to be registered in the Schema Registry, this API will store the schema version and return immediately. Otherwise, this call has the potential to run longer than other operations due to compatibility modes. You can call the <code>GetSchemaVersion</code> API with the <code>SchemaVersionId</code> to check compatibility modes.</p> <p>If the same schema definition is already stored in Schema Registry as a version, the schema ID of the existing schema is returned to the caller.</p>

        Args:
            schema_id: <p>This is a wrapper structure to contain schema identity fields. The structure contains:</p> <ul> <li> <p>SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. Either <code>SchemaArn</code> or <code>SchemaName</code> and <code>RegistryName</code> has to be provided.</p> </li> <li> <p>SchemaId$SchemaName: The name of the schema. Either <code>SchemaArn</code> or <code>SchemaName</code> and <code>RegistryName</code> has to be provided.</p> </li> </ul>
            schema_definition: <p>The schema definition using the <code>DataFormat</code> setting for the <code>SchemaName</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.register_schema_version_input.RegisterSchemaVersionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.register_schema_version_response.RegisterSchemaVersionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.register_schema_version

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.register_schema_version.async_register_schema_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.register_schema_version_input.RegisterSchemaVersionInput = {}  # type: ignore[typeddict-item]
        input_["schema_id"] = schema_id
        input_["schema_definition"] = schema_definition

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def remove_schema_version_metadata(
        self,
        metadata_key_value: "aws_sdk_glue.types.metadata_key_value_pair.MetadataKeyValuePair",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        schema_id: Optional["aws_sdk_glue.types.schema_id.SchemaId"] = None,
        schema_version_number: Optional[
            "aws_sdk_glue.types.schema_version_number.SchemaVersionNumber"
        ] = None,
        schema_version_id: Optional[
            "aws_sdk_glue.types.schema_version_id_string.SchemaVersionIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.remove_schema_version_metadata_response.RemoveSchemaVersionMetadataResponse":
        """<p>Removes a key value pair from the schema version metadata for the specified schema version ID.</p>

        Args:
            schema_id: <p>A wrapper structure that may contain the schema name and Amazon Resource Name (ARN).</p>
            schema_version_number: <p>The version number of the schema.</p>
            schema_version_id: <p>The unique version ID of the schema version.</p>
            metadata_key_value: <p>The value of the metadata key.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.remove_schema_version_metadata_input.RemoveSchemaVersionMetadataInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.remove_schema_version_metadata_response.RemoveSchemaVersionMetadataResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.remove_schema_version_metadata

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.remove_schema_version_metadata.async_remove_schema_version_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.remove_schema_version_metadata_input.RemoveSchemaVersionMetadataInput = {}  # type: ignore[typeddict-item]
        if schema_id is not None:
            input_["schema_id"] = schema_id
        if schema_version_number is not None:
            input_["schema_version_number"] = schema_version_number
        if schema_version_id is not None:
            input_["schema_version_id"] = schema_version_id
        input_["metadata_key_value"] = metadata_key_value

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def reset_job_bookmark(
        self,
        job_name: "aws_sdk_glue.types.job_name.JobName",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        run_id: Optional["aws_sdk_glue.types.run_id.RunId"] = None,
    ) -> "aws_sdk_glue.types.reset_job_bookmark_response.ResetJobBookmarkResponse":
        r"""<p>Resets a bookmark entry.</p> <p>For more information about enabling and using job bookmarks, see:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/glue/latest/dg/monitor-continuations.html\">Tracking processed data using job bookmarks</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html\">Job parameters used by Glue</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-job.html#aws-glue-api-jobs-job-Job\">Job structure</a> </p> </li> </ul>

        Args:
            job_name: <p>The name of the job in question.</p>
            run_id: <p>The unique run identifier associated with this job run.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.reset_job_bookmark_request.ResetJobBookmarkRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.reset_job_bookmark_response.ResetJobBookmarkResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.reset_job_bookmark

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.reset_job_bookmark.async_reset_job_bookmark(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.reset_job_bookmark_request.ResetJobBookmarkRequest = {}  # type: ignore[typeddict-item]
        input_["job_name"] = job_name
        if run_id is not None:
            input_["run_id"] = run_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def resume_workflow_run(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        run_id: "aws_sdk_glue.types.id_string.IdString",
        node_ids: "aws_sdk_glue.types.node_id_list.NodeIdList",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.resume_workflow_run_response.ResumeWorkflowRunResponse":
        """<p>Restarts selected nodes of a previous partially completed workflow run and resumes the workflow run. The selected nodes and all nodes that are downstream from the selected nodes are run.</p>

        Args:
            name: <p>The name of the workflow to resume.</p>
            run_id: <p>The ID of the workflow run to resume.</p>
            node_ids: <p>A list of the node IDs for the nodes you want to restart. The nodes that are to be restarted must have a run attempt in the original run.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.resume_workflow_run_request.ResumeWorkflowRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.resume_workflow_run_response.ResumeWorkflowRunResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.resume_workflow_run

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.resume_workflow_run.async_resume_workflow_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.resume_workflow_run_request.ResumeWorkflowRunRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["run_id"] = run_id
        input_["node_ids"] = node_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def run_statement(
        self,
        session_id: "aws_sdk_glue.types.name_string.NameString",
        code: "aws_sdk_glue.types.orchestration_statement_code_string.OrchestrationStatementCodeString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        request_origin: Optional[
            "aws_sdk_glue.types.orchestration_name_string.OrchestrationNameString"
        ] = None,
    ) -> "aws_sdk_glue.types.run_statement_response.RunStatementResponse":
        """<p>Executes the statement.</p>

        Args:
            session_id: <p>The Session Id of the statement to be run.</p>
            code: <p>The statement code to be run.</p>
            request_origin: <p>The origin of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.run_statement_request.RunStatementRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.run_statement_response.RunStatementResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.run_statement

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.run_statement.async_run_statement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.run_statement_request.RunStatementRequest = {}  # type: ignore[typeddict-item]
        input_["session_id"] = session_id
        input_["code"] = code
        if request_origin is not None:
            input_["request_origin"] = request_origin

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def search_tables(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
        next_token: Optional["aws_sdk_glue.types.token.Token"] = None,
        filters: Optional[
            "aws_sdk_glue.types.search_property_predicates.SearchPropertyPredicates"
        ] = None,
        search_text: Optional["aws_sdk_glue.types.value_string.ValueString"] = None,
        sort_criteria: Optional["aws_sdk_glue.types.sort_criteria.SortCriteria"] = None,
        max_results: Optional["aws_sdk_glue.types.page_size.PageSize"] = None,
        resource_share_type: Optional[
            "aws_sdk_glue.types.resource_share_type.ResourceShareType"
        ] = None,
        include_status_details: Optional[
            "aws_sdk_glue.types.boolean_nullable.BooleanNullable"
        ] = None,
    ) -> "aws_sdk_glue.types.search_tables_response.SearchTablesResponse":
        """<p>Searches a set of tables based on properties in the table metadata as well as on the parent database. You can search against text or filter conditions. </p> <p>You can only get tables that you have access to based on the security policies defined in Lake Formation. You need at least a read-only access to the table for it to be returned. If you do not have access to all the columns in the table, these columns will not be searched against when returning the list of tables back to you. If you have access to the columns but not the data in the columns, those columns and the associated metadata for those columns will be included in the search. </p>

        Args:
            catalog_id: <p>A unique identifier, consisting of <code> <i>account_id</i> </code>.</p>
            next_token: <p>A continuation token, included if this is a continuation call.</p>
            filters: <p>A list of key-value pairs, and a comparator used to filter the search results. Returns all entities matching the predicate.</p> <p>The <code>Comparator</code> member of the <code>PropertyPredicate</code> struct is used only for time fields, and can be omitted for other field types. Also, when comparing string values, such as when <code>Key=Name</code>, a fuzzy match algorithm is used. The <code>Key</code> field (for example, the value of the <code>Name</code> field) is split on certain punctuation characters, for example, -, :, #, etc. into tokens. Then each token is exact-match compared with the <code>Value</code> member of <code>PropertyPredicate</code>. For example, if <code>Key=Name</code> and <code>Value=link</code>, tables named <code>customer-link</code> and <code>xx-link-yy</code> are returned, but <code>xxlinkyy</code> is not returned.</p>
            search_text: <p>A string used for a text search.</p> <p>Specifying a value in quotes filters based on an exact match to the value.</p>
            sort_criteria: <p>A list of criteria for sorting the results by a field name, in an ascending or descending order.</p>
            max_results: <p>The maximum number of tables to return in a single response.</p>
            resource_share_type: <p>Allows you to specify that you want to search the tables shared with your account. The allowable values are <code>FOREIGN</code> or <code>ALL</code>. </p> <ul> <li> <p>If set to <code>FOREIGN</code>, will search the tables shared with your account. </p> </li> <li> <p>If set to <code>ALL</code>, will search the tables shared with your account, as well as the tables in yor local account. </p> </li> </ul>
            include_status_details: <p>Specifies whether to include status details related to a request to create or update an Glue Data Catalog view.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.search_tables_request.SearchTablesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.search_tables_response.SearchTablesResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.search_tables

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.search_tables.async_search_tables(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.search_tables_request.SearchTablesRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters
        if search_text is not None:
            input_["search_text"] = search_text
        if sort_criteria is not None:
            input_["sort_criteria"] = sort_criteria
        if max_results is not None:
            input_["max_results"] = max_results
        if resource_share_type is not None:
            input_["resource_share_type"] = resource_share_type
        if include_status_details is not None:
            input_["include_status_details"] = include_status_details

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_blueprint_run(
        self,
        blueprint_name: "aws_sdk_glue.types.orchestration_name_string.OrchestrationNameString",
        role_arn: "aws_sdk_glue.types.orchestration_iam_role_arn.OrchestrationIAMRoleArn",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        parameters: Optional[
            "aws_sdk_glue.types.blueprint_parameters.BlueprintParameters"
        ] = None,
    ) -> "aws_sdk_glue.types.start_blueprint_run_response.StartBlueprintRunResponse":
        """<p>Starts a new run of the specified blueprint.</p>

        Args:
            blueprint_name: <p>The name of the blueprint.</p>
            parameters: <p>Specifies the parameters as a <code>BlueprintParameters</code> object.</p>
            role_arn: <p>Specifies the IAM role used to create the workflow.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.start_blueprint_run_request.StartBlueprintRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.start_blueprint_run_response.StartBlueprintRunResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.start_blueprint_run

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.start_blueprint_run.async_start_blueprint_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.start_blueprint_run_request.StartBlueprintRunRequest = {}  # type: ignore[typeddict-item]
        input_["blueprint_name"] = blueprint_name
        if parameters is not None:
            input_["parameters"] = parameters
        input_["role_arn"] = role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_column_statistics_task_run(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        role: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        column_name_list: Optional[
            "aws_sdk_glue.types.column_name_list.ColumnNameList"
        ] = None,
        sample_size: Optional[
            "aws_sdk_glue.types.sample_size_percentage.SampleSizePercentage"
        ] = None,
        catalog_id: Optional["aws_sdk_glue.types.name_string.NameString"] = None,
        security_configuration: Optional[
            "aws_sdk_glue.types.name_string.NameString"
        ] = None,
    ) -> "aws_sdk_glue.types.start_column_statistics_task_run_response.StartColumnStatisticsTaskRunResponse":
        """<p>Starts a column statistics task run, for a specified table and columns.</p>

        Args:
            database_name: <p>The name of the database where the table resides.</p>
            table_name: <p>The name of the table to generate statistics.</p>
            column_name_list: <p>A list of the column names to generate statistics. If none is supplied, all column names for the table will be used by default.</p>
            role: <p>The IAM role that the service assumes to generate statistics.</p>
            sample_size: <p>The percentage of rows used to generate statistics. If none is supplied, the entire table will be used to generate stats.</p>
            catalog_id: <p>The ID of the Data Catalog where the table reside. If none is supplied, the Amazon Web Services account ID is used by default.</p>
            security_configuration: <p>Name of the security configuration that is used to encrypt CloudWatch logs for the column stats task run.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.start_column_statistics_task_run_request.StartColumnStatisticsTaskRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.start_column_statistics_task_run_response.StartColumnStatisticsTaskRunResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.start_column_statistics_task_run

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.start_column_statistics_task_run.async_start_column_statistics_task_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.start_column_statistics_task_run_request.StartColumnStatisticsTaskRunRequest = {}  # type: ignore[typeddict-item]
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        if column_name_list is not None:
            input_["column_name_list"] = column_name_list
        input_["role"] = role
        if sample_size is not None:
            input_["sample_size"] = sample_size
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        if security_configuration is not None:
            input_["security_configuration"] = security_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_column_statistics_task_run_schedule(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.start_column_statistics_task_run_schedule_response.StartColumnStatisticsTaskRunScheduleResponse":
        """<p>Starts a column statistics task run schedule.</p>

        Args:
            database_name: <p>The name of the database where the table resides.</p>
            table_name: <p>The name of the table for which to start a column statistic task run schedule.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.start_column_statistics_task_run_schedule_request.StartColumnStatisticsTaskRunScheduleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.start_column_statistics_task_run_schedule_response.StartColumnStatisticsTaskRunScheduleResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.start_column_statistics_task_run_schedule

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.start_column_statistics_task_run_schedule.async_start_column_statistics_task_run_schedule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.start_column_statistics_task_run_schedule_request.StartColumnStatisticsTaskRunScheduleRequest = {}  # type: ignore[typeddict-item]
        input_["database_name"] = database_name
        input_["table_name"] = table_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_crawler(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.start_crawler_response.StartCrawlerResponse":
        r"""<p>Starts a crawl using the specified crawler, regardless of what is scheduled. If the crawler is already running, returns a <a href=\"https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-exceptions.html#aws-glue-api-exceptions-CrawlerRunningException\">CrawlerRunningException</a>.</p>

        Args:
            name: <p>Name of the crawler to start.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.start_crawler_request.StartCrawlerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.start_crawler_response.StartCrawlerResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.start_crawler

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.start_crawler.async_start_crawler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.start_crawler_request.StartCrawlerRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_crawler_schedule(
        self,
        crawler_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.start_crawler_schedule_response.StartCrawlerScheduleResponse":
        """<p>Changes the schedule state of the specified crawler to <code>SCHEDULED</code>, unless the crawler is already running or the schedule state is already <code>SCHEDULED</code>.</p>

        Args:
            crawler_name: <p>Name of the crawler to schedule.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.start_crawler_schedule_request.StartCrawlerScheduleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.start_crawler_schedule_response.StartCrawlerScheduleResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.start_crawler_schedule

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.start_crawler_schedule.async_start_crawler_schedule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.start_crawler_schedule_request.StartCrawlerScheduleRequest = {}  # type: ignore[typeddict-item]
        input_["crawler_name"] = crawler_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_data_quality_rule_recommendation_run(
        self,
        data_source: "aws_sdk_glue.types.data_source.DataSource",
        role: "aws_sdk_glue.types.role_string.RoleString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        number_of_workers: Optional[
            "aws_sdk_glue.types.nullable_integer.NullableInteger"
        ] = None,
        timeout: Optional["aws_sdk_glue.types.timeout.Timeout"] = None,
        created_ruleset_name: Optional[
            "aws_sdk_glue.types.name_string.NameString"
        ] = None,
        data_quality_security_configuration: Optional[
            "aws_sdk_glue.types.name_string.NameString"
        ] = None,
        client_token: Optional["aws_sdk_glue.types.hash_string.HashString"] = None,
    ) -> "aws_sdk_glue.types.start_data_quality_rule_recommendation_run_response.StartDataQualityRuleRecommendationRunResponse":
        """<p>Starts a recommendation run that is used to generate rules when you don't know what rules to write. Glue Data Quality analyzes the data and comes up with recommendations for a potential ruleset. You can then triage the ruleset and modify the generated ruleset to your liking.</p> <p>Recommendation runs are automatically deleted after 90 days.</p>

        Args:
            data_source: <p>The data source (Glue table) associated with this run.</p>
            role: <p>An IAM role supplied to encrypt the results of the run.</p>
            number_of_workers: <p>The number of <code>G.1X</code> workers to be used in the run. The default is 5.</p>
            timeout: <p>The timeout for a run in minutes. This is the maximum time that a run can consume resources before it is terminated and enters <code>TIMEOUT</code> status. The default is 2,880 minutes (48 hours).</p>
            created_ruleset_name: <p>A name for the ruleset.</p>
            data_quality_security_configuration: <p>The name of the security configuration created with the data quality encryption option.</p>
            client_token: <p>Used for idempotency and is recommended to be set to a random ID (such as a UUID) to avoid creating or starting multiple instances of the same resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.start_data_quality_rule_recommendation_run_request.StartDataQualityRuleRecommendationRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.start_data_quality_rule_recommendation_run_response.StartDataQualityRuleRecommendationRunResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.start_data_quality_rule_recommendation_run

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.start_data_quality_rule_recommendation_run.async_start_data_quality_rule_recommendation_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.start_data_quality_rule_recommendation_run_request.StartDataQualityRuleRecommendationRunRequest = {}  # type: ignore[typeddict-item]
        input_["data_source"] = data_source
        input_["role"] = role
        if number_of_workers is not None:
            input_["number_of_workers"] = number_of_workers
        if timeout is not None:
            input_["timeout"] = timeout
        if created_ruleset_name is not None:
            input_["created_ruleset_name"] = created_ruleset_name
        if data_quality_security_configuration is not None:
            input_["data_quality_security_configuration"] = (
                data_quality_security_configuration
            )
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_data_quality_ruleset_evaluation_run(
        self,
        data_source: "aws_sdk_glue.types.data_source.DataSource",
        role: "aws_sdk_glue.types.role_string.RoleString",
        ruleset_names: "aws_sdk_glue.types.ruleset_names.RulesetNames",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        number_of_workers: Optional[
            "aws_sdk_glue.types.nullable_integer.NullableInteger"
        ] = None,
        timeout: Optional["aws_sdk_glue.types.timeout.Timeout"] = None,
        client_token: Optional["aws_sdk_glue.types.hash_string.HashString"] = None,
        additional_run_options: Optional[
            "aws_sdk_glue.types.data_quality_evaluation_run_additional_run_options.DataQualityEvaluationRunAdditionalRunOptions"
        ] = None,
        additional_data_sources: Optional[
            "aws_sdk_glue.types.data_source_map.DataSourceMap"
        ] = None,
    ) -> "aws_sdk_glue.types.start_data_quality_ruleset_evaluation_run_response.StartDataQualityRulesetEvaluationRunResponse":
        """<p>Once you have a ruleset definition (either recommended or your own), you call this operation to evaluate the ruleset against a data source (Glue table). The evaluation computes results which you can retrieve with the <code>GetDataQualityResult</code> API.</p>

        Args:
            data_source: <p>The data source (Glue table) associated with this run.</p>
            role: <p>An IAM role supplied to encrypt the results of the run.</p>
            number_of_workers: <p>The number of <code>G.1X</code> workers to be used in the run. The default is 5.</p>
            timeout: <p>The timeout for a run in minutes. This is the maximum time that a run can consume resources before it is terminated and enters <code>TIMEOUT</code> status. The default is 2,880 minutes (48 hours).</p>
            client_token: <p>Used for idempotency and is recommended to be set to a random ID (such as a UUID) to avoid creating or starting multiple instances of the same resource.</p>
            additional_run_options: <p>Additional run options you can specify for an evaluation run.</p>
            ruleset_names: <p>A list of ruleset names.</p>
            additional_data_sources: <p>A map of reference strings to additional data sources you can specify for an evaluation run.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.start_data_quality_ruleset_evaluation_run_request.StartDataQualityRulesetEvaluationRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.start_data_quality_ruleset_evaluation_run_response.StartDataQualityRulesetEvaluationRunResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.start_data_quality_ruleset_evaluation_run

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.start_data_quality_ruleset_evaluation_run.async_start_data_quality_ruleset_evaluation_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.start_data_quality_ruleset_evaluation_run_request.StartDataQualityRulesetEvaluationRunRequest = {}  # type: ignore[typeddict-item]
        input_["data_source"] = data_source
        input_["role"] = role
        if number_of_workers is not None:
            input_["number_of_workers"] = number_of_workers
        if timeout is not None:
            input_["timeout"] = timeout
        if client_token is not None:
            input_["client_token"] = client_token
        if additional_run_options is not None:
            input_["additional_run_options"] = additional_run_options
        input_["ruleset_names"] = ruleset_names
        if additional_data_sources is not None:
            input_["additional_data_sources"] = additional_data_sources

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_export_labels_task_run(
        self,
        transform_id: "aws_sdk_glue.types.hash_string.HashString",
        output_s3_path: "aws_sdk_glue.types.uri_string.UriString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.start_export_labels_task_run_response.StartExportLabelsTaskRunResponse":
        """<p>Begins an asynchronous task to export all labeled data for a particular transform. This task is the only label-related API call that is not part of the typical active learning workflow. You typically use <code>StartExportLabelsTaskRun</code> when you want to work with all of your existing labels at the same time, such as when you want to remove or change labels that were previously submitted as truth. This API operation accepts the <code>TransformId</code> whose labels you want to export and an Amazon Simple Storage Service (Amazon S3) path to export the labels to. The operation returns a <code>TaskRunId</code>. You can check on the status of your task run by calling the <code>GetMLTaskRun</code> API.</p>

        Args:
            transform_id: <p>The unique identifier of the machine learning transform.</p>
            output_s3_path: <p>The Amazon S3 path where you export the labels.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.start_export_labels_task_run_request.StartExportLabelsTaskRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.start_export_labels_task_run_response.StartExportLabelsTaskRunResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.start_export_labels_task_run

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.start_export_labels_task_run.async_start_export_labels_task_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.start_export_labels_task_run_request.StartExportLabelsTaskRunRequest = {}  # type: ignore[typeddict-item]
        input_["transform_id"] = transform_id
        input_["output_s3_path"] = output_s3_path

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_import_labels_task_run(
        self,
        transform_id: "aws_sdk_glue.types.hash_string.HashString",
        input_s3_path: "aws_sdk_glue.types.uri_string.UriString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        replace_all_labels: Optional[
            "aws_sdk_glue.types.replace_boolean.ReplaceBoolean"
        ] = None,
    ) -> "aws_sdk_glue.types.start_import_labels_task_run_response.StartImportLabelsTaskRunResponse":
        """<p>Enables you to provide additional labels (examples of truth) to be used to teach the machine learning transform and improve its quality. This API operation is generally used as part of the active learning workflow that starts with the <code>StartMLLabelingSetGenerationTaskRun</code> call and that ultimately results in improving the quality of your machine learning transform. </p> <p>After the <code>StartMLLabelingSetGenerationTaskRun</code> finishes, Glue machine learning will have generated a series of questions for humans to answer. (Answering these questions is often called 'labeling' in the machine learning workflows). In the case of the <code>FindMatches</code> transform, these questions are of the form, “What is the correct way to group these rows together into groups composed entirely of matching records?” After the labeling process is finished, users upload their answers/labels with a call to <code>StartImportLabelsTaskRun</code>. After <code>StartImportLabelsTaskRun</code> finishes, all future runs of the machine learning transform use the new and improved labels and perform a higher-quality transformation.</p> <p>By default, <code>StartMLLabelingSetGenerationTaskRun</code> continually learns from and combines all labels that you upload unless you set <code>Replace</code> to true. If you set <code>Replace</code> to true, <code>StartImportLabelsTaskRun</code> deletes and forgets all previously uploaded labels and learns only from the exact set that you upload. Replacing labels can be helpful if you realize that you previously uploaded incorrect labels, and you believe that they are having a negative effect on your transform quality.</p> <p>You can check on the status of your task run by calling the <code>GetMLTaskRun</code> operation. </p>

        Args:
            transform_id: <p>The unique identifier of the machine learning transform.</p>
            input_s3_path: <p>The Amazon Simple Storage Service (Amazon S3) path from where you import the labels.</p>
            replace_all_labels: <p>Indicates whether to overwrite your existing labels.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.start_import_labels_task_run_request.StartImportLabelsTaskRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.start_import_labels_task_run_response.StartImportLabelsTaskRunResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.start_import_labels_task_run

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.start_import_labels_task_run.async_start_import_labels_task_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.start_import_labels_task_run_request.StartImportLabelsTaskRunRequest = {}  # type: ignore[typeddict-item]
        input_["transform_id"] = transform_id
        input_["input_s3_path"] = input_s3_path
        if replace_all_labels is not None:
            input_["replace_all_labels"] = replace_all_labels

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_job_run(
        self,
        job_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        job_run_queuing_enabled: Optional[
            "aws_sdk_glue.types.nullable_boolean.NullableBoolean"
        ] = None,
        job_run_id: Optional["aws_sdk_glue.types.id_string.IdString"] = None,
        arguments: Optional["aws_sdk_glue.types.generic_map.GenericMap"] = None,
        allocated_capacity: Optional[
            "aws_sdk_glue.types.integer_value.IntegerValue"
        ] = None,
        timeout: Optional["aws_sdk_glue.types.timeout.Timeout"] = None,
        max_capacity: Optional[
            "aws_sdk_glue.types.nullable_double.NullableDouble"
        ] = None,
        security_configuration: Optional[
            "aws_sdk_glue.types.name_string.NameString"
        ] = None,
        notification_property: Optional[
            "aws_sdk_glue.types.notification_property.NotificationProperty"
        ] = None,
        worker_type: Optional["aws_sdk_glue.types.worker_type.WorkerType"] = None,
        number_of_workers: Optional[
            "aws_sdk_glue.types.nullable_integer.NullableInteger"
        ] = None,
        execution_class: Optional[
            "aws_sdk_glue.types.execution_class.ExecutionClass"
        ] = None,
        execution_role_session_policy: Optional[
            "aws_sdk_glue.types.orchestration_policy_json_string.OrchestrationPolicyJsonString"
        ] = None,
    ) -> "aws_sdk_glue.types.start_job_run_response.StartJobRunResponse":
        r"""<p>Starts a job run using a job definition.</p>

        Args:
            job_name: <p>The name of the job definition to use.</p>
            job_run_queuing_enabled: <p>Specifies whether job run queuing is enabled for the job run.</p> <p>A value of true means job run queuing is enabled for the job run. If false or not populated, the job run will not be considered for queueing.</p>
            job_run_id: <p>The ID of a previous <code>JobRun</code> to retry.</p>
            arguments: <p>The job arguments associated with this run. For this job run, they replace the default arguments set in the job definition itself.</p> <p>You can specify arguments here that your own job-execution script consumes, as well as arguments that Glue itself consumes.</p> <p>Job arguments may be logged. Do not pass plaintext secrets as arguments. Retrieve secrets from a Glue Connection, Secrets Manager or other secret management mechanism if you intend to keep them within the Job. </p> <p>For information about how to specify and consume your own Job arguments, see the <a href=\"https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html\">Calling Glue APIs in Python</a> topic in the developer guide.</p> <p>For information about the arguments you can provide to this field when configuring Spark jobs, see the <a href=\"https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html\">Special Parameters Used by Glue</a> topic in the developer guide.</p> <p>For information about the arguments you can provide to this field when configuring Ray jobs, see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/author-job-ray-job-parameters.html\">Using job parameters in Ray jobs</a> in the developer guide.</p>
            allocated_capacity: <p>This field is deprecated. Use <code>MaxCapacity</code> instead.</p> <p>The number of Glue data processing units (DPUs) to allocate to this JobRun. You can allocate a minimum of 2 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the <a href=\"https://aws.amazon.com/glue/pricing/\">Glue pricing page</a>.</p>
            timeout: <p>The <code>JobRun</code> timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters <code>TIMEOUT</code> status. This value overrides the timeout value set in the parent job. </p> <p>Jobs must have timeout values less than 7 days or 10080 minutes. Otherwise, the jobs will throw an exception.</p> <p>When the value is left blank, the timeout is defaulted to 2,880 minutes for Glue version 4.0 and earlier, or 480 minutes for Glue version 5.0 and later.</p> <p>Any existing Glue jobs that had a timeout value greater than 7 days will be defaulted to 7 days. For instance if you have specified a timeout of 20 days for a batch job, it will be stopped on the 7th day.</p> <p>For streaming jobs, if you have set up a maintenance window, it will be restarted during the maintenance window after 7 days.</p>
            max_capacity: <p>For Glue version 1.0 or earlier jobs, using the standard worker type, the number of Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the <a href=\"https://aws.amazon.com/glue/pricing/\"> Glue pricing page</a>.</p> <p>For Glue version 2.0+ jobs, you cannot specify a <code>Maximum capacity</code>. Instead, you should specify a <code>Worker type</code> and the <code>Number of workers</code>.</p> <p>Do not set <code>MaxCapacity</code> if using <code>WorkerType</code> and <code>NumberOfWorkers</code>.</p> <p>The value that can be allocated for <code>MaxCapacity</code> depends on whether you are running a Python shell job, an Apache Spark ETL job, or an Apache Spark streaming ETL job:</p> <ul> <li> <p>When you specify a Python shell job (<code>JobCommand.Name</code>=\"pythonshell\"), you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.</p> </li> <li> <p>When you specify an Apache Spark ETL job (<code>JobCommand.Name</code>=\"glueetl\") or Apache Spark streaming ETL job (<code>JobCommand.Name</code>=\"gluestreaming\"), you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.</p> </li> </ul>
            security_configuration: <p>The name of the <code>SecurityConfiguration</code> structure to be used with this job run.</p>
            notification_property: <p>Specifies configuration properties of a job run notification.</p>
            worker_type: <p>The type of predefined worker that is allocated when a job runs. Accepts a value of G.1X, G.2X, G.4X, G.8X or G.025X for Spark jobs. Accepts the value Z.2X for Ray jobs.</p> <ul> <li> <p>For the <code>G.1X</code> worker type, each worker maps to 1 DPU (4 vCPUs, 16 GB of memory) with 94GB disk, and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs.</p> </li> <li> <p>For the <code>G.2X</code> worker type, each worker maps to 2 DPU (8 vCPUs, 32 GB of memory) with 138GB disk, and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs.</p> </li> <li> <p>For the <code>G.4X</code> worker type, each worker maps to 4 DPU (16 vCPUs, 64 GB of memory) with 256GB disk, and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for Glue version 3.0 or later Spark ETL jobs in the following Amazon Web Services Regions: US East (Ohio), US East (N. Virginia), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central), Europe (Frankfurt), Europe (Ireland), and Europe (Stockholm).</p> </li> <li> <p>For the <code>G.8X</code> worker type, each worker maps to 8 DPU (32 vCPUs, 128 GB of memory) with 512GB disk, and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for Glue version 3.0 or later Spark ETL jobs, in the same Amazon Web Services Regions as supported for the <code>G.4X</code> worker type.</p> </li> <li> <p>For the <code>G.025X</code> worker type, each worker maps to 0.25 DPU (2 vCPUs, 4 GB of memory) with 84GB disk, and provides 1 executor per worker. We recommend this worker type for low volume streaming jobs. This worker type is only available for Glue version 3.0 or later streaming jobs.</p> </li> <li> <p>For the <code>Z.2X</code> worker type, each worker maps to 2 M-DPU (8vCPUs, 64 GB of memory) with 128 GB disk, and provides up to 8 Ray workers based on the autoscaler.</p> </li> </ul>
            number_of_workers: <p>The number of workers of a defined <code>workerType</code> that are allocated when a job runs.</p>
            execution_class: <p>Indicates whether the job is run with a standard or flexible execution class. The standard execution-class is ideal for time-sensitive workloads that require fast job startup and dedicated resources.</p> <p>The flexible execution class is appropriate for time-insensitive jobs whose start and completion times may vary. </p> <p>Only jobs with Glue version 3.0 and above and command type <code>glueetl</code> will be allowed to set <code>ExecutionClass</code> to <code>FLEX</code>. The flexible execution class is available for Spark jobs.</p>
            execution_role_session_policy: <p>This inline session policy to the StartJobRun API allows you to dynamically restrict the permissions of the specified execution role for the scope of the job, without requiring the creation of additional IAM roles.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.start_job_run_request.StartJobRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.start_job_run_response.StartJobRunResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.start_job_run

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.start_job_run.async_start_job_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.start_job_run_request.StartJobRunRequest = {}  # type: ignore[typeddict-item]
        input_["job_name"] = job_name
        if job_run_queuing_enabled is not None:
            input_["job_run_queuing_enabled"] = job_run_queuing_enabled
        if job_run_id is not None:
            input_["job_run_id"] = job_run_id
        if arguments is not None:
            input_["arguments"] = arguments
        if allocated_capacity is not None:
            input_["allocated_capacity"] = allocated_capacity
        if timeout is not None:
            input_["timeout"] = timeout
        if max_capacity is not None:
            input_["max_capacity"] = max_capacity
        if security_configuration is not None:
            input_["security_configuration"] = security_configuration
        if notification_property is not None:
            input_["notification_property"] = notification_property
        if worker_type is not None:
            input_["worker_type"] = worker_type
        if number_of_workers is not None:
            input_["number_of_workers"] = number_of_workers
        if execution_class is not None:
            input_["execution_class"] = execution_class
        if execution_role_session_policy is not None:
            input_["execution_role_session_policy"] = execution_role_session_policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_materialized_view_refresh_task_run(
        self,
        catalog_id: "aws_sdk_glue.types.name_string.NameString",
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        full_refresh: Optional[
            "aws_sdk_glue.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "aws_sdk_glue.types.start_materialized_view_refresh_task_run_response.StartMaterializedViewRefreshTaskRunResponse":
        """<p>Starts a materialized view refresh task run, for a specified table and columns.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog where the table reside. If none is supplied, the account ID is used by default.</p>
            database_name: <p>The name of the database where the table resides.</p>
            table_name: <p>The name of the table to generate run the materialized view refresh task.</p>
            full_refresh: <p>Specifies whether this is a full refresh of the task run.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.start_materialized_view_refresh_task_run_request.StartMaterializedViewRefreshTaskRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.start_materialized_view_refresh_task_run_response.StartMaterializedViewRefreshTaskRunResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.start_materialized_view_refresh_task_run

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.start_materialized_view_refresh_task_run.async_start_materialized_view_refresh_task_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.start_materialized_view_refresh_task_run_request.StartMaterializedViewRefreshTaskRunRequest = {}  # type: ignore[typeddict-item]
        input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        if full_refresh is not None:
            input_["full_refresh"] = full_refresh

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_ml_evaluation_task_run(
        self,
        transform_id: "aws_sdk_glue.types.hash_string.HashString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.start_ml_evaluation_task_run_response.StartMLEvaluationTaskRunResponse":
        """<p>Starts a task to estimate the quality of the transform. </p> <p>When you provide label sets as examples of truth, Glue machine learning uses some of those examples to learn from them. The rest of the labels are used as a test to estimate quality.</p> <p>Returns a unique identifier for the run. You can call <code>GetMLTaskRun</code> to get more information about the stats of the <code>EvaluationTaskRun</code>.</p>

        Args:
            transform_id: <p>The unique identifier of the machine learning transform.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.start_ml_evaluation_task_run_request.StartMLEvaluationTaskRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.start_ml_evaluation_task_run_response.StartMLEvaluationTaskRunResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.start_ml_evaluation_task_run

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.start_ml_evaluation_task_run.async_start_ml_evaluation_task_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.start_ml_evaluation_task_run_request.StartMLEvaluationTaskRunRequest = {}  # type: ignore[typeddict-item]
        input_["transform_id"] = transform_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_ml_labeling_set_generation_task_run(
        self,
        transform_id: "aws_sdk_glue.types.hash_string.HashString",
        output_s3_path: "aws_sdk_glue.types.uri_string.UriString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.start_ml_labeling_set_generation_task_run_response.StartMLLabelingSetGenerationTaskRunResponse":
        r"""<p>Starts the active learning workflow for your machine learning transform to improve the transform's quality by generating label sets and adding labels.</p> <p>When the <code>StartMLLabelingSetGenerationTaskRun</code> finishes, Glue will have generated a \"labeling set\" or a set of questions for humans to answer.</p> <p>In the case of the <code>FindMatches</code> transform, these questions are of the form, “What is the correct way to group these rows together into groups composed entirely of matching records?” </p> <p>After the labeling process is finished, you can upload your labels with a call to <code>StartImportLabelsTaskRun</code>. After <code>StartImportLabelsTaskRun</code> finishes, all future runs of the machine learning transform will use the new and improved labels and perform a higher-quality transformation.</p> <p>Note: The role used to write the generated labeling set to the <code>OutputS3Path</code> is the role associated with the Machine Learning Transform, specified in the <code>CreateMLTransform</code> API.</p>

        Args:
            transform_id: <p>The unique identifier of the machine learning transform.</p>
            output_s3_path: <p>The Amazon Simple Storage Service (Amazon S3) path where you generate the labeling set.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.start_ml_labeling_set_generation_task_run_request.StartMLLabelingSetGenerationTaskRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.start_ml_labeling_set_generation_task_run_response.StartMLLabelingSetGenerationTaskRunResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.start_ml_labeling_set_generation_task_run

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.start_ml_labeling_set_generation_task_run.async_start_ml_labeling_set_generation_task_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.start_ml_labeling_set_generation_task_run_request.StartMLLabelingSetGenerationTaskRunRequest = {}  # type: ignore[typeddict-item]
        input_["transform_id"] = transform_id
        input_["output_s3_path"] = output_s3_path

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_trigger(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.start_trigger_response.StartTriggerResponse":
        r"""<p>Starts an existing trigger. See <a href=\"https://docs.aws.amazon.com/glue/latest/dg/trigger-job.html\">Triggering Jobs</a> for information about how different types of trigger are started.</p>

        Args:
            name: <p>The name of the trigger to start.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.start_trigger_request.StartTriggerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.start_trigger_response.StartTriggerResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.start_trigger

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.start_trigger.async_start_trigger(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.start_trigger_request.StartTriggerRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_workflow_run(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        run_properties: Optional[
            "aws_sdk_glue.types.workflow_run_properties.WorkflowRunProperties"
        ] = None,
    ) -> "aws_sdk_glue.types.start_workflow_run_response.StartWorkflowRunResponse":
        """<p>Starts a new run of the specified workflow.</p>

        Args:
            name: <p>The name of the workflow to start.</p>
            run_properties: <p>The workflow run properties for the new workflow run.</p> <p>Run properties may be logged. Do not pass plaintext secrets as properties. Retrieve secrets from a Glue Connection, Amazon Web Services Secrets Manager or other secret management mechanism if you intend to use them within the workflow run.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.start_workflow_run_request.StartWorkflowRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.start_workflow_run_response.StartWorkflowRunResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.start_workflow_run

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.start_workflow_run.async_start_workflow_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.start_workflow_run_request.StartWorkflowRunRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if run_properties is not None:
            input_["run_properties"] = run_properties

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_column_statistics_task_run(
        self,
        database_name: "aws_sdk_glue.types.database_name.DatabaseName",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.stop_column_statistics_task_run_response.StopColumnStatisticsTaskRunResponse":
        """<p>Stops a task run for the specified table.</p>

        Args:
            database_name: <p>The name of the database where the table resides.</p>
            table_name: <p>The name of the table.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.stop_column_statistics_task_run_request.StopColumnStatisticsTaskRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.stop_column_statistics_task_run_response.StopColumnStatisticsTaskRunResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.stop_column_statistics_task_run

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.stop_column_statistics_task_run.async_stop_column_statistics_task_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.stop_column_statistics_task_run_request.StopColumnStatisticsTaskRunRequest = {}  # type: ignore[typeddict-item]
        input_["database_name"] = database_name
        input_["table_name"] = table_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_column_statistics_task_run_schedule(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.stop_column_statistics_task_run_schedule_response.StopColumnStatisticsTaskRunScheduleResponse":
        """<p>Stops a column statistics task run schedule.</p>

        Args:
            database_name: <p>The name of the database where the table resides.</p>
            table_name: <p>The name of the table for which to stop a column statistic task run schedule.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.stop_column_statistics_task_run_schedule_request.StopColumnStatisticsTaskRunScheduleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.stop_column_statistics_task_run_schedule_response.StopColumnStatisticsTaskRunScheduleResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.stop_column_statistics_task_run_schedule

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.stop_column_statistics_task_run_schedule.async_stop_column_statistics_task_run_schedule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.stop_column_statistics_task_run_schedule_request.StopColumnStatisticsTaskRunScheduleRequest = {}  # type: ignore[typeddict-item]
        input_["database_name"] = database_name
        input_["table_name"] = table_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_crawler(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.stop_crawler_response.StopCrawlerResponse":
        """<p>If the specified crawler is running, stops the crawl.</p>

        Args:
            name: <p>Name of the crawler to stop.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.stop_crawler_request.StopCrawlerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.stop_crawler_response.StopCrawlerResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.stop_crawler

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.stop_crawler.async_stop_crawler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.stop_crawler_request.StopCrawlerRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_crawler_schedule(
        self,
        crawler_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> (
        "aws_sdk_glue.types.stop_crawler_schedule_response.StopCrawlerScheduleResponse"
    ):
        """<p>Sets the schedule state of the specified crawler to <code>NOT_SCHEDULED</code>, but does not stop the crawler if it is already running.</p>

        Args:
            crawler_name: <p>Name of the crawler whose schedule state to set.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.stop_crawler_schedule_request.StopCrawlerScheduleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.stop_crawler_schedule_response.StopCrawlerScheduleResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.stop_crawler_schedule

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.stop_crawler_schedule.async_stop_crawler_schedule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.stop_crawler_schedule_request.StopCrawlerScheduleRequest = {}  # type: ignore[typeddict-item]
        input_["crawler_name"] = crawler_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_materialized_view_refresh_task_run(
        self,
        catalog_id: "aws_sdk_glue.types.name_string.NameString",
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.stop_materialized_view_refresh_task_run_response.StopMaterializedViewRefreshTaskRunResponse":
        """<p>Stops a materialized view refresh task run, for a specified table and columns.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog where the table reside. If none is supplied, the account ID is used by default.</p>
            database_name: <p>The name of the database where the table resides.</p>
            table_name: <p>The name of the table to generate statistics.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.stop_materialized_view_refresh_task_run_request.StopMaterializedViewRefreshTaskRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.stop_materialized_view_refresh_task_run_response.StopMaterializedViewRefreshTaskRunResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.stop_materialized_view_refresh_task_run

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.stop_materialized_view_refresh_task_run.async_stop_materialized_view_refresh_task_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.stop_materialized_view_refresh_task_run_request.StopMaterializedViewRefreshTaskRunRequest = {}  # type: ignore[typeddict-item]
        input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_session(
        self,
        id: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        request_origin: Optional[
            "aws_sdk_glue.types.orchestration_name_string.OrchestrationNameString"
        ] = None,
    ) -> "aws_sdk_glue.types.stop_session_response.StopSessionResponse":
        """<p>Stops the session.</p>

        Args:
            id: <p>The ID of the session to be stopped.</p>
            request_origin: <p>The origin of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.stop_session_request.StopSessionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.stop_session_response.StopSessionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.stop_session

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.stop_session.async_stop_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.stop_session_request.StopSessionRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if request_origin is not None:
            input_["request_origin"] = request_origin

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_trigger(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.stop_trigger_response.StopTriggerResponse":
        """<p>Stops a specified trigger.</p>

        Args:
            name: <p>The name of the trigger to stop.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.stop_trigger_request.StopTriggerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.stop_trigger_response.StopTriggerResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.stop_trigger

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.stop_trigger.async_stop_trigger(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.stop_trigger_request.StopTriggerRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_workflow_run(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        run_id: "aws_sdk_glue.types.id_string.IdString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.stop_workflow_run_response.StopWorkflowRunResponse":
        """<p>Stops the execution of the specified workflow run.</p>

        Args:
            name: <p>The name of the workflow to stop.</p>
            run_id: <p>The ID of the workflow run to stop.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.stop_workflow_run_request.StopWorkflowRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.stop_workflow_run_response.StopWorkflowRunResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.stop_workflow_run

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.stop_workflow_run.async_stop_workflow_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.stop_workflow_run_request.StopWorkflowRunRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["run_id"] = run_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_glue.types.glue_resource_arn.GlueResourceArn",
        tags_to_add: "aws_sdk_glue.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.tag_resource_response.TagResourceResponse":
        r"""<p>Adds tags to a resource. A tag is a label you can assign to an Amazon Web Services resource. In Glue, you can tag only certain resources. For information about what resources you can tag, see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html\">Amazon Web Services Tags in Glue</a>.</p>

        Args:
            resource_arn: <p>The ARN of the Glue resource to which to add the tags. For more information about Glue resource ARNs, see the <a href=\"https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-common.html#aws-glue-api-regex-aws-glue-arn-id\">Glue ARN string pattern</a>.</p>
            tags_to_add: <p>Tags to add to this resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags_to_add"] = tags_to_add

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def test_connection(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        connection_name: Optional["aws_sdk_glue.types.name_string.NameString"] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
        test_connection_input: Optional[
            "aws_sdk_glue.types.test_connection_input.TestConnectionInput"
        ] = None,
    ) -> "aws_sdk_glue.types.test_connection_response.TestConnectionResponse":
        """<p>Tests a connection to a service to validate the service credentials that you provide.</p> <p>You can either provide an existing connection name or a <code>TestConnectionInput</code> for testing a non-existing connection input. Providing both at the same time will cause an error.</p> <p>If the action is successful, the service sends back an HTTP 200 response.</p>

        Args:
            connection_name: <p>Optional. The name of the connection to test. If only name is provided, the operation will get the connection and use that for testing.</p>
            catalog_id: <p>The catalog ID where the connection resides.</p>
            test_connection_input: <p>A structure that is used to specify testing a connection to a service.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.test_connection_request.TestConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.test_connection_response.TestConnectionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.test_connection

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.test_connection.async_test_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.test_connection_request.TestConnectionRequest = {}  # type: ignore[typeddict-item]
        if connection_name is not None:
            input_["connection_name"] = connection_name
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        if test_connection_input is not None:
            input_["test_connection_input"] = test_connection_input

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_glue.types.glue_resource_arn.GlueResourceArn",
        tags_to_remove: "aws_sdk_glue.types.tag_keys_list.TagKeysList",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource from which to remove the tags.</p>
            tags_to_remove: <p>Tags to remove from this resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags_to_remove"] = tags_to_remove

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_blueprint(
        self,
        name: "aws_sdk_glue.types.orchestration_name_string.OrchestrationNameString",
        blueprint_location: "aws_sdk_glue.types.orchestration_s3_location.OrchestrationS3Location",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        description: Optional[
            "aws_sdk_glue.types.generic512_char_string.Generic512CharString"
        ] = None,
    ) -> "aws_sdk_glue.types.update_blueprint_response.UpdateBlueprintResponse":
        """<p>Updates a registered blueprint.</p>

        Args:
            name: <p>The name of the blueprint.</p>
            description: <p>A description of the blueprint.</p>
            blueprint_location: <p>Specifies a path in Amazon S3 where the blueprint is published.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.update_blueprint_request.UpdateBlueprintRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.update_blueprint_response.UpdateBlueprintResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.update_blueprint

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.update_blueprint.async_update_blueprint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.update_blueprint_request.UpdateBlueprintRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["blueprint_location"] = blueprint_location

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_catalog(
        self,
        catalog_id: "aws_sdk_glue.types.catalog_id_string.CatalogIdString",
        catalog_input: "aws_sdk_glue.types.catalog_input.CatalogInput",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.update_catalog_response.UpdateCatalogResponse":
        """<p>Updates an existing catalog's properties in the Glue Data Catalog.</p>

        Args:
            catalog_id: <p>The ID of the catalog.</p>
            catalog_input: <p>A <code>CatalogInput</code> object specifying the new properties of an existing catalog.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.update_catalog_request.UpdateCatalogRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.update_catalog_response.UpdateCatalogResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.update_catalog

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.update_catalog.async_update_catalog(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.update_catalog_request.UpdateCatalogRequest = {}  # type: ignore[typeddict-item]
        input_["catalog_id"] = catalog_id
        input_["catalog_input"] = catalog_input

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_classifier(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        grok_classifier: Optional[
            "aws_sdk_glue.types.update_grok_classifier_request.UpdateGrokClassifierRequest"
        ] = None,
        xml_classifier: Optional[
            "aws_sdk_glue.types.update_xml_classifier_request.UpdateXMLClassifierRequest"
        ] = None,
        json_classifier: Optional[
            "aws_sdk_glue.types.update_json_classifier_request.UpdateJsonClassifierRequest"
        ] = None,
        csv_classifier: Optional[
            "aws_sdk_glue.types.update_csv_classifier_request.UpdateCsvClassifierRequest"
        ] = None,
    ) -> "aws_sdk_glue.types.update_classifier_response.UpdateClassifierResponse":
        """<p>Modifies an existing classifier (a <code>GrokClassifier</code>, an <code>XMLClassifier</code>, a <code>JsonClassifier</code>, or a <code>CsvClassifier</code>, depending on which field is present).</p>

        Args:
            grok_classifier: <p>A <code>GrokClassifier</code> object with updated fields.</p>
            xml_classifier: <p>An <code>XMLClassifier</code> object with updated fields.</p>
            json_classifier: <p>A <code>JsonClassifier</code> object with updated fields.</p>
            csv_classifier: <p>A <code>CsvClassifier</code> object with updated fields.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.update_classifier_request.UpdateClassifierRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.update_classifier_response.UpdateClassifierResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.update_classifier

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.update_classifier.async_update_classifier(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.update_classifier_request.UpdateClassifierRequest = {}  # type: ignore[typeddict-item]
        if grok_classifier is not None:
            input_["grok_classifier"] = grok_classifier
        if xml_classifier is not None:
            input_["xml_classifier"] = xml_classifier
        if json_classifier is not None:
            input_["json_classifier"] = json_classifier
        if csv_classifier is not None:
            input_["csv_classifier"] = csv_classifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_column_statistics_for_partition(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        partition_values: "aws_sdk_glue.types.value_string_list.ValueStringList",
        column_statistics_list: "aws_sdk_glue.types.update_column_statistics_list.UpdateColumnStatisticsList",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.update_column_statistics_for_partition_response.UpdateColumnStatisticsForPartitionResponse":
        """<p>Creates or updates partition statistics of columns.</p> <p>The Identity and Access Management (IAM) permission required for this operation is <code>UpdatePartition</code>.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog where the partitions in question reside. If none is supplied, the Amazon Web Services account ID is used by default.</p>
            database_name: <p>The name of the catalog database where the partitions reside.</p>
            table_name: <p>The name of the partitions' table.</p>
            partition_values: <p>A list of partition values identifying the partition.</p>
            column_statistics_list: <p>A list of the column statistics.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.update_column_statistics_for_partition_request.UpdateColumnStatisticsForPartitionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.update_column_statistics_for_partition_response.UpdateColumnStatisticsForPartitionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.update_column_statistics_for_partition

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.update_column_statistics_for_partition.async_update_column_statistics_for_partition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.update_column_statistics_for_partition_request.UpdateColumnStatisticsForPartitionRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        input_["partition_values"] = partition_values
        input_["column_statistics_list"] = column_statistics_list

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_column_statistics_for_table(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        column_statistics_list: "aws_sdk_glue.types.update_column_statistics_list.UpdateColumnStatisticsList",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.update_column_statistics_for_table_response.UpdateColumnStatisticsForTableResponse":
        """<p>Creates or updates table statistics of columns.</p> <p>The Identity and Access Management (IAM) permission required for this operation is <code>UpdateTable</code>.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog where the partitions in question reside. If none is supplied, the Amazon Web Services account ID is used by default.</p>
            database_name: <p>The name of the catalog database where the partitions reside.</p>
            table_name: <p>The name of the partitions' table.</p>
            column_statistics_list: <p>A list of the column statistics.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.update_column_statistics_for_table_request.UpdateColumnStatisticsForTableRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.update_column_statistics_for_table_response.UpdateColumnStatisticsForTableResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.update_column_statistics_for_table

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.update_column_statistics_for_table.async_update_column_statistics_for_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.update_column_statistics_for_table_request.UpdateColumnStatisticsForTableRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        input_["column_statistics_list"] = column_statistics_list

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_column_statistics_task_settings(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        role: Optional["aws_sdk_glue.types.name_string.NameString"] = None,
        schedule: Optional["aws_sdk_glue.types.cron_expression.CronExpression"] = None,
        column_name_list: Optional[
            "aws_sdk_glue.types.column_name_list.ColumnNameList"
        ] = None,
        sample_size: Optional[
            "aws_sdk_glue.types.sample_size_percentage.SampleSizePercentage"
        ] = None,
        catalog_id: Optional["aws_sdk_glue.types.name_string.NameString"] = None,
        security_configuration: Optional[
            "aws_sdk_glue.types.name_string.NameString"
        ] = None,
    ) -> "aws_sdk_glue.types.update_column_statistics_task_settings_response.UpdateColumnStatisticsTaskSettingsResponse":
        """<p>Updates settings for a column statistics task.</p>

        Args:
            database_name: <p>The name of the database where the table resides.</p>
            table_name: <p>The name of the table for which to generate column statistics.</p>
            role: <p>The role used for running the column statistics.</p>
            schedule: <p>A schedule for running the column statistics, specified in CRON syntax.</p>
            column_name_list: <p>A list of column names for which to run statistics.</p>
            sample_size: <p>The percentage of data to sample.</p>
            catalog_id: <p>The ID of the Data Catalog in which the database resides.</p>
            security_configuration: <p>Name of the security configuration that is used to encrypt CloudWatch logs.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.update_column_statistics_task_settings_request.UpdateColumnStatisticsTaskSettingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.update_column_statistics_task_settings_response.UpdateColumnStatisticsTaskSettingsResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.update_column_statistics_task_settings

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.update_column_statistics_task_settings.async_update_column_statistics_task_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.update_column_statistics_task_settings_request.UpdateColumnStatisticsTaskSettingsRequest = {}  # type: ignore[typeddict-item]
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        if role is not None:
            input_["role"] = role
        if schedule is not None:
            input_["schedule"] = schedule
        if column_name_list is not None:
            input_["column_name_list"] = column_name_list
        if sample_size is not None:
            input_["sample_size"] = sample_size
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        if security_configuration is not None:
            input_["security_configuration"] = security_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_connection(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        connection_input: "aws_sdk_glue.types.connection_input.ConnectionInput",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.update_connection_response.UpdateConnectionResponse":
        """<p>Updates a connection definition in the Data Catalog.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog in which the connection resides. If none is provided, the Amazon Web Services account ID is used by default.</p>
            name: <p>The name of the connection definition to update.</p>
            connection_input: <p>A <code>ConnectionInput</code> object that redefines the connection in question.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.update_connection_request.UpdateConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.update_connection_response.UpdateConnectionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.update_connection

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.update_connection.async_update_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.update_connection_request.UpdateConnectionRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["name"] = name
        input_["connection_input"] = connection_input

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_crawler(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        role: Optional["aws_sdk_glue.types.role.Role"] = None,
        database_name: Optional["aws_sdk_glue.types.database_name.DatabaseName"] = None,
        description: Optional[
            "aws_sdk_glue.types.description_string_removable.DescriptionStringRemovable"
        ] = None,
        targets: Optional["aws_sdk_glue.types.crawler_targets.CrawlerTargets"] = None,
        schedule: Optional["aws_sdk_glue.types.cron_expression.CronExpression"] = None,
        classifiers: Optional[
            "aws_sdk_glue.types.classifier_name_list.ClassifierNameList"
        ] = None,
        table_prefix: Optional["aws_sdk_glue.types.table_prefix.TablePrefix"] = None,
        schema_change_policy: Optional[
            "aws_sdk_glue.types.schema_change_policy.SchemaChangePolicy"
        ] = None,
        recrawl_policy: Optional[
            "aws_sdk_glue.types.recrawl_policy.RecrawlPolicy"
        ] = None,
        lineage_configuration: Optional[
            "aws_sdk_glue.types.lineage_configuration.LineageConfiguration"
        ] = None,
        lake_formation_configuration: Optional[
            "aws_sdk_glue.types.lake_formation_configuration.LakeFormationConfiguration"
        ] = None,
        configuration: Optional[
            "aws_sdk_glue.types.crawler_configuration.CrawlerConfiguration"
        ] = None,
        crawler_security_configuration: Optional[
            "aws_sdk_glue.types.crawler_security_configuration.CrawlerSecurityConfiguration"
        ] = None,
    ) -> "aws_sdk_glue.types.update_crawler_response.UpdateCrawlerResponse":
        r"""<p>Updates a crawler. If a crawler is running, you must stop it using <code>StopCrawler</code> before updating it.</p>

        Args:
            name: <p>Name of the new crawler.</p>
            role: <p>The IAM role or Amazon Resource Name (ARN) of an IAM role that is used by the new crawler to access customer resources.</p>
            database_name: <p>The Glue database where results are stored, such as: <code>arn:aws:daylight:us-east-1::database/sometable/*</code>.</p>
            description: <p>A description of the new crawler.</p>
            targets: <p>A list of targets to crawl.</p>
            schedule: <p>A <code>cron</code> expression used to specify the schedule (see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html\">Time-Based Schedules for Jobs and Crawlers</a>. For example, to run something every day at 12:15 UTC, you would specify: <code>cron(15 12 * * ? *)</code>.</p>
            classifiers: <p>A list of custom classifiers that the user has registered. By default, all built-in classifiers are included in a crawl, but these custom classifiers always override the default classifiers for a given classification.</p>
            table_prefix: <p>The table prefix used for catalog tables that are created.</p>
            schema_change_policy: <p>The policy for the crawler's update and deletion behavior.</p>
            recrawl_policy: <p>A policy that specifies whether to crawl the entire dataset again, or to crawl only folders that were added since the last crawler run.</p>
            lineage_configuration: <p>Specifies data lineage configuration settings for the crawler.</p>
            lake_formation_configuration: <p>Specifies Lake Formation configuration settings for the crawler.</p>
            configuration: <p>Crawler configuration information. This versioned JSON string allows users to specify aspects of a crawler's behavior. For more information, see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/crawler-configuration.html\">Setting crawler configuration options</a>.</p>
            crawler_security_configuration: <p>The name of the <code>SecurityConfiguration</code> structure to be used by this crawler.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.update_crawler_request.UpdateCrawlerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.update_crawler_response.UpdateCrawlerResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.update_crawler

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.update_crawler.async_update_crawler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.update_crawler_request.UpdateCrawlerRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if role is not None:
            input_["role"] = role
        if database_name is not None:
            input_["database_name"] = database_name
        if description is not None:
            input_["description"] = description
        if targets is not None:
            input_["targets"] = targets
        if schedule is not None:
            input_["schedule"] = schedule
        if classifiers is not None:
            input_["classifiers"] = classifiers
        if table_prefix is not None:
            input_["table_prefix"] = table_prefix
        if schema_change_policy is not None:
            input_["schema_change_policy"] = schema_change_policy
        if recrawl_policy is not None:
            input_["recrawl_policy"] = recrawl_policy
        if lineage_configuration is not None:
            input_["lineage_configuration"] = lineage_configuration
        if lake_formation_configuration is not None:
            input_["lake_formation_configuration"] = lake_formation_configuration
        if configuration is not None:
            input_["configuration"] = configuration
        if crawler_security_configuration is not None:
            input_["crawler_security_configuration"] = crawler_security_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_crawler_schedule(
        self,
        crawler_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        schedule: Optional["aws_sdk_glue.types.cron_expression.CronExpression"] = None,
    ) -> "aws_sdk_glue.types.update_crawler_schedule_response.UpdateCrawlerScheduleResponse":
        r"""<p>Updates the schedule of a crawler using a <code>cron</code> expression. </p>

        Args:
            crawler_name: <p>The name of the crawler whose schedule to update.</p>
            schedule: <p>The updated <code>cron</code> expression used to specify the schedule (see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html\">Time-Based Schedules for Jobs and Crawlers</a>. For example, to run something every day at 12:15 UTC, you would specify: <code>cron(15 12 * * ? *)</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.update_crawler_schedule_request.UpdateCrawlerScheduleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.update_crawler_schedule_response.UpdateCrawlerScheduleResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.update_crawler_schedule

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.update_crawler_schedule.async_update_crawler_schedule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.update_crawler_schedule_request.UpdateCrawlerScheduleRequest = {}  # type: ignore[typeddict-item]
        input_["crawler_name"] = crawler_name
        if schedule is not None:
            input_["schedule"] = schedule

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_database(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        database_input: "aws_sdk_glue.types.database_input.DatabaseInput",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.update_database_response.UpdateDatabaseResponse":
        """<p>Updates an existing database definition in a Data Catalog.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog in which the metadata database resides. If none is provided, the Amazon Web Services account ID is used by default.</p>
            name: <p>The name of the database to update in the catalog. For Hive compatibility, this is folded to lowercase.</p>
            database_input: <p>A <code>DatabaseInput</code> object specifying the new definition of the metadata database in the catalog.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.update_database_request.UpdateDatabaseRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.update_database_response.UpdateDatabaseResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.update_database

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.update_database.async_update_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.update_database_request.UpdateDatabaseRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["name"] = name
        input_["database_input"] = database_input

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_data_quality_ruleset(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        description: Optional[
            "aws_sdk_glue.types.description_string.DescriptionString"
        ] = None,
        ruleset: Optional[
            "aws_sdk_glue.types.data_quality_ruleset_string.DataQualityRulesetString"
        ] = None,
    ) -> "aws_sdk_glue.types.update_data_quality_ruleset_response.UpdateDataQualityRulesetResponse":
        """<p>Updates the specified data quality ruleset.</p>

        Args:
            name: <p>The name of the data quality ruleset.</p>
            description: <p>A description of the ruleset.</p>
            ruleset: <p>A Data Quality Definition Language (DQDL) ruleset. For more information, see the Glue developer guide.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.update_data_quality_ruleset_request.UpdateDataQualityRulesetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.update_data_quality_ruleset_response.UpdateDataQualityRulesetResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.update_data_quality_ruleset

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.update_data_quality_ruleset.async_update_data_quality_ruleset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.update_data_quality_ruleset_request.UpdateDataQualityRulesetRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if ruleset is not None:
            input_["ruleset"] = ruleset

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_dev_endpoint(
        self,
        endpoint_name: "aws_sdk_glue.types.generic_string.GenericString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        public_key: Optional["aws_sdk_glue.types.generic_string.GenericString"] = None,
        add_public_keys: Optional[
            "aws_sdk_glue.types.public_keys_list.PublicKeysList"
        ] = None,
        delete_public_keys: Optional[
            "aws_sdk_glue.types.public_keys_list.PublicKeysList"
        ] = None,
        custom_libraries: Optional[
            "aws_sdk_glue.types.dev_endpoint_custom_libraries.DevEndpointCustomLibraries"
        ] = None,
        update_etl_libraries: Optional[
            "aws_sdk_glue.types.boolean_value.BooleanValue"
        ] = None,
        delete_arguments: Optional["aws_sdk_glue.types.string_list.StringList"] = None,
        add_arguments: Optional["aws_sdk_glue.types.map_value.MapValue"] = None,
    ) -> "aws_sdk_glue.types.update_dev_endpoint_response.UpdateDevEndpointResponse":
        r"""<p>Updates a specified development endpoint.</p>

        Args:
            endpoint_name: <p>The name of the <code>DevEndpoint</code> to be updated.</p>
            public_key: <p>The public key for the <code>DevEndpoint</code> to use.</p>
            add_public_keys: <p>The list of public keys for the <code>DevEndpoint</code> to use.</p>
            delete_public_keys: <p>The list of public keys to be deleted from the <code>DevEndpoint</code>.</p>
            custom_libraries: <p>Custom Python or Java libraries to be loaded in the <code>DevEndpoint</code>.</p>
            update_etl_libraries: <p> <code>True</code> if the list of custom libraries to be loaded in the development endpoint needs to be updated, or <code>False</code> if otherwise.</p>
            delete_arguments: <p>The list of argument keys to be deleted from the map of arguments used to configure the <code>DevEndpoint</code>.</p>
            add_arguments: <p>The map of arguments to add the map of arguments used to configure the <code>DevEndpoint</code>.</p> <p>Valid arguments are:</p> <ul> <li> <p> <code>\"--enable-glue-datacatalog\": \"\"</code> </p> </li> </ul> <p>You can specify a version of Python support for development endpoints by using the <code>Arguments</code> parameter in the <code>CreateDevEndpoint</code> or <code>UpdateDevEndpoint</code> APIs. If no arguments are provided, the version defaults to Python 2.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.update_dev_endpoint_request.UpdateDevEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.update_dev_endpoint_response.UpdateDevEndpointResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.update_dev_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.update_dev_endpoint.async_update_dev_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.update_dev_endpoint_request.UpdateDevEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["endpoint_name"] = endpoint_name
        if public_key is not None:
            input_["public_key"] = public_key
        if add_public_keys is not None:
            input_["add_public_keys"] = add_public_keys
        if delete_public_keys is not None:
            input_["delete_public_keys"] = delete_public_keys
        if custom_libraries is not None:
            input_["custom_libraries"] = custom_libraries
        if update_etl_libraries is not None:
            input_["update_etl_libraries"] = update_etl_libraries
        if delete_arguments is not None:
            input_["delete_arguments"] = delete_arguments
        if add_arguments is not None:
            input_["add_arguments"] = add_arguments

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_glue_identity_center_configuration(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        scopes: Optional[
            "aws_sdk_glue.types.identity_center_scopes_list.IdentityCenterScopesList"
        ] = None,
        user_background_sessions_enabled: Optional[
            "aws_sdk_glue.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "aws_sdk_glue.types.update_glue_identity_center_configuration_response.UpdateGlueIdentityCenterConfigurationResponse":
        """<p>Updates the existing Glue Identity Center configuration, allowing modification of scopes and permissions for the integration.</p>

        Args:
            scopes: <p>A list of Identity Center scopes that define the updated permissions and access levels for the Glue configuration.</p>
            user_background_sessions_enabled: <p>Specifies whether users can run background sessions when using Identity Center authentication with Glue services.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.update_glue_identity_center_configuration_request.UpdateGlueIdentityCenterConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.update_glue_identity_center_configuration_response.UpdateGlueIdentityCenterConfigurationResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.update_glue_identity_center_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.update_glue_identity_center_configuration.async_update_glue_identity_center_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.update_glue_identity_center_configuration_request.UpdateGlueIdentityCenterConfigurationRequest = {}  # type: ignore[typeddict-item]
        if scopes is not None:
            input_["scopes"] = scopes
        if user_background_sessions_enabled is not None:
            input_["user_background_sessions_enabled"] = (
                user_background_sessions_enabled
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_integration_resource_property(
        self,
        resource_arn: "aws_sdk_glue.types.string512.String512",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        source_processing_properties: Optional[
            "aws_sdk_glue.types.source_processing_properties.SourceProcessingProperties"
        ] = None,
        target_processing_properties: Optional[
            "aws_sdk_glue.types.target_processing_properties.TargetProcessingProperties"
        ] = None,
    ) -> "aws_sdk_glue.types.update_integration_resource_property_response.UpdateIntegrationResourcePropertyResponse":
        """<p>This API can be used for updating the <code>ResourceProperty</code> of the Glue connection (for the source) or Glue database ARN (for the target). These properties can include the role to access the connection or database. Since the same resource can be used across multiple integrations, updating resource properties will impact all the integrations using it.</p>

        Args:
            resource_arn: <p>The connection ARN of the source, or the database ARN of the target.</p>
            source_processing_properties: <p>The resource properties associated with the integration source.</p>
            target_processing_properties: <p>The resource properties associated with the integration target.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.update_integration_resource_property_request.UpdateIntegrationResourcePropertyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.update_integration_resource_property_response.UpdateIntegrationResourcePropertyResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.update_integration_resource_property

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.update_integration_resource_property.async_update_integration_resource_property(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.update_integration_resource_property_request.UpdateIntegrationResourcePropertyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        if source_processing_properties is not None:
            input_["source_processing_properties"] = source_processing_properties
        if target_processing_properties is not None:
            input_["target_processing_properties"] = target_processing_properties

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_integration_table_properties(
        self,
        resource_arn: "aws_sdk_glue.types.string512.String512",
        table_name: "aws_sdk_glue.types.string128.String128",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        source_table_config: Optional[
            "aws_sdk_glue.types.source_table_config.SourceTableConfig"
        ] = None,
        target_table_config: Optional[
            "aws_sdk_glue.types.target_table_config.TargetTableConfig"
        ] = None,
    ) -> "aws_sdk_glue.types.update_integration_table_properties_response.UpdateIntegrationTablePropertiesResponse":
        """<p>This API is used to provide optional override properties for the tables that need to be replicated. These properties can include properties for filtering and partitioning for the source and target tables. To set both source and target properties the same API need to be invoked with the Glue connection ARN as <code>ResourceArn</code> with <code>SourceTableConfig</code>, and the Glue database ARN as <code>ResourceArn</code> with <code>TargetTableConfig</code> respectively.</p> <p>The override will be reflected across all the integrations using same <code>ResourceArn</code> and source table.</p>

        Args:
            resource_arn: <p>The connection ARN of the source, or the database ARN of the target.</p>
            table_name: <p>The name of the table to be replicated.</p>
            source_table_config: <p>A structure for the source table configuration.</p>
            target_table_config: <p>A structure for the target table configuration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.update_integration_table_properties_request.UpdateIntegrationTablePropertiesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.update_integration_table_properties_response.UpdateIntegrationTablePropertiesResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.update_integration_table_properties

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.update_integration_table_properties.async_update_integration_table_properties(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.update_integration_table_properties_request.UpdateIntegrationTablePropertiesRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["table_name"] = table_name
        if source_table_config is not None:
            input_["source_table_config"] = source_table_config
        if target_table_config is not None:
            input_["target_table_config"] = target_table_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_job(
        self,
        job_name: "aws_sdk_glue.types.name_string.NameString",
        job_update: "aws_sdk_glue.types.job_update.JobUpdate",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.update_job_response.UpdateJobResponse":
        """<p>Updates an existing job definition. The previous job definition is completely overwritten by this information.</p>

        Args:
            job_name: <p>The name of the job definition to update.</p>
            job_update: <p>Specifies the values with which to update the job definition. Unspecified configuration is removed or reset to default values.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.update_job_request.UpdateJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.update_job_response.UpdateJobResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.update_job

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.update_job.async_update_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.update_job_request.UpdateJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_name"] = job_name
        input_["job_update"] = job_update

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_job_from_source_control(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        job_name: Optional["aws_sdk_glue.types.name_string.NameString"] = None,
        provider: Optional[
            "aws_sdk_glue.types.source_control_provider.SourceControlProvider"
        ] = None,
        repository_name: Optional["aws_sdk_glue.types.name_string.NameString"] = None,
        repository_owner: Optional["aws_sdk_glue.types.name_string.NameString"] = None,
        branch_name: Optional["aws_sdk_glue.types.name_string.NameString"] = None,
        folder: Optional["aws_sdk_glue.types.name_string.NameString"] = None,
        commit_id: Optional[
            "aws_sdk_glue.types.commit_id_string.CommitIdString"
        ] = None,
        auth_strategy: Optional[
            "aws_sdk_glue.types.source_control_auth_strategy.SourceControlAuthStrategy"
        ] = None,
        auth_token: Optional[
            "aws_sdk_glue.types.auth_token_string.AuthTokenString"
        ] = None,
    ) -> "aws_sdk_glue.types.update_job_from_source_control_response.UpdateJobFromSourceControlResponse":
        """<p>Synchronizes a job from the source control repository. This operation takes the job artifacts that are located in the remote repository and updates the Glue internal stores with these artifacts.</p> <p>This API supports optional parameters which take in the repository information.</p>

        Args:
            job_name: <p>The name of the Glue job to be synchronized to or from the remote repository.</p>
            provider: <p> The provider for the remote repository. Possible values: GITHUB, AWS_CODE_COMMIT, GITLAB, BITBUCKET. </p>
            repository_name: <p>The name of the remote repository that contains the job artifacts. For BitBucket providers, <code>RepositoryName</code> should include <code>WorkspaceName</code>. Use the format <code><WorkspaceName>/<RepositoryName></code>. </p>
            repository_owner: <p>The owner of the remote repository that contains the job artifacts.</p>
            branch_name: <p>An optional branch in the remote repository.</p>
            folder: <p>An optional folder in the remote repository.</p>
            commit_id: <p>A commit ID for a commit in the remote repository.</p>
            auth_strategy: <p>The type of authentication, which can be an authentication token stored in Amazon Web Services Secrets Manager, or a personal access token.</p>
            auth_token: <p>The value of the authorization token.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.update_job_from_source_control_request.UpdateJobFromSourceControlRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.update_job_from_source_control_response.UpdateJobFromSourceControlResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.update_job_from_source_control

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.update_job_from_source_control.async_update_job_from_source_control(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.update_job_from_source_control_request.UpdateJobFromSourceControlRequest = {}  # type: ignore[typeddict-item]
        if job_name is not None:
            input_["job_name"] = job_name
        if provider is not None:
            input_["provider"] = provider
        if repository_name is not None:
            input_["repository_name"] = repository_name
        if repository_owner is not None:
            input_["repository_owner"] = repository_owner
        if branch_name is not None:
            input_["branch_name"] = branch_name
        if folder is not None:
            input_["folder"] = folder
        if commit_id is not None:
            input_["commit_id"] = commit_id
        if auth_strategy is not None:
            input_["auth_strategy"] = auth_strategy
        if auth_token is not None:
            input_["auth_token"] = auth_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_ml_transform(
        self,
        transform_id: "aws_sdk_glue.types.hash_string.HashString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        name: Optional["aws_sdk_glue.types.name_string.NameString"] = None,
        description: Optional[
            "aws_sdk_glue.types.description_string.DescriptionString"
        ] = None,
        parameters: Optional[
            "aws_sdk_glue.types.transform_parameters.TransformParameters"
        ] = None,
        role: Optional["aws_sdk_glue.types.role_string.RoleString"] = None,
        glue_version: Optional[
            "aws_sdk_glue.types.glue_version_string.GlueVersionString"
        ] = None,
        max_capacity: Optional[
            "aws_sdk_glue.types.nullable_double.NullableDouble"
        ] = None,
        worker_type: Optional["aws_sdk_glue.types.worker_type.WorkerType"] = None,
        number_of_workers: Optional[
            "aws_sdk_glue.types.nullable_integer.NullableInteger"
        ] = None,
        timeout: Optional["aws_sdk_glue.types.timeout.Timeout"] = None,
        max_retries: Optional[
            "aws_sdk_glue.types.nullable_integer.NullableInteger"
        ] = None,
    ) -> "aws_sdk_glue.types.update_ml_transform_response.UpdateMLTransformResponse":
        r"""<p>Updates an existing machine learning transform. Call this operation to tune the algorithm parameters to achieve better results.</p> <p>After calling this operation, you can call the <code>StartMLEvaluationTaskRun</code> operation to assess how well your new parameters achieved your goals (such as improving the quality of your machine learning transform, or making it more cost-effective).</p>

        Args:
            transform_id: <p>A unique identifier that was generated when the transform was created.</p>
            name: <p>The unique name that you gave the transform when you created it.</p>
            description: <p>A description of the transform. The default is an empty string.</p>
            parameters: <p>The configuration parameters that are specific to the transform type (algorithm) used. Conditionally dependent on the transform type.</p>
            role: <p>The name or Amazon Resource Name (ARN) of the IAM role with the required permissions.</p>
            glue_version: <p>This value determines which version of Glue this machine learning transform is compatible with. Glue 1.0 is recommended for most customers. If the value is not set, the Glue compatibility defaults to Glue 0.9. For more information, see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/release-notes.html#release-notes-versions\">Glue Versions</a> in the developer guide.</p>
            max_capacity: <p>The number of Glue data processing units (DPUs) that are allocated to task runs for this transform. You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the <a href=\"https://aws.amazon.com/glue/pricing/\">Glue pricing page</a>. </p> <p>When the <code>WorkerType</code> field is set to a value other than <code>Standard</code>, the <code>MaxCapacity</code> field is set automatically and becomes read-only.</p>
            worker_type: <p>The type of predefined worker that is allocated when this task runs. Accepts a value of Standard, G.1X, or G.2X.</p> <ul> <li> <p>For the <code>Standard</code> worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.</p> </li> <li> <p>For the <code>G.1X</code> worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk, and 1 executor per worker.</p> </li> <li> <p>For the <code>G.2X</code> worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB disk, and 1 executor per worker.</p> </li> </ul>
            number_of_workers: <p>The number of workers of a defined <code>workerType</code> that are allocated when this task runs.</p>
            timeout: <p>The timeout for a task run for this transform in minutes. This is the maximum time that a task run for this transform can consume resources before it is terminated and enters <code>TIMEOUT</code> status. The default is 2,880 minutes (48 hours).</p>
            max_retries: <p>The maximum number of times to retry a task for this transform after a task run fails.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.update_ml_transform_request.UpdateMLTransformRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.update_ml_transform_response.UpdateMLTransformResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.update_ml_transform

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.update_ml_transform.async_update_ml_transform(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.update_ml_transform_request.UpdateMLTransformRequest = {}  # type: ignore[typeddict-item]
        input_["transform_id"] = transform_id
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if parameters is not None:
            input_["parameters"] = parameters
        if role is not None:
            input_["role"] = role
        if glue_version is not None:
            input_["glue_version"] = glue_version
        if max_capacity is not None:
            input_["max_capacity"] = max_capacity
        if worker_type is not None:
            input_["worker_type"] = worker_type
        if number_of_workers is not None:
            input_["number_of_workers"] = number_of_workers
        if timeout is not None:
            input_["timeout"] = timeout
        if max_retries is not None:
            input_["max_retries"] = max_retries

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_partition(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        partition_value_list: "aws_sdk_glue.types.bounded_partition_value_list.BoundedPartitionValueList",
        partition_input: "aws_sdk_glue.types.partition_input.PartitionInput",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.update_partition_response.UpdatePartitionResponse":
        """<p>Updates a partition.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog where the partition to be updated resides. If none is provided, the Amazon Web Services account ID is used by default.</p>
            database_name: <p>The name of the catalog database in which the table in question resides.</p>
            table_name: <p>The name of the table in which the partition to be updated is located.</p>
            partition_value_list: <p>List of partition key values that define the partition to update.</p>
            partition_input: <p>The new partition object to update the partition to.</p> <p>The <code>Values</code> property can't be changed. If you want to change the partition key values for a partition, delete and recreate the partition.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.update_partition_request.UpdatePartitionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.update_partition_response.UpdatePartitionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.update_partition

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.update_partition.async_update_partition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.update_partition_request.UpdatePartitionRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        input_["partition_value_list"] = partition_value_list
        input_["partition_input"] = partition_input

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_registry(
        self,
        registry_id: "aws_sdk_glue.types.registry_id.RegistryId",
        description: "aws_sdk_glue.types.description_string.DescriptionString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.update_registry_response.UpdateRegistryResponse":
        """<p>Updates an existing registry which is used to hold a collection of schemas. The updated properties relate to the registry, and do not modify any of the schemas within the registry. </p>

        Args:
            registry_id: <p>This is a wrapper structure that may contain the registry name and Amazon Resource Name (ARN).</p>
            description: <p>A description of the registry. If description is not provided, this field will not be updated.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.update_registry_input.UpdateRegistryInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.update_registry_response.UpdateRegistryResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.update_registry

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.update_registry.async_update_registry(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.update_registry_input.UpdateRegistryInput = {}  # type: ignore[typeddict-item]
        input_["registry_id"] = registry_id
        input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_schema(
        self,
        schema_id: "aws_sdk_glue.types.schema_id.SchemaId",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        schema_version_number: Optional[
            "aws_sdk_glue.types.schema_version_number.SchemaVersionNumber"
        ] = None,
        compatibility: Optional[
            "aws_sdk_glue.types.compatibility.Compatibility"
        ] = None,
        description: Optional[
            "aws_sdk_glue.types.description_string.DescriptionString"
        ] = None,
    ) -> "aws_sdk_glue.types.update_schema_response.UpdateSchemaResponse":
        """<p>Updates the description, compatibility setting, or version checkpoint for a schema set.</p> <p>For updating the compatibility setting, the call will not validate compatibility for the entire set of schema versions with the new compatibility setting. If the value for <code>Compatibility</code> is provided, the <code>VersionNumber</code> (a checkpoint) is also required. The API will validate the checkpoint version number for consistency.</p> <p>If the value for the <code>VersionNumber</code> (checkpoint) is provided, <code>Compatibility</code> is optional and this can be used to set/reset a checkpoint for the schema.</p> <p>This update will happen only if the schema is in the AVAILABLE state.</p>

        Args:
            schema_id: <p>This is a wrapper structure to contain schema identity fields. The structure contains:</p> <ul> <li> <p>SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. One of <code>SchemaArn</code> or <code>SchemaName</code> has to be provided.</p> </li> <li> <p>SchemaId$SchemaName: The name of the schema. One of <code>SchemaArn</code> or <code>SchemaName</code> has to be provided.</p> </li> </ul>
            schema_version_number: <p>Version number required for check pointing. One of <code>VersionNumber</code> or <code>Compatibility</code> has to be provided.</p>
            compatibility: <p>The new compatibility setting for the schema.</p>
            description: <p>The new description for the schema.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.update_schema_input.UpdateSchemaInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.update_schema_response.UpdateSchemaResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.update_schema

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.update_schema.async_update_schema(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.update_schema_input.UpdateSchemaInput = {}  # type: ignore[typeddict-item]
        input_["schema_id"] = schema_id
        if schema_version_number is not None:
            input_["schema_version_number"] = schema_version_number
        if compatibility is not None:
            input_["compatibility"] = compatibility
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_source_control_from_job(
        self,
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        job_name: Optional["aws_sdk_glue.types.name_string.NameString"] = None,
        provider: Optional[
            "aws_sdk_glue.types.source_control_provider.SourceControlProvider"
        ] = None,
        repository_name: Optional["aws_sdk_glue.types.name_string.NameString"] = None,
        repository_owner: Optional["aws_sdk_glue.types.name_string.NameString"] = None,
        branch_name: Optional["aws_sdk_glue.types.name_string.NameString"] = None,
        folder: Optional["aws_sdk_glue.types.name_string.NameString"] = None,
        commit_id: Optional[
            "aws_sdk_glue.types.commit_id_string.CommitIdString"
        ] = None,
        auth_strategy: Optional[
            "aws_sdk_glue.types.source_control_auth_strategy.SourceControlAuthStrategy"
        ] = None,
        auth_token: Optional[
            "aws_sdk_glue.types.auth_token_string.AuthTokenString"
        ] = None,
    ) -> "aws_sdk_glue.types.update_source_control_from_job_response.UpdateSourceControlFromJobResponse":
        """<p>Synchronizes a job to the source control repository. This operation takes the job artifacts from the Glue internal stores and makes a commit to the remote repository that is configured on the job.</p> <p>This API supports optional parameters which take in the repository information.</p>

        Args:
            job_name: <p>The name of the Glue job to be synchronized to or from the remote repository.</p>
            provider: <p> The provider for the remote repository. Possible values: GITHUB, AWS_CODE_COMMIT, GITLAB, BITBUCKET. </p>
            repository_name: <p>The name of the remote repository that contains the job artifacts. For BitBucket providers, <code>RepositoryName</code> should include <code>WorkspaceName</code>. Use the format <code><WorkspaceName>/<RepositoryName></code>. </p>
            repository_owner: <p>The owner of the remote repository that contains the job artifacts.</p>
            branch_name: <p>An optional branch in the remote repository.</p>
            folder: <p>An optional folder in the remote repository.</p>
            commit_id: <p>A commit ID for a commit in the remote repository.</p>
            auth_strategy: <p>The type of authentication, which can be an authentication token stored in Amazon Web Services Secrets Manager, or a personal access token.</p>
            auth_token: <p>The value of the authorization token.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.update_source_control_from_job_request.UpdateSourceControlFromJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.update_source_control_from_job_response.UpdateSourceControlFromJobResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.update_source_control_from_job

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.update_source_control_from_job.async_update_source_control_from_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.update_source_control_from_job_request.UpdateSourceControlFromJobRequest = {}  # type: ignore[typeddict-item]
        if job_name is not None:
            input_["job_name"] = job_name
        if provider is not None:
            input_["provider"] = provider
        if repository_name is not None:
            input_["repository_name"] = repository_name
        if repository_owner is not None:
            input_["repository_owner"] = repository_owner
        if branch_name is not None:
            input_["branch_name"] = branch_name
        if folder is not None:
            input_["folder"] = folder
        if commit_id is not None:
            input_["commit_id"] = commit_id
        if auth_strategy is not None:
            input_["auth_strategy"] = auth_strategy
        if auth_token is not None:
            input_["auth_token"] = auth_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_table(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
        name: Optional["aws_sdk_glue.types.name_string.NameString"] = None,
        table_input: Optional["aws_sdk_glue.types.table_input.TableInput"] = None,
        skip_archive: Optional[
            "aws_sdk_glue.types.boolean_nullable.BooleanNullable"
        ] = None,
        transaction_id: Optional[
            "aws_sdk_glue.types.transaction_id_string.TransactionIdString"
        ] = None,
        version_id: Optional["aws_sdk_glue.types.version_string.VersionString"] = None,
        view_update_action: Optional[
            "aws_sdk_glue.types.view_update_action.ViewUpdateAction"
        ] = None,
        force: Optional["aws_sdk_glue.types.boolean.Boolean"] = None,
        update_open_table_format_input: Optional[
            "aws_sdk_glue.types.update_open_table_format_input.UpdateOpenTableFormatInput"
        ] = None,
    ) -> "aws_sdk_glue.types.update_table_response.UpdateTableResponse":
        """<p>Updates a metadata table in the Data Catalog.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog where the table resides. If none is provided, the Amazon Web Services account ID is used by default.</p>
            database_name: <p>The name of the catalog database in which the table resides. For Hive compatibility, this name is entirely lowercase.</p>
            name: <p>The unique identifier for the table within the specified database that will be created in the Glue Data Catalog.</p>
            table_input: <p>An updated <code>TableInput</code> object to define the metadata table in the catalog.</p>
            skip_archive: <p>By default, <code>UpdateTable</code> always creates an archived version of the table before updating it. However, if <code>skipArchive</code> is set to true, <code>UpdateTable</code> does not create the archived version.</p>
            transaction_id: <p>The transaction ID at which to update the table contents. </p>
            version_id: <p>The version ID at which to update the table contents. </p>
            view_update_action: <p>The operation to be performed when updating the view.</p>
            force: <p>A flag that can be set to true to ignore matching storage descriptor and subobject matching requirements.</p>
            update_open_table_format_input: <p>Input parameters for updating open table format tables in GlueData Catalog, serving as a wrapper for format-specific update operations such as Apache Iceberg.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.update_table_request.UpdateTableRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.update_table_response.UpdateTableResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.update_table

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.update_table.async_update_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.update_table_request.UpdateTableRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        if name is not None:
            input_["name"] = name
        if table_input is not None:
            input_["table_input"] = table_input
        if skip_archive is not None:
            input_["skip_archive"] = skip_archive
        if transaction_id is not None:
            input_["transaction_id"] = transaction_id
        if version_id is not None:
            input_["version_id"] = version_id
        if view_update_action is not None:
            input_["view_update_action"] = view_update_action
        if force is not None:
            input_["force"] = force
        if update_open_table_format_input is not None:
            input_["update_open_table_format_input"] = update_open_table_format_input

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_table_optimizer(
        self,
        catalog_id: "aws_sdk_glue.types.catalog_id_string.CatalogIdString",
        database_name: "aws_sdk_glue.types.name_string.NameString",
        table_name: "aws_sdk_glue.types.name_string.NameString",
        type: "aws_sdk_glue.types.table_optimizer_type.TableOptimizerType",
        table_optimizer_configuration: "aws_sdk_glue.types.table_optimizer_configuration.TableOptimizerConfiguration",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.update_table_optimizer_response.UpdateTableOptimizerResponse":
        """<p>Updates the configuration for an existing table optimizer.</p>

        Args:
            catalog_id: <p>The Catalog ID of the table.</p>
            database_name: <p>The name of the database in the catalog in which the table resides.</p>
            table_name: <p>The name of the table.</p>
            type: <p>The type of table optimizer.</p>
            table_optimizer_configuration: <p>A <code>TableOptimizerConfiguration</code> object representing the configuration of a table optimizer.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.update_table_optimizer_request.UpdateTableOptimizerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.update_table_optimizer_response.UpdateTableOptimizerResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.update_table_optimizer

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.update_table_optimizer.async_update_table_optimizer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.update_table_optimizer_request.UpdateTableOptimizerRequest = {}  # type: ignore[typeddict-item]
        input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["table_name"] = table_name
        input_["type"] = type
        input_["table_optimizer_configuration"] = table_optimizer_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_trigger(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        trigger_update: "aws_sdk_glue.types.trigger_update.TriggerUpdate",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
    ) -> "aws_sdk_glue.types.update_trigger_response.UpdateTriggerResponse":
        """<p>Updates a trigger definition.</p> <p>Job arguments may be logged. Do not pass plaintext secrets as arguments. Retrieve secrets from a Glue Connection, Amazon Web Services Secrets Manager or other secret management mechanism if you intend to keep them within the Job.</p>

        Args:
            name: <p>The name of the trigger to update.</p>
            trigger_update: <p>The new values with which to update the trigger.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.update_trigger_request.UpdateTriggerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.update_trigger_response.UpdateTriggerResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.update_trigger

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.update_trigger.async_update_trigger(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.update_trigger_request.UpdateTriggerRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["trigger_update"] = trigger_update

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_usage_profile(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        configuration: "aws_sdk_glue.types.profile_configuration.ProfileConfiguration",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        description: Optional[
            "aws_sdk_glue.types.description_string.DescriptionString"
        ] = None,
    ) -> "aws_sdk_glue.types.update_usage_profile_response.UpdateUsageProfileResponse":
        """<p>Update an Glue usage profile.</p>

        Args:
            name: <p>The name of the usage profile.</p>
            description: <p>A description of the usage profile.</p>
            configuration: <p>A <code>ProfileConfiguration</code> object specifying the job and session values for the profile.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.update_usage_profile_request.UpdateUsageProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.update_usage_profile_response.UpdateUsageProfileResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.update_usage_profile

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.update_usage_profile.async_update_usage_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.update_usage_profile_request.UpdateUsageProfileRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["configuration"] = configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_user_defined_function(
        self,
        database_name: "aws_sdk_glue.types.name_string.NameString",
        function_name: "aws_sdk_glue.types.name_string.NameString",
        function_input: "aws_sdk_glue.types.user_defined_function_input.UserDefinedFunctionInput",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        catalog_id: Optional[
            "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "aws_sdk_glue.types.update_user_defined_function_response.UpdateUserDefinedFunctionResponse":
        """<p>Updates an existing function definition in the Data Catalog.</p>

        Args:
            catalog_id: <p>The ID of the Data Catalog where the function to be updated is located. If none is provided, the Amazon Web Services account ID is used by default.</p>
            database_name: <p>The name of the catalog database where the function to be updated is located.</p>
            function_name: <p>The name of the function.</p>
            function_input: <p>A <code>FunctionInput</code> object that redefines the function in the Data Catalog.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.update_user_defined_function_request.UpdateUserDefinedFunctionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.update_user_defined_function_response.UpdateUserDefinedFunctionResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.update_user_defined_function

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.update_user_defined_function.async_update_user_defined_function(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.update_user_defined_function_request.UpdateUserDefinedFunctionRequest = {}  # type: ignore[typeddict-item]
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        input_["database_name"] = database_name
        input_["function_name"] = function_name
        input_["function_input"] = function_input

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_workflow(
        self,
        name: "aws_sdk_glue.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncGlueClientConfig] = None,
        description: Optional[
            "aws_sdk_glue.types.workflow_description_string.WorkflowDescriptionString"
        ] = None,
        default_run_properties: Optional[
            "aws_sdk_glue.types.workflow_run_properties.WorkflowRunProperties"
        ] = None,
        max_concurrent_runs: Optional[
            "aws_sdk_glue.types.nullable_integer.NullableInteger"
        ] = None,
    ) -> "aws_sdk_glue.types.update_workflow_response.UpdateWorkflowResponse":
        """<p>Updates an existing workflow.</p>

        Args:
            name: <p>Name of the workflow to be updated.</p>
            description: <p>The description of the workflow.</p>
            default_run_properties: <p>A collection of properties to be used as part of each execution of the workflow.</p> <p>Run properties may be logged. Do not pass plaintext secrets as properties. Retrieve secrets from a Glue Connection, Amazon Web Services Secrets Manager or other secret management mechanism if you intend to use them within the workflow run.</p>
            max_concurrent_runs: <p>You can use this parameter to prevent unwanted multiple updates to data, to control costs, or in some cases, to prevent exceeding the maximum number of concurrent runs of any of the component jobs. If you leave this parameter blank, there is no limit to the number of concurrent workflow runs.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_glue.types.update_workflow_request.UpdateWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_glue.types.update_workflow_response.UpdateWorkflowResponse"
        ]:
            import aws_sdk_glue._operations.aws_glue.update_workflow

            (
                output,
                http_response,
            ) = await aws_sdk_glue._operations.aws_glue.update_workflow.async_update_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_glue.types.update_workflow_request.UpdateWorkflowRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if default_run_properties is not None:
            input_["default_run_properties"] = default_run_properties
        if max_concurrent_runs is not None:
            input_["max_concurrent_runs"] = max_concurrent_runs

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
