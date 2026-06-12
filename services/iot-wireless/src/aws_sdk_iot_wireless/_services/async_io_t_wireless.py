"""Generated from Smithy shape ``com.amazonaws.iotwireless#iotwireless``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_iot_wireless._auth._signers
import aws_sdk_iot_wireless._auth._sigv4
from aws_sdk_iot_wireless._auth._identity import Credentials
from aws_sdk_iot_wireless._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_iot_wireless._auth._zapros_handler import AuthMiddleware
from aws_sdk_iot_wireless._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.advanced_configuration
    import aws_sdk_iot_wireless.types.amazon_resource_name
    import aws_sdk_iot_wireless.types.associate_aws_account_with_partner_account_request
    import aws_sdk_iot_wireless.types.associate_aws_account_with_partner_account_response
    import aws_sdk_iot_wireless.types.associate_multicast_group_with_fuota_task_request
    import aws_sdk_iot_wireless.types.associate_multicast_group_with_fuota_task_response
    import aws_sdk_iot_wireless.types.associate_wireless_device_with_fuota_task_request
    import aws_sdk_iot_wireless.types.associate_wireless_device_with_fuota_task_response
    import aws_sdk_iot_wireless.types.associate_wireless_device_with_multicast_group_request
    import aws_sdk_iot_wireless.types.associate_wireless_device_with_multicast_group_response
    import aws_sdk_iot_wireless.types.associate_wireless_device_with_thing_request
    import aws_sdk_iot_wireless.types.associate_wireless_device_with_thing_response
    import aws_sdk_iot_wireless.types.associate_wireless_gateway_with_certificate_request
    import aws_sdk_iot_wireless.types.associate_wireless_gateway_with_certificate_response
    import aws_sdk_iot_wireless.types.associate_wireless_gateway_with_thing_request
    import aws_sdk_iot_wireless.types.associate_wireless_gateway_with_thing_response
    import aws_sdk_iot_wireless.types.auto_create_tasks
    import aws_sdk_iot_wireless.types.cancel_multicast_group_session_request
    import aws_sdk_iot_wireless.types.cancel_multicast_group_session_response
    import aws_sdk_iot_wireless.types.cell_towers
    import aws_sdk_iot_wireless.types.client_request_token
    import aws_sdk_iot_wireless.types.connection_status_event_configuration
    import aws_sdk_iot_wireless.types.connection_status_resource_type_event_configuration
    import aws_sdk_iot_wireless.types.create_destination_request
    import aws_sdk_iot_wireless.types.create_destination_response
    import aws_sdk_iot_wireless.types.create_device_profile_request
    import aws_sdk_iot_wireless.types.create_device_profile_response
    import aws_sdk_iot_wireless.types.create_fuota_task_request
    import aws_sdk_iot_wireless.types.create_fuota_task_response
    import aws_sdk_iot_wireless.types.create_multicast_group_request
    import aws_sdk_iot_wireless.types.create_multicast_group_response
    import aws_sdk_iot_wireless.types.create_network_analyzer_configuration_request
    import aws_sdk_iot_wireless.types.create_network_analyzer_configuration_response
    import aws_sdk_iot_wireless.types.create_service_profile_request
    import aws_sdk_iot_wireless.types.create_service_profile_response
    import aws_sdk_iot_wireless.types.create_wireless_device_request
    import aws_sdk_iot_wireless.types.create_wireless_device_response
    import aws_sdk_iot_wireless.types.create_wireless_gateway_request
    import aws_sdk_iot_wireless.types.create_wireless_gateway_response
    import aws_sdk_iot_wireless.types.create_wireless_gateway_task_definition_request
    import aws_sdk_iot_wireless.types.create_wireless_gateway_task_definition_response
    import aws_sdk_iot_wireless.types.create_wireless_gateway_task_request
    import aws_sdk_iot_wireless.types.create_wireless_gateway_task_response
    import aws_sdk_iot_wireless.types.creation_date
    import aws_sdk_iot_wireless.types.delete_destination_request
    import aws_sdk_iot_wireless.types.delete_destination_response
    import aws_sdk_iot_wireless.types.delete_device_profile_request
    import aws_sdk_iot_wireless.types.delete_device_profile_response
    import aws_sdk_iot_wireless.types.delete_fuota_task_request
    import aws_sdk_iot_wireless.types.delete_fuota_task_response
    import aws_sdk_iot_wireless.types.delete_multicast_group_request
    import aws_sdk_iot_wireless.types.delete_multicast_group_response
    import aws_sdk_iot_wireless.types.delete_network_analyzer_configuration_request
    import aws_sdk_iot_wireless.types.delete_network_analyzer_configuration_response
    import aws_sdk_iot_wireless.types.delete_queued_messages_request
    import aws_sdk_iot_wireless.types.delete_queued_messages_response
    import aws_sdk_iot_wireless.types.delete_service_profile_request
    import aws_sdk_iot_wireless.types.delete_service_profile_response
    import aws_sdk_iot_wireless.types.delete_wireless_device_import_task_request
    import aws_sdk_iot_wireless.types.delete_wireless_device_import_task_response
    import aws_sdk_iot_wireless.types.delete_wireless_device_request
    import aws_sdk_iot_wireless.types.delete_wireless_device_response
    import aws_sdk_iot_wireless.types.delete_wireless_gateway_request
    import aws_sdk_iot_wireless.types.delete_wireless_gateway_response
    import aws_sdk_iot_wireless.types.delete_wireless_gateway_task_definition_request
    import aws_sdk_iot_wireless.types.delete_wireless_gateway_task_definition_response
    import aws_sdk_iot_wireless.types.delete_wireless_gateway_task_request
    import aws_sdk_iot_wireless.types.delete_wireless_gateway_task_response
    import aws_sdk_iot_wireless.types.deregister_wireless_device_request
    import aws_sdk_iot_wireless.types.deregister_wireless_device_response
    import aws_sdk_iot_wireless.types.description
    import aws_sdk_iot_wireless.types.destination_name
    import aws_sdk_iot_wireless.types.device_name
    import aws_sdk_iot_wireless.types.device_profile_id
    import aws_sdk_iot_wireless.types.device_profile_name
    import aws_sdk_iot_wireless.types.device_profile_type
    import aws_sdk_iot_wireless.types.device_registration_state_event_configuration
    import aws_sdk_iot_wireless.types.device_registration_state_resource_type_event_configuration
    import aws_sdk_iot_wireless.types.disassociate_aws_account_from_partner_account_request
    import aws_sdk_iot_wireless.types.disassociate_aws_account_from_partner_account_response
    import aws_sdk_iot_wireless.types.disassociate_multicast_group_from_fuota_task_request
    import aws_sdk_iot_wireless.types.disassociate_multicast_group_from_fuota_task_response
    import aws_sdk_iot_wireless.types.disassociate_wireless_device_from_fuota_task_request
    import aws_sdk_iot_wireless.types.disassociate_wireless_device_from_fuota_task_response
    import aws_sdk_iot_wireless.types.disassociate_wireless_device_from_multicast_group_request
    import aws_sdk_iot_wireless.types.disassociate_wireless_device_from_multicast_group_response
    import aws_sdk_iot_wireless.types.disassociate_wireless_device_from_thing_request
    import aws_sdk_iot_wireless.types.disassociate_wireless_device_from_thing_response
    import aws_sdk_iot_wireless.types.disassociate_wireless_gateway_from_certificate_request
    import aws_sdk_iot_wireless.types.disassociate_wireless_gateway_from_certificate_response
    import aws_sdk_iot_wireless.types.disassociate_wireless_gateway_from_thing_request
    import aws_sdk_iot_wireless.types.disassociate_wireless_gateway_from_thing_response
    import aws_sdk_iot_wireless.types.event_notification_partner_type
    import aws_sdk_iot_wireless.types.event_notification_resource_type
    import aws_sdk_iot_wireless.types.expression
    import aws_sdk_iot_wireless.types.expression_type
    import aws_sdk_iot_wireless.types.file_descriptor
    import aws_sdk_iot_wireless.types.firmware_update_image
    import aws_sdk_iot_wireless.types.firmware_update_role
    import aws_sdk_iot_wireless.types.fragment_interval_ms
    import aws_sdk_iot_wireless.types.fragment_size_bytes
    import aws_sdk_iot_wireless.types.fuota_task_id
    import aws_sdk_iot_wireless.types.fuota_task_log_option_list
    import aws_sdk_iot_wireless.types.fuota_task_name
    import aws_sdk_iot_wireless.types.gateway_max_eirp
    import aws_sdk_iot_wireless.types.geo_json_payload
    import aws_sdk_iot_wireless.types.get_destination_request
    import aws_sdk_iot_wireless.types.get_destination_response
    import aws_sdk_iot_wireless.types.get_device_profile_request
    import aws_sdk_iot_wireless.types.get_device_profile_response
    import aws_sdk_iot_wireless.types.get_event_configuration_by_resource_types_request
    import aws_sdk_iot_wireless.types.get_event_configuration_by_resource_types_response
    import aws_sdk_iot_wireless.types.get_fuota_task_request
    import aws_sdk_iot_wireless.types.get_fuota_task_response
    import aws_sdk_iot_wireless.types.get_log_levels_by_resource_types_request
    import aws_sdk_iot_wireless.types.get_log_levels_by_resource_types_response
    import aws_sdk_iot_wireless.types.get_metric_configuration_request
    import aws_sdk_iot_wireless.types.get_metric_configuration_response
    import aws_sdk_iot_wireless.types.get_metrics_request
    import aws_sdk_iot_wireless.types.get_metrics_response
    import aws_sdk_iot_wireless.types.get_multicast_group_request
    import aws_sdk_iot_wireless.types.get_multicast_group_response
    import aws_sdk_iot_wireless.types.get_multicast_group_session_request
    import aws_sdk_iot_wireless.types.get_multicast_group_session_response
    import aws_sdk_iot_wireless.types.get_network_analyzer_configuration_request
    import aws_sdk_iot_wireless.types.get_network_analyzer_configuration_response
    import aws_sdk_iot_wireless.types.get_partner_account_request
    import aws_sdk_iot_wireless.types.get_partner_account_response
    import aws_sdk_iot_wireless.types.get_position_configuration_request
    import aws_sdk_iot_wireless.types.get_position_configuration_response
    import aws_sdk_iot_wireless.types.get_position_estimate_request
    import aws_sdk_iot_wireless.types.get_position_estimate_response
    import aws_sdk_iot_wireless.types.get_position_request
    import aws_sdk_iot_wireless.types.get_position_response
    import aws_sdk_iot_wireless.types.get_resource_event_configuration_request
    import aws_sdk_iot_wireless.types.get_resource_event_configuration_response
    import aws_sdk_iot_wireless.types.get_resource_log_level_request
    import aws_sdk_iot_wireless.types.get_resource_log_level_response
    import aws_sdk_iot_wireless.types.get_resource_position_request
    import aws_sdk_iot_wireless.types.get_resource_position_response
    import aws_sdk_iot_wireless.types.get_service_endpoint_request
    import aws_sdk_iot_wireless.types.get_service_endpoint_response
    import aws_sdk_iot_wireless.types.get_service_profile_request
    import aws_sdk_iot_wireless.types.get_service_profile_response
    import aws_sdk_iot_wireless.types.get_wireless_device_import_task_request
    import aws_sdk_iot_wireless.types.get_wireless_device_import_task_response
    import aws_sdk_iot_wireless.types.get_wireless_device_request
    import aws_sdk_iot_wireless.types.get_wireless_device_response
    import aws_sdk_iot_wireless.types.get_wireless_device_statistics_request
    import aws_sdk_iot_wireless.types.get_wireless_device_statistics_response
    import aws_sdk_iot_wireless.types.get_wireless_gateway_certificate_request
    import aws_sdk_iot_wireless.types.get_wireless_gateway_certificate_response
    import aws_sdk_iot_wireless.types.get_wireless_gateway_firmware_information_request
    import aws_sdk_iot_wireless.types.get_wireless_gateway_firmware_information_response
    import aws_sdk_iot_wireless.types.get_wireless_gateway_request
    import aws_sdk_iot_wireless.types.get_wireless_gateway_response
    import aws_sdk_iot_wireless.types.get_wireless_gateway_statistics_request
    import aws_sdk_iot_wireless.types.get_wireless_gateway_statistics_response
    import aws_sdk_iot_wireless.types.get_wireless_gateway_task_definition_request
    import aws_sdk_iot_wireless.types.get_wireless_gateway_task_definition_response
    import aws_sdk_iot_wireless.types.get_wireless_gateway_task_request
    import aws_sdk_iot_wireless.types.get_wireless_gateway_task_response
    import aws_sdk_iot_wireless.types.gnss
    import aws_sdk_iot_wireless.types.identifier
    import aws_sdk_iot_wireless.types.identifier_type
    import aws_sdk_iot_wireless.types.import_task_id
    import aws_sdk_iot_wireless.types.iot_certificate_id
    import aws_sdk_iot_wireless.types.ip
    import aws_sdk_iot_wireless.types.join_eui_filters
    import aws_sdk_iot_wireless.types.join_event_configuration
    import aws_sdk_iot_wireless.types.join_resource_type_event_configuration
    import aws_sdk_iot_wireless.types.list_destinations_request
    import aws_sdk_iot_wireless.types.list_destinations_response
    import aws_sdk_iot_wireless.types.list_device_profiles_request
    import aws_sdk_iot_wireless.types.list_device_profiles_response
    import aws_sdk_iot_wireless.types.list_devices_for_wireless_device_import_task_request
    import aws_sdk_iot_wireless.types.list_devices_for_wireless_device_import_task_response
    import aws_sdk_iot_wireless.types.list_event_configurations_request
    import aws_sdk_iot_wireless.types.list_event_configurations_response
    import aws_sdk_iot_wireless.types.list_fuota_tasks_request
    import aws_sdk_iot_wireless.types.list_fuota_tasks_response
    import aws_sdk_iot_wireless.types.list_multicast_groups_by_fuota_task_request
    import aws_sdk_iot_wireless.types.list_multicast_groups_by_fuota_task_response
    import aws_sdk_iot_wireless.types.list_multicast_groups_request
    import aws_sdk_iot_wireless.types.list_multicast_groups_response
    import aws_sdk_iot_wireless.types.list_network_analyzer_configurations_request
    import aws_sdk_iot_wireless.types.list_network_analyzer_configurations_response
    import aws_sdk_iot_wireless.types.list_partner_accounts_request
    import aws_sdk_iot_wireless.types.list_partner_accounts_response
    import aws_sdk_iot_wireless.types.list_position_configurations_request
    import aws_sdk_iot_wireless.types.list_position_configurations_response
    import aws_sdk_iot_wireless.types.list_queued_messages_request
    import aws_sdk_iot_wireless.types.list_queued_messages_response
    import aws_sdk_iot_wireless.types.list_service_profiles_request
    import aws_sdk_iot_wireless.types.list_service_profiles_response
    import aws_sdk_iot_wireless.types.list_tags_for_resource_request
    import aws_sdk_iot_wireless.types.list_tags_for_resource_response
    import aws_sdk_iot_wireless.types.list_wireless_device_import_tasks_request
    import aws_sdk_iot_wireless.types.list_wireless_device_import_tasks_response
    import aws_sdk_iot_wireless.types.list_wireless_devices_request
    import aws_sdk_iot_wireless.types.list_wireless_devices_response
    import aws_sdk_iot_wireless.types.list_wireless_gateway_task_definitions_request
    import aws_sdk_iot_wireless.types.list_wireless_gateway_task_definitions_response
    import aws_sdk_iot_wireless.types.list_wireless_gateways_request
    import aws_sdk_iot_wireless.types.list_wireless_gateways_response
    import aws_sdk_iot_wireless.types.lo_ra_wan_device
    import aws_sdk_iot_wireless.types.lo_ra_wan_device_profile
    import aws_sdk_iot_wireless.types.lo_ra_wan_fuota_task
    import aws_sdk_iot_wireless.types.lo_ra_wan_gateway
    import aws_sdk_iot_wireless.types.lo_ra_wan_multicast
    import aws_sdk_iot_wireless.types.lo_ra_wan_multicast_session
    import aws_sdk_iot_wireless.types.lo_ra_wan_service_profile
    import aws_sdk_iot_wireless.types.lo_ra_wan_start_fuota_task
    import aws_sdk_iot_wireless.types.lo_ra_wan_update_device
    import aws_sdk_iot_wireless.types.log_level
    import aws_sdk_iot_wireless.types.max_results
    import aws_sdk_iot_wireless.types.message_delivery_status_event_configuration
    import aws_sdk_iot_wireless.types.message_delivery_status_resource_type_event_configuration
    import aws_sdk_iot_wireless.types.message_id
    import aws_sdk_iot_wireless.types.multicast_group_id
    import aws_sdk_iot_wireless.types.multicast_group_name
    import aws_sdk_iot_wireless.types.multicast_wireless_metadata
    import aws_sdk_iot_wireless.types.net_id_filters
    import aws_sdk_iot_wireless.types.network_analyzer_configuration_name
    import aws_sdk_iot_wireless.types.network_analyzer_multicast_group_list
    import aws_sdk_iot_wireless.types.next_token
    import aws_sdk_iot_wireless.types.onboard_status
    import aws_sdk_iot_wireless.types.partner_account_id
    import aws_sdk_iot_wireless.types.partner_type
    import aws_sdk_iot_wireless.types.payload_data
    import aws_sdk_iot_wireless.types.position_coordinate
    import aws_sdk_iot_wireless.types.position_resource_identifier
    import aws_sdk_iot_wireless.types.position_resource_type
    import aws_sdk_iot_wireless.types.position_solver_configurations
    import aws_sdk_iot_wireless.types.positioning_config_status
    import aws_sdk_iot_wireless.types.proximity_event_configuration
    import aws_sdk_iot_wireless.types.proximity_resource_type_event_configuration
    import aws_sdk_iot_wireless.types.put_position_configuration_request
    import aws_sdk_iot_wireless.types.put_position_configuration_response
    import aws_sdk_iot_wireless.types.put_resource_log_level_request
    import aws_sdk_iot_wireless.types.put_resource_log_level_response
    import aws_sdk_iot_wireless.types.query_string
    import aws_sdk_iot_wireless.types.redundancy_percent
    import aws_sdk_iot_wireless.types.reset_all_resource_log_levels_request
    import aws_sdk_iot_wireless.types.reset_all_resource_log_levels_response
    import aws_sdk_iot_wireless.types.reset_resource_log_level_request
    import aws_sdk_iot_wireless.types.reset_resource_log_level_response
    import aws_sdk_iot_wireless.types.resource_identifier
    import aws_sdk_iot_wireless.types.resource_type
    import aws_sdk_iot_wireless.types.role_arn
    import aws_sdk_iot_wireless.types.send_data_to_multicast_group_request
    import aws_sdk_iot_wireless.types.send_data_to_multicast_group_response
    import aws_sdk_iot_wireless.types.send_data_to_wireless_device_request
    import aws_sdk_iot_wireless.types.send_data_to_wireless_device_response
    import aws_sdk_iot_wireless.types.service_profile_id
    import aws_sdk_iot_wireless.types.service_profile_name
    import aws_sdk_iot_wireless.types.sidewalk_account_info
    import aws_sdk_iot_wireless.types.sidewalk_create_device_profile
    import aws_sdk_iot_wireless.types.sidewalk_create_wireless_device
    import aws_sdk_iot_wireless.types.sidewalk_single_start_import_info
    import aws_sdk_iot_wireless.types.sidewalk_start_import_info
    import aws_sdk_iot_wireless.types.sidewalk_update_account
    import aws_sdk_iot_wireless.types.sidewalk_update_import_info
    import aws_sdk_iot_wireless.types.sidewalk_update_wireless_device
    import aws_sdk_iot_wireless.types.start_bulk_associate_wireless_device_with_multicast_group_request
    import aws_sdk_iot_wireless.types.start_bulk_associate_wireless_device_with_multicast_group_response
    import aws_sdk_iot_wireless.types.start_bulk_disassociate_wireless_device_from_multicast_group_request
    import aws_sdk_iot_wireless.types.start_bulk_disassociate_wireless_device_from_multicast_group_response
    import aws_sdk_iot_wireless.types.start_fuota_task_request
    import aws_sdk_iot_wireless.types.start_fuota_task_response
    import aws_sdk_iot_wireless.types.start_multicast_group_session_request
    import aws_sdk_iot_wireless.types.start_multicast_group_session_response
    import aws_sdk_iot_wireless.types.start_single_wireless_device_import_task_request
    import aws_sdk_iot_wireless.types.start_single_wireless_device_import_task_response
    import aws_sdk_iot_wireless.types.start_wireless_device_import_task_request
    import aws_sdk_iot_wireless.types.start_wireless_device_import_task_response
    import aws_sdk_iot_wireless.types.summary_metric_configuration
    import aws_sdk_iot_wireless.types.summary_metric_queries
    import aws_sdk_iot_wireless.types.tag_key_list
    import aws_sdk_iot_wireless.types.tag_list
    import aws_sdk_iot_wireless.types.tag_resource_request
    import aws_sdk_iot_wireless.types.tag_resource_response
    import aws_sdk_iot_wireless.types.test_wireless_device_request
    import aws_sdk_iot_wireless.types.test_wireless_device_response
    import aws_sdk_iot_wireless.types.thing_arn
    import aws_sdk_iot_wireless.types.trace_content
    import aws_sdk_iot_wireless.types.transmit_mode
    import aws_sdk_iot_wireless.types.untag_resource_request
    import aws_sdk_iot_wireless.types.untag_resource_response
    import aws_sdk_iot_wireless.types.update_destination_request
    import aws_sdk_iot_wireless.types.update_destination_response
    import aws_sdk_iot_wireless.types.update_event_configuration_by_resource_types_request
    import aws_sdk_iot_wireless.types.update_event_configuration_by_resource_types_response
    import aws_sdk_iot_wireless.types.update_fuota_task_request
    import aws_sdk_iot_wireless.types.update_fuota_task_response
    import aws_sdk_iot_wireless.types.update_log_levels_by_resource_types_request
    import aws_sdk_iot_wireless.types.update_log_levels_by_resource_types_response
    import aws_sdk_iot_wireless.types.update_metric_configuration_request
    import aws_sdk_iot_wireless.types.update_metric_configuration_response
    import aws_sdk_iot_wireless.types.update_multicast_group_request
    import aws_sdk_iot_wireless.types.update_multicast_group_response
    import aws_sdk_iot_wireless.types.update_network_analyzer_configuration_request
    import aws_sdk_iot_wireless.types.update_network_analyzer_configuration_response
    import aws_sdk_iot_wireless.types.update_partner_account_request
    import aws_sdk_iot_wireless.types.update_partner_account_response
    import aws_sdk_iot_wireless.types.update_position_request
    import aws_sdk_iot_wireless.types.update_position_response
    import aws_sdk_iot_wireless.types.update_resource_event_configuration_request
    import aws_sdk_iot_wireless.types.update_resource_event_configuration_response
    import aws_sdk_iot_wireless.types.update_resource_position_request
    import aws_sdk_iot_wireless.types.update_resource_position_response
    import aws_sdk_iot_wireless.types.update_wireless_device_import_task_request
    import aws_sdk_iot_wireless.types.update_wireless_device_import_task_response
    import aws_sdk_iot_wireless.types.update_wireless_device_request
    import aws_sdk_iot_wireless.types.update_wireless_device_response
    import aws_sdk_iot_wireless.types.update_wireless_gateway_request
    import aws_sdk_iot_wireless.types.update_wireless_gateway_response
    import aws_sdk_iot_wireless.types.update_wireless_gateway_task_create
    import aws_sdk_iot_wireless.types.wi_fi_access_points
    import aws_sdk_iot_wireless.types.wireless_device_id
    import aws_sdk_iot_wireless.types.wireless_device_id_type
    import aws_sdk_iot_wireless.types.wireless_device_list
    import aws_sdk_iot_wireless.types.wireless_device_log_option_list
    import aws_sdk_iot_wireless.types.wireless_device_name
    import aws_sdk_iot_wireless.types.wireless_device_type
    import aws_sdk_iot_wireless.types.wireless_gateway_id
    import aws_sdk_iot_wireless.types.wireless_gateway_id_type
    import aws_sdk_iot_wireless.types.wireless_gateway_list
    import aws_sdk_iot_wireless.types.wireless_gateway_log_option_list
    import aws_sdk_iot_wireless.types.wireless_gateway_name
    import aws_sdk_iot_wireless.types.wireless_gateway_service_type
    import aws_sdk_iot_wireless.types.wireless_gateway_task_definition_id
    import aws_sdk_iot_wireless.types.wireless_gateway_task_definition_type
    import aws_sdk_iot_wireless.types.wireless_gateway_task_name
    import aws_sdk_iot_wireless.types.wireless_metadata


class AsyncIoTWirelessClientConfig(TypedDict, total=False):
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


class AsyncIoTWirelessClient:
    """A client for the ``IoTWireless`` service.

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
        self.config = AsyncIoTWirelessClientConfig(
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
        self, config_overrides: Optional[AsyncIoTWirelessClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncIoTWirelessClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self.config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            region=overrides.get("region", self.config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self.config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def associate_aws_account_with_partner_account(
        self,
        sidewalk: "aws_sdk_iot_wireless.types.sidewalk_account_info.SidewalkAccountInfo",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        client_request_token: Optional[
            "aws_sdk_iot_wireless.types.client_request_token.ClientRequestToken"
        ] = None,
        tags: Optional["aws_sdk_iot_wireless.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_iot_wireless.types.associate_aws_account_with_partner_account_response.AssociateAwsAccountWithPartnerAccountResponse":
        """<p>Associates a partner account with your AWS account.</p>

        Args:
            sidewalk: <p>The Sidewalk account credentials.</p>
            client_request_token: <p>Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency in Amazon EC2 API requests</a>.</p>
            tags: <p>The tags to attach to the specified resource. Tags are metadata that you can use to manage a resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.associate_aws_account_with_partner_account_request.AssociateAwsAccountWithPartnerAccountRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.associate_aws_account_with_partner_account_response.AssociateAwsAccountWithPartnerAccountResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.associate_aws_account_with_partner_account

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.associate_aws_account_with_partner_account.async_associate_aws_account_with_partner_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.associate_aws_account_with_partner_account_request.AssociateAwsAccountWithPartnerAccountRequest = {}  # type: ignore[typeddict-item]
        input["sidewalk"] = sidewalk
        if client_request_token is not None:
            input["client_request_token"] = client_request_token
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_multicast_group_with_fuota_task(
        self,
        id: "aws_sdk_iot_wireless.types.fuota_task_id.FuotaTaskId",
        multicast_group_id: "aws_sdk_iot_wireless.types.multicast_group_id.MulticastGroupId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.associate_multicast_group_with_fuota_task_response.AssociateMulticastGroupWithFuotaTaskResponse":
        """<p>Associate a multicast group with a FUOTA task.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.associate_multicast_group_with_fuota_task_request.AssociateMulticastGroupWithFuotaTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.associate_multicast_group_with_fuota_task_response.AssociateMulticastGroupWithFuotaTaskResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.associate_multicast_group_with_fuota_task

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.associate_multicast_group_with_fuota_task.async_associate_multicast_group_with_fuota_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.associate_multicast_group_with_fuota_task_request.AssociateMulticastGroupWithFuotaTaskRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        input["multicast_group_id"] = multicast_group_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_wireless_device_with_fuota_task(
        self,
        id: "aws_sdk_iot_wireless.types.fuota_task_id.FuotaTaskId",
        wireless_device_id: "aws_sdk_iot_wireless.types.wireless_device_id.WirelessDeviceId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.associate_wireless_device_with_fuota_task_response.AssociateWirelessDeviceWithFuotaTaskResponse":
        """<p>Associate a wireless device with a FUOTA task.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.associate_wireless_device_with_fuota_task_request.AssociateWirelessDeviceWithFuotaTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.associate_wireless_device_with_fuota_task_response.AssociateWirelessDeviceWithFuotaTaskResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.associate_wireless_device_with_fuota_task

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.associate_wireless_device_with_fuota_task.async_associate_wireless_device_with_fuota_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.associate_wireless_device_with_fuota_task_request.AssociateWirelessDeviceWithFuotaTaskRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        input["wireless_device_id"] = wireless_device_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_wireless_device_with_multicast_group(
        self,
        id: "aws_sdk_iot_wireless.types.multicast_group_id.MulticastGroupId",
        wireless_device_id: "aws_sdk_iot_wireless.types.wireless_device_id.WirelessDeviceId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.associate_wireless_device_with_multicast_group_response.AssociateWirelessDeviceWithMulticastGroupResponse":
        """<p>Associates a wireless device with a multicast group.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.associate_wireless_device_with_multicast_group_request.AssociateWirelessDeviceWithMulticastGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.associate_wireless_device_with_multicast_group_response.AssociateWirelessDeviceWithMulticastGroupResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.associate_wireless_device_with_multicast_group

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.associate_wireless_device_with_multicast_group.async_associate_wireless_device_with_multicast_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.associate_wireless_device_with_multicast_group_request.AssociateWirelessDeviceWithMulticastGroupRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        input["wireless_device_id"] = wireless_device_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_wireless_device_with_thing(
        self,
        id: "aws_sdk_iot_wireless.types.wireless_device_id.WirelessDeviceId",
        thing_arn: "aws_sdk_iot_wireless.types.thing_arn.ThingArn",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.associate_wireless_device_with_thing_response.AssociateWirelessDeviceWithThingResponse":
        """<p>Associates a wireless device with a thing.</p>

        Args:
            id: <p>The ID of the resource to update.</p>
            thing_arn: <p>The ARN of the thing to associate with the wireless device.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.associate_wireless_device_with_thing_request.AssociateWirelessDeviceWithThingRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.associate_wireless_device_with_thing_response.AssociateWirelessDeviceWithThingResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.associate_wireless_device_with_thing

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.associate_wireless_device_with_thing.async_associate_wireless_device_with_thing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.associate_wireless_device_with_thing_request.AssociateWirelessDeviceWithThingRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        input["thing_arn"] = thing_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_wireless_gateway_with_certificate(
        self,
        id: "aws_sdk_iot_wireless.types.wireless_gateway_id.WirelessGatewayId",
        iot_certificate_id: "aws_sdk_iot_wireless.types.iot_certificate_id.IotCertificateId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.associate_wireless_gateway_with_certificate_response.AssociateWirelessGatewayWithCertificateResponse":
        """<p>Associates a wireless gateway with a certificate.</p>

        Args:
            id: <p>The ID of the resource to update.</p>
            iot_certificate_id: <p>The ID of the certificate to associate with the wireless gateway.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.associate_wireless_gateway_with_certificate_request.AssociateWirelessGatewayWithCertificateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.associate_wireless_gateway_with_certificate_response.AssociateWirelessGatewayWithCertificateResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.associate_wireless_gateway_with_certificate

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.associate_wireless_gateway_with_certificate.async_associate_wireless_gateway_with_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.associate_wireless_gateway_with_certificate_request.AssociateWirelessGatewayWithCertificateRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        input["iot_certificate_id"] = iot_certificate_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_wireless_gateway_with_thing(
        self,
        id: "aws_sdk_iot_wireless.types.wireless_gateway_id.WirelessGatewayId",
        thing_arn: "aws_sdk_iot_wireless.types.thing_arn.ThingArn",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.associate_wireless_gateway_with_thing_response.AssociateWirelessGatewayWithThingResponse":
        """<p>Associates a wireless gateway with a thing.</p>

        Args:
            id: <p>The ID of the resource to update.</p>
            thing_arn: <p>The ARN of the thing to associate with the wireless gateway.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.associate_wireless_gateway_with_thing_request.AssociateWirelessGatewayWithThingRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.associate_wireless_gateway_with_thing_response.AssociateWirelessGatewayWithThingResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.associate_wireless_gateway_with_thing

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.associate_wireless_gateway_with_thing.async_associate_wireless_gateway_with_thing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.associate_wireless_gateway_with_thing_request.AssociateWirelessGatewayWithThingRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        input["thing_arn"] = thing_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_multicast_group_session(
        self,
        id: "aws_sdk_iot_wireless.types.multicast_group_id.MulticastGroupId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.cancel_multicast_group_session_response.CancelMulticastGroupSessionResponse":
        """<p>Cancels an existing multicast group session.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.cancel_multicast_group_session_request.CancelMulticastGroupSessionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.cancel_multicast_group_session_response.CancelMulticastGroupSessionResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.cancel_multicast_group_session

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.cancel_multicast_group_session.async_cancel_multicast_group_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.cancel_multicast_group_session_request.CancelMulticastGroupSessionRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_destination(
        self,
        name: "aws_sdk_iot_wireless.types.destination_name.DestinationName",
        expression_type: "aws_sdk_iot_wireless.types.expression_type.ExpressionType",
        expression: "aws_sdk_iot_wireless.types.expression.Expression",
        role_arn: "aws_sdk_iot_wireless.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        description: Optional[
            "aws_sdk_iot_wireless.types.description.Description"
        ] = None,
        tags: Optional["aws_sdk_iot_wireless.types.tag_list.TagList"] = None,
        client_request_token: Optional[
            "aws_sdk_iot_wireless.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.create_destination_response.CreateDestinationResponse":
        """<p>Creates a new destination that maps a device message to an AWS IoT rule.</p>

        Args:
            name: <p>The name of the new resource.</p>
            expression_type: <p>The type of value in <code>Expression</code>.</p>
            expression: <p>The rule name or topic rule to send messages to.</p>
            description: <p>The description of the new resource.</p>
            role_arn: <p>The ARN of the IAM Role that authorizes the destination.</p>
            tags: <p>The tags to attach to the new destination. Tags are metadata that you can use to manage a resource.</p>
            client_request_token: <p>Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency in Amazon EC2 API requests</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.create_destination_request.CreateDestinationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.create_destination_response.CreateDestinationResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.create_destination

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.create_destination.async_create_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.create_destination_request.CreateDestinationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["expression_type"] = expression_type
        input["expression"] = expression
        if description is not None:
            input["description"] = description
        input["role_arn"] = role_arn
        if tags is not None:
            input["tags"] = tags
        if client_request_token is not None:
            input["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_device_profile(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        name: Optional[
            "aws_sdk_iot_wireless.types.device_profile_name.DeviceProfileName"
        ] = None,
        lo_ra_wan: Optional[
            "aws_sdk_iot_wireless.types.lo_ra_wan_device_profile.LoRaWANDeviceProfile"
        ] = None,
        tags: Optional["aws_sdk_iot_wireless.types.tag_list.TagList"] = None,
        client_request_token: Optional[
            "aws_sdk_iot_wireless.types.client_request_token.ClientRequestToken"
        ] = None,
        sidewalk: Optional[
            "aws_sdk_iot_wireless.types.sidewalk_create_device_profile.SidewalkCreateDeviceProfile"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.create_device_profile_response.CreateDeviceProfileResponse":
        """<p>Creates a new device profile.</p>

        Args:
            name: <p>The name of the new resource.</p> <note> <p>The following special characters aren't accepted: <code><>^#~$</code> </p> </note>
            lo_ra_wan: <p>The device profile information to use to create the device profile.</p>
            tags: <p>The tags to attach to the new device profile. Tags are metadata that you can use to manage a resource.</p>
            client_request_token: <p>Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency in Amazon EC2 API requests</a>.</p>
            sidewalk: <p>The Sidewalk-related information for creating the Sidewalk device profile.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.create_device_profile_request.CreateDeviceProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.create_device_profile_response.CreateDeviceProfileResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.create_device_profile

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.create_device_profile.async_create_device_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.create_device_profile_request.CreateDeviceProfileRequest = {}  # type: ignore[typeddict-item]
        if name is not None:
            input["name"] = name
        if lo_ra_wan is not None:
            input["lo_ra_wan"] = lo_ra_wan
        if tags is not None:
            input["tags"] = tags
        if client_request_token is not None:
            input["client_request_token"] = client_request_token
        if sidewalk is not None:
            input["sidewalk"] = sidewalk

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_fuota_task(
        self,
        firmware_update_image: "aws_sdk_iot_wireless.types.firmware_update_image.FirmwareUpdateImage",
        firmware_update_role: "aws_sdk_iot_wireless.types.firmware_update_role.FirmwareUpdateRole",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        name: Optional[
            "aws_sdk_iot_wireless.types.fuota_task_name.FuotaTaskName"
        ] = None,
        description: Optional[
            "aws_sdk_iot_wireless.types.description.Description"
        ] = None,
        client_request_token: Optional[
            "aws_sdk_iot_wireless.types.client_request_token.ClientRequestToken"
        ] = None,
        lo_ra_wan: Optional[
            "aws_sdk_iot_wireless.types.lo_ra_wan_fuota_task.LoRaWANFuotaTask"
        ] = None,
        tags: Optional["aws_sdk_iot_wireless.types.tag_list.TagList"] = None,
        redundancy_percent: Optional[
            "aws_sdk_iot_wireless.types.redundancy_percent.RedundancyPercent"
        ] = None,
        fragment_size_bytes: Optional[
            "aws_sdk_iot_wireless.types.fragment_size_bytes.FragmentSizeBytes"
        ] = None,
        fragment_interval_ms: Optional[
            "aws_sdk_iot_wireless.types.fragment_interval_ms.FragmentIntervalMS"
        ] = None,
        descriptor: Optional[
            "aws_sdk_iot_wireless.types.file_descriptor.FileDescriptor"
        ] = None,
    ) -> (
        "aws_sdk_iot_wireless.types.create_fuota_task_response.CreateFuotaTaskResponse"
    ):
        """<p>Creates a FUOTA task.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.create_fuota_task_request.CreateFuotaTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.create_fuota_task_response.CreateFuotaTaskResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.create_fuota_task

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.create_fuota_task.async_create_fuota_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.create_fuota_task_request.CreateFuotaTaskRequest = {}  # type: ignore[typeddict-item]
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if client_request_token is not None:
            input["client_request_token"] = client_request_token
        if lo_ra_wan is not None:
            input["lo_ra_wan"] = lo_ra_wan
        input["firmware_update_image"] = firmware_update_image
        input["firmware_update_role"] = firmware_update_role
        if tags is not None:
            input["tags"] = tags
        if redundancy_percent is not None:
            input["redundancy_percent"] = redundancy_percent
        if fragment_size_bytes is not None:
            input["fragment_size_bytes"] = fragment_size_bytes
        if fragment_interval_ms is not None:
            input["fragment_interval_ms"] = fragment_interval_ms
        if descriptor is not None:
            input["descriptor"] = descriptor

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_multicast_group(
        self,
        lo_ra_wan: "aws_sdk_iot_wireless.types.lo_ra_wan_multicast.LoRaWANMulticast",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        name: Optional[
            "aws_sdk_iot_wireless.types.multicast_group_name.MulticastGroupName"
        ] = None,
        description: Optional[
            "aws_sdk_iot_wireless.types.description.Description"
        ] = None,
        client_request_token: Optional[
            "aws_sdk_iot_wireless.types.client_request_token.ClientRequestToken"
        ] = None,
        tags: Optional["aws_sdk_iot_wireless.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_iot_wireless.types.create_multicast_group_response.CreateMulticastGroupResponse":
        """<p>Creates a multicast group.</p>

        Args:
            description: <p>The description of the multicast group.</p>
            client_request_token: <p>Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency in Amazon EC2 API requests</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.create_multicast_group_request.CreateMulticastGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.create_multicast_group_response.CreateMulticastGroupResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.create_multicast_group

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.create_multicast_group.async_create_multicast_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.create_multicast_group_request.CreateMulticastGroupRequest = {}  # type: ignore[typeddict-item]
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if client_request_token is not None:
            input["client_request_token"] = client_request_token
        input["lo_ra_wan"] = lo_ra_wan
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_network_analyzer_configuration(
        self,
        name: "aws_sdk_iot_wireless.types.network_analyzer_configuration_name.NetworkAnalyzerConfigurationName",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        trace_content: Optional[
            "aws_sdk_iot_wireless.types.trace_content.TraceContent"
        ] = None,
        wireless_devices: Optional[
            "aws_sdk_iot_wireless.types.wireless_device_list.WirelessDeviceList"
        ] = None,
        wireless_gateways: Optional[
            "aws_sdk_iot_wireless.types.wireless_gateway_list.WirelessGatewayList"
        ] = None,
        description: Optional[
            "aws_sdk_iot_wireless.types.description.Description"
        ] = None,
        tags: Optional["aws_sdk_iot_wireless.types.tag_list.TagList"] = None,
        client_request_token: Optional[
            "aws_sdk_iot_wireless.types.client_request_token.ClientRequestToken"
        ] = None,
        multicast_groups: Optional[
            "aws_sdk_iot_wireless.types.network_analyzer_multicast_group_list.NetworkAnalyzerMulticastGroupList"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.create_network_analyzer_configuration_response.CreateNetworkAnalyzerConfigurationResponse":
        """<p>Creates a new network analyzer configuration.</p>

        Args:
            wireless_devices: <p>Wireless device resources to add to the network analyzer configuration. Provide the <code>WirelessDeviceId</code> of the resource to add in the input array.</p>
            wireless_gateways: <p>Wireless gateway resources to add to the network analyzer configuration. Provide the <code>WirelessGatewayId</code> of the resource to add in the input array.</p>
            multicast_groups: <p>Multicast Group resources to add to the network analyzer configruation. Provide the <code>MulticastGroupId</code> of the resource to add in the input array.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.create_network_analyzer_configuration_request.CreateNetworkAnalyzerConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.create_network_analyzer_configuration_response.CreateNetworkAnalyzerConfigurationResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.create_network_analyzer_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.create_network_analyzer_configuration.async_create_network_analyzer_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.create_network_analyzer_configuration_request.CreateNetworkAnalyzerConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if trace_content is not None:
            input["trace_content"] = trace_content
        if wireless_devices is not None:
            input["wireless_devices"] = wireless_devices
        if wireless_gateways is not None:
            input["wireless_gateways"] = wireless_gateways
        if description is not None:
            input["description"] = description
        if tags is not None:
            input["tags"] = tags
        if client_request_token is not None:
            input["client_request_token"] = client_request_token
        if multicast_groups is not None:
            input["multicast_groups"] = multicast_groups

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_service_profile(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        name: Optional[
            "aws_sdk_iot_wireless.types.service_profile_name.ServiceProfileName"
        ] = None,
        lo_ra_wan: Optional[
            "aws_sdk_iot_wireless.types.lo_ra_wan_service_profile.LoRaWANServiceProfile"
        ] = None,
        tags: Optional["aws_sdk_iot_wireless.types.tag_list.TagList"] = None,
        client_request_token: Optional[
            "aws_sdk_iot_wireless.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.create_service_profile_response.CreateServiceProfileResponse":
        """<p>Creates a new service profile.</p>

        Args:
            name: <p>The name of the new resource.</p> <note> <p>The following special characters aren't accepted: <code><>^#~$</code> </p> </note>
            lo_ra_wan: <p>The service profile information to use to create the service profile.</p>
            tags: <p>The tags to attach to the new service profile. Tags are metadata that you can use to manage a resource.</p>
            client_request_token: <p>Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency in Amazon EC2 API requests</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.create_service_profile_request.CreateServiceProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.create_service_profile_response.CreateServiceProfileResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.create_service_profile

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.create_service_profile.async_create_service_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.create_service_profile_request.CreateServiceProfileRequest = {}  # type: ignore[typeddict-item]
        if name is not None:
            input["name"] = name
        if lo_ra_wan is not None:
            input["lo_ra_wan"] = lo_ra_wan
        if tags is not None:
            input["tags"] = tags
        if client_request_token is not None:
            input["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_wireless_device(
        self,
        type: "aws_sdk_iot_wireless.types.wireless_device_type.WirelessDeviceType",
        destination_name: "aws_sdk_iot_wireless.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        name: Optional[
            "aws_sdk_iot_wireless.types.wireless_device_name.WirelessDeviceName"
        ] = None,
        description: Optional[
            "aws_sdk_iot_wireless.types.description.Description"
        ] = None,
        client_request_token: Optional[
            "aws_sdk_iot_wireless.types.client_request_token.ClientRequestToken"
        ] = None,
        lo_ra_wan: Optional[
            "aws_sdk_iot_wireless.types.lo_ra_wan_device.LoRaWANDevice"
        ] = None,
        tags: Optional["aws_sdk_iot_wireless.types.tag_list.TagList"] = None,
        positioning: Optional[
            "aws_sdk_iot_wireless.types.positioning_config_status.PositioningConfigStatus"
        ] = None,
        sidewalk: Optional[
            "aws_sdk_iot_wireless.types.sidewalk_create_wireless_device.SidewalkCreateWirelessDevice"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.create_wireless_device_response.CreateWirelessDeviceResponse":
        """<p>Provisions a wireless device.</p>

        Args:
            type: <p>The wireless device type.</p>
            name: <p>The name of the new resource.</p> <note> <p>The following special characters aren't accepted: <code><>^#~$</code> </p> </note>
            description: <p>The description of the new resource.</p>
            destination_name: <p>The name of the destination to assign to the new wireless device.</p>
            client_request_token: <p>Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency in Amazon EC2 API requests</a>.</p>
            lo_ra_wan: <p>The device configuration information to use to create the wireless device.</p>
            tags: <p>The tags to attach to the new wireless device. Tags are metadata that you can use to manage a resource.</p>
            positioning: <p>The integration status of the Device Location feature for LoRaWAN and Sidewalk devices.</p>
            sidewalk: <p>The device configuration information to use to create the Sidewalk device.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.create_wireless_device_request.CreateWirelessDeviceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.create_wireless_device_response.CreateWirelessDeviceResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.create_wireless_device

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.create_wireless_device.async_create_wireless_device(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.create_wireless_device_request.CreateWirelessDeviceRequest = {}  # type: ignore[typeddict-item]
        input["type"] = type
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        input["destination_name"] = destination_name
        if client_request_token is not None:
            input["client_request_token"] = client_request_token
        if lo_ra_wan is not None:
            input["lo_ra_wan"] = lo_ra_wan
        if tags is not None:
            input["tags"] = tags
        if positioning is not None:
            input["positioning"] = positioning
        if sidewalk is not None:
            input["sidewalk"] = sidewalk

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_wireless_gateway(
        self,
        lo_ra_wan: "aws_sdk_iot_wireless.types.lo_ra_wan_gateway.LoRaWANGateway",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        name: Optional[
            "aws_sdk_iot_wireless.types.wireless_gateway_name.WirelessGatewayName"
        ] = None,
        description: Optional[
            "aws_sdk_iot_wireless.types.description.Description"
        ] = None,
        tags: Optional["aws_sdk_iot_wireless.types.tag_list.TagList"] = None,
        client_request_token: Optional[
            "aws_sdk_iot_wireless.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.create_wireless_gateway_response.CreateWirelessGatewayResponse":
        """<p>Provisions a wireless gateway.</p> <note> <p>When provisioning a wireless gateway, you might run into duplication errors for the following reasons.</p> <ul> <li> <p>If you specify a <code>GatewayEui</code> value that already exists.</p> </li> <li> <p>If you used a <code>ClientRequestToken</code> with the same parameters within the last 10 minutes.</p> </li> </ul> <p>To avoid this error, make sure that you use unique identifiers and parameters for each request within the specified time period.</p> </note>

        Args:
            name: <p>The name of the new resource.</p> <note> <p>The following special characters aren't accepted: <code><>^#~$</code> </p> </note>
            description: <p>The description of the new resource.</p>
            lo_ra_wan: <p>The gateway configuration information to use to create the wireless gateway.</p>
            tags: <p>The tags to attach to the new wireless gateway. Tags are metadata that you can use to manage a resource.</p>
            client_request_token: <p>Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency in Amazon EC2 API requests</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.create_wireless_gateway_request.CreateWirelessGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.create_wireless_gateway_response.CreateWirelessGatewayResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.create_wireless_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.create_wireless_gateway.async_create_wireless_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.create_wireless_gateway_request.CreateWirelessGatewayRequest = {}  # type: ignore[typeddict-item]
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        input["lo_ra_wan"] = lo_ra_wan
        if tags is not None:
            input["tags"] = tags
        if client_request_token is not None:
            input["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_wireless_gateway_task(
        self,
        id: "aws_sdk_iot_wireless.types.wireless_gateway_id.WirelessGatewayId",
        wireless_gateway_task_definition_id: "aws_sdk_iot_wireless.types.wireless_gateway_task_definition_id.WirelessGatewayTaskDefinitionId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.create_wireless_gateway_task_response.CreateWirelessGatewayTaskResponse":
        """<p>Creates a task for a wireless gateway.</p>

        Args:
            id: <p>The ID of the resource to update.</p>
            wireless_gateway_task_definition_id: <p>The ID of the WirelessGatewayTaskDefinition.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.create_wireless_gateway_task_request.CreateWirelessGatewayTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.create_wireless_gateway_task_response.CreateWirelessGatewayTaskResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.create_wireless_gateway_task

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.create_wireless_gateway_task.async_create_wireless_gateway_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.create_wireless_gateway_task_request.CreateWirelessGatewayTaskRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        input["wireless_gateway_task_definition_id"] = (
            wireless_gateway_task_definition_id
        )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_wireless_gateway_task_definition(
        self,
        auto_create_tasks: "aws_sdk_iot_wireless.types.auto_create_tasks.AutoCreateTasks",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        name: Optional[
            "aws_sdk_iot_wireless.types.wireless_gateway_task_name.WirelessGatewayTaskName"
        ] = None,
        update: Optional[
            "aws_sdk_iot_wireless.types.update_wireless_gateway_task_create.UpdateWirelessGatewayTaskCreate"
        ] = None,
        client_request_token: Optional[
            "aws_sdk_iot_wireless.types.client_request_token.ClientRequestToken"
        ] = None,
        tags: Optional["aws_sdk_iot_wireless.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_iot_wireless.types.create_wireless_gateway_task_definition_response.CreateWirelessGatewayTaskDefinitionResponse":
        """<p>Creates a gateway task definition.</p>

        Args:
            auto_create_tasks: <p>Whether to automatically create tasks using this task definition for all gateways with the specified current version. If <code>false</code>, the task must me created by calling <code>CreateWirelessGatewayTask</code>.</p>
            name: <p>The name of the new resource.</p>
            update: <p>Information about the gateways to update.</p>
            client_request_token: <p>Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency in Amazon EC2 API requests</a>.</p>
            tags: <p>The tags to attach to the specified resource. Tags are metadata that you can use to manage a resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.create_wireless_gateway_task_definition_request.CreateWirelessGatewayTaskDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.create_wireless_gateway_task_definition_response.CreateWirelessGatewayTaskDefinitionResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.create_wireless_gateway_task_definition

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.create_wireless_gateway_task_definition.async_create_wireless_gateway_task_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.create_wireless_gateway_task_definition_request.CreateWirelessGatewayTaskDefinitionRequest = {}  # type: ignore[typeddict-item]
        input["auto_create_tasks"] = auto_create_tasks
        if name is not None:
            input["name"] = name
        if update is not None:
            input["update"] = update
        if client_request_token is not None:
            input["client_request_token"] = client_request_token
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_destination(
        self,
        name: "aws_sdk_iot_wireless.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.delete_destination_response.DeleteDestinationResponse":
        """<p>Deletes a destination.</p>

        Args:
            name: <p>The name of the resource to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.delete_destination_request.DeleteDestinationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.delete_destination_response.DeleteDestinationResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.delete_destination

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.delete_destination.async_delete_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.delete_destination_request.DeleteDestinationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_device_profile(
        self,
        id: "aws_sdk_iot_wireless.types.device_profile_id.DeviceProfileId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.delete_device_profile_response.DeleteDeviceProfileResponse":
        """<p>Deletes a device profile.</p>

        Args:
            id: <p>The ID of the resource to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.delete_device_profile_request.DeleteDeviceProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.delete_device_profile_response.DeleteDeviceProfileResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.delete_device_profile

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.delete_device_profile.async_delete_device_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.delete_device_profile_request.DeleteDeviceProfileRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_fuota_task(
        self,
        id: "aws_sdk_iot_wireless.types.fuota_task_id.FuotaTaskId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> (
        "aws_sdk_iot_wireless.types.delete_fuota_task_response.DeleteFuotaTaskResponse"
    ):
        """<p>Deletes a FUOTA task.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.delete_fuota_task_request.DeleteFuotaTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.delete_fuota_task_response.DeleteFuotaTaskResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.delete_fuota_task

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.delete_fuota_task.async_delete_fuota_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.delete_fuota_task_request.DeleteFuotaTaskRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_multicast_group(
        self,
        id: "aws_sdk_iot_wireless.types.multicast_group_id.MulticastGroupId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.delete_multicast_group_response.DeleteMulticastGroupResponse":
        """<p>Deletes a multicast group if it is not in use by a FUOTA task.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.delete_multicast_group_request.DeleteMulticastGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.delete_multicast_group_response.DeleteMulticastGroupResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.delete_multicast_group

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.delete_multicast_group.async_delete_multicast_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.delete_multicast_group_request.DeleteMulticastGroupRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_network_analyzer_configuration(
        self,
        configuration_name: "aws_sdk_iot_wireless.types.network_analyzer_configuration_name.NetworkAnalyzerConfigurationName",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.delete_network_analyzer_configuration_response.DeleteNetworkAnalyzerConfigurationResponse":
        """<p>Deletes a network analyzer configuration.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.delete_network_analyzer_configuration_request.DeleteNetworkAnalyzerConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.delete_network_analyzer_configuration_response.DeleteNetworkAnalyzerConfigurationResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.delete_network_analyzer_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.delete_network_analyzer_configuration.async_delete_network_analyzer_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.delete_network_analyzer_configuration_request.DeleteNetworkAnalyzerConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["configuration_name"] = configuration_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_queued_messages(
        self,
        id: "aws_sdk_iot_wireless.types.wireless_device_id.WirelessDeviceId",
        message_id: "aws_sdk_iot_wireless.types.message_id.MessageId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        wireless_device_type: Optional[
            "aws_sdk_iot_wireless.types.wireless_device_type.WirelessDeviceType"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.delete_queued_messages_response.DeleteQueuedMessagesResponse":
        """<p>Remove queued messages from the downlink queue.</p>

        Args:
            id: <p>The ID of a given wireless device for which downlink messages will be deleted.</p>
            message_id: <p>If message ID is <code>\"*\"</code>, it cleares the entire downlink queue for a given device, specified by the wireless device ID. Otherwise, the downlink message with the specified message ID will be deleted.</p>
            wireless_device_type: <p>The wireless device type, which can be either Sidewalk or LoRaWAN.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.delete_queued_messages_request.DeleteQueuedMessagesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.delete_queued_messages_response.DeleteQueuedMessagesResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.delete_queued_messages

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.delete_queued_messages.async_delete_queued_messages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.delete_queued_messages_request.DeleteQueuedMessagesRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        input["message_id"] = message_id
        if wireless_device_type is not None:
            input["wireless_device_type"] = wireless_device_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_service_profile(
        self,
        id: "aws_sdk_iot_wireless.types.service_profile_id.ServiceProfileId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.delete_service_profile_response.DeleteServiceProfileResponse":
        """<p>Deletes a service profile.</p>

        Args:
            id: <p>The ID of the resource to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.delete_service_profile_request.DeleteServiceProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.delete_service_profile_response.DeleteServiceProfileResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.delete_service_profile

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.delete_service_profile.async_delete_service_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.delete_service_profile_request.DeleteServiceProfileRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_wireless_device(
        self,
        id: "aws_sdk_iot_wireless.types.wireless_device_id.WirelessDeviceId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.delete_wireless_device_response.DeleteWirelessDeviceResponse":
        """<p>Deletes a wireless device.</p>

        Args:
            id: <p>The ID of the resource to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.delete_wireless_device_request.DeleteWirelessDeviceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.delete_wireless_device_response.DeleteWirelessDeviceResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.delete_wireless_device

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.delete_wireless_device.async_delete_wireless_device(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.delete_wireless_device_request.DeleteWirelessDeviceRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_wireless_device_import_task(
        self,
        id: "aws_sdk_iot_wireless.types.import_task_id.ImportTaskId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.delete_wireless_device_import_task_response.DeleteWirelessDeviceImportTaskResponse":
        """<p>Delete an import task.</p>

        Args:
            id: <p>The unique identifier of the import task to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.delete_wireless_device_import_task_request.DeleteWirelessDeviceImportTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.delete_wireless_device_import_task_response.DeleteWirelessDeviceImportTaskResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.delete_wireless_device_import_task

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.delete_wireless_device_import_task.async_delete_wireless_device_import_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.delete_wireless_device_import_task_request.DeleteWirelessDeviceImportTaskRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_wireless_gateway(
        self,
        id: "aws_sdk_iot_wireless.types.wireless_gateway_id.WirelessGatewayId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.delete_wireless_gateway_response.DeleteWirelessGatewayResponse":
        """<p>Deletes a wireless gateway.</p> <note> <p>When deleting a wireless gateway, you might run into duplication errors for the following reasons.</p> <ul> <li> <p>If you specify a <code>GatewayEui</code> value that already exists.</p> </li> <li> <p>If you used a <code>ClientRequestToken</code> with the same parameters within the last 10 minutes.</p> </li> </ul> <p>To avoid this error, make sure that you use unique identifiers and parameters for each request within the specified time period.</p> </note>

        Args:
            id: <p>The ID of the resource to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.delete_wireless_gateway_request.DeleteWirelessGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.delete_wireless_gateway_response.DeleteWirelessGatewayResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.delete_wireless_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.delete_wireless_gateway.async_delete_wireless_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.delete_wireless_gateway_request.DeleteWirelessGatewayRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_wireless_gateway_task(
        self,
        id: "aws_sdk_iot_wireless.types.wireless_gateway_id.WirelessGatewayId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.delete_wireless_gateway_task_response.DeleteWirelessGatewayTaskResponse":
        """<p>Deletes a wireless gateway task.</p>

        Args:
            id: <p>The ID of the resource to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.delete_wireless_gateway_task_request.DeleteWirelessGatewayTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.delete_wireless_gateway_task_response.DeleteWirelessGatewayTaskResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.delete_wireless_gateway_task

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.delete_wireless_gateway_task.async_delete_wireless_gateway_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.delete_wireless_gateway_task_request.DeleteWirelessGatewayTaskRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_wireless_gateway_task_definition(
        self,
        id: "aws_sdk_iot_wireless.types.wireless_gateway_task_definition_id.WirelessGatewayTaskDefinitionId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.delete_wireless_gateway_task_definition_response.DeleteWirelessGatewayTaskDefinitionResponse":
        """<p>Deletes a wireless gateway task definition. Deleting this task definition does not affect tasks that are currently in progress.</p>

        Args:
            id: <p>The ID of the resource to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.delete_wireless_gateway_task_definition_request.DeleteWirelessGatewayTaskDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.delete_wireless_gateway_task_definition_response.DeleteWirelessGatewayTaskDefinitionResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.delete_wireless_gateway_task_definition

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.delete_wireless_gateway_task_definition.async_delete_wireless_gateway_task_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.delete_wireless_gateway_task_definition_request.DeleteWirelessGatewayTaskDefinitionRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def deregister_wireless_device(
        self,
        identifier: "aws_sdk_iot_wireless.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        wireless_device_type: Optional[
            "aws_sdk_iot_wireless.types.wireless_device_type.WirelessDeviceType"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.deregister_wireless_device_response.DeregisterWirelessDeviceResponse":
        """<p>Deregister a wireless device from AWS IoT Wireless.</p>

        Args:
            identifier: <p>The identifier of the wireless device to deregister from AWS IoT Wireless.</p>
            wireless_device_type: <p>The type of wireless device to deregister from AWS IoT Wireless, which can be <code>LoRaWAN</code> or <code>Sidewalk</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.deregister_wireless_device_request.DeregisterWirelessDeviceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.deregister_wireless_device_response.DeregisterWirelessDeviceResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.deregister_wireless_device

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.deregister_wireless_device.async_deregister_wireless_device(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.deregister_wireless_device_request.DeregisterWirelessDeviceRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier
        if wireless_device_type is not None:
            input["wireless_device_type"] = wireless_device_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_aws_account_from_partner_account(
        self,
        partner_account_id: "aws_sdk_iot_wireless.types.partner_account_id.PartnerAccountId",
        partner_type: "aws_sdk_iot_wireless.types.partner_type.PartnerType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.disassociate_aws_account_from_partner_account_response.DisassociateAwsAccountFromPartnerAccountResponse":
        """<p>Disassociates your AWS account from a partner account. If <code>PartnerAccountId</code> and <code>PartnerType</code> are <code>null</code>, disassociates your AWS account from all partner accounts.</p>

        Args:
            partner_account_id: <p>The partner account ID to disassociate from the AWS account.</p>
            partner_type: <p>The partner type.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.disassociate_aws_account_from_partner_account_request.DisassociateAwsAccountFromPartnerAccountRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.disassociate_aws_account_from_partner_account_response.DisassociateAwsAccountFromPartnerAccountResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.disassociate_aws_account_from_partner_account

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.disassociate_aws_account_from_partner_account.async_disassociate_aws_account_from_partner_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.disassociate_aws_account_from_partner_account_request.DisassociateAwsAccountFromPartnerAccountRequest = {}  # type: ignore[typeddict-item]
        input["partner_account_id"] = partner_account_id
        input["partner_type"] = partner_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_multicast_group_from_fuota_task(
        self,
        id: "aws_sdk_iot_wireless.types.fuota_task_id.FuotaTaskId",
        multicast_group_id: "aws_sdk_iot_wireless.types.multicast_group_id.MulticastGroupId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.disassociate_multicast_group_from_fuota_task_response.DisassociateMulticastGroupFromFuotaTaskResponse":
        """<p>Disassociates a multicast group from a FUOTA task.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.disassociate_multicast_group_from_fuota_task_request.DisassociateMulticastGroupFromFuotaTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.disassociate_multicast_group_from_fuota_task_response.DisassociateMulticastGroupFromFuotaTaskResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.disassociate_multicast_group_from_fuota_task

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.disassociate_multicast_group_from_fuota_task.async_disassociate_multicast_group_from_fuota_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.disassociate_multicast_group_from_fuota_task_request.DisassociateMulticastGroupFromFuotaTaskRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        input["multicast_group_id"] = multicast_group_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_wireless_device_from_fuota_task(
        self,
        id: "aws_sdk_iot_wireless.types.fuota_task_id.FuotaTaskId",
        wireless_device_id: "aws_sdk_iot_wireless.types.wireless_device_id.WirelessDeviceId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.disassociate_wireless_device_from_fuota_task_response.DisassociateWirelessDeviceFromFuotaTaskResponse":
        """<p>Disassociates a wireless device from a FUOTA task.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.disassociate_wireless_device_from_fuota_task_request.DisassociateWirelessDeviceFromFuotaTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.disassociate_wireless_device_from_fuota_task_response.DisassociateWirelessDeviceFromFuotaTaskResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.disassociate_wireless_device_from_fuota_task

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.disassociate_wireless_device_from_fuota_task.async_disassociate_wireless_device_from_fuota_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.disassociate_wireless_device_from_fuota_task_request.DisassociateWirelessDeviceFromFuotaTaskRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        input["wireless_device_id"] = wireless_device_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_wireless_device_from_multicast_group(
        self,
        id: "aws_sdk_iot_wireless.types.multicast_group_id.MulticastGroupId",
        wireless_device_id: "aws_sdk_iot_wireless.types.wireless_device_id.WirelessDeviceId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.disassociate_wireless_device_from_multicast_group_response.DisassociateWirelessDeviceFromMulticastGroupResponse":
        """<p>Disassociates a wireless device from a multicast group.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.disassociate_wireless_device_from_multicast_group_request.DisassociateWirelessDeviceFromMulticastGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.disassociate_wireless_device_from_multicast_group_response.DisassociateWirelessDeviceFromMulticastGroupResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.disassociate_wireless_device_from_multicast_group

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.disassociate_wireless_device_from_multicast_group.async_disassociate_wireless_device_from_multicast_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.disassociate_wireless_device_from_multicast_group_request.DisassociateWirelessDeviceFromMulticastGroupRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        input["wireless_device_id"] = wireless_device_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_wireless_device_from_thing(
        self,
        id: "aws_sdk_iot_wireless.types.wireless_device_id.WirelessDeviceId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.disassociate_wireless_device_from_thing_response.DisassociateWirelessDeviceFromThingResponse":
        """<p>Disassociates a wireless device from its currently associated thing.</p>

        Args:
            id: <p>The ID of the resource to update.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.disassociate_wireless_device_from_thing_request.DisassociateWirelessDeviceFromThingRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.disassociate_wireless_device_from_thing_response.DisassociateWirelessDeviceFromThingResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.disassociate_wireless_device_from_thing

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.disassociate_wireless_device_from_thing.async_disassociate_wireless_device_from_thing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.disassociate_wireless_device_from_thing_request.DisassociateWirelessDeviceFromThingRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_wireless_gateway_from_certificate(
        self,
        id: "aws_sdk_iot_wireless.types.wireless_gateway_id.WirelessGatewayId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.disassociate_wireless_gateway_from_certificate_response.DisassociateWirelessGatewayFromCertificateResponse":
        """<p>Disassociates a wireless gateway from its currently associated certificate.</p>

        Args:
            id: <p>The ID of the resource to update.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.disassociate_wireless_gateway_from_certificate_request.DisassociateWirelessGatewayFromCertificateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.disassociate_wireless_gateway_from_certificate_response.DisassociateWirelessGatewayFromCertificateResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.disassociate_wireless_gateway_from_certificate

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.disassociate_wireless_gateway_from_certificate.async_disassociate_wireless_gateway_from_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.disassociate_wireless_gateway_from_certificate_request.DisassociateWirelessGatewayFromCertificateRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_wireless_gateway_from_thing(
        self,
        id: "aws_sdk_iot_wireless.types.wireless_gateway_id.WirelessGatewayId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.disassociate_wireless_gateway_from_thing_response.DisassociateWirelessGatewayFromThingResponse":
        """<p>Disassociates a wireless gateway from its currently associated thing.</p>

        Args:
            id: <p>The ID of the resource to update.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.disassociate_wireless_gateway_from_thing_request.DisassociateWirelessGatewayFromThingRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.disassociate_wireless_gateway_from_thing_response.DisassociateWirelessGatewayFromThingResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.disassociate_wireless_gateway_from_thing

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.disassociate_wireless_gateway_from_thing.async_disassociate_wireless_gateway_from_thing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.disassociate_wireless_gateway_from_thing_request.DisassociateWirelessGatewayFromThingRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_destination(
        self,
        name: "aws_sdk_iot_wireless.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.get_destination_response.GetDestinationResponse":
        """<p>Gets information about a destination.</p>

        Args:
            name: <p>The name of the resource to get.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.get_destination_request.GetDestinationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.get_destination_response.GetDestinationResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.get_destination

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.get_destination.async_get_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.get_destination_request.GetDestinationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_device_profile(
        self,
        id: "aws_sdk_iot_wireless.types.device_profile_id.DeviceProfileId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.get_device_profile_response.GetDeviceProfileResponse":
        """<p>Gets information about a device profile.</p>

        Args:
            id: <p>The ID of the resource to get.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.get_device_profile_request.GetDeviceProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.get_device_profile_response.GetDeviceProfileResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.get_device_profile

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.get_device_profile.async_get_device_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.get_device_profile_request.GetDeviceProfileRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_event_configuration_by_resource_types(
        self, *, config_overrides: Optional[AsyncIoTWirelessClientConfig] = None
    ) -> "aws_sdk_iot_wireless.types.get_event_configuration_by_resource_types_response.GetEventConfigurationByResourceTypesResponse":
        """<p>Get the event configuration based on resource types.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.get_event_configuration_by_resource_types_request.GetEventConfigurationByResourceTypesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.get_event_configuration_by_resource_types_response.GetEventConfigurationByResourceTypesResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.get_event_configuration_by_resource_types

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.get_event_configuration_by_resource_types.async_get_event_configuration_by_resource_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.get_event_configuration_by_resource_types_request.GetEventConfigurationByResourceTypesRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_fuota_task(
        self,
        id: "aws_sdk_iot_wireless.types.fuota_task_id.FuotaTaskId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.get_fuota_task_response.GetFuotaTaskResponse":
        """<p>Gets information about a FUOTA task.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.get_fuota_task_request.GetFuotaTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.get_fuota_task_response.GetFuotaTaskResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.get_fuota_task

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.get_fuota_task.async_get_fuota_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.get_fuota_task_request.GetFuotaTaskRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_log_levels_by_resource_types(
        self, *, config_overrides: Optional[AsyncIoTWirelessClientConfig] = None
    ) -> "aws_sdk_iot_wireless.types.get_log_levels_by_resource_types_response.GetLogLevelsByResourceTypesResponse":
        """<p>Returns current default log levels or log levels by resource types. Based on the resource type, log levels can be returned for wireless device, wireless gateway, or FUOTA task log options.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.get_log_levels_by_resource_types_request.GetLogLevelsByResourceTypesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.get_log_levels_by_resource_types_response.GetLogLevelsByResourceTypesResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.get_log_levels_by_resource_types

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.get_log_levels_by_resource_types.async_get_log_levels_by_resource_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.get_log_levels_by_resource_types_request.GetLogLevelsByResourceTypesRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_metric_configuration(
        self, *, config_overrides: Optional[AsyncIoTWirelessClientConfig] = None
    ) -> "aws_sdk_iot_wireless.types.get_metric_configuration_response.GetMetricConfigurationResponse":
        """<p>Get the metric configuration status for this AWS account.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.get_metric_configuration_request.GetMetricConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.get_metric_configuration_response.GetMetricConfigurationResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.get_metric_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.get_metric_configuration.async_get_metric_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.get_metric_configuration_request.GetMetricConfigurationRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_metrics(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        summary_metric_queries: Optional[
            "aws_sdk_iot_wireless.types.summary_metric_queries.SummaryMetricQueries"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.get_metrics_response.GetMetricsResponse":
        """<p>Get the summary metrics for this AWS account.</p>

        Args:
            summary_metric_queries: <p>The list of queries to retrieve the summary metrics.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.get_metrics_request.GetMetricsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.get_metrics_response.GetMetricsResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.get_metrics

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.get_metrics.async_get_metrics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.get_metrics_request.GetMetricsRequest = {}  # type: ignore[typeddict-item]
        if summary_metric_queries is not None:
            input["summary_metric_queries"] = summary_metric_queries

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_multicast_group(
        self,
        id: "aws_sdk_iot_wireless.types.multicast_group_id.MulticastGroupId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.get_multicast_group_response.GetMulticastGroupResponse":
        """<p>Gets information about a multicast group.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.get_multicast_group_request.GetMulticastGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.get_multicast_group_response.GetMulticastGroupResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.get_multicast_group

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.get_multicast_group.async_get_multicast_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.get_multicast_group_request.GetMulticastGroupRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_multicast_group_session(
        self,
        id: "aws_sdk_iot_wireless.types.multicast_group_id.MulticastGroupId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.get_multicast_group_session_response.GetMulticastGroupSessionResponse":
        """<p>Gets information about a multicast group session.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.get_multicast_group_session_request.GetMulticastGroupSessionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.get_multicast_group_session_response.GetMulticastGroupSessionResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.get_multicast_group_session

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.get_multicast_group_session.async_get_multicast_group_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.get_multicast_group_session_request.GetMulticastGroupSessionRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_network_analyzer_configuration(
        self,
        configuration_name: "aws_sdk_iot_wireless.types.network_analyzer_configuration_name.NetworkAnalyzerConfigurationName",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.get_network_analyzer_configuration_response.GetNetworkAnalyzerConfigurationResponse":
        """<p>Get network analyzer configuration.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.get_network_analyzer_configuration_request.GetNetworkAnalyzerConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.get_network_analyzer_configuration_response.GetNetworkAnalyzerConfigurationResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.get_network_analyzer_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.get_network_analyzer_configuration.async_get_network_analyzer_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.get_network_analyzer_configuration_request.GetNetworkAnalyzerConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["configuration_name"] = configuration_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_partner_account(
        self,
        partner_account_id: "aws_sdk_iot_wireless.types.partner_account_id.PartnerAccountId",
        partner_type: "aws_sdk_iot_wireless.types.partner_type.PartnerType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.get_partner_account_response.GetPartnerAccountResponse":
        """<p>Gets information about a partner account. If <code>PartnerAccountId</code> and <code>PartnerType</code> are <code>null</code>, returns all partner accounts.</p>

        Args:
            partner_account_id: <p>The partner account ID to disassociate from the AWS account.</p>
            partner_type: <p>The partner type.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.get_partner_account_request.GetPartnerAccountRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.get_partner_account_response.GetPartnerAccountResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.get_partner_account

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.get_partner_account.async_get_partner_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.get_partner_account_request.GetPartnerAccountRequest = {}  # type: ignore[typeddict-item]
        input["partner_account_id"] = partner_account_id
        input["partner_type"] = partner_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_position(
        self,
        resource_identifier: "aws_sdk_iot_wireless.types.position_resource_identifier.PositionResourceIdentifier",
        resource_type: "aws_sdk_iot_wireless.types.position_resource_type.PositionResourceType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.get_position_response.GetPositionResponse":
        """<p>Get the position information for a given resource.</p> <important> <p>This action is no longer supported. Calls to retrieve the position information should use the <a href=\"https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetResourcePosition.html\">GetResourcePosition</a> API operation instead.</p> </important>

        Args:
            resource_identifier: <p>Resource identifier used to retrieve the position information.</p>
            resource_type: <p>Resource type of the resource for which position information is retrieved.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.get_position_request.GetPositionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.get_position_response.GetPositionResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.get_position

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.get_position.async_get_position(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.get_position_request.GetPositionRequest = {}  # type: ignore[typeddict-item]
        input["resource_identifier"] = resource_identifier
        input["resource_type"] = resource_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_position_configuration(
        self,
        resource_identifier: "aws_sdk_iot_wireless.types.position_resource_identifier.PositionResourceIdentifier",
        resource_type: "aws_sdk_iot_wireless.types.position_resource_type.PositionResourceType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.get_position_configuration_response.GetPositionConfigurationResponse":
        """<p>Get position configuration for a given resource.</p> <important> <p>This action is no longer supported. Calls to retrieve the position configuration should use the <a href=\"https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetResourcePosition.html\">GetResourcePosition</a> API operation instead.</p> </important>

        Args:
            resource_identifier: <p>Resource identifier used in a position configuration.</p>
            resource_type: <p>Resource type of the resource for which position configuration is retrieved.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.get_position_configuration_request.GetPositionConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.get_position_configuration_response.GetPositionConfigurationResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.get_position_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.get_position_configuration.async_get_position_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.get_position_configuration_request.GetPositionConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["resource_identifier"] = resource_identifier
        input["resource_type"] = resource_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_position_estimate(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        wi_fi_access_points: Optional[
            "aws_sdk_iot_wireless.types.wi_fi_access_points.WiFiAccessPoints"
        ] = None,
        cell_towers: Optional[
            "aws_sdk_iot_wireless.types.cell_towers.CellTowers"
        ] = None,
        ip: Optional["aws_sdk_iot_wireless.types.ip.Ip"] = None,
        gnss: Optional["aws_sdk_iot_wireless.types.gnss.Gnss"] = None,
        timestamp: Optional[
            "aws_sdk_iot_wireless.types.creation_date.CreationDate"
        ] = None,
        advanced_configuration: Optional[
            "aws_sdk_iot_wireless.types.advanced_configuration.AdvancedConfiguration"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.get_position_estimate_response.GetPositionEstimateResponse":
        """<p>Get estimated position information as a payload in GeoJSON format. The payload measurement data is resolved using solvers that are provided by third-party vendors.</p>

        Args:
            wi_fi_access_points: <p>Retrieves an estimated device position by resolving WLAN measurement data. The position is resolved using HERE's Wi-Fi based solver.</p>
            cell_towers: <p>Retrieves an estimated device position by resolving measurement data from cellular radio towers. The position is resolved using HERE's cellular-based solver.</p>
            ip: <p>Retrieves an estimated device position by resolving the IP address information from the device. The position is resolved using MaxMind's IP-based solver.</p>
            gnss: <p>Retrieves an estimated device position by resolving the global navigation satellite system (GNSS) scan data. The position is resolved using the GNSS solver powered by LoRa Cloud.</p>
            timestamp: <p>Optional information that specifies the time when the position information will be resolved. It uses the Unix timestamp format. If not specified, the time at which the request was received will be used.</p>
            advanced_configuration: Optional configuration to customize position estimates. If not provided, defaults are applied.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.get_position_estimate_request.GetPositionEstimateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.get_position_estimate_response.GetPositionEstimateResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.get_position_estimate

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.get_position_estimate.async_get_position_estimate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.get_position_estimate_request.GetPositionEstimateRequest = {}  # type: ignore[typeddict-item]
        if wi_fi_access_points is not None:
            input["wi_fi_access_points"] = wi_fi_access_points
        if cell_towers is not None:
            input["cell_towers"] = cell_towers
        if ip is not None:
            input["ip"] = ip
        if gnss is not None:
            input["gnss"] = gnss
        if timestamp is not None:
            input["timestamp"] = timestamp
        if advanced_configuration is not None:
            input["advanced_configuration"] = advanced_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_resource_event_configuration(
        self,
        identifier: "aws_sdk_iot_wireless.types.identifier.Identifier",
        identifier_type: "aws_sdk_iot_wireless.types.identifier_type.IdentifierType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        partner_type: Optional[
            "aws_sdk_iot_wireless.types.event_notification_partner_type.EventNotificationPartnerType"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.get_resource_event_configuration_response.GetResourceEventConfigurationResponse":
        """<p>Get the event configuration for a particular resource identifier.</p>

        Args:
            identifier: <p>Resource identifier to opt in for event messaging.</p>
            identifier_type: <p>Identifier type of the particular resource identifier for event configuration.</p>
            partner_type: <p>Partner type of the resource if the identifier type is <code>PartnerAccountId</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.get_resource_event_configuration_request.GetResourceEventConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.get_resource_event_configuration_response.GetResourceEventConfigurationResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.get_resource_event_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.get_resource_event_configuration.async_get_resource_event_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.get_resource_event_configuration_request.GetResourceEventConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier
        input["identifier_type"] = identifier_type
        if partner_type is not None:
            input["partner_type"] = partner_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_resource_log_level(
        self,
        resource_identifier: "aws_sdk_iot_wireless.types.resource_identifier.ResourceIdentifier",
        resource_type: "aws_sdk_iot_wireless.types.resource_type.ResourceType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.get_resource_log_level_response.GetResourceLogLevelResponse":
        """<p>Fetches the log-level override, if any, for a given resource ID and resource type..</p>

        Args:
            resource_type: <p>The type of resource, which can be <code>WirelessDevice</code>, <code>WirelessGateway</code>, or <code>FuotaTask</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.get_resource_log_level_request.GetResourceLogLevelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.get_resource_log_level_response.GetResourceLogLevelResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.get_resource_log_level

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.get_resource_log_level.async_get_resource_log_level(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.get_resource_log_level_request.GetResourceLogLevelRequest = {}  # type: ignore[typeddict-item]
        input["resource_identifier"] = resource_identifier
        input["resource_type"] = resource_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_resource_position(
        self,
        resource_identifier: "aws_sdk_iot_wireless.types.position_resource_identifier.PositionResourceIdentifier",
        resource_type: "aws_sdk_iot_wireless.types.position_resource_type.PositionResourceType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.get_resource_position_response.GetResourcePositionResponse":
        """<p>Get the position information for a given wireless device or a wireless gateway resource. The position information uses the <a href=\"https://gisgeography.com/wgs84-world-geodetic-system/\"> World Geodetic System (WGS84)</a>.</p>

        Args:
            resource_identifier: <p>The identifier of the resource for which position information is retrieved. It can be the wireless device ID or the wireless gateway ID, depending on the resource type.</p>
            resource_type: <p>The type of resource for which position information is retrieved, which can be a wireless device or a wireless gateway.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.get_resource_position_request.GetResourcePositionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.get_resource_position_response.GetResourcePositionResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.get_resource_position

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.get_resource_position.async_get_resource_position(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.get_resource_position_request.GetResourcePositionRequest = {}  # type: ignore[typeddict-item]
        input["resource_identifier"] = resource_identifier
        input["resource_type"] = resource_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_service_endpoint(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        service_type: Optional[
            "aws_sdk_iot_wireless.types.wireless_gateway_service_type.WirelessGatewayServiceType"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.get_service_endpoint_response.GetServiceEndpointResponse":
        """<p>Gets the account-specific endpoint for Configuration and Update Server (CUPS) protocol or LoRaWAN Network Server (LNS) connections.</p>

        Args:
            service_type: <p>The service type for which to get endpoint information about. Can be <code>CUPS</code> for the Configuration and Update Server endpoint, or <code>LNS</code> for the LoRaWAN Network Server endpoint.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.get_service_endpoint_request.GetServiceEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.get_service_endpoint_response.GetServiceEndpointResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.get_service_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.get_service_endpoint.async_get_service_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.get_service_endpoint_request.GetServiceEndpointRequest = {}  # type: ignore[typeddict-item]
        if service_type is not None:
            input["service_type"] = service_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_service_profile(
        self,
        id: "aws_sdk_iot_wireless.types.service_profile_id.ServiceProfileId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.get_service_profile_response.GetServiceProfileResponse":
        """<p>Gets information about a service profile.</p>

        Args:
            id: <p>The ID of the resource to get.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.get_service_profile_request.GetServiceProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.get_service_profile_response.GetServiceProfileResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.get_service_profile

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.get_service_profile.async_get_service_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.get_service_profile_request.GetServiceProfileRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_wireless_device(
        self,
        identifier: "aws_sdk_iot_wireless.types.identifier.Identifier",
        identifier_type: "aws_sdk_iot_wireless.types.wireless_device_id_type.WirelessDeviceIdType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.get_wireless_device_response.GetWirelessDeviceResponse":
        """<p>Gets information about a wireless device.</p>

        Args:
            identifier: <p>The identifier of the wireless device to get.</p>
            identifier_type: <p>The type of identifier used in <code>identifier</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.get_wireless_device_request.GetWirelessDeviceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.get_wireless_device_response.GetWirelessDeviceResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.get_wireless_device

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.get_wireless_device.async_get_wireless_device(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.get_wireless_device_request.GetWirelessDeviceRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier
        input["identifier_type"] = identifier_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_wireless_device_import_task(
        self,
        id: "aws_sdk_iot_wireless.types.import_task_id.ImportTaskId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.get_wireless_device_import_task_response.GetWirelessDeviceImportTaskResponse":
        """<p>Get information about an import task and count of device onboarding summary information for the import task.</p>

        Args:
            id: <p>The identifier of the import task for which information is requested.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.get_wireless_device_import_task_request.GetWirelessDeviceImportTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.get_wireless_device_import_task_response.GetWirelessDeviceImportTaskResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.get_wireless_device_import_task

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.get_wireless_device_import_task.async_get_wireless_device_import_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.get_wireless_device_import_task_request.GetWirelessDeviceImportTaskRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_wireless_device_statistics(
        self,
        wireless_device_id: "aws_sdk_iot_wireless.types.wireless_device_id.WirelessDeviceId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.get_wireless_device_statistics_response.GetWirelessDeviceStatisticsResponse":
        """<p>Gets operating information about a wireless device.</p>

        Args:
            wireless_device_id: <p>The ID of the wireless device for which to get the data.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.get_wireless_device_statistics_request.GetWirelessDeviceStatisticsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.get_wireless_device_statistics_response.GetWirelessDeviceStatisticsResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.get_wireless_device_statistics

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.get_wireless_device_statistics.async_get_wireless_device_statistics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.get_wireless_device_statistics_request.GetWirelessDeviceStatisticsRequest = {}  # type: ignore[typeddict-item]
        input["wireless_device_id"] = wireless_device_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_wireless_gateway(
        self,
        identifier: "aws_sdk_iot_wireless.types.identifier.Identifier",
        identifier_type: "aws_sdk_iot_wireless.types.wireless_gateway_id_type.WirelessGatewayIdType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.get_wireless_gateway_response.GetWirelessGatewayResponse":
        """<p>Gets information about a wireless gateway.</p>

        Args:
            identifier: <p>The identifier of the wireless gateway to get.</p>
            identifier_type: <p>The type of identifier used in <code>identifier</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.get_wireless_gateway_request.GetWirelessGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.get_wireless_gateway_response.GetWirelessGatewayResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.get_wireless_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.get_wireless_gateway.async_get_wireless_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.get_wireless_gateway_request.GetWirelessGatewayRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier
        input["identifier_type"] = identifier_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_wireless_gateway_certificate(
        self,
        id: "aws_sdk_iot_wireless.types.wireless_gateway_id.WirelessGatewayId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.get_wireless_gateway_certificate_response.GetWirelessGatewayCertificateResponse":
        """<p>Gets the ID of the certificate that is currently associated with a wireless gateway.</p>

        Args:
            id: <p>The ID of the resource to get.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.get_wireless_gateway_certificate_request.GetWirelessGatewayCertificateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.get_wireless_gateway_certificate_response.GetWirelessGatewayCertificateResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.get_wireless_gateway_certificate

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.get_wireless_gateway_certificate.async_get_wireless_gateway_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.get_wireless_gateway_certificate_request.GetWirelessGatewayCertificateRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_wireless_gateway_firmware_information(
        self,
        id: "aws_sdk_iot_wireless.types.wireless_gateway_id.WirelessGatewayId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.get_wireless_gateway_firmware_information_response.GetWirelessGatewayFirmwareInformationResponse":
        """<p>Gets the firmware version and other information about a wireless gateway.</p>

        Args:
            id: <p>The ID of the resource to get.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.get_wireless_gateway_firmware_information_request.GetWirelessGatewayFirmwareInformationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.get_wireless_gateway_firmware_information_response.GetWirelessGatewayFirmwareInformationResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.get_wireless_gateway_firmware_information

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.get_wireless_gateway_firmware_information.async_get_wireless_gateway_firmware_information(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.get_wireless_gateway_firmware_information_request.GetWirelessGatewayFirmwareInformationRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_wireless_gateway_statistics(
        self,
        wireless_gateway_id: "aws_sdk_iot_wireless.types.wireless_gateway_id.WirelessGatewayId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.get_wireless_gateway_statistics_response.GetWirelessGatewayStatisticsResponse":
        """<p>Gets operating information about a wireless gateway.</p>

        Args:
            wireless_gateway_id: <p>The ID of the wireless gateway for which to get the data.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.get_wireless_gateway_statistics_request.GetWirelessGatewayStatisticsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.get_wireless_gateway_statistics_response.GetWirelessGatewayStatisticsResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.get_wireless_gateway_statistics

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.get_wireless_gateway_statistics.async_get_wireless_gateway_statistics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.get_wireless_gateway_statistics_request.GetWirelessGatewayStatisticsRequest = {}  # type: ignore[typeddict-item]
        input["wireless_gateway_id"] = wireless_gateway_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_wireless_gateway_task(
        self,
        id: "aws_sdk_iot_wireless.types.wireless_gateway_id.WirelessGatewayId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.get_wireless_gateway_task_response.GetWirelessGatewayTaskResponse":
        """<p>Gets information about a wireless gateway task.</p>

        Args:
            id: <p>The ID of the resource to get.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.get_wireless_gateway_task_request.GetWirelessGatewayTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.get_wireless_gateway_task_response.GetWirelessGatewayTaskResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.get_wireless_gateway_task

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.get_wireless_gateway_task.async_get_wireless_gateway_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.get_wireless_gateway_task_request.GetWirelessGatewayTaskRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_wireless_gateway_task_definition(
        self,
        id: "aws_sdk_iot_wireless.types.wireless_gateway_task_definition_id.WirelessGatewayTaskDefinitionId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.get_wireless_gateway_task_definition_response.GetWirelessGatewayTaskDefinitionResponse":
        """<p>Gets information about a wireless gateway task definition.</p>

        Args:
            id: <p>The ID of the resource to get.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.get_wireless_gateway_task_definition_request.GetWirelessGatewayTaskDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.get_wireless_gateway_task_definition_response.GetWirelessGatewayTaskDefinitionResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.get_wireless_gateway_task_definition

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.get_wireless_gateway_task_definition.async_get_wireless_gateway_task_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.get_wireless_gateway_task_definition_request.GetWirelessGatewayTaskDefinitionRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_destinations(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_iot_wireless.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_iot_wireless.types.next_token.NextToken"] = None,
    ) -> (
        "aws_sdk_iot_wireless.types.list_destinations_response.ListDestinationsResponse"
    ):
        """<p>Lists the destinations registered to your AWS account.</p>

        Args:
            max_results: <p>The maximum number of results to return in this operation.</p>
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.list_destinations_request.ListDestinationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.list_destinations_response.ListDestinationsResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.list_destinations

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.list_destinations.async_list_destinations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.list_destinations_request.ListDestinationsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_device_profiles(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        next_token: Optional["aws_sdk_iot_wireless.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iot_wireless.types.max_results.MaxResults"
        ] = None,
        device_profile_type: Optional[
            "aws_sdk_iot_wireless.types.device_profile_type.DeviceProfileType"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.list_device_profiles_response.ListDeviceProfilesResponse":
        """<p>Lists the device profiles registered to your AWS account.</p>

        Args:
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>
            max_results: <p>The maximum number of results to return in this operation.</p>
            device_profile_type: <p>A filter to list only device profiles that use this type, which can be <code>LoRaWAN</code> or <code>Sidewalk</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.list_device_profiles_request.ListDeviceProfilesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.list_device_profiles_response.ListDeviceProfilesResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.list_device_profiles

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.list_device_profiles.async_list_device_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.list_device_profiles_request.ListDeviceProfilesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        if device_profile_type is not None:
            input["device_profile_type"] = device_profile_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_devices_for_wireless_device_import_task(
        self,
        id: "aws_sdk_iot_wireless.types.import_task_id.ImportTaskId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_iot_wireless.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_iot_wireless.types.next_token.NextToken"] = None,
        status: Optional[
            "aws_sdk_iot_wireless.types.onboard_status.OnboardStatus"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.list_devices_for_wireless_device_import_task_response.ListDevicesForWirelessDeviceImportTaskResponse":
        """<p>List the Sidewalk devices in an import task and their onboarding status.</p>

        Args:
            id: <p>The identifier of the import task for which wireless devices are listed.</p>
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <code>null</code> to receive the first set of results.</p>
            status: <p>The status of the devices in the import task.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.list_devices_for_wireless_device_import_task_request.ListDevicesForWirelessDeviceImportTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.list_devices_for_wireless_device_import_task_response.ListDevicesForWirelessDeviceImportTaskResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.list_devices_for_wireless_device_import_task

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.list_devices_for_wireless_device_import_task.async_list_devices_for_wireless_device_import_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.list_devices_for_wireless_device_import_task_request.ListDevicesForWirelessDeviceImportTaskRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if status is not None:
            input["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_event_configurations(
        self,
        resource_type: "aws_sdk_iot_wireless.types.event_notification_resource_type.EventNotificationResourceType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_iot_wireless.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_iot_wireless.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_iot_wireless.types.list_event_configurations_response.ListEventConfigurationsResponse":
        """<p>List event configurations where at least one event topic has been enabled.</p>

        Args:
            resource_type: <p>Resource type to filter event configurations.</p>
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.list_event_configurations_request.ListEventConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.list_event_configurations_response.ListEventConfigurationsResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.list_event_configurations

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.list_event_configurations.async_list_event_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.list_event_configurations_request.ListEventConfigurationsRequest = {}  # type: ignore[typeddict-item]
        input["resource_type"] = resource_type
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_fuota_tasks(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        next_token: Optional["aws_sdk_iot_wireless.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iot_wireless.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.list_fuota_tasks_response.ListFuotaTasksResponse":
        """<p>Lists the FUOTA tasks registered to your AWS account.</p>

        Args:
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.list_fuota_tasks_request.ListFuotaTasksRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.list_fuota_tasks_response.ListFuotaTasksResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.list_fuota_tasks

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.list_fuota_tasks.async_list_fuota_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.list_fuota_tasks_request.ListFuotaTasksRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_multicast_groups(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        next_token: Optional["aws_sdk_iot_wireless.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iot_wireless.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.list_multicast_groups_response.ListMulticastGroupsResponse":
        """<p>Lists the multicast groups registered to your AWS account.</p>

        Args:
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.list_multicast_groups_request.ListMulticastGroupsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.list_multicast_groups_response.ListMulticastGroupsResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.list_multicast_groups

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.list_multicast_groups.async_list_multicast_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.list_multicast_groups_request.ListMulticastGroupsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_multicast_groups_by_fuota_task(
        self,
        id: "aws_sdk_iot_wireless.types.fuota_task_id.FuotaTaskId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        next_token: Optional["aws_sdk_iot_wireless.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iot_wireless.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.list_multicast_groups_by_fuota_task_response.ListMulticastGroupsByFuotaTaskResponse":
        """<p>List all multicast groups associated with a FUOTA task.</p>

        Args:
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.list_multicast_groups_by_fuota_task_request.ListMulticastGroupsByFuotaTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.list_multicast_groups_by_fuota_task_response.ListMulticastGroupsByFuotaTaskResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.list_multicast_groups_by_fuota_task

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.list_multicast_groups_by_fuota_task.async_list_multicast_groups_by_fuota_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.list_multicast_groups_by_fuota_task_request.ListMulticastGroupsByFuotaTaskRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_network_analyzer_configurations(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_iot_wireless.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_iot_wireless.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_iot_wireless.types.list_network_analyzer_configurations_response.ListNetworkAnalyzerConfigurationsResponse":
        """<p>Lists the network analyzer configurations.</p>

        Args:
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.list_network_analyzer_configurations_request.ListNetworkAnalyzerConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.list_network_analyzer_configurations_response.ListNetworkAnalyzerConfigurationsResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.list_network_analyzer_configurations

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.list_network_analyzer_configurations.async_list_network_analyzer_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.list_network_analyzer_configurations_request.ListNetworkAnalyzerConfigurationsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_partner_accounts(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        next_token: Optional["aws_sdk_iot_wireless.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iot_wireless.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.list_partner_accounts_response.ListPartnerAccountsResponse":
        """<p>Lists the partner accounts associated with your AWS account.</p>

        Args:
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>
            max_results: <p>The maximum number of results to return in this operation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.list_partner_accounts_request.ListPartnerAccountsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.list_partner_accounts_response.ListPartnerAccountsResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.list_partner_accounts

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.list_partner_accounts.async_list_partner_accounts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.list_partner_accounts_request.ListPartnerAccountsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_position_configurations(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        resource_type: Optional[
            "aws_sdk_iot_wireless.types.position_resource_type.PositionResourceType"
        ] = None,
        max_results: Optional[
            "aws_sdk_iot_wireless.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_iot_wireless.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_iot_wireless.types.list_position_configurations_response.ListPositionConfigurationsResponse":
        """<p>List position configurations for a given resource, such as positioning solvers.</p> <important> <p>This action is no longer supported. Calls to retrieve position information should use the <a href=\"https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetResourcePosition.html\">GetResourcePosition</a> API operation instead.</p> </important>

        Args:
            resource_type: <p>Resource type for which position configurations are listed.</p>
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.list_position_configurations_request.ListPositionConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.list_position_configurations_response.ListPositionConfigurationsResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.list_position_configurations

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.list_position_configurations.async_list_position_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.list_position_configurations_request.ListPositionConfigurationsRequest = {}  # type: ignore[typeddict-item]
        if resource_type is not None:
            input["resource_type"] = resource_type
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_queued_messages(
        self,
        id: "aws_sdk_iot_wireless.types.wireless_device_id.WirelessDeviceId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        next_token: Optional["aws_sdk_iot_wireless.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iot_wireless.types.max_results.MaxResults"
        ] = None,
        wireless_device_type: Optional[
            "aws_sdk_iot_wireless.types.wireless_device_type.WirelessDeviceType"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.list_queued_messages_response.ListQueuedMessagesResponse":
        """<p>List queued messages in the downlink queue.</p>

        Args:
            id: <p>The ID of a given wireless device which the downlink message packets are being sent.</p>
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>
            max_results: <p>The maximum number of results to return in this operation.</p>
            wireless_device_type: <p>The wireless device type, whic can be either Sidewalk or LoRaWAN.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.list_queued_messages_request.ListQueuedMessagesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.list_queued_messages_response.ListQueuedMessagesResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.list_queued_messages

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.list_queued_messages.async_list_queued_messages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.list_queued_messages_request.ListQueuedMessagesRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        if wireless_device_type is not None:
            input["wireless_device_type"] = wireless_device_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_service_profiles(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        next_token: Optional["aws_sdk_iot_wireless.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iot_wireless.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.list_service_profiles_response.ListServiceProfilesResponse":
        """<p>Lists the service profiles registered to your AWS account.</p>

        Args:
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>
            max_results: <p>The maximum number of results to return in this operation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.list_service_profiles_request.ListServiceProfilesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.list_service_profiles_response.ListServiceProfilesResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.list_service_profiles

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.list_service_profiles.async_list_service_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.list_service_profiles_request.ListServiceProfilesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_iot_wireless.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags (metadata) you have assigned to the resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource for which you want to list tags.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_wireless_device_import_tasks(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_iot_wireless.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_iot_wireless.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_iot_wireless.types.list_wireless_device_import_tasks_response.ListWirelessDeviceImportTasksResponse":
        """<p>List of import tasks and summary information of onboarding status of devices in each import task.</p>

        Args:
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <code>null</code> to receive the first set of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.list_wireless_device_import_tasks_request.ListWirelessDeviceImportTasksRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.list_wireless_device_import_tasks_response.ListWirelessDeviceImportTasksResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.list_wireless_device_import_tasks

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.list_wireless_device_import_tasks.async_list_wireless_device_import_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.list_wireless_device_import_tasks_request.ListWirelessDeviceImportTasksRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_wireless_devices(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_iot_wireless.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_iot_wireless.types.next_token.NextToken"] = None,
        destination_name: Optional[
            "aws_sdk_iot_wireless.types.destination_name.DestinationName"
        ] = None,
        device_profile_id: Optional[
            "aws_sdk_iot_wireless.types.device_profile_id.DeviceProfileId"
        ] = None,
        service_profile_id: Optional[
            "aws_sdk_iot_wireless.types.service_profile_id.ServiceProfileId"
        ] = None,
        wireless_device_type: Optional[
            "aws_sdk_iot_wireless.types.wireless_device_type.WirelessDeviceType"
        ] = None,
        fuota_task_id: Optional[
            "aws_sdk_iot_wireless.types.fuota_task_id.FuotaTaskId"
        ] = None,
        multicast_group_id: Optional[
            "aws_sdk_iot_wireless.types.multicast_group_id.MulticastGroupId"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.list_wireless_devices_response.ListWirelessDevicesResponse":
        """<p>Lists the wireless devices registered to your AWS account.</p>

        Args:
            max_results: <p>The maximum number of results to return in this operation.</p>
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>
            destination_name: <p>A filter to list only the wireless devices that use as uplink destination.</p>
            device_profile_id: <p>A filter to list only the wireless devices that use this device profile.</p>
            service_profile_id: <p>A filter to list only the wireless devices that use this service profile.</p>
            wireless_device_type: <p>A filter to list only the wireless devices that use this wireless device type.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.list_wireless_devices_request.ListWirelessDevicesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.list_wireless_devices_response.ListWirelessDevicesResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.list_wireless_devices

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.list_wireless_devices.async_list_wireless_devices(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.list_wireless_devices_request.ListWirelessDevicesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if destination_name is not None:
            input["destination_name"] = destination_name
        if device_profile_id is not None:
            input["device_profile_id"] = device_profile_id
        if service_profile_id is not None:
            input["service_profile_id"] = service_profile_id
        if wireless_device_type is not None:
            input["wireless_device_type"] = wireless_device_type
        if fuota_task_id is not None:
            input["fuota_task_id"] = fuota_task_id
        if multicast_group_id is not None:
            input["multicast_group_id"] = multicast_group_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_wireless_gateways(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        next_token: Optional["aws_sdk_iot_wireless.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_iot_wireless.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.list_wireless_gateways_response.ListWirelessGatewaysResponse":
        """<p>Lists the wireless gateways registered to your AWS account.</p>

        Args:
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>
            max_results: <p>The maximum number of results to return in this operation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.list_wireless_gateways_request.ListWirelessGatewaysRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.list_wireless_gateways_response.ListWirelessGatewaysResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.list_wireless_gateways

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.list_wireless_gateways.async_list_wireless_gateways(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.list_wireless_gateways_request.ListWirelessGatewaysRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_wireless_gateway_task_definitions(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_iot_wireless.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_iot_wireless.types.next_token.NextToken"] = None,
        task_definition_type: Optional[
            "aws_sdk_iot_wireless.types.wireless_gateway_task_definition_type.WirelessGatewayTaskDefinitionType"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.list_wireless_gateway_task_definitions_response.ListWirelessGatewayTaskDefinitionsResponse":
        """<p>List the wireless gateway tasks definitions registered to your AWS account.</p>

        Args:
            max_results: <p>The maximum number of results to return in this operation.</p>
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>
            task_definition_type: <p>A filter to list only the wireless gateway task definitions that use this task definition type.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.list_wireless_gateway_task_definitions_request.ListWirelessGatewayTaskDefinitionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.list_wireless_gateway_task_definitions_response.ListWirelessGatewayTaskDefinitionsResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.list_wireless_gateway_task_definitions

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.list_wireless_gateway_task_definitions.async_list_wireless_gateway_task_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.list_wireless_gateway_task_definitions_request.ListWirelessGatewayTaskDefinitionsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if task_definition_type is not None:
            input["task_definition_type"] = task_definition_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_position_configuration(
        self,
        resource_identifier: "aws_sdk_iot_wireless.types.position_resource_identifier.PositionResourceIdentifier",
        resource_type: "aws_sdk_iot_wireless.types.position_resource_type.PositionResourceType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        solvers: Optional[
            "aws_sdk_iot_wireless.types.position_solver_configurations.PositionSolverConfigurations"
        ] = None,
        destination: Optional[
            "aws_sdk_iot_wireless.types.destination_name.DestinationName"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.put_position_configuration_response.PutPositionConfigurationResponse":
        """<p>Put position configuration for a given resource.</p> <important> <p>This action is no longer supported. Calls to update the position configuration should use the <a href=\"https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateResourcePosition.html\">UpdateResourcePosition</a> API operation instead.</p> </important>

        Args:
            resource_identifier: <p>Resource identifier used to update the position configuration.</p>
            resource_type: <p>Resource type of the resource for which you want to update the position configuration.</p>
            solvers: <p>The positioning solvers used to update the position configuration of the resource.</p>
            destination: <p>The position data destination that describes the AWS IoT rule that processes the device's position data for use by AWS IoT Core for LoRaWAN.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.put_position_configuration_request.PutPositionConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.put_position_configuration_response.PutPositionConfigurationResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.put_position_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.put_position_configuration.async_put_position_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.put_position_configuration_request.PutPositionConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["resource_identifier"] = resource_identifier
        input["resource_type"] = resource_type
        if solvers is not None:
            input["solvers"] = solvers
        if destination is not None:
            input["destination"] = destination

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_resource_log_level(
        self,
        resource_identifier: "aws_sdk_iot_wireless.types.resource_identifier.ResourceIdentifier",
        resource_type: "aws_sdk_iot_wireless.types.resource_type.ResourceType",
        log_level: "aws_sdk_iot_wireless.types.log_level.LogLevel",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.put_resource_log_level_response.PutResourceLogLevelResponse":
        """<p>Sets the log-level override for a resource ID and resource type. A limit of 200 log level override can be set per account.</p>

        Args:
            resource_type: <p>The type of resource, which can be <code>WirelessDevice</code>, <code>WirelessGateway</code>, or <code>FuotaTask</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.put_resource_log_level_request.PutResourceLogLevelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.put_resource_log_level_response.PutResourceLogLevelResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.put_resource_log_level

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.put_resource_log_level.async_put_resource_log_level(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.put_resource_log_level_request.PutResourceLogLevelRequest = {}  # type: ignore[typeddict-item]
        input["resource_identifier"] = resource_identifier
        input["resource_type"] = resource_type
        input["log_level"] = log_level

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def reset_all_resource_log_levels(
        self, *, config_overrides: Optional[AsyncIoTWirelessClientConfig] = None
    ) -> "aws_sdk_iot_wireless.types.reset_all_resource_log_levels_response.ResetAllResourceLogLevelsResponse":
        """<p>Removes the log-level overrides for all resources; wireless devices, wireless gateways, and FUOTA tasks.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.reset_all_resource_log_levels_request.ResetAllResourceLogLevelsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.reset_all_resource_log_levels_response.ResetAllResourceLogLevelsResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.reset_all_resource_log_levels

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.reset_all_resource_log_levels.async_reset_all_resource_log_levels(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.reset_all_resource_log_levels_request.ResetAllResourceLogLevelsRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def reset_resource_log_level(
        self,
        resource_identifier: "aws_sdk_iot_wireless.types.resource_identifier.ResourceIdentifier",
        resource_type: "aws_sdk_iot_wireless.types.resource_type.ResourceType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.reset_resource_log_level_response.ResetResourceLogLevelResponse":
        """<p>Removes the log-level override, if any, for a specific resource ID and resource type. It can be used for a wireless device, a wireless gateway, or a FUOTA task.</p>

        Args:
            resource_type: <p>The type of resource, which can be <code>WirelessDevice</code>, <code>WirelessGateway</code>, or <code>FuotaTask</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.reset_resource_log_level_request.ResetResourceLogLevelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.reset_resource_log_level_response.ResetResourceLogLevelResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.reset_resource_log_level

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.reset_resource_log_level.async_reset_resource_log_level(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.reset_resource_log_level_request.ResetResourceLogLevelRequest = {}  # type: ignore[typeddict-item]
        input["resource_identifier"] = resource_identifier
        input["resource_type"] = resource_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def send_data_to_multicast_group(
        self,
        id: "aws_sdk_iot_wireless.types.multicast_group_id.MulticastGroupId",
        payload_data: "aws_sdk_iot_wireless.types.payload_data.PayloadData",
        wireless_metadata: "aws_sdk_iot_wireless.types.multicast_wireless_metadata.MulticastWirelessMetadata",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.send_data_to_multicast_group_response.SendDataToMulticastGroupResponse":
        """<p>Sends the specified data to a multicast group.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.send_data_to_multicast_group_request.SendDataToMulticastGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.send_data_to_multicast_group_response.SendDataToMulticastGroupResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.send_data_to_multicast_group

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.send_data_to_multicast_group.async_send_data_to_multicast_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.send_data_to_multicast_group_request.SendDataToMulticastGroupRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        input["payload_data"] = payload_data
        input["wireless_metadata"] = wireless_metadata

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def send_data_to_wireless_device(
        self,
        id: "aws_sdk_iot_wireless.types.wireless_device_id.WirelessDeviceId",
        transmit_mode: "aws_sdk_iot_wireless.types.transmit_mode.TransmitMode",
        payload_data: "aws_sdk_iot_wireless.types.payload_data.PayloadData",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        wireless_metadata: Optional[
            "aws_sdk_iot_wireless.types.wireless_metadata.WirelessMetadata"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.send_data_to_wireless_device_response.SendDataToWirelessDeviceResponse":
        """<p>Sends a decrypted application data frame to a device.</p>

        Args:
            id: <p>The ID of the wireless device to receive the data.</p>
            transmit_mode: <p>The transmit mode to use to send data to the wireless device. Can be: <code>0</code> for UM (unacknowledge mode) or <code>1</code> for AM (acknowledge mode).</p>
            wireless_metadata: <p>Metadata about the message request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.send_data_to_wireless_device_request.SendDataToWirelessDeviceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.send_data_to_wireless_device_response.SendDataToWirelessDeviceResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.send_data_to_wireless_device

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.send_data_to_wireless_device.async_send_data_to_wireless_device(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.send_data_to_wireless_device_request.SendDataToWirelessDeviceRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        input["transmit_mode"] = transmit_mode
        input["payload_data"] = payload_data
        if wireless_metadata is not None:
            input["wireless_metadata"] = wireless_metadata

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_bulk_associate_wireless_device_with_multicast_group(
        self,
        id: "aws_sdk_iot_wireless.types.multicast_group_id.MulticastGroupId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        query_string: Optional[
            "aws_sdk_iot_wireless.types.query_string.QueryString"
        ] = None,
        tags: Optional["aws_sdk_iot_wireless.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_iot_wireless.types.start_bulk_associate_wireless_device_with_multicast_group_response.StartBulkAssociateWirelessDeviceWithMulticastGroupResponse":
        """<p>Starts a bulk association of all qualifying wireless devices with a multicast group.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.start_bulk_associate_wireless_device_with_multicast_group_request.StartBulkAssociateWirelessDeviceWithMulticastGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.start_bulk_associate_wireless_device_with_multicast_group_response.StartBulkAssociateWirelessDeviceWithMulticastGroupResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.start_bulk_associate_wireless_device_with_multicast_group

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.start_bulk_associate_wireless_device_with_multicast_group.async_start_bulk_associate_wireless_device_with_multicast_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.start_bulk_associate_wireless_device_with_multicast_group_request.StartBulkAssociateWirelessDeviceWithMulticastGroupRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        if query_string is not None:
            input["query_string"] = query_string
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_bulk_disassociate_wireless_device_from_multicast_group(
        self,
        id: "aws_sdk_iot_wireless.types.multicast_group_id.MulticastGroupId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        query_string: Optional[
            "aws_sdk_iot_wireless.types.query_string.QueryString"
        ] = None,
        tags: Optional["aws_sdk_iot_wireless.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_iot_wireless.types.start_bulk_disassociate_wireless_device_from_multicast_group_response.StartBulkDisassociateWirelessDeviceFromMulticastGroupResponse":
        """<p>Starts a bulk disassociatin of all qualifying wireless devices from a multicast group.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.start_bulk_disassociate_wireless_device_from_multicast_group_request.StartBulkDisassociateWirelessDeviceFromMulticastGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.start_bulk_disassociate_wireless_device_from_multicast_group_response.StartBulkDisassociateWirelessDeviceFromMulticastGroupResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.start_bulk_disassociate_wireless_device_from_multicast_group

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.start_bulk_disassociate_wireless_device_from_multicast_group.async_start_bulk_disassociate_wireless_device_from_multicast_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.start_bulk_disassociate_wireless_device_from_multicast_group_request.StartBulkDisassociateWirelessDeviceFromMulticastGroupRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        if query_string is not None:
            input["query_string"] = query_string
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_fuota_task(
        self,
        id: "aws_sdk_iot_wireless.types.fuota_task_id.FuotaTaskId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        lo_ra_wan: Optional[
            "aws_sdk_iot_wireless.types.lo_ra_wan_start_fuota_task.LoRaWANStartFuotaTask"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.start_fuota_task_response.StartFuotaTaskResponse":
        """<p>Starts a FUOTA task.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.start_fuota_task_request.StartFuotaTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.start_fuota_task_response.StartFuotaTaskResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.start_fuota_task

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.start_fuota_task.async_start_fuota_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.start_fuota_task_request.StartFuotaTaskRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        if lo_ra_wan is not None:
            input["lo_ra_wan"] = lo_ra_wan

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_multicast_group_session(
        self,
        id: "aws_sdk_iot_wireless.types.multicast_group_id.MulticastGroupId",
        lo_ra_wan: "aws_sdk_iot_wireless.types.lo_ra_wan_multicast_session.LoRaWANMulticastSession",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.start_multicast_group_session_response.StartMulticastGroupSessionResponse":
        """<p>Starts a multicast group session.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.start_multicast_group_session_request.StartMulticastGroupSessionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.start_multicast_group_session_response.StartMulticastGroupSessionResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.start_multicast_group_session

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.start_multicast_group_session.async_start_multicast_group_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.start_multicast_group_session_request.StartMulticastGroupSessionRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        input["lo_ra_wan"] = lo_ra_wan

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_single_wireless_device_import_task(
        self,
        destination_name: "aws_sdk_iot_wireless.types.destination_name.DestinationName",
        sidewalk: "aws_sdk_iot_wireless.types.sidewalk_single_start_import_info.SidewalkSingleStartImportInfo",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        client_request_token: Optional[
            "aws_sdk_iot_wireless.types.client_request_token.ClientRequestToken"
        ] = None,
        device_name: Optional[
            "aws_sdk_iot_wireless.types.device_name.DeviceName"
        ] = None,
        tags: Optional["aws_sdk_iot_wireless.types.tag_list.TagList"] = None,
        positioning: Optional[
            "aws_sdk_iot_wireless.types.positioning_config_status.PositioningConfigStatus"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.start_single_wireless_device_import_task_response.StartSingleWirelessDeviceImportTaskResponse":
        """<p>Start import task for a single wireless device.</p>

        Args:
            destination_name: <p>The name of the Sidewalk destination that describes the IoT rule to route messages from the device in the import task that will be onboarded to AWS IoT Wireless.</p>
            device_name: <p>The name of the wireless device for which an import task is being started.</p>
            positioning: <p>The integration status of the Device Location feature for Sidewalk devices.</p>
            sidewalk: <p>The Sidewalk-related parameters for importing a single wireless device.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.start_single_wireless_device_import_task_request.StartSingleWirelessDeviceImportTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.start_single_wireless_device_import_task_response.StartSingleWirelessDeviceImportTaskResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.start_single_wireless_device_import_task

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.start_single_wireless_device_import_task.async_start_single_wireless_device_import_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.start_single_wireless_device_import_task_request.StartSingleWirelessDeviceImportTaskRequest = {}  # type: ignore[typeddict-item]
        input["destination_name"] = destination_name
        if client_request_token is not None:
            input["client_request_token"] = client_request_token
        if device_name is not None:
            input["device_name"] = device_name
        if tags is not None:
            input["tags"] = tags
        if positioning is not None:
            input["positioning"] = positioning
        input["sidewalk"] = sidewalk

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_wireless_device_import_task(
        self,
        destination_name: "aws_sdk_iot_wireless.types.destination_name.DestinationName",
        sidewalk: "aws_sdk_iot_wireless.types.sidewalk_start_import_info.SidewalkStartImportInfo",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        client_request_token: Optional[
            "aws_sdk_iot_wireless.types.client_request_token.ClientRequestToken"
        ] = None,
        tags: Optional["aws_sdk_iot_wireless.types.tag_list.TagList"] = None,
        positioning: Optional[
            "aws_sdk_iot_wireless.types.positioning_config_status.PositioningConfigStatus"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.start_wireless_device_import_task_response.StartWirelessDeviceImportTaskResponse":
        """<p>Start import task for provisioning Sidewalk devices in bulk using an S3 CSV file.</p>

        Args:
            destination_name: <p>The name of the Sidewalk destination that describes the IoT rule to route messages from the devices in the import task that are onboarded to AWS IoT Wireless.</p>
            positioning: <p>The integration status of the Device Location feature for Sidewalk devices.</p>
            sidewalk: <p>The Sidewalk-related parameters for importing wireless devices that need to be provisioned in bulk.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.start_wireless_device_import_task_request.StartWirelessDeviceImportTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.start_wireless_device_import_task_response.StartWirelessDeviceImportTaskResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.start_wireless_device_import_task

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.start_wireless_device_import_task.async_start_wireless_device_import_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.start_wireless_device_import_task_request.StartWirelessDeviceImportTaskRequest = {}  # type: ignore[typeddict-item]
        input["destination_name"] = destination_name
        if client_request_token is not None:
            input["client_request_token"] = client_request_token
        if tags is not None:
            input["tags"] = tags
        if positioning is not None:
            input["positioning"] = positioning
        input["sidewalk"] = sidewalk

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_iot_wireless.types.amazon_resource_name.AmazonResourceName",
        tags: "aws_sdk_iot_wireless.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.tag_resource_response.TagResourceResponse":
        """<p>Adds a tag to a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource to add tags to.</p>
            tags: <p>Adds to or modifies the tags of the given resource. Tags are metadata that you can use to manage a resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def test_wireless_device(
        self,
        id: "aws_sdk_iot_wireless.types.wireless_device_id.WirelessDeviceId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.test_wireless_device_response.TestWirelessDeviceResponse":
        """<p>Simulates a provisioned device by sending an uplink data payload of <code>Hello</code>.</p>

        Args:
            id: <p>The ID of the wireless device to test.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.test_wireless_device_request.TestWirelessDeviceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.test_wireless_device_response.TestWirelessDeviceResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.test_wireless_device

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.test_wireless_device.async_test_wireless_device(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.test_wireless_device_request.TestWirelessDeviceRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_iot_wireless.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "aws_sdk_iot_wireless.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource to remove tags from.</p>
            tag_keys: <p>A list of the keys of the tags to remove from the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_destination(
        self,
        name: "aws_sdk_iot_wireless.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        expression_type: Optional[
            "aws_sdk_iot_wireless.types.expression_type.ExpressionType"
        ] = None,
        expression: Optional["aws_sdk_iot_wireless.types.expression.Expression"] = None,
        description: Optional[
            "aws_sdk_iot_wireless.types.description.Description"
        ] = None,
        role_arn: Optional["aws_sdk_iot_wireless.types.role_arn.RoleArn"] = None,
    ) -> "aws_sdk_iot_wireless.types.update_destination_response.UpdateDestinationResponse":
        """<p>Updates properties of a destination.</p>

        Args:
            name: <p>The new name of the resource.</p>
            expression_type: <p>The type of value in <code>Expression</code>.</p>
            expression: <p>The new rule name or topic rule to send messages to.</p>
            description: <p>A new description of the resource.</p>
            role_arn: <p>The ARN of the IAM Role that authorizes the destination.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.update_destination_request.UpdateDestinationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.update_destination_response.UpdateDestinationResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.update_destination

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.update_destination.async_update_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.update_destination_request.UpdateDestinationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if expression_type is not None:
            input["expression_type"] = expression_type
        if expression is not None:
            input["expression"] = expression
        if description is not None:
            input["description"] = description
        if role_arn is not None:
            input["role_arn"] = role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_event_configuration_by_resource_types(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        device_registration_state: Optional[
            "aws_sdk_iot_wireless.types.device_registration_state_resource_type_event_configuration.DeviceRegistrationStateResourceTypeEventConfiguration"
        ] = None,
        proximity: Optional[
            "aws_sdk_iot_wireless.types.proximity_resource_type_event_configuration.ProximityResourceTypeEventConfiguration"
        ] = None,
        join: Optional[
            "aws_sdk_iot_wireless.types.join_resource_type_event_configuration.JoinResourceTypeEventConfiguration"
        ] = None,
        connection_status: Optional[
            "aws_sdk_iot_wireless.types.connection_status_resource_type_event_configuration.ConnectionStatusResourceTypeEventConfiguration"
        ] = None,
        message_delivery_status: Optional[
            "aws_sdk_iot_wireless.types.message_delivery_status_resource_type_event_configuration.MessageDeliveryStatusResourceTypeEventConfiguration"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.update_event_configuration_by_resource_types_response.UpdateEventConfigurationByResourceTypesResponse":
        """<p>Update the event configuration based on resource types.</p>

        Args:
            device_registration_state: <p>Device registration state resource type event configuration object for enabling and disabling wireless gateway topic.</p>
            proximity: <p>Proximity resource type event configuration object for enabling and disabling wireless gateway topic.</p>
            join: <p>Join resource type event configuration object for enabling and disabling wireless device topic.</p>
            connection_status: <p>Connection status resource type event configuration object for enabling and disabling wireless gateway topic.</p>
            message_delivery_status: <p>Message delivery status resource type event configuration object for enabling and disabling wireless device topic.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.update_event_configuration_by_resource_types_request.UpdateEventConfigurationByResourceTypesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.update_event_configuration_by_resource_types_response.UpdateEventConfigurationByResourceTypesResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.update_event_configuration_by_resource_types

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.update_event_configuration_by_resource_types.async_update_event_configuration_by_resource_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.update_event_configuration_by_resource_types_request.UpdateEventConfigurationByResourceTypesRequest = {}  # type: ignore[typeddict-item]
        if device_registration_state is not None:
            input["device_registration_state"] = device_registration_state
        if proximity is not None:
            input["proximity"] = proximity
        if join is not None:
            input["join"] = join
        if connection_status is not None:
            input["connection_status"] = connection_status
        if message_delivery_status is not None:
            input["message_delivery_status"] = message_delivery_status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_fuota_task(
        self,
        id: "aws_sdk_iot_wireless.types.fuota_task_id.FuotaTaskId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        name: Optional[
            "aws_sdk_iot_wireless.types.fuota_task_name.FuotaTaskName"
        ] = None,
        description: Optional[
            "aws_sdk_iot_wireless.types.description.Description"
        ] = None,
        lo_ra_wan: Optional[
            "aws_sdk_iot_wireless.types.lo_ra_wan_fuota_task.LoRaWANFuotaTask"
        ] = None,
        firmware_update_image: Optional[
            "aws_sdk_iot_wireless.types.firmware_update_image.FirmwareUpdateImage"
        ] = None,
        firmware_update_role: Optional[
            "aws_sdk_iot_wireless.types.firmware_update_role.FirmwareUpdateRole"
        ] = None,
        redundancy_percent: Optional[
            "aws_sdk_iot_wireless.types.redundancy_percent.RedundancyPercent"
        ] = None,
        fragment_size_bytes: Optional[
            "aws_sdk_iot_wireless.types.fragment_size_bytes.FragmentSizeBytes"
        ] = None,
        fragment_interval_ms: Optional[
            "aws_sdk_iot_wireless.types.fragment_interval_ms.FragmentIntervalMS"
        ] = None,
        descriptor: Optional[
            "aws_sdk_iot_wireless.types.file_descriptor.FileDescriptor"
        ] = None,
    ) -> (
        "aws_sdk_iot_wireless.types.update_fuota_task_response.UpdateFuotaTaskResponse"
    ):
        """<p>Updates properties of a FUOTA task.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.update_fuota_task_request.UpdateFuotaTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.update_fuota_task_response.UpdateFuotaTaskResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.update_fuota_task

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.update_fuota_task.async_update_fuota_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.update_fuota_task_request.UpdateFuotaTaskRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if lo_ra_wan is not None:
            input["lo_ra_wan"] = lo_ra_wan
        if firmware_update_image is not None:
            input["firmware_update_image"] = firmware_update_image
        if firmware_update_role is not None:
            input["firmware_update_role"] = firmware_update_role
        if redundancy_percent is not None:
            input["redundancy_percent"] = redundancy_percent
        if fragment_size_bytes is not None:
            input["fragment_size_bytes"] = fragment_size_bytes
        if fragment_interval_ms is not None:
            input["fragment_interval_ms"] = fragment_interval_ms
        if descriptor is not None:
            input["descriptor"] = descriptor

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_log_levels_by_resource_types(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        default_log_level: Optional[
            "aws_sdk_iot_wireless.types.log_level.LogLevel"
        ] = None,
        fuota_task_log_options: Optional[
            "aws_sdk_iot_wireless.types.fuota_task_log_option_list.FuotaTaskLogOptionList"
        ] = None,
        wireless_device_log_options: Optional[
            "aws_sdk_iot_wireless.types.wireless_device_log_option_list.WirelessDeviceLogOptionList"
        ] = None,
        wireless_gateway_log_options: Optional[
            "aws_sdk_iot_wireless.types.wireless_gateway_log_option_list.WirelessGatewayLogOptionList"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.update_log_levels_by_resource_types_response.UpdateLogLevelsByResourceTypesResponse":
        """<p>Set default log level, or log levels by resource types. This can be for wireless device, wireless gateway, or FUOTA task log options, and is used to control the log messages that'll be displayed in CloudWatch.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.update_log_levels_by_resource_types_request.UpdateLogLevelsByResourceTypesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.update_log_levels_by_resource_types_response.UpdateLogLevelsByResourceTypesResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.update_log_levels_by_resource_types

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.update_log_levels_by_resource_types.async_update_log_levels_by_resource_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.update_log_levels_by_resource_types_request.UpdateLogLevelsByResourceTypesRequest = {}  # type: ignore[typeddict-item]
        if default_log_level is not None:
            input["default_log_level"] = default_log_level
        if fuota_task_log_options is not None:
            input["fuota_task_log_options"] = fuota_task_log_options
        if wireless_device_log_options is not None:
            input["wireless_device_log_options"] = wireless_device_log_options
        if wireless_gateway_log_options is not None:
            input["wireless_gateway_log_options"] = wireless_gateway_log_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_metric_configuration(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        summary_metric: Optional[
            "aws_sdk_iot_wireless.types.summary_metric_configuration.SummaryMetricConfiguration"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.update_metric_configuration_response.UpdateMetricConfigurationResponse":
        """<p>Update the summary metric configuration.</p>

        Args:
            summary_metric: <p>The value to be used to set summary metric configuration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.update_metric_configuration_request.UpdateMetricConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.update_metric_configuration_response.UpdateMetricConfigurationResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.update_metric_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.update_metric_configuration.async_update_metric_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.update_metric_configuration_request.UpdateMetricConfigurationRequest = {}  # type: ignore[typeddict-item]
        if summary_metric is not None:
            input["summary_metric"] = summary_metric

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_multicast_group(
        self,
        id: "aws_sdk_iot_wireless.types.multicast_group_id.MulticastGroupId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        name: Optional[
            "aws_sdk_iot_wireless.types.multicast_group_name.MulticastGroupName"
        ] = None,
        description: Optional[
            "aws_sdk_iot_wireless.types.description.Description"
        ] = None,
        lo_ra_wan: Optional[
            "aws_sdk_iot_wireless.types.lo_ra_wan_multicast.LoRaWANMulticast"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.update_multicast_group_response.UpdateMulticastGroupResponse":
        """<p>Updates properties of a multicast group session.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.update_multicast_group_request.UpdateMulticastGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.update_multicast_group_response.UpdateMulticastGroupResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.update_multicast_group

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.update_multicast_group.async_update_multicast_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.update_multicast_group_request.UpdateMulticastGroupRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if lo_ra_wan is not None:
            input["lo_ra_wan"] = lo_ra_wan

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_network_analyzer_configuration(
        self,
        configuration_name: "aws_sdk_iot_wireless.types.network_analyzer_configuration_name.NetworkAnalyzerConfigurationName",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        trace_content: Optional[
            "aws_sdk_iot_wireless.types.trace_content.TraceContent"
        ] = None,
        wireless_devices_to_add: Optional[
            "aws_sdk_iot_wireless.types.wireless_device_list.WirelessDeviceList"
        ] = None,
        wireless_devices_to_remove: Optional[
            "aws_sdk_iot_wireless.types.wireless_device_list.WirelessDeviceList"
        ] = None,
        wireless_gateways_to_add: Optional[
            "aws_sdk_iot_wireless.types.wireless_gateway_list.WirelessGatewayList"
        ] = None,
        wireless_gateways_to_remove: Optional[
            "aws_sdk_iot_wireless.types.wireless_gateway_list.WirelessGatewayList"
        ] = None,
        description: Optional[
            "aws_sdk_iot_wireless.types.description.Description"
        ] = None,
        multicast_groups_to_add: Optional[
            "aws_sdk_iot_wireless.types.network_analyzer_multicast_group_list.NetworkAnalyzerMulticastGroupList"
        ] = None,
        multicast_groups_to_remove: Optional[
            "aws_sdk_iot_wireless.types.network_analyzer_multicast_group_list.NetworkAnalyzerMulticastGroupList"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.update_network_analyzer_configuration_response.UpdateNetworkAnalyzerConfigurationResponse":
        """<p>Update network analyzer configuration.</p>

        Args:
            wireless_devices_to_add: <p>Wireless device resources to add to the network analyzer configuration. Provide the <code>WirelessDeviceId</code> of the resource to add in the input array.</p>
            wireless_devices_to_remove: <p>Wireless device resources to remove from the network analyzer configuration. Provide the <code>WirelessDeviceId</code> of the resources to remove in the input array.</p>
            wireless_gateways_to_add: <p>Wireless gateway resources to add to the network analyzer configuration. Provide the <code>WirelessGatewayId</code> of the resource to add in the input array.</p>
            wireless_gateways_to_remove: <p>Wireless gateway resources to remove from the network analyzer configuration. Provide the <code>WirelessGatewayId</code> of the resources to remove in the input array.</p>
            multicast_groups_to_add: <p>Multicast group resources to add to the network analyzer configuration. Provide the <code>MulticastGroupId</code> of the resource to add in the input array.</p>
            multicast_groups_to_remove: <p>Multicast group resources to remove from the network analyzer configuration. Provide the <code>MulticastGroupId</code> of the resources to remove in the input array.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.update_network_analyzer_configuration_request.UpdateNetworkAnalyzerConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.update_network_analyzer_configuration_response.UpdateNetworkAnalyzerConfigurationResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.update_network_analyzer_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.update_network_analyzer_configuration.async_update_network_analyzer_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.update_network_analyzer_configuration_request.UpdateNetworkAnalyzerConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["configuration_name"] = configuration_name
        if trace_content is not None:
            input["trace_content"] = trace_content
        if wireless_devices_to_add is not None:
            input["wireless_devices_to_add"] = wireless_devices_to_add
        if wireless_devices_to_remove is not None:
            input["wireless_devices_to_remove"] = wireless_devices_to_remove
        if wireless_gateways_to_add is not None:
            input["wireless_gateways_to_add"] = wireless_gateways_to_add
        if wireless_gateways_to_remove is not None:
            input["wireless_gateways_to_remove"] = wireless_gateways_to_remove
        if description is not None:
            input["description"] = description
        if multicast_groups_to_add is not None:
            input["multicast_groups_to_add"] = multicast_groups_to_add
        if multicast_groups_to_remove is not None:
            input["multicast_groups_to_remove"] = multicast_groups_to_remove

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_partner_account(
        self,
        sidewalk: "aws_sdk_iot_wireless.types.sidewalk_update_account.SidewalkUpdateAccount",
        partner_account_id: "aws_sdk_iot_wireless.types.partner_account_id.PartnerAccountId",
        partner_type: "aws_sdk_iot_wireless.types.partner_type.PartnerType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.update_partner_account_response.UpdatePartnerAccountResponse":
        """<p>Updates properties of a partner account.</p>

        Args:
            sidewalk: <p>The Sidewalk account credentials.</p>
            partner_account_id: <p>The ID of the partner account to update.</p>
            partner_type: <p>The partner type.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.update_partner_account_request.UpdatePartnerAccountRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.update_partner_account_response.UpdatePartnerAccountResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.update_partner_account

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.update_partner_account.async_update_partner_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.update_partner_account_request.UpdatePartnerAccountRequest = {}  # type: ignore[typeddict-item]
        input["sidewalk"] = sidewalk
        input["partner_account_id"] = partner_account_id
        input["partner_type"] = partner_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_position(
        self,
        resource_identifier: "aws_sdk_iot_wireless.types.position_resource_identifier.PositionResourceIdentifier",
        resource_type: "aws_sdk_iot_wireless.types.position_resource_type.PositionResourceType",
        position: "aws_sdk_iot_wireless.types.position_coordinate.PositionCoordinate",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.update_position_response.UpdatePositionResponse":
        """<p>Update the position information of a resource.</p> <important> <p>This action is no longer supported. Calls to update the position information should use the <a href=\"https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateResourcePosition.html\">UpdateResourcePosition</a> API operation instead.</p> </important>

        Args:
            resource_identifier: <p>Resource identifier of the resource for which position is updated.</p>
            resource_type: <p>Resource type of the resource for which position is updated.</p>
            position: <p>The position information of the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.update_position_request.UpdatePositionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.update_position_response.UpdatePositionResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.update_position

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.update_position.async_update_position(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.update_position_request.UpdatePositionRequest = {}  # type: ignore[typeddict-item]
        input["resource_identifier"] = resource_identifier
        input["resource_type"] = resource_type
        input["position"] = position

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_resource_event_configuration(
        self,
        identifier: "aws_sdk_iot_wireless.types.identifier.Identifier",
        identifier_type: "aws_sdk_iot_wireless.types.identifier_type.IdentifierType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        partner_type: Optional[
            "aws_sdk_iot_wireless.types.event_notification_partner_type.EventNotificationPartnerType"
        ] = None,
        device_registration_state: Optional[
            "aws_sdk_iot_wireless.types.device_registration_state_event_configuration.DeviceRegistrationStateEventConfiguration"
        ] = None,
        proximity: Optional[
            "aws_sdk_iot_wireless.types.proximity_event_configuration.ProximityEventConfiguration"
        ] = None,
        join: Optional[
            "aws_sdk_iot_wireless.types.join_event_configuration.JoinEventConfiguration"
        ] = None,
        connection_status: Optional[
            "aws_sdk_iot_wireless.types.connection_status_event_configuration.ConnectionStatusEventConfiguration"
        ] = None,
        message_delivery_status: Optional[
            "aws_sdk_iot_wireless.types.message_delivery_status_event_configuration.MessageDeliveryStatusEventConfiguration"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.update_resource_event_configuration_response.UpdateResourceEventConfigurationResponse":
        """<p>Update the event configuration for a particular resource identifier.</p>

        Args:
            identifier: <p>Resource identifier to opt in for event messaging.</p>
            identifier_type: <p>Identifier type of the particular resource identifier for event configuration.</p>
            partner_type: <p>Partner type of the resource if the identifier type is <code>PartnerAccountId</code> </p>
            device_registration_state: <p>Event configuration for the device registration state event.</p>
            proximity: <p>Event configuration for the proximity event.</p>
            join: <p>Event configuration for the join event.</p>
            connection_status: <p>Event configuration for the connection status event.</p>
            message_delivery_status: <p>Event configuration for the message delivery status event.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.update_resource_event_configuration_request.UpdateResourceEventConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.update_resource_event_configuration_response.UpdateResourceEventConfigurationResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.update_resource_event_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.update_resource_event_configuration.async_update_resource_event_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.update_resource_event_configuration_request.UpdateResourceEventConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier
        input["identifier_type"] = identifier_type
        if partner_type is not None:
            input["partner_type"] = partner_type
        if device_registration_state is not None:
            input["device_registration_state"] = device_registration_state
        if proximity is not None:
            input["proximity"] = proximity
        if join is not None:
            input["join"] = join
        if connection_status is not None:
            input["connection_status"] = connection_status
        if message_delivery_status is not None:
            input["message_delivery_status"] = message_delivery_status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_resource_position(
        self,
        resource_identifier: "aws_sdk_iot_wireless.types.position_resource_identifier.PositionResourceIdentifier",
        resource_type: "aws_sdk_iot_wireless.types.position_resource_type.PositionResourceType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        geo_json_payload: Optional[
            "aws_sdk_iot_wireless.types.geo_json_payload.GeoJsonPayload"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.update_resource_position_response.UpdateResourcePositionResponse":
        """<p>Update the position information of a given wireless device or a wireless gateway resource. The position coordinates are based on the <a href=\"https://gisgeography.com/wgs84-world-geodetic-system/\"> World Geodetic System (WGS84)</a>.</p>

        Args:
            resource_identifier: <p>The identifier of the resource for which position information is updated. It can be the wireless device ID or the wireless gateway ID, depending on the resource type.</p>
            resource_type: <p>The type of resource for which position information is updated, which can be a wireless device or a wireless gateway.</p>
            geo_json_payload: <p>The position information of the resource, displayed as a JSON payload. The payload uses the GeoJSON format, which a format that's used to encode geographic data structures. For more information, see <a href=\"https://geojson.org/\">GeoJSON</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.update_resource_position_request.UpdateResourcePositionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.update_resource_position_response.UpdateResourcePositionResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.update_resource_position

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.update_resource_position.async_update_resource_position(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.update_resource_position_request.UpdateResourcePositionRequest = {}  # type: ignore[typeddict-item]
        input["resource_identifier"] = resource_identifier
        input["resource_type"] = resource_type
        if geo_json_payload is not None:
            input["geo_json_payload"] = geo_json_payload

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_wireless_device(
        self,
        id: "aws_sdk_iot_wireless.types.wireless_device_id.WirelessDeviceId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        destination_name: Optional[
            "aws_sdk_iot_wireless.types.destination_name.DestinationName"
        ] = None,
        name: Optional[
            "aws_sdk_iot_wireless.types.wireless_device_name.WirelessDeviceName"
        ] = None,
        description: Optional[
            "aws_sdk_iot_wireless.types.description.Description"
        ] = None,
        lo_ra_wan: Optional[
            "aws_sdk_iot_wireless.types.lo_ra_wan_update_device.LoRaWANUpdateDevice"
        ] = None,
        positioning: Optional[
            "aws_sdk_iot_wireless.types.positioning_config_status.PositioningConfigStatus"
        ] = None,
        sidewalk: Optional[
            "aws_sdk_iot_wireless.types.sidewalk_update_wireless_device.SidewalkUpdateWirelessDevice"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.update_wireless_device_response.UpdateWirelessDeviceResponse":
        """<p>Updates properties of a wireless device.</p>

        Args:
            id: <p>The ID of the resource to update.</p>
            destination_name: <p>The name of the new destination for the device.</p>
            name: <p>The new name of the resource.</p> <note> <p>The following special characters aren't accepted: <code><>^#~$</code> </p> </note>
            description: <p>A new description of the resource.</p>
            lo_ra_wan: <p>The updated wireless device's configuration.</p>
            positioning: <p>The integration status of the Device Location feature for LoRaWAN and Sidewalk devices.</p>
            sidewalk: <p>The updated sidewalk properties.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.update_wireless_device_request.UpdateWirelessDeviceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.update_wireless_device_response.UpdateWirelessDeviceResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.update_wireless_device

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.update_wireless_device.async_update_wireless_device(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.update_wireless_device_request.UpdateWirelessDeviceRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        if destination_name is not None:
            input["destination_name"] = destination_name
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if lo_ra_wan is not None:
            input["lo_ra_wan"] = lo_ra_wan
        if positioning is not None:
            input["positioning"] = positioning
        if sidewalk is not None:
            input["sidewalk"] = sidewalk

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_wireless_device_import_task(
        self,
        id: "aws_sdk_iot_wireless.types.import_task_id.ImportTaskId",
        sidewalk: "aws_sdk_iot_wireless.types.sidewalk_update_import_info.SidewalkUpdateImportInfo",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "aws_sdk_iot_wireless.types.update_wireless_device_import_task_response.UpdateWirelessDeviceImportTaskResponse":
        """<p>Update an import task to add more devices to the task.</p>

        Args:
            id: <p>The identifier of the import task to be updated.</p>
            sidewalk: <p>The Sidewalk-related parameters of the import task to be updated.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.update_wireless_device_import_task_request.UpdateWirelessDeviceImportTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.update_wireless_device_import_task_response.UpdateWirelessDeviceImportTaskResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.update_wireless_device_import_task

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.update_wireless_device_import_task.async_update_wireless_device_import_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.update_wireless_device_import_task_request.UpdateWirelessDeviceImportTaskRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        input["sidewalk"] = sidewalk

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_wireless_gateway(
        self,
        id: "aws_sdk_iot_wireless.types.wireless_gateway_id.WirelessGatewayId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        name: Optional[
            "aws_sdk_iot_wireless.types.wireless_gateway_name.WirelessGatewayName"
        ] = None,
        description: Optional[
            "aws_sdk_iot_wireless.types.description.Description"
        ] = None,
        join_eui_filters: Optional[
            "aws_sdk_iot_wireless.types.join_eui_filters.JoinEuiFilters"
        ] = None,
        net_id_filters: Optional[
            "aws_sdk_iot_wireless.types.net_id_filters.NetIdFilters"
        ] = None,
        max_eirp: Optional[
            "aws_sdk_iot_wireless.types.gateway_max_eirp.GatewayMaxEirp"
        ] = None,
    ) -> "aws_sdk_iot_wireless.types.update_wireless_gateway_response.UpdateWirelessGatewayResponse":
        """<p>Updates properties of a wireless gateway.</p>

        Args:
            id: <p>The ID of the resource to update.</p>
            name: <p>The new name of the resource.</p> <note> <p>The following special characters aren't accepted: <code><>^#~$</code> </p> </note>
            description: <p>A new description of the resource.</p>
            max_eirp: <p>The MaxEIRP value.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_wireless.types.update_wireless_gateway_request.UpdateWirelessGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_wireless.types.update_wireless_gateway_response.UpdateWirelessGatewayResponse"
        ]:
            import aws_sdk_iot_wireless._operations.iotwireless.update_wireless_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_iot_wireless._operations.iotwireless.update_wireless_gateway.async_update_wireless_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_iot_wireless.types.update_wireless_gateway_request.UpdateWirelessGatewayRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if join_eui_filters is not None:
            input["join_eui_filters"] = join_eui_filters
        if net_id_filters is not None:
            input["net_id_filters"] = net_id_filters
        if max_eirp is not None:
            input["max_eirp"] = max_eirp

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
