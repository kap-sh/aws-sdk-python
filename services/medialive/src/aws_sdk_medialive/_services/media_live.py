"""Generated from Smithy shape ``com.amazonaws.medialive#MediaLive``."""

import warnings
from collections.abc import Generator, Iterator
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import aws_sdk_medialive._auth._signers
import aws_sdk_medialive._auth._sigv4
from aws_sdk_medialive._auth._identity import Credentials
from aws_sdk_medialive._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_medialive._auth._zapros_handler import AuthMiddleware
from aws_sdk_medialive._pagination import resolve_path as _resolve_path
from aws_sdk_medialive._services._aws_config import aws_config
from aws_sdk_medialive._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__boolean
    import aws_sdk_medialive.types.__double
    import aws_sdk_medialive.types.__integer_min1
    import aws_sdk_medialive.types.__integer_min10_max86400
    import aws_sdk_medialive.types.__list_of__string
    import aws_sdk_medialive.types.__list_of__string_pattern_s
    import aws_sdk_medialive.types.__list_of_channel_pipeline_id_to_restart
    import aws_sdk_medialive.types.__list_of_event_bridge_rule_template_target
    import aws_sdk_medialive.types.__list_of_input_attachment
    import aws_sdk_medialive.types.__list_of_input_destination_request
    import aws_sdk_medialive.types.__list_of_input_device_request
    import aws_sdk_medialive.types.__list_of_input_device_settings
    import aws_sdk_medialive.types.__list_of_input_source_request
    import aws_sdk_medialive.types.__list_of_input_whitelist_rule_cidr
    import aws_sdk_medialive.types.__list_of_ip_pool_create_request
    import aws_sdk_medialive.types.__list_of_ip_pool_update_request
    import aws_sdk_medialive.types.__list_of_media_connect_flow_request
    import aws_sdk_medialive.types.__list_of_node_interface_mapping
    import aws_sdk_medialive.types.__list_of_node_interface_mapping_create_request
    import aws_sdk_medialive.types.__list_of_output_destination
    import aws_sdk_medialive.types.__list_of_route_create_request
    import aws_sdk_medialive.types.__list_of_route_update_request
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.__string_max64
    import aws_sdk_medialive.types.__string_min0_max1024
    import aws_sdk_medialive.types.__string_min1_max255_pattern_s
    import aws_sdk_medialive.types.__string_min1_max256_pattern_s
    import aws_sdk_medialive.types.__string_min1_max2048
    import aws_sdk_medialive.types.__string_pattern_s
    import aws_sdk_medialive.types.accept_header
    import aws_sdk_medialive.types.accept_input_device_transfer_request
    import aws_sdk_medialive.types.accept_input_device_transfer_response
    import aws_sdk_medialive.types.account_configuration
    import aws_sdk_medialive.types.anywhere_settings
    import aws_sdk_medialive.types.batch_delete_request
    import aws_sdk_medialive.types.batch_delete_response
    import aws_sdk_medialive.types.batch_schedule_action_create_request
    import aws_sdk_medialive.types.batch_schedule_action_delete_request
    import aws_sdk_medialive.types.batch_start_request
    import aws_sdk_medialive.types.batch_start_response
    import aws_sdk_medialive.types.batch_stop_request
    import aws_sdk_medialive.types.batch_stop_response
    import aws_sdk_medialive.types.batch_update_schedule_request
    import aws_sdk_medialive.types.batch_update_schedule_response
    import aws_sdk_medialive.types.cancel_input_device_transfer_request
    import aws_sdk_medialive.types.cancel_input_device_transfer_response
    import aws_sdk_medialive.types.cdi_input_specification
    import aws_sdk_medialive.types.channel_alert
    import aws_sdk_medialive.types.channel_class
    import aws_sdk_medialive.types.channel_engine_version_request
    import aws_sdk_medialive.types.channel_summary
    import aws_sdk_medialive.types.claim_device_request
    import aws_sdk_medialive.types.claim_device_response
    import aws_sdk_medialive.types.cloud_watch_alarm_template_comparison_operator
    import aws_sdk_medialive.types.cloud_watch_alarm_template_group_summary
    import aws_sdk_medialive.types.cloud_watch_alarm_template_statistic
    import aws_sdk_medialive.types.cloud_watch_alarm_template_summary
    import aws_sdk_medialive.types.cloud_watch_alarm_template_target_resource_type
    import aws_sdk_medialive.types.cloud_watch_alarm_template_treat_missing_data
    import aws_sdk_medialive.types.cluster_alert
    import aws_sdk_medialive.types.cluster_network_settings_create_request
    import aws_sdk_medialive.types.cluster_network_settings_update_request
    import aws_sdk_medialive.types.cluster_type
    import aws_sdk_medialive.types.create_channel_placement_group_request
    import aws_sdk_medialive.types.create_channel_placement_group_response
    import aws_sdk_medialive.types.create_channel_request
    import aws_sdk_medialive.types.create_channel_response
    import aws_sdk_medialive.types.create_cloud_watch_alarm_template_group_request
    import aws_sdk_medialive.types.create_cloud_watch_alarm_template_group_response
    import aws_sdk_medialive.types.create_cloud_watch_alarm_template_request
    import aws_sdk_medialive.types.create_cloud_watch_alarm_template_response
    import aws_sdk_medialive.types.create_cluster_request
    import aws_sdk_medialive.types.create_cluster_response
    import aws_sdk_medialive.types.create_event_bridge_rule_template_group_request
    import aws_sdk_medialive.types.create_event_bridge_rule_template_group_response
    import aws_sdk_medialive.types.create_event_bridge_rule_template_request
    import aws_sdk_medialive.types.create_event_bridge_rule_template_response
    import aws_sdk_medialive.types.create_input_request
    import aws_sdk_medialive.types.create_input_response
    import aws_sdk_medialive.types.create_input_security_group_request
    import aws_sdk_medialive.types.create_input_security_group_response
    import aws_sdk_medialive.types.create_multiplex_program_request
    import aws_sdk_medialive.types.create_multiplex_program_response
    import aws_sdk_medialive.types.create_multiplex_request
    import aws_sdk_medialive.types.create_multiplex_response
    import aws_sdk_medialive.types.create_network_request
    import aws_sdk_medialive.types.create_network_response
    import aws_sdk_medialive.types.create_node_registration_script_request
    import aws_sdk_medialive.types.create_node_registration_script_response
    import aws_sdk_medialive.types.create_node_request
    import aws_sdk_medialive.types.create_node_response
    import aws_sdk_medialive.types.create_partner_input_request
    import aws_sdk_medialive.types.create_partner_input_response
    import aws_sdk_medialive.types.create_sdi_source_request
    import aws_sdk_medialive.types.create_sdi_source_response
    import aws_sdk_medialive.types.create_signal_map_request
    import aws_sdk_medialive.types.create_signal_map_response
    import aws_sdk_medialive.types.create_tags_request
    import aws_sdk_medialive.types.delete_channel_placement_group_request
    import aws_sdk_medialive.types.delete_channel_placement_group_response
    import aws_sdk_medialive.types.delete_channel_request
    import aws_sdk_medialive.types.delete_channel_response
    import aws_sdk_medialive.types.delete_cloud_watch_alarm_template_group_request
    import aws_sdk_medialive.types.delete_cloud_watch_alarm_template_request
    import aws_sdk_medialive.types.delete_cluster_request
    import aws_sdk_medialive.types.delete_cluster_response
    import aws_sdk_medialive.types.delete_event_bridge_rule_template_group_request
    import aws_sdk_medialive.types.delete_event_bridge_rule_template_request
    import aws_sdk_medialive.types.delete_input_request
    import aws_sdk_medialive.types.delete_input_response
    import aws_sdk_medialive.types.delete_input_security_group_request
    import aws_sdk_medialive.types.delete_input_security_group_response
    import aws_sdk_medialive.types.delete_multiplex_program_request
    import aws_sdk_medialive.types.delete_multiplex_program_response
    import aws_sdk_medialive.types.delete_multiplex_request
    import aws_sdk_medialive.types.delete_multiplex_response
    import aws_sdk_medialive.types.delete_network_request
    import aws_sdk_medialive.types.delete_network_response
    import aws_sdk_medialive.types.delete_node_request
    import aws_sdk_medialive.types.delete_node_response
    import aws_sdk_medialive.types.delete_reservation_request
    import aws_sdk_medialive.types.delete_reservation_response
    import aws_sdk_medialive.types.delete_schedule_request
    import aws_sdk_medialive.types.delete_schedule_response
    import aws_sdk_medialive.types.delete_sdi_source_request
    import aws_sdk_medialive.types.delete_sdi_source_response
    import aws_sdk_medialive.types.delete_signal_map_request
    import aws_sdk_medialive.types.delete_tags_request
    import aws_sdk_medialive.types.describe_account_configuration_request
    import aws_sdk_medialive.types.describe_account_configuration_response
    import aws_sdk_medialive.types.describe_channel_placement_group_request
    import aws_sdk_medialive.types.describe_channel_placement_group_response
    import aws_sdk_medialive.types.describe_channel_placement_group_summary
    import aws_sdk_medialive.types.describe_channel_request
    import aws_sdk_medialive.types.describe_channel_response
    import aws_sdk_medialive.types.describe_cluster_request
    import aws_sdk_medialive.types.describe_cluster_response
    import aws_sdk_medialive.types.describe_cluster_summary
    import aws_sdk_medialive.types.describe_input_device_request
    import aws_sdk_medialive.types.describe_input_device_response
    import aws_sdk_medialive.types.describe_input_device_thumbnail_request
    import aws_sdk_medialive.types.describe_input_device_thumbnail_response
    import aws_sdk_medialive.types.describe_input_request
    import aws_sdk_medialive.types.describe_input_response
    import aws_sdk_medialive.types.describe_input_security_group_request
    import aws_sdk_medialive.types.describe_input_security_group_response
    import aws_sdk_medialive.types.describe_multiplex_program_request
    import aws_sdk_medialive.types.describe_multiplex_program_response
    import aws_sdk_medialive.types.describe_multiplex_request
    import aws_sdk_medialive.types.describe_multiplex_response
    import aws_sdk_medialive.types.describe_network_request
    import aws_sdk_medialive.types.describe_network_response
    import aws_sdk_medialive.types.describe_network_summary
    import aws_sdk_medialive.types.describe_node_request
    import aws_sdk_medialive.types.describe_node_response
    import aws_sdk_medialive.types.describe_node_summary
    import aws_sdk_medialive.types.describe_offering_request
    import aws_sdk_medialive.types.describe_offering_response
    import aws_sdk_medialive.types.describe_reservation_request
    import aws_sdk_medialive.types.describe_reservation_response
    import aws_sdk_medialive.types.describe_schedule_request
    import aws_sdk_medialive.types.describe_schedule_response
    import aws_sdk_medialive.types.describe_sdi_source_request
    import aws_sdk_medialive.types.describe_sdi_source_response
    import aws_sdk_medialive.types.describe_thumbnails_request
    import aws_sdk_medialive.types.describe_thumbnails_response
    import aws_sdk_medialive.types.encoder_settings
    import aws_sdk_medialive.types.event_bridge_rule_template_event_type
    import aws_sdk_medialive.types.event_bridge_rule_template_group_summary
    import aws_sdk_medialive.types.event_bridge_rule_template_summary
    import aws_sdk_medialive.types.get_cloud_watch_alarm_template_group_request
    import aws_sdk_medialive.types.get_cloud_watch_alarm_template_group_response
    import aws_sdk_medialive.types.get_cloud_watch_alarm_template_request
    import aws_sdk_medialive.types.get_cloud_watch_alarm_template_response
    import aws_sdk_medialive.types.get_event_bridge_rule_template_group_request
    import aws_sdk_medialive.types.get_event_bridge_rule_template_group_response
    import aws_sdk_medialive.types.get_event_bridge_rule_template_request
    import aws_sdk_medialive.types.get_event_bridge_rule_template_response
    import aws_sdk_medialive.types.get_signal_map_request
    import aws_sdk_medialive.types.get_signal_map_response
    import aws_sdk_medialive.types.inference_settings
    import aws_sdk_medialive.types.input
    import aws_sdk_medialive.types.input_device_configurable_settings
    import aws_sdk_medialive.types.input_device_summary
    import aws_sdk_medialive.types.input_network_location
    import aws_sdk_medialive.types.input_sdi_sources
    import aws_sdk_medialive.types.input_security_group
    import aws_sdk_medialive.types.input_specification
    import aws_sdk_medialive.types.input_type
    import aws_sdk_medialive.types.input_vpc_request
    import aws_sdk_medialive.types.linked_channel_settings
    import aws_sdk_medialive.types.list_alerts_request
    import aws_sdk_medialive.types.list_alerts_response
    import aws_sdk_medialive.types.list_channel_placement_groups_request
    import aws_sdk_medialive.types.list_channel_placement_groups_response
    import aws_sdk_medialive.types.list_channels_request
    import aws_sdk_medialive.types.list_channels_response
    import aws_sdk_medialive.types.list_cloud_watch_alarm_template_groups_request
    import aws_sdk_medialive.types.list_cloud_watch_alarm_template_groups_response
    import aws_sdk_medialive.types.list_cloud_watch_alarm_templates_request
    import aws_sdk_medialive.types.list_cloud_watch_alarm_templates_response
    import aws_sdk_medialive.types.list_cluster_alerts_request
    import aws_sdk_medialive.types.list_cluster_alerts_response
    import aws_sdk_medialive.types.list_clusters_request
    import aws_sdk_medialive.types.list_clusters_response
    import aws_sdk_medialive.types.list_event_bridge_rule_template_groups_request
    import aws_sdk_medialive.types.list_event_bridge_rule_template_groups_response
    import aws_sdk_medialive.types.list_event_bridge_rule_templates_request
    import aws_sdk_medialive.types.list_event_bridge_rule_templates_response
    import aws_sdk_medialive.types.list_input_device_transfers_request
    import aws_sdk_medialive.types.list_input_device_transfers_response
    import aws_sdk_medialive.types.list_input_devices_request
    import aws_sdk_medialive.types.list_input_devices_response
    import aws_sdk_medialive.types.list_input_security_groups_request
    import aws_sdk_medialive.types.list_input_security_groups_response
    import aws_sdk_medialive.types.list_inputs_request
    import aws_sdk_medialive.types.list_inputs_response
    import aws_sdk_medialive.types.list_multiplex_alerts_request
    import aws_sdk_medialive.types.list_multiplex_alerts_response
    import aws_sdk_medialive.types.list_multiplex_programs_request
    import aws_sdk_medialive.types.list_multiplex_programs_response
    import aws_sdk_medialive.types.list_multiplexes_request
    import aws_sdk_medialive.types.list_multiplexes_response
    import aws_sdk_medialive.types.list_networks_request
    import aws_sdk_medialive.types.list_networks_response
    import aws_sdk_medialive.types.list_nodes_request
    import aws_sdk_medialive.types.list_nodes_response
    import aws_sdk_medialive.types.list_offerings_request
    import aws_sdk_medialive.types.list_offerings_response
    import aws_sdk_medialive.types.list_reservations_request
    import aws_sdk_medialive.types.list_reservations_response
    import aws_sdk_medialive.types.list_sdi_sources_request
    import aws_sdk_medialive.types.list_sdi_sources_response
    import aws_sdk_medialive.types.list_signal_maps_request
    import aws_sdk_medialive.types.list_signal_maps_response
    import aws_sdk_medialive.types.list_tags_for_resource_request
    import aws_sdk_medialive.types.list_tags_for_resource_response
    import aws_sdk_medialive.types.list_versions_request
    import aws_sdk_medialive.types.list_versions_response
    import aws_sdk_medialive.types.log_level
    import aws_sdk_medialive.types.maintenance_create_settings
    import aws_sdk_medialive.types.maintenance_update_settings
    import aws_sdk_medialive.types.max_results
    import aws_sdk_medialive.types.multicast_settings_create_request
    import aws_sdk_medialive.types.multicast_settings_update_request
    import aws_sdk_medialive.types.multiplex_alert
    import aws_sdk_medialive.types.multiplex_packet_identifiers_mapping
    import aws_sdk_medialive.types.multiplex_program_settings
    import aws_sdk_medialive.types.multiplex_program_summary
    import aws_sdk_medialive.types.multiplex_settings
    import aws_sdk_medialive.types.multiplex_summary
    import aws_sdk_medialive.types.node_role
    import aws_sdk_medialive.types.offering
    import aws_sdk_medialive.types.purchase_offering_request
    import aws_sdk_medialive.types.purchase_offering_response
    import aws_sdk_medialive.types.reboot_input_device_force
    import aws_sdk_medialive.types.reboot_input_device_request
    import aws_sdk_medialive.types.reboot_input_device_response
    import aws_sdk_medialive.types.reject_input_device_transfer_request
    import aws_sdk_medialive.types.reject_input_device_transfer_response
    import aws_sdk_medialive.types.renewal_settings
    import aws_sdk_medialive.types.reservation
    import aws_sdk_medialive.types.restart_channel_pipelines_request
    import aws_sdk_medialive.types.restart_channel_pipelines_response
    import aws_sdk_medialive.types.router_settings
    import aws_sdk_medialive.types.schedule_action
    import aws_sdk_medialive.types.sdi_source_mappings_update_request
    import aws_sdk_medialive.types.sdi_source_mode
    import aws_sdk_medialive.types.sdi_source_summary
    import aws_sdk_medialive.types.sdi_source_type
    import aws_sdk_medialive.types.signal_map_summary
    import aws_sdk_medialive.types.smpte2110_receiver_group_settings
    import aws_sdk_medialive.types.special_router_settings
    import aws_sdk_medialive.types.srt_settings_request
    import aws_sdk_medialive.types.start_channel_request
    import aws_sdk_medialive.types.start_channel_response
    import aws_sdk_medialive.types.start_delete_monitor_deployment_request
    import aws_sdk_medialive.types.start_delete_monitor_deployment_response
    import aws_sdk_medialive.types.start_input_device_maintenance_window_request
    import aws_sdk_medialive.types.start_input_device_maintenance_window_response
    import aws_sdk_medialive.types.start_input_device_request
    import aws_sdk_medialive.types.start_input_device_response
    import aws_sdk_medialive.types.start_monitor_deployment_request
    import aws_sdk_medialive.types.start_monitor_deployment_response
    import aws_sdk_medialive.types.start_multiplex_request
    import aws_sdk_medialive.types.start_multiplex_response
    import aws_sdk_medialive.types.start_update_signal_map_request
    import aws_sdk_medialive.types.start_update_signal_map_response
    import aws_sdk_medialive.types.stop_channel_request
    import aws_sdk_medialive.types.stop_channel_response
    import aws_sdk_medialive.types.stop_input_device_request
    import aws_sdk_medialive.types.stop_input_device_response
    import aws_sdk_medialive.types.stop_multiplex_request
    import aws_sdk_medialive.types.stop_multiplex_response
    import aws_sdk_medialive.types.tag_map
    import aws_sdk_medialive.types.tags
    import aws_sdk_medialive.types.transfer_input_device_request
    import aws_sdk_medialive.types.transfer_input_device_response
    import aws_sdk_medialive.types.transferring_input_device_summary
    import aws_sdk_medialive.types.update_account_configuration_request
    import aws_sdk_medialive.types.update_account_configuration_response
    import aws_sdk_medialive.types.update_channel_class_request
    import aws_sdk_medialive.types.update_channel_class_response
    import aws_sdk_medialive.types.update_channel_placement_group_request
    import aws_sdk_medialive.types.update_channel_placement_group_response
    import aws_sdk_medialive.types.update_channel_request
    import aws_sdk_medialive.types.update_channel_response
    import aws_sdk_medialive.types.update_cloud_watch_alarm_template_group_request
    import aws_sdk_medialive.types.update_cloud_watch_alarm_template_group_response
    import aws_sdk_medialive.types.update_cloud_watch_alarm_template_request
    import aws_sdk_medialive.types.update_cloud_watch_alarm_template_response
    import aws_sdk_medialive.types.update_cluster_request
    import aws_sdk_medialive.types.update_cluster_response
    import aws_sdk_medialive.types.update_event_bridge_rule_template_group_request
    import aws_sdk_medialive.types.update_event_bridge_rule_template_group_response
    import aws_sdk_medialive.types.update_event_bridge_rule_template_request
    import aws_sdk_medialive.types.update_event_bridge_rule_template_response
    import aws_sdk_medialive.types.update_input_device_request
    import aws_sdk_medialive.types.update_input_device_response
    import aws_sdk_medialive.types.update_input_request
    import aws_sdk_medialive.types.update_input_response
    import aws_sdk_medialive.types.update_input_security_group_request
    import aws_sdk_medialive.types.update_input_security_group_response
    import aws_sdk_medialive.types.update_multiplex_program_request
    import aws_sdk_medialive.types.update_multiplex_program_response
    import aws_sdk_medialive.types.update_multiplex_request
    import aws_sdk_medialive.types.update_multiplex_response
    import aws_sdk_medialive.types.update_network_request
    import aws_sdk_medialive.types.update_network_response
    import aws_sdk_medialive.types.update_node_request
    import aws_sdk_medialive.types.update_node_response
    import aws_sdk_medialive.types.update_node_state_request
    import aws_sdk_medialive.types.update_node_state_response
    import aws_sdk_medialive.types.update_node_state_shape
    import aws_sdk_medialive.types.update_reservation_request
    import aws_sdk_medialive.types.update_reservation_response
    import aws_sdk_medialive.types.update_sdi_source_request
    import aws_sdk_medialive.types.update_sdi_source_response
    import aws_sdk_medialive.types.vpc_output_settings


class MediaLiveClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class MediaLiveClient:
    """A client for the ``MediaLive`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = MediaLiveClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[MediaLiveClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: MediaLiveClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
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

    def accept_input_device_transfer(
        self,
        input_device_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.accept_input_device_transfer_response.AcceptInputDeviceTransferResponse":
        """Accept an incoming input device transfer. The ownership of the device will transfer to your AWS account.

        Args:
            input_device_id: The unique ID of the input device to accept. For example, hd-123456789abcdef.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.accept_input_device_transfer_request.AcceptInputDeviceTransferRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.accept_input_device_transfer_response.AcceptInputDeviceTransferResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.accept_input_device_transfer

            output, http_response = (
                aws_sdk_medialive._operations.media_live.accept_input_device_transfer.accept_input_device_transfer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.accept_input_device_transfer_request.AcceptInputDeviceTransferRequest = {}  # type: ignore[typeddict-item]
        input_["input_device_id"] = input_device_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_delete(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        channel_ids: Optional[
            "aws_sdk_medialive.types.__list_of__string.__listOf__string"
        ] = None,
        input_ids: Optional[
            "aws_sdk_medialive.types.__list_of__string.__listOf__string"
        ] = None,
        input_security_group_ids: Optional[
            "aws_sdk_medialive.types.__list_of__string.__listOf__string"
        ] = None,
        multiplex_ids: Optional[
            "aws_sdk_medialive.types.__list_of__string.__listOf__string"
        ] = None,
    ) -> "aws_sdk_medialive.types.batch_delete_response.BatchDeleteResponse":
        """Starts delete of resources.

        Args:
            channel_ids: List of channel IDs
            input_ids: List of input IDs
            input_security_group_ids: List of input security group IDs
            multiplex_ids: List of multiplex IDs

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.batch_delete_request.BatchDeleteRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.batch_delete_response.BatchDeleteResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.batch_delete

            output, http_response = (
                aws_sdk_medialive._operations.media_live.batch_delete.batch_delete(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.batch_delete_request.BatchDeleteRequest = {}  # type: ignore[typeddict-item]
        if channel_ids is not None:
            input_["channel_ids"] = channel_ids
        if input_ids is not None:
            input_["input_ids"] = input_ids
        if input_security_group_ids is not None:
            input_["input_security_group_ids"] = input_security_group_ids
        if multiplex_ids is not None:
            input_["multiplex_ids"] = multiplex_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_start(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        channel_ids: Optional[
            "aws_sdk_medialive.types.__list_of__string.__listOf__string"
        ] = None,
        multiplex_ids: Optional[
            "aws_sdk_medialive.types.__list_of__string.__listOf__string"
        ] = None,
    ) -> "aws_sdk_medialive.types.batch_start_response.BatchStartResponse":
        """Starts existing resources

        Args:
            channel_ids: List of channel IDs
            multiplex_ids: List of multiplex IDs

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.batch_start_request.BatchStartRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.batch_start_response.BatchStartResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.batch_start

            output, http_response = (
                aws_sdk_medialive._operations.media_live.batch_start.batch_start(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.batch_start_request.BatchStartRequest = {}  # type: ignore[typeddict-item]
        if channel_ids is not None:
            input_["channel_ids"] = channel_ids
        if multiplex_ids is not None:
            input_["multiplex_ids"] = multiplex_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_stop(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        channel_ids: Optional[
            "aws_sdk_medialive.types.__list_of__string.__listOf__string"
        ] = None,
        multiplex_ids: Optional[
            "aws_sdk_medialive.types.__list_of__string.__listOf__string"
        ] = None,
    ) -> "aws_sdk_medialive.types.batch_stop_response.BatchStopResponse":
        """Stops running resources

        Args:
            channel_ids: List of channel IDs
            multiplex_ids: List of multiplex IDs

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.batch_stop_request.BatchStopRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.batch_stop_response.BatchStopResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.batch_stop

            output, http_response = (
                aws_sdk_medialive._operations.media_live.batch_stop.batch_stop(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.batch_stop_request.BatchStopRequest = {}  # type: ignore[typeddict-item]
        if channel_ids is not None:
            input_["channel_ids"] = channel_ids
        if multiplex_ids is not None:
            input_["multiplex_ids"] = multiplex_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_update_schedule(
        self,
        channel_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        creates: Optional[
            "aws_sdk_medialive.types.batch_schedule_action_create_request.BatchScheduleActionCreateRequest"
        ] = None,
        deletes: Optional[
            "aws_sdk_medialive.types.batch_schedule_action_delete_request.BatchScheduleActionDeleteRequest"
        ] = None,
    ) -> "aws_sdk_medialive.types.batch_update_schedule_response.BatchUpdateScheduleResponse":
        """Update a channel schedule

        Args:
            channel_id: Id of the channel whose schedule is being updated.
            creates: Schedule actions to create in the schedule.
            deletes: Schedule actions to delete from the schedule.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.batch_update_schedule_request.BatchUpdateScheduleRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.batch_update_schedule_response.BatchUpdateScheduleResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.batch_update_schedule

            output, http_response = (
                aws_sdk_medialive._operations.media_live.batch_update_schedule.batch_update_schedule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.batch_update_schedule_request.BatchUpdateScheduleRequest = {}  # type: ignore[typeddict-item]
        input_["channel_id"] = channel_id
        if creates is not None:
            input_["creates"] = creates
        if deletes is not None:
            input_["deletes"] = deletes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def cancel_input_device_transfer(
        self,
        input_device_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.cancel_input_device_transfer_response.CancelInputDeviceTransferResponse":
        """Cancel an input device transfer that you have requested.

        Args:
            input_device_id: The unique ID of the input device to cancel. For example, hd-123456789abcdef.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.cancel_input_device_transfer_request.CancelInputDeviceTransferRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.cancel_input_device_transfer_response.CancelInputDeviceTransferResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.cancel_input_device_transfer

            output, http_response = (
                aws_sdk_medialive._operations.media_live.cancel_input_device_transfer.cancel_input_device_transfer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.cancel_input_device_transfer_request.CancelInputDeviceTransferRequest = {}  # type: ignore[typeddict-item]
        input_["input_device_id"] = input_device_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def claim_device(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        id: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "aws_sdk_medialive.types.claim_device_response.ClaimDeviceResponse":
        """Send a request to claim an AWS Elemental device that you have purchased from a third-party vendor. After the request succeeds, you will own the device.

        Args:
            id: The id of the device you want to claim.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.claim_device_request.ClaimDeviceRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.claim_device_response.ClaimDeviceResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.claim_device

            output, http_response = (
                aws_sdk_medialive._operations.media_live.claim_device.claim_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.claim_device_request.ClaimDeviceRequest = {}  # type: ignore[typeddict-item]
        if id is not None:
            input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_channel(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        cdi_input_specification: Optional[
            "aws_sdk_medialive.types.cdi_input_specification.CdiInputSpecification"
        ] = None,
        channel_class: Optional[
            "aws_sdk_medialive.types.channel_class.ChannelClass"
        ] = None,
        destinations: Optional[
            "aws_sdk_medialive.types.__list_of_output_destination.__listOfOutputDestination"
        ] = None,
        encoder_settings: Optional[
            "aws_sdk_medialive.types.encoder_settings.EncoderSettings"
        ] = None,
        input_attachments: Optional[
            "aws_sdk_medialive.types.__list_of_input_attachment.__listOfInputAttachment"
        ] = None,
        input_specification: Optional[
            "aws_sdk_medialive.types.input_specification.InputSpecification"
        ] = None,
        log_level: Optional["aws_sdk_medialive.types.log_level.LogLevel"] = None,
        maintenance: Optional[
            "aws_sdk_medialive.types.maintenance_create_settings.MaintenanceCreateSettings"
        ] = None,
        name: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        request_id: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        reserved: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        role_arn: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        tags: Optional["aws_sdk_medialive.types.tags.Tags"] = None,
        vpc: Optional[
            "aws_sdk_medialive.types.vpc_output_settings.VpcOutputSettings"
        ] = None,
        anywhere_settings: Optional[
            "aws_sdk_medialive.types.anywhere_settings.AnywhereSettings"
        ] = None,
        channel_engine_version: Optional[
            "aws_sdk_medialive.types.channel_engine_version_request.ChannelEngineVersionRequest"
        ] = None,
        dry_run: Optional["aws_sdk_medialive.types.__boolean.__boolean"] = None,
        linked_channel_settings: Optional[
            "aws_sdk_medialive.types.linked_channel_settings.LinkedChannelSettings"
        ] = None,
        channel_security_groups: Optional[
            "aws_sdk_medialive.types.__list_of__string.__listOf__string"
        ] = None,
        inference_settings: Optional[
            "aws_sdk_medialive.types.inference_settings.InferenceSettings"
        ] = None,
    ) -> "aws_sdk_medialive.types.create_channel_response.CreateChannelResponse":
        """Creates a new channel

        Args:
            cdi_input_specification: Specification of CDI inputs for this channel
            channel_class: The class for this channel. STANDARD for a channel with two pipelines or SINGLE_PIPELINE for a channel with one pipeline.
            input_attachments: List of input attachments for channel.
            input_specification: Specification of network and file inputs for this channel
            log_level: The log level to write to CloudWatch Logs.
            maintenance: Maintenance settings for this channel.
            name: Name of channel.
            request_id: Unique request ID to be specified. This is needed to prevent retries from creating multiple resources.
            reserved: Deprecated field that's only usable by whitelisted customers.
            role_arn: An optional Amazon Resource Name (ARN) of the role to assume when running the Channel.
            tags: A collection of key-value pairs.
            vpc: Settings for the VPC outputs
            anywhere_settings: The Elemental Anywhere settings for this channel.
            channel_engine_version: The desired engine version for this channel.
            linked_channel_settings: The linked channel settings for the channel.
            channel_security_groups: A list of IDs for all the Input Security Groups attached to the channel.
            inference_settings: Include this setting to include Elemental Inference features in this channel.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.create_channel_request.CreateChannelRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.create_channel_response.CreateChannelResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.create_channel

            output, http_response = (
                aws_sdk_medialive._operations.media_live.create_channel.create_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.create_channel_request.CreateChannelRequest = {}  # type: ignore[typeddict-item]
        if cdi_input_specification is not None:
            input_["cdi_input_specification"] = cdi_input_specification
        if channel_class is not None:
            input_["channel_class"] = channel_class
        if destinations is not None:
            input_["destinations"] = destinations
        if encoder_settings is not None:
            input_["encoder_settings"] = encoder_settings
        if input_attachments is not None:
            input_["input_attachments"] = input_attachments
        if input_specification is not None:
            input_["input_specification"] = input_specification
        if log_level is not None:
            input_["log_level"] = log_level
        if maintenance is not None:
            input_["maintenance"] = maintenance
        if name is not None:
            input_["name"] = name
        if request_id is not None:
            input_["request_id"] = request_id
        if reserved is not None:
            input_["reserved"] = reserved
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if tags is not None:
            input_["tags"] = tags
        if vpc is not None:
            input_["vpc"] = vpc
        if anywhere_settings is not None:
            input_["anywhere_settings"] = anywhere_settings
        if channel_engine_version is not None:
            input_["channel_engine_version"] = channel_engine_version
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if linked_channel_settings is not None:
            input_["linked_channel_settings"] = linked_channel_settings
        if channel_security_groups is not None:
            input_["channel_security_groups"] = channel_security_groups
        if inference_settings is not None:
            input_["inference_settings"] = inference_settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_channel_placement_group(
        self,
        cluster_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        name: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        nodes: Optional[
            "aws_sdk_medialive.types.__list_of__string.__listOf__string"
        ] = None,
        request_id: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        tags: Optional["aws_sdk_medialive.types.tags.Tags"] = None,
    ) -> "aws_sdk_medialive.types.create_channel_placement_group_response.CreateChannelPlacementGroupResponse":
        """Create a ChannelPlacementGroup in the specified Cluster. As part of the create operation, you specify the Nodes to attach the group to.After you create a ChannelPlacementGroup, you add Channels to the group (you do this by modifying the Channels to add them to a specific group). You now have an association of Channels to ChannelPlacementGroup, and ChannelPlacementGroup to Nodes. This association means that all the Channels in the group are able to run on any of the Nodes associated with the group.

        Args:
            cluster_id: The ID of the cluster.
            name: Specify a name that is unique in the Cluster. You can't change the name. Names are case-sensitive.
            nodes: An array of one ID for the Node that you want to associate with the ChannelPlacementGroup. (You can't associate more than one Node with the ChannelPlacementGroup.) The Node and the ChannelPlacementGroup must be in the same Cluster.
            request_id: An ID that you assign to a create request. This ID ensures idempotency when creating resources. the request.
            tags: A collection of key-value pairs.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.create_channel_placement_group_request.CreateChannelPlacementGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.create_channel_placement_group_response.CreateChannelPlacementGroupResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.create_channel_placement_group

            output, http_response = (
                aws_sdk_medialive._operations.media_live.create_channel_placement_group.create_channel_placement_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.create_channel_placement_group_request.CreateChannelPlacementGroupRequest = {}  # type: ignore[typeddict-item]
        input_["cluster_id"] = cluster_id
        if name is not None:
            input_["name"] = name
        if nodes is not None:
            input_["nodes"] = nodes
        if request_id is not None:
            input_["request_id"] = request_id
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_cloud_watch_alarm_template(
        self,
        comparison_operator: "aws_sdk_medialive.types.cloud_watch_alarm_template_comparison_operator.CloudWatchAlarmTemplateComparisonOperator",
        evaluation_periods: "aws_sdk_medialive.types.__integer_min1.__integerMin1",
        group_identifier: "aws_sdk_medialive.types.__string_pattern_s.__stringPatternS",
        metric_name: "aws_sdk_medialive.types.__string_max64.__stringMax64",
        name: "aws_sdk_medialive.types.__string_min1_max255_pattern_s.__stringMin1Max255PatternS",
        period: "aws_sdk_medialive.types.__integer_min10_max86400.__integerMin10Max86400",
        statistic: "aws_sdk_medialive.types.cloud_watch_alarm_template_statistic.CloudWatchAlarmTemplateStatistic",
        target_resource_type: "aws_sdk_medialive.types.cloud_watch_alarm_template_target_resource_type.CloudWatchAlarmTemplateTargetResourceType",
        threshold: "aws_sdk_medialive.types.__double.__double",
        treat_missing_data: "aws_sdk_medialive.types.cloud_watch_alarm_template_treat_missing_data.CloudWatchAlarmTemplateTreatMissingData",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        datapoints_to_alarm: Optional[
            "aws_sdk_medialive.types.__integer_min1.__integerMin1"
        ] = None,
        description: Optional[
            "aws_sdk_medialive.types.__string_min0_max1024.__stringMin0Max1024"
        ] = None,
        tags: Optional["aws_sdk_medialive.types.tag_map.TagMap"] = None,
        request_id: Optional[
            "aws_sdk_medialive.types.__string_min1_max256_pattern_s.__stringMin1Max256PatternS"
        ] = None,
    ) -> "aws_sdk_medialive.types.create_cloud_watch_alarm_template_response.CreateCloudWatchAlarmTemplateResponse":
        """Creates a cloudwatch alarm template to dynamically generate cloudwatch metric alarms on targeted resource types.

        Args:
            datapoints_to_alarm: The number of datapoints within the evaluation period that must be breaching to trigger the alarm.
            description: A resource's optional description.
            evaluation_periods: The number of periods over which data is compared to the specified threshold.
            group_identifier: A cloudwatch alarm template group's identifier. Can be either be its id or current name.
            metric_name: The name of the metric associated with the alarm. Must be compatible with targetResourceType.
            name: A resource's name. Names must be unique within the scope of a resource type in a specific region.
            period: The period, in seconds, over which the specified statistic is applied.
            threshold: The threshold value to compare with the specified statistic.
            request_id: An ID that you assign to a create request. This ID ensures idempotency when creating resources.

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.create_cloud_watch_alarm_template_request.CreateCloudWatchAlarmTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.create_cloud_watch_alarm_template_response.CreateCloudWatchAlarmTemplateResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.create_cloud_watch_alarm_template

            output, http_response = (
                aws_sdk_medialive._operations.media_live.create_cloud_watch_alarm_template.create_cloud_watch_alarm_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.create_cloud_watch_alarm_template_request.CreateCloudWatchAlarmTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["comparison_operator"] = comparison_operator
        if datapoints_to_alarm is not None:
            input_["datapoints_to_alarm"] = datapoints_to_alarm
        if description is not None:
            input_["description"] = description
        input_["evaluation_periods"] = evaluation_periods
        input_["group_identifier"] = group_identifier
        input_["metric_name"] = metric_name
        input_["name"] = name
        input_["period"] = period
        input_["statistic"] = statistic
        if tags is not None:
            input_["tags"] = tags
        input_["target_resource_type"] = target_resource_type
        input_["threshold"] = threshold
        input_["treat_missing_data"] = treat_missing_data
        if request_id is not None:
            input_["request_id"] = request_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_cloud_watch_alarm_template_group(
        self,
        name: "aws_sdk_medialive.types.__string_min1_max255_pattern_s.__stringMin1Max255PatternS",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        description: Optional[
            "aws_sdk_medialive.types.__string_min0_max1024.__stringMin0Max1024"
        ] = None,
        tags: Optional["aws_sdk_medialive.types.tag_map.TagMap"] = None,
        request_id: Optional[
            "aws_sdk_medialive.types.__string_min1_max256_pattern_s.__stringMin1Max256PatternS"
        ] = None,
    ) -> "aws_sdk_medialive.types.create_cloud_watch_alarm_template_group_response.CreateCloudWatchAlarmTemplateGroupResponse":
        """Creates a cloudwatch alarm template group to group your cloudwatch alarm templates and to attach to signal maps for dynamically creating alarms.

        Args:
            description: A resource's optional description.
            name: A resource's name. Names must be unique within the scope of a resource type in a specific region.
            request_id: An ID that you assign to a create request. This ID ensures idempotency when creating resources.

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.create_cloud_watch_alarm_template_group_request.CreateCloudWatchAlarmTemplateGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.create_cloud_watch_alarm_template_group_response.CreateCloudWatchAlarmTemplateGroupResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.create_cloud_watch_alarm_template_group

            output, http_response = (
                aws_sdk_medialive._operations.media_live.create_cloud_watch_alarm_template_group.create_cloud_watch_alarm_template_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.create_cloud_watch_alarm_template_group_request.CreateCloudWatchAlarmTemplateGroupRequest = {}  # type: ignore[typeddict-item]
        if description is not None:
            input_["description"] = description
        input_["name"] = name
        if tags is not None:
            input_["tags"] = tags
        if request_id is not None:
            input_["request_id"] = request_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_cluster(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        cluster_type: Optional[
            "aws_sdk_medialive.types.cluster_type.ClusterType"
        ] = None,
        instance_role_arn: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        name: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        network_settings: Optional[
            "aws_sdk_medialive.types.cluster_network_settings_create_request.ClusterNetworkSettingsCreateRequest"
        ] = None,
        request_id: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        tags: Optional["aws_sdk_medialive.types.tags.Tags"] = None,
    ) -> "aws_sdk_medialive.types.create_cluster_response.CreateClusterResponse":
        """Create a new Cluster.

        Args:
            cluster_type: Specify a type. All the Nodes that you later add to this Cluster must be this type of hardware. One Cluster instance can't contain different hardware types. You won't be able to change this parameter after you create the Cluster.
            instance_role_arn: The ARN of the IAM role for the Node in this Cluster. The role must include all the operations that you expect these Node to perform. If necessary, create a role in IAM, then attach it here.
            name: Specify a name that is unique in the AWS account. We recommend that you assign a name that hints at the types of Nodes in the Cluster. Names are case-sensitive.
            network_settings: Network settings that connect the Nodes in the Cluster to one or more of the Networks that the Cluster is associated with.
            request_id: The unique ID of the request.
            tags: A collection of key-value pairs.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.create_cluster_request.CreateClusterRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.create_cluster_response.CreateClusterResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.create_cluster

            output, http_response = (
                aws_sdk_medialive._operations.media_live.create_cluster.create_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.create_cluster_request.CreateClusterRequest = {}  # type: ignore[typeddict-item]
        if cluster_type is not None:
            input_["cluster_type"] = cluster_type
        if instance_role_arn is not None:
            input_["instance_role_arn"] = instance_role_arn
        if name is not None:
            input_["name"] = name
        if network_settings is not None:
            input_["network_settings"] = network_settings
        if request_id is not None:
            input_["request_id"] = request_id
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_event_bridge_rule_template(
        self,
        event_type: "aws_sdk_medialive.types.event_bridge_rule_template_event_type.EventBridgeRuleTemplateEventType",
        group_identifier: "aws_sdk_medialive.types.__string_pattern_s.__stringPatternS",
        name: "aws_sdk_medialive.types.__string_min1_max255_pattern_s.__stringMin1Max255PatternS",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        description: Optional[
            "aws_sdk_medialive.types.__string_min0_max1024.__stringMin0Max1024"
        ] = None,
        event_targets: Optional[
            "aws_sdk_medialive.types.__list_of_event_bridge_rule_template_target.__listOfEventBridgeRuleTemplateTarget"
        ] = None,
        tags: Optional["aws_sdk_medialive.types.tag_map.TagMap"] = None,
        request_id: Optional[
            "aws_sdk_medialive.types.__string_min1_max256_pattern_s.__stringMin1Max256PatternS"
        ] = None,
    ) -> "aws_sdk_medialive.types.create_event_bridge_rule_template_response.CreateEventBridgeRuleTemplateResponse":
        """Creates an eventbridge rule template to monitor events and send notifications to your targeted resources.

        Args:
            description: A resource's optional description.
            group_identifier: An eventbridge rule template group's identifier. Can be either be its id or current name.
            name: A resource's name. Names must be unique within the scope of a resource type in a specific region.
            request_id: An ID that you assign to a create request. This ID ensures idempotency when creating resources.

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.create_event_bridge_rule_template_request.CreateEventBridgeRuleTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.create_event_bridge_rule_template_response.CreateEventBridgeRuleTemplateResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.create_event_bridge_rule_template

            output, http_response = (
                aws_sdk_medialive._operations.media_live.create_event_bridge_rule_template.create_event_bridge_rule_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.create_event_bridge_rule_template_request.CreateEventBridgeRuleTemplateRequest = {}  # type: ignore[typeddict-item]
        if description is not None:
            input_["description"] = description
        if event_targets is not None:
            input_["event_targets"] = event_targets
        input_["event_type"] = event_type
        input_["group_identifier"] = group_identifier
        input_["name"] = name
        if tags is not None:
            input_["tags"] = tags
        if request_id is not None:
            input_["request_id"] = request_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_event_bridge_rule_template_group(
        self,
        name: "aws_sdk_medialive.types.__string_min1_max255_pattern_s.__stringMin1Max255PatternS",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        description: Optional[
            "aws_sdk_medialive.types.__string_min0_max1024.__stringMin0Max1024"
        ] = None,
        tags: Optional["aws_sdk_medialive.types.tag_map.TagMap"] = None,
        request_id: Optional[
            "aws_sdk_medialive.types.__string_min1_max256_pattern_s.__stringMin1Max256PatternS"
        ] = None,
    ) -> "aws_sdk_medialive.types.create_event_bridge_rule_template_group_response.CreateEventBridgeRuleTemplateGroupResponse":
        """Creates an eventbridge rule template group to group your eventbridge rule templates and to attach to signal maps for dynamically creating notification rules.

        Args:
            description: A resource's optional description.
            name: A resource's name. Names must be unique within the scope of a resource type in a specific region.
            request_id: An ID that you assign to a create request. This ID ensures idempotency when creating resources.

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.create_event_bridge_rule_template_group_request.CreateEventBridgeRuleTemplateGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.create_event_bridge_rule_template_group_response.CreateEventBridgeRuleTemplateGroupResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.create_event_bridge_rule_template_group

            output, http_response = (
                aws_sdk_medialive._operations.media_live.create_event_bridge_rule_template_group.create_event_bridge_rule_template_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.create_event_bridge_rule_template_group_request.CreateEventBridgeRuleTemplateGroupRequest = {}  # type: ignore[typeddict-item]
        if description is not None:
            input_["description"] = description
        input_["name"] = name
        if tags is not None:
            input_["tags"] = tags
        if request_id is not None:
            input_["request_id"] = request_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_input(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        destinations: Optional[
            "aws_sdk_medialive.types.__list_of_input_destination_request.__listOfInputDestinationRequest"
        ] = None,
        input_devices: Optional[
            "aws_sdk_medialive.types.__list_of_input_device_settings.__listOfInputDeviceSettings"
        ] = None,
        input_security_groups: Optional[
            "aws_sdk_medialive.types.__list_of__string.__listOf__string"
        ] = None,
        media_connect_flows: Optional[
            "aws_sdk_medialive.types.__list_of_media_connect_flow_request.__listOfMediaConnectFlowRequest"
        ] = None,
        name: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        request_id: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        role_arn: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        sources: Optional[
            "aws_sdk_medialive.types.__list_of_input_source_request.__listOfInputSourceRequest"
        ] = None,
        tags: Optional["aws_sdk_medialive.types.tags.Tags"] = None,
        type: Optional["aws_sdk_medialive.types.input_type.InputType"] = None,
        vpc: Optional[
            "aws_sdk_medialive.types.input_vpc_request.InputVpcRequest"
        ] = None,
        srt_settings: Optional[
            "aws_sdk_medialive.types.srt_settings_request.SrtSettingsRequest"
        ] = None,
        input_network_location: Optional[
            "aws_sdk_medialive.types.input_network_location.InputNetworkLocation"
        ] = None,
        multicast_settings: Optional[
            "aws_sdk_medialive.types.multicast_settings_create_request.MulticastSettingsCreateRequest"
        ] = None,
        smpte2110_receiver_group_settings: Optional[
            "aws_sdk_medialive.types.smpte2110_receiver_group_settings.Smpte2110ReceiverGroupSettings"
        ] = None,
        sdi_sources: Optional[
            "aws_sdk_medialive.types.input_sdi_sources.InputSdiSources"
        ] = None,
        router_settings: Optional[
            "aws_sdk_medialive.types.router_settings.RouterSettings"
        ] = None,
    ) -> "aws_sdk_medialive.types.create_input_response.CreateInputResponse":
        """Create an input

        Args:
            destinations: Destination settings for PUSH type inputs.
            input_devices: Settings for the devices.
            input_security_groups: A list of security groups referenced by IDs to attach to the input.
            media_connect_flows: A list of the MediaConnect Flows that you want to use in this input. You can specify as few as one Flow and presently, as many as two. The only requirement is when you have more than one is that each Flow is in a separate Availability Zone as this ensures your EML input is redundant to AZ issues.
            name: Name of the input.
            request_id: Unique identifier of the request to ensure the request is handled exactly once in case of retries.
            role_arn: The Amazon Resource Name (ARN) of the role this input assumes during and after creation.
            sources: The source URLs for a PULL-type input. Every PULL type input needs exactly two source URLs for redundancy. Only specify sources for PULL type Inputs. Leave Destinations empty.
            tags: A collection of key-value pairs.
            srt_settings: The settings associated with an SRT input.
            input_network_location: The location of this input. AWS, for an input existing in the AWS Cloud, On-Prem for an input in a customer network.
            multicast_settings: Multicast Input settings.
            smpte2110_receiver_group_settings: Include this parameter if the input is a SMPTE 2110 input, to identify the stream sources for this input.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.create_input_request.CreateInputRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.create_input_response.CreateInputResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.create_input

            output, http_response = (
                aws_sdk_medialive._operations.media_live.create_input.create_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.create_input_request.CreateInputRequest = {}  # type: ignore[typeddict-item]
        if destinations is not None:
            input_["destinations"] = destinations
        if input_devices is not None:
            input_["input_devices"] = input_devices
        if input_security_groups is not None:
            input_["input_security_groups"] = input_security_groups
        if media_connect_flows is not None:
            input_["media_connect_flows"] = media_connect_flows
        if name is not None:
            input_["name"] = name
        if request_id is not None:
            input_["request_id"] = request_id
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if sources is not None:
            input_["sources"] = sources
        if tags is not None:
            input_["tags"] = tags
        if type is not None:
            input_["type"] = type
        if vpc is not None:
            input_["vpc"] = vpc
        if srt_settings is not None:
            input_["srt_settings"] = srt_settings
        if input_network_location is not None:
            input_["input_network_location"] = input_network_location
        if multicast_settings is not None:
            input_["multicast_settings"] = multicast_settings
        if smpte2110_receiver_group_settings is not None:
            input_["smpte2110_receiver_group_settings"] = (
                smpte2110_receiver_group_settings
            )
        if sdi_sources is not None:
            input_["sdi_sources"] = sdi_sources
        if router_settings is not None:
            input_["router_settings"] = router_settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_input_security_group(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        tags: Optional["aws_sdk_medialive.types.tags.Tags"] = None,
        whitelist_rules: Optional[
            "aws_sdk_medialive.types.__list_of_input_whitelist_rule_cidr.__listOfInputWhitelistRuleCidr"
        ] = None,
    ) -> "aws_sdk_medialive.types.create_input_security_group_response.CreateInputSecurityGroupResponse":
        """Creates a Input Security Group

        Args:
            tags: A collection of key-value pairs.
            whitelist_rules: List of IPv4 CIDR addresses to whitelist

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.create_input_security_group_request.CreateInputSecurityGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.create_input_security_group_response.CreateInputSecurityGroupResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.create_input_security_group

            output, http_response = (
                aws_sdk_medialive._operations.media_live.create_input_security_group.create_input_security_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.create_input_security_group_request.CreateInputSecurityGroupRequest = {}  # type: ignore[typeddict-item]
        if tags is not None:
            input_["tags"] = tags
        if whitelist_rules is not None:
            input_["whitelist_rules"] = whitelist_rules

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_multiplex(
        self,
        availability_zones: "aws_sdk_medialive.types.__list_of__string.__listOf__string",
        multiplex_settings: "aws_sdk_medialive.types.multiplex_settings.MultiplexSettings",
        name: "aws_sdk_medialive.types.__string.__string",
        request_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        tags: Optional["aws_sdk_medialive.types.tags.Tags"] = None,
    ) -> "aws_sdk_medialive.types.create_multiplex_response.CreateMultiplexResponse":
        """Create a new multiplex.

        Args:
            availability_zones: A list of availability zones for the multiplex. You must specify exactly two.
            multiplex_settings: Configuration for a multiplex event.
            name: Name of multiplex.
            request_id: Unique request ID. This prevents retries from creating multiple resources.
            tags: A collection of key-value pairs.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.create_multiplex_request.CreateMultiplexRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.create_multiplex_response.CreateMultiplexResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.create_multiplex

            output, http_response = (
                aws_sdk_medialive._operations.media_live.create_multiplex.create_multiplex(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.create_multiplex_request.CreateMultiplexRequest = {}  # type: ignore[typeddict-item]
        input_["availability_zones"] = availability_zones
        input_["multiplex_settings"] = multiplex_settings
        input_["name"] = name
        input_["request_id"] = request_id
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_multiplex_program(
        self,
        multiplex_id: "aws_sdk_medialive.types.__string.__string",
        multiplex_program_settings: "aws_sdk_medialive.types.multiplex_program_settings.MultiplexProgramSettings",
        program_name: "aws_sdk_medialive.types.__string.__string",
        request_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.create_multiplex_program_response.CreateMultiplexProgramResponse":
        """Create a new program in the multiplex.

        Args:
            multiplex_id: ID of the multiplex where the program is to be created.
            multiplex_program_settings: The settings for this multiplex program.
            program_name: Name of multiplex program.
            request_id: Unique request ID. This prevents retries from creating multiple resources.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.create_multiplex_program_request.CreateMultiplexProgramRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.create_multiplex_program_response.CreateMultiplexProgramResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.create_multiplex_program

            output, http_response = (
                aws_sdk_medialive._operations.media_live.create_multiplex_program.create_multiplex_program(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.create_multiplex_program_request.CreateMultiplexProgramRequest = {}  # type: ignore[typeddict-item]
        input_["multiplex_id"] = multiplex_id
        input_["multiplex_program_settings"] = multiplex_program_settings
        input_["program_name"] = program_name
        input_["request_id"] = request_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_network(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        ip_pools: Optional[
            "aws_sdk_medialive.types.__list_of_ip_pool_create_request.__listOfIpPoolCreateRequest"
        ] = None,
        name: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        request_id: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        routes: Optional[
            "aws_sdk_medialive.types.__list_of_route_create_request.__listOfRouteCreateRequest"
        ] = None,
        tags: Optional["aws_sdk_medialive.types.tags.Tags"] = None,
    ) -> "aws_sdk_medialive.types.create_network_response.CreateNetworkResponse":
        """Create as many Networks as you need. You will associate one or more Clusters with each Network.Each Network provides MediaLive Anywhere with required information about the network in your organization that you are using for video encoding using MediaLive.

        Args:
            ip_pools: An array of IpPoolCreateRequests that identify a collection of IP addresses in your network that you want to reserve for use in MediaLive Anywhere. MediaLiveAnywhere uses these IP addresses for Push inputs (in both Bridge and NATnetworks) and for output destinations (only in Bridge networks). EachIpPoolUpdateRequest specifies one CIDR block.
            name: Specify a name that is unique in the AWS account. We recommend that you assign a name that hints at the type of traffic on the network. Names are case-sensitive.
            request_id: An ID that you assign to a create request. This ID ensures idempotency when creating resources.
            routes: An array of routes that MediaLive Anywhere needs to know about in order to route encoding traffic.
            tags: A collection of key-value pairs.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.create_network_request.CreateNetworkRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.create_network_response.CreateNetworkResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.create_network

            output, http_response = (
                aws_sdk_medialive._operations.media_live.create_network.create_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.create_network_request.CreateNetworkRequest = {}  # type: ignore[typeddict-item]
        if ip_pools is not None:
            input_["ip_pools"] = ip_pools
        if name is not None:
            input_["name"] = name
        if request_id is not None:
            input_["request_id"] = request_id
        if routes is not None:
            input_["routes"] = routes
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_node(
        self,
        cluster_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        name: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        node_interface_mappings: Optional[
            "aws_sdk_medialive.types.__list_of_node_interface_mapping_create_request.__listOfNodeInterfaceMappingCreateRequest"
        ] = None,
        request_id: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        role: Optional["aws_sdk_medialive.types.node_role.NodeRole"] = None,
        tags: Optional["aws_sdk_medialive.types.tags.Tags"] = None,
    ) -> "aws_sdk_medialive.types.create_node_response.CreateNodeResponse":
        """Create a Node in the specified Cluster. You can also create Nodes using the CreateNodeRegistrationScript. Note that you can't move a Node to another Cluster.

        Args:
            cluster_id: The ID of the cluster.
            name: The user-specified name of the Node to be created.
            node_interface_mappings: Documentation update needed
            request_id: An ID that you assign to a create request. This ID ensures idempotency when creating resources.
            role: The initial role of the Node in the Cluster. ACTIVE means the Node is available for encoding. BACKUP means the Node is a redundant Node and might get used if an ACTIVE Node fails.
            tags: A collection of key-value pairs.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.create_node_request.CreateNodeRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.create_node_response.CreateNodeResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.create_node

            output, http_response = (
                aws_sdk_medialive._operations.media_live.create_node.create_node(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.create_node_request.CreateNodeRequest = {}  # type: ignore[typeddict-item]
        input_["cluster_id"] = cluster_id
        if name is not None:
            input_["name"] = name
        if node_interface_mappings is not None:
            input_["node_interface_mappings"] = node_interface_mappings
        if request_id is not None:
            input_["request_id"] = request_id
        if role is not None:
            input_["role"] = role
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_node_registration_script(
        self,
        cluster_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        id: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        name: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        node_interface_mappings: Optional[
            "aws_sdk_medialive.types.__list_of_node_interface_mapping.__listOfNodeInterfaceMapping"
        ] = None,
        request_id: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        role: Optional["aws_sdk_medialive.types.node_role.NodeRole"] = None,
    ) -> "aws_sdk_medialive.types.create_node_registration_script_response.CreateNodeRegistrationScriptResponse":
        """Create the Register Node script for all the nodes intended for a specific Cluster. You will then run the script on each hardware unit that is intended for that Cluster. The script creates a Node in the specified Cluster. It then binds the Node to this hardware unit, and activates the node hardware for use with MediaLive Anywhere.

        Args:
            cluster_id: The ID of the cluster
            id: If you're generating a re-registration script for an already existing node, this is where you provide the id.
            name: Specify a pattern for MediaLive Anywhere to use to assign a name to each Node in the Cluster. The pattern can include the variables $hn (hostname of the node hardware) and $ts for the date and time that the Node is created, in UTC (for example, 2024-08-20T23:35:12Z).
            node_interface_mappings: Documentation update needed
            request_id: An ID that you assign to a create request. This ID ensures idempotency when creating resources.
            role: The initial role of the Node in the Cluster. ACTIVE means the Node is available for encoding. BACKUP means the Node is a redundant Node and might get used if an ACTIVE Node fails.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.create_node_registration_script_request.CreateNodeRegistrationScriptRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.create_node_registration_script_response.CreateNodeRegistrationScriptResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.create_node_registration_script

            output, http_response = (
                aws_sdk_medialive._operations.media_live.create_node_registration_script.create_node_registration_script(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.create_node_registration_script_request.CreateNodeRegistrationScriptRequest = {}  # type: ignore[typeddict-item]
        input_["cluster_id"] = cluster_id
        if id is not None:
            input_["id"] = id
        if name is not None:
            input_["name"] = name
        if node_interface_mappings is not None:
            input_["node_interface_mappings"] = node_interface_mappings
        if request_id is not None:
            input_["request_id"] = request_id
        if role is not None:
            input_["role"] = role

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_partner_input(
        self,
        input_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        request_id: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        tags: Optional["aws_sdk_medialive.types.tags.Tags"] = None,
    ) -> "aws_sdk_medialive.types.create_partner_input_response.CreatePartnerInputResponse":
        """Create a partner input

        Args:
            input_id: Unique ID of the input.
            request_id: Unique identifier of the request to ensure the request is handled exactly once in case of retries.
            tags: A collection of key-value pairs.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.create_partner_input_request.CreatePartnerInputRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.create_partner_input_response.CreatePartnerInputResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.create_partner_input

            output, http_response = (
                aws_sdk_medialive._operations.media_live.create_partner_input.create_partner_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.create_partner_input_request.CreatePartnerInputRequest = {}  # type: ignore[typeddict-item]
        input_["input_id"] = input_id
        if request_id is not None:
            input_["request_id"] = request_id
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_sdi_source(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        mode: Optional["aws_sdk_medialive.types.sdi_source_mode.SdiSourceMode"] = None,
        name: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        request_id: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        tags: Optional["aws_sdk_medialive.types.tags.Tags"] = None,
        type: Optional["aws_sdk_medialive.types.sdi_source_type.SdiSourceType"] = None,
    ) -> "aws_sdk_medialive.types.create_sdi_source_response.CreateSdiSourceResponse":
        """Create an SdiSource for each video source that uses the SDI protocol. You will reference the SdiSource when you create an SDI input in MediaLive. You will also reference it in an SdiSourceMapping, in order to create a connection between the logical SdiSource and the physical SDI card and port that the physical SDI source uses.

        Args:
            mode: Applies only if the type is QUAD. Specify the mode for handling the quad-link signal: QUADRANT or INTERLEAVE.
            name: Specify a name that is unique in the AWS account. We recommend you assign a name that describes the source, for example curling-cameraA. Names are case-sensitive.
            request_id: An ID that you assign to a create request. This ID ensures idempotency when creating resources.
            tags: A collection of key-value pairs.
            type: Specify the type of the SDI source: SINGLE: The source is a single-link source. QUAD: The source is one part of a quad-link source.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.create_sdi_source_request.CreateSdiSourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.create_sdi_source_response.CreateSdiSourceResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.create_sdi_source

            output, http_response = (
                aws_sdk_medialive._operations.media_live.create_sdi_source.create_sdi_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.create_sdi_source_request.CreateSdiSourceRequest = {}  # type: ignore[typeddict-item]
        if mode is not None:
            input_["mode"] = mode
        if name is not None:
            input_["name"] = name
        if request_id is not None:
            input_["request_id"] = request_id
        if tags is not None:
            input_["tags"] = tags
        if type is not None:
            input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_signal_map(
        self,
        discovery_entry_point_arn: "aws_sdk_medialive.types.__string_min1_max2048.__stringMin1Max2048",
        name: "aws_sdk_medialive.types.__string_min1_max255_pattern_s.__stringMin1Max255PatternS",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        cloud_watch_alarm_template_group_identifiers: Optional[
            "aws_sdk_medialive.types.__list_of__string_pattern_s.__listOf__stringPatternS"
        ] = None,
        description: Optional[
            "aws_sdk_medialive.types.__string_min0_max1024.__stringMin0Max1024"
        ] = None,
        event_bridge_rule_template_group_identifiers: Optional[
            "aws_sdk_medialive.types.__list_of__string_pattern_s.__listOf__stringPatternS"
        ] = None,
        tags: Optional["aws_sdk_medialive.types.tag_map.TagMap"] = None,
        request_id: Optional[
            "aws_sdk_medialive.types.__string_min1_max256_pattern_s.__stringMin1Max256PatternS"
        ] = None,
    ) -> "aws_sdk_medialive.types.create_signal_map_response.CreateSignalMapResponse":
        """Initiates the creation of a new signal map. Will discover a new mediaResourceMap based on the provided discoveryEntryPointArn.

        Args:
            description: A resource's optional description.
            discovery_entry_point_arn: A top-level supported AWS resource ARN to discovery a signal map from.
            name: A resource's name. Names must be unique within the scope of a resource type in a specific region.
            request_id: An ID that you assign to a create request. This ID ensures idempotency when creating resources.

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.create_signal_map_request.CreateSignalMapRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.create_signal_map_response.CreateSignalMapResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.create_signal_map

            output, http_response = (
                aws_sdk_medialive._operations.media_live.create_signal_map.create_signal_map(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.create_signal_map_request.CreateSignalMapRequest = {}  # type: ignore[typeddict-item]
        if cloud_watch_alarm_template_group_identifiers is not None:
            input_["cloud_watch_alarm_template_group_identifiers"] = (
                cloud_watch_alarm_template_group_identifiers
            )
        if description is not None:
            input_["description"] = description
        input_["discovery_entry_point_arn"] = discovery_entry_point_arn
        if event_bridge_rule_template_group_identifiers is not None:
            input_["event_bridge_rule_template_group_identifiers"] = (
                event_bridge_rule_template_group_identifiers
            )
        input_["name"] = name
        if tags is not None:
            input_["tags"] = tags
        if request_id is not None:
            input_["request_id"] = request_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_tags(
        self,
        resource_arn: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        tags: Optional["aws_sdk_medialive.types.tags.Tags"] = None,
    ) -> None:
        """Create tags for a resource

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.create_tags_request.CreateTagsRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_medialive._operations.media_live.create_tags

            output, http_response = (
                aws_sdk_medialive._operations.media_live.create_tags.create_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.create_tags_request.CreateTagsRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_channel(
        self,
        channel_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.delete_channel_response.DeleteChannelResponse":
        """Starts deletion of channel. The associated outputs are also deleted.

        Args:
            channel_id: Unique ID of the channel.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.delete_channel_request.DeleteChannelRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.delete_channel_response.DeleteChannelResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.delete_channel

            output, http_response = (
                aws_sdk_medialive._operations.media_live.delete_channel.delete_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.delete_channel_request.DeleteChannelRequest = {}  # type: ignore[typeddict-item]
        input_["channel_id"] = channel_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_channel_placement_group(
        self,
        channel_placement_group_id: "aws_sdk_medialive.types.__string.__string",
        cluster_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.delete_channel_placement_group_response.DeleteChannelPlacementGroupResponse":
        """Delete the specified ChannelPlacementGroup that exists in the specified Cluster.

        Args:
            channel_placement_group_id: The ID of the channel placement group.
            cluster_id: The ID of the cluster.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.delete_channel_placement_group_request.DeleteChannelPlacementGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.delete_channel_placement_group_response.DeleteChannelPlacementGroupResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.delete_channel_placement_group

            output, http_response = (
                aws_sdk_medialive._operations.media_live.delete_channel_placement_group.delete_channel_placement_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.delete_channel_placement_group_request.DeleteChannelPlacementGroupRequest = {}  # type: ignore[typeddict-item]
        input_["channel_placement_group_id"] = channel_placement_group_id
        input_["cluster_id"] = cluster_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_cloud_watch_alarm_template(
        self,
        identifier: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> None:
        """Deletes a cloudwatch alarm template.

        Args:
            identifier: A cloudwatch alarm template's identifier. Can be either be its id or current name.

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.delete_cloud_watch_alarm_template_request.DeleteCloudWatchAlarmTemplateRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_medialive._operations.media_live.delete_cloud_watch_alarm_template

            output, http_response = (
                aws_sdk_medialive._operations.media_live.delete_cloud_watch_alarm_template.delete_cloud_watch_alarm_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.delete_cloud_watch_alarm_template_request.DeleteCloudWatchAlarmTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_cloud_watch_alarm_template_group(
        self,
        identifier: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> None:
        """Deletes a cloudwatch alarm template group. You must detach this group from all signal maps and ensure its existing templates are moved to another group or deleted.

        Args:
            identifier: A cloudwatch alarm template group's identifier. Can be either be its id or current name.

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.delete_cloud_watch_alarm_template_group_request.DeleteCloudWatchAlarmTemplateGroupRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_medialive._operations.media_live.delete_cloud_watch_alarm_template_group

            output, http_response = (
                aws_sdk_medialive._operations.media_live.delete_cloud_watch_alarm_template_group.delete_cloud_watch_alarm_template_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.delete_cloud_watch_alarm_template_group_request.DeleteCloudWatchAlarmTemplateGroupRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_cluster(
        self,
        cluster_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.delete_cluster_response.DeleteClusterResponse":
        """Delete a Cluster. The Cluster must be idle.

        Args:
            cluster_id: The ID of the cluster.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.delete_cluster_request.DeleteClusterRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.delete_cluster_response.DeleteClusterResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.delete_cluster

            output, http_response = (
                aws_sdk_medialive._operations.media_live.delete_cluster.delete_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.delete_cluster_request.DeleteClusterRequest = {}  # type: ignore[typeddict-item]
        input_["cluster_id"] = cluster_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_event_bridge_rule_template(
        self,
        identifier: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> None:
        """Deletes an eventbridge rule template.

        Args:
            identifier: An eventbridge rule template's identifier. Can be either be its id or current name.

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.delete_event_bridge_rule_template_request.DeleteEventBridgeRuleTemplateRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_medialive._operations.media_live.delete_event_bridge_rule_template

            output, http_response = (
                aws_sdk_medialive._operations.media_live.delete_event_bridge_rule_template.delete_event_bridge_rule_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.delete_event_bridge_rule_template_request.DeleteEventBridgeRuleTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_event_bridge_rule_template_group(
        self,
        identifier: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> None:
        """Deletes an eventbridge rule template group. You must detach this group from all signal maps and ensure its existing templates are moved to another group or deleted.

        Args:
            identifier: An eventbridge rule template group's identifier. Can be either be its id or current name.

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.delete_event_bridge_rule_template_group_request.DeleteEventBridgeRuleTemplateGroupRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_medialive._operations.media_live.delete_event_bridge_rule_template_group

            output, http_response = (
                aws_sdk_medialive._operations.media_live.delete_event_bridge_rule_template_group.delete_event_bridge_rule_template_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.delete_event_bridge_rule_template_group_request.DeleteEventBridgeRuleTemplateGroupRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_input(
        self,
        input_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.delete_input_response.DeleteInputResponse":
        """Deletes the input end point

        Args:
            input_id: Unique ID of the input

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.delete_input_request.DeleteInputRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.delete_input_response.DeleteInputResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.delete_input

            output, http_response = (
                aws_sdk_medialive._operations.media_live.delete_input.delete_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.delete_input_request.DeleteInputRequest = {}  # type: ignore[typeddict-item]
        input_["input_id"] = input_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_input_security_group(
        self,
        input_security_group_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.delete_input_security_group_response.DeleteInputSecurityGroupResponse":
        """Deletes an Input Security Group

        Args:
            input_security_group_id: The Input Security Group to delete

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.delete_input_security_group_request.DeleteInputSecurityGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.delete_input_security_group_response.DeleteInputSecurityGroupResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.delete_input_security_group

            output, http_response = (
                aws_sdk_medialive._operations.media_live.delete_input_security_group.delete_input_security_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.delete_input_security_group_request.DeleteInputSecurityGroupRequest = {}  # type: ignore[typeddict-item]
        input_["input_security_group_id"] = input_security_group_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_multiplex(
        self,
        multiplex_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.delete_multiplex_response.DeleteMultiplexResponse":
        """Delete a multiplex. The multiplex must be idle.

        Args:
            multiplex_id: The ID of the multiplex.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.delete_multiplex_request.DeleteMultiplexRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.delete_multiplex_response.DeleteMultiplexResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.delete_multiplex

            output, http_response = (
                aws_sdk_medialive._operations.media_live.delete_multiplex.delete_multiplex(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.delete_multiplex_request.DeleteMultiplexRequest = {}  # type: ignore[typeddict-item]
        input_["multiplex_id"] = multiplex_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_multiplex_program(
        self,
        multiplex_id: "aws_sdk_medialive.types.__string.__string",
        program_name: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.delete_multiplex_program_response.DeleteMultiplexProgramResponse":
        """Delete a program from a multiplex.

        Args:
            multiplex_id: The ID of the multiplex that the program belongs to.
            program_name: The multiplex program name.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.delete_multiplex_program_request.DeleteMultiplexProgramRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.delete_multiplex_program_response.DeleteMultiplexProgramResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.delete_multiplex_program

            output, http_response = (
                aws_sdk_medialive._operations.media_live.delete_multiplex_program.delete_multiplex_program(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.delete_multiplex_program_request.DeleteMultiplexProgramRequest = {}  # type: ignore[typeddict-item]
        input_["multiplex_id"] = multiplex_id
        input_["program_name"] = program_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_network(
        self,
        network_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.delete_network_response.DeleteNetworkResponse":
        """Delete a Network. The Network must have no resources associated with it.

        Args:
            network_id: The ID of the network.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.delete_network_request.DeleteNetworkRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.delete_network_response.DeleteNetworkResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.delete_network

            output, http_response = (
                aws_sdk_medialive._operations.media_live.delete_network.delete_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.delete_network_request.DeleteNetworkRequest = {}  # type: ignore[typeddict-item]
        input_["network_id"] = network_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_node(
        self,
        cluster_id: "aws_sdk_medialive.types.__string.__string",
        node_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.delete_node_response.DeleteNodeResponse":
        """Delete a Node. The Node must be IDLE.

        Args:
            cluster_id: The ID of the cluster
            node_id: The ID of the node.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.delete_node_request.DeleteNodeRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.delete_node_response.DeleteNodeResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.delete_node

            output, http_response = (
                aws_sdk_medialive._operations.media_live.delete_node.delete_node(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.delete_node_request.DeleteNodeRequest = {}  # type: ignore[typeddict-item]
        input_["cluster_id"] = cluster_id
        input_["node_id"] = node_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_reservation(
        self,
        reservation_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> (
        "aws_sdk_medialive.types.delete_reservation_response.DeleteReservationResponse"
    ):
        """Delete an expired reservation.

        Args:
            reservation_id: Unique reservation ID, e.g. '1234567'

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.delete_reservation_request.DeleteReservationRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.delete_reservation_response.DeleteReservationResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.delete_reservation

            output, http_response = (
                aws_sdk_medialive._operations.media_live.delete_reservation.delete_reservation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.delete_reservation_request.DeleteReservationRequest = {}  # type: ignore[typeddict-item]
        input_["reservation_id"] = reservation_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_schedule(
        self,
        channel_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.delete_schedule_response.DeleteScheduleResponse":
        """Delete all schedule actions on a channel.

        Args:
            channel_id: Id of the channel whose schedule is being deleted.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.delete_schedule_request.DeleteScheduleRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.delete_schedule_response.DeleteScheduleResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.delete_schedule

            output, http_response = (
                aws_sdk_medialive._operations.media_live.delete_schedule.delete_schedule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.delete_schedule_request.DeleteScheduleRequest = {}  # type: ignore[typeddict-item]
        input_["channel_id"] = channel_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_sdi_source(
        self,
        sdi_source_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.delete_sdi_source_response.DeleteSdiSourceResponse":
        """Delete an SdiSource. The SdiSource must not be part of any SidSourceMapping and must not be attached to any input.

        Args:
            sdi_source_id: The ID of the SdiSource.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.delete_sdi_source_request.DeleteSdiSourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.delete_sdi_source_response.DeleteSdiSourceResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.delete_sdi_source

            output, http_response = (
                aws_sdk_medialive._operations.media_live.delete_sdi_source.delete_sdi_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.delete_sdi_source_request.DeleteSdiSourceRequest = {}  # type: ignore[typeddict-item]
        input_["sdi_source_id"] = sdi_source_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_signal_map(
        self,
        identifier: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> None:
        """Deletes the specified signal map.

        Args:
            identifier: A signal map's identifier. Can be either be its id or current name.

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.delete_signal_map_request.DeleteSignalMapRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_medialive._operations.media_live.delete_signal_map

            output, http_response = (
                aws_sdk_medialive._operations.media_live.delete_signal_map.delete_signal_map(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.delete_signal_map_request.DeleteSignalMapRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_tags(
        self,
        resource_arn: "aws_sdk_medialive.types.__string.__string",
        tag_keys: "aws_sdk_medialive.types.__list_of__string.__listOf__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> None:
        """Removes tags for a resource

        Args:
            tag_keys: An array of tag keys to delete

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.delete_tags_request.DeleteTagsRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_medialive._operations.media_live.delete_tags

            output, http_response = (
                aws_sdk_medialive._operations.media_live.delete_tags.delete_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.delete_tags_request.DeleteTagsRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_account_configuration(
        self, *, config_overrides: Optional[MediaLiveClientConfig] = None
    ) -> "aws_sdk_medialive.types.describe_account_configuration_response.DescribeAccountConfigurationResponse":
        """Describe account configuration

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.describe_account_configuration_request.DescribeAccountConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.describe_account_configuration_response.DescribeAccountConfigurationResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.describe_account_configuration

            output, http_response = (
                aws_sdk_medialive._operations.media_live.describe_account_configuration.describe_account_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.describe_account_configuration_request.DescribeAccountConfigurationRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_channel(
        self,
        channel_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.describe_channel_response.DescribeChannelResponse":
        """Gets details about a channel

        Args:
            channel_id: channel ID

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.describe_channel_request.DescribeChannelRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.describe_channel_response.DescribeChannelResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.describe_channel

            output, http_response = (
                aws_sdk_medialive._operations.media_live.describe_channel.describe_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.describe_channel_request.DescribeChannelRequest = {}  # type: ignore[typeddict-item]
        input_["channel_id"] = channel_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_channel_placement_group(
        self,
        channel_placement_group_id: "aws_sdk_medialive.types.__string.__string",
        cluster_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.describe_channel_placement_group_response.DescribeChannelPlacementGroupResponse":
        """Get details about a ChannelPlacementGroup.

        Args:
            channel_placement_group_id: The ID of the channel placement group.
            cluster_id: The ID of the cluster.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.describe_channel_placement_group_request.DescribeChannelPlacementGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.describe_channel_placement_group_response.DescribeChannelPlacementGroupResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.describe_channel_placement_group

            output, http_response = (
                aws_sdk_medialive._operations.media_live.describe_channel_placement_group.describe_channel_placement_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.describe_channel_placement_group_request.DescribeChannelPlacementGroupRequest = {}  # type: ignore[typeddict-item]
        input_["channel_placement_group_id"] = channel_placement_group_id
        input_["cluster_id"] = cluster_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_cluster(
        self,
        cluster_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.describe_cluster_response.DescribeClusterResponse":
        """Get details about a Cluster.

        Args:
            cluster_id: The ID of the cluster.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.describe_cluster_request.DescribeClusterRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.describe_cluster_response.DescribeClusterResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.describe_cluster

            output, http_response = (
                aws_sdk_medialive._operations.media_live.describe_cluster.describe_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.describe_cluster_request.DescribeClusterRequest = {}  # type: ignore[typeddict-item]
        input_["cluster_id"] = cluster_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_input(
        self,
        input_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.describe_input_response.DescribeInputResponse":
        """Produces details about an input

        Args:
            input_id: Unique ID of the input

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.describe_input_request.DescribeInputRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.describe_input_response.DescribeInputResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.describe_input

            output, http_response = (
                aws_sdk_medialive._operations.media_live.describe_input.describe_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.describe_input_request.DescribeInputRequest = {}  # type: ignore[typeddict-item]
        input_["input_id"] = input_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_input_device(
        self,
        input_device_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.describe_input_device_response.DescribeInputDeviceResponse":
        """Gets the details for the input device

        Args:
            input_device_id: The unique ID of this input device. For example, hd-123456789abcdef.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.describe_input_device_request.DescribeInputDeviceRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.describe_input_device_response.DescribeInputDeviceResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.describe_input_device

            output, http_response = (
                aws_sdk_medialive._operations.media_live.describe_input_device.describe_input_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.describe_input_device_request.DescribeInputDeviceRequest = {}  # type: ignore[typeddict-item]
        input_["input_device_id"] = input_device_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    @contextmanager
    def describe_input_device_thumbnail(
        self,
        input_device_id: "aws_sdk_medialive.types.__string.__string",
        accept: "aws_sdk_medialive.types.accept_header.AcceptHeader",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "Generator[aws_sdk_medialive.types.describe_input_device_thumbnail_response.DescribeInputDeviceThumbnailResponse]":
        """Get the latest thumbnail data for the input device.

        Args:
            input_device_id: The unique ID of this input device. For example, hd-123456789abcdef.
            accept: The HTTP Accept header. Indicates the requested type for the thumbnail.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.describe_input_device_thumbnail_request.DescribeInputDeviceThumbnailRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.describe_input_device_thumbnail_response.DescribeInputDeviceThumbnailResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.describe_input_device_thumbnail

            output, http_response = (
                aws_sdk_medialive._operations.media_live.describe_input_device_thumbnail.describe_input_device_thumbnail(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.describe_input_device_thumbnail_request.DescribeInputDeviceThumbnailRequest = {}  # type: ignore[typeddict-item]
        input_["input_device_id"] = input_device_id
        input_["accept"] = accept

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        yield response.output

    def describe_input_security_group(
        self,
        input_security_group_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.describe_input_security_group_response.DescribeInputSecurityGroupResponse":
        """Produces a summary of an Input Security Group

        Args:
            input_security_group_id: The id of the Input Security Group to describe

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.describe_input_security_group_request.DescribeInputSecurityGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.describe_input_security_group_response.DescribeInputSecurityGroupResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.describe_input_security_group

            output, http_response = (
                aws_sdk_medialive._operations.media_live.describe_input_security_group.describe_input_security_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.describe_input_security_group_request.DescribeInputSecurityGroupRequest = {}  # type: ignore[typeddict-item]
        input_["input_security_group_id"] = input_security_group_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_multiplex(
        self,
        multiplex_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> (
        "aws_sdk_medialive.types.describe_multiplex_response.DescribeMultiplexResponse"
    ):
        """Gets details about a multiplex.

        Args:
            multiplex_id: The ID of the multiplex.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.describe_multiplex_request.DescribeMultiplexRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.describe_multiplex_response.DescribeMultiplexResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.describe_multiplex

            output, http_response = (
                aws_sdk_medialive._operations.media_live.describe_multiplex.describe_multiplex(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.describe_multiplex_request.DescribeMultiplexRequest = {}  # type: ignore[typeddict-item]
        input_["multiplex_id"] = multiplex_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_multiplex_program(
        self,
        multiplex_id: "aws_sdk_medialive.types.__string.__string",
        program_name: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.describe_multiplex_program_response.DescribeMultiplexProgramResponse":
        """Get the details for a program in a multiplex.

        Args:
            multiplex_id: The ID of the multiplex that the program belongs to.
            program_name: The name of the program.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.describe_multiplex_program_request.DescribeMultiplexProgramRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.describe_multiplex_program_response.DescribeMultiplexProgramResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.describe_multiplex_program

            output, http_response = (
                aws_sdk_medialive._operations.media_live.describe_multiplex_program.describe_multiplex_program(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.describe_multiplex_program_request.DescribeMultiplexProgramRequest = {}  # type: ignore[typeddict-item]
        input_["multiplex_id"] = multiplex_id
        input_["program_name"] = program_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_network(
        self,
        network_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.describe_network_response.DescribeNetworkResponse":
        """Get details about a Network.

        Args:
            network_id: The ID of the network.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.describe_network_request.DescribeNetworkRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.describe_network_response.DescribeNetworkResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.describe_network

            output, http_response = (
                aws_sdk_medialive._operations.media_live.describe_network.describe_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.describe_network_request.DescribeNetworkRequest = {}  # type: ignore[typeddict-item]
        input_["network_id"] = network_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_node(
        self,
        cluster_id: "aws_sdk_medialive.types.__string.__string",
        node_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.describe_node_response.DescribeNodeResponse":
        """Get details about a Node in the specified Cluster.

        Args:
            cluster_id: The ID of the cluster
            node_id: The ID of the node.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.describe_node_request.DescribeNodeRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.describe_node_response.DescribeNodeResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.describe_node

            output, http_response = (
                aws_sdk_medialive._operations.media_live.describe_node.describe_node(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.describe_node_request.DescribeNodeRequest = {}  # type: ignore[typeddict-item]
        input_["cluster_id"] = cluster_id
        input_["node_id"] = node_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_offering(
        self,
        offering_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.describe_offering_response.DescribeOfferingResponse":
        """Get details for an offering.

        Args:
            offering_id: Unique offering ID, e.g. '87654321'

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.describe_offering_request.DescribeOfferingRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.describe_offering_response.DescribeOfferingResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.describe_offering

            output, http_response = (
                aws_sdk_medialive._operations.media_live.describe_offering.describe_offering(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.describe_offering_request.DescribeOfferingRequest = {}  # type: ignore[typeddict-item]
        input_["offering_id"] = offering_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_reservation(
        self,
        reservation_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.describe_reservation_response.DescribeReservationResponse":
        """Get details for a reservation.

        Args:
            reservation_id: Unique reservation ID, e.g. '1234567'

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.describe_reservation_request.DescribeReservationRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.describe_reservation_response.DescribeReservationResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.describe_reservation

            output, http_response = (
                aws_sdk_medialive._operations.media_live.describe_reservation.describe_reservation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.describe_reservation_request.DescribeReservationRequest = {}  # type: ignore[typeddict-item]
        input_["reservation_id"] = reservation_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_schedule(
        self,
        channel_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "aws_sdk_medialive.types.describe_schedule_response.DescribeScheduleResponse":
        """Get a channel schedule

        Args:
            channel_id: Id of the channel whose schedule is being updated.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.describe_schedule_request.DescribeScheduleRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.describe_schedule_response.DescribeScheduleResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.describe_schedule

            output, http_response = (
                aws_sdk_medialive._operations.media_live.describe_schedule.describe_schedule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.describe_schedule_request.DescribeScheduleRequest = {}  # type: ignore[typeddict-item]
        input_["channel_id"] = channel_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_describe_schedule(
        self,
        channel_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "Iterator[aws_sdk_medialive.types.schedule_action.ScheduleAction]":
        _token = next_token
        while True:
            _response = self.describe_schedule(
                channel_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("schedule_actions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_sdi_source(
        self,
        sdi_source_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> (
        "aws_sdk_medialive.types.describe_sdi_source_response.DescribeSdiSourceResponse"
    ):
        """Gets details about a SdiSource.

        Args:
            sdi_source_id: Get details about an SdiSource.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.describe_sdi_source_request.DescribeSdiSourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.describe_sdi_source_response.DescribeSdiSourceResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.describe_sdi_source

            output, http_response = (
                aws_sdk_medialive._operations.media_live.describe_sdi_source.describe_sdi_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.describe_sdi_source_request.DescribeSdiSourceRequest = {}  # type: ignore[typeddict-item]
        input_["sdi_source_id"] = sdi_source_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_thumbnails(
        self,
        channel_id: "aws_sdk_medialive.types.__string.__string",
        pipeline_id: "aws_sdk_medialive.types.__string.__string",
        thumbnail_type: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.describe_thumbnails_response.DescribeThumbnailsResponse":
        r"""Describe the latest thumbnails data.

        Args:
            channel_id: Unique ID of the channel
            pipeline_id: Pipeline ID (\"0\" or \"1\")
            thumbnail_type: thumbnail type

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.describe_thumbnails_request.DescribeThumbnailsRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.describe_thumbnails_response.DescribeThumbnailsResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.describe_thumbnails

            output, http_response = (
                aws_sdk_medialive._operations.media_live.describe_thumbnails.describe_thumbnails(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.describe_thumbnails_request.DescribeThumbnailsRequest = {}  # type: ignore[typeddict-item]
        input_["channel_id"] = channel_id
        input_["pipeline_id"] = pipeline_id
        input_["thumbnail_type"] = thumbnail_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_cloud_watch_alarm_template(
        self,
        identifier: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.get_cloud_watch_alarm_template_response.GetCloudWatchAlarmTemplateResponse":
        """Retrieves the specified cloudwatch alarm template.

        Args:
            identifier: A cloudwatch alarm template's identifier. Can be either be its id or current name.

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.get_cloud_watch_alarm_template_request.GetCloudWatchAlarmTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.get_cloud_watch_alarm_template_response.GetCloudWatchAlarmTemplateResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.get_cloud_watch_alarm_template

            output, http_response = (
                aws_sdk_medialive._operations.media_live.get_cloud_watch_alarm_template.get_cloud_watch_alarm_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.get_cloud_watch_alarm_template_request.GetCloudWatchAlarmTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_cloud_watch_alarm_template_group(
        self,
        identifier: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.get_cloud_watch_alarm_template_group_response.GetCloudWatchAlarmTemplateGroupResponse":
        """Retrieves the specified cloudwatch alarm template group.

        Args:
            identifier: A cloudwatch alarm template group's identifier. Can be either be its id or current name.

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.get_cloud_watch_alarm_template_group_request.GetCloudWatchAlarmTemplateGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.get_cloud_watch_alarm_template_group_response.GetCloudWatchAlarmTemplateGroupResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.get_cloud_watch_alarm_template_group

            output, http_response = (
                aws_sdk_medialive._operations.media_live.get_cloud_watch_alarm_template_group.get_cloud_watch_alarm_template_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.get_cloud_watch_alarm_template_group_request.GetCloudWatchAlarmTemplateGroupRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_event_bridge_rule_template(
        self,
        identifier: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.get_event_bridge_rule_template_response.GetEventBridgeRuleTemplateResponse":
        """Retrieves the specified eventbridge rule template.

        Args:
            identifier: An eventbridge rule template's identifier. Can be either be its id or current name.

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.get_event_bridge_rule_template_request.GetEventBridgeRuleTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.get_event_bridge_rule_template_response.GetEventBridgeRuleTemplateResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.get_event_bridge_rule_template

            output, http_response = (
                aws_sdk_medialive._operations.media_live.get_event_bridge_rule_template.get_event_bridge_rule_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.get_event_bridge_rule_template_request.GetEventBridgeRuleTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_event_bridge_rule_template_group(
        self,
        identifier: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.get_event_bridge_rule_template_group_response.GetEventBridgeRuleTemplateGroupResponse":
        """Retrieves the specified eventbridge rule template group.

        Args:
            identifier: An eventbridge rule template group's identifier. Can be either be its id or current name.

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.get_event_bridge_rule_template_group_request.GetEventBridgeRuleTemplateGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.get_event_bridge_rule_template_group_response.GetEventBridgeRuleTemplateGroupResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.get_event_bridge_rule_template_group

            output, http_response = (
                aws_sdk_medialive._operations.media_live.get_event_bridge_rule_template_group.get_event_bridge_rule_template_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.get_event_bridge_rule_template_group_request.GetEventBridgeRuleTemplateGroupRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_signal_map(
        self,
        identifier: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.get_signal_map_response.GetSignalMapResponse":
        """Retrieves the specified signal map.

        Args:
            identifier: A signal map's identifier. Can be either be its id or current name.

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.get_signal_map_request.GetSignalMapRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.get_signal_map_response.GetSignalMapResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.get_signal_map

            output, http_response = (
                aws_sdk_medialive._operations.media_live.get_signal_map.get_signal_map(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.get_signal_map_request.GetSignalMapRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_alerts(
        self,
        channel_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        state_filter: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "aws_sdk_medialive.types.list_alerts_response.ListAlertsResponse":
        """List the alerts for a channel with optional filtering based on alert state.

        Args:
            channel_id: The unique ID of the channel
            max_results: The maximum number of items to return
            next_token: The next pagination token
            state_filter: Specifies the set of alerts to return based on their state. SET - Return only alerts with SET state. CLEARED - Return only alerts with CLEARED state. ALL - Return all alerts.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.list_alerts_request.ListAlertsRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.list_alerts_response.ListAlertsResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.list_alerts

            output, http_response = (
                aws_sdk_medialive._operations.media_live.list_alerts.list_alerts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.list_alerts_request.ListAlertsRequest = {}  # type: ignore[typeddict-item]
        input_["channel_id"] = channel_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if state_filter is not None:
            input_["state_filter"] = state_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_alerts(
        self,
        channel_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        state_filter: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "Iterator[aws_sdk_medialive.types.channel_alert.ChannelAlert]":
        _token = next_token
        while True:
            _response = self.list_alerts(
                channel_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                state_filter=state_filter,
            )
            _page = _resolve_path(_response, ("alerts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_channel_placement_groups(
        self,
        cluster_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "aws_sdk_medialive.types.list_channel_placement_groups_response.ListChannelPlacementGroupsResponse":
        """Retrieve the list of ChannelPlacementGroups in the specified Cluster.

        Args:
            cluster_id: The ID of the cluster
            max_results: The maximum number of items to return.
            next_token: The token to retrieve the next page of results.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.list_channel_placement_groups_request.ListChannelPlacementGroupsRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.list_channel_placement_groups_response.ListChannelPlacementGroupsResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.list_channel_placement_groups

            output, http_response = (
                aws_sdk_medialive._operations.media_live.list_channel_placement_groups.list_channel_placement_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.list_channel_placement_groups_request.ListChannelPlacementGroupsRequest = {}  # type: ignore[typeddict-item]
        input_["cluster_id"] = cluster_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_channel_placement_groups(
        self,
        cluster_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "Iterator[aws_sdk_medialive.types.describe_channel_placement_group_summary.DescribeChannelPlacementGroupSummary]":
        _token = next_token
        while True:
            _response = self.list_channel_placement_groups(
                cluster_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("channel_placement_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_channels(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "aws_sdk_medialive.types.list_channels_response.ListChannelsResponse":
        """Produces list of channels that have been created

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.list_channels_request.ListChannelsRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.list_channels_response.ListChannelsResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.list_channels

            output, http_response = (
                aws_sdk_medialive._operations.media_live.list_channels.list_channels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.list_channels_request.ListChannelsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_channels(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "Iterator[aws_sdk_medialive.types.channel_summary.ChannelSummary]":
        _token = next_token
        while True:
            _response = self.list_channels(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("channels",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_cloud_watch_alarm_template_groups(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        scope: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        signal_map_identifier: Optional[
            "aws_sdk_medialive.types.__string.__string"
        ] = None,
    ) -> "aws_sdk_medialive.types.list_cloud_watch_alarm_template_groups_response.ListCloudWatchAlarmTemplateGroupsResponse":
        """Lists cloudwatch alarm template groups.

        Args:
            next_token: A token used to retrieve the next set of results in paginated list responses.
            scope: Represents the scope of a resource, with options for all scopes, AWS provided resources, or local resources.
            signal_map_identifier: A signal map's identifier. Can be either be its id or current name.

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.list_cloud_watch_alarm_template_groups_request.ListCloudWatchAlarmTemplateGroupsRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.list_cloud_watch_alarm_template_groups_response.ListCloudWatchAlarmTemplateGroupsResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.list_cloud_watch_alarm_template_groups

            output, http_response = (
                aws_sdk_medialive._operations.media_live.list_cloud_watch_alarm_template_groups.list_cloud_watch_alarm_template_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.list_cloud_watch_alarm_template_groups_request.ListCloudWatchAlarmTemplateGroupsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if scope is not None:
            input_["scope"] = scope
        if signal_map_identifier is not None:
            input_["signal_map_identifier"] = signal_map_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_cloud_watch_alarm_template_groups(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        scope: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        signal_map_identifier: Optional[
            "aws_sdk_medialive.types.__string.__string"
        ] = None,
    ) -> "Iterator[aws_sdk_medialive.types.cloud_watch_alarm_template_group_summary.CloudWatchAlarmTemplateGroupSummary]":
        _token = next_token
        while True:
            _response = self.list_cloud_watch_alarm_template_groups(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                scope=scope,
                signal_map_identifier=signal_map_identifier,
            )
            _page = _resolve_path(_response, ("cloud_watch_alarm_template_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_cloud_watch_alarm_templates(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        group_identifier: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        scope: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        signal_map_identifier: Optional[
            "aws_sdk_medialive.types.__string.__string"
        ] = None,
    ) -> "aws_sdk_medialive.types.list_cloud_watch_alarm_templates_response.ListCloudWatchAlarmTemplatesResponse":
        """Lists cloudwatch alarm templates.

        Args:
            group_identifier: A cloudwatch alarm template group's identifier. Can be either be its id or current name.
            next_token: A token used to retrieve the next set of results in paginated list responses.
            scope: Represents the scope of a resource, with options for all scopes, AWS provided resources, or local resources.
            signal_map_identifier: A signal map's identifier. Can be either be its id or current name.

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.list_cloud_watch_alarm_templates_request.ListCloudWatchAlarmTemplatesRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.list_cloud_watch_alarm_templates_response.ListCloudWatchAlarmTemplatesResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.list_cloud_watch_alarm_templates

            output, http_response = (
                aws_sdk_medialive._operations.media_live.list_cloud_watch_alarm_templates.list_cloud_watch_alarm_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.list_cloud_watch_alarm_templates_request.ListCloudWatchAlarmTemplatesRequest = {}  # type: ignore[typeddict-item]
        if group_identifier is not None:
            input_["group_identifier"] = group_identifier
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if scope is not None:
            input_["scope"] = scope
        if signal_map_identifier is not None:
            input_["signal_map_identifier"] = signal_map_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_cloud_watch_alarm_templates(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        group_identifier: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        scope: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        signal_map_identifier: Optional[
            "aws_sdk_medialive.types.__string.__string"
        ] = None,
    ) -> "Iterator[aws_sdk_medialive.types.cloud_watch_alarm_template_summary.CloudWatchAlarmTemplateSummary]":
        _token = next_token
        while True:
            _response = self.list_cloud_watch_alarm_templates(
                config_overrides=config_overrides,
                group_identifier=group_identifier,
                max_results=max_results,
                next_token=_token,
                scope=scope,
                signal_map_identifier=signal_map_identifier,
            )
            _page = _resolve_path(_response, ("cloud_watch_alarm_templates",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_cluster_alerts(
        self,
        cluster_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        state_filter: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> (
        "aws_sdk_medialive.types.list_cluster_alerts_response.ListClusterAlertsResponse"
    ):
        """List the alerts for a cluster with optional filtering based on alert state.

        Args:
            cluster_id: The unique ID of the cluster
            max_results: The maximum number of items to return
            next_token: The next pagination token
            state_filter: Specifies the set of alerts to return based on their state. SET - Return only alerts with SET state. CLEARED - Return only alerts with CLEARED state. ALL - Return all alerts.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.list_cluster_alerts_request.ListClusterAlertsRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.list_cluster_alerts_response.ListClusterAlertsResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.list_cluster_alerts

            output, http_response = (
                aws_sdk_medialive._operations.media_live.list_cluster_alerts.list_cluster_alerts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.list_cluster_alerts_request.ListClusterAlertsRequest = {}  # type: ignore[typeddict-item]
        input_["cluster_id"] = cluster_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if state_filter is not None:
            input_["state_filter"] = state_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_cluster_alerts(
        self,
        cluster_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        state_filter: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "Iterator[aws_sdk_medialive.types.cluster_alert.ClusterAlert]":
        _token = next_token
        while True:
            _response = self.list_cluster_alerts(
                cluster_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                state_filter=state_filter,
            )
            _page = _resolve_path(_response, ("alerts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_clusters(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "aws_sdk_medialive.types.list_clusters_response.ListClustersResponse":
        """Retrieve the list of Clusters.

        Args:
            max_results: The maximum number of items to return.
            next_token: The token to retrieve the next page of results.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.list_clusters_request.ListClustersRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.list_clusters_response.ListClustersResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.list_clusters

            output, http_response = (
                aws_sdk_medialive._operations.media_live.list_clusters.list_clusters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.list_clusters_request.ListClustersRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_clusters(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "Iterator[aws_sdk_medialive.types.describe_cluster_summary.DescribeClusterSummary]":
        _token = next_token
        while True:
            _response = self.list_clusters(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("clusters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_event_bridge_rule_template_groups(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        signal_map_identifier: Optional[
            "aws_sdk_medialive.types.__string.__string"
        ] = None,
    ) -> "aws_sdk_medialive.types.list_event_bridge_rule_template_groups_response.ListEventBridgeRuleTemplateGroupsResponse":
        """Lists eventbridge rule template groups.

        Args:
            next_token: A token used to retrieve the next set of results in paginated list responses.
            signal_map_identifier: A signal map's identifier. Can be either be its id or current name.

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.list_event_bridge_rule_template_groups_request.ListEventBridgeRuleTemplateGroupsRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.list_event_bridge_rule_template_groups_response.ListEventBridgeRuleTemplateGroupsResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.list_event_bridge_rule_template_groups

            output, http_response = (
                aws_sdk_medialive._operations.media_live.list_event_bridge_rule_template_groups.list_event_bridge_rule_template_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.list_event_bridge_rule_template_groups_request.ListEventBridgeRuleTemplateGroupsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if signal_map_identifier is not None:
            input_["signal_map_identifier"] = signal_map_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_event_bridge_rule_template_groups(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        signal_map_identifier: Optional[
            "aws_sdk_medialive.types.__string.__string"
        ] = None,
    ) -> "Iterator[aws_sdk_medialive.types.event_bridge_rule_template_group_summary.EventBridgeRuleTemplateGroupSummary]":
        _token = next_token
        while True:
            _response = self.list_event_bridge_rule_template_groups(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                signal_map_identifier=signal_map_identifier,
            )
            _page = _resolve_path(_response, ("event_bridge_rule_template_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_event_bridge_rule_templates(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        group_identifier: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        signal_map_identifier: Optional[
            "aws_sdk_medialive.types.__string.__string"
        ] = None,
    ) -> "aws_sdk_medialive.types.list_event_bridge_rule_templates_response.ListEventBridgeRuleTemplatesResponse":
        """Lists eventbridge rule templates.

        Args:
            group_identifier: An eventbridge rule template group's identifier. Can be either be its id or current name.
            next_token: A token used to retrieve the next set of results in paginated list responses.
            signal_map_identifier: A signal map's identifier. Can be either be its id or current name.

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.list_event_bridge_rule_templates_request.ListEventBridgeRuleTemplatesRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.list_event_bridge_rule_templates_response.ListEventBridgeRuleTemplatesResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.list_event_bridge_rule_templates

            output, http_response = (
                aws_sdk_medialive._operations.media_live.list_event_bridge_rule_templates.list_event_bridge_rule_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.list_event_bridge_rule_templates_request.ListEventBridgeRuleTemplatesRequest = {}  # type: ignore[typeddict-item]
        if group_identifier is not None:
            input_["group_identifier"] = group_identifier
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if signal_map_identifier is not None:
            input_["signal_map_identifier"] = signal_map_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_event_bridge_rule_templates(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        group_identifier: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        signal_map_identifier: Optional[
            "aws_sdk_medialive.types.__string.__string"
        ] = None,
    ) -> "Iterator[aws_sdk_medialive.types.event_bridge_rule_template_summary.EventBridgeRuleTemplateSummary]":
        _token = next_token
        while True:
            _response = self.list_event_bridge_rule_templates(
                config_overrides=config_overrides,
                group_identifier=group_identifier,
                max_results=max_results,
                next_token=_token,
                signal_map_identifier=signal_map_identifier,
            )
            _page = _resolve_path(_response, ("event_bridge_rule_templates",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_input_devices(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "aws_sdk_medialive.types.list_input_devices_response.ListInputDevicesResponse":
        """List input devices

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.list_input_devices_request.ListInputDevicesRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.list_input_devices_response.ListInputDevicesResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.list_input_devices

            output, http_response = (
                aws_sdk_medialive._operations.media_live.list_input_devices.list_input_devices(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.list_input_devices_request.ListInputDevicesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_input_devices(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "Iterator[aws_sdk_medialive.types.input_device_summary.InputDeviceSummary]":
        _token = next_token
        while True:
            _response = self.list_input_devices(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("input_devices",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_input_device_transfers(
        self,
        transfer_type: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "aws_sdk_medialive.types.list_input_device_transfers_response.ListInputDeviceTransfersResponse":
        """List input devices that are currently being transferred. List input devices that you are transferring from your AWS account or input devices that another AWS account is transferring to you.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.list_input_device_transfers_request.ListInputDeviceTransfersRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.list_input_device_transfers_response.ListInputDeviceTransfersResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.list_input_device_transfers

            output, http_response = (
                aws_sdk_medialive._operations.media_live.list_input_device_transfers.list_input_device_transfers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.list_input_device_transfers_request.ListInputDeviceTransfersRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["transfer_type"] = transfer_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_input_device_transfers(
        self,
        transfer_type: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "Iterator[aws_sdk_medialive.types.transferring_input_device_summary.TransferringInputDeviceSummary]":
        _token = next_token
        while True:
            _response = self.list_input_device_transfers(
                transfer_type,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("input_device_transfers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_inputs(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "aws_sdk_medialive.types.list_inputs_response.ListInputsResponse":
        """Produces list of inputs that have been created

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.list_inputs_request.ListInputsRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.list_inputs_response.ListInputsResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.list_inputs

            output, http_response = (
                aws_sdk_medialive._operations.media_live.list_inputs.list_inputs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.list_inputs_request.ListInputsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_inputs(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "Iterator[aws_sdk_medialive.types.input.Input]":
        _token = next_token
        while True:
            _response = self.list_inputs(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("inputs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_input_security_groups(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "aws_sdk_medialive.types.list_input_security_groups_response.ListInputSecurityGroupsResponse":
        """Produces a list of Input Security Groups for an account

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.list_input_security_groups_request.ListInputSecurityGroupsRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.list_input_security_groups_response.ListInputSecurityGroupsResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.list_input_security_groups

            output, http_response = (
                aws_sdk_medialive._operations.media_live.list_input_security_groups.list_input_security_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.list_input_security_groups_request.ListInputSecurityGroupsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_input_security_groups(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "Iterator[aws_sdk_medialive.types.input_security_group.InputSecurityGroup]":
        _token = next_token
        while True:
            _response = self.list_input_security_groups(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("input_security_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_multiplex_alerts(
        self,
        multiplex_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        state_filter: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "aws_sdk_medialive.types.list_multiplex_alerts_response.ListMultiplexAlertsResponse":
        """List the alerts for a multiplex with optional filtering based on alert state.

        Args:
            max_results: The maximum number of items to return
            multiplex_id: The unique ID of the multiplex
            next_token: The next pagination token
            state_filter: Specifies the set of alerts to return based on their state. SET - Return only alerts with SET state. CLEARED - Return only alerts with CLEARED state. ALL - Return all alerts.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.list_multiplex_alerts_request.ListMultiplexAlertsRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.list_multiplex_alerts_response.ListMultiplexAlertsResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.list_multiplex_alerts

            output, http_response = (
                aws_sdk_medialive._operations.media_live.list_multiplex_alerts.list_multiplex_alerts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.list_multiplex_alerts_request.ListMultiplexAlertsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        input_["multiplex_id"] = multiplex_id
        if next_token is not None:
            input_["next_token"] = next_token
        if state_filter is not None:
            input_["state_filter"] = state_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_multiplex_alerts(
        self,
        multiplex_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        state_filter: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "Iterator[aws_sdk_medialive.types.multiplex_alert.MultiplexAlert]":
        _token = next_token
        while True:
            _response = self.list_multiplex_alerts(
                multiplex_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                state_filter=state_filter,
            )
            _page = _resolve_path(_response, ("alerts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_multiplexes(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "aws_sdk_medialive.types.list_multiplexes_response.ListMultiplexesResponse":
        """Retrieve a list of the existing multiplexes.

        Args:
            max_results: The maximum number of items to return.
            next_token: The token to retrieve the next page of results.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.list_multiplexes_request.ListMultiplexesRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.list_multiplexes_response.ListMultiplexesResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.list_multiplexes

            output, http_response = (
                aws_sdk_medialive._operations.media_live.list_multiplexes.list_multiplexes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.list_multiplexes_request.ListMultiplexesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_multiplexes(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "Iterator[aws_sdk_medialive.types.multiplex_summary.MultiplexSummary]":
        _token = next_token
        while True:
            _response = self.list_multiplexes(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("multiplexes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_multiplex_programs(
        self,
        multiplex_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "aws_sdk_medialive.types.list_multiplex_programs_response.ListMultiplexProgramsResponse":
        """List the programs that currently exist for a specific multiplex.

        Args:
            max_results: The maximum number of items to return.
            multiplex_id: The ID of the multiplex that the programs belong to.
            next_token: The token to retrieve the next page of results.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.list_multiplex_programs_request.ListMultiplexProgramsRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.list_multiplex_programs_response.ListMultiplexProgramsResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.list_multiplex_programs

            output, http_response = (
                aws_sdk_medialive._operations.media_live.list_multiplex_programs.list_multiplex_programs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.list_multiplex_programs_request.ListMultiplexProgramsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        input_["multiplex_id"] = multiplex_id
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_multiplex_programs(
        self,
        multiplex_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "Iterator[aws_sdk_medialive.types.multiplex_program_summary.MultiplexProgramSummary]":
        _token = next_token
        while True:
            _response = self.list_multiplex_programs(
                multiplex_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("multiplex_programs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_networks(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "aws_sdk_medialive.types.list_networks_response.ListNetworksResponse":
        """Retrieve the list of Networks.

        Args:
            max_results: The maximum number of items to return.
            next_token: The token to retrieve the next page of results.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.list_networks_request.ListNetworksRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.list_networks_response.ListNetworksResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.list_networks

            output, http_response = (
                aws_sdk_medialive._operations.media_live.list_networks.list_networks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.list_networks_request.ListNetworksRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_networks(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "Iterator[aws_sdk_medialive.types.describe_network_summary.DescribeNetworkSummary]":
        _token = next_token
        while True:
            _response = self.list_networks(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("networks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_nodes(
        self,
        cluster_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "aws_sdk_medialive.types.list_nodes_response.ListNodesResponse":
        """Retrieve the list of Nodes.

        Args:
            cluster_id: The ID of the cluster
            max_results: The maximum number of items to return.
            next_token: The token to retrieve the next page of results.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.list_nodes_request.ListNodesRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.list_nodes_response.ListNodesResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.list_nodes

            output, http_response = (
                aws_sdk_medialive._operations.media_live.list_nodes.list_nodes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.list_nodes_request.ListNodesRequest = {}  # type: ignore[typeddict-item]
        input_["cluster_id"] = cluster_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_nodes(
        self,
        cluster_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "Iterator[aws_sdk_medialive.types.describe_node_summary.DescribeNodeSummary]":
        _token = next_token
        while True:
            _response = self.list_nodes(
                cluster_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("nodes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_offerings(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        channel_class: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        channel_configuration: Optional[
            "aws_sdk_medialive.types.__string.__string"
        ] = None,
        codec: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        duration: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        maximum_bitrate: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        maximum_framerate: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        resolution: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        resource_type: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        special_feature: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        video_quality: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "aws_sdk_medialive.types.list_offerings_response.ListOfferingsResponse":
        """List offerings available for purchase.

        Args:
            channel_class: Filter by channel class, 'STANDARD' or 'SINGLE_PIPELINE'
            channel_configuration: Filter to offerings that match the configuration of an existing channel, e.g. '2345678' (a channel ID)
            codec: Filter by codec, 'AVC', 'HEVC', 'MPEG2', 'AUDIO', 'LINK', or 'AV1'
            duration: Filter by offering duration, e.g. '12'
            maximum_bitrate: Filter by bitrate, 'MAX_10_MBPS', 'MAX_20_MBPS', or 'MAX_50_MBPS'
            maximum_framerate: Filter by framerate, 'MAX_30_FPS' or 'MAX_60_FPS'
            resolution: Filter by resolution, 'SD', 'HD', 'FHD', or 'UHD'
            resource_type: Filter by resource type, 'INPUT', 'OUTPUT', 'MULTIPLEX', or 'CHANNEL'
            special_feature: Filter by special feature, 'ADVANCED_AUDIO' or 'AUDIO_NORMALIZATION'
            video_quality: Filter by video quality, 'STANDARD', 'ENHANCED', or 'PREMIUM'

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.list_offerings_request.ListOfferingsRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.list_offerings_response.ListOfferingsResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.list_offerings

            output, http_response = (
                aws_sdk_medialive._operations.media_live.list_offerings.list_offerings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.list_offerings_request.ListOfferingsRequest = {}  # type: ignore[typeddict-item]
        if channel_class is not None:
            input_["channel_class"] = channel_class
        if channel_configuration is not None:
            input_["channel_configuration"] = channel_configuration
        if codec is not None:
            input_["codec"] = codec
        if duration is not None:
            input_["duration"] = duration
        if max_results is not None:
            input_["max_results"] = max_results
        if maximum_bitrate is not None:
            input_["maximum_bitrate"] = maximum_bitrate
        if maximum_framerate is not None:
            input_["maximum_framerate"] = maximum_framerate
        if next_token is not None:
            input_["next_token"] = next_token
        if resolution is not None:
            input_["resolution"] = resolution
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if special_feature is not None:
            input_["special_feature"] = special_feature
        if video_quality is not None:
            input_["video_quality"] = video_quality

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_offerings(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        channel_class: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        channel_configuration: Optional[
            "aws_sdk_medialive.types.__string.__string"
        ] = None,
        codec: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        duration: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        maximum_bitrate: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        maximum_framerate: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        resolution: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        resource_type: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        special_feature: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        video_quality: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "Iterator[aws_sdk_medialive.types.offering.Offering]":
        _token = next_token
        while True:
            _response = self.list_offerings(
                config_overrides=config_overrides,
                channel_class=channel_class,
                channel_configuration=channel_configuration,
                codec=codec,
                duration=duration,
                max_results=max_results,
                maximum_bitrate=maximum_bitrate,
                maximum_framerate=maximum_framerate,
                next_token=_token,
                resolution=resolution,
                resource_type=resource_type,
                special_feature=special_feature,
                video_quality=video_quality,
            )
            _page = _resolve_path(_response, ("offerings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_reservations(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        channel_class: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        codec: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        maximum_bitrate: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        maximum_framerate: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        resolution: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        resource_type: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        special_feature: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        video_quality: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "aws_sdk_medialive.types.list_reservations_response.ListReservationsResponse":
        """List purchased reservations.

        Args:
            channel_class: Filter by channel class, 'STANDARD' or 'SINGLE_PIPELINE'
            codec: Filter by codec, 'AVC', 'HEVC', 'MPEG2', 'AUDIO', 'LINK', or 'AV1'
            maximum_bitrate: Filter by bitrate, 'MAX_10_MBPS', 'MAX_20_MBPS', or 'MAX_50_MBPS'
            maximum_framerate: Filter by framerate, 'MAX_30_FPS' or 'MAX_60_FPS'
            resolution: Filter by resolution, 'SD', 'HD', 'FHD', or 'UHD'
            resource_type: Filter by resource type, 'INPUT', 'OUTPUT', 'MULTIPLEX', or 'CHANNEL'
            special_feature: Filter by special feature, 'ADVANCED_AUDIO' or 'AUDIO_NORMALIZATION'
            video_quality: Filter by video quality, 'STANDARD', 'ENHANCED', or 'PREMIUM'

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.list_reservations_request.ListReservationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.list_reservations_response.ListReservationsResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.list_reservations

            output, http_response = (
                aws_sdk_medialive._operations.media_live.list_reservations.list_reservations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.list_reservations_request.ListReservationsRequest = {}  # type: ignore[typeddict-item]
        if channel_class is not None:
            input_["channel_class"] = channel_class
        if codec is not None:
            input_["codec"] = codec
        if max_results is not None:
            input_["max_results"] = max_results
        if maximum_bitrate is not None:
            input_["maximum_bitrate"] = maximum_bitrate
        if maximum_framerate is not None:
            input_["maximum_framerate"] = maximum_framerate
        if next_token is not None:
            input_["next_token"] = next_token
        if resolution is not None:
            input_["resolution"] = resolution
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if special_feature is not None:
            input_["special_feature"] = special_feature
        if video_quality is not None:
            input_["video_quality"] = video_quality

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_reservations(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        channel_class: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        codec: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        maximum_bitrate: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        maximum_framerate: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        resolution: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        resource_type: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        special_feature: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        video_quality: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "Iterator[aws_sdk_medialive.types.reservation.Reservation]":
        _token = next_token
        while True:
            _response = self.list_reservations(
                config_overrides=config_overrides,
                channel_class=channel_class,
                codec=codec,
                max_results=max_results,
                maximum_bitrate=maximum_bitrate,
                maximum_framerate=maximum_framerate,
                next_token=_token,
                resolution=resolution,
                resource_type=resource_type,
                special_feature=special_feature,
                video_quality=video_quality,
            )
            _page = _resolve_path(_response, ("reservations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_sdi_sources(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "aws_sdk_medialive.types.list_sdi_sources_response.ListSdiSourcesResponse":
        """List all the SdiSources in the AWS account.

        Args:
            max_results: The maximum number of items to return.
            next_token: The token to retrieve the next page of results.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.list_sdi_sources_request.ListSdiSourcesRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.list_sdi_sources_response.ListSdiSourcesResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.list_sdi_sources

            output, http_response = (
                aws_sdk_medialive._operations.media_live.list_sdi_sources.list_sdi_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.list_sdi_sources_request.ListSdiSourcesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_sdi_sources(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "Iterator[aws_sdk_medialive.types.sdi_source_summary.SdiSourceSummary]":
        _token = next_token
        while True:
            _response = self.list_sdi_sources(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("sdi_sources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_signal_maps(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        cloud_watch_alarm_template_group_identifier: Optional[
            "aws_sdk_medialive.types.__string.__string"
        ] = None,
        event_bridge_rule_template_group_identifier: Optional[
            "aws_sdk_medialive.types.__string.__string"
        ] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "aws_sdk_medialive.types.list_signal_maps_response.ListSignalMapsResponse":
        """Lists signal maps.

        Args:
            cloud_watch_alarm_template_group_identifier: A cloudwatch alarm template group's identifier. Can be either be its id or current name.
            event_bridge_rule_template_group_identifier: An eventbridge rule template group's identifier. Can be either be its id or current name.
            next_token: A token used to retrieve the next set of results in paginated list responses.

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.list_signal_maps_request.ListSignalMapsRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.list_signal_maps_response.ListSignalMapsResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.list_signal_maps

            output, http_response = (
                aws_sdk_medialive._operations.media_live.list_signal_maps.list_signal_maps(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.list_signal_maps_request.ListSignalMapsRequest = {}  # type: ignore[typeddict-item]
        if cloud_watch_alarm_template_group_identifier is not None:
            input_["cloud_watch_alarm_template_group_identifier"] = (
                cloud_watch_alarm_template_group_identifier
            )
        if event_bridge_rule_template_group_identifier is not None:
            input_["event_bridge_rule_template_group_identifier"] = (
                event_bridge_rule_template_group_identifier
            )
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_signal_maps(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        cloud_watch_alarm_template_group_identifier: Optional[
            "aws_sdk_medialive.types.__string.__string"
        ] = None,
        event_bridge_rule_template_group_identifier: Optional[
            "aws_sdk_medialive.types.__string.__string"
        ] = None,
        max_results: Optional["aws_sdk_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "Iterator[aws_sdk_medialive.types.signal_map_summary.SignalMapSummary]":
        _token = next_token
        while True:
            _response = self.list_signal_maps(
                config_overrides=config_overrides,
                cloud_watch_alarm_template_group_identifier=cloud_watch_alarm_template_group_identifier,
                event_bridge_rule_template_group_identifier=event_bridge_rule_template_group_identifier,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("signal_maps",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """Produces list of tags that have been created for a resource

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.list_tags_for_resource

            output, http_response = (
                aws_sdk_medialive._operations.media_live.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_versions(
        self, *, config_overrides: Optional[MediaLiveClientConfig] = None
    ) -> "aws_sdk_medialive.types.list_versions_response.ListVersionsResponse":
        """Retrieves an array of all the encoder engine versions that are available in this AWS account.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.list_versions_request.ListVersionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.list_versions_response.ListVersionsResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.list_versions

            output, http_response = (
                aws_sdk_medialive._operations.media_live.list_versions.list_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.list_versions_request.ListVersionsRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def purchase_offering(
        self,
        count: "aws_sdk_medialive.types.__integer_min1.__integerMin1",
        offering_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        name: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        renewal_settings: Optional[
            "aws_sdk_medialive.types.renewal_settings.RenewalSettings"
        ] = None,
        request_id: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        start: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        tags: Optional["aws_sdk_medialive.types.tags.Tags"] = None,
    ) -> "aws_sdk_medialive.types.purchase_offering_response.PurchaseOfferingResponse":
        """Purchase an offering and create a reservation.

        Args:
            count: Number of resources
            name: Name for the new reservation
            offering_id: Offering to purchase, e.g. '87654321'
            renewal_settings: Renewal settings for the reservation
            request_id: Unique request ID to be specified. This is needed to prevent retries from creating multiple resources.
            start: Requested reservation start time (UTC) in ISO-8601 format. The specified time must be between the first day of the current month and one year from now. If no value is given, the default is now.
            tags: A collection of key-value pairs

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.purchase_offering_request.PurchaseOfferingRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.purchase_offering_response.PurchaseOfferingResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.purchase_offering

            output, http_response = (
                aws_sdk_medialive._operations.media_live.purchase_offering.purchase_offering(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.purchase_offering_request.PurchaseOfferingRequest = {}  # type: ignore[typeddict-item]
        input_["count"] = count
        if name is not None:
            input_["name"] = name
        input_["offering_id"] = offering_id
        if renewal_settings is not None:
            input_["renewal_settings"] = renewal_settings
        if request_id is not None:
            input_["request_id"] = request_id
        if start is not None:
            input_["start"] = start
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def reboot_input_device(
        self,
        input_device_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        force: Optional[
            "aws_sdk_medialive.types.reboot_input_device_force.RebootInputDeviceForce"
        ] = None,
    ) -> (
        "aws_sdk_medialive.types.reboot_input_device_response.RebootInputDeviceResponse"
    ):
        """Send a reboot command to the specified input device. The device will begin rebooting within a few seconds of sending the command. When the reboot is complete, the device’s connection status will change to connected.

        Args:
            force: Force a reboot of an input device. If the device is streaming, it will stop streaming and begin rebooting within a few seconds of sending the command. If the device was streaming prior to the reboot, the device will resume streaming when the reboot completes.
            input_device_id: The unique ID of the input device to reboot. For example, hd-123456789abcdef.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.reboot_input_device_request.RebootInputDeviceRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.reboot_input_device_response.RebootInputDeviceResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.reboot_input_device

            output, http_response = (
                aws_sdk_medialive._operations.media_live.reboot_input_device.reboot_input_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.reboot_input_device_request.RebootInputDeviceRequest = {}  # type: ignore[typeddict-item]
        if force is not None:
            input_["force"] = force
        input_["input_device_id"] = input_device_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def reject_input_device_transfer(
        self,
        input_device_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.reject_input_device_transfer_response.RejectInputDeviceTransferResponse":
        """Reject the transfer of the specified input device to your AWS account.

        Args:
            input_device_id: The unique ID of the input device to reject. For example, hd-123456789abcdef.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.reject_input_device_transfer_request.RejectInputDeviceTransferRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.reject_input_device_transfer_response.RejectInputDeviceTransferResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.reject_input_device_transfer

            output, http_response = (
                aws_sdk_medialive._operations.media_live.reject_input_device_transfer.reject_input_device_transfer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.reject_input_device_transfer_request.RejectInputDeviceTransferRequest = {}  # type: ignore[typeddict-item]
        input_["input_device_id"] = input_device_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def restart_channel_pipelines(
        self,
        channel_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        pipeline_ids: Optional[
            "aws_sdk_medialive.types.__list_of_channel_pipeline_id_to_restart.__listOfChannelPipelineIdToRestart"
        ] = None,
    ) -> "aws_sdk_medialive.types.restart_channel_pipelines_response.RestartChannelPipelinesResponse":
        """Restart pipelines in one channel that is currently running.

        Args:
            channel_id: ID of channel
            pipeline_ids: An array of pipelines to restart in this channel. Format PIPELINE_0 or PIPELINE_1.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.restart_channel_pipelines_request.RestartChannelPipelinesRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.restart_channel_pipelines_response.RestartChannelPipelinesResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.restart_channel_pipelines

            output, http_response = (
                aws_sdk_medialive._operations.media_live.restart_channel_pipelines.restart_channel_pipelines(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.restart_channel_pipelines_request.RestartChannelPipelinesRequest = {}  # type: ignore[typeddict-item]
        input_["channel_id"] = channel_id
        if pipeline_ids is not None:
            input_["pipeline_ids"] = pipeline_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_channel(
        self,
        channel_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.start_channel_response.StartChannelResponse":
        """Starts an existing channel

        Args:
            channel_id: A request to start a channel

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.start_channel_request.StartChannelRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.start_channel_response.StartChannelResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.start_channel

            output, http_response = (
                aws_sdk_medialive._operations.media_live.start_channel.start_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.start_channel_request.StartChannelRequest = {}  # type: ignore[typeddict-item]
        input_["channel_id"] = channel_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_delete_monitor_deployment(
        self,
        identifier: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.start_delete_monitor_deployment_response.StartDeleteMonitorDeploymentResponse":
        """Initiates a deployment to delete the monitor of the specified signal map.

        Args:
            identifier: A signal map's identifier. Can be either be its id or current name.

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.start_delete_monitor_deployment_request.StartDeleteMonitorDeploymentRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.start_delete_monitor_deployment_response.StartDeleteMonitorDeploymentResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.start_delete_monitor_deployment

            output, http_response = (
                aws_sdk_medialive._operations.media_live.start_delete_monitor_deployment.start_delete_monitor_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.start_delete_monitor_deployment_request.StartDeleteMonitorDeploymentRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_input_device(
        self,
        input_device_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.start_input_device_response.StartInputDeviceResponse":
        """Start an input device that is attached to a MediaConnect flow. (There is no need to start a device that is attached to a MediaLive input; MediaLive starts the device when the channel starts.)

        Args:
            input_device_id: The unique ID of the input device to start. For example, hd-123456789abcdef.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.start_input_device_request.StartInputDeviceRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.start_input_device_response.StartInputDeviceResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.start_input_device

            output, http_response = (
                aws_sdk_medialive._operations.media_live.start_input_device.start_input_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.start_input_device_request.StartInputDeviceRequest = {}  # type: ignore[typeddict-item]
        input_["input_device_id"] = input_device_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_input_device_maintenance_window(
        self,
        input_device_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.start_input_device_maintenance_window_response.StartInputDeviceMaintenanceWindowResponse":
        """Start a maintenance window for the specified input device. Starting a maintenance window will give the device up to two hours to install software. If the device was streaming prior to the maintenance, it will resume streaming when the software is fully installed. Devices automatically install updates while they are powered on and their MediaLive channels are stopped. A maintenance window allows you to update a device without having to stop MediaLive channels that use the device. The device must remain powered on and connected to the internet for the duration of the maintenance.

        Args:
            input_device_id: The unique ID of the input device to start a maintenance window for. For example, hd-123456789abcdef.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.start_input_device_maintenance_window_request.StartInputDeviceMaintenanceWindowRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.start_input_device_maintenance_window_response.StartInputDeviceMaintenanceWindowResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.start_input_device_maintenance_window

            output, http_response = (
                aws_sdk_medialive._operations.media_live.start_input_device_maintenance_window.start_input_device_maintenance_window(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.start_input_device_maintenance_window_request.StartInputDeviceMaintenanceWindowRequest = {}  # type: ignore[typeddict-item]
        input_["input_device_id"] = input_device_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_monitor_deployment(
        self,
        identifier: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        dry_run: Optional["aws_sdk_medialive.types.__boolean.__boolean"] = None,
    ) -> "aws_sdk_medialive.types.start_monitor_deployment_response.StartMonitorDeploymentResponse":
        """Initiates a deployment to deploy the latest monitor of the specified signal map.

        Args:
            identifier: A signal map's identifier. Can be either be its id or current name.

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.start_monitor_deployment_request.StartMonitorDeploymentRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.start_monitor_deployment_response.StartMonitorDeploymentResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.start_monitor_deployment

            output, http_response = (
                aws_sdk_medialive._operations.media_live.start_monitor_deployment.start_monitor_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.start_monitor_deployment_request.StartMonitorDeploymentRequest = {}  # type: ignore[typeddict-item]
        if dry_run is not None:
            input_["dry_run"] = dry_run
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_multiplex(
        self,
        multiplex_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.start_multiplex_response.StartMultiplexResponse":
        """Start (run) the multiplex. Starting the multiplex does not start the channels. You must explicitly start each channel.

        Args:
            multiplex_id: The ID of the multiplex.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.start_multiplex_request.StartMultiplexRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.start_multiplex_response.StartMultiplexResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.start_multiplex

            output, http_response = (
                aws_sdk_medialive._operations.media_live.start_multiplex.start_multiplex(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.start_multiplex_request.StartMultiplexRequest = {}  # type: ignore[typeddict-item]
        input_["multiplex_id"] = multiplex_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_update_signal_map(
        self,
        identifier: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        cloud_watch_alarm_template_group_identifiers: Optional[
            "aws_sdk_medialive.types.__list_of__string_pattern_s.__listOf__stringPatternS"
        ] = None,
        description: Optional[
            "aws_sdk_medialive.types.__string_min0_max1024.__stringMin0Max1024"
        ] = None,
        discovery_entry_point_arn: Optional[
            "aws_sdk_medialive.types.__string_min1_max2048.__stringMin1Max2048"
        ] = None,
        event_bridge_rule_template_group_identifiers: Optional[
            "aws_sdk_medialive.types.__list_of__string_pattern_s.__listOf__stringPatternS"
        ] = None,
        force_rediscovery: Optional[
            "aws_sdk_medialive.types.__boolean.__boolean"
        ] = None,
        name: Optional[
            "aws_sdk_medialive.types.__string_min1_max255_pattern_s.__stringMin1Max255PatternS"
        ] = None,
    ) -> "aws_sdk_medialive.types.start_update_signal_map_response.StartUpdateSignalMapResponse":
        """Initiates an update for the specified signal map. Will discover a new signal map if a changed discoveryEntryPointArn is provided.

        Args:
            description: A resource's optional description.
            discovery_entry_point_arn: A top-level supported AWS resource ARN to discovery a signal map from.
            force_rediscovery: If true, will force a rediscovery of a signal map if an unchanged discoveryEntryPointArn is provided.
            identifier: A signal map's identifier. Can be either be its id or current name.
            name: A resource's name. Names must be unique within the scope of a resource type in a specific region.

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.start_update_signal_map_request.StartUpdateSignalMapRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.start_update_signal_map_response.StartUpdateSignalMapResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.start_update_signal_map

            output, http_response = (
                aws_sdk_medialive._operations.media_live.start_update_signal_map.start_update_signal_map(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.start_update_signal_map_request.StartUpdateSignalMapRequest = {}  # type: ignore[typeddict-item]
        if cloud_watch_alarm_template_group_identifiers is not None:
            input_["cloud_watch_alarm_template_group_identifiers"] = (
                cloud_watch_alarm_template_group_identifiers
            )
        if description is not None:
            input_["description"] = description
        if discovery_entry_point_arn is not None:
            input_["discovery_entry_point_arn"] = discovery_entry_point_arn
        if event_bridge_rule_template_group_identifiers is not None:
            input_["event_bridge_rule_template_group_identifiers"] = (
                event_bridge_rule_template_group_identifiers
            )
        if force_rediscovery is not None:
            input_["force_rediscovery"] = force_rediscovery
        input_["identifier"] = identifier
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_channel(
        self,
        channel_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.stop_channel_response.StopChannelResponse":
        """Stops a running channel

        Args:
            channel_id: A request to stop a running channel

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.stop_channel_request.StopChannelRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.stop_channel_response.StopChannelResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.stop_channel

            output, http_response = (
                aws_sdk_medialive._operations.media_live.stop_channel.stop_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.stop_channel_request.StopChannelRequest = {}  # type: ignore[typeddict-item]
        input_["channel_id"] = channel_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_input_device(
        self,
        input_device_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.stop_input_device_response.StopInputDeviceResponse":
        """Stop an input device that is attached to a MediaConnect flow. (There is no need to stop a device that is attached to a MediaLive input; MediaLive automatically stops the device when the channel stops.)

        Args:
            input_device_id: The unique ID of the input device to stop. For example, hd-123456789abcdef.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.stop_input_device_request.StopInputDeviceRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.stop_input_device_response.StopInputDeviceResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.stop_input_device

            output, http_response = (
                aws_sdk_medialive._operations.media_live.stop_input_device.stop_input_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.stop_input_device_request.StopInputDeviceRequest = {}  # type: ignore[typeddict-item]
        input_["input_device_id"] = input_device_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_multiplex(
        self,
        multiplex_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "aws_sdk_medialive.types.stop_multiplex_response.StopMultiplexResponse":
        """Stops a running multiplex. If the multiplex isn't running, this action has no effect.

        Args:
            multiplex_id: The ID of the multiplex.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.stop_multiplex_request.StopMultiplexRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.stop_multiplex_response.StopMultiplexResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.stop_multiplex

            output, http_response = (
                aws_sdk_medialive._operations.media_live.stop_multiplex.stop_multiplex(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.stop_multiplex_request.StopMultiplexRequest = {}  # type: ignore[typeddict-item]
        input_["multiplex_id"] = multiplex_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def transfer_input_device(
        self,
        input_device_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        target_customer_id: Optional[
            "aws_sdk_medialive.types.__string.__string"
        ] = None,
        target_region: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        transfer_message: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> "aws_sdk_medialive.types.transfer_input_device_response.TransferInputDeviceResponse":
        """Start an input device transfer to another AWS account. After you make the request, the other account must accept or reject the transfer.

        Args:
            input_device_id: The unique ID of this input device. For example, hd-123456789abcdef.
            target_customer_id: The AWS account ID (12 digits) for the recipient of the device transfer.
            target_region: The target AWS region to transfer the device.
            transfer_message: An optional message for the recipient. Maximum 280 characters.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.transfer_input_device_request.TransferInputDeviceRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.transfer_input_device_response.TransferInputDeviceResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.transfer_input_device

            output, http_response = (
                aws_sdk_medialive._operations.media_live.transfer_input_device.transfer_input_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.transfer_input_device_request.TransferInputDeviceRequest = {}  # type: ignore[typeddict-item]
        input_["input_device_id"] = input_device_id
        if target_customer_id is not None:
            input_["target_customer_id"] = target_customer_id
        if target_region is not None:
            input_["target_region"] = target_region
        if transfer_message is not None:
            input_["transfer_message"] = transfer_message

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_account_configuration(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        account_configuration: Optional[
            "aws_sdk_medialive.types.account_configuration.AccountConfiguration"
        ] = None,
    ) -> "aws_sdk_medialive.types.update_account_configuration_response.UpdateAccountConfigurationResponse":
        """Update account configuration

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.update_account_configuration_request.UpdateAccountConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.update_account_configuration_response.UpdateAccountConfigurationResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.update_account_configuration

            output, http_response = (
                aws_sdk_medialive._operations.media_live.update_account_configuration.update_account_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.update_account_configuration_request.UpdateAccountConfigurationRequest = {}  # type: ignore[typeddict-item]
        if account_configuration is not None:
            input_["account_configuration"] = account_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_channel(
        self,
        channel_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        cdi_input_specification: Optional[
            "aws_sdk_medialive.types.cdi_input_specification.CdiInputSpecification"
        ] = None,
        destinations: Optional[
            "aws_sdk_medialive.types.__list_of_output_destination.__listOfOutputDestination"
        ] = None,
        encoder_settings: Optional[
            "aws_sdk_medialive.types.encoder_settings.EncoderSettings"
        ] = None,
        input_attachments: Optional[
            "aws_sdk_medialive.types.__list_of_input_attachment.__listOfInputAttachment"
        ] = None,
        input_specification: Optional[
            "aws_sdk_medialive.types.input_specification.InputSpecification"
        ] = None,
        log_level: Optional["aws_sdk_medialive.types.log_level.LogLevel"] = None,
        maintenance: Optional[
            "aws_sdk_medialive.types.maintenance_update_settings.MaintenanceUpdateSettings"
        ] = None,
        name: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        role_arn: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        channel_engine_version: Optional[
            "aws_sdk_medialive.types.channel_engine_version_request.ChannelEngineVersionRequest"
        ] = None,
        dry_run: Optional["aws_sdk_medialive.types.__boolean.__boolean"] = None,
        anywhere_settings: Optional[
            "aws_sdk_medialive.types.anywhere_settings.AnywhereSettings"
        ] = None,
        linked_channel_settings: Optional[
            "aws_sdk_medialive.types.linked_channel_settings.LinkedChannelSettings"
        ] = None,
        channel_security_groups: Optional[
            "aws_sdk_medialive.types.__list_of__string.__listOf__string"
        ] = None,
        inference_settings: Optional[
            "aws_sdk_medialive.types.inference_settings.InferenceSettings"
        ] = None,
        special_router_settings: Optional[
            "aws_sdk_medialive.types.special_router_settings.SpecialRouterSettings"
        ] = None,
    ) -> "aws_sdk_medialive.types.update_channel_response.UpdateChannelResponse":
        """Updates a channel.

        Args:
            cdi_input_specification: Specification of CDI inputs for this channel
            channel_id: channel ID
            destinations: A list of output destinations for this channel.
            encoder_settings: The encoder settings for this channel.
            input_specification: Specification of network and file inputs for this channel
            log_level: The log level to write to CloudWatch Logs.
            maintenance: Maintenance settings for this channel.
            name: The name of the channel.
            role_arn: An optional Amazon Resource Name (ARN) of the role to assume when running the Channel. If you do not specify this on an update call but the role was previously set that role will be removed.
            channel_engine_version: Channel engine version for this channel
            anywhere_settings: The Elemental Anywhere settings for this channel.
            linked_channel_settings: The linked channel settings for the channel.
            channel_security_groups: A list of IDs for all the Input Security Groups attached to the channel.
            inference_settings: Include this setting to include Elemental Inference features in this channel.
            special_router_settings: When using MediaConnect Router as the source of a MediaLive input there's a special handoff that occurs when a router output is created. This group of settings is set on your behalf by the MediaConnect Router service using this set of settings. This setting object can only by used by that service.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.update_channel_request.UpdateChannelRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.update_channel_response.UpdateChannelResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.update_channel

            output, http_response = (
                aws_sdk_medialive._operations.media_live.update_channel.update_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.update_channel_request.UpdateChannelRequest = {}  # type: ignore[typeddict-item]
        if cdi_input_specification is not None:
            input_["cdi_input_specification"] = cdi_input_specification
        input_["channel_id"] = channel_id
        if destinations is not None:
            input_["destinations"] = destinations
        if encoder_settings is not None:
            input_["encoder_settings"] = encoder_settings
        if input_attachments is not None:
            input_["input_attachments"] = input_attachments
        if input_specification is not None:
            input_["input_specification"] = input_specification
        if log_level is not None:
            input_["log_level"] = log_level
        if maintenance is not None:
            input_["maintenance"] = maintenance
        if name is not None:
            input_["name"] = name
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if channel_engine_version is not None:
            input_["channel_engine_version"] = channel_engine_version
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if anywhere_settings is not None:
            input_["anywhere_settings"] = anywhere_settings
        if linked_channel_settings is not None:
            input_["linked_channel_settings"] = linked_channel_settings
        if channel_security_groups is not None:
            input_["channel_security_groups"] = channel_security_groups
        if inference_settings is not None:
            input_["inference_settings"] = inference_settings
        if special_router_settings is not None:
            input_["special_router_settings"] = special_router_settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_channel_class(
        self,
        channel_class: "aws_sdk_medialive.types.channel_class.ChannelClass",
        channel_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        destinations: Optional[
            "aws_sdk_medialive.types.__list_of_output_destination.__listOfOutputDestination"
        ] = None,
    ) -> "aws_sdk_medialive.types.update_channel_class_response.UpdateChannelClassResponse":
        """Changes the class of the channel.

        Args:
            channel_class: The channel class that you wish to update this channel to use.
            channel_id: Channel Id of the channel whose class should be updated.
            destinations: A list of output destinations for this channel.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.update_channel_class_request.UpdateChannelClassRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.update_channel_class_response.UpdateChannelClassResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.update_channel_class

            output, http_response = (
                aws_sdk_medialive._operations.media_live.update_channel_class.update_channel_class(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.update_channel_class_request.UpdateChannelClassRequest = {}  # type: ignore[typeddict-item]
        input_["channel_class"] = channel_class
        input_["channel_id"] = channel_id
        if destinations is not None:
            input_["destinations"] = destinations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_channel_placement_group(
        self,
        channel_placement_group_id: "aws_sdk_medialive.types.__string.__string",
        cluster_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        name: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        nodes: Optional[
            "aws_sdk_medialive.types.__list_of__string.__listOf__string"
        ] = None,
    ) -> "aws_sdk_medialive.types.update_channel_placement_group_response.UpdateChannelPlacementGroupResponse":
        """Change the settings for a ChannelPlacementGroup.

        Args:
            channel_placement_group_id: The ID of the channel placement group.
            cluster_id: The ID of the cluster.
            name: Include this parameter only if you want to change the current name of the ChannelPlacementGroup. Specify a name that is unique in the Cluster. You can't change the name. Names are case-sensitive.
            nodes: Include this parameter only if you want to change the list of Nodes that are associated with the ChannelPlacementGroup.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.update_channel_placement_group_request.UpdateChannelPlacementGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.update_channel_placement_group_response.UpdateChannelPlacementGroupResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.update_channel_placement_group

            output, http_response = (
                aws_sdk_medialive._operations.media_live.update_channel_placement_group.update_channel_placement_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.update_channel_placement_group_request.UpdateChannelPlacementGroupRequest = {}  # type: ignore[typeddict-item]
        input_["channel_placement_group_id"] = channel_placement_group_id
        input_["cluster_id"] = cluster_id
        if name is not None:
            input_["name"] = name
        if nodes is not None:
            input_["nodes"] = nodes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_cloud_watch_alarm_template(
        self,
        identifier: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        comparison_operator: Optional[
            "aws_sdk_medialive.types.cloud_watch_alarm_template_comparison_operator.CloudWatchAlarmTemplateComparisonOperator"
        ] = None,
        datapoints_to_alarm: Optional[
            "aws_sdk_medialive.types.__integer_min1.__integerMin1"
        ] = None,
        description: Optional[
            "aws_sdk_medialive.types.__string_min0_max1024.__stringMin0Max1024"
        ] = None,
        evaluation_periods: Optional[
            "aws_sdk_medialive.types.__integer_min1.__integerMin1"
        ] = None,
        group_identifier: Optional[
            "aws_sdk_medialive.types.__string_pattern_s.__stringPatternS"
        ] = None,
        metric_name: Optional[
            "aws_sdk_medialive.types.__string_max64.__stringMax64"
        ] = None,
        name: Optional[
            "aws_sdk_medialive.types.__string_min1_max255_pattern_s.__stringMin1Max255PatternS"
        ] = None,
        period: Optional[
            "aws_sdk_medialive.types.__integer_min10_max86400.__integerMin10Max86400"
        ] = None,
        statistic: Optional[
            "aws_sdk_medialive.types.cloud_watch_alarm_template_statistic.CloudWatchAlarmTemplateStatistic"
        ] = None,
        target_resource_type: Optional[
            "aws_sdk_medialive.types.cloud_watch_alarm_template_target_resource_type.CloudWatchAlarmTemplateTargetResourceType"
        ] = None,
        threshold: Optional["aws_sdk_medialive.types.__double.__double"] = None,
        treat_missing_data: Optional[
            "aws_sdk_medialive.types.cloud_watch_alarm_template_treat_missing_data.CloudWatchAlarmTemplateTreatMissingData"
        ] = None,
    ) -> "aws_sdk_medialive.types.update_cloud_watch_alarm_template_response.UpdateCloudWatchAlarmTemplateResponse":
        """Updates the specified cloudwatch alarm template.

        Args:
            datapoints_to_alarm: The number of datapoints within the evaluation period that must be breaching to trigger the alarm.
            description: A resource's optional description.
            evaluation_periods: The number of periods over which data is compared to the specified threshold.
            group_identifier: A cloudwatch alarm template group's identifier. Can be either be its id or current name.
            identifier: A cloudwatch alarm template's identifier. Can be either be its id or current name.
            metric_name: The name of the metric associated with the alarm. Must be compatible with targetResourceType.
            name: A resource's name. Names must be unique within the scope of a resource type in a specific region.
            period: The period, in seconds, over which the specified statistic is applied.
            threshold: The threshold value to compare with the specified statistic.

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.update_cloud_watch_alarm_template_request.UpdateCloudWatchAlarmTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.update_cloud_watch_alarm_template_response.UpdateCloudWatchAlarmTemplateResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.update_cloud_watch_alarm_template

            output, http_response = (
                aws_sdk_medialive._operations.media_live.update_cloud_watch_alarm_template.update_cloud_watch_alarm_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.update_cloud_watch_alarm_template_request.UpdateCloudWatchAlarmTemplateRequest = {}  # type: ignore[typeddict-item]
        if comparison_operator is not None:
            input_["comparison_operator"] = comparison_operator
        if datapoints_to_alarm is not None:
            input_["datapoints_to_alarm"] = datapoints_to_alarm
        if description is not None:
            input_["description"] = description
        if evaluation_periods is not None:
            input_["evaluation_periods"] = evaluation_periods
        if group_identifier is not None:
            input_["group_identifier"] = group_identifier
        input_["identifier"] = identifier
        if metric_name is not None:
            input_["metric_name"] = metric_name
        if name is not None:
            input_["name"] = name
        if period is not None:
            input_["period"] = period
        if statistic is not None:
            input_["statistic"] = statistic
        if target_resource_type is not None:
            input_["target_resource_type"] = target_resource_type
        if threshold is not None:
            input_["threshold"] = threshold
        if treat_missing_data is not None:
            input_["treat_missing_data"] = treat_missing_data

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_cloud_watch_alarm_template_group(
        self,
        identifier: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        description: Optional[
            "aws_sdk_medialive.types.__string_min0_max1024.__stringMin0Max1024"
        ] = None,
    ) -> "aws_sdk_medialive.types.update_cloud_watch_alarm_template_group_response.UpdateCloudWatchAlarmTemplateGroupResponse":
        """Updates the specified cloudwatch alarm template group.

        Args:
            description: A resource's optional description.
            identifier: A cloudwatch alarm template group's identifier. Can be either be its id or current name.

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.update_cloud_watch_alarm_template_group_request.UpdateCloudWatchAlarmTemplateGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.update_cloud_watch_alarm_template_group_response.UpdateCloudWatchAlarmTemplateGroupResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.update_cloud_watch_alarm_template_group

            output, http_response = (
                aws_sdk_medialive._operations.media_live.update_cloud_watch_alarm_template_group.update_cloud_watch_alarm_template_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.update_cloud_watch_alarm_template_group_request.UpdateCloudWatchAlarmTemplateGroupRequest = {}  # type: ignore[typeddict-item]
        if description is not None:
            input_["description"] = description
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_cluster(
        self,
        cluster_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        name: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        network_settings: Optional[
            "aws_sdk_medialive.types.cluster_network_settings_update_request.ClusterNetworkSettingsUpdateRequest"
        ] = None,
    ) -> "aws_sdk_medialive.types.update_cluster_response.UpdateClusterResponse":
        """Change the settings for a Cluster.

        Args:
            cluster_id: The ID of the cluster
            name: Include this parameter only if you want to change the current name of the Cluster. Specify a name that is unique in the AWS account. You can't change the name. Names are case-sensitive.
            network_settings: Include this property only if you want to change the current connections between the Nodes in the Cluster and the Networks the Cluster is associated with.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.update_cluster_request.UpdateClusterRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.update_cluster_response.UpdateClusterResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.update_cluster

            output, http_response = (
                aws_sdk_medialive._operations.media_live.update_cluster.update_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.update_cluster_request.UpdateClusterRequest = {}  # type: ignore[typeddict-item]
        input_["cluster_id"] = cluster_id
        if name is not None:
            input_["name"] = name
        if network_settings is not None:
            input_["network_settings"] = network_settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_event_bridge_rule_template(
        self,
        identifier: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        description: Optional[
            "aws_sdk_medialive.types.__string_min0_max1024.__stringMin0Max1024"
        ] = None,
        event_targets: Optional[
            "aws_sdk_medialive.types.__list_of_event_bridge_rule_template_target.__listOfEventBridgeRuleTemplateTarget"
        ] = None,
        event_type: Optional[
            "aws_sdk_medialive.types.event_bridge_rule_template_event_type.EventBridgeRuleTemplateEventType"
        ] = None,
        group_identifier: Optional[
            "aws_sdk_medialive.types.__string_pattern_s.__stringPatternS"
        ] = None,
        name: Optional[
            "aws_sdk_medialive.types.__string_min1_max255_pattern_s.__stringMin1Max255PatternS"
        ] = None,
    ) -> "aws_sdk_medialive.types.update_event_bridge_rule_template_response.UpdateEventBridgeRuleTemplateResponse":
        """Updates the specified eventbridge rule template.

        Args:
            description: A resource's optional description.
            group_identifier: An eventbridge rule template group's identifier. Can be either be its id or current name.
            identifier: An eventbridge rule template's identifier. Can be either be its id or current name.
            name: A resource's name. Names must be unique within the scope of a resource type in a specific region.

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.update_event_bridge_rule_template_request.UpdateEventBridgeRuleTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.update_event_bridge_rule_template_response.UpdateEventBridgeRuleTemplateResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.update_event_bridge_rule_template

            output, http_response = (
                aws_sdk_medialive._operations.media_live.update_event_bridge_rule_template.update_event_bridge_rule_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.update_event_bridge_rule_template_request.UpdateEventBridgeRuleTemplateRequest = {}  # type: ignore[typeddict-item]
        if description is not None:
            input_["description"] = description
        if event_targets is not None:
            input_["event_targets"] = event_targets
        if event_type is not None:
            input_["event_type"] = event_type
        if group_identifier is not None:
            input_["group_identifier"] = group_identifier
        input_["identifier"] = identifier
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_event_bridge_rule_template_group(
        self,
        identifier: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        description: Optional[
            "aws_sdk_medialive.types.__string_min0_max1024.__stringMin0Max1024"
        ] = None,
    ) -> "aws_sdk_medialive.types.update_event_bridge_rule_template_group_response.UpdateEventBridgeRuleTemplateGroupResponse":
        """Updates the specified eventbridge rule template group.

        Args:
            description: A resource's optional description.
            identifier: An eventbridge rule template group's identifier. Can be either be its id or current name.

        Raises:
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.update_event_bridge_rule_template_group_request.UpdateEventBridgeRuleTemplateGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.update_event_bridge_rule_template_group_response.UpdateEventBridgeRuleTemplateGroupResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.update_event_bridge_rule_template_group

            output, http_response = (
                aws_sdk_medialive._operations.media_live.update_event_bridge_rule_template_group.update_event_bridge_rule_template_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.update_event_bridge_rule_template_group_request.UpdateEventBridgeRuleTemplateGroupRequest = {}  # type: ignore[typeddict-item]
        if description is not None:
            input_["description"] = description
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_input(
        self,
        input_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        destinations: Optional[
            "aws_sdk_medialive.types.__list_of_input_destination_request.__listOfInputDestinationRequest"
        ] = None,
        input_devices: Optional[
            "aws_sdk_medialive.types.__list_of_input_device_request.__listOfInputDeviceRequest"
        ] = None,
        input_security_groups: Optional[
            "aws_sdk_medialive.types.__list_of__string.__listOf__string"
        ] = None,
        media_connect_flows: Optional[
            "aws_sdk_medialive.types.__list_of_media_connect_flow_request.__listOfMediaConnectFlowRequest"
        ] = None,
        name: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        role_arn: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        sources: Optional[
            "aws_sdk_medialive.types.__list_of_input_source_request.__listOfInputSourceRequest"
        ] = None,
        srt_settings: Optional[
            "aws_sdk_medialive.types.srt_settings_request.SrtSettingsRequest"
        ] = None,
        multicast_settings: Optional[
            "aws_sdk_medialive.types.multicast_settings_update_request.MulticastSettingsUpdateRequest"
        ] = None,
        smpte2110_receiver_group_settings: Optional[
            "aws_sdk_medialive.types.smpte2110_receiver_group_settings.Smpte2110ReceiverGroupSettings"
        ] = None,
        sdi_sources: Optional[
            "aws_sdk_medialive.types.input_sdi_sources.InputSdiSources"
        ] = None,
        special_router_settings: Optional[
            "aws_sdk_medialive.types.special_router_settings.SpecialRouterSettings"
        ] = None,
    ) -> "aws_sdk_medialive.types.update_input_response.UpdateInputResponse":
        """Updates an input.

        Args:
            destinations: Destination settings for PUSH type inputs.
            input_devices: Settings for the devices.
            input_id: Unique ID of the input.
            input_security_groups: A list of security groups referenced by IDs to attach to the input.
            media_connect_flows: A list of the MediaConnect Flow ARNs that you want to use as the source of the input. You can specify as few as one Flow and presently, as many as two. The only requirement is when you have more than one is that each Flow is in a separate Availability Zone as this ensures your EML input is redundant to AZ issues.
            name: Name of the input.
            role_arn: The Amazon Resource Name (ARN) of the role this input assumes during and after creation.
            sources: The source URLs for a PULL-type input. Every PULL type input needs exactly two source URLs for redundancy. Only specify sources for PULL type Inputs. Leave Destinations empty.
            srt_settings: The settings associated with an SRT input.
            multicast_settings: Multicast Input settings.
            smpte2110_receiver_group_settings: Include this parameter if the input is a SMPTE 2110 input, to identify the stream sources for this input.
            special_router_settings: When using MediaConnect Router as the source of a MediaLive input there's a special handoff that occurs when a router output is created. This group of settings is set on your behalf by the MediaConnect Router service using this set of settings. This setting object can only by used by that service.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.update_input_request.UpdateInputRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.update_input_response.UpdateInputResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.update_input

            output, http_response = (
                aws_sdk_medialive._operations.media_live.update_input.update_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.update_input_request.UpdateInputRequest = {}  # type: ignore[typeddict-item]
        if destinations is not None:
            input_["destinations"] = destinations
        if input_devices is not None:
            input_["input_devices"] = input_devices
        input_["input_id"] = input_id
        if input_security_groups is not None:
            input_["input_security_groups"] = input_security_groups
        if media_connect_flows is not None:
            input_["media_connect_flows"] = media_connect_flows
        if name is not None:
            input_["name"] = name
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if sources is not None:
            input_["sources"] = sources
        if srt_settings is not None:
            input_["srt_settings"] = srt_settings
        if multicast_settings is not None:
            input_["multicast_settings"] = multicast_settings
        if smpte2110_receiver_group_settings is not None:
            input_["smpte2110_receiver_group_settings"] = (
                smpte2110_receiver_group_settings
            )
        if sdi_sources is not None:
            input_["sdi_sources"] = sdi_sources
        if special_router_settings is not None:
            input_["special_router_settings"] = special_router_settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_input_device(
        self,
        input_device_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        hd_device_settings: Optional[
            "aws_sdk_medialive.types.input_device_configurable_settings.InputDeviceConfigurableSettings"
        ] = None,
        name: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        uhd_device_settings: Optional[
            "aws_sdk_medialive.types.input_device_configurable_settings.InputDeviceConfigurableSettings"
        ] = None,
        availability_zone: Optional["aws_sdk_medialive.types.__string.__string"] = None,
    ) -> (
        "aws_sdk_medialive.types.update_input_device_response.UpdateInputDeviceResponse"
    ):
        """Updates the parameters for the input device.

        Args:
            hd_device_settings: The settings that you want to apply to the HD input device.
            input_device_id: The unique ID of the input device. For example, hd-123456789abcdef.
            name: The name that you assigned to this input device (not the unique ID).
            uhd_device_settings: The settings that you want to apply to the UHD input device.
            availability_zone: The Availability Zone you want associated with this input device.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.update_input_device_request.UpdateInputDeviceRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.update_input_device_response.UpdateInputDeviceResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.update_input_device

            output, http_response = (
                aws_sdk_medialive._operations.media_live.update_input_device.update_input_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.update_input_device_request.UpdateInputDeviceRequest = {}  # type: ignore[typeddict-item]
        if hd_device_settings is not None:
            input_["hd_device_settings"] = hd_device_settings
        input_["input_device_id"] = input_device_id
        if name is not None:
            input_["name"] = name
        if uhd_device_settings is not None:
            input_["uhd_device_settings"] = uhd_device_settings
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_input_security_group(
        self,
        input_security_group_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        tags: Optional["aws_sdk_medialive.types.tags.Tags"] = None,
        whitelist_rules: Optional[
            "aws_sdk_medialive.types.__list_of_input_whitelist_rule_cidr.__listOfInputWhitelistRuleCidr"
        ] = None,
    ) -> "aws_sdk_medialive.types.update_input_security_group_response.UpdateInputSecurityGroupResponse":
        """Update an Input Security Group's Whilelists.

        Args:
            input_security_group_id: The id of the Input Security Group to update.
            tags: A collection of key-value pairs.
            whitelist_rules: List of IPv4 CIDR addresses to whitelist

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.update_input_security_group_request.UpdateInputSecurityGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.update_input_security_group_response.UpdateInputSecurityGroupResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.update_input_security_group

            output, http_response = (
                aws_sdk_medialive._operations.media_live.update_input_security_group.update_input_security_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.update_input_security_group_request.UpdateInputSecurityGroupRequest = {}  # type: ignore[typeddict-item]
        input_["input_security_group_id"] = input_security_group_id
        if tags is not None:
            input_["tags"] = tags
        if whitelist_rules is not None:
            input_["whitelist_rules"] = whitelist_rules

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_multiplex(
        self,
        multiplex_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        multiplex_settings: Optional[
            "aws_sdk_medialive.types.multiplex_settings.MultiplexSettings"
        ] = None,
        name: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        packet_identifiers_mapping: Optional[
            "aws_sdk_medialive.types.multiplex_packet_identifiers_mapping.MultiplexPacketIdentifiersMapping"
        ] = None,
    ) -> "aws_sdk_medialive.types.update_multiplex_response.UpdateMultiplexResponse":
        """Updates a multiplex.

        Args:
            multiplex_id: ID of the multiplex to update.
            multiplex_settings: The new settings for a multiplex.
            name: Name of the multiplex.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.update_multiplex_request.UpdateMultiplexRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.update_multiplex_response.UpdateMultiplexResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.update_multiplex

            output, http_response = (
                aws_sdk_medialive._operations.media_live.update_multiplex.update_multiplex(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.update_multiplex_request.UpdateMultiplexRequest = {}  # type: ignore[typeddict-item]
        input_["multiplex_id"] = multiplex_id
        if multiplex_settings is not None:
            input_["multiplex_settings"] = multiplex_settings
        if name is not None:
            input_["name"] = name
        if packet_identifiers_mapping is not None:
            input_["packet_identifiers_mapping"] = packet_identifiers_mapping

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_multiplex_program(
        self,
        multiplex_id: "aws_sdk_medialive.types.__string.__string",
        program_name: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        multiplex_program_settings: Optional[
            "aws_sdk_medialive.types.multiplex_program_settings.MultiplexProgramSettings"
        ] = None,
    ) -> "aws_sdk_medialive.types.update_multiplex_program_response.UpdateMultiplexProgramResponse":
        """Update a program in a multiplex.

        Args:
            multiplex_id: The ID of the multiplex of the program to update.
            multiplex_program_settings: The new settings for a multiplex program.
            program_name: The name of the program to update.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.update_multiplex_program_request.UpdateMultiplexProgramRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.update_multiplex_program_response.UpdateMultiplexProgramResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.update_multiplex_program

            output, http_response = (
                aws_sdk_medialive._operations.media_live.update_multiplex_program.update_multiplex_program(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.update_multiplex_program_request.UpdateMultiplexProgramRequest = {}  # type: ignore[typeddict-item]
        input_["multiplex_id"] = multiplex_id
        if multiplex_program_settings is not None:
            input_["multiplex_program_settings"] = multiplex_program_settings
        input_["program_name"] = program_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_network(
        self,
        network_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        ip_pools: Optional[
            "aws_sdk_medialive.types.__list_of_ip_pool_update_request.__listOfIpPoolUpdateRequest"
        ] = None,
        name: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        routes: Optional[
            "aws_sdk_medialive.types.__list_of_route_update_request.__listOfRouteUpdateRequest"
        ] = None,
    ) -> "aws_sdk_medialive.types.update_network_response.UpdateNetworkResponse":
        """Change the settings for a Network.

        Args:
            ip_pools: Include this parameter only if you want to change the pool of IP addresses in the network. An array of IpPoolCreateRequests that identify a collection of IP addresses in this network that you want to reserve for use in MediaLive Anywhere. MediaLive Anywhere uses these IP addresses for Push inputs (in both Bridge and NAT networks) and for output destinations (only in Bridge networks). Each IpPoolUpdateRequest specifies one CIDR block.
            name: Include this parameter only if you want to change the name of the Network. Specify a name that is unique in the AWS account. Names are case-sensitive.
            network_id: The ID of the network
            routes: Include this parameter only if you want to change or add routes in the Network. An array of Routes that MediaLive Anywhere needs to know about in order to route encoding traffic.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.update_network_request.UpdateNetworkRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.update_network_response.UpdateNetworkResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.update_network

            output, http_response = (
                aws_sdk_medialive._operations.media_live.update_network.update_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.update_network_request.UpdateNetworkRequest = {}  # type: ignore[typeddict-item]
        if ip_pools is not None:
            input_["ip_pools"] = ip_pools
        if name is not None:
            input_["name"] = name
        input_["network_id"] = network_id
        if routes is not None:
            input_["routes"] = routes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_node(
        self,
        cluster_id: "aws_sdk_medialive.types.__string.__string",
        node_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        name: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        role: Optional["aws_sdk_medialive.types.node_role.NodeRole"] = None,
        sdi_source_mappings: Optional[
            "aws_sdk_medialive.types.sdi_source_mappings_update_request.SdiSourceMappingsUpdateRequest"
        ] = None,
    ) -> "aws_sdk_medialive.types.update_node_response.UpdateNodeResponse":
        """Change the settings for a Node.

        Args:
            cluster_id: The ID of the cluster
            name: Include this parameter only if you want to change the current name of the Node. Specify a name that is unique in the Cluster. You can't change the name. Names are case-sensitive.
            node_id: The ID of the node.
            role: The initial role of the Node in the Cluster. ACTIVE means the Node is available for encoding. BACKUP means the Node is a redundant Node and might get used if an ACTIVE Node fails.
            sdi_source_mappings: The mappings of a SDI capture card port to a logical SDI data stream

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.update_node_request.UpdateNodeRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.update_node_response.UpdateNodeResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.update_node

            output, http_response = (
                aws_sdk_medialive._operations.media_live.update_node.update_node(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.update_node_request.UpdateNodeRequest = {}  # type: ignore[typeddict-item]
        input_["cluster_id"] = cluster_id
        if name is not None:
            input_["name"] = name
        input_["node_id"] = node_id
        if role is not None:
            input_["role"] = role
        if sdi_source_mappings is not None:
            input_["sdi_source_mappings"] = sdi_source_mappings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_node_state(
        self,
        cluster_id: "aws_sdk_medialive.types.__string.__string",
        node_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        state: Optional[
            "aws_sdk_medialive.types.update_node_state_shape.UpdateNodeStateShape"
        ] = None,
    ) -> "aws_sdk_medialive.types.update_node_state_response.UpdateNodeStateResponse":
        """Update the state of a node.

        Args:
            cluster_id: The ID of the cluster
            node_id: The ID of the node.
            state: The state to apply to the Node. Set to ACTIVE (COMMISSIONED) to indicate that the Node is deployable. MediaLive Anywhere will consider this node it needs a Node to run a Channel on, or when it needs a Node to promote from a backup node to an active node. Set to DRAINING to isolate the Node so that MediaLive Anywhere won't use it.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.update_node_state_request.UpdateNodeStateRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.update_node_state_response.UpdateNodeStateResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.update_node_state

            output, http_response = (
                aws_sdk_medialive._operations.media_live.update_node_state.update_node_state(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.update_node_state_request.UpdateNodeStateRequest = {}  # type: ignore[typeddict-item]
        input_["cluster_id"] = cluster_id
        input_["node_id"] = node_id
        if state is not None:
            input_["state"] = state

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_reservation(
        self,
        reservation_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        name: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        renewal_settings: Optional[
            "aws_sdk_medialive.types.renewal_settings.RenewalSettings"
        ] = None,
    ) -> (
        "aws_sdk_medialive.types.update_reservation_response.UpdateReservationResponse"
    ):
        """Update reservation.

        Args:
            name: Name of the reservation
            renewal_settings: Renewal settings for the reservation
            reservation_id: Unique reservation ID, e.g. '1234567'

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.update_reservation_request.UpdateReservationRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.update_reservation_response.UpdateReservationResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.update_reservation

            output, http_response = (
                aws_sdk_medialive._operations.media_live.update_reservation.update_reservation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.update_reservation_request.UpdateReservationRequest = {}  # type: ignore[typeddict-item]
        if name is not None:
            input_["name"] = name
        if renewal_settings is not None:
            input_["renewal_settings"] = renewal_settings
        input_["reservation_id"] = reservation_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_sdi_source(
        self,
        sdi_source_id: "aws_sdk_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        mode: Optional["aws_sdk_medialive.types.sdi_source_mode.SdiSourceMode"] = None,
        name: Optional["aws_sdk_medialive.types.__string.__string"] = None,
        type: Optional["aws_sdk_medialive.types.sdi_source_type.SdiSourceType"] = None,
    ) -> "aws_sdk_medialive.types.update_sdi_source_response.UpdateSdiSourceResponse":
        """Change some of the settings in an SdiSource.

        Args:
            mode: Include this parameter only if you want to change the name of the SdiSource. Specify a name that is unique in the AWS account. We recommend you assign a name that describes the source, for example curling-cameraA. Names are case-sensitive.
            name: Include this parameter only if you want to change the name of the SdiSource. Specify a name that is unique in the AWS account. We recommend you assign a name that describes the source, for example curling-cameraA. Names are case-sensitive.
            sdi_source_id: The ID of the SdiSource
            type: Include this parameter only if you want to change the mode. Specify the type of the SDI source: SINGLE: The source is a single-link source. QUAD: The source is one part of a quad-link source.

        Raises:
            aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            aws_sdk_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            aws_sdk_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            aws_sdk_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            aws_sdk_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medialive.types.update_sdi_source_request.UpdateSdiSourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_medialive.types.update_sdi_source_response.UpdateSdiSourceResponse"
        ]:
            import aws_sdk_medialive._operations.media_live.update_sdi_source

            output, http_response = (
                aws_sdk_medialive._operations.media_live.update_sdi_source.update_sdi_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medialive.types.update_sdi_source_request.UpdateSdiSourceRequest = {}  # type: ignore[typeddict-item]
        if mode is not None:
            input_["mode"] = mode
        if name is not None:
            input_["name"] = name
        input_["sdi_source_id"] = sdi_source_id
        if type is not None:
            input_["type"] = type

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
