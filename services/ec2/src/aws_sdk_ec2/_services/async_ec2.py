"""Generated from Smithy shape ``com.amazonaws.ec2#AmazonEC2``."""

import time
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_ec2._auth._signers
import aws_sdk_ec2._auth._sigv4
from aws_sdk_ec2._async import anysleep
from aws_sdk_ec2._auth._identity import Credentials
from aws_sdk_ec2._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_ec2._auth._zapros_handler import AuthMiddleware
from aws_sdk_ec2._pagination import resolve_path as _resolve_path
from aws_sdk_ec2._services._aws_config import aaws_config
from aws_sdk_ec2._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)
from aws_sdk_ec2.errors import ServiceError, WaiterTimeoutError

if TYPE_CHECKING:
    import aws_sdk_ec2.types.accept_address_transfer_request
    import aws_sdk_ec2.types.accept_address_transfer_result
    import aws_sdk_ec2.types.accept_capacity_reservation_billing_ownership_request
    import aws_sdk_ec2.types.accept_capacity_reservation_billing_ownership_result
    import aws_sdk_ec2.types.accept_reserved_instances_exchange_quote_request
    import aws_sdk_ec2.types.accept_reserved_instances_exchange_quote_result
    import aws_sdk_ec2.types.accept_transit_gateway_client_vpn_attachment_request
    import aws_sdk_ec2.types.accept_transit_gateway_client_vpn_attachment_result
    import aws_sdk_ec2.types.accept_transit_gateway_multicast_domain_associations_request
    import aws_sdk_ec2.types.accept_transit_gateway_multicast_domain_associations_result
    import aws_sdk_ec2.types.accept_transit_gateway_peering_attachment_request
    import aws_sdk_ec2.types.accept_transit_gateway_peering_attachment_result
    import aws_sdk_ec2.types.accept_transit_gateway_vpc_attachment_request
    import aws_sdk_ec2.types.accept_transit_gateway_vpc_attachment_result
    import aws_sdk_ec2.types.accept_vpc_endpoint_connections_request
    import aws_sdk_ec2.types.accept_vpc_endpoint_connections_result
    import aws_sdk_ec2.types.accept_vpc_peering_connection_request
    import aws_sdk_ec2.types.accept_vpc_peering_connection_result
    import aws_sdk_ec2.types.access_scope_analysis_finding
    import aws_sdk_ec2.types.access_scope_path_list_request
    import aws_sdk_ec2.types.account_attribute_name_string_list
    import aws_sdk_ec2.types.account_id
    import aws_sdk_ec2.types.add_ipam_operating_region_set
    import aws_sdk_ec2.types.add_ipam_organizational_unit_exclusion_set
    import aws_sdk_ec2.types.add_prefix_list_entries
    import aws_sdk_ec2.types.address_attribute
    import aws_sdk_ec2.types.address_attribute_name
    import aws_sdk_ec2.types.address_family
    import aws_sdk_ec2.types.address_max_results
    import aws_sdk_ec2.types.address_transfer
    import aws_sdk_ec2.types.advertise_byoip_cidr_request
    import aws_sdk_ec2.types.advertise_byoip_cidr_result
    import aws_sdk_ec2.types.affinity
    import aws_sdk_ec2.types.allocate_address_request
    import aws_sdk_ec2.types.allocate_address_result
    import aws_sdk_ec2.types.allocate_hosts_request
    import aws_sdk_ec2.types.allocate_hosts_result
    import aws_sdk_ec2.types.allocate_ipam_pool_cidr_request
    import aws_sdk_ec2.types.allocate_ipam_pool_cidr_result
    import aws_sdk_ec2.types.allocation_id
    import aws_sdk_ec2.types.allocation_id_list
    import aws_sdk_ec2.types.allocation_ids
    import aws_sdk_ec2.types.allowed_images_settings_enabled_state
    import aws_sdk_ec2.types.allowed_principal
    import aws_sdk_ec2.types.apply_security_groups_to_client_vpn_target_network_request
    import aws_sdk_ec2.types.apply_security_groups_to_client_vpn_target_network_result
    import aws_sdk_ec2.types.architecture_type_set
    import aws_sdk_ec2.types.architecture_values
    import aws_sdk_ec2.types.arn_list
    import aws_sdk_ec2.types.asn_authorization_context
    import aws_sdk_ec2.types.asset_id_list
    import aws_sdk_ec2.types.assign_ipv6_addresses_request
    import aws_sdk_ec2.types.assign_ipv6_addresses_result
    import aws_sdk_ec2.types.assign_private_ip_addresses_request
    import aws_sdk_ec2.types.assign_private_ip_addresses_result
    import aws_sdk_ec2.types.assign_private_nat_gateway_address_request
    import aws_sdk_ec2.types.assign_private_nat_gateway_address_result
    import aws_sdk_ec2.types.associate_address_request
    import aws_sdk_ec2.types.associate_address_result
    import aws_sdk_ec2.types.associate_capacity_reservation_billing_owner_request
    import aws_sdk_ec2.types.associate_capacity_reservation_billing_owner_result
    import aws_sdk_ec2.types.associate_client_vpn_target_network_request
    import aws_sdk_ec2.types.associate_client_vpn_target_network_result
    import aws_sdk_ec2.types.associate_dhcp_options_request
    import aws_sdk_ec2.types.associate_enclave_certificate_iam_role_request
    import aws_sdk_ec2.types.associate_enclave_certificate_iam_role_result
    import aws_sdk_ec2.types.associate_iam_instance_profile_request
    import aws_sdk_ec2.types.associate_iam_instance_profile_result
    import aws_sdk_ec2.types.associate_instance_event_window_request
    import aws_sdk_ec2.types.associate_instance_event_window_result
    import aws_sdk_ec2.types.associate_ipam_byoasn_request
    import aws_sdk_ec2.types.associate_ipam_byoasn_result
    import aws_sdk_ec2.types.associate_ipam_resource_discovery_request
    import aws_sdk_ec2.types.associate_ipam_resource_discovery_result
    import aws_sdk_ec2.types.associate_nat_gateway_address_request
    import aws_sdk_ec2.types.associate_nat_gateway_address_result
    import aws_sdk_ec2.types.associate_route_server_request
    import aws_sdk_ec2.types.associate_route_server_result
    import aws_sdk_ec2.types.associate_route_table_request
    import aws_sdk_ec2.types.associate_route_table_result
    import aws_sdk_ec2.types.associate_security_group_vpc_request
    import aws_sdk_ec2.types.associate_security_group_vpc_result
    import aws_sdk_ec2.types.associate_subnet_cidr_block_request
    import aws_sdk_ec2.types.associate_subnet_cidr_block_result
    import aws_sdk_ec2.types.associate_transit_gateway_multicast_domain_request
    import aws_sdk_ec2.types.associate_transit_gateway_multicast_domain_result
    import aws_sdk_ec2.types.associate_transit_gateway_policy_table_request
    import aws_sdk_ec2.types.associate_transit_gateway_policy_table_result
    import aws_sdk_ec2.types.associate_transit_gateway_route_table_request
    import aws_sdk_ec2.types.associate_transit_gateway_route_table_result
    import aws_sdk_ec2.types.associate_trunk_interface_request
    import aws_sdk_ec2.types.associate_trunk_interface_result
    import aws_sdk_ec2.types.associate_vpc_cidr_block_request
    import aws_sdk_ec2.types.associate_vpc_cidr_block_result
    import aws_sdk_ec2.types.association_id_list
    import aws_sdk_ec2.types.attach_classic_link_vpc_request
    import aws_sdk_ec2.types.attach_classic_link_vpc_result
    import aws_sdk_ec2.types.attach_internet_gateway_request
    import aws_sdk_ec2.types.attach_network_interface_request
    import aws_sdk_ec2.types.attach_network_interface_result
    import aws_sdk_ec2.types.attach_verified_access_trust_provider_request
    import aws_sdk_ec2.types.attach_verified_access_trust_provider_result
    import aws_sdk_ec2.types.attach_volume_request
    import aws_sdk_ec2.types.attach_vpn_gateway_request
    import aws_sdk_ec2.types.attach_vpn_gateway_result
    import aws_sdk_ec2.types.attribute_boolean_value
    import aws_sdk_ec2.types.attribute_value
    import aws_sdk_ec2.types.authorization_rule
    import aws_sdk_ec2.types.authorize_client_vpn_ingress_request
    import aws_sdk_ec2.types.authorize_client_vpn_ingress_result
    import aws_sdk_ec2.types.authorize_security_group_egress_request
    import aws_sdk_ec2.types.authorize_security_group_egress_result
    import aws_sdk_ec2.types.authorize_security_group_ingress_request
    import aws_sdk_ec2.types.authorize_security_group_ingress_result
    import aws_sdk_ec2.types.auto_placement
    import aws_sdk_ec2.types.availability_mode
    import aws_sdk_ec2.types.availability_zone_addresses
    import aws_sdk_ec2.types.availability_zone_id
    import aws_sdk_ec2.types.availability_zone_id_string_list
    import aws_sdk_ec2.types.availability_zone_name
    import aws_sdk_ec2.types.availability_zone_string_list
    import aws_sdk_ec2.types.billing_product_list
    import aws_sdk_ec2.types.blob
    import aws_sdk_ec2.types.blob_attribute_value
    import aws_sdk_ec2.types.block_device_mapping_request_list
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.boot_mode_values
    import aws_sdk_ec2.types.boxed_boolean
    import aws_sdk_ec2.types.boxed_integer
    import aws_sdk_ec2.types.boxed_long
    import aws_sdk_ec2.types.bundle_id
    import aws_sdk_ec2.types.bundle_id_string_list
    import aws_sdk_ec2.types.bundle_instance_request
    import aws_sdk_ec2.types.bundle_instance_result
    import aws_sdk_ec2.types.byoip_cidr
    import aws_sdk_ec2.types.caller_role
    import aws_sdk_ec2.types.cancel_bundle_task_request
    import aws_sdk_ec2.types.cancel_bundle_task_result
    import aws_sdk_ec2.types.cancel_capacity_reservation_fleets_request
    import aws_sdk_ec2.types.cancel_capacity_reservation_fleets_result
    import aws_sdk_ec2.types.cancel_capacity_reservation_request
    import aws_sdk_ec2.types.cancel_capacity_reservation_result
    import aws_sdk_ec2.types.cancel_conversion_request
    import aws_sdk_ec2.types.cancel_declarative_policies_report_request
    import aws_sdk_ec2.types.cancel_declarative_policies_report_result
    import aws_sdk_ec2.types.cancel_export_task_request
    import aws_sdk_ec2.types.cancel_image_launch_permission_request
    import aws_sdk_ec2.types.cancel_image_launch_permission_result
    import aws_sdk_ec2.types.cancel_import_task_request
    import aws_sdk_ec2.types.cancel_import_task_result
    import aws_sdk_ec2.types.cancel_reserved_instances_listing_request
    import aws_sdk_ec2.types.cancel_reserved_instances_listing_result
    import aws_sdk_ec2.types.cancel_spot_fleet_requests_request
    import aws_sdk_ec2.types.cancel_spot_fleet_requests_response
    import aws_sdk_ec2.types.cancel_spot_instance_requests_request
    import aws_sdk_ec2.types.cancel_spot_instance_requests_result
    import aws_sdk_ec2.types.capacity_block
    import aws_sdk_ec2.types.capacity_block_extension
    import aws_sdk_ec2.types.capacity_block_extension_offering
    import aws_sdk_ec2.types.capacity_block_ids
    import aws_sdk_ec2.types.capacity_block_offering
    import aws_sdk_ec2.types.capacity_block_status
    import aws_sdk_ec2.types.capacity_manager_condition_set
    import aws_sdk_ec2.types.capacity_manager_data_export_id
    import aws_sdk_ec2.types.capacity_manager_data_export_id_set
    import aws_sdk_ec2.types.capacity_manager_data_export_response
    import aws_sdk_ec2.types.capacity_manager_dimension
    import aws_sdk_ec2.types.capacity_manager_monitored_tag_key
    import aws_sdk_ec2.types.capacity_reservation
    import aws_sdk_ec2.types.capacity_reservation_billing_request
    import aws_sdk_ec2.types.capacity_reservation_commitment_duration
    import aws_sdk_ec2.types.capacity_reservation_delivery_preference
    import aws_sdk_ec2.types.capacity_reservation_fleet
    import aws_sdk_ec2.types.capacity_reservation_fleet_id
    import aws_sdk_ec2.types.capacity_reservation_fleet_id_set
    import aws_sdk_ec2.types.capacity_reservation_group
    import aws_sdk_ec2.types.capacity_reservation_id
    import aws_sdk_ec2.types.capacity_reservation_id_set
    import aws_sdk_ec2.types.capacity_reservation_instance_platform
    import aws_sdk_ec2.types.capacity_reservation_specification
    import aws_sdk_ec2.types.capacity_reservation_tenancy
    import aws_sdk_ec2.types.carrier_gateway
    import aws_sdk_ec2.types.carrier_gateway_id
    import aws_sdk_ec2.types.carrier_gateway_id_set
    import aws_sdk_ec2.types.carrier_gateway_max_results
    import aws_sdk_ec2.types.certificate_arn
    import aws_sdk_ec2.types.certificate_id
    import aws_sdk_ec2.types.cidr_authorization_context
    import aws_sdk_ec2.types.classic_link_dns_support
    import aws_sdk_ec2.types.classic_link_instance
    import aws_sdk_ec2.types.client_connect_options
    import aws_sdk_ec2.types.client_data
    import aws_sdk_ec2.types.client_login_banner_options
    import aws_sdk_ec2.types.client_route_enforcement_options
    import aws_sdk_ec2.types.client_vpn_authentication_request_list
    import aws_sdk_ec2.types.client_vpn_connection
    import aws_sdk_ec2.types.client_vpn_endpoint
    import aws_sdk_ec2.types.client_vpn_endpoint_id
    import aws_sdk_ec2.types.client_vpn_endpoint_id_list
    import aws_sdk_ec2.types.client_vpn_route
    import aws_sdk_ec2.types.client_vpn_security_group_id_set
    import aws_sdk_ec2.types.coip_pool
    import aws_sdk_ec2.types.coip_pool_id
    import aws_sdk_ec2.types.coip_pool_id_set
    import aws_sdk_ec2.types.coip_pool_max_results
    import aws_sdk_ec2.types.confirm_product_instance_request
    import aws_sdk_ec2.types.confirm_product_instance_result
    import aws_sdk_ec2.types.connection_log_options
    import aws_sdk_ec2.types.connection_notification
    import aws_sdk_ec2.types.connection_notification_id
    import aws_sdk_ec2.types.connection_notification_ids_list
    import aws_sdk_ec2.types.connection_tracking_specification_request
    import aws_sdk_ec2.types.connectivity_type
    import aws_sdk_ec2.types.conversion_id_string_list
    import aws_sdk_ec2.types.conversion_task_id
    import aws_sdk_ec2.types.cool_off_period_request_hours
    import aws_sdk_ec2.types.copy_fpga_image_request
    import aws_sdk_ec2.types.copy_fpga_image_result
    import aws_sdk_ec2.types.copy_image_client_token
    import aws_sdk_ec2.types.copy_image_request
    import aws_sdk_ec2.types.copy_image_result
    import aws_sdk_ec2.types.copy_snapshot_request
    import aws_sdk_ec2.types.copy_snapshot_request_psu
    import aws_sdk_ec2.types.copy_snapshot_result
    import aws_sdk_ec2.types.copy_tags_from_source
    import aws_sdk_ec2.types.copy_volumes_request
    import aws_sdk_ec2.types.copy_volumes_result
    import aws_sdk_ec2.types.core_network_arn
    import aws_sdk_ec2.types.cpu_options_request
    import aws_sdk_ec2.types.create_capacity_manager_data_export_request
    import aws_sdk_ec2.types.create_capacity_manager_data_export_result
    import aws_sdk_ec2.types.create_capacity_reservation_by_splitting_request
    import aws_sdk_ec2.types.create_capacity_reservation_by_splitting_result
    import aws_sdk_ec2.types.create_capacity_reservation_fleet_request
    import aws_sdk_ec2.types.create_capacity_reservation_fleet_result
    import aws_sdk_ec2.types.create_capacity_reservation_request
    import aws_sdk_ec2.types.create_capacity_reservation_result
    import aws_sdk_ec2.types.create_carrier_gateway_request
    import aws_sdk_ec2.types.create_carrier_gateway_result
    import aws_sdk_ec2.types.create_client_vpn_endpoint_request
    import aws_sdk_ec2.types.create_client_vpn_endpoint_result
    import aws_sdk_ec2.types.create_client_vpn_route_request
    import aws_sdk_ec2.types.create_client_vpn_route_result
    import aws_sdk_ec2.types.create_coip_cidr_request
    import aws_sdk_ec2.types.create_coip_cidr_result
    import aws_sdk_ec2.types.create_coip_pool_request
    import aws_sdk_ec2.types.create_coip_pool_result
    import aws_sdk_ec2.types.create_customer_gateway_request
    import aws_sdk_ec2.types.create_customer_gateway_result
    import aws_sdk_ec2.types.create_default_subnet_request
    import aws_sdk_ec2.types.create_default_subnet_result
    import aws_sdk_ec2.types.create_default_vpc_request
    import aws_sdk_ec2.types.create_default_vpc_result
    import aws_sdk_ec2.types.create_delegate_mac_volume_ownership_task_request
    import aws_sdk_ec2.types.create_delegate_mac_volume_ownership_task_result
    import aws_sdk_ec2.types.create_dhcp_options_request
    import aws_sdk_ec2.types.create_dhcp_options_result
    import aws_sdk_ec2.types.create_egress_only_internet_gateway_request
    import aws_sdk_ec2.types.create_egress_only_internet_gateway_result
    import aws_sdk_ec2.types.create_fleet_request
    import aws_sdk_ec2.types.create_fleet_result
    import aws_sdk_ec2.types.create_flow_logs_request
    import aws_sdk_ec2.types.create_flow_logs_result
    import aws_sdk_ec2.types.create_fpga_image_request
    import aws_sdk_ec2.types.create_fpga_image_result
    import aws_sdk_ec2.types.create_image_request
    import aws_sdk_ec2.types.create_image_result
    import aws_sdk_ec2.types.create_image_usage_report_client_token
    import aws_sdk_ec2.types.create_image_usage_report_request
    import aws_sdk_ec2.types.create_image_usage_report_result
    import aws_sdk_ec2.types.create_instance_connect_endpoint_request
    import aws_sdk_ec2.types.create_instance_connect_endpoint_result
    import aws_sdk_ec2.types.create_instance_event_window_request
    import aws_sdk_ec2.types.create_instance_event_window_result
    import aws_sdk_ec2.types.create_instance_export_task_request
    import aws_sdk_ec2.types.create_instance_export_task_result
    import aws_sdk_ec2.types.create_internet_gateway_request
    import aws_sdk_ec2.types.create_internet_gateway_result
    import aws_sdk_ec2.types.create_interruptible_capacity_reservation_allocation_request
    import aws_sdk_ec2.types.create_interruptible_capacity_reservation_allocation_result
    import aws_sdk_ec2.types.create_ipam_external_resource_verification_token_request
    import aws_sdk_ec2.types.create_ipam_external_resource_verification_token_result
    import aws_sdk_ec2.types.create_ipam_policy_request
    import aws_sdk_ec2.types.create_ipam_policy_result
    import aws_sdk_ec2.types.create_ipam_pool_request
    import aws_sdk_ec2.types.create_ipam_pool_result
    import aws_sdk_ec2.types.create_ipam_prefix_list_resolver_request
    import aws_sdk_ec2.types.create_ipam_prefix_list_resolver_result
    import aws_sdk_ec2.types.create_ipam_prefix_list_resolver_target_request
    import aws_sdk_ec2.types.create_ipam_prefix_list_resolver_target_result
    import aws_sdk_ec2.types.create_ipam_request
    import aws_sdk_ec2.types.create_ipam_resource_discovery_request
    import aws_sdk_ec2.types.create_ipam_resource_discovery_result
    import aws_sdk_ec2.types.create_ipam_result
    import aws_sdk_ec2.types.create_ipam_scope_request
    import aws_sdk_ec2.types.create_ipam_scope_result
    import aws_sdk_ec2.types.create_key_pair_request
    import aws_sdk_ec2.types.create_launch_template_request
    import aws_sdk_ec2.types.create_launch_template_result
    import aws_sdk_ec2.types.create_launch_template_version_request
    import aws_sdk_ec2.types.create_launch_template_version_result
    import aws_sdk_ec2.types.create_local_gateway_route_request
    import aws_sdk_ec2.types.create_local_gateway_route_result
    import aws_sdk_ec2.types.create_local_gateway_route_table_request
    import aws_sdk_ec2.types.create_local_gateway_route_table_result
    import aws_sdk_ec2.types.create_local_gateway_route_table_virtual_interface_group_association_request
    import aws_sdk_ec2.types.create_local_gateway_route_table_virtual_interface_group_association_result
    import aws_sdk_ec2.types.create_local_gateway_route_table_vpc_association_request
    import aws_sdk_ec2.types.create_local_gateway_route_table_vpc_association_result
    import aws_sdk_ec2.types.create_local_gateway_virtual_interface_group_request
    import aws_sdk_ec2.types.create_local_gateway_virtual_interface_group_result
    import aws_sdk_ec2.types.create_local_gateway_virtual_interface_request
    import aws_sdk_ec2.types.create_local_gateway_virtual_interface_result
    import aws_sdk_ec2.types.create_mac_system_integrity_protection_modification_task_request
    import aws_sdk_ec2.types.create_mac_system_integrity_protection_modification_task_result
    import aws_sdk_ec2.types.create_managed_prefix_list_request
    import aws_sdk_ec2.types.create_managed_prefix_list_result
    import aws_sdk_ec2.types.create_nat_gateway_request
    import aws_sdk_ec2.types.create_nat_gateway_result
    import aws_sdk_ec2.types.create_network_acl_entry_request
    import aws_sdk_ec2.types.create_network_acl_request
    import aws_sdk_ec2.types.create_network_acl_result
    import aws_sdk_ec2.types.create_network_insights_access_scope_request
    import aws_sdk_ec2.types.create_network_insights_access_scope_result
    import aws_sdk_ec2.types.create_network_insights_path_request
    import aws_sdk_ec2.types.create_network_insights_path_result
    import aws_sdk_ec2.types.create_network_interface_permission_request
    import aws_sdk_ec2.types.create_network_interface_permission_result
    import aws_sdk_ec2.types.create_network_interface_request
    import aws_sdk_ec2.types.create_network_interface_result
    import aws_sdk_ec2.types.create_placement_group_request
    import aws_sdk_ec2.types.create_placement_group_result
    import aws_sdk_ec2.types.create_public_ipv4_pool_request
    import aws_sdk_ec2.types.create_public_ipv4_pool_result
    import aws_sdk_ec2.types.create_replace_root_volume_task_request
    import aws_sdk_ec2.types.create_replace_root_volume_task_result
    import aws_sdk_ec2.types.create_reserved_instances_listing_request
    import aws_sdk_ec2.types.create_reserved_instances_listing_result
    import aws_sdk_ec2.types.create_restore_image_task_request
    import aws_sdk_ec2.types.create_restore_image_task_result
    import aws_sdk_ec2.types.create_route_request
    import aws_sdk_ec2.types.create_route_result
    import aws_sdk_ec2.types.create_route_server_endpoint_request
    import aws_sdk_ec2.types.create_route_server_endpoint_result
    import aws_sdk_ec2.types.create_route_server_peer_request
    import aws_sdk_ec2.types.create_route_server_peer_result
    import aws_sdk_ec2.types.create_route_server_request
    import aws_sdk_ec2.types.create_route_server_result
    import aws_sdk_ec2.types.create_route_table_request
    import aws_sdk_ec2.types.create_route_table_result
    import aws_sdk_ec2.types.create_secondary_network_request
    import aws_sdk_ec2.types.create_secondary_network_result
    import aws_sdk_ec2.types.create_secondary_subnet_request
    import aws_sdk_ec2.types.create_secondary_subnet_result
    import aws_sdk_ec2.types.create_security_group_request
    import aws_sdk_ec2.types.create_security_group_result
    import aws_sdk_ec2.types.create_snapshot_request
    import aws_sdk_ec2.types.create_snapshots_request
    import aws_sdk_ec2.types.create_snapshots_result
    import aws_sdk_ec2.types.create_spot_datafeed_subscription_request
    import aws_sdk_ec2.types.create_spot_datafeed_subscription_result
    import aws_sdk_ec2.types.create_store_image_task_request
    import aws_sdk_ec2.types.create_store_image_task_result
    import aws_sdk_ec2.types.create_subnet_cidr_reservation_request
    import aws_sdk_ec2.types.create_subnet_cidr_reservation_result
    import aws_sdk_ec2.types.create_subnet_request
    import aws_sdk_ec2.types.create_subnet_result
    import aws_sdk_ec2.types.create_tags_request
    import aws_sdk_ec2.types.create_traffic_mirror_filter_request
    import aws_sdk_ec2.types.create_traffic_mirror_filter_result
    import aws_sdk_ec2.types.create_traffic_mirror_filter_rule_request
    import aws_sdk_ec2.types.create_traffic_mirror_filter_rule_result
    import aws_sdk_ec2.types.create_traffic_mirror_session_request
    import aws_sdk_ec2.types.create_traffic_mirror_session_result
    import aws_sdk_ec2.types.create_traffic_mirror_target_request
    import aws_sdk_ec2.types.create_traffic_mirror_target_result
    import aws_sdk_ec2.types.create_transit_gateway_connect_peer_request
    import aws_sdk_ec2.types.create_transit_gateway_connect_peer_result
    import aws_sdk_ec2.types.create_transit_gateway_connect_request
    import aws_sdk_ec2.types.create_transit_gateway_connect_request_options
    import aws_sdk_ec2.types.create_transit_gateway_connect_result
    import aws_sdk_ec2.types.create_transit_gateway_metering_policy_entry_request
    import aws_sdk_ec2.types.create_transit_gateway_metering_policy_entry_result
    import aws_sdk_ec2.types.create_transit_gateway_metering_policy_request
    import aws_sdk_ec2.types.create_transit_gateway_metering_policy_result
    import aws_sdk_ec2.types.create_transit_gateway_multicast_domain_request
    import aws_sdk_ec2.types.create_transit_gateway_multicast_domain_request_options
    import aws_sdk_ec2.types.create_transit_gateway_multicast_domain_result
    import aws_sdk_ec2.types.create_transit_gateway_peering_attachment_request
    import aws_sdk_ec2.types.create_transit_gateway_peering_attachment_request_options
    import aws_sdk_ec2.types.create_transit_gateway_peering_attachment_result
    import aws_sdk_ec2.types.create_transit_gateway_policy_table_request
    import aws_sdk_ec2.types.create_transit_gateway_policy_table_result
    import aws_sdk_ec2.types.create_transit_gateway_prefix_list_reference_request
    import aws_sdk_ec2.types.create_transit_gateway_prefix_list_reference_result
    import aws_sdk_ec2.types.create_transit_gateway_request
    import aws_sdk_ec2.types.create_transit_gateway_result
    import aws_sdk_ec2.types.create_transit_gateway_route_request
    import aws_sdk_ec2.types.create_transit_gateway_route_result
    import aws_sdk_ec2.types.create_transit_gateway_route_table_announcement_request
    import aws_sdk_ec2.types.create_transit_gateway_route_table_announcement_result
    import aws_sdk_ec2.types.create_transit_gateway_route_table_request
    import aws_sdk_ec2.types.create_transit_gateway_route_table_result
    import aws_sdk_ec2.types.create_transit_gateway_vpc_attachment_request
    import aws_sdk_ec2.types.create_transit_gateway_vpc_attachment_request_options
    import aws_sdk_ec2.types.create_transit_gateway_vpc_attachment_result
    import aws_sdk_ec2.types.create_verified_access_endpoint_cidr_options
    import aws_sdk_ec2.types.create_verified_access_endpoint_eni_options
    import aws_sdk_ec2.types.create_verified_access_endpoint_load_balancer_options
    import aws_sdk_ec2.types.create_verified_access_endpoint_rds_options
    import aws_sdk_ec2.types.create_verified_access_endpoint_request
    import aws_sdk_ec2.types.create_verified_access_endpoint_result
    import aws_sdk_ec2.types.create_verified_access_group_request
    import aws_sdk_ec2.types.create_verified_access_group_result
    import aws_sdk_ec2.types.create_verified_access_instance_request
    import aws_sdk_ec2.types.create_verified_access_instance_result
    import aws_sdk_ec2.types.create_verified_access_native_application_oidc_options
    import aws_sdk_ec2.types.create_verified_access_trust_provider_device_options
    import aws_sdk_ec2.types.create_verified_access_trust_provider_oidc_options
    import aws_sdk_ec2.types.create_verified_access_trust_provider_request
    import aws_sdk_ec2.types.create_verified_access_trust_provider_result
    import aws_sdk_ec2.types.create_volume_permission_modifications
    import aws_sdk_ec2.types.create_volume_request
    import aws_sdk_ec2.types.create_vpc_block_public_access_exclusion_request
    import aws_sdk_ec2.types.create_vpc_block_public_access_exclusion_result
    import aws_sdk_ec2.types.create_vpc_encryption_control_request
    import aws_sdk_ec2.types.create_vpc_encryption_control_result
    import aws_sdk_ec2.types.create_vpc_endpoint_connection_notification_request
    import aws_sdk_ec2.types.create_vpc_endpoint_connection_notification_result
    import aws_sdk_ec2.types.create_vpc_endpoint_request
    import aws_sdk_ec2.types.create_vpc_endpoint_result
    import aws_sdk_ec2.types.create_vpc_endpoint_service_configuration_request
    import aws_sdk_ec2.types.create_vpc_endpoint_service_configuration_result
    import aws_sdk_ec2.types.create_vpc_peering_connection_request
    import aws_sdk_ec2.types.create_vpc_peering_connection_result
    import aws_sdk_ec2.types.create_vpc_request
    import aws_sdk_ec2.types.create_vpc_result
    import aws_sdk_ec2.types.create_vpn_concentrator_request
    import aws_sdk_ec2.types.create_vpn_concentrator_result
    import aws_sdk_ec2.types.create_vpn_connection_request
    import aws_sdk_ec2.types.create_vpn_connection_result
    import aws_sdk_ec2.types.create_vpn_connection_route_request
    import aws_sdk_ec2.types.create_vpn_gateway_request
    import aws_sdk_ec2.types.create_vpn_gateway_result
    import aws_sdk_ec2.types.credit_specification_request
    import aws_sdk_ec2.types.currency_code_values
    import aws_sdk_ec2.types.customer_gateway_id
    import aws_sdk_ec2.types.customer_gateway_id_string_list
    import aws_sdk_ec2.types.data_queries
    import aws_sdk_ec2.types.data_response
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.declarative_policies_max_results
    import aws_sdk_ec2.types.declarative_policies_report_id
    import aws_sdk_ec2.types.dedicated_host_id
    import aws_sdk_ec2.types.default_http_tokens_enforced_state
    import aws_sdk_ec2.types.default_instance_metadata_endpoint_state
    import aws_sdk_ec2.types.default_instance_metadata_tags_state
    import aws_sdk_ec2.types.defaulting_dhcp_options_id
    import aws_sdk_ec2.types.delete_capacity_manager_data_export_request
    import aws_sdk_ec2.types.delete_capacity_manager_data_export_result
    import aws_sdk_ec2.types.delete_carrier_gateway_request
    import aws_sdk_ec2.types.delete_carrier_gateway_result
    import aws_sdk_ec2.types.delete_client_vpn_endpoint_request
    import aws_sdk_ec2.types.delete_client_vpn_endpoint_result
    import aws_sdk_ec2.types.delete_client_vpn_route_request
    import aws_sdk_ec2.types.delete_client_vpn_route_result
    import aws_sdk_ec2.types.delete_coip_cidr_request
    import aws_sdk_ec2.types.delete_coip_cidr_result
    import aws_sdk_ec2.types.delete_coip_pool_request
    import aws_sdk_ec2.types.delete_coip_pool_result
    import aws_sdk_ec2.types.delete_customer_gateway_request
    import aws_sdk_ec2.types.delete_dhcp_options_request
    import aws_sdk_ec2.types.delete_egress_only_internet_gateway_request
    import aws_sdk_ec2.types.delete_egress_only_internet_gateway_result
    import aws_sdk_ec2.types.delete_fleets_request
    import aws_sdk_ec2.types.delete_fleets_result
    import aws_sdk_ec2.types.delete_flow_logs_request
    import aws_sdk_ec2.types.delete_flow_logs_result
    import aws_sdk_ec2.types.delete_fpga_image_request
    import aws_sdk_ec2.types.delete_fpga_image_result
    import aws_sdk_ec2.types.delete_image_usage_report_request
    import aws_sdk_ec2.types.delete_image_usage_report_result
    import aws_sdk_ec2.types.delete_instance_connect_endpoint_request
    import aws_sdk_ec2.types.delete_instance_connect_endpoint_result
    import aws_sdk_ec2.types.delete_instance_event_window_request
    import aws_sdk_ec2.types.delete_instance_event_window_result
    import aws_sdk_ec2.types.delete_internet_gateway_request
    import aws_sdk_ec2.types.delete_ipam_external_resource_verification_token_request
    import aws_sdk_ec2.types.delete_ipam_external_resource_verification_token_result
    import aws_sdk_ec2.types.delete_ipam_policy_request
    import aws_sdk_ec2.types.delete_ipam_policy_result
    import aws_sdk_ec2.types.delete_ipam_pool_request
    import aws_sdk_ec2.types.delete_ipam_pool_result
    import aws_sdk_ec2.types.delete_ipam_prefix_list_resolver_request
    import aws_sdk_ec2.types.delete_ipam_prefix_list_resolver_result
    import aws_sdk_ec2.types.delete_ipam_prefix_list_resolver_target_request
    import aws_sdk_ec2.types.delete_ipam_prefix_list_resolver_target_result
    import aws_sdk_ec2.types.delete_ipam_request
    import aws_sdk_ec2.types.delete_ipam_resource_discovery_request
    import aws_sdk_ec2.types.delete_ipam_resource_discovery_result
    import aws_sdk_ec2.types.delete_ipam_result
    import aws_sdk_ec2.types.delete_ipam_scope_request
    import aws_sdk_ec2.types.delete_ipam_scope_result
    import aws_sdk_ec2.types.delete_key_pair_request
    import aws_sdk_ec2.types.delete_key_pair_result
    import aws_sdk_ec2.types.delete_launch_template_request
    import aws_sdk_ec2.types.delete_launch_template_result
    import aws_sdk_ec2.types.delete_launch_template_versions_request
    import aws_sdk_ec2.types.delete_launch_template_versions_result
    import aws_sdk_ec2.types.delete_local_gateway_route_request
    import aws_sdk_ec2.types.delete_local_gateway_route_result
    import aws_sdk_ec2.types.delete_local_gateway_route_table_request
    import aws_sdk_ec2.types.delete_local_gateway_route_table_result
    import aws_sdk_ec2.types.delete_local_gateway_route_table_virtual_interface_group_association_request
    import aws_sdk_ec2.types.delete_local_gateway_route_table_virtual_interface_group_association_result
    import aws_sdk_ec2.types.delete_local_gateway_route_table_vpc_association_request
    import aws_sdk_ec2.types.delete_local_gateway_route_table_vpc_association_result
    import aws_sdk_ec2.types.delete_local_gateway_virtual_interface_group_request
    import aws_sdk_ec2.types.delete_local_gateway_virtual_interface_group_result
    import aws_sdk_ec2.types.delete_local_gateway_virtual_interface_request
    import aws_sdk_ec2.types.delete_local_gateway_virtual_interface_result
    import aws_sdk_ec2.types.delete_managed_prefix_list_request
    import aws_sdk_ec2.types.delete_managed_prefix_list_result
    import aws_sdk_ec2.types.delete_nat_gateway_request
    import aws_sdk_ec2.types.delete_nat_gateway_result
    import aws_sdk_ec2.types.delete_network_acl_entry_request
    import aws_sdk_ec2.types.delete_network_acl_request
    import aws_sdk_ec2.types.delete_network_insights_access_scope_analysis_request
    import aws_sdk_ec2.types.delete_network_insights_access_scope_analysis_result
    import aws_sdk_ec2.types.delete_network_insights_access_scope_request
    import aws_sdk_ec2.types.delete_network_insights_access_scope_result
    import aws_sdk_ec2.types.delete_network_insights_analysis_request
    import aws_sdk_ec2.types.delete_network_insights_analysis_result
    import aws_sdk_ec2.types.delete_network_insights_path_request
    import aws_sdk_ec2.types.delete_network_insights_path_result
    import aws_sdk_ec2.types.delete_network_interface_permission_request
    import aws_sdk_ec2.types.delete_network_interface_permission_result
    import aws_sdk_ec2.types.delete_network_interface_request
    import aws_sdk_ec2.types.delete_placement_group_request
    import aws_sdk_ec2.types.delete_public_ipv4_pool_request
    import aws_sdk_ec2.types.delete_public_ipv4_pool_result
    import aws_sdk_ec2.types.delete_queued_reserved_instances_id_list
    import aws_sdk_ec2.types.delete_queued_reserved_instances_request
    import aws_sdk_ec2.types.delete_queued_reserved_instances_result
    import aws_sdk_ec2.types.delete_route_request
    import aws_sdk_ec2.types.delete_route_server_endpoint_request
    import aws_sdk_ec2.types.delete_route_server_endpoint_result
    import aws_sdk_ec2.types.delete_route_server_peer_request
    import aws_sdk_ec2.types.delete_route_server_peer_result
    import aws_sdk_ec2.types.delete_route_server_request
    import aws_sdk_ec2.types.delete_route_server_result
    import aws_sdk_ec2.types.delete_route_table_request
    import aws_sdk_ec2.types.delete_secondary_network_request
    import aws_sdk_ec2.types.delete_secondary_network_result
    import aws_sdk_ec2.types.delete_secondary_subnet_request
    import aws_sdk_ec2.types.delete_secondary_subnet_result
    import aws_sdk_ec2.types.delete_security_group_request
    import aws_sdk_ec2.types.delete_security_group_result
    import aws_sdk_ec2.types.delete_snapshot_request
    import aws_sdk_ec2.types.delete_spot_datafeed_subscription_request
    import aws_sdk_ec2.types.delete_subnet_cidr_reservation_request
    import aws_sdk_ec2.types.delete_subnet_cidr_reservation_result
    import aws_sdk_ec2.types.delete_subnet_request
    import aws_sdk_ec2.types.delete_tags_request
    import aws_sdk_ec2.types.delete_traffic_mirror_filter_request
    import aws_sdk_ec2.types.delete_traffic_mirror_filter_result
    import aws_sdk_ec2.types.delete_traffic_mirror_filter_rule_request
    import aws_sdk_ec2.types.delete_traffic_mirror_filter_rule_result
    import aws_sdk_ec2.types.delete_traffic_mirror_session_request
    import aws_sdk_ec2.types.delete_traffic_mirror_session_result
    import aws_sdk_ec2.types.delete_traffic_mirror_target_request
    import aws_sdk_ec2.types.delete_traffic_mirror_target_result
    import aws_sdk_ec2.types.delete_transit_gateway_client_vpn_attachment_request
    import aws_sdk_ec2.types.delete_transit_gateway_client_vpn_attachment_result
    import aws_sdk_ec2.types.delete_transit_gateway_connect_peer_request
    import aws_sdk_ec2.types.delete_transit_gateway_connect_peer_result
    import aws_sdk_ec2.types.delete_transit_gateway_connect_request
    import aws_sdk_ec2.types.delete_transit_gateway_connect_result
    import aws_sdk_ec2.types.delete_transit_gateway_metering_policy_entry_request
    import aws_sdk_ec2.types.delete_transit_gateway_metering_policy_entry_result
    import aws_sdk_ec2.types.delete_transit_gateway_metering_policy_request
    import aws_sdk_ec2.types.delete_transit_gateway_metering_policy_result
    import aws_sdk_ec2.types.delete_transit_gateway_multicast_domain_request
    import aws_sdk_ec2.types.delete_transit_gateway_multicast_domain_result
    import aws_sdk_ec2.types.delete_transit_gateway_peering_attachment_request
    import aws_sdk_ec2.types.delete_transit_gateway_peering_attachment_result
    import aws_sdk_ec2.types.delete_transit_gateway_policy_table_request
    import aws_sdk_ec2.types.delete_transit_gateway_policy_table_result
    import aws_sdk_ec2.types.delete_transit_gateway_prefix_list_reference_request
    import aws_sdk_ec2.types.delete_transit_gateway_prefix_list_reference_result
    import aws_sdk_ec2.types.delete_transit_gateway_request
    import aws_sdk_ec2.types.delete_transit_gateway_result
    import aws_sdk_ec2.types.delete_transit_gateway_route_request
    import aws_sdk_ec2.types.delete_transit_gateway_route_result
    import aws_sdk_ec2.types.delete_transit_gateway_route_table_announcement_request
    import aws_sdk_ec2.types.delete_transit_gateway_route_table_announcement_result
    import aws_sdk_ec2.types.delete_transit_gateway_route_table_request
    import aws_sdk_ec2.types.delete_transit_gateway_route_table_result
    import aws_sdk_ec2.types.delete_transit_gateway_vpc_attachment_request
    import aws_sdk_ec2.types.delete_transit_gateway_vpc_attachment_result
    import aws_sdk_ec2.types.delete_verified_access_endpoint_request
    import aws_sdk_ec2.types.delete_verified_access_endpoint_result
    import aws_sdk_ec2.types.delete_verified_access_group_request
    import aws_sdk_ec2.types.delete_verified_access_group_result
    import aws_sdk_ec2.types.delete_verified_access_instance_request
    import aws_sdk_ec2.types.delete_verified_access_instance_result
    import aws_sdk_ec2.types.delete_verified_access_trust_provider_request
    import aws_sdk_ec2.types.delete_verified_access_trust_provider_result
    import aws_sdk_ec2.types.delete_volume_request
    import aws_sdk_ec2.types.delete_vpc_block_public_access_exclusion_request
    import aws_sdk_ec2.types.delete_vpc_block_public_access_exclusion_result
    import aws_sdk_ec2.types.delete_vpc_encryption_control_request
    import aws_sdk_ec2.types.delete_vpc_encryption_control_result
    import aws_sdk_ec2.types.delete_vpc_endpoint_connection_notifications_request
    import aws_sdk_ec2.types.delete_vpc_endpoint_connection_notifications_result
    import aws_sdk_ec2.types.delete_vpc_endpoint_service_configurations_request
    import aws_sdk_ec2.types.delete_vpc_endpoint_service_configurations_result
    import aws_sdk_ec2.types.delete_vpc_endpoints_request
    import aws_sdk_ec2.types.delete_vpc_endpoints_result
    import aws_sdk_ec2.types.delete_vpc_peering_connection_request
    import aws_sdk_ec2.types.delete_vpc_peering_connection_result
    import aws_sdk_ec2.types.delete_vpc_request
    import aws_sdk_ec2.types.delete_vpn_concentrator_request
    import aws_sdk_ec2.types.delete_vpn_concentrator_result
    import aws_sdk_ec2.types.delete_vpn_connection_request
    import aws_sdk_ec2.types.delete_vpn_connection_route_request
    import aws_sdk_ec2.types.delete_vpn_gateway_request
    import aws_sdk_ec2.types.deprovision_byoip_cidr_request
    import aws_sdk_ec2.types.deprovision_byoip_cidr_result
    import aws_sdk_ec2.types.deprovision_ipam_byoasn_request
    import aws_sdk_ec2.types.deprovision_ipam_byoasn_result
    import aws_sdk_ec2.types.deprovision_ipam_pool_cidr_request
    import aws_sdk_ec2.types.deprovision_ipam_pool_cidr_result
    import aws_sdk_ec2.types.deprovision_public_ipv4_pool_cidr_request
    import aws_sdk_ec2.types.deprovision_public_ipv4_pool_cidr_result
    import aws_sdk_ec2.types.deregister_image_request
    import aws_sdk_ec2.types.deregister_image_result
    import aws_sdk_ec2.types.deregister_instance_event_notification_attributes_request
    import aws_sdk_ec2.types.deregister_instance_event_notification_attributes_result
    import aws_sdk_ec2.types.deregister_instance_tag_attribute_request
    import aws_sdk_ec2.types.deregister_transit_gateway_multicast_group_members_request
    import aws_sdk_ec2.types.deregister_transit_gateway_multicast_group_members_result
    import aws_sdk_ec2.types.deregister_transit_gateway_multicast_group_sources_request
    import aws_sdk_ec2.types.deregister_transit_gateway_multicast_group_sources_result
    import aws_sdk_ec2.types.describe_account_attributes_request
    import aws_sdk_ec2.types.describe_account_attributes_result
    import aws_sdk_ec2.types.describe_address_transfers_max_results
    import aws_sdk_ec2.types.describe_address_transfers_request
    import aws_sdk_ec2.types.describe_address_transfers_result
    import aws_sdk_ec2.types.describe_addresses_attribute_request
    import aws_sdk_ec2.types.describe_addresses_attribute_result
    import aws_sdk_ec2.types.describe_addresses_request
    import aws_sdk_ec2.types.describe_addresses_result
    import aws_sdk_ec2.types.describe_aggregate_id_format_request
    import aws_sdk_ec2.types.describe_aggregate_id_format_result
    import aws_sdk_ec2.types.describe_availability_zones_request
    import aws_sdk_ec2.types.describe_availability_zones_result
    import aws_sdk_ec2.types.describe_aws_network_performance_metric_subscriptions_request
    import aws_sdk_ec2.types.describe_aws_network_performance_metric_subscriptions_result
    import aws_sdk_ec2.types.describe_bundle_tasks_request
    import aws_sdk_ec2.types.describe_bundle_tasks_result
    import aws_sdk_ec2.types.describe_byoip_cidrs_max_results
    import aws_sdk_ec2.types.describe_byoip_cidrs_request
    import aws_sdk_ec2.types.describe_byoip_cidrs_result
    import aws_sdk_ec2.types.describe_capacity_block_extension_history_request
    import aws_sdk_ec2.types.describe_capacity_block_extension_history_result
    import aws_sdk_ec2.types.describe_capacity_block_extension_offerings_max_results
    import aws_sdk_ec2.types.describe_capacity_block_extension_offerings_request
    import aws_sdk_ec2.types.describe_capacity_block_extension_offerings_result
    import aws_sdk_ec2.types.describe_capacity_block_offerings_max_results
    import aws_sdk_ec2.types.describe_capacity_block_offerings_request
    import aws_sdk_ec2.types.describe_capacity_block_offerings_result
    import aws_sdk_ec2.types.describe_capacity_block_status_max_results
    import aws_sdk_ec2.types.describe_capacity_block_status_request
    import aws_sdk_ec2.types.describe_capacity_block_status_result
    import aws_sdk_ec2.types.describe_capacity_blocks_max_results
    import aws_sdk_ec2.types.describe_capacity_blocks_request
    import aws_sdk_ec2.types.describe_capacity_blocks_result
    import aws_sdk_ec2.types.describe_capacity_manager_data_exports_request
    import aws_sdk_ec2.types.describe_capacity_manager_data_exports_request_max_results
    import aws_sdk_ec2.types.describe_capacity_manager_data_exports_result
    import aws_sdk_ec2.types.describe_capacity_reservation_billing_requests_request
    import aws_sdk_ec2.types.describe_capacity_reservation_billing_requests_request_max_results
    import aws_sdk_ec2.types.describe_capacity_reservation_billing_requests_result
    import aws_sdk_ec2.types.describe_capacity_reservation_fleets_max_results
    import aws_sdk_ec2.types.describe_capacity_reservation_fleets_request
    import aws_sdk_ec2.types.describe_capacity_reservation_fleets_result
    import aws_sdk_ec2.types.describe_capacity_reservation_topology_max_results
    import aws_sdk_ec2.types.describe_capacity_reservation_topology_request
    import aws_sdk_ec2.types.describe_capacity_reservation_topology_result
    import aws_sdk_ec2.types.describe_capacity_reservations_max_results
    import aws_sdk_ec2.types.describe_capacity_reservations_request
    import aws_sdk_ec2.types.describe_capacity_reservations_result
    import aws_sdk_ec2.types.describe_carrier_gateways_request
    import aws_sdk_ec2.types.describe_carrier_gateways_result
    import aws_sdk_ec2.types.describe_classic_link_instances_max_results
    import aws_sdk_ec2.types.describe_classic_link_instances_request
    import aws_sdk_ec2.types.describe_classic_link_instances_result
    import aws_sdk_ec2.types.describe_client_vpn_authorization_rules_max_results
    import aws_sdk_ec2.types.describe_client_vpn_authorization_rules_request
    import aws_sdk_ec2.types.describe_client_vpn_authorization_rules_result
    import aws_sdk_ec2.types.describe_client_vpn_connections_max_results
    import aws_sdk_ec2.types.describe_client_vpn_connections_request
    import aws_sdk_ec2.types.describe_client_vpn_connections_result
    import aws_sdk_ec2.types.describe_client_vpn_endpoint_max_results
    import aws_sdk_ec2.types.describe_client_vpn_endpoints_request
    import aws_sdk_ec2.types.describe_client_vpn_endpoints_result
    import aws_sdk_ec2.types.describe_client_vpn_routes_max_results
    import aws_sdk_ec2.types.describe_client_vpn_routes_request
    import aws_sdk_ec2.types.describe_client_vpn_routes_result
    import aws_sdk_ec2.types.describe_client_vpn_target_networks_max_results
    import aws_sdk_ec2.types.describe_client_vpn_target_networks_request
    import aws_sdk_ec2.types.describe_client_vpn_target_networks_result
    import aws_sdk_ec2.types.describe_coip_pools_request
    import aws_sdk_ec2.types.describe_coip_pools_result
    import aws_sdk_ec2.types.describe_conversion_tasks_request
    import aws_sdk_ec2.types.describe_conversion_tasks_result
    import aws_sdk_ec2.types.describe_customer_gateways_request
    import aws_sdk_ec2.types.describe_customer_gateways_result
    import aws_sdk_ec2.types.describe_declarative_policies_reports_request
    import aws_sdk_ec2.types.describe_declarative_policies_reports_result
    import aws_sdk_ec2.types.describe_dhcp_options_max_results
    import aws_sdk_ec2.types.describe_dhcp_options_request
    import aws_sdk_ec2.types.describe_dhcp_options_result
    import aws_sdk_ec2.types.describe_egress_only_internet_gateways_max_results
    import aws_sdk_ec2.types.describe_egress_only_internet_gateways_request
    import aws_sdk_ec2.types.describe_egress_only_internet_gateways_result
    import aws_sdk_ec2.types.describe_elastic_gpus_max_results
    import aws_sdk_ec2.types.describe_elastic_gpus_request
    import aws_sdk_ec2.types.describe_elastic_gpus_result
    import aws_sdk_ec2.types.describe_export_image_tasks_max_results
    import aws_sdk_ec2.types.describe_export_image_tasks_request
    import aws_sdk_ec2.types.describe_export_image_tasks_result
    import aws_sdk_ec2.types.describe_export_tasks_request
    import aws_sdk_ec2.types.describe_export_tasks_result
    import aws_sdk_ec2.types.describe_fast_launch_images_request
    import aws_sdk_ec2.types.describe_fast_launch_images_request_max_results
    import aws_sdk_ec2.types.describe_fast_launch_images_result
    import aws_sdk_ec2.types.describe_fast_launch_images_success_item
    import aws_sdk_ec2.types.describe_fast_snapshot_restore_success_item
    import aws_sdk_ec2.types.describe_fast_snapshot_restores_max_results
    import aws_sdk_ec2.types.describe_fast_snapshot_restores_request
    import aws_sdk_ec2.types.describe_fast_snapshot_restores_result
    import aws_sdk_ec2.types.describe_fleet_history_request
    import aws_sdk_ec2.types.describe_fleet_history_result
    import aws_sdk_ec2.types.describe_fleet_instances_request
    import aws_sdk_ec2.types.describe_fleet_instances_result
    import aws_sdk_ec2.types.describe_fleets_request
    import aws_sdk_ec2.types.describe_fleets_result
    import aws_sdk_ec2.types.describe_flow_logs_request
    import aws_sdk_ec2.types.describe_flow_logs_result
    import aws_sdk_ec2.types.describe_fpga_image_attribute_request
    import aws_sdk_ec2.types.describe_fpga_image_attribute_result
    import aws_sdk_ec2.types.describe_fpga_images_max_results
    import aws_sdk_ec2.types.describe_fpga_images_request
    import aws_sdk_ec2.types.describe_fpga_images_result
    import aws_sdk_ec2.types.describe_future_capacity_max_results
    import aws_sdk_ec2.types.describe_host_reservation_offerings_request
    import aws_sdk_ec2.types.describe_host_reservation_offerings_result
    import aws_sdk_ec2.types.describe_host_reservations_max_results
    import aws_sdk_ec2.types.describe_host_reservations_request
    import aws_sdk_ec2.types.describe_host_reservations_result
    import aws_sdk_ec2.types.describe_hosts_request
    import aws_sdk_ec2.types.describe_hosts_result
    import aws_sdk_ec2.types.describe_iam_instance_profile_associations_max_results
    import aws_sdk_ec2.types.describe_iam_instance_profile_associations_request
    import aws_sdk_ec2.types.describe_iam_instance_profile_associations_result
    import aws_sdk_ec2.types.describe_id_format_request
    import aws_sdk_ec2.types.describe_id_format_result
    import aws_sdk_ec2.types.describe_identity_id_format_request
    import aws_sdk_ec2.types.describe_identity_id_format_result
    import aws_sdk_ec2.types.describe_image_attribute_request
    import aws_sdk_ec2.types.describe_image_references_image_id_string_list
    import aws_sdk_ec2.types.describe_image_references_max_results
    import aws_sdk_ec2.types.describe_image_references_request
    import aws_sdk_ec2.types.describe_image_references_result
    import aws_sdk_ec2.types.describe_image_usage_report_entries_max_results
    import aws_sdk_ec2.types.describe_image_usage_report_entries_request
    import aws_sdk_ec2.types.describe_image_usage_report_entries_result
    import aws_sdk_ec2.types.describe_image_usage_reports_image_id_string_list
    import aws_sdk_ec2.types.describe_image_usage_reports_max_results
    import aws_sdk_ec2.types.describe_image_usage_reports_request
    import aws_sdk_ec2.types.describe_image_usage_reports_result
    import aws_sdk_ec2.types.describe_images_request
    import aws_sdk_ec2.types.describe_images_result
    import aws_sdk_ec2.types.describe_import_image_tasks_request
    import aws_sdk_ec2.types.describe_import_image_tasks_result
    import aws_sdk_ec2.types.describe_import_snapshot_tasks_request
    import aws_sdk_ec2.types.describe_import_snapshot_tasks_result
    import aws_sdk_ec2.types.describe_instance_attribute_request
    import aws_sdk_ec2.types.describe_instance_connect_endpoints_request
    import aws_sdk_ec2.types.describe_instance_connect_endpoints_result
    import aws_sdk_ec2.types.describe_instance_credit_specifications_max_results
    import aws_sdk_ec2.types.describe_instance_credit_specifications_request
    import aws_sdk_ec2.types.describe_instance_credit_specifications_result
    import aws_sdk_ec2.types.describe_instance_event_notification_attributes_request
    import aws_sdk_ec2.types.describe_instance_event_notification_attributes_result
    import aws_sdk_ec2.types.describe_instance_event_windows_request
    import aws_sdk_ec2.types.describe_instance_event_windows_result
    import aws_sdk_ec2.types.describe_instance_image_metadata_max_results
    import aws_sdk_ec2.types.describe_instance_image_metadata_request
    import aws_sdk_ec2.types.describe_instance_image_metadata_result
    import aws_sdk_ec2.types.describe_instance_sql_ha_history_states_request
    import aws_sdk_ec2.types.describe_instance_sql_ha_history_states_result
    import aws_sdk_ec2.types.describe_instance_sql_ha_states_request
    import aws_sdk_ec2.types.describe_instance_sql_ha_states_request_max_results_integer
    import aws_sdk_ec2.types.describe_instance_sql_ha_states_result
    import aws_sdk_ec2.types.describe_instance_status_request
    import aws_sdk_ec2.types.describe_instance_status_result
    import aws_sdk_ec2.types.describe_instance_topology_group_name_set
    import aws_sdk_ec2.types.describe_instance_topology_instance_id_set
    import aws_sdk_ec2.types.describe_instance_topology_max_results
    import aws_sdk_ec2.types.describe_instance_topology_request
    import aws_sdk_ec2.types.describe_instance_topology_result
    import aws_sdk_ec2.types.describe_instance_type_offerings_request
    import aws_sdk_ec2.types.describe_instance_type_offerings_result
    import aws_sdk_ec2.types.describe_instance_types_request
    import aws_sdk_ec2.types.describe_instance_types_result
    import aws_sdk_ec2.types.describe_instances_request
    import aws_sdk_ec2.types.describe_instances_result
    import aws_sdk_ec2.types.describe_internet_gateways_max_results
    import aws_sdk_ec2.types.describe_internet_gateways_request
    import aws_sdk_ec2.types.describe_internet_gateways_result
    import aws_sdk_ec2.types.describe_ipam_byoasn_max_results
    import aws_sdk_ec2.types.describe_ipam_byoasn_request
    import aws_sdk_ec2.types.describe_ipam_byoasn_result
    import aws_sdk_ec2.types.describe_ipam_external_resource_verification_tokens_request
    import aws_sdk_ec2.types.describe_ipam_external_resource_verification_tokens_result
    import aws_sdk_ec2.types.describe_ipam_policies_request
    import aws_sdk_ec2.types.describe_ipam_policies_result
    import aws_sdk_ec2.types.describe_ipam_pool_allocations_max_results
    import aws_sdk_ec2.types.describe_ipam_pool_allocations_request
    import aws_sdk_ec2.types.describe_ipam_pool_allocations_result
    import aws_sdk_ec2.types.describe_ipam_pools_request
    import aws_sdk_ec2.types.describe_ipam_pools_result
    import aws_sdk_ec2.types.describe_ipam_prefix_list_resolver_targets_request
    import aws_sdk_ec2.types.describe_ipam_prefix_list_resolver_targets_result
    import aws_sdk_ec2.types.describe_ipam_prefix_list_resolvers_request
    import aws_sdk_ec2.types.describe_ipam_prefix_list_resolvers_result
    import aws_sdk_ec2.types.describe_ipam_resource_discoveries_request
    import aws_sdk_ec2.types.describe_ipam_resource_discoveries_result
    import aws_sdk_ec2.types.describe_ipam_resource_discovery_associations_request
    import aws_sdk_ec2.types.describe_ipam_resource_discovery_associations_result
    import aws_sdk_ec2.types.describe_ipam_scopes_request
    import aws_sdk_ec2.types.describe_ipam_scopes_result
    import aws_sdk_ec2.types.describe_ipams_request
    import aws_sdk_ec2.types.describe_ipams_result
    import aws_sdk_ec2.types.describe_ipv6_pools_request
    import aws_sdk_ec2.types.describe_ipv6_pools_result
    import aws_sdk_ec2.types.describe_key_pairs_request
    import aws_sdk_ec2.types.describe_key_pairs_result
    import aws_sdk_ec2.types.describe_launch_template_versions_request
    import aws_sdk_ec2.types.describe_launch_template_versions_result
    import aws_sdk_ec2.types.describe_launch_templates_max_results
    import aws_sdk_ec2.types.describe_launch_templates_request
    import aws_sdk_ec2.types.describe_launch_templates_result
    import aws_sdk_ec2.types.describe_local_gateway_route_table_virtual_interface_group_associations_request
    import aws_sdk_ec2.types.describe_local_gateway_route_table_virtual_interface_group_associations_result
    import aws_sdk_ec2.types.describe_local_gateway_route_table_vpc_associations_request
    import aws_sdk_ec2.types.describe_local_gateway_route_table_vpc_associations_result
    import aws_sdk_ec2.types.describe_local_gateway_route_tables_request
    import aws_sdk_ec2.types.describe_local_gateway_route_tables_result
    import aws_sdk_ec2.types.describe_local_gateway_virtual_interface_groups_request
    import aws_sdk_ec2.types.describe_local_gateway_virtual_interface_groups_result
    import aws_sdk_ec2.types.describe_local_gateway_virtual_interfaces_request
    import aws_sdk_ec2.types.describe_local_gateway_virtual_interfaces_result
    import aws_sdk_ec2.types.describe_local_gateways_request
    import aws_sdk_ec2.types.describe_local_gateways_result
    import aws_sdk_ec2.types.describe_locked_snapshots_max_results
    import aws_sdk_ec2.types.describe_locked_snapshots_request
    import aws_sdk_ec2.types.describe_locked_snapshots_result
    import aws_sdk_ec2.types.describe_mac_hosts_request
    import aws_sdk_ec2.types.describe_mac_hosts_request_max_results
    import aws_sdk_ec2.types.describe_mac_hosts_result
    import aws_sdk_ec2.types.describe_mac_modification_tasks_max_results
    import aws_sdk_ec2.types.describe_mac_modification_tasks_request
    import aws_sdk_ec2.types.describe_mac_modification_tasks_result
    import aws_sdk_ec2.types.describe_managed_prefix_lists_request
    import aws_sdk_ec2.types.describe_managed_prefix_lists_result
    import aws_sdk_ec2.types.describe_moving_addresses_max_results
    import aws_sdk_ec2.types.describe_moving_addresses_request
    import aws_sdk_ec2.types.describe_moving_addresses_result
    import aws_sdk_ec2.types.describe_nat_gateways_max_results
    import aws_sdk_ec2.types.describe_nat_gateways_request
    import aws_sdk_ec2.types.describe_nat_gateways_result
    import aws_sdk_ec2.types.describe_network_acls_max_results
    import aws_sdk_ec2.types.describe_network_acls_request
    import aws_sdk_ec2.types.describe_network_acls_result
    import aws_sdk_ec2.types.describe_network_insights_access_scope_analyses_request
    import aws_sdk_ec2.types.describe_network_insights_access_scope_analyses_result
    import aws_sdk_ec2.types.describe_network_insights_access_scopes_request
    import aws_sdk_ec2.types.describe_network_insights_access_scopes_result
    import aws_sdk_ec2.types.describe_network_insights_analyses_request
    import aws_sdk_ec2.types.describe_network_insights_analyses_result
    import aws_sdk_ec2.types.describe_network_insights_paths_request
    import aws_sdk_ec2.types.describe_network_insights_paths_result
    import aws_sdk_ec2.types.describe_network_interface_attribute_request
    import aws_sdk_ec2.types.describe_network_interface_attribute_result
    import aws_sdk_ec2.types.describe_network_interface_permissions_max_results
    import aws_sdk_ec2.types.describe_network_interface_permissions_request
    import aws_sdk_ec2.types.describe_network_interface_permissions_result
    import aws_sdk_ec2.types.describe_network_interfaces_max_results
    import aws_sdk_ec2.types.describe_network_interfaces_request
    import aws_sdk_ec2.types.describe_network_interfaces_result
    import aws_sdk_ec2.types.describe_outpost_lags_request
    import aws_sdk_ec2.types.describe_outpost_lags_result
    import aws_sdk_ec2.types.describe_placement_groups_request
    import aws_sdk_ec2.types.describe_placement_groups_result
    import aws_sdk_ec2.types.describe_prefix_lists_request
    import aws_sdk_ec2.types.describe_prefix_lists_result
    import aws_sdk_ec2.types.describe_principal_id_format_max_results
    import aws_sdk_ec2.types.describe_principal_id_format_request
    import aws_sdk_ec2.types.describe_principal_id_format_result
    import aws_sdk_ec2.types.describe_public_ipv4_pools_request
    import aws_sdk_ec2.types.describe_public_ipv4_pools_result
    import aws_sdk_ec2.types.describe_regions_request
    import aws_sdk_ec2.types.describe_regions_result
    import aws_sdk_ec2.types.describe_replace_root_volume_tasks_max_results
    import aws_sdk_ec2.types.describe_replace_root_volume_tasks_request
    import aws_sdk_ec2.types.describe_replace_root_volume_tasks_result
    import aws_sdk_ec2.types.describe_reserved_instances_listings_request
    import aws_sdk_ec2.types.describe_reserved_instances_listings_result
    import aws_sdk_ec2.types.describe_reserved_instances_modifications_request
    import aws_sdk_ec2.types.describe_reserved_instances_modifications_result
    import aws_sdk_ec2.types.describe_reserved_instances_offerings_request
    import aws_sdk_ec2.types.describe_reserved_instances_offerings_result
    import aws_sdk_ec2.types.describe_reserved_instances_request
    import aws_sdk_ec2.types.describe_reserved_instances_result
    import aws_sdk_ec2.types.describe_route_server_endpoints_request
    import aws_sdk_ec2.types.describe_route_server_endpoints_result
    import aws_sdk_ec2.types.describe_route_server_peers_request
    import aws_sdk_ec2.types.describe_route_server_peers_result
    import aws_sdk_ec2.types.describe_route_servers_request
    import aws_sdk_ec2.types.describe_route_servers_result
    import aws_sdk_ec2.types.describe_route_tables_max_results
    import aws_sdk_ec2.types.describe_route_tables_request
    import aws_sdk_ec2.types.describe_route_tables_result
    import aws_sdk_ec2.types.describe_scheduled_instance_availability_max_results
    import aws_sdk_ec2.types.describe_scheduled_instance_availability_request
    import aws_sdk_ec2.types.describe_scheduled_instance_availability_result
    import aws_sdk_ec2.types.describe_scheduled_instances_request
    import aws_sdk_ec2.types.describe_scheduled_instances_result
    import aws_sdk_ec2.types.describe_secondary_interfaces_max_results
    import aws_sdk_ec2.types.describe_secondary_interfaces_request
    import aws_sdk_ec2.types.describe_secondary_interfaces_result
    import aws_sdk_ec2.types.describe_secondary_networks_max_results
    import aws_sdk_ec2.types.describe_secondary_networks_request
    import aws_sdk_ec2.types.describe_secondary_networks_result
    import aws_sdk_ec2.types.describe_secondary_subnets_max_results
    import aws_sdk_ec2.types.describe_secondary_subnets_request
    import aws_sdk_ec2.types.describe_secondary_subnets_result
    import aws_sdk_ec2.types.describe_security_group_references_request
    import aws_sdk_ec2.types.describe_security_group_references_result
    import aws_sdk_ec2.types.describe_security_group_rules_max_results
    import aws_sdk_ec2.types.describe_security_group_rules_request
    import aws_sdk_ec2.types.describe_security_group_rules_result
    import aws_sdk_ec2.types.describe_security_group_vpc_associations_max_results
    import aws_sdk_ec2.types.describe_security_group_vpc_associations_request
    import aws_sdk_ec2.types.describe_security_group_vpc_associations_result
    import aws_sdk_ec2.types.describe_security_groups_max_results
    import aws_sdk_ec2.types.describe_security_groups_request
    import aws_sdk_ec2.types.describe_security_groups_result
    import aws_sdk_ec2.types.describe_service_link_virtual_interfaces_request
    import aws_sdk_ec2.types.describe_service_link_virtual_interfaces_result
    import aws_sdk_ec2.types.describe_snapshot_attribute_request
    import aws_sdk_ec2.types.describe_snapshot_attribute_result
    import aws_sdk_ec2.types.describe_snapshot_tier_status_max_results
    import aws_sdk_ec2.types.describe_snapshot_tier_status_request
    import aws_sdk_ec2.types.describe_snapshot_tier_status_result
    import aws_sdk_ec2.types.describe_snapshots_request
    import aws_sdk_ec2.types.describe_snapshots_result
    import aws_sdk_ec2.types.describe_spot_datafeed_subscription_request
    import aws_sdk_ec2.types.describe_spot_datafeed_subscription_result
    import aws_sdk_ec2.types.describe_spot_fleet_instances_max_results
    import aws_sdk_ec2.types.describe_spot_fleet_instances_request
    import aws_sdk_ec2.types.describe_spot_fleet_instances_response
    import aws_sdk_ec2.types.describe_spot_fleet_request_history_max_results
    import aws_sdk_ec2.types.describe_spot_fleet_request_history_request
    import aws_sdk_ec2.types.describe_spot_fleet_request_history_response
    import aws_sdk_ec2.types.describe_spot_fleet_requests_request
    import aws_sdk_ec2.types.describe_spot_fleet_requests_response
    import aws_sdk_ec2.types.describe_spot_instance_requests_request
    import aws_sdk_ec2.types.describe_spot_instance_requests_result
    import aws_sdk_ec2.types.describe_spot_price_history_request
    import aws_sdk_ec2.types.describe_spot_price_history_result
    import aws_sdk_ec2.types.describe_stale_security_groups_max_results
    import aws_sdk_ec2.types.describe_stale_security_groups_next_token
    import aws_sdk_ec2.types.describe_stale_security_groups_request
    import aws_sdk_ec2.types.describe_stale_security_groups_result
    import aws_sdk_ec2.types.describe_store_image_tasks_request
    import aws_sdk_ec2.types.describe_store_image_tasks_request_max_results
    import aws_sdk_ec2.types.describe_store_image_tasks_result
    import aws_sdk_ec2.types.describe_subnets_max_results
    import aws_sdk_ec2.types.describe_subnets_request
    import aws_sdk_ec2.types.describe_subnets_result
    import aws_sdk_ec2.types.describe_tags_request
    import aws_sdk_ec2.types.describe_tags_result
    import aws_sdk_ec2.types.describe_traffic_mirror_filter_rules_request
    import aws_sdk_ec2.types.describe_traffic_mirror_filter_rules_result
    import aws_sdk_ec2.types.describe_traffic_mirror_filters_request
    import aws_sdk_ec2.types.describe_traffic_mirror_filters_result
    import aws_sdk_ec2.types.describe_traffic_mirror_sessions_request
    import aws_sdk_ec2.types.describe_traffic_mirror_sessions_result
    import aws_sdk_ec2.types.describe_traffic_mirror_targets_request
    import aws_sdk_ec2.types.describe_traffic_mirror_targets_result
    import aws_sdk_ec2.types.describe_transit_gateway_attachments_request
    import aws_sdk_ec2.types.describe_transit_gateway_attachments_result
    import aws_sdk_ec2.types.describe_transit_gateway_connect_peers_request
    import aws_sdk_ec2.types.describe_transit_gateway_connect_peers_result
    import aws_sdk_ec2.types.describe_transit_gateway_connects_request
    import aws_sdk_ec2.types.describe_transit_gateway_connects_result
    import aws_sdk_ec2.types.describe_transit_gateway_metering_policies_request
    import aws_sdk_ec2.types.describe_transit_gateway_metering_policies_result
    import aws_sdk_ec2.types.describe_transit_gateway_multicast_domains_request
    import aws_sdk_ec2.types.describe_transit_gateway_multicast_domains_result
    import aws_sdk_ec2.types.describe_transit_gateway_peering_attachments_request
    import aws_sdk_ec2.types.describe_transit_gateway_peering_attachments_result
    import aws_sdk_ec2.types.describe_transit_gateway_policy_tables_request
    import aws_sdk_ec2.types.describe_transit_gateway_policy_tables_result
    import aws_sdk_ec2.types.describe_transit_gateway_route_table_announcements_request
    import aws_sdk_ec2.types.describe_transit_gateway_route_table_announcements_result
    import aws_sdk_ec2.types.describe_transit_gateway_route_tables_request
    import aws_sdk_ec2.types.describe_transit_gateway_route_tables_result
    import aws_sdk_ec2.types.describe_transit_gateway_vpc_attachments_request
    import aws_sdk_ec2.types.describe_transit_gateway_vpc_attachments_result
    import aws_sdk_ec2.types.describe_transit_gateways_request
    import aws_sdk_ec2.types.describe_transit_gateways_result
    import aws_sdk_ec2.types.describe_trunk_interface_associations_max_results
    import aws_sdk_ec2.types.describe_trunk_interface_associations_request
    import aws_sdk_ec2.types.describe_trunk_interface_associations_result
    import aws_sdk_ec2.types.describe_verified_access_endpoints_max_results
    import aws_sdk_ec2.types.describe_verified_access_endpoints_request
    import aws_sdk_ec2.types.describe_verified_access_endpoints_result
    import aws_sdk_ec2.types.describe_verified_access_group_max_results
    import aws_sdk_ec2.types.describe_verified_access_groups_request
    import aws_sdk_ec2.types.describe_verified_access_groups_result
    import aws_sdk_ec2.types.describe_verified_access_instance_logging_configurations_max_results
    import aws_sdk_ec2.types.describe_verified_access_instance_logging_configurations_request
    import aws_sdk_ec2.types.describe_verified_access_instance_logging_configurations_result
    import aws_sdk_ec2.types.describe_verified_access_instances_max_results
    import aws_sdk_ec2.types.describe_verified_access_instances_request
    import aws_sdk_ec2.types.describe_verified_access_instances_result
    import aws_sdk_ec2.types.describe_verified_access_trust_providers_max_results
    import aws_sdk_ec2.types.describe_verified_access_trust_providers_request
    import aws_sdk_ec2.types.describe_verified_access_trust_providers_result
    import aws_sdk_ec2.types.describe_volume_attribute_request
    import aws_sdk_ec2.types.describe_volume_attribute_result
    import aws_sdk_ec2.types.describe_volume_status_request
    import aws_sdk_ec2.types.describe_volume_status_result
    import aws_sdk_ec2.types.describe_volumes_modifications_request
    import aws_sdk_ec2.types.describe_volumes_modifications_result
    import aws_sdk_ec2.types.describe_volumes_request
    import aws_sdk_ec2.types.describe_volumes_result
    import aws_sdk_ec2.types.describe_vpc_attribute_request
    import aws_sdk_ec2.types.describe_vpc_attribute_result
    import aws_sdk_ec2.types.describe_vpc_block_public_access_exclusions_max_results
    import aws_sdk_ec2.types.describe_vpc_block_public_access_exclusions_request
    import aws_sdk_ec2.types.describe_vpc_block_public_access_exclusions_result
    import aws_sdk_ec2.types.describe_vpc_block_public_access_options_request
    import aws_sdk_ec2.types.describe_vpc_block_public_access_options_result
    import aws_sdk_ec2.types.describe_vpc_classic_link_dns_support_max_results
    import aws_sdk_ec2.types.describe_vpc_classic_link_dns_support_next_token
    import aws_sdk_ec2.types.describe_vpc_classic_link_dns_support_request
    import aws_sdk_ec2.types.describe_vpc_classic_link_dns_support_result
    import aws_sdk_ec2.types.describe_vpc_classic_link_request
    import aws_sdk_ec2.types.describe_vpc_classic_link_result
    import aws_sdk_ec2.types.describe_vpc_encryption_controls_max_results
    import aws_sdk_ec2.types.describe_vpc_encryption_controls_request
    import aws_sdk_ec2.types.describe_vpc_encryption_controls_result
    import aws_sdk_ec2.types.describe_vpc_endpoint_associations_request
    import aws_sdk_ec2.types.describe_vpc_endpoint_associations_result
    import aws_sdk_ec2.types.describe_vpc_endpoint_connection_notifications_request
    import aws_sdk_ec2.types.describe_vpc_endpoint_connection_notifications_result
    import aws_sdk_ec2.types.describe_vpc_endpoint_connections_request
    import aws_sdk_ec2.types.describe_vpc_endpoint_connections_result
    import aws_sdk_ec2.types.describe_vpc_endpoint_service_configurations_request
    import aws_sdk_ec2.types.describe_vpc_endpoint_service_configurations_result
    import aws_sdk_ec2.types.describe_vpc_endpoint_service_permissions_request
    import aws_sdk_ec2.types.describe_vpc_endpoint_service_permissions_result
    import aws_sdk_ec2.types.describe_vpc_endpoint_services_request
    import aws_sdk_ec2.types.describe_vpc_endpoint_services_result
    import aws_sdk_ec2.types.describe_vpc_endpoints_request
    import aws_sdk_ec2.types.describe_vpc_endpoints_result
    import aws_sdk_ec2.types.describe_vpc_peering_connections_max_results
    import aws_sdk_ec2.types.describe_vpc_peering_connections_request
    import aws_sdk_ec2.types.describe_vpc_peering_connections_result
    import aws_sdk_ec2.types.describe_vpcs_max_results
    import aws_sdk_ec2.types.describe_vpcs_request
    import aws_sdk_ec2.types.describe_vpcs_result
    import aws_sdk_ec2.types.describe_vpn_concentrators_request
    import aws_sdk_ec2.types.describe_vpn_concentrators_result
    import aws_sdk_ec2.types.describe_vpn_connections_request
    import aws_sdk_ec2.types.describe_vpn_connections_result
    import aws_sdk_ec2.types.describe_vpn_gateways_request
    import aws_sdk_ec2.types.describe_vpn_gateways_result
    import aws_sdk_ec2.types.destination_options_request
    import aws_sdk_ec2.types.detach_classic_link_vpc_request
    import aws_sdk_ec2.types.detach_classic_link_vpc_result
    import aws_sdk_ec2.types.detach_internet_gateway_request
    import aws_sdk_ec2.types.detach_network_interface_request
    import aws_sdk_ec2.types.detach_verified_access_trust_provider_request
    import aws_sdk_ec2.types.detach_verified_access_trust_provider_result
    import aws_sdk_ec2.types.detach_volume_request
    import aws_sdk_ec2.types.detach_vpn_gateway_request
    import aws_sdk_ec2.types.device_trust_provider_type
    import aws_sdk_ec2.types.dhcp_options
    import aws_sdk_ec2.types.dhcp_options_id
    import aws_sdk_ec2.types.dhcp_options_id_string_list
    import aws_sdk_ec2.types.disable_address_transfer_request
    import aws_sdk_ec2.types.disable_address_transfer_result
    import aws_sdk_ec2.types.disable_allowed_images_settings_request
    import aws_sdk_ec2.types.disable_allowed_images_settings_result
    import aws_sdk_ec2.types.disable_aws_network_performance_metric_subscription_request
    import aws_sdk_ec2.types.disable_aws_network_performance_metric_subscription_result
    import aws_sdk_ec2.types.disable_capacity_manager_request
    import aws_sdk_ec2.types.disable_capacity_manager_result
    import aws_sdk_ec2.types.disable_ebs_encryption_by_default_request
    import aws_sdk_ec2.types.disable_ebs_encryption_by_default_result
    import aws_sdk_ec2.types.disable_fast_launch_request
    import aws_sdk_ec2.types.disable_fast_launch_result
    import aws_sdk_ec2.types.disable_fast_snapshot_restores_request
    import aws_sdk_ec2.types.disable_fast_snapshot_restores_result
    import aws_sdk_ec2.types.disable_image_block_public_access_request
    import aws_sdk_ec2.types.disable_image_block_public_access_result
    import aws_sdk_ec2.types.disable_image_deprecation_request
    import aws_sdk_ec2.types.disable_image_deprecation_result
    import aws_sdk_ec2.types.disable_image_deregistration_protection_request
    import aws_sdk_ec2.types.disable_image_deregistration_protection_result
    import aws_sdk_ec2.types.disable_image_request
    import aws_sdk_ec2.types.disable_image_result
    import aws_sdk_ec2.types.disable_instance_sql_ha_standby_detections_request
    import aws_sdk_ec2.types.disable_instance_sql_ha_standby_detections_result
    import aws_sdk_ec2.types.disable_ipam_organization_admin_account_request
    import aws_sdk_ec2.types.disable_ipam_organization_admin_account_result
    import aws_sdk_ec2.types.disable_ipam_policy_request
    import aws_sdk_ec2.types.disable_ipam_policy_result
    import aws_sdk_ec2.types.disable_route_server_propagation_request
    import aws_sdk_ec2.types.disable_route_server_propagation_result
    import aws_sdk_ec2.types.disable_serial_console_access_request
    import aws_sdk_ec2.types.disable_serial_console_access_result
    import aws_sdk_ec2.types.disable_snapshot_block_public_access_request
    import aws_sdk_ec2.types.disable_snapshot_block_public_access_result
    import aws_sdk_ec2.types.disable_transit_gateway_route_table_propagation_request
    import aws_sdk_ec2.types.disable_transit_gateway_route_table_propagation_result
    import aws_sdk_ec2.types.disable_vgw_route_propagation_request
    import aws_sdk_ec2.types.disable_vpc_classic_link_dns_support_request
    import aws_sdk_ec2.types.disable_vpc_classic_link_dns_support_result
    import aws_sdk_ec2.types.disable_vpc_classic_link_request
    import aws_sdk_ec2.types.disable_vpc_classic_link_result
    import aws_sdk_ec2.types.disassociate_address_request
    import aws_sdk_ec2.types.disassociate_capacity_reservation_billing_owner_request
    import aws_sdk_ec2.types.disassociate_capacity_reservation_billing_owner_result
    import aws_sdk_ec2.types.disassociate_client_vpn_target_network_request
    import aws_sdk_ec2.types.disassociate_client_vpn_target_network_result
    import aws_sdk_ec2.types.disassociate_enclave_certificate_iam_role_request
    import aws_sdk_ec2.types.disassociate_enclave_certificate_iam_role_result
    import aws_sdk_ec2.types.disassociate_iam_instance_profile_request
    import aws_sdk_ec2.types.disassociate_iam_instance_profile_result
    import aws_sdk_ec2.types.disassociate_instance_event_window_request
    import aws_sdk_ec2.types.disassociate_instance_event_window_result
    import aws_sdk_ec2.types.disassociate_ipam_byoasn_request
    import aws_sdk_ec2.types.disassociate_ipam_byoasn_result
    import aws_sdk_ec2.types.disassociate_ipam_resource_discovery_request
    import aws_sdk_ec2.types.disassociate_ipam_resource_discovery_result
    import aws_sdk_ec2.types.disassociate_nat_gateway_address_request
    import aws_sdk_ec2.types.disassociate_nat_gateway_address_result
    import aws_sdk_ec2.types.disassociate_route_server_request
    import aws_sdk_ec2.types.disassociate_route_server_result
    import aws_sdk_ec2.types.disassociate_route_table_request
    import aws_sdk_ec2.types.disassociate_security_group_vpc_request
    import aws_sdk_ec2.types.disassociate_security_group_vpc_result
    import aws_sdk_ec2.types.disassociate_security_group_vpc_security_group_id
    import aws_sdk_ec2.types.disassociate_subnet_cidr_block_request
    import aws_sdk_ec2.types.disassociate_subnet_cidr_block_result
    import aws_sdk_ec2.types.disassociate_transit_gateway_multicast_domain_request
    import aws_sdk_ec2.types.disassociate_transit_gateway_multicast_domain_result
    import aws_sdk_ec2.types.disassociate_transit_gateway_policy_table_request
    import aws_sdk_ec2.types.disassociate_transit_gateway_policy_table_result
    import aws_sdk_ec2.types.disassociate_transit_gateway_route_table_request
    import aws_sdk_ec2.types.disassociate_transit_gateway_route_table_result
    import aws_sdk_ec2.types.disassociate_trunk_interface_request
    import aws_sdk_ec2.types.disassociate_trunk_interface_result
    import aws_sdk_ec2.types.disassociate_vpc_cidr_block_request
    import aws_sdk_ec2.types.disassociate_vpc_cidr_block_result
    import aws_sdk_ec2.types.disk_image_detail
    import aws_sdk_ec2.types.disk_image_format
    import aws_sdk_ec2.types.disk_image_list
    import aws_sdk_ec2.types.dit_max_results
    import aws_sdk_ec2.types.dito_max_results
    import aws_sdk_ec2.types.dns_options_specification
    import aws_sdk_ec2.types.dns_servers_options_modify_structure
    import aws_sdk_ec2.types.domain_type
    import aws_sdk_ec2.types.drain_seconds
    import aws_sdk_ec2.types.ec2_instance_connect_endpoint
    import aws_sdk_ec2.types.egress_only_internet_gateway
    import aws_sdk_ec2.types.egress_only_internet_gateway_id
    import aws_sdk_ec2.types.egress_only_internet_gateway_id_list
    import aws_sdk_ec2.types.eip_allocation_public_ip
    import aws_sdk_ec2.types.eip_association_id_list
    import aws_sdk_ec2.types.ek_pub_key_format
    import aws_sdk_ec2.types.ek_pub_key_type
    import aws_sdk_ec2.types.elastic_gpu_id_set
    import aws_sdk_ec2.types.elastic_gpu_specifications
    import aws_sdk_ec2.types.elastic_inference_accelerators
    import aws_sdk_ec2.types.elastic_ip_association_id
    import aws_sdk_ec2.types.ena_srd_specification
    import aws_sdk_ec2.types.enable_address_transfer_request
    import aws_sdk_ec2.types.enable_address_transfer_result
    import aws_sdk_ec2.types.enable_allowed_images_settings_request
    import aws_sdk_ec2.types.enable_allowed_images_settings_result
    import aws_sdk_ec2.types.enable_aws_network_performance_metric_subscription_request
    import aws_sdk_ec2.types.enable_aws_network_performance_metric_subscription_result
    import aws_sdk_ec2.types.enable_capacity_manager_request
    import aws_sdk_ec2.types.enable_capacity_manager_result
    import aws_sdk_ec2.types.enable_ebs_encryption_by_default_request
    import aws_sdk_ec2.types.enable_ebs_encryption_by_default_result
    import aws_sdk_ec2.types.enable_fast_launch_request
    import aws_sdk_ec2.types.enable_fast_launch_result
    import aws_sdk_ec2.types.enable_fast_snapshot_restores_request
    import aws_sdk_ec2.types.enable_fast_snapshot_restores_result
    import aws_sdk_ec2.types.enable_image_block_public_access_request
    import aws_sdk_ec2.types.enable_image_block_public_access_result
    import aws_sdk_ec2.types.enable_image_deprecation_request
    import aws_sdk_ec2.types.enable_image_deprecation_result
    import aws_sdk_ec2.types.enable_image_deregistration_protection_request
    import aws_sdk_ec2.types.enable_image_deregistration_protection_result
    import aws_sdk_ec2.types.enable_image_request
    import aws_sdk_ec2.types.enable_image_result
    import aws_sdk_ec2.types.enable_instance_sql_ha_standby_detections_request
    import aws_sdk_ec2.types.enable_instance_sql_ha_standby_detections_result
    import aws_sdk_ec2.types.enable_ipam_organization_admin_account_request
    import aws_sdk_ec2.types.enable_ipam_organization_admin_account_result
    import aws_sdk_ec2.types.enable_ipam_policy_request
    import aws_sdk_ec2.types.enable_ipam_policy_result
    import aws_sdk_ec2.types.enable_reachability_analyzer_organization_sharing_request
    import aws_sdk_ec2.types.enable_reachability_analyzer_organization_sharing_result
    import aws_sdk_ec2.types.enable_route_server_propagation_request
    import aws_sdk_ec2.types.enable_route_server_propagation_result
    import aws_sdk_ec2.types.enable_serial_console_access_request
    import aws_sdk_ec2.types.enable_serial_console_access_result
    import aws_sdk_ec2.types.enable_snapshot_block_public_access_request
    import aws_sdk_ec2.types.enable_snapshot_block_public_access_result
    import aws_sdk_ec2.types.enable_transit_gateway_route_table_propagation_request
    import aws_sdk_ec2.types.enable_transit_gateway_route_table_propagation_result
    import aws_sdk_ec2.types.enable_vgw_route_propagation_request
    import aws_sdk_ec2.types.enable_volume_io_request
    import aws_sdk_ec2.types.enable_vpc_classic_link_dns_support_request
    import aws_sdk_ec2.types.enable_vpc_classic_link_dns_support_result
    import aws_sdk_ec2.types.enable_vpc_classic_link_request
    import aws_sdk_ec2.types.enable_vpc_classic_link_result
    import aws_sdk_ec2.types.enclave_options_request
    import aws_sdk_ec2.types.end_date_type
    import aws_sdk_ec2.types.endpoint_ip_address_type
    import aws_sdk_ec2.types.event_type
    import aws_sdk_ec2.types.excess_capacity_termination_policy
    import aws_sdk_ec2.types.executable_by_string_list
    import aws_sdk_ec2.types.export_client_vpn_client_certificate_revocation_list_request
    import aws_sdk_ec2.types.export_client_vpn_client_certificate_revocation_list_result
    import aws_sdk_ec2.types.export_client_vpn_client_configuration_request
    import aws_sdk_ec2.types.export_client_vpn_client_configuration_result
    import aws_sdk_ec2.types.export_environment
    import aws_sdk_ec2.types.export_image_request
    import aws_sdk_ec2.types.export_image_result
    import aws_sdk_ec2.types.export_image_task
    import aws_sdk_ec2.types.export_image_task_id_list
    import aws_sdk_ec2.types.export_task_id_string_list
    import aws_sdk_ec2.types.export_task_s3_location_request
    import aws_sdk_ec2.types.export_to_s3_task_specification
    import aws_sdk_ec2.types.export_transit_gateway_routes_request
    import aws_sdk_ec2.types.export_transit_gateway_routes_result
    import aws_sdk_ec2.types.export_verified_access_instance_client_configuration_request
    import aws_sdk_ec2.types.export_verified_access_instance_client_configuration_result
    import aws_sdk_ec2.types.export_vm_task_id
    import aws_sdk_ec2.types.external_authority_configuration
    import aws_sdk_ec2.types.fast_launch_image_id_list
    import aws_sdk_ec2.types.fast_launch_launch_template_specification_request
    import aws_sdk_ec2.types.fast_launch_snapshot_configuration_request
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.fleet_capacity_reservation_tenancy
    import aws_sdk_ec2.types.fleet_data
    import aws_sdk_ec2.types.fleet_event_type
    import aws_sdk_ec2.types.fleet_excess_capacity_termination_policy
    import aws_sdk_ec2.types.fleet_id
    import aws_sdk_ec2.types.fleet_id_set
    import aws_sdk_ec2.types.fleet_instance_match_criteria
    import aws_sdk_ec2.types.fleet_launch_template_config_list_request
    import aws_sdk_ec2.types.fleet_type
    import aws_sdk_ec2.types.flow_log
    import aws_sdk_ec2.types.flow_log_id_list
    import aws_sdk_ec2.types.flow_log_resource_ids
    import aws_sdk_ec2.types.flow_logs_resource_type
    import aws_sdk_ec2.types.fpga_image
    import aws_sdk_ec2.types.fpga_image_attribute_name
    import aws_sdk_ec2.types.fpga_image_id
    import aws_sdk_ec2.types.fpga_image_id_list
    import aws_sdk_ec2.types.gateway_type
    import aws_sdk_ec2.types.get_active_vpn_tunnel_status_request
    import aws_sdk_ec2.types.get_active_vpn_tunnel_status_result
    import aws_sdk_ec2.types.get_allowed_images_settings_request
    import aws_sdk_ec2.types.get_allowed_images_settings_result
    import aws_sdk_ec2.types.get_associated_enclave_certificate_iam_roles_request
    import aws_sdk_ec2.types.get_associated_enclave_certificate_iam_roles_result
    import aws_sdk_ec2.types.get_associated_ipv6_pool_cidrs_request
    import aws_sdk_ec2.types.get_associated_ipv6_pool_cidrs_result
    import aws_sdk_ec2.types.get_aws_network_performance_data_request
    import aws_sdk_ec2.types.get_aws_network_performance_data_result
    import aws_sdk_ec2.types.get_capacity_manager_attributes_request
    import aws_sdk_ec2.types.get_capacity_manager_attributes_result
    import aws_sdk_ec2.types.get_capacity_manager_metric_data_request
    import aws_sdk_ec2.types.get_capacity_manager_metric_data_result
    import aws_sdk_ec2.types.get_capacity_manager_metric_dimensions_request
    import aws_sdk_ec2.types.get_capacity_manager_metric_dimensions_result
    import aws_sdk_ec2.types.get_capacity_manager_monitored_tag_keys_request
    import aws_sdk_ec2.types.get_capacity_manager_monitored_tag_keys_request_max_results
    import aws_sdk_ec2.types.get_capacity_manager_monitored_tag_keys_result
    import aws_sdk_ec2.types.get_capacity_reservation_usage_request
    import aws_sdk_ec2.types.get_capacity_reservation_usage_request_max_results
    import aws_sdk_ec2.types.get_capacity_reservation_usage_result
    import aws_sdk_ec2.types.get_coip_pool_usage_request
    import aws_sdk_ec2.types.get_coip_pool_usage_result
    import aws_sdk_ec2.types.get_console_output_request
    import aws_sdk_ec2.types.get_console_output_result
    import aws_sdk_ec2.types.get_console_screenshot_request
    import aws_sdk_ec2.types.get_console_screenshot_result
    import aws_sdk_ec2.types.get_declarative_policies_report_summary_request
    import aws_sdk_ec2.types.get_declarative_policies_report_summary_result
    import aws_sdk_ec2.types.get_default_credit_specification_request
    import aws_sdk_ec2.types.get_default_credit_specification_result
    import aws_sdk_ec2.types.get_ebs_default_kms_key_id_request
    import aws_sdk_ec2.types.get_ebs_default_kms_key_id_result
    import aws_sdk_ec2.types.get_ebs_encryption_by_default_request
    import aws_sdk_ec2.types.get_ebs_encryption_by_default_result
    import aws_sdk_ec2.types.get_enabled_ipam_policy_request
    import aws_sdk_ec2.types.get_enabled_ipam_policy_result
    import aws_sdk_ec2.types.get_flow_logs_integration_template_request
    import aws_sdk_ec2.types.get_flow_logs_integration_template_result
    import aws_sdk_ec2.types.get_groups_for_capacity_reservation_request
    import aws_sdk_ec2.types.get_groups_for_capacity_reservation_request_max_results
    import aws_sdk_ec2.types.get_groups_for_capacity_reservation_result
    import aws_sdk_ec2.types.get_host_reservation_purchase_preview_request
    import aws_sdk_ec2.types.get_host_reservation_purchase_preview_result
    import aws_sdk_ec2.types.get_image_ancestry_request
    import aws_sdk_ec2.types.get_image_ancestry_result
    import aws_sdk_ec2.types.get_image_block_public_access_state_request
    import aws_sdk_ec2.types.get_image_block_public_access_state_result
    import aws_sdk_ec2.types.get_instance_metadata_defaults_request
    import aws_sdk_ec2.types.get_instance_metadata_defaults_result
    import aws_sdk_ec2.types.get_instance_tpm_ek_pub_request
    import aws_sdk_ec2.types.get_instance_tpm_ek_pub_result
    import aws_sdk_ec2.types.get_instance_types_from_instance_requirements_request
    import aws_sdk_ec2.types.get_instance_types_from_instance_requirements_result
    import aws_sdk_ec2.types.get_instance_uefi_data_request
    import aws_sdk_ec2.types.get_instance_uefi_data_result
    import aws_sdk_ec2.types.get_ipam_address_history_request
    import aws_sdk_ec2.types.get_ipam_address_history_result
    import aws_sdk_ec2.types.get_ipam_discovered_accounts_request
    import aws_sdk_ec2.types.get_ipam_discovered_accounts_result
    import aws_sdk_ec2.types.get_ipam_discovered_public_addresses_request
    import aws_sdk_ec2.types.get_ipam_discovered_public_addresses_result
    import aws_sdk_ec2.types.get_ipam_discovered_resource_cidrs_request
    import aws_sdk_ec2.types.get_ipam_discovered_resource_cidrs_result
    import aws_sdk_ec2.types.get_ipam_policy_allocation_rules_request
    import aws_sdk_ec2.types.get_ipam_policy_allocation_rules_result
    import aws_sdk_ec2.types.get_ipam_policy_organization_targets_request
    import aws_sdk_ec2.types.get_ipam_policy_organization_targets_result
    import aws_sdk_ec2.types.get_ipam_pool_allocations_max_results
    import aws_sdk_ec2.types.get_ipam_pool_allocations_request
    import aws_sdk_ec2.types.get_ipam_pool_allocations_result
    import aws_sdk_ec2.types.get_ipam_pool_cidrs_request
    import aws_sdk_ec2.types.get_ipam_pool_cidrs_result
    import aws_sdk_ec2.types.get_ipam_prefix_list_resolver_rules_request
    import aws_sdk_ec2.types.get_ipam_prefix_list_resolver_rules_result
    import aws_sdk_ec2.types.get_ipam_prefix_list_resolver_version_entries_request
    import aws_sdk_ec2.types.get_ipam_prefix_list_resolver_version_entries_result
    import aws_sdk_ec2.types.get_ipam_prefix_list_resolver_versions_request
    import aws_sdk_ec2.types.get_ipam_prefix_list_resolver_versions_result
    import aws_sdk_ec2.types.get_ipam_resource_cidrs_request
    import aws_sdk_ec2.types.get_ipam_resource_cidrs_result
    import aws_sdk_ec2.types.get_launch_template_data_request
    import aws_sdk_ec2.types.get_launch_template_data_result
    import aws_sdk_ec2.types.get_managed_prefix_list_associations_max_results
    import aws_sdk_ec2.types.get_managed_prefix_list_associations_request
    import aws_sdk_ec2.types.get_managed_prefix_list_associations_result
    import aws_sdk_ec2.types.get_managed_prefix_list_entries_request
    import aws_sdk_ec2.types.get_managed_prefix_list_entries_result
    import aws_sdk_ec2.types.get_managed_resource_visibility_request
    import aws_sdk_ec2.types.get_managed_resource_visibility_result
    import aws_sdk_ec2.types.get_network_insights_access_scope_analysis_findings_max_results
    import aws_sdk_ec2.types.get_network_insights_access_scope_analysis_findings_request
    import aws_sdk_ec2.types.get_network_insights_access_scope_analysis_findings_result
    import aws_sdk_ec2.types.get_network_insights_access_scope_content_request
    import aws_sdk_ec2.types.get_network_insights_access_scope_content_result
    import aws_sdk_ec2.types.get_password_data_request
    import aws_sdk_ec2.types.get_password_data_result
    import aws_sdk_ec2.types.get_reserved_instances_exchange_quote_request
    import aws_sdk_ec2.types.get_reserved_instances_exchange_quote_result
    import aws_sdk_ec2.types.get_route_server_associations_request
    import aws_sdk_ec2.types.get_route_server_associations_result
    import aws_sdk_ec2.types.get_route_server_propagations_request
    import aws_sdk_ec2.types.get_route_server_propagations_result
    import aws_sdk_ec2.types.get_route_server_routing_database_request
    import aws_sdk_ec2.types.get_route_server_routing_database_result
    import aws_sdk_ec2.types.get_security_groups_for_vpc_request
    import aws_sdk_ec2.types.get_security_groups_for_vpc_request_max_results
    import aws_sdk_ec2.types.get_security_groups_for_vpc_result
    import aws_sdk_ec2.types.get_serial_console_access_status_request
    import aws_sdk_ec2.types.get_serial_console_access_status_result
    import aws_sdk_ec2.types.get_snapshot_block_public_access_state_request
    import aws_sdk_ec2.types.get_snapshot_block_public_access_state_result
    import aws_sdk_ec2.types.get_spot_placement_scores_request
    import aws_sdk_ec2.types.get_spot_placement_scores_result
    import aws_sdk_ec2.types.get_subnet_cidr_reservations_max_results
    import aws_sdk_ec2.types.get_subnet_cidr_reservations_request
    import aws_sdk_ec2.types.get_subnet_cidr_reservations_result
    import aws_sdk_ec2.types.get_transit_gateway_attachment_propagations_request
    import aws_sdk_ec2.types.get_transit_gateway_attachment_propagations_result
    import aws_sdk_ec2.types.get_transit_gateway_metering_policy_entries_request
    import aws_sdk_ec2.types.get_transit_gateway_metering_policy_entries_result
    import aws_sdk_ec2.types.get_transit_gateway_multicast_domain_associations_request
    import aws_sdk_ec2.types.get_transit_gateway_multicast_domain_associations_result
    import aws_sdk_ec2.types.get_transit_gateway_policy_table_associations_request
    import aws_sdk_ec2.types.get_transit_gateway_policy_table_associations_result
    import aws_sdk_ec2.types.get_transit_gateway_policy_table_entries_request
    import aws_sdk_ec2.types.get_transit_gateway_policy_table_entries_result
    import aws_sdk_ec2.types.get_transit_gateway_prefix_list_references_request
    import aws_sdk_ec2.types.get_transit_gateway_prefix_list_references_result
    import aws_sdk_ec2.types.get_transit_gateway_route_table_associations_request
    import aws_sdk_ec2.types.get_transit_gateway_route_table_associations_result
    import aws_sdk_ec2.types.get_transit_gateway_route_table_propagations_request
    import aws_sdk_ec2.types.get_transit_gateway_route_table_propagations_result
    import aws_sdk_ec2.types.get_verified_access_endpoint_policy_request
    import aws_sdk_ec2.types.get_verified_access_endpoint_policy_result
    import aws_sdk_ec2.types.get_verified_access_endpoint_targets_max_results
    import aws_sdk_ec2.types.get_verified_access_endpoint_targets_request
    import aws_sdk_ec2.types.get_verified_access_endpoint_targets_result
    import aws_sdk_ec2.types.get_verified_access_group_policy_request
    import aws_sdk_ec2.types.get_verified_access_group_policy_result
    import aws_sdk_ec2.types.get_vpc_resources_blocking_encryption_enforcement_max_results
    import aws_sdk_ec2.types.get_vpc_resources_blocking_encryption_enforcement_request
    import aws_sdk_ec2.types.get_vpc_resources_blocking_encryption_enforcement_result
    import aws_sdk_ec2.types.get_vpn_connection_device_sample_configuration_request
    import aws_sdk_ec2.types.get_vpn_connection_device_sample_configuration_result
    import aws_sdk_ec2.types.get_vpn_connection_device_types_request
    import aws_sdk_ec2.types.get_vpn_connection_device_types_result
    import aws_sdk_ec2.types.get_vpn_tunnel_replacement_status_request
    import aws_sdk_ec2.types.get_vpn_tunnel_replacement_status_result
    import aws_sdk_ec2.types.group_by_set
    import aws_sdk_ec2.types.group_id_string_list
    import aws_sdk_ec2.types.group_ids
    import aws_sdk_ec2.types.group_name_string_list
    import aws_sdk_ec2.types.gvcd_max_results
    import aws_sdk_ec2.types.hibernation_options_request
    import aws_sdk_ec2.types.host
    import aws_sdk_ec2.types.host_maintenance
    import aws_sdk_ec2.types.host_offering
    import aws_sdk_ec2.types.host_recovery
    import aws_sdk_ec2.types.host_reservation
    import aws_sdk_ec2.types.host_reservation_id_set
    import aws_sdk_ec2.types.host_tenancy
    import aws_sdk_ec2.types.hostname_type
    import aws_sdk_ec2.types.http_tokens_state
    import aws_sdk_ec2.types.iam_instance_profile_association
    import aws_sdk_ec2.types.iam_instance_profile_association_id
    import aws_sdk_ec2.types.iam_instance_profile_specification
    import aws_sdk_ec2.types.icmp_type_code
    import aws_sdk_ec2.types.image
    import aws_sdk_ec2.types.image_attribute
    import aws_sdk_ec2.types.image_attribute_name
    import aws_sdk_ec2.types.image_block_public_access_enabled_state
    import aws_sdk_ec2.types.image_criterion_request_list
    import aws_sdk_ec2.types.image_description_request
    import aws_sdk_ec2.types.image_disk_container_list
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.image_id_list
    import aws_sdk_ec2.types.image_id_string_list
    import aws_sdk_ec2.types.image_name_request
    import aws_sdk_ec2.types.image_recycle_bin_info
    import aws_sdk_ec2.types.image_reference
    import aws_sdk_ec2.types.image_uefi_data_request
    import aws_sdk_ec2.types.image_usage_report
    import aws_sdk_ec2.types.image_usage_report_entry
    import aws_sdk_ec2.types.image_usage_report_id
    import aws_sdk_ec2.types.image_usage_report_id_string_list
    import aws_sdk_ec2.types.image_usage_report_user_id_string_list
    import aws_sdk_ec2.types.image_usage_resource_type_request_list
    import aws_sdk_ec2.types.imds_support_values
    import aws_sdk_ec2.types.import_client_vpn_client_certificate_revocation_list_request
    import aws_sdk_ec2.types.import_client_vpn_client_certificate_revocation_list_result
    import aws_sdk_ec2.types.import_image_license_specification_list_request
    import aws_sdk_ec2.types.import_image_request
    import aws_sdk_ec2.types.import_image_result
    import aws_sdk_ec2.types.import_image_task
    import aws_sdk_ec2.types.import_instance_launch_specification
    import aws_sdk_ec2.types.import_instance_request
    import aws_sdk_ec2.types.import_instance_result
    import aws_sdk_ec2.types.import_key_pair_request
    import aws_sdk_ec2.types.import_key_pair_result
    import aws_sdk_ec2.types.import_snapshot_request
    import aws_sdk_ec2.types.import_snapshot_result
    import aws_sdk_ec2.types.import_snapshot_task
    import aws_sdk_ec2.types.import_snapshot_task_id_list
    import aws_sdk_ec2.types.import_task_id
    import aws_sdk_ec2.types.import_task_id_list
    import aws_sdk_ec2.types.import_volume_request
    import aws_sdk_ec2.types.import_volume_result
    import aws_sdk_ec2.types.include_unsupported_in_region
    import aws_sdk_ec2.types.inside_cidr_blocks_string_list
    import aws_sdk_ec2.types.instance_attribute
    import aws_sdk_ec2.types.instance_attribute_name
    import aws_sdk_ec2.types.instance_auto_recovery_state
    import aws_sdk_ec2.types.instance_bandwidth_weighting
    import aws_sdk_ec2.types.instance_block_device_mapping_specification_list
    import aws_sdk_ec2.types.instance_connect_endpoint_id
    import aws_sdk_ec2.types.instance_connect_endpoint_max_results
    import aws_sdk_ec2.types.instance_credit_specification
    import aws_sdk_ec2.types.instance_credit_specification_list_request
    import aws_sdk_ec2.types.instance_event_window
    import aws_sdk_ec2.types.instance_event_window_association_request
    import aws_sdk_ec2.types.instance_event_window_cron_expression
    import aws_sdk_ec2.types.instance_event_window_disassociation_request
    import aws_sdk_ec2.types.instance_event_window_id
    import aws_sdk_ec2.types.instance_event_window_id_set
    import aws_sdk_ec2.types.instance_event_window_time_range_request_set
    import aws_sdk_ec2.types.instance_id
    import aws_sdk_ec2.types.instance_id_for_resolver
    import aws_sdk_ec2.types.instance_id_string_list
    import aws_sdk_ec2.types.instance_id_update_string_list
    import aws_sdk_ec2.types.instance_image_metadata
    import aws_sdk_ec2.types.instance_interruption_behavior
    import aws_sdk_ec2.types.instance_ipv6_address_list
    import aws_sdk_ec2.types.instance_maintenance_options_request
    import aws_sdk_ec2.types.instance_market_options_request
    import aws_sdk_ec2.types.instance_match_criteria
    import aws_sdk_ec2.types.instance_metadata_endpoint_state
    import aws_sdk_ec2.types.instance_metadata_options_request
    import aws_sdk_ec2.types.instance_metadata_protocol_state
    import aws_sdk_ec2.types.instance_metadata_tags_state
    import aws_sdk_ec2.types.instance_network_interface_specification_list
    import aws_sdk_ec2.types.instance_network_performance_options_request
    import aws_sdk_ec2.types.instance_reboot_migration_state
    import aws_sdk_ec2.types.instance_requirements_request
    import aws_sdk_ec2.types.instance_requirements_with_metadata_request
    import aws_sdk_ec2.types.instance_secondary_interface_specification_list_request
    import aws_sdk_ec2.types.instance_specification
    import aws_sdk_ec2.types.instance_status
    import aws_sdk_ec2.types.instance_topology
    import aws_sdk_ec2.types.instance_type
    import aws_sdk_ec2.types.instance_type_info
    import aws_sdk_ec2.types.instance_type_info_from_instance_requirements
    import aws_sdk_ec2.types.instance_type_list
    import aws_sdk_ec2.types.instance_type_offering
    import aws_sdk_ec2.types.instance_types
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.integrate_services
    import aws_sdk_ec2.types.interface_permission_type
    import aws_sdk_ec2.types.internet_gateway
    import aws_sdk_ec2.types.internet_gateway_block_mode
    import aws_sdk_ec2.types.internet_gateway_exclusion_mode
    import aws_sdk_ec2.types.internet_gateway_id
    import aws_sdk_ec2.types.internet_gateway_id_list
    import aws_sdk_ec2.types.ip_address
    import aws_sdk_ec2.types.ip_address_type
    import aws_sdk_ec2.types.ip_list
    import aws_sdk_ec2.types.ip_permission_list
    import aws_sdk_ec2.types.ip_prefix_list
    import aws_sdk_ec2.types.ipam
    import aws_sdk_ec2.types.ipam_address_history_max_results
    import aws_sdk_ec2.types.ipam_address_history_record
    import aws_sdk_ec2.types.ipam_cidr_authorization_context
    import aws_sdk_ec2.types.ipam_discovered_account
    import aws_sdk_ec2.types.ipam_discovered_resource_cidr
    import aws_sdk_ec2.types.ipam_external_resource_verification_token_id
    import aws_sdk_ec2.types.ipam_id
    import aws_sdk_ec2.types.ipam_max_results
    import aws_sdk_ec2.types.ipam_metered_account
    import aws_sdk_ec2.types.ipam_netmask_length
    import aws_sdk_ec2.types.ipam_policy_allocation_rule_list_request
    import aws_sdk_ec2.types.ipam_policy_id
    import aws_sdk_ec2.types.ipam_policy_resource_type
    import aws_sdk_ec2.types.ipam_pool
    import aws_sdk_ec2.types.ipam_pool_allocation
    import aws_sdk_ec2.types.ipam_pool_allocation_allowed_cidrs
    import aws_sdk_ec2.types.ipam_pool_allocation_disallowed_cidrs
    import aws_sdk_ec2.types.ipam_pool_allocation_id
    import aws_sdk_ec2.types.ipam_pool_aws_service
    import aws_sdk_ec2.types.ipam_pool_cidr
    import aws_sdk_ec2.types.ipam_pool_id
    import aws_sdk_ec2.types.ipam_pool_public_ip_source
    import aws_sdk_ec2.types.ipam_pool_source_resource_request
    import aws_sdk_ec2.types.ipam_prefix_list_resolver
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_id
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_rule
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_request_set
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_target
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_target_id
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_version
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_version_entry
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_version_number_set
    import aws_sdk_ec2.types.ipam_resource_cidr
    import aws_sdk_ec2.types.ipam_resource_discovery
    import aws_sdk_ec2.types.ipam_resource_discovery_association
    import aws_sdk_ec2.types.ipam_resource_discovery_association_id
    import aws_sdk_ec2.types.ipam_resource_discovery_id
    import aws_sdk_ec2.types.ipam_resource_type
    import aws_sdk_ec2.types.ipam_scope
    import aws_sdk_ec2.types.ipam_scope_id
    import aws_sdk_ec2.types.ipam_tier
    import aws_sdk_ec2.types.ipv4_pool_coip_id
    import aws_sdk_ec2.types.ipv4_pool_ec2_id
    import aws_sdk_ec2.types.ipv4_prefix_list
    import aws_sdk_ec2.types.ipv6_address_list
    import aws_sdk_ec2.types.ipv6_cidr_association
    import aws_sdk_ec2.types.ipv6_pool
    import aws_sdk_ec2.types.ipv6_pool_ec2_id
    import aws_sdk_ec2.types.ipv6_pool_id_list
    import aws_sdk_ec2.types.ipv6_pool_max_results
    import aws_sdk_ec2.types.ipv6_prefix_list
    import aws_sdk_ec2.types.kernel_id
    import aws_sdk_ec2.types.key_format
    import aws_sdk_ec2.types.key_name_string_list
    import aws_sdk_ec2.types.key_pair
    import aws_sdk_ec2.types.key_pair_id
    import aws_sdk_ec2.types.key_pair_id_string_list
    import aws_sdk_ec2.types.key_pair_name
    import aws_sdk_ec2.types.key_pair_name_with_resolver
    import aws_sdk_ec2.types.key_type
    import aws_sdk_ec2.types.kms_key_id
    import aws_sdk_ec2.types.launch_permission_modifications
    import aws_sdk_ec2.types.launch_template
    import aws_sdk_ec2.types.launch_template_config_list
    import aws_sdk_ec2.types.launch_template_id
    import aws_sdk_ec2.types.launch_template_id_string_list
    import aws_sdk_ec2.types.launch_template_name
    import aws_sdk_ec2.types.launch_template_name_string_list
    import aws_sdk_ec2.types.launch_template_specification
    import aws_sdk_ec2.types.launch_template_version
    import aws_sdk_ec2.types.license_specification_list_request
    import aws_sdk_ec2.types.list_images_in_recycle_bin_max_results
    import aws_sdk_ec2.types.list_images_in_recycle_bin_request
    import aws_sdk_ec2.types.list_images_in_recycle_bin_result
    import aws_sdk_ec2.types.list_snapshots_in_recycle_bin_max_results
    import aws_sdk_ec2.types.list_snapshots_in_recycle_bin_request
    import aws_sdk_ec2.types.list_snapshots_in_recycle_bin_result
    import aws_sdk_ec2.types.list_volumes_in_recycle_bin_request
    import aws_sdk_ec2.types.list_volumes_in_recycle_bin_result
    import aws_sdk_ec2.types.load_permission_modifications
    import aws_sdk_ec2.types.local_gateway
    import aws_sdk_ec2.types.local_gateway_id
    import aws_sdk_ec2.types.local_gateway_id_set
    import aws_sdk_ec2.types.local_gateway_max_results
    import aws_sdk_ec2.types.local_gateway_route
    import aws_sdk_ec2.types.local_gateway_route_table
    import aws_sdk_ec2.types.local_gateway_route_table_id_set
    import aws_sdk_ec2.types.local_gateway_route_table_mode
    import aws_sdk_ec2.types.local_gateway_route_table_virtual_interface_group_association
    import aws_sdk_ec2.types.local_gateway_route_table_virtual_interface_group_association_id
    import aws_sdk_ec2.types.local_gateway_route_table_virtual_interface_group_association_id_set
    import aws_sdk_ec2.types.local_gateway_route_table_vpc_association
    import aws_sdk_ec2.types.local_gateway_route_table_vpc_association_id
    import aws_sdk_ec2.types.local_gateway_route_table_vpc_association_id_set
    import aws_sdk_ec2.types.local_gateway_routetable_id
    import aws_sdk_ec2.types.local_gateway_virtual_interface
    import aws_sdk_ec2.types.local_gateway_virtual_interface_group
    import aws_sdk_ec2.types.local_gateway_virtual_interface_group_id
    import aws_sdk_ec2.types.local_gateway_virtual_interface_group_id_set
    import aws_sdk_ec2.types.local_gateway_virtual_interface_id
    import aws_sdk_ec2.types.local_gateway_virtual_interface_id_set
    import aws_sdk_ec2.types.location_type
    import aws_sdk_ec2.types.lock_mode
    import aws_sdk_ec2.types.lock_snapshot_request
    import aws_sdk_ec2.types.lock_snapshot_result
    import aws_sdk_ec2.types.log_destination_type
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.mac_host
    import aws_sdk_ec2.types.mac_modification_task
    import aws_sdk_ec2.types.mac_modification_task_id_list
    import aws_sdk_ec2.types.mac_system_integrity_protection_configuration_request
    import aws_sdk_ec2.types.mac_system_integrity_protection_setting_status
    import aws_sdk_ec2.types.managed_prefix_list
    import aws_sdk_ec2.types.managed_resource_default_visibility
    import aws_sdk_ec2.types.max_results
    import aws_sdk_ec2.types.max_results2
    import aws_sdk_ec2.types.max_results_param
    import aws_sdk_ec2.types.metadata_default_http_tokens_state
    import aws_sdk_ec2.types.metric_data_result
    import aws_sdk_ec2.types.metric_set
    import aws_sdk_ec2.types.metric_type
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.modify_address_attribute_request
    import aws_sdk_ec2.types.modify_address_attribute_result
    import aws_sdk_ec2.types.modify_availability_zone_group_request
    import aws_sdk_ec2.types.modify_availability_zone_group_result
    import aws_sdk_ec2.types.modify_availability_zone_opt_in_status
    import aws_sdk_ec2.types.modify_capacity_reservation_fleet_request
    import aws_sdk_ec2.types.modify_capacity_reservation_fleet_result
    import aws_sdk_ec2.types.modify_capacity_reservation_request
    import aws_sdk_ec2.types.modify_capacity_reservation_result
    import aws_sdk_ec2.types.modify_client_vpn_endpoint_request
    import aws_sdk_ec2.types.modify_client_vpn_endpoint_result
    import aws_sdk_ec2.types.modify_default_credit_specification_request
    import aws_sdk_ec2.types.modify_default_credit_specification_result
    import aws_sdk_ec2.types.modify_ebs_default_kms_key_id_request
    import aws_sdk_ec2.types.modify_ebs_default_kms_key_id_result
    import aws_sdk_ec2.types.modify_fleet_request
    import aws_sdk_ec2.types.modify_fleet_result
    import aws_sdk_ec2.types.modify_fpga_image_attribute_request
    import aws_sdk_ec2.types.modify_fpga_image_attribute_result
    import aws_sdk_ec2.types.modify_hosts_request
    import aws_sdk_ec2.types.modify_hosts_result
    import aws_sdk_ec2.types.modify_id_format_request
    import aws_sdk_ec2.types.modify_identity_id_format_request
    import aws_sdk_ec2.types.modify_image_attribute_request
    import aws_sdk_ec2.types.modify_instance_attribute_request
    import aws_sdk_ec2.types.modify_instance_attribute_value
    import aws_sdk_ec2.types.modify_instance_capacity_reservation_attributes_request
    import aws_sdk_ec2.types.modify_instance_capacity_reservation_attributes_result
    import aws_sdk_ec2.types.modify_instance_connect_endpoint_request
    import aws_sdk_ec2.types.modify_instance_connect_endpoint_result
    import aws_sdk_ec2.types.modify_instance_cpu_options_request
    import aws_sdk_ec2.types.modify_instance_cpu_options_result
    import aws_sdk_ec2.types.modify_instance_credit_specification_request
    import aws_sdk_ec2.types.modify_instance_credit_specification_result
    import aws_sdk_ec2.types.modify_instance_event_start_time_request
    import aws_sdk_ec2.types.modify_instance_event_start_time_result
    import aws_sdk_ec2.types.modify_instance_event_window_request
    import aws_sdk_ec2.types.modify_instance_event_window_result
    import aws_sdk_ec2.types.modify_instance_maintenance_options_request
    import aws_sdk_ec2.types.modify_instance_maintenance_options_result
    import aws_sdk_ec2.types.modify_instance_metadata_defaults_request
    import aws_sdk_ec2.types.modify_instance_metadata_defaults_result
    import aws_sdk_ec2.types.modify_instance_metadata_options_request
    import aws_sdk_ec2.types.modify_instance_metadata_options_result
    import aws_sdk_ec2.types.modify_instance_network_performance_request
    import aws_sdk_ec2.types.modify_instance_network_performance_result
    import aws_sdk_ec2.types.modify_instance_placement_request
    import aws_sdk_ec2.types.modify_instance_placement_result
    import aws_sdk_ec2.types.modify_ipam_policy_allocation_rules_request
    import aws_sdk_ec2.types.modify_ipam_policy_allocation_rules_result
    import aws_sdk_ec2.types.modify_ipam_pool_allocation_request
    import aws_sdk_ec2.types.modify_ipam_pool_allocation_result
    import aws_sdk_ec2.types.modify_ipam_pool_request
    import aws_sdk_ec2.types.modify_ipam_pool_result
    import aws_sdk_ec2.types.modify_ipam_prefix_list_resolver_request
    import aws_sdk_ec2.types.modify_ipam_prefix_list_resolver_result
    import aws_sdk_ec2.types.modify_ipam_prefix_list_resolver_target_request
    import aws_sdk_ec2.types.modify_ipam_prefix_list_resolver_target_result
    import aws_sdk_ec2.types.modify_ipam_request
    import aws_sdk_ec2.types.modify_ipam_resource_cidr_request
    import aws_sdk_ec2.types.modify_ipam_resource_cidr_result
    import aws_sdk_ec2.types.modify_ipam_resource_discovery_request
    import aws_sdk_ec2.types.modify_ipam_resource_discovery_result
    import aws_sdk_ec2.types.modify_ipam_result
    import aws_sdk_ec2.types.modify_ipam_scope_request
    import aws_sdk_ec2.types.modify_ipam_scope_result
    import aws_sdk_ec2.types.modify_launch_template_request
    import aws_sdk_ec2.types.modify_launch_template_result
    import aws_sdk_ec2.types.modify_local_gateway_route_request
    import aws_sdk_ec2.types.modify_local_gateway_route_result
    import aws_sdk_ec2.types.modify_managed_prefix_list_request
    import aws_sdk_ec2.types.modify_managed_prefix_list_result
    import aws_sdk_ec2.types.modify_managed_resource_visibility_request
    import aws_sdk_ec2.types.modify_managed_resource_visibility_result
    import aws_sdk_ec2.types.modify_network_interface_attribute_request
    import aws_sdk_ec2.types.modify_private_dns_name_options_request
    import aws_sdk_ec2.types.modify_private_dns_name_options_result
    import aws_sdk_ec2.types.modify_public_ip_dns_name_options_request
    import aws_sdk_ec2.types.modify_public_ip_dns_name_options_result
    import aws_sdk_ec2.types.modify_reserved_instances_request
    import aws_sdk_ec2.types.modify_reserved_instances_result
    import aws_sdk_ec2.types.modify_route_server_request
    import aws_sdk_ec2.types.modify_route_server_result
    import aws_sdk_ec2.types.modify_security_group_rules_request
    import aws_sdk_ec2.types.modify_security_group_rules_result
    import aws_sdk_ec2.types.modify_snapshot_attribute_request
    import aws_sdk_ec2.types.modify_snapshot_tier_request
    import aws_sdk_ec2.types.modify_snapshot_tier_result
    import aws_sdk_ec2.types.modify_spot_fleet_request_request
    import aws_sdk_ec2.types.modify_spot_fleet_request_response
    import aws_sdk_ec2.types.modify_subnet_attribute_request
    import aws_sdk_ec2.types.modify_traffic_mirror_filter_network_services_request
    import aws_sdk_ec2.types.modify_traffic_mirror_filter_network_services_result
    import aws_sdk_ec2.types.modify_traffic_mirror_filter_rule_request
    import aws_sdk_ec2.types.modify_traffic_mirror_filter_rule_result
    import aws_sdk_ec2.types.modify_traffic_mirror_session_request
    import aws_sdk_ec2.types.modify_traffic_mirror_session_result
    import aws_sdk_ec2.types.modify_transit_gateway_metering_policy_request
    import aws_sdk_ec2.types.modify_transit_gateway_metering_policy_result
    import aws_sdk_ec2.types.modify_transit_gateway_options
    import aws_sdk_ec2.types.modify_transit_gateway_prefix_list_reference_request
    import aws_sdk_ec2.types.modify_transit_gateway_prefix_list_reference_result
    import aws_sdk_ec2.types.modify_transit_gateway_request
    import aws_sdk_ec2.types.modify_transit_gateway_result
    import aws_sdk_ec2.types.modify_transit_gateway_vpc_attachment_request
    import aws_sdk_ec2.types.modify_transit_gateway_vpc_attachment_request_options
    import aws_sdk_ec2.types.modify_transit_gateway_vpc_attachment_result
    import aws_sdk_ec2.types.modify_verified_access_endpoint_cidr_options
    import aws_sdk_ec2.types.modify_verified_access_endpoint_eni_options
    import aws_sdk_ec2.types.modify_verified_access_endpoint_load_balancer_options
    import aws_sdk_ec2.types.modify_verified_access_endpoint_policy_request
    import aws_sdk_ec2.types.modify_verified_access_endpoint_policy_result
    import aws_sdk_ec2.types.modify_verified_access_endpoint_rds_options
    import aws_sdk_ec2.types.modify_verified_access_endpoint_request
    import aws_sdk_ec2.types.modify_verified_access_endpoint_result
    import aws_sdk_ec2.types.modify_verified_access_group_policy_request
    import aws_sdk_ec2.types.modify_verified_access_group_policy_result
    import aws_sdk_ec2.types.modify_verified_access_group_request
    import aws_sdk_ec2.types.modify_verified_access_group_result
    import aws_sdk_ec2.types.modify_verified_access_instance_logging_configuration_request
    import aws_sdk_ec2.types.modify_verified_access_instance_logging_configuration_result
    import aws_sdk_ec2.types.modify_verified_access_instance_request
    import aws_sdk_ec2.types.modify_verified_access_instance_result
    import aws_sdk_ec2.types.modify_verified_access_native_application_oidc_options
    import aws_sdk_ec2.types.modify_verified_access_trust_provider_device_options
    import aws_sdk_ec2.types.modify_verified_access_trust_provider_oidc_options
    import aws_sdk_ec2.types.modify_verified_access_trust_provider_request
    import aws_sdk_ec2.types.modify_verified_access_trust_provider_result
    import aws_sdk_ec2.types.modify_volume_attribute_request
    import aws_sdk_ec2.types.modify_volume_request
    import aws_sdk_ec2.types.modify_volume_result
    import aws_sdk_ec2.types.modify_vpc_attribute_request
    import aws_sdk_ec2.types.modify_vpc_block_public_access_exclusion_request
    import aws_sdk_ec2.types.modify_vpc_block_public_access_exclusion_result
    import aws_sdk_ec2.types.modify_vpc_block_public_access_options_request
    import aws_sdk_ec2.types.modify_vpc_block_public_access_options_result
    import aws_sdk_ec2.types.modify_vpc_encryption_control_request
    import aws_sdk_ec2.types.modify_vpc_encryption_control_result
    import aws_sdk_ec2.types.modify_vpc_endpoint_connection_notification_request
    import aws_sdk_ec2.types.modify_vpc_endpoint_connection_notification_result
    import aws_sdk_ec2.types.modify_vpc_endpoint_request
    import aws_sdk_ec2.types.modify_vpc_endpoint_result
    import aws_sdk_ec2.types.modify_vpc_endpoint_service_configuration_request
    import aws_sdk_ec2.types.modify_vpc_endpoint_service_configuration_result
    import aws_sdk_ec2.types.modify_vpc_endpoint_service_payer_responsibility_request
    import aws_sdk_ec2.types.modify_vpc_endpoint_service_payer_responsibility_result
    import aws_sdk_ec2.types.modify_vpc_endpoint_service_permissions_request
    import aws_sdk_ec2.types.modify_vpc_endpoint_service_permissions_result
    import aws_sdk_ec2.types.modify_vpc_peering_connection_options_request
    import aws_sdk_ec2.types.modify_vpc_peering_connection_options_result
    import aws_sdk_ec2.types.modify_vpc_tenancy_request
    import aws_sdk_ec2.types.modify_vpc_tenancy_result
    import aws_sdk_ec2.types.modify_vpn_connection_options_request
    import aws_sdk_ec2.types.modify_vpn_connection_options_result
    import aws_sdk_ec2.types.modify_vpn_connection_request
    import aws_sdk_ec2.types.modify_vpn_connection_result
    import aws_sdk_ec2.types.modify_vpn_tunnel_certificate_request
    import aws_sdk_ec2.types.modify_vpn_tunnel_certificate_result
    import aws_sdk_ec2.types.modify_vpn_tunnel_options_request
    import aws_sdk_ec2.types.modify_vpn_tunnel_options_result
    import aws_sdk_ec2.types.modify_vpn_tunnel_options_specification
    import aws_sdk_ec2.types.monitor_instances_request
    import aws_sdk_ec2.types.monitor_instances_result
    import aws_sdk_ec2.types.move_address_to_vpc_request
    import aws_sdk_ec2.types.move_address_to_vpc_result
    import aws_sdk_ec2.types.move_byoip_cidr_to_ipam_request
    import aws_sdk_ec2.types.move_byoip_cidr_to_ipam_result
    import aws_sdk_ec2.types.move_capacity_reservation_instances_request
    import aws_sdk_ec2.types.move_capacity_reservation_instances_result
    import aws_sdk_ec2.types.moving_address_status
    import aws_sdk_ec2.types.nat_gateway
    import aws_sdk_ec2.types.nat_gateway_id
    import aws_sdk_ec2.types.nat_gateway_id_string_list
    import aws_sdk_ec2.types.nested_virtualization_specification
    import aws_sdk_ec2.types.netmask_length
    import aws_sdk_ec2.types.network_acl
    import aws_sdk_ec2.types.network_acl_association_id
    import aws_sdk_ec2.types.network_acl_id
    import aws_sdk_ec2.types.network_acl_id_string_list
    import aws_sdk_ec2.types.network_insights_access_scope
    import aws_sdk_ec2.types.network_insights_access_scope_analysis
    import aws_sdk_ec2.types.network_insights_access_scope_analysis_id
    import aws_sdk_ec2.types.network_insights_access_scope_analysis_id_list
    import aws_sdk_ec2.types.network_insights_access_scope_id
    import aws_sdk_ec2.types.network_insights_access_scope_id_list
    import aws_sdk_ec2.types.network_insights_analysis
    import aws_sdk_ec2.types.network_insights_analysis_id
    import aws_sdk_ec2.types.network_insights_analysis_id_list
    import aws_sdk_ec2.types.network_insights_max_results
    import aws_sdk_ec2.types.network_insights_path
    import aws_sdk_ec2.types.network_insights_path_id
    import aws_sdk_ec2.types.network_insights_path_id_list
    import aws_sdk_ec2.types.network_insights_resource_id
    import aws_sdk_ec2.types.network_interface
    import aws_sdk_ec2.types.network_interface_attachment_changes
    import aws_sdk_ec2.types.network_interface_attachment_id
    import aws_sdk_ec2.types.network_interface_attribute
    import aws_sdk_ec2.types.network_interface_creation_type
    import aws_sdk_ec2.types.network_interface_id
    import aws_sdk_ec2.types.network_interface_id_list
    import aws_sdk_ec2.types.network_interface_permission
    import aws_sdk_ec2.types.network_interface_permission_id
    import aws_sdk_ec2.types.network_interface_permission_id_list
    import aws_sdk_ec2.types.new_dhcp_configuration_list
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.odb_network_arn
    import aws_sdk_ec2.types.offering_class_type
    import aws_sdk_ec2.types.offering_id
    import aws_sdk_ec2.types.offering_type_values
    import aws_sdk_ec2.types.on_demand_options_request
    import aws_sdk_ec2.types.operation_type
    import aws_sdk_ec2.types.operator_request
    import aws_sdk_ec2.types.organization_arn_string_list
    import aws_sdk_ec2.types.organizational_unit_arn_string_list
    import aws_sdk_ec2.types.outpost_arn
    import aws_sdk_ec2.types.outpost_lag_id
    import aws_sdk_ec2.types.outpost_lag_id_set
    import aws_sdk_ec2.types.outpost_lag_max_results
    import aws_sdk_ec2.types.output_format
    import aws_sdk_ec2.types.owner_string_list
    import aws_sdk_ec2.types.path_request_filter
    import aws_sdk_ec2.types.payer_responsibility
    import aws_sdk_ec2.types.peering_connection_options_request
    import aws_sdk_ec2.types.period
    import aws_sdk_ec2.types.placement
    import aws_sdk_ec2.types.placement_group_arn
    import aws_sdk_ec2.types.placement_group_id
    import aws_sdk_ec2.types.placement_group_id_string_list
    import aws_sdk_ec2.types.placement_group_name
    import aws_sdk_ec2.types.placement_group_name_with_resolver
    import aws_sdk_ec2.types.placement_group_string_list
    import aws_sdk_ec2.types.placement_strategy
    import aws_sdk_ec2.types.platform_values
    import aws_sdk_ec2.types.pool_max_results
    import aws_sdk_ec2.types.port
    import aws_sdk_ec2.types.port_range
    import aws_sdk_ec2.types.prefix_list
    import aws_sdk_ec2.types.prefix_list_association
    import aws_sdk_ec2.types.prefix_list_entry
    import aws_sdk_ec2.types.prefix_list_max_results
    import aws_sdk_ec2.types.prefix_list_resource_id
    import aws_sdk_ec2.types.prefix_list_resource_id_string_list
    import aws_sdk_ec2.types.price_schedule_specification_list
    import aws_sdk_ec2.types.principal_id_format
    import aws_sdk_ec2.types.private_dns_name_options_request
    import aws_sdk_ec2.types.private_ip_address_count
    import aws_sdk_ec2.types.private_ip_address_specification_list
    import aws_sdk_ec2.types.private_ip_address_string_list
    import aws_sdk_ec2.types.product_code_string_list
    import aws_sdk_ec2.types.product_description_list
    import aws_sdk_ec2.types.protocol
    import aws_sdk_ec2.types.provision_byoip_cidr_request
    import aws_sdk_ec2.types.provision_byoip_cidr_result
    import aws_sdk_ec2.types.provision_ipam_byoasn_request
    import aws_sdk_ec2.types.provision_ipam_byoasn_result
    import aws_sdk_ec2.types.provision_ipam_pool_cidr_request
    import aws_sdk_ec2.types.provision_ipam_pool_cidr_result
    import aws_sdk_ec2.types.provision_public_ipv4_pool_cidr_request
    import aws_sdk_ec2.types.provision_public_ipv4_pool_cidr_result
    import aws_sdk_ec2.types.public_ip_address
    import aws_sdk_ec2.types.public_ip_dns_option
    import aws_sdk_ec2.types.public_ip_string_list
    import aws_sdk_ec2.types.public_ipv4_pool
    import aws_sdk_ec2.types.public_ipv4_pool_id_string_list
    import aws_sdk_ec2.types.purchase_capacity_block_extension_request
    import aws_sdk_ec2.types.purchase_capacity_block_extension_result
    import aws_sdk_ec2.types.purchase_capacity_block_request
    import aws_sdk_ec2.types.purchase_capacity_block_result
    import aws_sdk_ec2.types.purchase_host_reservation_request
    import aws_sdk_ec2.types.purchase_host_reservation_result
    import aws_sdk_ec2.types.purchase_request_set
    import aws_sdk_ec2.types.purchase_reserved_instances_offering_request
    import aws_sdk_ec2.types.purchase_reserved_instances_offering_result
    import aws_sdk_ec2.types.purchase_scheduled_instances_request
    import aws_sdk_ec2.types.purchase_scheduled_instances_result
    import aws_sdk_ec2.types.ramdisk_id
    import aws_sdk_ec2.types.reason_codes_list
    import aws_sdk_ec2.types.reboot_instances_request
    import aws_sdk_ec2.types.region_name_string_list
    import aws_sdk_ec2.types.region_names
    import aws_sdk_ec2.types.register_image_request
    import aws_sdk_ec2.types.register_image_result
    import aws_sdk_ec2.types.register_instance_event_notification_attributes_request
    import aws_sdk_ec2.types.register_instance_event_notification_attributes_result
    import aws_sdk_ec2.types.register_instance_tag_attribute_request
    import aws_sdk_ec2.types.register_transit_gateway_multicast_group_members_request
    import aws_sdk_ec2.types.register_transit_gateway_multicast_group_members_result
    import aws_sdk_ec2.types.register_transit_gateway_multicast_group_sources_request
    import aws_sdk_ec2.types.register_transit_gateway_multicast_group_sources_result
    import aws_sdk_ec2.types.reject_capacity_reservation_billing_ownership_request
    import aws_sdk_ec2.types.reject_capacity_reservation_billing_ownership_result
    import aws_sdk_ec2.types.reject_transit_gateway_client_vpn_attachment_request
    import aws_sdk_ec2.types.reject_transit_gateway_client_vpn_attachment_result
    import aws_sdk_ec2.types.reject_transit_gateway_multicast_domain_associations_request
    import aws_sdk_ec2.types.reject_transit_gateway_multicast_domain_associations_result
    import aws_sdk_ec2.types.reject_transit_gateway_peering_attachment_request
    import aws_sdk_ec2.types.reject_transit_gateway_peering_attachment_result
    import aws_sdk_ec2.types.reject_transit_gateway_vpc_attachment_request
    import aws_sdk_ec2.types.reject_transit_gateway_vpc_attachment_result
    import aws_sdk_ec2.types.reject_vpc_endpoint_connections_request
    import aws_sdk_ec2.types.reject_vpc_endpoint_connections_result
    import aws_sdk_ec2.types.reject_vpc_peering_connection_request
    import aws_sdk_ec2.types.reject_vpc_peering_connection_result
    import aws_sdk_ec2.types.release_address_request
    import aws_sdk_ec2.types.release_hosts_request
    import aws_sdk_ec2.types.release_hosts_result
    import aws_sdk_ec2.types.release_ipam_pool_allocation_request
    import aws_sdk_ec2.types.release_ipam_pool_allocation_result
    import aws_sdk_ec2.types.remove_ipam_operating_region_set
    import aws_sdk_ec2.types.remove_ipam_organizational_unit_exclusion_set
    import aws_sdk_ec2.types.remove_prefix_list_entries
    import aws_sdk_ec2.types.replace_iam_instance_profile_association_request
    import aws_sdk_ec2.types.replace_iam_instance_profile_association_result
    import aws_sdk_ec2.types.replace_image_criteria_in_allowed_images_settings_request
    import aws_sdk_ec2.types.replace_image_criteria_in_allowed_images_settings_result
    import aws_sdk_ec2.types.replace_network_acl_association_request
    import aws_sdk_ec2.types.replace_network_acl_association_result
    import aws_sdk_ec2.types.replace_network_acl_entry_request
    import aws_sdk_ec2.types.replace_root_volume_task
    import aws_sdk_ec2.types.replace_root_volume_task_ids
    import aws_sdk_ec2.types.replace_route_request
    import aws_sdk_ec2.types.replace_route_table_association_request
    import aws_sdk_ec2.types.replace_route_table_association_result
    import aws_sdk_ec2.types.replace_transit_gateway_route_request
    import aws_sdk_ec2.types.replace_transit_gateway_route_result
    import aws_sdk_ec2.types.replace_vpn_tunnel_request
    import aws_sdk_ec2.types.replace_vpn_tunnel_result
    import aws_sdk_ec2.types.report_instance_status_request
    import aws_sdk_ec2.types.report_instance_status_request_description
    import aws_sdk_ec2.types.report_status_type
    import aws_sdk_ec2.types.request_host_id_list
    import aws_sdk_ec2.types.request_host_id_set
    import aws_sdk_ec2.types.request_instance_type_list
    import aws_sdk_ec2.types.request_ipam_resource_tag
    import aws_sdk_ec2.types.request_ipam_resource_tag_list
    import aws_sdk_ec2.types.request_launch_template_data
    import aws_sdk_ec2.types.request_spot_fleet_request
    import aws_sdk_ec2.types.request_spot_fleet_response
    import aws_sdk_ec2.types.request_spot_instances_request
    import aws_sdk_ec2.types.request_spot_instances_result
    import aws_sdk_ec2.types.request_spot_launch_specification
    import aws_sdk_ec2.types.reservation
    import aws_sdk_ec2.types.reservation_fleet_instance_specification_list
    import aws_sdk_ec2.types.reservation_id
    import aws_sdk_ec2.types.reserved_capacity_options_request
    import aws_sdk_ec2.types.reserved_instance_id_set
    import aws_sdk_ec2.types.reserved_instance_limit_price
    import aws_sdk_ec2.types.reserved_instances_configuration_list
    import aws_sdk_ec2.types.reserved_instances_id_string_list
    import aws_sdk_ec2.types.reserved_instances_listing_id
    import aws_sdk_ec2.types.reserved_instances_modification
    import aws_sdk_ec2.types.reserved_instances_modification_id_string_list
    import aws_sdk_ec2.types.reserved_instances_offering
    import aws_sdk_ec2.types.reserved_instances_offering_id
    import aws_sdk_ec2.types.reserved_instances_offering_id_string_list
    import aws_sdk_ec2.types.reset_address_attribute_request
    import aws_sdk_ec2.types.reset_address_attribute_result
    import aws_sdk_ec2.types.reset_ebs_default_kms_key_id_request
    import aws_sdk_ec2.types.reset_ebs_default_kms_key_id_result
    import aws_sdk_ec2.types.reset_fpga_image_attribute_name
    import aws_sdk_ec2.types.reset_fpga_image_attribute_request
    import aws_sdk_ec2.types.reset_fpga_image_attribute_result
    import aws_sdk_ec2.types.reset_image_attribute_name
    import aws_sdk_ec2.types.reset_image_attribute_request
    import aws_sdk_ec2.types.reset_instance_attribute_request
    import aws_sdk_ec2.types.reset_network_interface_attribute_request
    import aws_sdk_ec2.types.reset_snapshot_attribute_request
    import aws_sdk_ec2.types.resource_configuration_arn
    import aws_sdk_ec2.types.resource_id_list
    import aws_sdk_ec2.types.resource_list
    import aws_sdk_ec2.types.resource_type_request_list
    import aws_sdk_ec2.types.restorable_by_string_list
    import aws_sdk_ec2.types.restore_address_to_classic_request
    import aws_sdk_ec2.types.restore_address_to_classic_result
    import aws_sdk_ec2.types.restore_image_from_recycle_bin_request
    import aws_sdk_ec2.types.restore_image_from_recycle_bin_result
    import aws_sdk_ec2.types.restore_managed_prefix_list_version_request
    import aws_sdk_ec2.types.restore_managed_prefix_list_version_result
    import aws_sdk_ec2.types.restore_snapshot_from_recycle_bin_request
    import aws_sdk_ec2.types.restore_snapshot_from_recycle_bin_result
    import aws_sdk_ec2.types.restore_snapshot_tier_request
    import aws_sdk_ec2.types.restore_snapshot_tier_request_temporary_restore_days
    import aws_sdk_ec2.types.restore_snapshot_tier_result
    import aws_sdk_ec2.types.restore_volume_from_recycle_bin_request
    import aws_sdk_ec2.types.restore_volume_from_recycle_bin_result
    import aws_sdk_ec2.types.result_range
    import aws_sdk_ec2.types.retention_period_request_days
    import aws_sdk_ec2.types.revoke_client_vpn_ingress_request
    import aws_sdk_ec2.types.revoke_client_vpn_ingress_result
    import aws_sdk_ec2.types.revoke_security_group_egress_request
    import aws_sdk_ec2.types.revoke_security_group_egress_result
    import aws_sdk_ec2.types.revoke_security_group_ingress_request
    import aws_sdk_ec2.types.revoke_security_group_ingress_result
    import aws_sdk_ec2.types.ri_product_description
    import aws_sdk_ec2.types.role_id
    import aws_sdk_ec2.types.route_gateway_id
    import aws_sdk_ec2.types.route_server
    import aws_sdk_ec2.types.route_server_bgp_options_request
    import aws_sdk_ec2.types.route_server_endpoint
    import aws_sdk_ec2.types.route_server_endpoint_id
    import aws_sdk_ec2.types.route_server_endpoint_ids_list
    import aws_sdk_ec2.types.route_server_id
    import aws_sdk_ec2.types.route_server_ids_list
    import aws_sdk_ec2.types.route_server_max_results
    import aws_sdk_ec2.types.route_server_peer
    import aws_sdk_ec2.types.route_server_peer_id
    import aws_sdk_ec2.types.route_server_peer_ids_list
    import aws_sdk_ec2.types.route_server_persist_routes_action
    import aws_sdk_ec2.types.route_table
    import aws_sdk_ec2.types.route_table_association_id
    import aws_sdk_ec2.types.route_table_id
    import aws_sdk_ec2.types.route_table_id_string_list
    import aws_sdk_ec2.types.rule_action
    import aws_sdk_ec2.types.run_instances_monitoring_enabled
    import aws_sdk_ec2.types.run_instances_request
    import aws_sdk_ec2.types.run_instances_user_data
    import aws_sdk_ec2.types.run_scheduled_instances_request
    import aws_sdk_ec2.types.run_scheduled_instances_result
    import aws_sdk_ec2.types.s3_object_tag_list
    import aws_sdk_ec2.types.schedule
    import aws_sdk_ec2.types.scheduled_instance
    import aws_sdk_ec2.types.scheduled_instance_availability
    import aws_sdk_ec2.types.scheduled_instance_id
    import aws_sdk_ec2.types.scheduled_instance_id_request_set
    import aws_sdk_ec2.types.scheduled_instance_recurrence_request
    import aws_sdk_ec2.types.scheduled_instances_launch_specification
    import aws_sdk_ec2.types.search_local_gateway_routes_request
    import aws_sdk_ec2.types.search_local_gateway_routes_result
    import aws_sdk_ec2.types.search_transit_gateway_multicast_groups_request
    import aws_sdk_ec2.types.search_transit_gateway_multicast_groups_result
    import aws_sdk_ec2.types.search_transit_gateway_routes_request
    import aws_sdk_ec2.types.search_transit_gateway_routes_result
    import aws_sdk_ec2.types.secondary_interface
    import aws_sdk_ec2.types.secondary_interface_id_list
    import aws_sdk_ec2.types.secondary_network
    import aws_sdk_ec2.types.secondary_network_id
    import aws_sdk_ec2.types.secondary_network_id_list
    import aws_sdk_ec2.types.secondary_network_type
    import aws_sdk_ec2.types.secondary_subnet
    import aws_sdk_ec2.types.secondary_subnet_id
    import aws_sdk_ec2.types.secondary_subnet_id_list
    import aws_sdk_ec2.types.secret_arn
    import aws_sdk_ec2.types.security_group
    import aws_sdk_ec2.types.security_group_for_vpc
    import aws_sdk_ec2.types.security_group_id
    import aws_sdk_ec2.types.security_group_id_list
    import aws_sdk_ec2.types.security_group_id_string_list
    import aws_sdk_ec2.types.security_group_id_string_list_request
    import aws_sdk_ec2.types.security_group_name
    import aws_sdk_ec2.types.security_group_rule
    import aws_sdk_ec2.types.security_group_rule_description_list
    import aws_sdk_ec2.types.security_group_rule_id_list
    import aws_sdk_ec2.types.security_group_rule_update_list
    import aws_sdk_ec2.types.security_group_string_list
    import aws_sdk_ec2.types.security_group_vpc_association
    import aws_sdk_ec2.types.self_service_portal
    import aws_sdk_ec2.types.send_diagnostic_interrupt_request
    import aws_sdk_ec2.types.sensitive_mac_credentials
    import aws_sdk_ec2.types.service_configuration
    import aws_sdk_ec2.types.service_link_max_results
    import aws_sdk_ec2.types.service_link_virtual_interface_id_set
    import aws_sdk_ec2.types.service_network_arn
    import aws_sdk_ec2.types.shutdown_behavior
    import aws_sdk_ec2.types.slot_date_time_range_request
    import aws_sdk_ec2.types.slot_start_time_range_request
    import aws_sdk_ec2.types.snapshot
    import aws_sdk_ec2.types.snapshot_attribute_name
    import aws_sdk_ec2.types.snapshot_block_public_access_state
    import aws_sdk_ec2.types.snapshot_completion_duration_minutes_request
    import aws_sdk_ec2.types.snapshot_disk_container
    import aws_sdk_ec2.types.snapshot_id
    import aws_sdk_ec2.types.snapshot_id_string_list
    import aws_sdk_ec2.types.snapshot_location_enum
    import aws_sdk_ec2.types.snapshot_recycle_bin_info
    import aws_sdk_ec2.types.snapshot_tier_status
    import aws_sdk_ec2.types.spot_fleet_request_config
    import aws_sdk_ec2.types.spot_fleet_request_config_data
    import aws_sdk_ec2.types.spot_fleet_request_id
    import aws_sdk_ec2.types.spot_fleet_request_id_list
    import aws_sdk_ec2.types.spot_instance_request
    import aws_sdk_ec2.types.spot_instance_request_id_list
    import aws_sdk_ec2.types.spot_instance_type
    import aws_sdk_ec2.types.spot_options_request
    import aws_sdk_ec2.types.spot_placement_score
    import aws_sdk_ec2.types.spot_placement_scores_max_results
    import aws_sdk_ec2.types.spot_placement_scores_target_capacity
    import aws_sdk_ec2.types.spot_price
    import aws_sdk_ec2.types.spread_level
    import aws_sdk_ec2.types.stale_security_group
    import aws_sdk_ec2.types.start_declarative_policies_report_request
    import aws_sdk_ec2.types.start_declarative_policies_report_result
    import aws_sdk_ec2.types.start_instances_request
    import aws_sdk_ec2.types.start_instances_result
    import aws_sdk_ec2.types.start_network_insights_access_scope_analysis_request
    import aws_sdk_ec2.types.start_network_insights_access_scope_analysis_result
    import aws_sdk_ec2.types.start_network_insights_analysis_request
    import aws_sdk_ec2.types.start_network_insights_analysis_result
    import aws_sdk_ec2.types.start_vpc_endpoint_service_private_dns_verification_request
    import aws_sdk_ec2.types.start_vpc_endpoint_service_private_dns_verification_result
    import aws_sdk_ec2.types.statistic_type
    import aws_sdk_ec2.types.stop_instances_request
    import aws_sdk_ec2.types.stop_instances_result
    import aws_sdk_ec2.types.storage
    import aws_sdk_ec2.types.storage_location
    import aws_sdk_ec2.types.store_image_task_result
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet
    import aws_sdk_ec2.types.subnet_cidr_association_id
    import aws_sdk_ec2.types.subnet_cidr_reservation_id
    import aws_sdk_ec2.types.subnet_cidr_reservation_type
    import aws_sdk_ec2.types.subnet_configurations_list
    import aws_sdk_ec2.types.subnet_id
    import aws_sdk_ec2.types.subnet_id_list
    import aws_sdk_ec2.types.subnet_id_string_list
    import aws_sdk_ec2.types.subscription
    import aws_sdk_ec2.types.tag_description
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.target_capacity_specification_request
    import aws_sdk_ec2.types.target_capacity_unit_type
    import aws_sdk_ec2.types.target_configuration_request_set
    import aws_sdk_ec2.types.target_network
    import aws_sdk_ec2.types.target_storage_tier
    import aws_sdk_ec2.types.tenancy
    import aws_sdk_ec2.types.terminate_client_vpn_connections_request
    import aws_sdk_ec2.types.terminate_client_vpn_connections_result
    import aws_sdk_ec2.types.terminate_instances_request
    import aws_sdk_ec2.types.terminate_instances_result
    import aws_sdk_ec2.types.tpm_support_values
    import aws_sdk_ec2.types.traffic_direction
    import aws_sdk_ec2.types.traffic_ip_address_type
    import aws_sdk_ec2.types.traffic_mirror_filter
    import aws_sdk_ec2.types.traffic_mirror_filter_id
    import aws_sdk_ec2.types.traffic_mirror_filter_id_list
    import aws_sdk_ec2.types.traffic_mirror_filter_rule_field_list
    import aws_sdk_ec2.types.traffic_mirror_filter_rule_id_list
    import aws_sdk_ec2.types.traffic_mirror_filter_rule_id_with_resolver
    import aws_sdk_ec2.types.traffic_mirror_network_service_list
    import aws_sdk_ec2.types.traffic_mirror_port_range_request
    import aws_sdk_ec2.types.traffic_mirror_rule_action
    import aws_sdk_ec2.types.traffic_mirror_session
    import aws_sdk_ec2.types.traffic_mirror_session_field_list
    import aws_sdk_ec2.types.traffic_mirror_session_id
    import aws_sdk_ec2.types.traffic_mirror_session_id_list
    import aws_sdk_ec2.types.traffic_mirror_target
    import aws_sdk_ec2.types.traffic_mirror_target_id
    import aws_sdk_ec2.types.traffic_mirror_target_id_list
    import aws_sdk_ec2.types.traffic_mirroring_max_results
    import aws_sdk_ec2.types.traffic_type
    import aws_sdk_ec2.types.transit_association_gateway_id
    import aws_sdk_ec2.types.transit_gateway
    import aws_sdk_ec2.types.transit_gateway_attachment
    import aws_sdk_ec2.types.transit_gateway_attachment_id
    import aws_sdk_ec2.types.transit_gateway_attachment_id_string_list
    import aws_sdk_ec2.types.transit_gateway_attachment_propagation
    import aws_sdk_ec2.types.transit_gateway_attachment_resource_type
    import aws_sdk_ec2.types.transit_gateway_configuration_input_structure
    import aws_sdk_ec2.types.transit_gateway_connect
    import aws_sdk_ec2.types.transit_gateway_connect_peer
    import aws_sdk_ec2.types.transit_gateway_connect_peer_id
    import aws_sdk_ec2.types.transit_gateway_connect_peer_id_string_list
    import aws_sdk_ec2.types.transit_gateway_connect_request_bgp_options
    import aws_sdk_ec2.types.transit_gateway_id
    import aws_sdk_ec2.types.transit_gateway_id_string_list
    import aws_sdk_ec2.types.transit_gateway_max_results
    import aws_sdk_ec2.types.transit_gateway_metering_payer_type
    import aws_sdk_ec2.types.transit_gateway_metering_policy_id
    import aws_sdk_ec2.types.transit_gateway_metering_policy_id_string_list
    import aws_sdk_ec2.types.transit_gateway_multicast_domain
    import aws_sdk_ec2.types.transit_gateway_multicast_domain_association
    import aws_sdk_ec2.types.transit_gateway_multicast_domain_id
    import aws_sdk_ec2.types.transit_gateway_multicast_domain_id_string_list
    import aws_sdk_ec2.types.transit_gateway_multicast_group
    import aws_sdk_ec2.types.transit_gateway_network_interface_id_list
    import aws_sdk_ec2.types.transit_gateway_peering_attachment
    import aws_sdk_ec2.types.transit_gateway_policy_table
    import aws_sdk_ec2.types.transit_gateway_policy_table_association
    import aws_sdk_ec2.types.transit_gateway_policy_table_id
    import aws_sdk_ec2.types.transit_gateway_policy_table_id_string_list
    import aws_sdk_ec2.types.transit_gateway_prefix_list_reference
    import aws_sdk_ec2.types.transit_gateway_request_options
    import aws_sdk_ec2.types.transit_gateway_route
    import aws_sdk_ec2.types.transit_gateway_route_table
    import aws_sdk_ec2.types.transit_gateway_route_table_announcement
    import aws_sdk_ec2.types.transit_gateway_route_table_announcement_id
    import aws_sdk_ec2.types.transit_gateway_route_table_announcement_id_string_list
    import aws_sdk_ec2.types.transit_gateway_route_table_association
    import aws_sdk_ec2.types.transit_gateway_route_table_id
    import aws_sdk_ec2.types.transit_gateway_route_table_id_string_list
    import aws_sdk_ec2.types.transit_gateway_route_table_propagation
    import aws_sdk_ec2.types.transit_gateway_subnet_id_list
    import aws_sdk_ec2.types.transit_gateway_vpc_attachment
    import aws_sdk_ec2.types.transport_protocol
    import aws_sdk_ec2.types.trunk_interface_association
    import aws_sdk_ec2.types.trunk_interface_association_id
    import aws_sdk_ec2.types.trunk_interface_association_id_list
    import aws_sdk_ec2.types.trust_provider_type
    import aws_sdk_ec2.types.unassign_ipv6_addresses_request
    import aws_sdk_ec2.types.unassign_ipv6_addresses_result
    import aws_sdk_ec2.types.unassign_private_ip_addresses_request
    import aws_sdk_ec2.types.unassign_private_nat_gateway_address_request
    import aws_sdk_ec2.types.unassign_private_nat_gateway_address_result
    import aws_sdk_ec2.types.unlimited_supported_instance_family
    import aws_sdk_ec2.types.unlock_snapshot_request
    import aws_sdk_ec2.types.unlock_snapshot_result
    import aws_sdk_ec2.types.unmonitor_instances_request
    import aws_sdk_ec2.types.unmonitor_instances_result
    import aws_sdk_ec2.types.update_capacity_manager_monitored_tag_keys_request
    import aws_sdk_ec2.types.update_capacity_manager_monitored_tag_keys_result
    import aws_sdk_ec2.types.update_capacity_manager_organizations_access_request
    import aws_sdk_ec2.types.update_capacity_manager_organizations_access_result
    import aws_sdk_ec2.types.update_interruptible_capacity_reservation_allocation_request
    import aws_sdk_ec2.types.update_interruptible_capacity_reservation_allocation_result
    import aws_sdk_ec2.types.update_security_group_rule_descriptions_egress_request
    import aws_sdk_ec2.types.update_security_group_rule_descriptions_egress_result
    import aws_sdk_ec2.types.update_security_group_rule_descriptions_ingress_request
    import aws_sdk_ec2.types.update_security_group_rule_descriptions_ingress_result
    import aws_sdk_ec2.types.user_group_string_list
    import aws_sdk_ec2.types.user_id_string_list
    import aws_sdk_ec2.types.user_trust_provider_type
    import aws_sdk_ec2.types.value_string_list
    import aws_sdk_ec2.types.verification_method
    import aws_sdk_ec2.types.verified_access_endpoint
    import aws_sdk_ec2.types.verified_access_endpoint_attachment_type
    import aws_sdk_ec2.types.verified_access_endpoint_id
    import aws_sdk_ec2.types.verified_access_endpoint_id_list
    import aws_sdk_ec2.types.verified_access_endpoint_type
    import aws_sdk_ec2.types.verified_access_group
    import aws_sdk_ec2.types.verified_access_group_id
    import aws_sdk_ec2.types.verified_access_group_id_list
    import aws_sdk_ec2.types.verified_access_instance
    import aws_sdk_ec2.types.verified_access_instance_id
    import aws_sdk_ec2.types.verified_access_instance_id_list
    import aws_sdk_ec2.types.verified_access_instance_logging_configuration
    import aws_sdk_ec2.types.verified_access_log_options
    import aws_sdk_ec2.types.verified_access_sse_specification_request
    import aws_sdk_ec2.types.verified_access_trust_provider
    import aws_sdk_ec2.types.verified_access_trust_provider_id
    import aws_sdk_ec2.types.verified_access_trust_provider_id_list
    import aws_sdk_ec2.types.version_description
    import aws_sdk_ec2.types.version_string_list
    import aws_sdk_ec2.types.virtualization_type_set
    import aws_sdk_ec2.types.volume
    import aws_sdk_ec2.types.volume_attachment
    import aws_sdk_ec2.types.volume_attribute_name
    import aws_sdk_ec2.types.volume_detail
    import aws_sdk_ec2.types.volume_id
    import aws_sdk_ec2.types.volume_id_string_list
    import aws_sdk_ec2.types.volume_id_with_resolver
    import aws_sdk_ec2.types.volume_modification
    import aws_sdk_ec2.types.volume_status_item
    import aws_sdk_ec2.types.volume_type
    import aws_sdk_ec2.types.vpc
    import aws_sdk_ec2.types.vpc_attribute_name
    import aws_sdk_ec2.types.vpc_block_public_access_exclusion_id
    import aws_sdk_ec2.types.vpc_block_public_access_exclusion_id_list
    import aws_sdk_ec2.types.vpc_cidr_association_id
    import aws_sdk_ec2.types.vpc_classic_link_id_list
    import aws_sdk_ec2.types.vpc_encryption_control_configuration
    import aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input
    import aws_sdk_ec2.types.vpc_encryption_control_id
    import aws_sdk_ec2.types.vpc_encryption_control_id_list
    import aws_sdk_ec2.types.vpc_encryption_control_mode
    import aws_sdk_ec2.types.vpc_endpoint
    import aws_sdk_ec2.types.vpc_endpoint_connection
    import aws_sdk_ec2.types.vpc_endpoint_id
    import aws_sdk_ec2.types.vpc_endpoint_id_list
    import aws_sdk_ec2.types.vpc_endpoint_route_table_id_list
    import aws_sdk_ec2.types.vpc_endpoint_security_group_id_list
    import aws_sdk_ec2.types.vpc_endpoint_service_id
    import aws_sdk_ec2.types.vpc_endpoint_service_id_list
    import aws_sdk_ec2.types.vpc_endpoint_subnet_id_list
    import aws_sdk_ec2.types.vpc_endpoint_type
    import aws_sdk_ec2.types.vpc_flow_log_id
    import aws_sdk_ec2.types.vpc_id
    import aws_sdk_ec2.types.vpc_id_string_list
    import aws_sdk_ec2.types.vpc_peering_connection
    import aws_sdk_ec2.types.vpc_peering_connection_id
    import aws_sdk_ec2.types.vpc_peering_connection_id_list
    import aws_sdk_ec2.types.vpc_peering_connection_id_with_resolver
    import aws_sdk_ec2.types.vpc_tenancy
    import aws_sdk_ec2.types.vpn_concentrator
    import aws_sdk_ec2.types.vpn_concentrator_id
    import aws_sdk_ec2.types.vpn_concentrator_id_string_list
    import aws_sdk_ec2.types.vpn_concentrator_type
    import aws_sdk_ec2.types.vpn_connection_device_type
    import aws_sdk_ec2.types.vpn_connection_device_type_id
    import aws_sdk_ec2.types.vpn_connection_id
    import aws_sdk_ec2.types.vpn_connection_id_string_list
    import aws_sdk_ec2.types.vpn_connection_options_specification
    import aws_sdk_ec2.types.vpn_gateway_id
    import aws_sdk_ec2.types.vpn_gateway_id_string_list
    import aws_sdk_ec2.types.vpn_tunnel_bandwidth
    import aws_sdk_ec2.types.withdraw_byoip_cidr_request
    import aws_sdk_ec2.types.withdraw_byoip_cidr_result
    import aws_sdk_ec2.types.zone_id_string_list
    import aws_sdk_ec2.types.zone_name_string_list


class AsyncEC2ClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


class AsyncEC2Client:
    """A client for the ``EC2`` service.

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
        self._config = AsyncEC2ClientConfig(
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
        self, config_overrides: Optional[AsyncEC2ClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncEC2ClientConfig = config_overrides or {}
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

    async def accept_address_transfer(
        self,
        address: "aws_sdk_ec2.types.string.String",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.accept_address_transfer_result.AcceptAddressTransferResult":
        r"""<p>Accepts an Elastic IP address transfer. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/vpc-eips.html#using-instance-addressing-eips-transfer-accept\">Accept a transferred Elastic IP address</a> in the <i>Amazon VPC User Guide</i>.</p>

        Args:
            address: <p>The Elastic IP address you are accepting for transfer.</p>
            tag_specifications: <p> <code>tag</code>:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.accept_address_transfer_request.AcceptAddressTransferRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.accept_address_transfer_result.AcceptAddressTransferResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.accept_address_transfer

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.accept_address_transfer.async_accept_address_transfer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.accept_address_transfer_request.AcceptAddressTransferRequest = {}  # type: ignore[typeddict-item]
        input_["address"] = address
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def accept_capacity_reservation_billing_ownership(
        self,
        capacity_reservation_id: "aws_sdk_ec2.types.capacity_reservation_id.CapacityReservationId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.accept_capacity_reservation_billing_ownership_result.AcceptCapacityReservationBillingOwnershipResult":
        r"""<p>Accepts a request to assign billing of the available capacity of a shared Capacity Reservation to your account. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/assign-billing.html\"> Billing assignment for shared Amazon EC2 Capacity Reservations</a>.</p>

        Args:
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            capacity_reservation_id: <p>The ID of the Capacity Reservation for which to accept the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.accept_capacity_reservation_billing_ownership_request.AcceptCapacityReservationBillingOwnershipRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.accept_capacity_reservation_billing_ownership_result.AcceptCapacityReservationBillingOwnershipResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.accept_capacity_reservation_billing_ownership

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.accept_capacity_reservation_billing_ownership.async_accept_capacity_reservation_billing_ownership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.accept_capacity_reservation_billing_ownership_request.AcceptCapacityReservationBillingOwnershipRequest = {}  # type: ignore[typeddict-item]
        if dry_run is not None:
            input_["dry_run"] = dry_run
        input_["capacity_reservation_id"] = capacity_reservation_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def accept_reserved_instances_exchange_quote(
        self,
        reserved_instance_ids: "aws_sdk_ec2.types.reserved_instance_id_set.ReservedInstanceIdSet",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        target_configurations: Optional[
            "aws_sdk_ec2.types.target_configuration_request_set.TargetConfigurationRequestSet"
        ] = None,
    ) -> "aws_sdk_ec2.types.accept_reserved_instances_exchange_quote_result.AcceptReservedInstancesExchangeQuoteResult":
        """<p>Accepts the Convertible Reserved Instance exchange quote described in the <a>GetReservedInstancesExchangeQuote</a> call.</p>

        Args:
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            reserved_instance_ids: <p>The IDs of the Convertible Reserved Instances to exchange for another Convertible Reserved Instance of the same or higher value.</p>
            target_configurations: <p>The configuration of the target Convertible Reserved Instance to exchange for your current Convertible Reserved Instances.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.accept_reserved_instances_exchange_quote_request.AcceptReservedInstancesExchangeQuoteRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.accept_reserved_instances_exchange_quote_result.AcceptReservedInstancesExchangeQuoteResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.accept_reserved_instances_exchange_quote

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.accept_reserved_instances_exchange_quote.async_accept_reserved_instances_exchange_quote(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.accept_reserved_instances_exchange_quote_request.AcceptReservedInstancesExchangeQuoteRequest = {}  # type: ignore[typeddict-item]
        if dry_run is not None:
            input_["dry_run"] = dry_run
        input_["reserved_instance_ids"] = reserved_instance_ids
        if target_configurations is not None:
            input_["target_configurations"] = target_configurations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def accept_transit_gateway_client_vpn_attachment(
        self,
        transit_gateway_attachment_id: "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.accept_transit_gateway_client_vpn_attachment_result.AcceptTransitGatewayClientVpnAttachmentResult":
        """<p>Accepts a Transit Gateway attachment request for a Client VPN endpoint. The Transit Gateway owner must accept the attachment request before the Client VPN endpoint can route traffic through the Transit Gateway.</p>

        Args:
            transit_gateway_attachment_id: <p>The ID of the Transit Gateway attachment.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.accept_transit_gateway_client_vpn_attachment_request.AcceptTransitGatewayClientVpnAttachmentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.accept_transit_gateway_client_vpn_attachment_result.AcceptTransitGatewayClientVpnAttachmentResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.accept_transit_gateway_client_vpn_attachment

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.accept_transit_gateway_client_vpn_attachment.async_accept_transit_gateway_client_vpn_attachment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.accept_transit_gateway_client_vpn_attachment_request.AcceptTransitGatewayClientVpnAttachmentRequest = {}  # type: ignore[typeddict-item]
        input_["transit_gateway_attachment_id"] = transit_gateway_attachment_id
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def accept_transit_gateway_multicast_domain_associations(
        self,
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        transit_gateway_multicast_domain_id: Optional[
            "aws_sdk_ec2.types.transit_gateway_multicast_domain_id.TransitGatewayMulticastDomainId"
        ] = None,
        transit_gateway_attachment_id: Optional[
            "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
        ] = None,
        subnet_ids: Optional[
            "aws_sdk_ec2.types.value_string_list.ValueStringList"
        ] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.accept_transit_gateway_multicast_domain_associations_result.AcceptTransitGatewayMulticastDomainAssociationsResult":
        """<p>Accepts a request to associate subnets with a transit gateway multicast domain.</p>

        Args:
            transit_gateway_multicast_domain_id: <p>The ID of the transit gateway multicast domain.</p>
            transit_gateway_attachment_id: <p>The ID of the transit gateway attachment.</p>
            subnet_ids: <p>The IDs of the subnets to associate with the transit gateway multicast domain.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.accept_transit_gateway_multicast_domain_associations_request.AcceptTransitGatewayMulticastDomainAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.accept_transit_gateway_multicast_domain_associations_result.AcceptTransitGatewayMulticastDomainAssociationsResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.accept_transit_gateway_multicast_domain_associations

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.accept_transit_gateway_multicast_domain_associations.async_accept_transit_gateway_multicast_domain_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.accept_transit_gateway_multicast_domain_associations_request.AcceptTransitGatewayMulticastDomainAssociationsRequest = {}  # type: ignore[typeddict-item]
        if transit_gateway_multicast_domain_id is not None:
            input_["transit_gateway_multicast_domain_id"] = (
                transit_gateway_multicast_domain_id
            )
        if transit_gateway_attachment_id is not None:
            input_["transit_gateway_attachment_id"] = transit_gateway_attachment_id
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def accept_transit_gateway_peering_attachment(
        self,
        transit_gateway_attachment_id: "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.accept_transit_gateway_peering_attachment_result.AcceptTransitGatewayPeeringAttachmentResult":
        """<p>Accepts a transit gateway peering attachment request. The peering attachment must be in the <code>pendingAcceptance</code> state.</p>

        Args:
            transit_gateway_attachment_id: <p>The ID of the transit gateway attachment.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.accept_transit_gateway_peering_attachment_request.AcceptTransitGatewayPeeringAttachmentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.accept_transit_gateway_peering_attachment_result.AcceptTransitGatewayPeeringAttachmentResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.accept_transit_gateway_peering_attachment

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.accept_transit_gateway_peering_attachment.async_accept_transit_gateway_peering_attachment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.accept_transit_gateway_peering_attachment_request.AcceptTransitGatewayPeeringAttachmentRequest = {}  # type: ignore[typeddict-item]
        input_["transit_gateway_attachment_id"] = transit_gateway_attachment_id
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def accept_transit_gateway_vpc_attachment(
        self,
        transit_gateway_attachment_id: "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.accept_transit_gateway_vpc_attachment_result.AcceptTransitGatewayVpcAttachmentResult":
        """<p>Accepts a request to attach a VPC to a transit gateway.</p> <p>The VPC attachment must be in the <code>pendingAcceptance</code> state. Use <a>DescribeTransitGatewayVpcAttachments</a> to view your pending VPC attachment requests. Use <a>RejectTransitGatewayVpcAttachment</a> to reject a VPC attachment request.</p>

        Args:
            transit_gateway_attachment_id: <p>The ID of the attachment.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.accept_transit_gateway_vpc_attachment_request.AcceptTransitGatewayVpcAttachmentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.accept_transit_gateway_vpc_attachment_result.AcceptTransitGatewayVpcAttachmentResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.accept_transit_gateway_vpc_attachment

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.accept_transit_gateway_vpc_attachment.async_accept_transit_gateway_vpc_attachment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.accept_transit_gateway_vpc_attachment_request.AcceptTransitGatewayVpcAttachmentRequest = {}  # type: ignore[typeddict-item]
        input_["transit_gateway_attachment_id"] = transit_gateway_attachment_id
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def accept_vpc_endpoint_connections(
        self,
        service_id: "aws_sdk_ec2.types.vpc_endpoint_service_id.VpcEndpointServiceId",
        vpc_endpoint_ids: "aws_sdk_ec2.types.vpc_endpoint_id_list.VpcEndpointIdList",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.accept_vpc_endpoint_connections_result.AcceptVpcEndpointConnectionsResult":
        """<p>Accepts connection requests to your VPC endpoint service.</p>

        Args:
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            service_id: <p>The ID of the VPC endpoint service.</p>
            vpc_endpoint_ids: <p>The IDs of the interface VPC endpoints.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.accept_vpc_endpoint_connections_request.AcceptVpcEndpointConnectionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.accept_vpc_endpoint_connections_result.AcceptVpcEndpointConnectionsResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.accept_vpc_endpoint_connections

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.accept_vpc_endpoint_connections.async_accept_vpc_endpoint_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.accept_vpc_endpoint_connections_request.AcceptVpcEndpointConnectionsRequest = {}  # type: ignore[typeddict-item]
        if dry_run is not None:
            input_["dry_run"] = dry_run
        input_["service_id"] = service_id
        input_["vpc_endpoint_ids"] = vpc_endpoint_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def accept_vpc_peering_connection(
        self,
        vpc_peering_connection_id: "aws_sdk_ec2.types.vpc_peering_connection_id_with_resolver.VpcPeeringConnectionIdWithResolver",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.accept_vpc_peering_connection_result.AcceptVpcPeeringConnectionResult":
        """<p>Accept a VPC peering connection request. To accept a request, the VPC peering connection must be in the <code>pending-acceptance</code> state, and you must be the owner of the peer VPC. Use <a>DescribeVpcPeeringConnections</a> to view your outstanding VPC peering connection requests.</p> <p>For an inter-Region VPC peering connection request, you must accept the VPC peering connection in the Region of the accepter VPC.</p>

        Args:
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            vpc_peering_connection_id: <p>The ID of the VPC peering connection. You must specify this parameter in the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.accept_vpc_peering_connection_request.AcceptVpcPeeringConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.accept_vpc_peering_connection_result.AcceptVpcPeeringConnectionResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.accept_vpc_peering_connection

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.accept_vpc_peering_connection.async_accept_vpc_peering_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.accept_vpc_peering_connection_request.AcceptVpcPeeringConnectionRequest = {}  # type: ignore[typeddict-item]
        if dry_run is not None:
            input_["dry_run"] = dry_run
        input_["vpc_peering_connection_id"] = vpc_peering_connection_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def advertise_byoip_cidr(
        self,
        cidr: "aws_sdk_ec2.types.string.String",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        asn: Optional["aws_sdk_ec2.types.string.String"] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        network_border_group: Optional["aws_sdk_ec2.types.string.String"] = None,
    ) -> "aws_sdk_ec2.types.advertise_byoip_cidr_result.AdvertiseByoipCidrResult":
        r"""<p>Advertises an IPv4 or IPv6 address range that is provisioned for use with your Amazon Web Services resources through bring your own IP addresses (BYOIP).</p> <p>You can perform this operation at most once every 10 seconds, even if you specify different address ranges each time.</p> <p>We recommend that you stop advertising the BYOIP CIDR from other locations when you advertise it from Amazon Web Services. To minimize down time, you can configure your Amazon Web Services resources to use an address from a BYOIP CIDR before it is advertised, and then simultaneously stop advertising it from the current location and start advertising it through Amazon Web Services.</p> <p>It can take a few minutes before traffic to the specified addresses starts routing to Amazon Web Services because of BGP propagation delays.</p>

        Args:
            cidr: <p>The address range, in CIDR notation. This must be the exact range that you provisioned. You can't advertise only a portion of the provisioned range.</p>
            asn: <p>The public 2-byte or 4-byte ASN that you want to advertise.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            network_border_group: <p>If you have <a href=\"https://docs.aws.amazon.com/local-zones/latest/ug/how-local-zones-work.html\">Local Zones</a> enabled, you can choose a network border group for Local Zones when you provision and advertise a BYOIPv4 CIDR. Choose the network border group carefully as the EIP and the Amazon Web Services resource it is associated with must reside in the same network border group.</p> <p>You can provision BYOIP address ranges to and advertise them in the following Local Zone network border groups:</p> <ul> <li> <p>us-east-1-dfw-2</p> </li> <li> <p>us-west-2-lax-1</p> </li> <li> <p>us-west-2-phx-2</p> </li> </ul> <note> <p>You cannot provision or advertise BYOIPv6 address ranges in Local Zones at this time.</p> </note>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.advertise_byoip_cidr_request.AdvertiseByoipCidrRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.advertise_byoip_cidr_result.AdvertiseByoipCidrResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.advertise_byoip_cidr

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.advertise_byoip_cidr.async_advertise_byoip_cidr(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.advertise_byoip_cidr_request.AdvertiseByoipCidrRequest = {}  # type: ignore[typeddict-item]
        input_["cidr"] = cidr
        if asn is not None:
            input_["asn"] = asn
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if network_border_group is not None:
            input_["network_border_group"] = network_border_group

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def allocate_address(
        self,
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        domain: Optional["aws_sdk_ec2.types.domain_type.DomainType"] = None,
        address: Optional["aws_sdk_ec2.types.public_ip_address.PublicIpAddress"] = None,
        public_ipv4_pool: Optional[
            "aws_sdk_ec2.types.ipv4_pool_ec2_id.Ipv4PoolEc2Id"
        ] = None,
        network_border_group: Optional["aws_sdk_ec2.types.string.String"] = None,
        customer_owned_ipv4_pool: Optional["aws_sdk_ec2.types.string.String"] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
        ipam_pool_id: Optional["aws_sdk_ec2.types.ipam_pool_id.IpamPoolId"] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.allocate_address_result.AllocateAddressResult":
        r"""<p>Allocates an Elastic IP address to your Amazon Web Services account. After you allocate the Elastic IP address you can associate it with an instance or network interface. After you release an Elastic IP address, it is released to the IP address pool and can be allocated to a different Amazon Web Services account.</p> <p>You can allocate an Elastic IP address from one of the following address pools:</p> <ul> <li> <p>Amazon's pool of IPv4 addresses</p> </li> <li> <p>Public IPv4 address range that you own and bring to your Amazon Web Services account using <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html\">Bring Your Own IP Addresses (BYOIP)</a> </p> </li> <li> <p>An IPv4 IPAM pool with an Amazon-provided or BYOIP public IPv4 address range</p> </li> <li> <p>IPv4 addresses from your on-premises network made available for use with an Outpost using a <a href=\"https://docs.aws.amazon.com/outposts/latest/userguide/routing.html#ip-addressing\">customer-owned IP address pool</a> (CoIP pool)</p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html\">Elastic IP Addresses</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>If you release an Elastic IP address, you might be able to recover it. You cannot recover an Elastic IP address that you released after it is allocated to another Amazon Web Services account. To attempt to recover an Elastic IP address that you released, specify it in this operation.</p> <p>You can allocate a carrier IP address which is a public IP address from a telecommunication carrier, to a network interface which resides in a subnet in a Wavelength Zone (for example an EC2 instance).</p>

        Args:
            domain: <p>The network (<code>vpc</code>).</p>
            address: <p>The Elastic IP address to recover or an IPv4 address from an address pool.</p>
            public_ipv4_pool: <p>The ID of an address pool that you own. Use this parameter to let Amazon EC2 select an address from the address pool. To specify a specific address from the address pool, use the <code>Address</code> parameter instead.</p>
            network_border_group: <p> A unique set of Availability Zones, Local Zones, or Wavelength Zones from which Amazon Web Services advertises IP addresses. Use this parameter to limit the IP address to this location. IP addresses cannot move between network border groups.</p>
            customer_owned_ipv4_pool: <p>The ID of a customer-owned address pool. Use this parameter to let Amazon EC2 select an address from the address pool. Alternatively, specify a specific address from the address pool.</p>
            tag_specifications: <p>The tags to assign to the Elastic IP address.</p>
            ipam_pool_id: <p>The ID of an IPAM pool which has an Amazon-provided or BYOIP public IPv4 CIDR provisioned to it. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-eip-pool.html\">Allocate sequential Elastic IP addresses from an IPAM pool</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>

        Examples:
            To allocate an Elastic IP address
            This example allocates an Elastic IP address.

            >>> await client.allocate_address()
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.allocate_address_request.AllocateAddressRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.allocate_address_result.AllocateAddressResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.allocate_address

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.allocate_address.async_allocate_address(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.allocate_address_request.AllocateAddressRequest = {}  # type: ignore[typeddict-item]
        if domain is not None:
            input_["domain"] = domain
        if address is not None:
            input_["address"] = address
        if public_ipv4_pool is not None:
            input_["public_ipv4_pool"] = public_ipv4_pool
        if network_border_group is not None:
            input_["network_border_group"] = network_border_group
        if customer_owned_ipv4_pool is not None:
            input_["customer_owned_ipv4_pool"] = customer_owned_ipv4_pool
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications
        if ipam_pool_id is not None:
            input_["ipam_pool_id"] = ipam_pool_id
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def allocate_hosts(
        self,
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        instance_family: Optional["aws_sdk_ec2.types.string.String"] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
        host_recovery: Optional["aws_sdk_ec2.types.host_recovery.HostRecovery"] = None,
        outpost_arn: Optional["aws_sdk_ec2.types.string.String"] = None,
        host_maintenance: Optional[
            "aws_sdk_ec2.types.host_maintenance.HostMaintenance"
        ] = None,
        asset_ids: Optional["aws_sdk_ec2.types.asset_id_list.AssetIdList"] = None,
        availability_zone_id: Optional[
            "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
        ] = None,
        auto_placement: Optional[
            "aws_sdk_ec2.types.auto_placement.AutoPlacement"
        ] = None,
        client_token: Optional["aws_sdk_ec2.types.string.String"] = None,
        instance_type: Optional["aws_sdk_ec2.types.string.String"] = None,
        quantity: Optional["aws_sdk_ec2.types.integer.Integer"] = None,
        availability_zone: Optional[
            "aws_sdk_ec2.types.availability_zone_name.AvailabilityZoneName"
        ] = None,
    ) -> "aws_sdk_ec2.types.allocate_hosts_result.AllocateHostsResult":
        r"""<p>Allocates a Dedicated Host to your account. At a minimum, specify the supported instance type or instance family, the Availability Zone in which to allocate the host, and the number of hosts to allocate.</p>

        Args:
            instance_family: <p>Specifies the instance family to be supported by the Dedicated Hosts. If you specify an instance family, the Dedicated Hosts support multiple instance types within that instance family.</p> <p>If you want the Dedicated Hosts to support a specific instance type only, omit this parameter and specify <b>InstanceType</b> instead. You cannot specify <b>InstanceFamily</b> and <b>InstanceType</b> in the same request.</p>
            tag_specifications: <p>The tags to apply to the Dedicated Host during creation.</p>
            host_recovery: <p>Indicates whether to enable or disable host recovery for the Dedicated Host. Host recovery is disabled by default. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-recovery.html\"> Host recovery</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>Default: <code>off</code> </p>
            outpost_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services Outpost on which to allocate the Dedicated Host. If you specify <b>OutpostArn</b>, you can optionally specify <b>AssetIds</b>.</p> <p>If you are allocating the Dedicated Host in a Region, omit this parameter.</p>
            host_maintenance: <p>Indicates whether to enable or disable host maintenance for the Dedicated Host. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-maintenance.html\">Host maintenance</a> in the <i>Amazon EC2 User Guide</i>.</p>
            asset_ids: <p>The IDs of the Outpost hardware assets on which to allocate the Dedicated Hosts. Targeting specific hardware assets on an Outpost can help to minimize latency between your workloads. This parameter is supported only if you specify <b>OutpostArn</b>. If you are allocating the Dedicated Hosts in a Region, omit this parameter.</p> <ul> <li> <p>If you specify this parameter, you can omit <b>Quantity</b>. In this case, Amazon EC2 allocates a Dedicated Host on each specified hardware asset.</p> </li> <li> <p>If you specify both <b>AssetIds</b> and <b>Quantity</b>, then the value for <b>Quantity</b> must be equal to the number of asset IDs specified.</p> </li> </ul>
            availability_zone_id: <p>The ID of the Availability Zone.</p>
            auto_placement: <p>Indicates whether the host accepts any untargeted instance launches that match its instance type configuration, or if it only accepts Host tenancy instance launches that specify its unique host ID. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-dedicated-hosts-work.html#dedicated-hosts-understanding\"> Understanding auto-placement and affinity</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>Default: <code>off</code> </p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring Idempotency</a>.</p>
            instance_type: <p>Specifies the instance type to be supported by the Dedicated Hosts. If you specify an instance type, the Dedicated Hosts support instances of the specified instance type only.</p> <p>If you want the Dedicated Hosts to support multiple instance types in a specific instance family, omit this parameter and specify <b>InstanceFamily</b> instead. You cannot specify <b>InstanceType</b> and <b>InstanceFamily</b> in the same request.</p>
            quantity: <p>The number of Dedicated Hosts to allocate to your account with these parameters. If you are allocating the Dedicated Hosts on an Outpost, and you specify <b>AssetIds</b>, you can omit this parameter. In this case, Amazon EC2 allocates a Dedicated Host on each specified hardware asset. If you specify both <b>AssetIds</b> and <b>Quantity</b>, then the value that you specify for <b>Quantity</b> must be equal to the number of asset IDs specified.</p>
            availability_zone: <p>The Availability Zone in which to allocate the Dedicated Host.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.allocate_hosts_request.AllocateHostsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.allocate_hosts_result.AllocateHostsResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.allocate_hosts

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.allocate_hosts.async_allocate_hosts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.allocate_hosts_request.AllocateHostsRequest = {}  # type: ignore[typeddict-item]
        if instance_family is not None:
            input_["instance_family"] = instance_family
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications
        if host_recovery is not None:
            input_["host_recovery"] = host_recovery
        if outpost_arn is not None:
            input_["outpost_arn"] = outpost_arn
        if host_maintenance is not None:
            input_["host_maintenance"] = host_maintenance
        if asset_ids is not None:
            input_["asset_ids"] = asset_ids
        if availability_zone_id is not None:
            input_["availability_zone_id"] = availability_zone_id
        if auto_placement is not None:
            input_["auto_placement"] = auto_placement
        if client_token is not None:
            input_["client_token"] = client_token
        if instance_type is not None:
            input_["instance_type"] = instance_type
        if quantity is not None:
            input_["quantity"] = quantity
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def allocate_ipam_pool_cidr(
        self,
        ipam_pool_id: "aws_sdk_ec2.types.ipam_pool_id.IpamPoolId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        cidr: Optional["aws_sdk_ec2.types.string.String"] = None,
        netmask_length: Optional["aws_sdk_ec2.types.integer.Integer"] = None,
        client_token: Optional["aws_sdk_ec2.types.string.String"] = None,
        description: Optional["aws_sdk_ec2.types.string.String"] = None,
        preview_next_cidr: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        allowed_cidrs: Optional[
            "aws_sdk_ec2.types.ipam_pool_allocation_allowed_cidrs.IpamPoolAllocationAllowedCidrs"
        ] = None,
        disallowed_cidrs: Optional[
            "aws_sdk_ec2.types.ipam_pool_allocation_disallowed_cidrs.IpamPoolAllocationDisallowedCidrs"
        ] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
    ) -> "aws_sdk_ec2.types.allocate_ipam_pool_cidr_result.AllocateIpamPoolCidrResult":
        r"""<p>Allocate a CIDR from an IPAM pool. The Region you use should be the IPAM pool locale. The locale is the Amazon Web Services Region where this IPAM pool is available for allocations.</p> <p>In IPAM, an allocation is a CIDR assignment from an IPAM pool to another IPAM pool or to a resource. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/allocate-cidrs-ipam.html\">Allocate CIDRs</a> in the <i>Amazon VPC IPAM User Guide</i>.</p> <note> <p>This action creates an allocation with strong consistency. The returned CIDR will not overlap with any other allocations from the same pool.</p> </note>

        Args:
            dry_run: <p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            ipam_pool_id: <p>The ID of the IPAM pool from which you would like to allocate a CIDR.</p>
            cidr: <p>The CIDR you would like to allocate from the IPAM pool. Note the following:</p> <ul> <li> <p>If there is no DefaultNetmaskLength allocation rule set on the pool, you must specify either the NetmaskLength or the CIDR.</p> </li> <li> <p>If the DefaultNetmaskLength allocation rule is set on the pool, you can specify either the NetmaskLength or the CIDR and the DefaultNetmaskLength allocation rule will be ignored.</p> </li> </ul> <p>Possible values: Any available IPv4 or IPv6 CIDR.</p>
            netmask_length: <p>The netmask length of the CIDR you would like to allocate from the IPAM pool. Note the following:</p> <ul> <li> <p>If there is no DefaultNetmaskLength allocation rule set on the pool, you must specify either the NetmaskLength or the CIDR.</p> </li> <li> <p>If the DefaultNetmaskLength allocation rule is set on the pool, you can specify either the NetmaskLength or the CIDR and the DefaultNetmaskLength allocation rule will be ignored.</p> </li> </ul> <p>Possible netmask lengths for IPv4 addresses are 0 - 32. Possible netmask lengths for IPv6 addresses are 0 - 128.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>
            description: <p>A description for the allocation.</p>
            preview_next_cidr: <p>A preview of the next available CIDR in a pool.</p>
            allowed_cidrs: <p>Include a particular CIDR range that can be returned by the pool. Allowed CIDRs are only allowed if using netmask length for allocation.</p>
            disallowed_cidrs: <p>Exclude a particular CIDR range from being returned by the pool. Disallowed CIDRs are only allowed if using netmask length for allocation.</p>
            tag_specifications: <p>The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> <p>If you specify tags, the request is authorized against the allocation resource in addition to the pool resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.allocate_ipam_pool_cidr_request.AllocateIpamPoolCidrRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.allocate_ipam_pool_cidr_result.AllocateIpamPoolCidrResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.allocate_ipam_pool_cidr

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.allocate_ipam_pool_cidr.async_allocate_ipam_pool_cidr(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.allocate_ipam_pool_cidr_request.AllocateIpamPoolCidrRequest = {}  # type: ignore[typeddict-item]
        if dry_run is not None:
            input_["dry_run"] = dry_run
        input_["ipam_pool_id"] = ipam_pool_id
        if cidr is not None:
            input_["cidr"] = cidr
        if netmask_length is not None:
            input_["netmask_length"] = netmask_length
        if client_token is not None:
            input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if preview_next_cidr is not None:
            input_["preview_next_cidr"] = preview_next_cidr
        if allowed_cidrs is not None:
            input_["allowed_cidrs"] = allowed_cidrs
        if disallowed_cidrs is not None:
            input_["disallowed_cidrs"] = disallowed_cidrs
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def apply_security_groups_to_client_vpn_target_network(
        self,
        client_vpn_endpoint_id: "aws_sdk_ec2.types.client_vpn_endpoint_id.ClientVpnEndpointId",
        vpc_id: "aws_sdk_ec2.types.vpc_id.VpcId",
        security_group_ids: "aws_sdk_ec2.types.client_vpn_security_group_id_set.ClientVpnSecurityGroupIdSet",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.apply_security_groups_to_client_vpn_target_network_result.ApplySecurityGroupsToClientVpnTargetNetworkResult":
        """<p>Applies a security group to the association between the target network and the Client VPN endpoint. This action replaces the existing security groups with the specified security groups.</p>

        Args:
            client_vpn_endpoint_id: <p>The ID of the Client VPN endpoint.</p>
            vpc_id: <p>The ID of the VPC in which the associated target network is located.</p>
            security_group_ids: <p>The IDs of the security groups to apply to the associated target network. Up to 5 security groups can be applied to an associated target network.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.apply_security_groups_to_client_vpn_target_network_request.ApplySecurityGroupsToClientVpnTargetNetworkRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.apply_security_groups_to_client_vpn_target_network_result.ApplySecurityGroupsToClientVpnTargetNetworkResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.apply_security_groups_to_client_vpn_target_network

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.apply_security_groups_to_client_vpn_target_network.async_apply_security_groups_to_client_vpn_target_network(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.apply_security_groups_to_client_vpn_target_network_request.ApplySecurityGroupsToClientVpnTargetNetworkRequest = {}  # type: ignore[typeddict-item]
        input_["client_vpn_endpoint_id"] = client_vpn_endpoint_id
        input_["vpc_id"] = vpc_id
        input_["security_group_ids"] = security_group_ids
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def assign_ipv6_addresses(
        self,
        network_interface_id: "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        ipv6_prefix_count: Optional["aws_sdk_ec2.types.integer.Integer"] = None,
        ipv6_prefixes: Optional["aws_sdk_ec2.types.ip_prefix_list.IpPrefixList"] = None,
        ipv6_addresses: Optional[
            "aws_sdk_ec2.types.ipv6_address_list.Ipv6AddressList"
        ] = None,
        ipv6_address_count: Optional["aws_sdk_ec2.types.integer.Integer"] = None,
    ) -> "aws_sdk_ec2.types.assign_ipv6_addresses_result.AssignIpv6AddressesResult":
        r"""<p>Assigns the specified IPv6 addresses to the specified network interface. You can specify specific IPv6 addresses, or you can specify the number of IPv6 addresses to be automatically assigned from the subnet's IPv6 CIDR block range. You can assign as many IPv6 addresses to a network interface as you can assign private IPv4 addresses, and the limit varies by instance type.</p> <p>You must specify either the IPv6 addresses or the IPv6 address count in the request. </p> <p>You can optionally use Prefix Delegation on the network interface. You must specify either the IPV6 Prefix Delegation prefixes, or the IPv6 Prefix Delegation count. For information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-prefix-eni.html\"> Assigning prefixes to network interfaces</a> in the <i>Amazon EC2 User Guide</i>.</p>

        Args:
            ipv6_prefix_count: <p>The number of IPv6 prefixes that Amazon Web Services automatically assigns to the network interface. You cannot use this option if you use the <code>Ipv6Prefixes</code> option.</p>
            ipv6_prefixes: <p>One or more IPv6 prefixes assigned to the network interface. You can't use this option if you use the <code>Ipv6PrefixCount</code> option.</p>
            network_interface_id: <p>The ID of the network interface.</p>
            ipv6_addresses: <p>The IPv6 addresses to be assigned to the network interface. You can't use this option if you're specifying a number of IPv6 addresses.</p>
            ipv6_address_count: <p>The number of additional IPv6 addresses to assign to the network interface. The specified number of IPv6 addresses are assigned in addition to the existing IPv6 addresses that are already assigned to the network interface. Amazon EC2 automatically selects the IPv6 addresses from the subnet range. You can't use this option if specifying specific IPv6 addresses.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.assign_ipv6_addresses_request.AssignIpv6AddressesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.assign_ipv6_addresses_result.AssignIpv6AddressesResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.assign_ipv6_addresses

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.assign_ipv6_addresses.async_assign_ipv6_addresses(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.assign_ipv6_addresses_request.AssignIpv6AddressesRequest = {}  # type: ignore[typeddict-item]
        if ipv6_prefix_count is not None:
            input_["ipv6_prefix_count"] = ipv6_prefix_count
        if ipv6_prefixes is not None:
            input_["ipv6_prefixes"] = ipv6_prefixes
        input_["network_interface_id"] = network_interface_id
        if ipv6_addresses is not None:
            input_["ipv6_addresses"] = ipv6_addresses
        if ipv6_address_count is not None:
            input_["ipv6_address_count"] = ipv6_address_count

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def assign_private_ip_addresses(
        self,
        network_interface_id: "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        ipv4_prefixes: Optional["aws_sdk_ec2.types.ip_prefix_list.IpPrefixList"] = None,
        ipv4_prefix_count: Optional["aws_sdk_ec2.types.integer.Integer"] = None,
        private_ip_addresses: Optional[
            "aws_sdk_ec2.types.private_ip_address_string_list.PrivateIpAddressStringList"
        ] = None,
        secondary_private_ip_address_count: Optional[
            "aws_sdk_ec2.types.integer.Integer"
        ] = None,
        allow_reassignment: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.assign_private_ip_addresses_result.AssignPrivateIpAddressesResult":
        r"""<p>Assigns the specified secondary private IP addresses to the specified network interface.</p> <p>You can specify specific secondary IP addresses, or you can specify the number of secondary IP addresses to be automatically assigned from the subnet's CIDR block range. The number of secondary IP addresses that you can assign to an instance varies by instance type. For more information about Elastic IP addresses, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html\">Elastic IP Addresses</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>When you move a secondary private IP address to another network interface, any Elastic IP address that is associated with the IP address is also moved.</p> <p>Remapping an IP address is an asynchronous operation. When you move an IP address from one network interface to another, check <code>network/interfaces/macs/mac/local-ipv4s</code> in the instance metadata to confirm that the remapping is complete.</p> <p>You must specify either the IP addresses or the IP address count in the request.</p> <p>You can optionally use Prefix Delegation on the network interface. You must specify either the IPv4 Prefix Delegation prefixes, or the IPv4 Prefix Delegation count. For information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-prefix-eni.html\"> Assigning prefixes to network interfaces</a> in the <i>Amazon EC2 User Guide</i>.</p>

        Args:
            ipv4_prefixes: <p>One or more IPv4 prefixes assigned to the network interface. You can't use this option if you use the <code>Ipv4PrefixCount</code> option.</p>
            ipv4_prefix_count: <p>The number of IPv4 prefixes that Amazon Web Services automatically assigns to the network interface. You can't use this option if you use the <code>Ipv4 Prefixes</code> option.</p>
            network_interface_id: <p>The ID of the network interface.</p>
            private_ip_addresses: <p>The IP addresses to be assigned as a secondary private IP address to the network interface. You can't specify this parameter when also specifying a number of secondary IP addresses.</p> <p>If you don't specify an IP address, Amazon EC2 automatically selects an IP address within the subnet range.</p>
            secondary_private_ip_address_count: <p>The number of secondary IP addresses to assign to the network interface. You can't specify this parameter when also specifying private IP addresses.</p>
            allow_reassignment: <p>Indicates whether to allow an IP address that is already assigned to another network interface or instance to be reassigned to the specified network interface.</p>

        Examples:
            To assign a specific secondary private IP address to an interface
            This example assigns the specified secondary private IP address to the specified network interface.

            >>> await client.assign_private_ip_addresses(network_interface_id='eni-e5aa89a3', private_ip_addresses=['10.0.0.82'])
            To assign secondary private IP addresses that Amazon EC2 selects to an interface
            This example assigns two secondary private IP addresses to the specified network interface. Amazon EC2 automatically assigns these IP addresses from the available IP addresses in the CIDR block range of the subnet the network interface is associated with.

            >>> await client.assign_private_ip_addresses(network_interface_id='eni-e5aa89a3', secondary_private_ip_address_count=2)
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.assign_private_ip_addresses_request.AssignPrivateIpAddressesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.assign_private_ip_addresses_result.AssignPrivateIpAddressesResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.assign_private_ip_addresses

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.assign_private_ip_addresses.async_assign_private_ip_addresses(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.assign_private_ip_addresses_request.AssignPrivateIpAddressesRequest = {}  # type: ignore[typeddict-item]
        if ipv4_prefixes is not None:
            input_["ipv4_prefixes"] = ipv4_prefixes
        if ipv4_prefix_count is not None:
            input_["ipv4_prefix_count"] = ipv4_prefix_count
        input_["network_interface_id"] = network_interface_id
        if private_ip_addresses is not None:
            input_["private_ip_addresses"] = private_ip_addresses
        if secondary_private_ip_address_count is not None:
            input_["secondary_private_ip_address_count"] = (
                secondary_private_ip_address_count
            )
        if allow_reassignment is not None:
            input_["allow_reassignment"] = allow_reassignment

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def assign_private_nat_gateway_address(
        self,
        nat_gateway_id: "aws_sdk_ec2.types.nat_gateway_id.NatGatewayId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        private_ip_addresses: Optional["aws_sdk_ec2.types.ip_list.IpList"] = None,
        private_ip_address_count: Optional[
            "aws_sdk_ec2.types.private_ip_address_count.PrivateIpAddressCount"
        ] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.assign_private_nat_gateway_address_result.AssignPrivateNatGatewayAddressResult":
        r"""<p>Assigns private IPv4 addresses to a private NAT gateway. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-working-with.html\">Work with NAT gateways</a> in the <i>Amazon VPC User Guide</i>.</p>

        Args:
            nat_gateway_id: <p>The ID of the NAT gateway.</p>
            private_ip_addresses: <p>The private IPv4 addresses you want to assign to the private NAT gateway.</p>
            private_ip_address_count: <p>The number of private IP addresses to assign to the NAT gateway. You can't specify this parameter when also specifying private IP addresses.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.assign_private_nat_gateway_address_request.AssignPrivateNatGatewayAddressRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.assign_private_nat_gateway_address_result.AssignPrivateNatGatewayAddressResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.assign_private_nat_gateway_address

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.assign_private_nat_gateway_address.async_assign_private_nat_gateway_address(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.assign_private_nat_gateway_address_request.AssignPrivateNatGatewayAddressRequest = {}  # type: ignore[typeddict-item]
        input_["nat_gateway_id"] = nat_gateway_id
        if private_ip_addresses is not None:
            input_["private_ip_addresses"] = private_ip_addresses
        if private_ip_address_count is not None:
            input_["private_ip_address_count"] = private_ip_address_count
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_address(
        self,
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        allocation_id: Optional["aws_sdk_ec2.types.allocation_id.AllocationId"] = None,
        instance_id: Optional["aws_sdk_ec2.types.instance_id.InstanceId"] = None,
        public_ip: Optional[
            "aws_sdk_ec2.types.eip_allocation_public_ip.EipAllocationPublicIp"
        ] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        network_interface_id: Optional[
            "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId"
        ] = None,
        private_ip_address: Optional["aws_sdk_ec2.types.string.String"] = None,
        allow_reassociation: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.associate_address_result.AssociateAddressResult":
        r"""<p>Associates an Elastic IP address, or carrier IP address (for instances that are in subnets in Wavelength Zones) with an instance or a network interface. Before you can use an Elastic IP address, you must allocate it to your account.</p> <p>If the Elastic IP address is already associated with a different instance, it is disassociated from that instance and associated with the specified instance. If you associate an Elastic IP address with an instance that has an existing Elastic IP address, the existing address is disassociated from the instance, but remains allocated to your account.</p> <p>[Subnets in Wavelength Zones] You can associate an IP address from the telecommunication carrier to the instance or network interface. </p> <p>You cannot associate an Elastic IP address with an interface in a different network border group.</p> <important> <p>This is an idempotent operation. If you perform the operation more than once, Amazon EC2 doesn't return an error, and you may be charged for each time the Elastic IP address is remapped to the same instance. For more information, see the <i>Elastic IP Addresses</i> section of <a href=\"http://aws.amazon.com/ec2/pricing/\">Amazon EC2 Pricing</a>.</p> </important>

        Args:
            allocation_id: <p>The allocation ID. This is required.</p>
            instance_id: <p>The ID of the instance. The instance must have exactly one attached network interface. You can specify either the instance ID or the network interface ID, but not both.</p>
            public_ip: <p>Deprecated.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            network_interface_id: <p>The ID of the network interface. If the instance has more than one network interface, you must specify a network interface ID.</p> <p>You can specify either the instance ID or the network interface ID, but not both. </p>
            private_ip_address: <p>The primary or secondary private IP address to associate with the Elastic IP address. If no private IP address is specified, the Elastic IP address is associated with the primary private IP address.</p>
            allow_reassociation: <p>Reassociation is automatic, but you can specify false to ensure the operation fails if the Elastic IP address is already associated with another resource.</p>

        Examples:
            To associate an Elastic IP address
            This example associates the specified Elastic IP address with the specified instance.

            >>> await client.associate_address(allocation_id='eipalloc-64d5890a', instance_id='i-0b263919b6498b123')
            To associate an Elastic IP address with a network interface
            This example associates the specified Elastic IP address with the specified network interface.

            >>> await client.associate_address(allocation_id='eipalloc-64d5890a', network_interface_id='eni-1a2b3c4d')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.associate_address_request.AssociateAddressRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.associate_address_result.AssociateAddressResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.associate_address

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.associate_address.async_associate_address(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.associate_address_request.AssociateAddressRequest = {}  # type: ignore[typeddict-item]
        if allocation_id is not None:
            input_["allocation_id"] = allocation_id
        if instance_id is not None:
            input_["instance_id"] = instance_id
        if public_ip is not None:
            input_["public_ip"] = public_ip
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if network_interface_id is not None:
            input_["network_interface_id"] = network_interface_id
        if private_ip_address is not None:
            input_["private_ip_address"] = private_ip_address
        if allow_reassociation is not None:
            input_["allow_reassociation"] = allow_reassociation

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_capacity_reservation_billing_owner(
        self,
        capacity_reservation_id: "aws_sdk_ec2.types.capacity_reservation_id.CapacityReservationId",
        unused_reservation_billing_owner_id: "aws_sdk_ec2.types.account_id.AccountID",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.associate_capacity_reservation_billing_owner_result.AssociateCapacityReservationBillingOwnerResult":
        r"""<p>Initiates a request to assign billing of the unused capacity of a shared Capacity Reservation to a consumer account that is consolidated under the same Amazon Web Services organizations payer account. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/assign-billing.html\">Billing assignment for shared Amazon EC2 Capacity Reservations</a>.</p>

        Args:
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            capacity_reservation_id: <p>The ID of the Capacity Reservation.</p>
            unused_reservation_billing_owner_id: <p>The ID of the consumer account to which to assign billing.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.associate_capacity_reservation_billing_owner_request.AssociateCapacityReservationBillingOwnerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.associate_capacity_reservation_billing_owner_result.AssociateCapacityReservationBillingOwnerResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.associate_capacity_reservation_billing_owner

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.associate_capacity_reservation_billing_owner.async_associate_capacity_reservation_billing_owner(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.associate_capacity_reservation_billing_owner_request.AssociateCapacityReservationBillingOwnerRequest = {}  # type: ignore[typeddict-item]
        if dry_run is not None:
            input_["dry_run"] = dry_run
        input_["capacity_reservation_id"] = capacity_reservation_id
        input_["unused_reservation_billing_owner_id"] = (
            unused_reservation_billing_owner_id
        )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_client_vpn_target_network(
        self,
        client_vpn_endpoint_id: "aws_sdk_ec2.types.client_vpn_endpoint_id.ClientVpnEndpointId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        subnet_id: Optional["aws_sdk_ec2.types.subnet_id.SubnetId"] = None,
        client_token: Optional["aws_sdk_ec2.types.string.String"] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        availability_zone: Optional[
            "aws_sdk_ec2.types.availability_zone_name.AvailabilityZoneName"
        ] = None,
        availability_zone_id: Optional[
            "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
        ] = None,
    ) -> "aws_sdk_ec2.types.associate_client_vpn_target_network_result.AssociateClientVpnTargetNetworkResult":
        r"""<p>Associates a target network with a Client VPN endpoint. A target network is a subnet in a VPC. You can associate multiple subnets from the same VPC with a Client VPN endpoint. You can associate only one subnet in each Availability Zone. We recommend that you associate at least two subnets to provide Availability Zone redundancy.</p> <p>If you specified a VPC when you created the Client VPN endpoint or if you have previous subnet associations, the specified subnet must be in the same VPC. To specify a subnet that's in a different VPC, you must first modify the Client VPN endpoint (<a>ModifyClientVpnEndpoint</a>) and change the VPC that's associated with it.</p>

        Args:
            client_vpn_endpoint_id: <p>The ID of the Client VPN endpoint.</p>
            subnet_id: <p>The ID of the subnet to associate with the Client VPN endpoint. Required for VPC-based endpoints. For Transit Gateway-based endpoints, use <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> instead.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            availability_zone: <p>The Availability Zone name for the Transit Gateway association. Required if when associating an Availability Zone with a Client VPN endpoint that uses a Transit Gateway. You cannot specify both <code>SubnetId</code> and <code>AvailabilityZone</code>.</p>
            availability_zone_id: <p>The Availability Zone ID for the Transit Gateway association. Required if when associating an Availability Zone with a Client VPN endpoint that uses a Transit Gateway. You cannot specify both <code>AvailabilityZone</code> and <code>AvailabilityZoneId</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.associate_client_vpn_target_network_request.AssociateClientVpnTargetNetworkRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.associate_client_vpn_target_network_result.AssociateClientVpnTargetNetworkResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.associate_client_vpn_target_network

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.associate_client_vpn_target_network.async_associate_client_vpn_target_network(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.associate_client_vpn_target_network_request.AssociateClientVpnTargetNetworkRequest = {}  # type: ignore[typeddict-item]
        input_["client_vpn_endpoint_id"] = client_vpn_endpoint_id
        if subnet_id is not None:
            input_["subnet_id"] = subnet_id
        if client_token is not None:
            input_["client_token"] = client_token
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if availability_zone_id is not None:
            input_["availability_zone_id"] = availability_zone_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_dhcp_options(
        self,
        dhcp_options_id: "aws_sdk_ec2.types.defaulting_dhcp_options_id.DefaultingDhcpOptionsId",
        vpc_id: "aws_sdk_ec2.types.vpc_id.VpcId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> None:
        r"""<p>Associates a set of DHCP options (that you've previously created) with the specified VPC, or associates no DHCP options with the VPC.</p> <p>After you associate the options with the VPC, any existing instances and all new instances that you launch in that VPC use the options. You don't need to restart or relaunch the instances. They automatically pick up the changes within a few hours, depending on how frequently the instance renews its DHCP lease. You can explicitly renew the lease using the operating system on the instance.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html\">DHCP option sets</a> in the <i>Amazon VPC User Guide</i>.</p>

        Args:
            dhcp_options_id: <p>The ID of the DHCP options set, or <code>default</code> to associate no DHCP options with the VPC.</p>
            vpc_id: <p>The ID of the VPC.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>

        Examples:
            To associate a DHCP options set with a VPC
            This example associates the specified DHCP options set with the specified VPC.

            >>> await client.associate_dhcp_options(dhcp_options_id='dopt-d9070ebb', vpc_id='vpc-a01106c2')
            To associate the default DHCP options set with a VPC
            This example associates the default DHCP options set with the specified VPC.

            >>> await client.associate_dhcp_options(dhcp_options_id='default', vpc_id='vpc-a01106c2')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.associate_dhcp_options_request.AssociateDhcpOptionsRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_ec2._operations.amazon_ec2.associate_dhcp_options

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.associate_dhcp_options.async_associate_dhcp_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.associate_dhcp_options_request.AssociateDhcpOptionsRequest = {}  # type: ignore[typeddict-item]
        input_["dhcp_options_id"] = dhcp_options_id
        input_["vpc_id"] = vpc_id
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_enclave_certificate_iam_role(
        self,
        certificate_arn: "aws_sdk_ec2.types.certificate_id.CertificateId",
        role_arn: "aws_sdk_ec2.types.role_id.RoleId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.associate_enclave_certificate_iam_role_result.AssociateEnclaveCertificateIamRoleResult":
        r"""<p>Associates an Identity and Access Management (IAM) role with an Certificate Manager (ACM) certificate. This enables the certificate to be used by the ACM for Nitro Enclaves application inside an enclave. For more information, see <a href=\"https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave-refapp.html\">Certificate Manager for Nitro Enclaves</a> in the <i>Amazon Web Services Nitro Enclaves User Guide</i>.</p> <p>When the IAM role is associated with the ACM certificate, the certificate, certificate chain, and encrypted private key are placed in an Amazon S3 location that only the associated IAM role can access. The private key of the certificate is encrypted with an Amazon Web Services managed key that has an attached attestation-based key policy.</p> <p>To enable the IAM role to access the Amazon S3 object, you must grant it permission to call <code>s3:GetObject</code> on the Amazon S3 bucket returned by the command. To enable the IAM role to access the KMS key, you must grant it permission to call <code>kms:Decrypt</code> on the KMS key returned by the command. For more information, see <a href=\"https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave-refapp.html#add-policy\"> Grant the role permission to access the certificate and encryption key</a> in the <i>Amazon Web Services Nitro Enclaves User Guide</i>.</p>

        Args:
            certificate_arn: <p>The ARN of the ACM certificate with which to associate the IAM role.</p>
            role_arn: <p>The ARN of the IAM role to associate with the ACM certificate. You can associate up to 16 IAM roles with an ACM certificate.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.associate_enclave_certificate_iam_role_request.AssociateEnclaveCertificateIamRoleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.associate_enclave_certificate_iam_role_result.AssociateEnclaveCertificateIamRoleResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.associate_enclave_certificate_iam_role

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.associate_enclave_certificate_iam_role.async_associate_enclave_certificate_iam_role(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.associate_enclave_certificate_iam_role_request.AssociateEnclaveCertificateIamRoleRequest = {}  # type: ignore[typeddict-item]
        input_["certificate_arn"] = certificate_arn
        input_["role_arn"] = role_arn
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_iam_instance_profile(
        self,
        iam_instance_profile: "aws_sdk_ec2.types.iam_instance_profile_specification.IamInstanceProfileSpecification",
        instance_id: "aws_sdk_ec2.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
    ) -> "aws_sdk_ec2.types.associate_iam_instance_profile_result.AssociateIamInstanceProfileResult":
        """<p>Associates an IAM instance profile with a running or stopped instance. You cannot associate more than one IAM instance profile with an instance.</p>

        Args:
            iam_instance_profile: <p>The IAM instance profile.</p>
            instance_id: <p>The ID of the instance.</p>

        Examples:
            To associate an IAM instance profile with an instance
            This example associates an IAM instance profile named admin-role with the specified instance.

            >>> await client.associate_iam_instance_profile(iam_instance_profile={'Name': 'admin-role'}, instance_id='i-123456789abcde123')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.associate_iam_instance_profile_request.AssociateIamInstanceProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.associate_iam_instance_profile_result.AssociateIamInstanceProfileResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.associate_iam_instance_profile

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.associate_iam_instance_profile.async_associate_iam_instance_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.associate_iam_instance_profile_request.AssociateIamInstanceProfileRequest = {}  # type: ignore[typeddict-item]
        input_["iam_instance_profile"] = iam_instance_profile
        input_["instance_id"] = instance_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_instance_event_window(
        self,
        instance_event_window_id: "aws_sdk_ec2.types.instance_event_window_id.InstanceEventWindowId",
        association_target: "aws_sdk_ec2.types.instance_event_window_association_request.InstanceEventWindowAssociationRequest",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.associate_instance_event_window_result.AssociateInstanceEventWindowResult":
        r"""<p>Associates one or more targets with an event window. Only one type of target (instance IDs, Dedicated Host IDs, or tags) can be specified with an event window.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/event-windows.html\">Define event windows for scheduled events</a> in the <i>Amazon EC2 User Guide</i>.</p>

        Args:
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            instance_event_window_id: <p>The ID of the event window.</p>
            association_target: <p>One or more targets associated with the specified event window.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.associate_instance_event_window_request.AssociateInstanceEventWindowRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.associate_instance_event_window_result.AssociateInstanceEventWindowResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.associate_instance_event_window

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.associate_instance_event_window.async_associate_instance_event_window(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.associate_instance_event_window_request.AssociateInstanceEventWindowRequest = {}  # type: ignore[typeddict-item]
        if dry_run is not None:
            input_["dry_run"] = dry_run
        input_["instance_event_window_id"] = instance_event_window_id
        input_["association_target"] = association_target

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_ipam_byoasn(
        self,
        asn: "aws_sdk_ec2.types.string.String",
        cidr: "aws_sdk_ec2.types.string.String",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.associate_ipam_byoasn_result.AssociateIpamByoasnResult":
        r"""<p>Associates your Autonomous System Number (ASN) with a BYOIP CIDR that you own in the same Amazon Web Services Region. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-byoasn.html\">Tutorial: Bring your ASN to IPAM</a> in the <i>Amazon VPC IPAM guide</i>.</p> <p>After the association succeeds, the ASN is eligible for advertisement. You can view the association with <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeByoipCidrs.html\">DescribeByoipCidrs</a>. You can advertise the CIDR with <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AdvertiseByoipCidr.html\">AdvertiseByoipCidr</a>.</p>

        Args:
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            asn: <p>A public 2-byte or 4-byte ASN.</p>
            cidr: <p>The BYOIP CIDR you want to associate with an ASN.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.associate_ipam_byoasn_request.AssociateIpamByoasnRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.associate_ipam_byoasn_result.AssociateIpamByoasnResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.associate_ipam_byoasn

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.associate_ipam_byoasn.async_associate_ipam_byoasn(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.associate_ipam_byoasn_request.AssociateIpamByoasnRequest = {}  # type: ignore[typeddict-item]
        if dry_run is not None:
            input_["dry_run"] = dry_run
        input_["asn"] = asn
        input_["cidr"] = cidr

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_ipam_resource_discovery(
        self,
        ipam_id: "aws_sdk_ec2.types.ipam_id.IpamId",
        ipam_resource_discovery_id: "aws_sdk_ec2.types.ipam_resource_discovery_id.IpamResourceDiscoveryId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
        client_token: Optional["aws_sdk_ec2.types.string.String"] = None,
    ) -> "aws_sdk_ec2.types.associate_ipam_resource_discovery_result.AssociateIpamResourceDiscoveryResult":
        """<p>Associates an IPAM resource discovery with an Amazon VPC IPAM. A resource discovery is an IPAM component that enables IPAM to manage and monitor resources that belong to the owning account.</p>

        Args:
            dry_run: <p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            ipam_id: <p>An IPAM ID.</p>
            ipam_resource_discovery_id: <p>A resource discovery ID.</p>
            tag_specifications: <p>Tag specifications.</p>
            client_token: <p>A client token.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.associate_ipam_resource_discovery_request.AssociateIpamResourceDiscoveryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.associate_ipam_resource_discovery_result.AssociateIpamResourceDiscoveryResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.associate_ipam_resource_discovery

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.associate_ipam_resource_discovery.async_associate_ipam_resource_discovery(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.associate_ipam_resource_discovery_request.AssociateIpamResourceDiscoveryRequest = {}  # type: ignore[typeddict-item]
        if dry_run is not None:
            input_["dry_run"] = dry_run
        input_["ipam_id"] = ipam_id
        input_["ipam_resource_discovery_id"] = ipam_resource_discovery_id
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_nat_gateway_address(
        self,
        nat_gateway_id: "aws_sdk_ec2.types.nat_gateway_id.NatGatewayId",
        allocation_ids: "aws_sdk_ec2.types.allocation_id_list.AllocationIdList",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        private_ip_addresses: Optional["aws_sdk_ec2.types.ip_list.IpList"] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        availability_zone: Optional[
            "aws_sdk_ec2.types.availability_zone_name.AvailabilityZoneName"
        ] = None,
        availability_zone_id: Optional[
            "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
        ] = None,
    ) -> "aws_sdk_ec2.types.associate_nat_gateway_address_result.AssociateNatGatewayAddressResult":
        r"""<p>Associates Elastic IP addresses (EIPs) and private IPv4 addresses with a public NAT gateway. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-working-with.html\">Work with NAT gateways</a> in the <i>Amazon VPC User Guide</i>.</p> <p>By default, you can associate up to 2 Elastic IP addresses per public NAT gateway. You can increase the limit by requesting a quota adjustment. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html#vpc-limits-eips\">Elastic IP address quotas</a> in the <i>Amazon VPC User Guide</i>.</p> <important> <p>When you associate an EIP or secondary EIPs with a public NAT gateway, the network border group of the EIPs must match the network border group of the Availability Zone (AZ) that the public NAT gateway is in. If it's not the same, the EIP will fail to associate. You can see the network border group for the subnet's AZ by viewing the details of the subnet. Similarly, you can view the network border group of an EIP by viewing the details of the EIP address. For more information about network border groups and EIPs, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/WorkWithEIPs.html\">Allocate an Elastic IP address</a> in the <i>Amazon VPC User Guide</i>. </p> </important>

        Args:
            nat_gateway_id: <p>The ID of the NAT gateway.</p>
            allocation_ids: <p>The allocation IDs of EIPs that you want to associate with your NAT gateway.</p>
            private_ip_addresses: <p>The private IPv4 addresses that you want to assign to the NAT gateway.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            availability_zone: <p>For regional NAT gateways only: The Availability Zone where you want to associate an Elastic IP address (EIP). The regional NAT gateway uses a separate EIP in each AZ to handle outbound NAT traffic from that AZ.</p> <p>A regional NAT gateway is a single NAT Gateway that works across multiple availability zones (AZs) in your VPC, providing redundancy, scalability and availability across all the AZs in a Region.</p>
            availability_zone_id: <p>For regional NAT gateways only: The ID of the Availability Zone where you want to associate an Elastic IP address (EIP). The regional NAT gateway uses a separate EIP in each AZ to handle outbound NAT traffic from that AZ. Use this instead of AvailabilityZone for consistent identification of AZs across Amazon Web Services Regions. </p> <p>A regional NAT gateway is a single NAT Gateway that works across multiple availability zones (AZs) in your VPC, providing redundancy, scalability and availability across all the AZs in a Region.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.associate_nat_gateway_address_request.AssociateNatGatewayAddressRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.associate_nat_gateway_address_result.AssociateNatGatewayAddressResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.associate_nat_gateway_address

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.associate_nat_gateway_address.async_associate_nat_gateway_address(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.associate_nat_gateway_address_request.AssociateNatGatewayAddressRequest = {}  # type: ignore[typeddict-item]
        input_["nat_gateway_id"] = nat_gateway_id
        input_["allocation_ids"] = allocation_ids
        if private_ip_addresses is not None:
            input_["private_ip_addresses"] = private_ip_addresses
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if availability_zone_id is not None:
            input_["availability_zone_id"] = availability_zone_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_route_server(
        self,
        route_server_id: "aws_sdk_ec2.types.route_server_id.RouteServerId",
        vpc_id: "aws_sdk_ec2.types.vpc_id.VpcId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.associate_route_server_result.AssociateRouteServerResult":
        r"""<p>Associates a route server with a VPC to enable dynamic route updates.</p> <p>A route server association is the connection established between a route server and a VPC.</p> <p>For more information see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/dynamic-routing-route-server.html\">Dynamic routing in your VPC with VPC Route Server</a> in the <i>Amazon VPC User Guide</i>.</p>

        Args:
            route_server_id: <p>The unique identifier for the route server to be associated.</p>
            vpc_id: <p>The ID of the VPC to associate with the route server.</p>
            dry_run: <p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.associate_route_server_request.AssociateRouteServerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.associate_route_server_result.AssociateRouteServerResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.associate_route_server

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.associate_route_server.async_associate_route_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.associate_route_server_request.AssociateRouteServerRequest = {}  # type: ignore[typeddict-item]
        input_["route_server_id"] = route_server_id
        input_["vpc_id"] = vpc_id
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_route_table(
        self,
        route_table_id: "aws_sdk_ec2.types.route_table_id.RouteTableId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        gateway_id: Optional[
            "aws_sdk_ec2.types.route_gateway_id.RouteGatewayId"
        ] = None,
        public_ipv4_pool: Optional[
            "aws_sdk_ec2.types.ipv4_pool_ec2_id.Ipv4PoolEc2Id"
        ] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        subnet_id: Optional["aws_sdk_ec2.types.subnet_id.SubnetId"] = None,
    ) -> "aws_sdk_ec2.types.associate_route_table_result.AssociateRouteTableResult":
        r"""<p>Associates a subnet in your VPC or an internet gateway or virtual private gateway attached to your VPC with a route table in your VPC. This association causes traffic from the subnet or gateway to be routed according to the routes in the route table. The action returns an association ID, which you need in order to disassociate the route table later. A route table can be associated with multiple subnets.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html\">Route tables</a> in the <i>Amazon VPC User Guide</i>.</p>

        Args:
            gateway_id: <p>The ID of the internet gateway or virtual private gateway.</p>
            public_ipv4_pool: <p>The ID of a public IPv4 pool. A public IPv4 pool is a pool of IPv4 addresses that you've brought to Amazon Web Services with BYOIP.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            subnet_id: <p>The ID of the subnet.</p>
            route_table_id: <p>The ID of the route table.</p>

        Examples:
            To associate a route table with a subnet
            This example associates the specified route table with the specified subnet.

            >>> await client.associate_route_table(subnet_id='subnet-9d4a7b6', route_table_id='rtb-22574640')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.associate_route_table_request.AssociateRouteTableRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.associate_route_table_result.AssociateRouteTableResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.associate_route_table

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.associate_route_table.async_associate_route_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.associate_route_table_request.AssociateRouteTableRequest = {}  # type: ignore[typeddict-item]
        if gateway_id is not None:
            input_["gateway_id"] = gateway_id
        if public_ipv4_pool is not None:
            input_["public_ipv4_pool"] = public_ipv4_pool
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if subnet_id is not None:
            input_["subnet_id"] = subnet_id
        input_["route_table_id"] = route_table_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_security_group_vpc(
        self,
        group_id: "aws_sdk_ec2.types.security_group_id.SecurityGroupId",
        vpc_id: "aws_sdk_ec2.types.vpc_id.VpcId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.associate_security_group_vpc_result.AssociateSecurityGroupVpcResult":
        """<p>Associates a security group with another VPC in the same Region. This enables you to use the same security group with network interfaces and instances in the specified VPC.</p> <note> <ul> <li> <p>The VPC you want to associate the security group with must be in the same Region.</p> </li> <li> <p>You can associate the security group with another VPC if your account owns the VPC or if the VPC was shared with you.</p> </li> <li> <p>You must own the security group.</p> </li> <li> <p>You cannot use this feature with default security groups.</p> </li> <li> <p>You cannot use this feature with the default VPC.</p> </li> </ul> </note>

        Args:
            group_id: <p>A security group ID.</p>
            vpc_id: <p>A VPC ID.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.associate_security_group_vpc_request.AssociateSecurityGroupVpcRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.associate_security_group_vpc_result.AssociateSecurityGroupVpcResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.associate_security_group_vpc

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.associate_security_group_vpc.async_associate_security_group_vpc(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.associate_security_group_vpc_request.AssociateSecurityGroupVpcRequest = {}  # type: ignore[typeddict-item]
        input_["group_id"] = group_id
        input_["vpc_id"] = vpc_id
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_subnet_cidr_block(
        self,
        subnet_id: "aws_sdk_ec2.types.subnet_id.SubnetId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        ipv6_ipam_pool_id: Optional["aws_sdk_ec2.types.ipam_pool_id.IpamPoolId"] = None,
        ipv6_netmask_length: Optional[
            "aws_sdk_ec2.types.netmask_length.NetmaskLength"
        ] = None,
        ipv6_cidr_block: Optional["aws_sdk_ec2.types.string.String"] = None,
    ) -> "aws_sdk_ec2.types.associate_subnet_cidr_block_result.AssociateSubnetCidrBlockResult":
        """<p>Associates a CIDR block with your subnet. You can only associate a single IPv6 CIDR block with your subnet.</p>

        Args:
            ipv6_ipam_pool_id: <p>An IPv6 IPAM pool ID.</p>
            ipv6_netmask_length: <p>An IPv6 netmask length.</p>
            subnet_id: <p>The ID of your subnet.</p>
            ipv6_cidr_block: <p>The IPv6 CIDR block for your subnet.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.associate_subnet_cidr_block_request.AssociateSubnetCidrBlockRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.associate_subnet_cidr_block_result.AssociateSubnetCidrBlockResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.associate_subnet_cidr_block

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.associate_subnet_cidr_block.async_associate_subnet_cidr_block(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.associate_subnet_cidr_block_request.AssociateSubnetCidrBlockRequest = {}  # type: ignore[typeddict-item]
        if ipv6_ipam_pool_id is not None:
            input_["ipv6_ipam_pool_id"] = ipv6_ipam_pool_id
        if ipv6_netmask_length is not None:
            input_["ipv6_netmask_length"] = ipv6_netmask_length
        input_["subnet_id"] = subnet_id
        if ipv6_cidr_block is not None:
            input_["ipv6_cidr_block"] = ipv6_cidr_block

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_transit_gateway_multicast_domain(
        self,
        transit_gateway_multicast_domain_id: "aws_sdk_ec2.types.transit_gateway_multicast_domain_id.TransitGatewayMulticastDomainId",
        transit_gateway_attachment_id: "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId",
        subnet_ids: "aws_sdk_ec2.types.transit_gateway_subnet_id_list.TransitGatewaySubnetIdList",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.associate_transit_gateway_multicast_domain_result.AssociateTransitGatewayMulticastDomainResult":
        r"""<p>Associates the specified subnets and transit gateway attachments with the specified transit gateway multicast domain.</p> <p>The transit gateway attachment must be in the available state before you can add a resource. Use <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGatewayAttachments.html\">DescribeTransitGatewayAttachments</a> to see the state of the attachment.</p>

        Args:
            transit_gateway_multicast_domain_id: <p>The ID of the transit gateway multicast domain.</p>
            transit_gateway_attachment_id: <p>The ID of the transit gateway attachment to associate with the transit gateway multicast domain.</p>
            subnet_ids: <p>The IDs of the subnets to associate with the transit gateway multicast domain.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.associate_transit_gateway_multicast_domain_request.AssociateTransitGatewayMulticastDomainRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.associate_transit_gateway_multicast_domain_result.AssociateTransitGatewayMulticastDomainResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.associate_transit_gateway_multicast_domain

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.associate_transit_gateway_multicast_domain.async_associate_transit_gateway_multicast_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.associate_transit_gateway_multicast_domain_request.AssociateTransitGatewayMulticastDomainRequest = {}  # type: ignore[typeddict-item]
        input_["transit_gateway_multicast_domain_id"] = (
            transit_gateway_multicast_domain_id
        )
        input_["transit_gateway_attachment_id"] = transit_gateway_attachment_id
        input_["subnet_ids"] = subnet_ids
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_transit_gateway_policy_table(
        self,
        transit_gateway_policy_table_id: "aws_sdk_ec2.types.transit_gateway_policy_table_id.TransitGatewayPolicyTableId",
        transit_gateway_attachment_id: "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.associate_transit_gateway_policy_table_result.AssociateTransitGatewayPolicyTableResult":
        """<p>Associates the specified transit gateway attachment with a transit gateway policy table.</p>

        Args:
            transit_gateway_policy_table_id: <p>The ID of the transit gateway policy table to associate with the transit gateway attachment.</p>
            transit_gateway_attachment_id: <p>The ID of the transit gateway attachment to associate with the policy table.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.associate_transit_gateway_policy_table_request.AssociateTransitGatewayPolicyTableRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.associate_transit_gateway_policy_table_result.AssociateTransitGatewayPolicyTableResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.associate_transit_gateway_policy_table

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.associate_transit_gateway_policy_table.async_associate_transit_gateway_policy_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.associate_transit_gateway_policy_table_request.AssociateTransitGatewayPolicyTableRequest = {}  # type: ignore[typeddict-item]
        input_["transit_gateway_policy_table_id"] = transit_gateway_policy_table_id
        input_["transit_gateway_attachment_id"] = transit_gateway_attachment_id
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_transit_gateway_route_table(
        self,
        transit_gateway_route_table_id: "aws_sdk_ec2.types.transit_gateway_route_table_id.TransitGatewayRouteTableId",
        transit_gateway_attachment_id: "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.associate_transit_gateway_route_table_result.AssociateTransitGatewayRouteTableResult":
        """<p>Associates the specified attachment with the specified transit gateway route table. You can associate only one route table with an attachment.</p>

        Args:
            transit_gateway_route_table_id: <p>The ID of the transit gateway route table.</p>
            transit_gateway_attachment_id: <p>The ID of the attachment.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.associate_transit_gateway_route_table_request.AssociateTransitGatewayRouteTableRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.associate_transit_gateway_route_table_result.AssociateTransitGatewayRouteTableResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.associate_transit_gateway_route_table

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.associate_transit_gateway_route_table.async_associate_transit_gateway_route_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.associate_transit_gateway_route_table_request.AssociateTransitGatewayRouteTableRequest = {}  # type: ignore[typeddict-item]
        input_["transit_gateway_route_table_id"] = transit_gateway_route_table_id
        input_["transit_gateway_attachment_id"] = transit_gateway_attachment_id
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_trunk_interface(
        self,
        branch_interface_id: "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId",
        trunk_interface_id: "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        vlan_id: Optional["aws_sdk_ec2.types.integer.Integer"] = None,
        gre_key: Optional["aws_sdk_ec2.types.integer.Integer"] = None,
        client_token: Optional["aws_sdk_ec2.types.string.String"] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.associate_trunk_interface_result.AssociateTrunkInterfaceResult":
        r"""<p>Associates a branch network interface with a trunk network interface.</p> <p>Before you create the association, use <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInterface.html\">CreateNetworkInterface</a> command and set the interface type to <code>trunk</code>. You must also create a network interface for each branch network interface that you want to associate with the trunk network interface.</p>

        Args:
            branch_interface_id: <p>The ID of the branch network interface.</p>
            trunk_interface_id: <p>The ID of the trunk network interface.</p>
            vlan_id: <p>The ID of the VLAN. This applies to the VLAN protocol.</p>
            gre_key: <p>The application key. This applies to the GRE protocol.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.associate_trunk_interface_request.AssociateTrunkInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.associate_trunk_interface_result.AssociateTrunkInterfaceResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.associate_trunk_interface

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.associate_trunk_interface.async_associate_trunk_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.associate_trunk_interface_request.AssociateTrunkInterfaceRequest = {}  # type: ignore[typeddict-item]
        input_["branch_interface_id"] = branch_interface_id
        input_["trunk_interface_id"] = trunk_interface_id
        if vlan_id is not None:
            input_["vlan_id"] = vlan_id
        if gre_key is not None:
            input_["gre_key"] = gre_key
        if client_token is not None:
            input_["client_token"] = client_token
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_vpc_cidr_block(
        self,
        vpc_id: "aws_sdk_ec2.types.vpc_id.VpcId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        cidr_block: Optional["aws_sdk_ec2.types.string.String"] = None,
        ipv6_cidr_block_network_border_group: Optional[
            "aws_sdk_ec2.types.string.String"
        ] = None,
        ipv6_pool: Optional["aws_sdk_ec2.types.ipv6_pool_ec2_id.Ipv6PoolEc2Id"] = None,
        ipv6_cidr_block: Optional["aws_sdk_ec2.types.string.String"] = None,
        ipv4_ipam_pool_id: Optional["aws_sdk_ec2.types.ipam_pool_id.IpamPoolId"] = None,
        ipv4_netmask_length: Optional[
            "aws_sdk_ec2.types.netmask_length.NetmaskLength"
        ] = None,
        ipv6_ipam_pool_id: Optional["aws_sdk_ec2.types.ipam_pool_id.IpamPoolId"] = None,
        ipv6_netmask_length: Optional[
            "aws_sdk_ec2.types.netmask_length.NetmaskLength"
        ] = None,
        amazon_provided_ipv6_cidr_block: Optional[
            "aws_sdk_ec2.types.boolean.Boolean"
        ] = None,
    ) -> (
        "aws_sdk_ec2.types.associate_vpc_cidr_block_result.AssociateVpcCidrBlockResult"
    ):
        r"""<p>Associates a CIDR block with your VPC. You can associate a secondary IPv4 CIDR block, an Amazon-provided IPv6 CIDR block, or an IPv6 CIDR block from an IPv6 address pool that you provisioned through bring your own IP addresses (<a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html\">BYOIP</a>).</p> <p>You must specify one of the following in the request: an IPv4 CIDR block, an IPv6 pool, or an Amazon-provided IPv6 CIDR block.</p> <p>For more information about associating CIDR blocks with your VPC and applicable restrictions, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html\">IP addressing for your VPCs and subnets</a> in the <i>Amazon VPC User Guide</i>.</p>

        Args:
            cidr_block: <p>An IPv4 CIDR block to associate with the VPC.</p>
            ipv6_cidr_block_network_border_group: <p>The name of the location from which we advertise the IPV6 CIDR block. Use this parameter to limit the CIDR block to this location.</p> <p> You must set <code>AmazonProvidedIpv6CidrBlock</code> to <code>true</code> to use this parameter.</p> <p> You can have one IPv6 CIDR block association per network border group.</p>
            ipv6_pool: <p>The ID of an IPv6 address pool from which to allocate the IPv6 CIDR block.</p>
            ipv6_cidr_block: <p>An IPv6 CIDR block from the IPv6 address pool. You must also specify <code>Ipv6Pool</code> in the request.</p> <p>To let Amazon choose the IPv6 CIDR block for you, omit this parameter.</p>
            ipv4_ipam_pool_id: <p>Associate a CIDR allocated from an IPv4 IPAM pool to a VPC. For more information about Amazon VPC IP Address Manager (IPAM), see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html\">What is IPAM?</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>
            ipv4_netmask_length: <p>The netmask length of the IPv4 CIDR you would like to associate from an Amazon VPC IP Address Manager (IPAM) pool. For more information about IPAM, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html\">What is IPAM?</a> in the <i>Amazon VPC IPAM User Guide</i>. </p>
            ipv6_ipam_pool_id: <p>Associates a CIDR allocated from an IPv6 IPAM pool to a VPC. For more information about Amazon VPC IP Address Manager (IPAM), see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html\">What is IPAM?</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>
            ipv6_netmask_length: <p>The netmask length of the IPv6 CIDR you would like to associate from an Amazon VPC IP Address Manager (IPAM) pool. For more information about IPAM, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html\">What is IPAM?</a> in the <i>Amazon VPC IPAM User Guide</i>. </p>
            vpc_id: <p>The ID of the VPC.</p>
            amazon_provided_ipv6_cidr_block: <p>Requests an Amazon-provided IPv6 CIDR block with a /56 prefix length for the VPC. You cannot specify the range of IPv6 addresses or the size of the CIDR block.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.associate_vpc_cidr_block_request.AssociateVpcCidrBlockRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.associate_vpc_cidr_block_result.AssociateVpcCidrBlockResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.associate_vpc_cidr_block

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.associate_vpc_cidr_block.async_associate_vpc_cidr_block(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.associate_vpc_cidr_block_request.AssociateVpcCidrBlockRequest = {}  # type: ignore[typeddict-item]
        if cidr_block is not None:
            input_["cidr_block"] = cidr_block
        if ipv6_cidr_block_network_border_group is not None:
            input_["ipv6_cidr_block_network_border_group"] = (
                ipv6_cidr_block_network_border_group
            )
        if ipv6_pool is not None:
            input_["ipv6_pool"] = ipv6_pool
        if ipv6_cidr_block is not None:
            input_["ipv6_cidr_block"] = ipv6_cidr_block
        if ipv4_ipam_pool_id is not None:
            input_["ipv4_ipam_pool_id"] = ipv4_ipam_pool_id
        if ipv4_netmask_length is not None:
            input_["ipv4_netmask_length"] = ipv4_netmask_length
        if ipv6_ipam_pool_id is not None:
            input_["ipv6_ipam_pool_id"] = ipv6_ipam_pool_id
        if ipv6_netmask_length is not None:
            input_["ipv6_netmask_length"] = ipv6_netmask_length
        input_["vpc_id"] = vpc_id
        if amazon_provided_ipv6_cidr_block is not None:
            input_["amazon_provided_ipv6_cidr_block"] = amazon_provided_ipv6_cidr_block

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def attach_classic_link_vpc(
        self,
        instance_id: "aws_sdk_ec2.types.instance_id.InstanceId",
        vpc_id: "aws_sdk_ec2.types.vpc_id.VpcId",
        groups: "aws_sdk_ec2.types.group_id_string_list.GroupIdStringList",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.attach_classic_link_vpc_result.AttachClassicLinkVpcResult":
        """<note> <p>This action is deprecated.</p> </note> <p>Links an EC2-Classic instance to a ClassicLink-enabled VPC through one or more of the VPC security groups. You cannot link an EC2-Classic instance to more than one VPC at a time. You can only link an instance that's in the <code>running</code> state. An instance is automatically unlinked from a VPC when it's stopped - you can link it to the VPC again when you restart it.</p> <p>After you've linked an instance, you cannot change the VPC security groups that are associated with it. To change the security groups, you must first unlink the instance, and then link it again.</p> <p>Linking your instance to a VPC is sometimes referred to as <i>attaching</i> your instance.</p>

        Args:
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            instance_id: <p>The ID of the EC2-Classic instance.</p>
            vpc_id: <p>The ID of the ClassicLink-enabled VPC.</p>
            groups: <p>The IDs of the security groups. You cannot specify security groups from a different VPC.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.attach_classic_link_vpc_request.AttachClassicLinkVpcRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.attach_classic_link_vpc_result.AttachClassicLinkVpcResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.attach_classic_link_vpc

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.attach_classic_link_vpc.async_attach_classic_link_vpc(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.attach_classic_link_vpc_request.AttachClassicLinkVpcRequest = {}  # type: ignore[typeddict-item]
        if dry_run is not None:
            input_["dry_run"] = dry_run
        input_["instance_id"] = instance_id
        input_["vpc_id"] = vpc_id
        input_["groups"] = groups

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def attach_internet_gateway(
        self,
        internet_gateway_id: "aws_sdk_ec2.types.internet_gateway_id.InternetGatewayId",
        vpc_id: "aws_sdk_ec2.types.vpc_id.VpcId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> None:
        r"""<p>Attaches an internet gateway or a virtual private gateway to a VPC, enabling connectivity between the internet and the VPC. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html\">Internet gateways</a> in the <i>Amazon VPC User Guide</i>.</p>

        Args:
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            internet_gateway_id: <p>The ID of the internet gateway.</p>
            vpc_id: <p>The ID of the VPC.</p>

        Examples:
            To attach an Internet gateway to a VPC
            This example attaches the specified Internet gateway to the specified VPC.

            >>> await client.attach_internet_gateway(internet_gateway_id='igw-c0a643a9', vpc_id='vpc-a01106c2')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.attach_internet_gateway_request.AttachInternetGatewayRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_ec2._operations.amazon_ec2.attach_internet_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.attach_internet_gateway.async_attach_internet_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.attach_internet_gateway_request.AttachInternetGatewayRequest = {}  # type: ignore[typeddict-item]
        if dry_run is not None:
            input_["dry_run"] = dry_run
        input_["internet_gateway_id"] = internet_gateway_id
        input_["vpc_id"] = vpc_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def attach_network_interface(
        self,
        network_interface_id: "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId",
        instance_id: "aws_sdk_ec2.types.instance_id.InstanceId",
        device_index: "aws_sdk_ec2.types.integer.Integer",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        network_card_index: Optional["aws_sdk_ec2.types.integer.Integer"] = None,
        ena_srd_specification: Optional[
            "aws_sdk_ec2.types.ena_srd_specification.EnaSrdSpecification"
        ] = None,
        ena_queue_count: Optional["aws_sdk_ec2.types.integer.Integer"] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> (
        "aws_sdk_ec2.types.attach_network_interface_result.AttachNetworkInterfaceResult"
    ):
        """<p>Attaches a network interface to an instance.</p>

        Args:
            network_card_index: <p>The index of the network card. Some instance types support multiple network cards. The primary network interface must be assigned to network card index 0. The default is network card index 0.</p>
            ena_srd_specification: <p>Configures ENA Express for the network interface that this action attaches to the instance.</p>
            ena_queue_count: <p>The number of ENA queues to be created with the instance.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            network_interface_id: <p>The ID of the network interface.</p>
            instance_id: <p>The ID of the instance.</p>
            device_index: <p>The index of the device for the network interface attachment.</p>

        Examples:
            To attach a network interface to an instance
            This example attaches the specified network interface to the specified instance.

            >>> await client.attach_network_interface(network_interface_id='eni-e5aa89a3', instance_id='i-1234567890abcdef0', device_index=1)
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.attach_network_interface_request.AttachNetworkInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.attach_network_interface_result.AttachNetworkInterfaceResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.attach_network_interface

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.attach_network_interface.async_attach_network_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.attach_network_interface_request.AttachNetworkInterfaceRequest = {}  # type: ignore[typeddict-item]
        if network_card_index is not None:
            input_["network_card_index"] = network_card_index
        if ena_srd_specification is not None:
            input_["ena_srd_specification"] = ena_srd_specification
        if ena_queue_count is not None:
            input_["ena_queue_count"] = ena_queue_count
        if dry_run is not None:
            input_["dry_run"] = dry_run
        input_["network_interface_id"] = network_interface_id
        input_["instance_id"] = instance_id
        input_["device_index"] = device_index

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def attach_verified_access_trust_provider(
        self,
        verified_access_instance_id: "aws_sdk_ec2.types.verified_access_instance_id.VerifiedAccessInstanceId",
        verified_access_trust_provider_id: "aws_sdk_ec2.types.verified_access_trust_provider_id.VerifiedAccessTrustProviderId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        client_token: Optional["aws_sdk_ec2.types.string.String"] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.attach_verified_access_trust_provider_result.AttachVerifiedAccessTrustProviderResult":
        r"""<p>Attaches the specified Amazon Web Services Verified Access trust provider to the specified Amazon Web Services Verified Access instance.</p>

        Args:
            verified_access_instance_id: <p>The ID of the Verified Access instance.</p>
            verified_access_trust_provider_id: <p>The ID of the Verified Access trust provider.</p>
            client_token: <p>A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.attach_verified_access_trust_provider_request.AttachVerifiedAccessTrustProviderRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.attach_verified_access_trust_provider_result.AttachVerifiedAccessTrustProviderResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.attach_verified_access_trust_provider

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.attach_verified_access_trust_provider.async_attach_verified_access_trust_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.attach_verified_access_trust_provider_request.AttachVerifiedAccessTrustProviderRequest = {}  # type: ignore[typeddict-item]
        input_["verified_access_instance_id"] = verified_access_instance_id
        input_["verified_access_trust_provider_id"] = verified_access_trust_provider_id
        if client_token is not None:
            input_["client_token"] = client_token
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def attach_volume(
        self,
        device: "aws_sdk_ec2.types.string.String",
        instance_id: "aws_sdk_ec2.types.instance_id.InstanceId",
        volume_id: "aws_sdk_ec2.types.volume_id.VolumeId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        ebs_card_index: Optional["aws_sdk_ec2.types.boxed_integer.BoxedInteger"] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.volume_attachment.VolumeAttachment":
        r"""<p>Attaches an Amazon EBS volume to a <code>running</code> or <code>stopped</code> instance, and exposes it to the instance with the specified device name.</p> <note> <p>The maximum number of Amazon EBS volumes that you can attach to an instance depends on the instance type. If you exceed the volume attachment limit for an instance type, the attachment request fails with the <code>AttachmentLimitExceeded</code> error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/volume_limits.html\">Instance volume limits</a>.</p> </note> <p>After you attach an EBS volume, you must make it available for use. For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/ebs-using-volumes.html\">Make an EBS volume available for use</a>.</p> <p>If a volume has an Amazon Web Services Marketplace product code:</p> <ul> <li> <p>The volume can be attached only to a stopped instance.</p> </li> <li> <p>Amazon Web Services Marketplace product codes are copied from the volume to the instance.</p> </li> <li> <p>You must be subscribed to the product.</p> </li> <li> <p>The instance type and operating system of the instance must support the product. For example, you can't detach a volume from a Windows instance and attach it to a Linux instance.</p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/ebs-attaching-volume.html\">Attach an Amazon EBS volume to an instance</a> in the <i>Amazon EBS User Guide</i>.</p>

        Args:
            device: <p>The device name (for example, <code>/dev/sdh</code> or <code>xvdh</code>).</p>
            instance_id: <p>The ID of the instance.</p>
            volume_id: <p>The ID of the EBS volume. The volume and instance must be within the same Availability Zone.</p>
            ebs_card_index: <p>The index of the EBS card. Some instance types support multiple EBS cards. The default EBS card index is 0.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>

        Examples:
            To attach a volume to an instance
            This example attaches a volume (``vol-1234567890abcdef0``) to an instance (``i-01474ef662b89480``) as ``/dev/sdf``.

            >>> await client.attach_volume(volume_id='vol-1234567890abcdef0', instance_id='i-01474ef662b89480', device='/dev/sdf')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.attach_volume_request.AttachVolumeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.volume_attachment.VolumeAttachment"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.attach_volume

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.attach_volume.async_attach_volume(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.attach_volume_request.AttachVolumeRequest = {}  # type: ignore[typeddict-item]
        input_["device"] = device
        input_["instance_id"] = instance_id
        input_["volume_id"] = volume_id
        if ebs_card_index is not None:
            input_["ebs_card_index"] = ebs_card_index
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def attach_vpn_gateway(
        self,
        vpc_id: "aws_sdk_ec2.types.vpc_id.VpcId",
        vpn_gateway_id: "aws_sdk_ec2.types.vpn_gateway_id.VpnGatewayId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.attach_vpn_gateway_result.AttachVpnGatewayResult":
        r"""<p>Attaches an available virtual private gateway to a VPC. You can attach one virtual private gateway to one VPC at a time.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html\">Amazon Web Services Site-to-Site VPN</a> in the <i>Amazon Web Services Site-to-Site VPN User Guide</i>.</p>

        Args:
            vpc_id: <p>The ID of the VPC.</p>
            vpn_gateway_id: <p>The ID of the virtual private gateway.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.attach_vpn_gateway_request.AttachVpnGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.attach_vpn_gateway_result.AttachVpnGatewayResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.attach_vpn_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.attach_vpn_gateway.async_attach_vpn_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.attach_vpn_gateway_request.AttachVpnGatewayRequest = {}  # type: ignore[typeddict-item]
        input_["vpc_id"] = vpc_id
        input_["vpn_gateway_id"] = vpn_gateway_id
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def authorize_client_vpn_ingress(
        self,
        client_vpn_endpoint_id: "aws_sdk_ec2.types.client_vpn_endpoint_id.ClientVpnEndpointId",
        target_network_cidr: "aws_sdk_ec2.types.string.String",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        access_group_id: Optional["aws_sdk_ec2.types.string.String"] = None,
        authorize_all_groups: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        description: Optional["aws_sdk_ec2.types.string.String"] = None,
        client_token: Optional["aws_sdk_ec2.types.string.String"] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.authorize_client_vpn_ingress_result.AuthorizeClientVpnIngressResult":
        r"""<p>Adds an ingress authorization rule to a Client VPN endpoint. Ingress authorization rules act as firewall rules that grant access to networks. You must configure ingress authorization rules to enable clients to access resources in Amazon Web Services or on-premises networks.</p>

        Args:
            client_vpn_endpoint_id: <p>The ID of the Client VPN endpoint.</p>
            target_network_cidr: <p>The IPv4 address range, in CIDR notation, of the network for which access is being authorized.</p>
            access_group_id: <p>The ID of the group to grant access to, for example, the Active Directory group or identity provider (IdP) group. Required if <code>AuthorizeAllGroups</code> is <code>false</code> or not specified.</p>
            authorize_all_groups: <p>Indicates whether to grant access to all clients. Specify <code>true</code> to grant all clients who successfully establish a VPN connection access to the network. Must be set to <code>true</code> if <code>AccessGroupId</code> is not specified.</p>
            description: <p>A brief description of the authorization rule.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.authorize_client_vpn_ingress_request.AuthorizeClientVpnIngressRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.authorize_client_vpn_ingress_result.AuthorizeClientVpnIngressResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.authorize_client_vpn_ingress

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.authorize_client_vpn_ingress.async_authorize_client_vpn_ingress(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.authorize_client_vpn_ingress_request.AuthorizeClientVpnIngressRequest = {}  # type: ignore[typeddict-item]
        input_["client_vpn_endpoint_id"] = client_vpn_endpoint_id
        input_["target_network_cidr"] = target_network_cidr
        if access_group_id is not None:
            input_["access_group_id"] = access_group_id
        if authorize_all_groups is not None:
            input_["authorize_all_groups"] = authorize_all_groups
        if description is not None:
            input_["description"] = description
        if client_token is not None:
            input_["client_token"] = client_token
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def authorize_security_group_egress(
        self,
        group_id: "aws_sdk_ec2.types.security_group_id.SecurityGroupId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        source_security_group_name: Optional["aws_sdk_ec2.types.string.String"] = None,
        source_security_group_owner_id: Optional[
            "aws_sdk_ec2.types.string.String"
        ] = None,
        ip_protocol: Optional["aws_sdk_ec2.types.string.String"] = None,
        from_port: Optional["aws_sdk_ec2.types.integer.Integer"] = None,
        to_port: Optional["aws_sdk_ec2.types.integer.Integer"] = None,
        cidr_ip: Optional["aws_sdk_ec2.types.string.String"] = None,
        ip_permissions: Optional[
            "aws_sdk_ec2.types.ip_permission_list.IpPermissionList"
        ] = None,
    ) -> "aws_sdk_ec2.types.authorize_security_group_egress_result.AuthorizeSecurityGroupEgressResult":
        r"""<p>Adds the specified outbound (egress) rules to a security group.</p> <p>An outbound rule permits instances to send traffic to the specified IPv4 or IPv6 address ranges, the IP address ranges specified by a prefix list, or the instances that are associated with a source security group. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html\">Security group rules</a>.</p> <p>You must specify exactly one of the following destinations: an IPv4 or IPv6 address range, a prefix list, or a security group. You must specify a protocol for each rule (for example, TCP). If the protocol is TCP or UDP, you must also specify a port or port range. If the protocol is ICMP or ICMPv6, you must also specify the ICMP type and code.</p> <p>Rule changes are propagated to instances associated with the security group as quickly as possible. However, a small delay might occur.</p> <p>For examples of rules that you can add to security groups for specific access scenarios, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html\">Security group rules for different use cases</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>For information about security group quotas, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html\">Amazon VPC quotas</a> in the <i>Amazon VPC User Guide</i>.</p>

        Args:
            tag_specifications: <p>The tags applied to the security group rule.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            group_id: <p>The ID of the security group.</p>
            source_security_group_name: <p>Not supported. Use IP permissions instead.</p>
            source_security_group_owner_id: <p>Not supported. Use IP permissions instead.</p>
            ip_protocol: <p>Not supported. Use IP permissions instead.</p>
            from_port: <p>Not supported. Use IP permissions instead.</p>
            to_port: <p>Not supported. Use IP permissions instead.</p>
            cidr_ip: <p>Not supported. Use IP permissions instead.</p>
            ip_permissions: <p>The permissions for the security group rules.</p>

        Examples:
            To add a rule that allows outbound traffic to a specific address range
            This example adds a rule that grants access to the specified address ranges on TCP port 80.

            >>> await client.authorize_security_group_egress(group_id='sg-1a2b3c4d', ip_permissions=[{'IpProtocol': 'tcp', 'FromPort': 80, 'ToPort': 80, 'IpRanges': [{'CidrIp': '10.0.0.0/16'}]}])
            To add a rule that allows outbound traffic to a specific security group
            This example adds a rule that grants access to the specified security group on TCP port 80.

            >>> await client.authorize_security_group_egress(group_id='sg-1a2b3c4d', ip_permissions=[{'IpProtocol': 'tcp', 'FromPort': 80, 'ToPort': 80, 'UserIdGroupPairs': [{'GroupId': 'sg-4b51a32f'}]}])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.authorize_security_group_egress_request.AuthorizeSecurityGroupEgressRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.authorize_security_group_egress_result.AuthorizeSecurityGroupEgressResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.authorize_security_group_egress

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.authorize_security_group_egress.async_authorize_security_group_egress(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.authorize_security_group_egress_request.AuthorizeSecurityGroupEgressRequest = {}  # type: ignore[typeddict-item]
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications
        if dry_run is not None:
            input_["dry_run"] = dry_run
        input_["group_id"] = group_id
        if source_security_group_name is not None:
            input_["source_security_group_name"] = source_security_group_name
        if source_security_group_owner_id is not None:
            input_["source_security_group_owner_id"] = source_security_group_owner_id
        if ip_protocol is not None:
            input_["ip_protocol"] = ip_protocol
        if from_port is not None:
            input_["from_port"] = from_port
        if to_port is not None:
            input_["to_port"] = to_port
        if cidr_ip is not None:
            input_["cidr_ip"] = cidr_ip
        if ip_permissions is not None:
            input_["ip_permissions"] = ip_permissions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def authorize_security_group_ingress(
        self,
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        cidr_ip: Optional["aws_sdk_ec2.types.string.String"] = None,
        from_port: Optional["aws_sdk_ec2.types.integer.Integer"] = None,
        group_id: Optional[
            "aws_sdk_ec2.types.security_group_id.SecurityGroupId"
        ] = None,
        group_name: Optional[
            "aws_sdk_ec2.types.security_group_name.SecurityGroupName"
        ] = None,
        ip_permissions: Optional[
            "aws_sdk_ec2.types.ip_permission_list.IpPermissionList"
        ] = None,
        ip_protocol: Optional["aws_sdk_ec2.types.string.String"] = None,
        source_security_group_name: Optional["aws_sdk_ec2.types.string.String"] = None,
        source_security_group_owner_id: Optional[
            "aws_sdk_ec2.types.string.String"
        ] = None,
        to_port: Optional["aws_sdk_ec2.types.integer.Integer"] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.authorize_security_group_ingress_result.AuthorizeSecurityGroupIngressResult":
        r"""<p>Adds the specified inbound (ingress) rules to a security group.</p> <p>An inbound rule permits instances to receive traffic from the specified IPv4 or IPv6 address range, the IP address ranges that are specified by a prefix list, or the instances that are associated with a destination security group. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html\">Security group rules</a>.</p> <p>You must specify exactly one of the following sources: an IPv4 or IPv6 address range, a prefix list, or a security group. You must specify a protocol for each rule (for example, TCP). If the protocol is TCP or UDP, you must also specify a port or port range. If the protocol is ICMP or ICMPv6, you must also specify the ICMP/ICMPv6 type and code.</p> <p>Rule changes are propagated to instances associated with the security group as quickly as possible. However, a small delay might occur.</p> <p>For examples of rules that you can add to security groups for specific access scenarios, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html\">Security group rules for different use cases</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>For more information about security group quotas, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html\">Amazon VPC quotas</a> in the <i>Amazon VPC User Guide</i>.</p>

        Args:
            cidr_ip: <p>The IPv4 address range, in CIDR format.</p> <note> <p> Amazon Web Services <a href=\"https://en.wikipedia.org/wiki/Canonicalization\">canonicalizes</a> IPv4 and IPv6 CIDRs. For example, if you specify 100.68.0.18/18 for the CIDR block, Amazon Web Services canonicalizes the CIDR block to 100.68.0.0/18. Any subsequent DescribeSecurityGroups and DescribeSecurityGroupRules calls will return the canonicalized form of the CIDR block. Additionally, if you attempt to add another rule with the non-canonical form of the CIDR (such as 100.68.0.18/18) and there is already a rule for the canonicalized form of the CIDR block (such as 100.68.0.0/18), the API throws an duplicate rule error.</p> </note> <p>To specify an IPv6 address range, use IP permissions instead.</p> <p>To specify multiple rules and descriptions for the rules, use IP permissions instead.</p>
            from_port: <p>If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP, this is the ICMP type or -1 (all ICMP types).</p> <p>To specify multiple rules and descriptions for the rules, use IP permissions instead.</p>
            group_id: <p>The ID of the security group.</p>
            group_name: <p>[Default VPC] The name of the security group. For security groups for a default VPC you can specify either the ID or the name of the security group. For security groups for a nondefault VPC, you must specify the ID of the security group.</p>
            ip_permissions: <p>The permissions for the security group rules.</p>
            ip_protocol: <p>The IP protocol name (<code>tcp</code>, <code>udp</code>, <code>icmp</code>) or number (see <a href=\"http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml\">Protocol Numbers</a>). To specify all protocols, use <code>-1</code>.</p> <p>To specify <code>icmpv6</code>, use IP permissions instead.</p> <p>If you specify a protocol other than one of the supported values, traffic is allowed on all ports, regardless of any ports that you specify.</p> <p>To specify multiple rules and descriptions for the rules, use IP permissions instead.</p>
            source_security_group_name: <p>[Default VPC] The name of the source security group.</p> <p>The rule grants full ICMP, UDP, and TCP access. To create a rule with a specific protocol and port range, specify a set of IP permissions instead.</p>
            source_security_group_owner_id: <p>The Amazon Web Services account ID for the source security group, if the source security group is in a different account.</p> <p>The rule grants full ICMP, UDP, and TCP access. To create a rule with a specific protocol and port range, use IP permissions instead.</p>
            to_port: <p>If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP, this is the ICMP code or -1 (all ICMP codes). If the start port is -1 (all ICMP types), then the end port must be -1 (all ICMP codes).</p> <p>To specify multiple rules and descriptions for the rules, use IP permissions instead.</p>
            tag_specifications: <p>The tags applied to the security group rule.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>

        Examples:
            To add a rule that allows inbound HTTP traffic from another security group
            This example enables inbound traffic on TCP port 80 from the specified security group. The group must be in the same VPC or a peer VPC. Incoming traffic is allowed based on the private IP addresses of instances that are associated with the specified security group.

            >>> await client.authorize_security_group_ingress(group_id='sg-111aaa22', ip_permissions=[{'IpProtocol': 'tcp', 'FromPort': 80, 'ToPort': 80, 'UserIdGroupPairs': [{'GroupId': 'sg-1a2b3c4d', 'Description': 'HTTP access from other instances'}]}])
            To add a rule that allows inbound SSH traffic from an IPv4 address range
            This example enables inbound traffic on TCP port 22 (SSH). The rule includes a description to help you identify it later.

            >>> await client.authorize_security_group_ingress(group_id='sg-903004f8', ip_permissions=[{'IpProtocol': 'tcp', 'FromPort': 22, 'ToPort': 22, 'IpRanges': [{'CidrIp': '203.0.113.0/24', 'Description': 'SSH access from the LA office'}]}])
            To add a rule that allows inbound RDP traffic from an IPv6 address range
            This example adds an inbound rule that allows RDP traffic from the specified IPv6 address range. The rule includes a description to help you identify it later.

            >>> await client.authorize_security_group_ingress(group_id='sg-123abc12 ', ip_permissions=[{'IpProtocol': 'tcp', 'FromPort': 3389, 'ToPort': 3389, 'Ipv6Ranges': [{'CidrIpv6': '2001:db8:1234:1a00::/64', 'Description': 'RDP access from the NY office'}]}])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.authorize_security_group_ingress_request.AuthorizeSecurityGroupIngressRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.authorize_security_group_ingress_result.AuthorizeSecurityGroupIngressResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.authorize_security_group_ingress

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.authorize_security_group_ingress.async_authorize_security_group_ingress(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.authorize_security_group_ingress_request.AuthorizeSecurityGroupIngressRequest = {}  # type: ignore[typeddict-item]
        if cidr_ip is not None:
            input_["cidr_ip"] = cidr_ip
        if from_port is not None:
            input_["from_port"] = from_port
        if group_id is not None:
            input_["group_id"] = group_id
        if group_name is not None:
            input_["group_name"] = group_name
        if ip_permissions is not None:
            input_["ip_permissions"] = ip_permissions
        if ip_protocol is not None:
            input_["ip_protocol"] = ip_protocol
        if source_security_group_name is not None:
            input_["source_security_group_name"] = source_security_group_name
        if source_security_group_owner_id is not None:
            input_["source_security_group_owner_id"] = source_security_group_owner_id
        if to_port is not None:
            input_["to_port"] = to_port
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def bundle_instance(
        self,
        instance_id: "aws_sdk_ec2.types.instance_id.InstanceId",
        storage: "aws_sdk_ec2.types.storage.Storage",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.bundle_instance_result.BundleInstanceResult":
        r"""<p>Bundles an Amazon instance store-backed Windows instance.</p> <p>During bundling, only the root device volume (C:\) is bundled. Data on other instance store volumes is not preserved.</p> <note> <p>This action is no longer supported. To create an AMI, use <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateImage.html\">CreateImage</a>. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html\"> Create an Amazon EBS-backed AMI</a> in the <i>Amazon EC2 User Guide</i>.</p> </note>

        Args:
            instance_id: <p>The ID of the instance to bundle.</p> <p>Default: None</p>
            storage: <p>The bucket in which to store the AMI. You can specify a bucket that you already own or a new bucket that Amazon EC2 creates on your behalf. If you specify a bucket that belongs to someone else, Amazon EC2 returns an error.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.bundle_instance_request.BundleInstanceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.bundle_instance_result.BundleInstanceResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.bundle_instance

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.bundle_instance.async_bundle_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.bundle_instance_request.BundleInstanceRequest = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["storage"] = storage
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_bundle_task(
        self,
        bundle_id: "aws_sdk_ec2.types.bundle_id.BundleId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.cancel_bundle_task_result.CancelBundleTaskResult":
        """<p>Cancels a bundling operation for an instance store-backed Windows instance.</p>

        Args:
            bundle_id: <p>The ID of the bundle task.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.cancel_bundle_task_request.CancelBundleTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.cancel_bundle_task_result.CancelBundleTaskResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.cancel_bundle_task

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.cancel_bundle_task.async_cancel_bundle_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.cancel_bundle_task_request.CancelBundleTaskRequest = {}  # type: ignore[typeddict-item]
        input_["bundle_id"] = bundle_id
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_capacity_reservation(
        self,
        capacity_reservation_id: "aws_sdk_ec2.types.capacity_reservation_id.CapacityReservationId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.cancel_capacity_reservation_result.CancelCapacityReservationResult":
        r"""<p>Cancels the specified Capacity Reservation, releases the reserved capacity, and changes the Capacity Reservation's state to <code>cancelled</code>.</p> <p>You can cancel a Capacity Reservation that is in the following states:</p> <ul> <li> <p> <code>assessing</code> </p> </li> <li> <p> <code>active</code> and there is no commitment duration or the commitment duration has elapsed. You can't cancel a future-dated Capacity Reservation during the commitment duration.</p> </li> </ul> <note> <p>You can't modify or cancel a Capacity Block. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-blocks.html\">Capacity Blocks for ML</a>.</p> </note> <p>If a future-dated Capacity Reservation enters the <code>delayed</code> state, the commitment duration is waived, and you can cancel it as soon as it enters the <code>active</code> state.</p> <p>Instances running in the reserved capacity continue running until you stop them. Stopped instances that target the Capacity Reservation can no longer launch. Modify these instances to either target a different Capacity Reservation, launch On-Demand Instance capacity, or run in any open Capacity Reservation that has matching attributes and sufficient capacity.</p>

        Args:
            capacity_reservation_id: <p>The ID of the Capacity Reservation to be cancelled.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.cancel_capacity_reservation_request.CancelCapacityReservationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.cancel_capacity_reservation_result.CancelCapacityReservationResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.cancel_capacity_reservation

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.cancel_capacity_reservation.async_cancel_capacity_reservation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.cancel_capacity_reservation_request.CancelCapacityReservationRequest = {}  # type: ignore[typeddict-item]
        input_["capacity_reservation_id"] = capacity_reservation_id
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_capacity_reservation_fleets(
        self,
        capacity_reservation_fleet_ids: "aws_sdk_ec2.types.capacity_reservation_fleet_id_set.CapacityReservationFleetIdSet",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.cancel_capacity_reservation_fleets_result.CancelCapacityReservationFleetsResult":
        """<p>Cancels one or more Capacity Reservation Fleets. When you cancel a Capacity Reservation Fleet, the following happens:</p> <ul> <li> <p>The Capacity Reservation Fleet's status changes to <code>cancelled</code>.</p> </li> <li> <p>The individual Capacity Reservations in the Fleet are cancelled. Instances running in the Capacity Reservations at the time of cancelling the Fleet continue to run in shared capacity.</p> </li> <li> <p>The Fleet stops creating new Capacity Reservations.</p> </li> </ul>

        Args:
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            capacity_reservation_fleet_ids: <p>The IDs of the Capacity Reservation Fleets to cancel.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.cancel_capacity_reservation_fleets_request.CancelCapacityReservationFleetsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.cancel_capacity_reservation_fleets_result.CancelCapacityReservationFleetsResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.cancel_capacity_reservation_fleets

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.cancel_capacity_reservation_fleets.async_cancel_capacity_reservation_fleets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.cancel_capacity_reservation_fleets_request.CancelCapacityReservationFleetsRequest = {}  # type: ignore[typeddict-item]
        if dry_run is not None:
            input_["dry_run"] = dry_run
        input_["capacity_reservation_fleet_ids"] = capacity_reservation_fleet_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_conversion_task(
        self,
        conversion_task_id: "aws_sdk_ec2.types.conversion_task_id.ConversionTaskId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        reason_message: Optional["aws_sdk_ec2.types.string.String"] = None,
    ) -> None:
        """<p>Cancels an active conversion task. The task can be the import of an instance or volume. The action removes all artifacts of the conversion, including a partially uploaded volume or instance. If the conversion is complete or is in the process of transferring the final disk image, the command fails and returns an exception.</p>

        Args:
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            conversion_task_id: <p>The ID of the conversion task.</p>
            reason_message: <p>The reason for canceling the conversion task.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.cancel_conversion_request.CancelConversionRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_ec2._operations.amazon_ec2.cancel_conversion_task

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.cancel_conversion_task.async_cancel_conversion_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.cancel_conversion_request.CancelConversionRequest = {}  # type: ignore[typeddict-item]
        if dry_run is not None:
            input_["dry_run"] = dry_run
        input_["conversion_task_id"] = conversion_task_id
        if reason_message is not None:
            input_["reason_message"] = reason_message

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_declarative_policies_report(
        self,
        report_id: "aws_sdk_ec2.types.declarative_policies_report_id.DeclarativePoliciesReportId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.cancel_declarative_policies_report_result.CancelDeclarativePoliciesReportResult":
        r"""<p>Cancels the generation of an account status report.</p> <p>You can only cancel a report while it has the <code>running</code> status. Reports with other statuses (<code>complete</code>, <code>cancelled</code>, or <code>error</code>) can't be canceled.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative_status-report.html\">Generating the account status report for declarative policies</a> in the <i>Amazon Web Services Organizations User Guide</i>.</p>

        Args:
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            report_id: <p>The ID of the report.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.cancel_declarative_policies_report_request.CancelDeclarativePoliciesReportRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.cancel_declarative_policies_report_result.CancelDeclarativePoliciesReportResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.cancel_declarative_policies_report

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.cancel_declarative_policies_report.async_cancel_declarative_policies_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.cancel_declarative_policies_report_request.CancelDeclarativePoliciesReportRequest = {}  # type: ignore[typeddict-item]
        if dry_run is not None:
            input_["dry_run"] = dry_run
        input_["report_id"] = report_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_export_task(
        self,
        export_task_id: "aws_sdk_ec2.types.export_vm_task_id.ExportVmTaskId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
    ) -> None:
        """<p>Cancels an active export task. The request removes all artifacts of the export, including any partially-created Amazon S3 objects. If the export task is complete or is in the process of transferring the final disk image, the command fails and returns an error.</p>

        Args:
            export_task_id: <p>The ID of the export task. This is the ID returned by the <code>CreateInstanceExportTask</code> and <code>ExportImage</code> operations.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.cancel_export_task_request.CancelExportTaskRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_ec2._operations.amazon_ec2.cancel_export_task

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.cancel_export_task.async_cancel_export_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.cancel_export_task_request.CancelExportTaskRequest = {}  # type: ignore[typeddict-item]
        input_["export_task_id"] = export_task_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_image_launch_permission(
        self,
        image_id: "aws_sdk_ec2.types.image_id.ImageId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.cancel_image_launch_permission_result.CancelImageLaunchPermissionResult":
        r"""<p>Removes your Amazon Web Services account from the launch permissions for the specified AMI. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cancel-sharing-an-AMI.html\">Cancel having an AMI shared with your Amazon Web Services account</a> in the <i>Amazon EC2 User Guide</i>.</p>

        Args:
            image_id: <p>The ID of the AMI that was shared with your Amazon Web Services account.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.cancel_image_launch_permission_request.CancelImageLaunchPermissionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.cancel_image_launch_permission_result.CancelImageLaunchPermissionResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.cancel_image_launch_permission

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.cancel_image_launch_permission.async_cancel_image_launch_permission(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.cancel_image_launch_permission_request.CancelImageLaunchPermissionRequest = {}  # type: ignore[typeddict-item]
        input_["image_id"] = image_id
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_import_task(
        self,
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        cancel_reason: Optional["aws_sdk_ec2.types.string.String"] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        import_task_id: Optional[
            "aws_sdk_ec2.types.import_task_id.ImportTaskId"
        ] = None,
    ) -> "aws_sdk_ec2.types.cancel_import_task_result.CancelImportTaskResult":
        """<p>Cancels an in-process import virtual machine or import snapshot task.</p>

        Args:
            cancel_reason: <p>The reason for canceling the task.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            import_task_id: <p>The ID of the import image or import snapshot task to be canceled.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.cancel_import_task_request.CancelImportTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.cancel_import_task_result.CancelImportTaskResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.cancel_import_task

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.cancel_import_task.async_cancel_import_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.cancel_import_task_request.CancelImportTaskRequest = {}  # type: ignore[typeddict-item]
        if cancel_reason is not None:
            input_["cancel_reason"] = cancel_reason
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if import_task_id is not None:
            input_["import_task_id"] = import_task_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_reserved_instances_listing(
        self,
        reserved_instances_listing_id: "aws_sdk_ec2.types.reserved_instances_listing_id.ReservedInstancesListingId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
    ) -> "aws_sdk_ec2.types.cancel_reserved_instances_listing_result.CancelReservedInstancesListingResult":
        r"""<p>Cancels the specified Reserved Instance listing in the Reserved Instance Marketplace.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-market-general.html\">Sell in the Reserved Instance Marketplace</a> in the <i>Amazon EC2 User Guide</i>.</p>

        Args:
            reserved_instances_listing_id: <p>The ID of the Reserved Instance listing.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.cancel_reserved_instances_listing_request.CancelReservedInstancesListingRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.cancel_reserved_instances_listing_result.CancelReservedInstancesListingResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.cancel_reserved_instances_listing

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.cancel_reserved_instances_listing.async_cancel_reserved_instances_listing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.cancel_reserved_instances_listing_request.CancelReservedInstancesListingRequest = {}  # type: ignore[typeddict-item]
        input_["reserved_instances_listing_id"] = reserved_instances_listing_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_spot_fleet_requests(
        self,
        spot_fleet_request_ids: "aws_sdk_ec2.types.spot_fleet_request_id_list.SpotFleetRequestIdList",
        terminate_instances: "aws_sdk_ec2.types.boolean.Boolean",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.cancel_spot_fleet_requests_response.CancelSpotFleetRequestsResponse":
        r"""<p>Cancels the specified Spot Fleet requests.</p> <p>After you cancel a Spot Fleet request, the Spot Fleet launches no new instances.</p> <p>You must also specify whether a canceled Spot Fleet request should terminate its instances. If you choose to terminate the instances, the Spot Fleet request enters the <code>cancelled_terminating</code> state. Otherwise, the Spot Fleet request enters the <code>cancelled_running</code> state and the instances continue to run until they are interrupted or you terminate them manually.</p> <important> <p> <b>Terminating an instance is permanent and irreversible.</b> </p> <p>After you terminate an instance, you can no longer connect to it, and it can't be recovered. All attached Amazon EBS volumes that are configured to be deleted on termination are also permanently deleted and can't be recovered. All data stored on instance store volumes is permanently lost. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-ec2-instance-termination-works.html\"> How instance termination works</a>.</p> <p>Before you terminate an instance, ensure that you have backed up all data that you need to retain after the termination to persistent storage.</p> </important> <p class=\"title\"> <b>Restrictions</b> </p> <ul> <li> <p>You can delete up to 100 fleets in a single request. If you exceed the specified number, no fleets are deleted.</p> </li> </ul>

        Args:
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            spot_fleet_request_ids: <p>The IDs of the Spot Fleet requests.</p> <p>Constraint: You can specify up to 100 IDs in a single request.</p>
            terminate_instances: <p>Indicates whether to terminate the associated instances when the Spot Fleet request is canceled. The default is to terminate the instances.</p> <p>To let the instances continue to run after the Spot Fleet request is canceled, specify <code>no-terminate-instances</code>.</p>

        Examples:
            To cancel a Spot fleet request
            This example cancels the specified Spot fleet request and terminates its associated Spot Instances.

            >>> await client.cancel_spot_fleet_requests(spot_fleet_request_ids=['sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE'], terminate_instances=True)
            To cancel a Spot fleet request without terminating its Spot Instances
            This example cancels the specified Spot fleet request without terminating its associated Spot Instances.

            >>> await client.cancel_spot_fleet_requests(spot_fleet_request_ids=['sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE'], terminate_instances=False)
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.cancel_spot_fleet_requests_request.CancelSpotFleetRequestsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.cancel_spot_fleet_requests_response.CancelSpotFleetRequestsResponse"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.cancel_spot_fleet_requests

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.cancel_spot_fleet_requests.async_cancel_spot_fleet_requests(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.cancel_spot_fleet_requests_request.CancelSpotFleetRequestsRequest = {}  # type: ignore[typeddict-item]
        if dry_run is not None:
            input_["dry_run"] = dry_run
        input_["spot_fleet_request_ids"] = spot_fleet_request_ids
        input_["terminate_instances"] = terminate_instances

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_spot_instance_requests(
        self,
        spot_instance_request_ids: "aws_sdk_ec2.types.spot_instance_request_id_list.SpotInstanceRequestIdList",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.cancel_spot_instance_requests_result.CancelSpotInstanceRequestsResult":
        """<p>Cancels one or more Spot Instance requests.</p> <important> <p>Canceling a Spot Instance request does not terminate running Spot Instances associated with the request.</p> </important>

        Args:
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            spot_instance_request_ids: <p>The IDs of the Spot Instance requests.</p>

        Examples:
            To cancel Spot Instance requests
            This example cancels a Spot Instance request.

            >>> await client.cancel_spot_instance_requests(spot_instance_request_ids=['sir-08b93456'])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.cancel_spot_instance_requests_request.CancelSpotInstanceRequestsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.cancel_spot_instance_requests_result.CancelSpotInstanceRequestsResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.cancel_spot_instance_requests

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.cancel_spot_instance_requests.async_cancel_spot_instance_requests(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.cancel_spot_instance_requests_request.CancelSpotInstanceRequestsRequest = {}  # type: ignore[typeddict-item]
        if dry_run is not None:
            input_["dry_run"] = dry_run
        input_["spot_instance_request_ids"] = spot_instance_request_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def confirm_product_instance(
        self,
        instance_id: "aws_sdk_ec2.types.instance_id.InstanceId",
        product_code: "aws_sdk_ec2.types.string.String",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> (
        "aws_sdk_ec2.types.confirm_product_instance_result.ConfirmProductInstanceResult"
    ):
        """<p>Determines whether a product code is associated with an instance. This action can only be used by the owner of the product code. It is useful when a product code owner must verify whether another user's instance is eligible for support.</p>

        Args:
            instance_id: <p>The ID of the instance.</p>
            product_code: <p>The product code. This must be a product code that you own.</p>
            dry_run: <p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>

        Examples:
            To confirm the product instance
            This example determines whether the specified product code is associated with the specified instance.

            >>> await client.confirm_product_instance(product_code='774F4FF8', instance_id='i-1234567890abcdef0')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.confirm_product_instance_request.ConfirmProductInstanceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.confirm_product_instance_result.ConfirmProductInstanceResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.confirm_product_instance

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.confirm_product_instance.async_confirm_product_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.confirm_product_instance_request.ConfirmProductInstanceRequest = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["product_code"] = product_code
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def copy_fpga_image(
        self,
        source_fpga_image_id: "aws_sdk_ec2.types.string.String",
        source_region: "aws_sdk_ec2.types.string.String",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        description: Optional["aws_sdk_ec2.types.string.String"] = None,
        name: Optional["aws_sdk_ec2.types.string.String"] = None,
        client_token: Optional["aws_sdk_ec2.types.string.String"] = None,
    ) -> "aws_sdk_ec2.types.copy_fpga_image_result.CopyFpgaImageResult":
        r"""<p>Copies the specified Amazon FPGA Image (AFI) to the current Region.</p>

        Args:
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            source_fpga_image_id: <p>The ID of the source AFI.</p>
            description: <p>The description for the new AFI.</p>
            name: <p>The name for the new AFI. The default is the name of the source AFI.</p>
            source_region: <p>The Region that contains the source AFI.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.copy_fpga_image_request.CopyFpgaImageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.copy_fpga_image_result.CopyFpgaImageResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.copy_fpga_image

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.copy_fpga_image.async_copy_fpga_image(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.copy_fpga_image_request.CopyFpgaImageRequest = {}  # type: ignore[typeddict-item]
        if dry_run is not None:
            input_["dry_run"] = dry_run
        input_["source_fpga_image_id"] = source_fpga_image_id
        if description is not None:
            input_["description"] = description
        if name is not None:
            input_["name"] = name
        input_["source_region"] = source_region
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def copy_image(
        self,
        name: "aws_sdk_ec2.types.image_name_request.ImageNameRequest",
        source_image_id: "aws_sdk_ec2.types.string.String",
        source_region: "aws_sdk_ec2.types.string.String",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        client_token: Optional[
            "aws_sdk_ec2.types.copy_image_client_token.CopyImageClientToken"
        ] = None,
        description: Optional[
            "aws_sdk_ec2.types.image_description_request.ImageDescriptionRequest"
        ] = None,
        encrypted: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        kms_key_id: Optional["aws_sdk_ec2.types.kms_key_id.KmsKeyId"] = None,
        destination_outpost_arn: Optional["aws_sdk_ec2.types.string.String"] = None,
        copy_image_tags: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
        snapshot_copy_completion_duration_minutes: Optional[
            "aws_sdk_ec2.types.long.Long"
        ] = None,
        destination_availability_zone: Optional[
            "aws_sdk_ec2.types.string.String"
        ] = None,
        destination_availability_zone_id: Optional[
            "aws_sdk_ec2.types.string.String"
        ] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.copy_image_result.CopyImageResult":
        r"""<p>Initiates an AMI copy operation. You must specify the source AMI ID and both the source and destination locations. The copy operation must be initiated in the destination Region.</p> <p class=\"title\"> <b>CopyImage supports the following source to destination copies:</b> </p> <ul> <li> <p>Region to Region</p> </li> <li> <p>Region to Outpost</p> </li> <li> <p>Parent Region to Local Zone</p> </li> <li> <p>Local Zone to parent Region</p> </li> <li> <p>Between Local Zones with the same parent Region (only supported for certain Local Zones)</p> </li> </ul> <p class=\"title\"> <b>CopyImage does not support the following source to destination copies:</b> </p> <ul> <li> <p>Local Zone to non-parent Regions</p> </li> <li> <p>Between Local Zones with different parent Regions</p> </li> <li> <p>Local Zone to Outpost</p> </li> <li> <p>Outpost to Local Zone</p> </li> <li> <p>Outpost to Region</p> </li> <li> <p>Between Outposts</p> </li> <li> <p>Within same Outpost</p> </li> <li> <p>Cross-partition copies (use <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateStoreImageTask.html\">CreateStoreImageTask</a> instead)</p> </li> </ul> <p class=\"title\"> <b>Destination specification</b> </p> <ul> <li> <p>Region to Region: The destination Region is the Region in which you initiate the copy operation.</p> </li> <li> <p>Region to Outpost: Specify the destination using the <code>DestinationOutpostArn</code> parameter (the ARN of the Outpost)</p> </li> <li> <p>Region to Local Zone, and Local Zone to Local Zone copies: Specify the destination using the <code>DestinationAvailabilityZone</code> parameter (the name of the destination Local Zone) or <code>DestinationAvailabilityZoneId</code> parameter (the ID of the destination Local Zone).</p> </li> </ul> <p class=\"title\"> <b>Snapshot encryption</b> </p> <ul> <li> <p>Region to Outpost: Backing snapshots copied to an Outpost are encrypted by default using the default encryption key for the Region or the key that you specify. Outposts do not support unencrypted snapshots.</p> </li> <li> <p>Region to Local Zone, and Local Zone to Local Zone: Not all Local Zones require encrypted snapshots. In Local Zones that require encrypted snapshots, backing snapshots are automatically encrypted during copy. In Local Zones where encryption is not required, snapshots retain their original encryption state (encrypted or unencrypted) by default.</p> </li> </ul> <p>For more information, including the required permissions for copying an AMI, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/CopyingAMIs.html\">Copy an Amazon EC2 AMI</a> in the <i>Amazon EC2 User Guide</i>.</p>

        Args:
            client_token: <p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency in Amazon EC2 API requests</a> in the <i>Amazon EC2 API Reference</i>.</p>
            description: <p>A description for the new AMI.</p>
            encrypted: <p>Specifies whether to encrypt the snapshots of the copied image.</p> <p>You can encrypt a copy of an unencrypted snapshot, but you cannot create an unencrypted copy of an encrypted snapshot. The default KMS key for Amazon EBS is used unless you specify a non-default Key Management Service (KMS) KMS key using <code>KmsKeyId</code>. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html\">Use encryption with EBS-backed AMIs</a> in the <i>Amazon EC2 User Guide</i>.</p>
            kms_key_id: <p>The identifier of the symmetric Key Management Service (KMS) KMS key to use when creating encrypted volumes. If this parameter is not specified, your Amazon Web Services managed KMS key for Amazon EBS is used. If you specify a KMS key, you must also set the encrypted state to <code>true</code>.</p> <p>You can specify a KMS key using any of the following:</p> <ul> <li> <p>Key ID. For example, 1234abcd-12ab-34cd-56ef-1234567890ab.</p> </li> <li> <p>Key alias. For example, alias/ExampleAlias.</p> </li> <li> <p>Key ARN. For example, arn:aws:kms:us-east-1:012345678910:key/1234abcd-12ab-34cd-56ef-1234567890ab.</p> </li> <li> <p>Alias ARN. For example, arn:aws:kms:us-east-1:012345678910:alias/ExampleAlias.</p> </li> </ul> <p>Amazon Web Services authenticates the KMS key asynchronously. Therefore, if you specify an identifier that is not valid, the action can appear to complete, but eventually fails.</p> <p>The specified KMS key must exist in the destination Region.</p> <p>Amazon EBS does not support asymmetric KMS keys.</p>
            name: <p>The name of the new AMI.</p>
            source_image_id: <p>The ID of the AMI to copy.</p>
            source_region: <p>The name of the Region that contains the AMI to copy.</p>
            destination_outpost_arn: <p>The Amazon Resource Name (ARN) of the Outpost for the new AMI.</p> <p>Only specify this parameter when copying an AMI from an Amazon Web Services Region to an Outpost. The AMI must be in the Region of the destination Outpost. You can't copy an AMI from an Outpost to a Region, from one Outpost to another, or within the same Outpost.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/snapshots-outposts.html#copy-amis\">Copy AMIs from an Amazon Web Services Region to an Outpost</a> in the <i>Amazon EBS User Guide</i>.</p> <p>Only one of <code>DestinationAvailabilityZone</code>, <code>DestinationAvailabilityZoneId</code>, or <code>DestinationOutpostArn</code> can be specified.</p>
            copy_image_tags: <p>Specifies whether to copy your user-defined AMI tags to the new AMI.</p> <p>The following tags are not be copied:</p> <ul> <li> <p>System tags (prefixed with <code>aws:</code>)</p> </li> <li> <p>For public and shared AMIs, user-defined tags that are attached by other Amazon Web Services accounts</p> </li> </ul> <p>Default: Your user-defined AMI tags are not copied.</p>
            tag_specifications: <p>The tags to apply to the new AMI and new snapshots. You can tag the AMI, the snapshots, or both.</p> <ul> <li> <p>To tag the new AMI, the value for <code>ResourceType</code> must be <code>image</code>.</p> </li> <li> <p>To tag the new snapshots, the value for <code>ResourceType</code> must be <code>snapshot</code>. The same tag is applied to all the new snapshots.</p> </li> </ul> <p>If you specify other values for <code>ResourceType</code>, the request fails.</p> <p>To tag an AMI or snapshot after it has been created, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html\">CreateTags</a>.</p>
            snapshot_copy_completion_duration_minutes: <p>Specify a completion duration, in 15 minute increments, to initiate a time-based AMI copy. The specified completion duration applies to each of the snapshots associated with the AMI. Each snapshot associated with the AMI will be completed within the specified completion duration, with copy throughput automatically adjusted for each snapshot based on its size to meet the timing target.</p> <p>If you do not specify a value, the AMI copy operation is completed on a best-effort basis.</p> <note> <p>This parameter is not supported when copying an AMI to or from a Local Zone, or to an Outpost.</p> </note> <p>For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/time-based-copies.html\">Time-based copies for Amazon EBS snapshots and EBS-backed AMIs</a>.</p>
            destination_availability_zone: <p>The Local Zone for the new AMI (for example, <code>cn-north-1-pkx-1a</code>).</p> <p>Only one of <code>DestinationAvailabilityZone</code>, <code>DestinationAvailabilityZoneId</code>, or <code>DestinationOutpostArn</code> can be specified.</p>
            destination_availability_zone_id: <p>The ID of the Local Zone for the new AMI (for example, <code>cnn1-pkx1-az1</code>).</p> <p>Only one of <code>DestinationAvailabilityZone</code>, <code>DestinationAvailabilityZoneId</code>, or <code>DestinationOutpostArn</code> can be specified.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>

        Examples:
            To copy an AMI to another region
            This example copies the specified AMI from the us-east-1 region to the current region.

            >>> await client.copy_image(description='', name='My server', source_image_id='ami-5731123e', source_region='us-east-1')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.copy_image_request.CopyImageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.copy_image_result.CopyImageResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.copy_image

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.copy_image.async_copy_image(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.copy_image_request.CopyImageRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if encrypted is not None:
            input_["encrypted"] = encrypted
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        input_["name"] = name
        input_["source_image_id"] = source_image_id
        input_["source_region"] = source_region
        if destination_outpost_arn is not None:
            input_["destination_outpost_arn"] = destination_outpost_arn
        if copy_image_tags is not None:
            input_["copy_image_tags"] = copy_image_tags
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications
        if snapshot_copy_completion_duration_minutes is not None:
            input_["snapshot_copy_completion_duration_minutes"] = (
                snapshot_copy_completion_duration_minutes
            )
        if destination_availability_zone is not None:
            input_["destination_availability_zone"] = destination_availability_zone
        if destination_availability_zone_id is not None:
            input_["destination_availability_zone_id"] = (
                destination_availability_zone_id
            )
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def copy_snapshot(
        self,
        source_region: "aws_sdk_ec2.types.string.String",
        source_snapshot_id: "aws_sdk_ec2.types.string.String",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        description: Optional["aws_sdk_ec2.types.string.String"] = None,
        destination_outpost_arn: Optional["aws_sdk_ec2.types.string.String"] = None,
        destination_region: Optional["aws_sdk_ec2.types.string.String"] = None,
        encrypted: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        kms_key_id: Optional["aws_sdk_ec2.types.kms_key_id.KmsKeyId"] = None,
        presigned_url: Optional[
            "aws_sdk_ec2.types.copy_snapshot_request_psu.CopySnapshotRequestPSU"
        ] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
        completion_duration_minutes: Optional[
            "aws_sdk_ec2.types.snapshot_completion_duration_minutes_request.SnapshotCompletionDurationMinutesRequest"
        ] = None,
        destination_availability_zone: Optional[
            "aws_sdk_ec2.types.string.String"
        ] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.copy_snapshot_result.CopySnapshotResult":
        r"""<p>Creates an exact copy of an Amazon EBS snapshot.</p> <p>The location of the source snapshot determines whether you can copy it or not, and the allowed destinations for the snapshot copy.</p> <ul> <li> <p>If the source snapshot is in a Region, you can copy it within that Region, to another Region, to an Outpost associated with that Region, or to a Local Zone in that Region.</p> </li> <li> <p>If the source snapshot is in a Local Zone, you can copy it within that Local Zone, to another Local Zone in the same zone group, or to the parent Region of the Local Zone.</p> </li> <li> <p>If the source snapshot is on an Outpost, you can't copy it.</p> </li> </ul> <p>When copying snapshots to a Region, the encryption outcome for the snapshot copy depends on the Amazon EBS encryption by default setting for the destination Region, the encryption status of the source snapshot, and the encryption parameters you specify in the request. For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/ebs-copy-snapshot.html#creating-encrypted-snapshots\"> Encryption and snapshot copying</a>.</p> <p>Snapshots copied to an Outpost must be encrypted. Unencrypted snapshots are not supported on Outposts. For more information, <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/snapshots-outposts.html#considerations\"> Amazon EBS local snapshots on Outposts</a>.</p> <note> <p>Snapshots copies have an arbitrary source volume ID. Do not use this volume ID for any purpose.</p> </note> <p>For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/ebs-copy-snapshot.html\">Copy an Amazon EBS snapshot</a> in the <i>Amazon EBS User Guide</i>.</p>

        Args:
            description: <p>A description for the EBS snapshot.</p>
            destination_outpost_arn: <p>The Amazon Resource Name (ARN) of the Outpost to which to copy the snapshot.</p> <note> <p>Only supported when copying a snapshot to an Outpost.</p> </note> <p>For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/snapshots-outposts.html#copy-snapshots\"> Copy snapshots from an Amazon Web Services Region to an Outpost</a> in the <i>Amazon EBS User Guide</i>.</p>
            destination_region: <p>The destination Region to use in the <code>PresignedUrl</code> parameter of a snapshot copy operation. This parameter is only valid for specifying the destination Region in a <code>PresignedUrl</code> parameter, where it is required.</p> <p>The snapshot copy is sent to the regional endpoint that you sent the HTTP request to (for example, <code>ec2.us-east-1.amazonaws.com</code>). With the CLI, this is specified using the <code>--region</code> parameter or the default Region in your Amazon Web Services configuration file.</p>
            encrypted: <p>To encrypt a copy of an unencrypted snapshot if encryption by default is not enabled, enable encryption using this parameter. Otherwise, omit this parameter. Copies of encrypted snapshots are encrypted, even if you omit this parameter and encryption by default is not enabled. You cannot set this parameter to false. For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html\">Amazon EBS encryption</a> in the <i>Amazon EBS User Guide</i>.</p>
            kms_key_id: <p>The identifier of the KMS key to use for Amazon EBS encryption. If this parameter is not specified, your KMS key for Amazon EBS is used. If <code>KmsKeyId</code> is specified, the encrypted state must be <code>true</code>.</p> <p>You can specify the KMS key using any of the following:</p> <ul> <li> <p>Key ID. For example, 1234abcd-12ab-34cd-56ef-1234567890ab.</p> </li> <li> <p>Key alias. For example, alias/ExampleAlias.</p> </li> <li> <p>Key ARN. For example, arn:aws:kms:us-east-1:012345678910:key/1234abcd-12ab-34cd-56ef-1234567890ab.</p> </li> <li> <p>Alias ARN. For example, arn:aws:kms:us-east-1:012345678910:alias/ExampleAlias.</p> </li> </ul> <p>Amazon Web Services authenticates the KMS key asynchronously. Therefore, if you specify an ID, alias, or ARN that is not valid, the action can appear to complete, but eventually fails.</p>
            presigned_url: <p>When you copy an encrypted source snapshot using the Amazon EC2 Query API, you must supply a pre-signed URL. This parameter is optional for unencrypted snapshots. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html\">Query requests</a>.</p> <p>The <code>PresignedUrl</code> should use the snapshot source endpoint, the <code>CopySnapshot</code> action, and include the <code>SourceRegion</code>, <code>SourceSnapshotId</code>, and <code>DestinationRegion</code> parameters. The <code>PresignedUrl</code> must be signed using Amazon Web Services Signature Version 4. Because EBS snapshots are stored in Amazon S3, the signing algorithm for this parameter uses the same logic that is described in <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html\"> Authenticating Requests: Using Query Parameters (Amazon Web Services Signature Version 4)</a> in the <i>Amazon S3 API Reference</i>. An invalid or improperly signed <code>PresignedUrl</code> will cause the copy operation to fail asynchronously, and the snapshot will move to an <code>error</code> state.</p>
            source_region: <p>The ID of the Region that contains the snapshot to be copied.</p>
            source_snapshot_id: <p>The ID of the EBS snapshot to copy.</p>
            tag_specifications: <p>The tags to apply to the new snapshot.</p>
            completion_duration_minutes: <note> <p>Not supported when copying snapshots to or from Local Zones or Outposts.</p> </note> <p>Specify a completion duration, in 15 minute increments, to initiate a time-based snapshot copy. Time-based snapshot copy operations complete within the specified duration. For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/time-based-copies.html\"> Time-based copies</a>.</p> <p>If you do not specify a value, the snapshot copy operation is completed on a best-effort basis.</p>
            destination_availability_zone: <p>The Local Zone, for example, <code>cn-north-1-pkx-1a</code> to which to copy the snapshot.</p> <note> <p>Only supported when copying a snapshot to a Local Zone.</p> </note>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>

        Examples:
            To copy a snapshot
            This example copies a snapshot with the snapshot ID of ``snap-066877671789bd71b`` from the ``us-west-2`` region to the ``us-east-1`` region and adds a short description to identify the snapshot.

            >>> await client.copy_snapshot(source_region='us-west-2', source_snapshot_id='snap-066877671789bd71b', description='This is my copied snapshot.', destination_region='us-east-1')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.copy_snapshot_request.CopySnapshotRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.copy_snapshot_result.CopySnapshotResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.copy_snapshot

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.copy_snapshot.async_copy_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.copy_snapshot_request.CopySnapshotRequest = {}  # type: ignore[typeddict-item]
        if description is not None:
            input_["description"] = description
        if destination_outpost_arn is not None:
            input_["destination_outpost_arn"] = destination_outpost_arn
        if destination_region is not None:
            input_["destination_region"] = destination_region
        if encrypted is not None:
            input_["encrypted"] = encrypted
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if presigned_url is not None:
            input_["presigned_url"] = presigned_url
        input_["source_region"] = source_region
        input_["source_snapshot_id"] = source_snapshot_id
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications
        if completion_duration_minutes is not None:
            input_["completion_duration_minutes"] = completion_duration_minutes
        if destination_availability_zone is not None:
            input_["destination_availability_zone"] = destination_availability_zone
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def copy_volumes(
        self,
        source_volume_id: "aws_sdk_ec2.types.volume_id.VolumeId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        iops: Optional["aws_sdk_ec2.types.integer.Integer"] = None,
        size: Optional["aws_sdk_ec2.types.integer.Integer"] = None,
        volume_type: Optional["aws_sdk_ec2.types.volume_type.VolumeType"] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
        multi_attach_enabled: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        throughput: Optional["aws_sdk_ec2.types.integer.Integer"] = None,
        client_token: Optional["aws_sdk_ec2.types.string.String"] = None,
    ) -> "aws_sdk_ec2.types.copy_volumes_result.CopyVolumesResult":
        r"""<p>Creates a crash-consistent, point-in-time copy of an existing Amazon EBS volume within the same Availability Zone. The volume copy can be attached to an Amazon EC2 instance once it reaches the <code>available</code> state. For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/ebs-copying-volume.html\">Copy an Amazon EBS volume</a>.</p>

        Args:
            source_volume_id: <p>The ID of the source EBS volume to copy.</p>
            iops: <p>The number of I/O operations per second (IOPS) to provision for the volume copy. Required for <code>io1</code> and <code>io2</code> volumes. Optional for <code>gp3</code> volumes. Omit for all other volume types. Full provisioned IOPS performance can be achieved only once the volume copy is fully initialized. </p> <p>Valid ranges:</p> <ul> <li> <p>gp3: <code>3,000 </code>(<i>default</i>)<code> - 80,000</code> IOPS</p> </li> <li> <p>io1: <code>100 - 64,000</code> IOPS</p> </li> <li> <p>io2: <code>100 - 256,000</code> IOPS</p> </li> </ul> <note> <p> <a href=\"https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html\"> Instances built on the Nitro System</a> can support up to 256,000 IOPS. Other instances can support up to 32,000 IOPS.</p> </note>
            size: <p>The size of the volume copy, in GiBs. The size must be equal to or greater than the size of the source volume. If not specified, the size defaults to the size of the source volume.</p> <p>Maximum supported sizes:</p> <ul> <li> <p>gp2: <code>16,384</code> GiB</p> </li> <li> <p>gp3: <code>65,536</code> GiB</p> </li> <li> <p>io1: <code>16,384</code> GiB</p> </li> <li> <p>io2: <code>65,536</code> GiB</p> </li> <li> <p>st1 and sc1: <code>16,384</code> GiB</p> </li> <li> <p>standard: <code>1024</code> GiB</p> </li> </ul>
            volume_type: <p>The volume type for the volume copy. If not specified, the volume type defaults to <code>gp2</code>.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            tag_specifications: <p>The tags to apply to the volume copy during creation.</p>
            multi_attach_enabled: <p>Indicates whether to enable Amazon EBS Multi-Attach for the volume copy. If you enable Multi-Attach, you can attach the volume to up to 16 Nitro instances in the same Availability Zone simultaneously. Supported with <code>io1</code> and <code>io2</code> volumes only. For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes-multi.html\"> Amazon EBS Multi-Attach</a>.</p>
            throughput: <p>The throughput to provision for the volume copy, in MiB/s. Supported for <code>gp3</code> volumes only. Omit for all other volume types. Full provisioned throughput performance can be achieved only once the volume copy is fully initialized.</p> <p>Valid Range: <code>125 - 2000</code> MiB/s</p> <p></p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\"> Ensure Idempotency</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.copy_volumes_request.CopyVolumesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.copy_volumes_result.CopyVolumesResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.copy_volumes

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.copy_volumes.async_copy_volumes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.copy_volumes_request.CopyVolumesRequest = {}  # type: ignore[typeddict-item]
        input_["source_volume_id"] = source_volume_id
        if iops is not None:
            input_["iops"] = iops
        if size is not None:
            input_["size"] = size
        if volume_type is not None:
            input_["volume_type"] = volume_type
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications
        if multi_attach_enabled is not None:
            input_["multi_attach_enabled"] = multi_attach_enabled
        if throughput is not None:
            input_["throughput"] = throughput
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_capacity_manager_data_export(
        self,
        s3_bucket_name: "aws_sdk_ec2.types.string.String",
        schedule: "aws_sdk_ec2.types.schedule.Schedule",
        output_format: "aws_sdk_ec2.types.output_format.OutputFormat",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        s3_bucket_prefix: Optional["aws_sdk_ec2.types.string.String"] = None,
        client_token: Optional["aws_sdk_ec2.types.string.String"] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
    ) -> "aws_sdk_ec2.types.create_capacity_manager_data_export_result.CreateCapacityManagerDataExportResult":
        """<p> Creates a new data export configuration for EC2 Capacity Manager. This allows you to automatically export capacity usage data to an S3 bucket on a scheduled basis. The exported data includes metrics for On-Demand, Spot, and Capacity Reservations usage across your organization. </p>

        Args:
            s3_bucket_name: <p> The name of the S3 bucket where the capacity data export files will be delivered. The bucket must exist and you must have write permissions to it. </p>
            s3_bucket_prefix: <p> The S3 key prefix for the exported data files. This allows you to organize exports in a specific folder structure within your bucket. If not specified, files are placed at the bucket root. </p>
            schedule: <p> The frequency at which data exports are generated. </p>
            output_format: <p> The file format for the exported data. Parquet format is recommended for large datasets and better compression. </p>
            client_token: <p> Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see Ensure Idempotency. </p>
            dry_run: <p> Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>. </p>
            tag_specifications: <p> The tags to apply to the data export configuration. You can tag the export for organization and cost tracking purposes. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.create_capacity_manager_data_export_request.CreateCapacityManagerDataExportRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.create_capacity_manager_data_export_result.CreateCapacityManagerDataExportResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.create_capacity_manager_data_export

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.create_capacity_manager_data_export.async_create_capacity_manager_data_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.create_capacity_manager_data_export_request.CreateCapacityManagerDataExportRequest = {}  # type: ignore[typeddict-item]
        input_["s3_bucket_name"] = s3_bucket_name
        if s3_bucket_prefix is not None:
            input_["s3_bucket_prefix"] = s3_bucket_prefix
        input_["schedule"] = schedule
        input_["output_format"] = output_format
        if client_token is not None:
            input_["client_token"] = client_token
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_capacity_reservation(
        self,
        instance_type: "aws_sdk_ec2.types.string.String",
        instance_platform: "aws_sdk_ec2.types.capacity_reservation_instance_platform.CapacityReservationInstancePlatform",
        instance_count: "aws_sdk_ec2.types.integer.Integer",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        client_token: Optional["aws_sdk_ec2.types.string.String"] = None,
        availability_zone: Optional[
            "aws_sdk_ec2.types.availability_zone_name.AvailabilityZoneName"
        ] = None,
        availability_zone_id: Optional[
            "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
        ] = None,
        tenancy: Optional[
            "aws_sdk_ec2.types.capacity_reservation_tenancy.CapacityReservationTenancy"
        ] = None,
        ebs_optimized: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        ephemeral_storage: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        end_date: Optional["aws_sdk_ec2.types.date_time.DateTime"] = None,
        end_date_type: Optional["aws_sdk_ec2.types.end_date_type.EndDateType"] = None,
        instance_match_criteria: Optional[
            "aws_sdk_ec2.types.instance_match_criteria.InstanceMatchCriteria"
        ] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        outpost_arn: Optional["aws_sdk_ec2.types.outpost_arn.OutpostArn"] = None,
        placement_group_arn: Optional[
            "aws_sdk_ec2.types.placement_group_arn.PlacementGroupArn"
        ] = None,
        start_date: Optional[
            "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
        ] = None,
        commitment_duration: Optional[
            "aws_sdk_ec2.types.capacity_reservation_commitment_duration.CapacityReservationCommitmentDuration"
        ] = None,
        delivery_preference: Optional[
            "aws_sdk_ec2.types.capacity_reservation_delivery_preference.CapacityReservationDeliveryPreference"
        ] = None,
    ) -> "aws_sdk_ec2.types.create_capacity_reservation_result.CreateCapacityReservationResult":
        r"""<p>Creates a new Capacity Reservation with the specified attributes. Capacity Reservations enable you to reserve capacity for your Amazon EC2 instances in a specific Availability Zone for any duration.</p> <p>You can create a Capacity Reservation at any time, and you can choose when it starts. You can create a Capacity Reservation for immediate use or you can request a Capacity Reservation for a future date.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html\"> Reserve compute capacity with On-Demand Capacity Reservations</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>Your request to create a Capacity Reservation could fail if:</p> <ul> <li> <p>Amazon EC2 does not have sufficient capacity. In this case, try again at a later time, try in a different Availability Zone, or request a smaller Capacity Reservation. If your workload is flexible across instance types and sizes, try with different instance attributes.</p> </li> <li> <p>The requested quantity exceeds your On-Demand Instance quota. In this case, increase your On-Demand Instance quota for the requested instance type and try again. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html\"> Amazon EC2 Service Quotas</a> in the <i>Amazon EC2 User Guide</i>.</p> </li> </ul>

        Args:
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensure Idempotency</a>.</p>
            instance_type: <p>The instance type for which to reserve capacity.</p> <note> <p>You can request future-dated Capacity Reservations for instance types in the C, M, R, I, T, and G instance families only.</p> </note> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html\">Instance types</a> in the <i>Amazon EC2 User Guide</i>.</p>
            instance_platform: <p>The type of operating system for which to reserve capacity.</p>
            availability_zone: <p>The Availability Zone in which to create the Capacity Reservation.</p>
            availability_zone_id: <p>The ID of the Availability Zone in which to create the Capacity Reservation.</p>
            tenancy: <p>Indicates the tenancy of the Capacity Reservation. A Capacity Reservation can have one of the following tenancy settings:</p> <ul> <li> <p> <code>default</code> - The Capacity Reservation is created on hardware that is shared with other Amazon Web Services accounts.</p> </li> <li> <p> <code>dedicated</code> - The Capacity Reservation is created on single-tenant hardware that is dedicated to a single Amazon Web Services account.</p> </li> </ul>
            instance_count: <p>The number of instances for which to reserve capacity.</p> <note> <p>You can request future-dated Capacity Reservations for an instance count with a minimum of 32 vCPUs. For example, if you request a future-dated Capacity Reservation for <code>m5.xlarge</code> instances, you must request at least 8 instances (<i>8 * m5.xlarge = 32 vCPUs</i>).</p> </note> <p>Valid range: 1 - 1000</p>
            ebs_optimized: <p>Indicates whether the Capacity Reservation supports EBS-optimized instances. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS- optimized instance.</p>
            ephemeral_storage: <p> <i>Deprecated.</i> </p>
            end_date: <p>The date and time at which the Capacity Reservation expires. When a Capacity Reservation expires, the reserved capacity is released and you can no longer launch instances into it. The Capacity Reservation's state changes to <code>expired</code> when it reaches its end date and time.</p> <p>You must provide an <code>EndDate</code> value if <code>EndDateType</code> is <code>limited</code>. Omit <code>EndDate</code> if <code>EndDateType</code> is <code>unlimited</code>.</p> <p>If the <code>EndDateType</code> is <code>limited</code>, the Capacity Reservation is cancelled within an hour from the specified time. For example, if you specify 5/31/2019, 13:30:55, the Capacity Reservation is guaranteed to end between 13:30:55 and 14:30:55 on 5/31/2019.</p> <p>If you are requesting a future-dated Capacity Reservation, you can't specify an end date and time that is within the commitment duration.</p>
            end_date_type: <p>Indicates the way in which the Capacity Reservation ends. A Capacity Reservation can have one of the following end types:</p> <ul> <li> <p> <code>unlimited</code> - The Capacity Reservation remains active until you explicitly cancel it. Do not provide an <code>EndDate</code> if the <code>EndDateType</code> is <code>unlimited</code>.</p> </li> <li> <p> <code>limited</code> - The Capacity Reservation expires automatically at a specified date and time. You must provide an <code>EndDate</code> value if the <code>EndDateType</code> value is <code>limited</code>.</p> </li> </ul>
            instance_match_criteria: <p>Indicates the type of instance launches that the Capacity Reservation accepts. The options include:</p> <ul> <li> <p> <code>open</code> - The Capacity Reservation automatically matches all instances that have matching attributes (instance type, platform, and Availability Zone). Instances that have matching attributes run in the Capacity Reservation automatically without specifying any additional parameters.</p> </li> <li> <p> <code>targeted</code> - The Capacity Reservation only accepts instances that have matching attributes (instance type, platform, and Availability Zone), and explicitly target the Capacity Reservation. This ensures that only permitted instances can use the reserved capacity. </p> </li> </ul> <note> <p>If you are requesting a future-dated Capacity Reservation, you must specify <code>targeted</code>.</p> </note> <p>Default: <code>open</code> </p>
            tag_specifications: <p>The tags to apply to the Capacity Reservation during launch.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            outpost_arn: <note> <p>Not supported for future-dated Capacity Reservations.</p> </note> <p>The Amazon Resource Name (ARN) of the Outpost on which to create the Capacity Reservation.</p>
            placement_group_arn: <note> <p>Not supported for future-dated Capacity Reservations.</p> </note> <p>The Amazon Resource Name (ARN) of the cluster placement group in which to create the Capacity Reservation. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-cpg.html\"> Capacity Reservations for cluster placement groups</a> in the <i>Amazon EC2 User Guide</i>.</p>
            start_date: <note> <p>Required for future-dated Capacity Reservations only. To create a Capacity Reservation for immediate use, omit this parameter. </p> </note> <p>The date and time at which the future-dated Capacity Reservation should become available for use, in the ISO8601 format in the UTC time zone (<code>YYYY-MM-DDThh:mm:ss.sssZ</code>).</p> <p>You can request a future-dated Capacity Reservation between 5 and 120 days in advance.</p>
            commitment_duration: <note> <p>Required for future-dated Capacity Reservations only. To create a Capacity Reservation for immediate use, omit this parameter. </p> </note> <p>Specify a commitment duration, in seconds, for the future-dated Capacity Reservation.</p> <p>The commitment duration is a minimum duration for which you commit to having the future-dated Capacity Reservation in the <code>active</code> state in your account after it has been delivered.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-concepts.html#cr-commitment-duration\"> Commitment duration</a>.</p>
            delivery_preference: <note> <p>Required for future-dated Capacity Reservations only. To create a Capacity Reservation for immediate use, omit this parameter. </p> </note> <p>Indicates that the requested capacity will be delivered in addition to any running instances or reserved capacity that you have in your account at the requested date and time.</p> <p>The only supported value is <code>incremental</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.create_capacity_reservation_request.CreateCapacityReservationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.create_capacity_reservation_result.CreateCapacityReservationResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.create_capacity_reservation

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.create_capacity_reservation.async_create_capacity_reservation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.create_capacity_reservation_request.CreateCapacityReservationRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["instance_type"] = instance_type
        input_["instance_platform"] = instance_platform
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if availability_zone_id is not None:
            input_["availability_zone_id"] = availability_zone_id
        if tenancy is not None:
            input_["tenancy"] = tenancy
        input_["instance_count"] = instance_count
        if ebs_optimized is not None:
            input_["ebs_optimized"] = ebs_optimized
        if ephemeral_storage is not None:
            input_["ephemeral_storage"] = ephemeral_storage
        if end_date is not None:
            input_["end_date"] = end_date
        if end_date_type is not None:
            input_["end_date_type"] = end_date_type
        if instance_match_criteria is not None:
            input_["instance_match_criteria"] = instance_match_criteria
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if outpost_arn is not None:
            input_["outpost_arn"] = outpost_arn
        if placement_group_arn is not None:
            input_["placement_group_arn"] = placement_group_arn
        if start_date is not None:
            input_["start_date"] = start_date
        if commitment_duration is not None:
            input_["commitment_duration"] = commitment_duration
        if delivery_preference is not None:
            input_["delivery_preference"] = delivery_preference

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_capacity_reservation_by_splitting(
        self,
        source_capacity_reservation_id: "aws_sdk_ec2.types.capacity_reservation_id.CapacityReservationId",
        instance_count: "aws_sdk_ec2.types.integer.Integer",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        client_token: Optional["aws_sdk_ec2.types.string.String"] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
    ) -> "aws_sdk_ec2.types.create_capacity_reservation_by_splitting_result.CreateCapacityReservationBySplittingResult":
        r"""<p> Create a new Capacity Reservation by splitting the capacity of the source Capacity Reservation. The new Capacity Reservation will have the same attributes as the source Capacity Reservation except for tags. The source Capacity Reservation must be <code>active</code> and owned by your Amazon Web Services account. </p>

        Args:
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensure Idempotency</a>.</p>
            source_capacity_reservation_id: <p> The ID of the Capacity Reservation from which you want to split the capacity. </p>
            instance_count: <p> The number of instances to split from the source Capacity Reservation. </p>
            tag_specifications: <p> The tags to apply to the new Capacity Reservation. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.create_capacity_reservation_by_splitting_request.CreateCapacityReservationBySplittingRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.create_capacity_reservation_by_splitting_result.CreateCapacityReservationBySplittingResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.create_capacity_reservation_by_splitting

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.create_capacity_reservation_by_splitting.async_create_capacity_reservation_by_splitting(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.create_capacity_reservation_by_splitting_request.CreateCapacityReservationBySplittingRequest = {}  # type: ignore[typeddict-item]
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if client_token is not None:
            input_["client_token"] = client_token
        input_["source_capacity_reservation_id"] = source_capacity_reservation_id
        input_["instance_count"] = instance_count
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_capacity_reservation_fleet(
        self,
        instance_type_specifications: "aws_sdk_ec2.types.reservation_fleet_instance_specification_list.ReservationFleetInstanceSpecificationList",
        total_target_capacity: "aws_sdk_ec2.types.integer.Integer",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        allocation_strategy: Optional["aws_sdk_ec2.types.string.String"] = None,
        client_token: Optional["aws_sdk_ec2.types.string.String"] = None,
        tenancy: Optional[
            "aws_sdk_ec2.types.fleet_capacity_reservation_tenancy.FleetCapacityReservationTenancy"
        ] = None,
        end_date: Optional[
            "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
        ] = None,
        instance_match_criteria: Optional[
            "aws_sdk_ec2.types.fleet_instance_match_criteria.FleetInstanceMatchCriteria"
        ] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.create_capacity_reservation_fleet_result.CreateCapacityReservationFleetResult":
        r"""<p>Creates a Capacity Reservation Fleet. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-cr-fleets.html#create-crfleet\">Create a Capacity Reservation Fleet</a> in the <i>Amazon EC2 User Guide</i>.</p>

        Args:
            allocation_strategy: <p>The strategy used by the Capacity Reservation Fleet to determine which of the specified instance types to use. Currently, only the <code>prioritized</code> allocation strategy is supported. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#allocation-strategy\"> Allocation strategy</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>Valid values: <code>prioritized</code> </p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensure Idempotency</a>.</p>
            instance_type_specifications: <p>Information about the instance types for which to reserve the capacity.</p>
            tenancy: <p>Indicates the tenancy of the Capacity Reservation Fleet. All Capacity Reservations in the Fleet inherit this tenancy. The Capacity Reservation Fleet can have one of the following tenancy settings:</p> <ul> <li> <p> <code>default</code> - The Capacity Reservation Fleet is created on hardware that is shared with other Amazon Web Services accounts.</p> </li> <li> <p> <code>dedicated</code> - The Capacity Reservations are created on single-tenant hardware that is dedicated to a single Amazon Web Services account.</p> </li> </ul>
            total_target_capacity: <p>The total number of capacity units to be reserved by the Capacity Reservation Fleet. This value, together with the instance type weights that you assign to each instance type used by the Fleet determine the number of instances for which the Fleet reserves capacity. Both values are based on units that make sense for your workload. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#target-capacity\">Total target capacity</a> in the <i>Amazon EC2 User Guide</i>.</p>
            end_date: <p>The date and time at which the Capacity Reservation Fleet expires. When the Capacity Reservation Fleet expires, its state changes to <code>expired</code> and all of the Capacity Reservations in the Fleet expire.</p> <p>The Capacity Reservation Fleet expires within an hour after the specified time. For example, if you specify <code>5/31/2019</code>, <code>13:30:55</code>, the Capacity Reservation Fleet is guaranteed to expire between <code>13:30:55</code> and <code>14:30:55</code> on <code>5/31/2019</code>. </p>
            instance_match_criteria: <p>Indicates the type of instance launches that the Capacity Reservation Fleet accepts. All Capacity Reservations in the Fleet inherit this instance matching criteria.</p> <p>Currently, Capacity Reservation Fleets support <code>open</code> instance matching criteria only. This means that instances that have matching attributes (instance type, platform, and Availability Zone) run in the Capacity Reservations automatically. Instances do not need to explicitly target a Capacity Reservation Fleet to use its reserved capacity.</p>
            tag_specifications: <p>The tags to assign to the Capacity Reservation Fleet. The tags are automatically assigned to the Capacity Reservations in the Fleet.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.create_capacity_reservation_fleet_request.CreateCapacityReservationFleetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.create_capacity_reservation_fleet_result.CreateCapacityReservationFleetResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.create_capacity_reservation_fleet

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.create_capacity_reservation_fleet.async_create_capacity_reservation_fleet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.create_capacity_reservation_fleet_request.CreateCapacityReservationFleetRequest = {}  # type: ignore[typeddict-item]
        if allocation_strategy is not None:
            input_["allocation_strategy"] = allocation_strategy
        if client_token is not None:
            input_["client_token"] = client_token
        input_["instance_type_specifications"] = instance_type_specifications
        if tenancy is not None:
            input_["tenancy"] = tenancy
        input_["total_target_capacity"] = total_target_capacity
        if end_date is not None:
            input_["end_date"] = end_date
        if instance_match_criteria is not None:
            input_["instance_match_criteria"] = instance_match_criteria
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_carrier_gateway(
        self,
        vpc_id: "aws_sdk_ec2.types.vpc_id.VpcId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        client_token: Optional["aws_sdk_ec2.types.string.String"] = None,
    ) -> "aws_sdk_ec2.types.create_carrier_gateway_result.CreateCarrierGatewayResult":
        r"""<p>Creates a carrier gateway. For more information about carrier gateways, see <a href=\"https://docs.aws.amazon.com/wavelength/latest/developerguide/how-wavelengths-work.html#wavelength-carrier-gateway\">Carrier gateways</a> in the <i>Amazon Web Services Wavelength Developer Guide</i>.</p>

        Args:
            vpc_id: <p>The ID of the VPC to associate with the carrier gateway.</p>
            tag_specifications: <p>The tags to associate with the carrier gateway.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">How to ensure idempotency</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.create_carrier_gateway_request.CreateCarrierGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.create_carrier_gateway_result.CreateCarrierGatewayResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.create_carrier_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.create_carrier_gateway.async_create_carrier_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.create_carrier_gateway_request.CreateCarrierGatewayRequest = {}  # type: ignore[typeddict-item]
        input_["vpc_id"] = vpc_id
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_client_vpn_endpoint(
        self,
        server_certificate_arn: "aws_sdk_ec2.types.string.String",
        authentication_options: "aws_sdk_ec2.types.client_vpn_authentication_request_list.ClientVpnAuthenticationRequestList",
        connection_log_options: "aws_sdk_ec2.types.connection_log_options.ConnectionLogOptions",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        client_cidr_block: Optional["aws_sdk_ec2.types.string.String"] = None,
        dns_servers: Optional[
            "aws_sdk_ec2.types.value_string_list.ValueStringList"
        ] = None,
        transport_protocol: Optional[
            "aws_sdk_ec2.types.transport_protocol.TransportProtocol"
        ] = None,
        vpn_port: Optional["aws_sdk_ec2.types.integer.Integer"] = None,
        description: Optional["aws_sdk_ec2.types.string.String"] = None,
        split_tunnel: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        client_token: Optional["aws_sdk_ec2.types.string.String"] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
        security_group_ids: Optional[
            "aws_sdk_ec2.types.client_vpn_security_group_id_set.ClientVpnSecurityGroupIdSet"
        ] = None,
        vpc_id: Optional["aws_sdk_ec2.types.vpc_id.VpcId"] = None,
        self_service_portal: Optional[
            "aws_sdk_ec2.types.self_service_portal.SelfServicePortal"
        ] = None,
        client_connect_options: Optional[
            "aws_sdk_ec2.types.client_connect_options.ClientConnectOptions"
        ] = None,
        session_timeout_hours: Optional["aws_sdk_ec2.types.integer.Integer"] = None,
        client_login_banner_options: Optional[
            "aws_sdk_ec2.types.client_login_banner_options.ClientLoginBannerOptions"
        ] = None,
        client_route_enforcement_options: Optional[
            "aws_sdk_ec2.types.client_route_enforcement_options.ClientRouteEnforcementOptions"
        ] = None,
        disconnect_on_session_timeout: Optional[
            "aws_sdk_ec2.types.boolean.Boolean"
        ] = None,
        endpoint_ip_address_type: Optional[
            "aws_sdk_ec2.types.endpoint_ip_address_type.EndpointIpAddressType"
        ] = None,
        traffic_ip_address_type: Optional[
            "aws_sdk_ec2.types.traffic_ip_address_type.TrafficIpAddressType"
        ] = None,
        transit_gateway_configuration: Optional[
            "aws_sdk_ec2.types.transit_gateway_configuration_input_structure.TransitGatewayConfigurationInputStructure"
        ] = None,
    ) -> "aws_sdk_ec2.types.create_client_vpn_endpoint_result.CreateClientVpnEndpointResult":
        r"""<p>Creates a Client VPN endpoint. A Client VPN endpoint is the resource you create and configure to enable and manage client VPN sessions. It is the destination endpoint at which all client VPN sessions are terminated.</p>

        Args:
            client_cidr_block: <p>The IPv4 address range, in CIDR notation, from which to assign client IP addresses. The address range cannot overlap with the local CIDR of the VPC in which the associated subnet is located, or the routes that you add manually. The address range cannot be changed after the Client VPN endpoint has been created. Client CIDR range must have a size of at least /22 and must not be greater than /12.</p>
            server_certificate_arn: <p>The ARN of the server certificate. For more information, see the <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/\">Certificate Manager User Guide</a>.</p>
            authentication_options: <p>Information about the authentication method to be used to authenticate clients.</p>
            connection_log_options: <p>Information about the client connection logging options.</p> <p>If you enable client connection logging, data about client connections is sent to a Cloudwatch Logs log stream. The following information is logged:</p> <ul> <li> <p>Client connection requests</p> </li> <li> <p>Client connection results (successful and unsuccessful)</p> </li> <li> <p>Reasons for unsuccessful client connection requests</p> </li> <li> <p>Client connection termination time</p> </li> </ul>
            dns_servers: <p>Information about the DNS servers to be used for DNS resolution. A Client VPN endpoint can have up to two DNS servers. If no DNS server is specified, the DNS address configured on the device is used for the DNS server.</p>
            transport_protocol: <p>The transport protocol to be used by the VPN session.</p> <p>Default value: <code>udp</code> </p>
            vpn_port: <p>The port number to assign to the Client VPN endpoint for TCP and UDP traffic.</p> <p>Valid Values: <code>443</code> | <code>1194</code> </p> <p>Default Value: <code>443</code> </p>
            description: <p>A brief description of the Client VPN endpoint.</p>
            split_tunnel: <p>Indicates whether split-tunnel is enabled on the Client VPN endpoint.</p> <p>By default, split-tunnel on a VPN endpoint is disabled.</p> <p>For information about split-tunnel VPN endpoints, see <a href=\"https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/split-tunnel-vpn.html\">Split-tunnel Client VPN endpoint</a> in the <i>Client VPN Administrator Guide</i>.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>
            tag_specifications: <p>The tags to apply to the Client VPN endpoint during creation.</p>
            security_group_ids: <p>The IDs of one or more security groups to apply to the target network. You must also specify the ID of the VPC that contains the security groups.</p>
            vpc_id: <p>The ID of the VPC to associate with the Client VPN endpoint. If no security group IDs are specified in the request, the default security group for the VPC is applied.</p>
            self_service_portal: <p>Specify whether to enable the self-service portal for the Client VPN endpoint.</p> <p>Default Value: <code>enabled</code> </p>
            client_connect_options: <p>The options for managing connection authorization for new client connections.</p>
            session_timeout_hours: <p>The maximum VPN session duration time in hours.</p> <p>Valid values: <code>8 | 10 | 12 | 24</code> </p> <p>Default value: <code>24</code> </p>
            client_login_banner_options: <p>Options for enabling a customizable text banner that will be displayed on Amazon Web Services provided clients when a VPN session is established.</p>
            client_route_enforcement_options: <p>Client route enforcement is a feature of the Client VPN service that helps enforce administrator defined routes on devices connected through the VPN. T his feature helps improve your security posture by ensuring that network traffic originating from a connected client is not inadvertently sent outside the VPN tunnel.</p> <p>Client route enforcement works by monitoring the route table of a connected device for routing policy changes to the VPN connection. If the feature detects any VPN routing policy modifications, it will automatically force an update to the route table, reverting it back to the expected route configurations.</p>
            disconnect_on_session_timeout: <p>Indicates whether the client VPN session is disconnected after the maximum timeout specified in <code>SessionTimeoutHours</code> is reached. If <code>true</code>, users are prompted to reconnect client VPN. If <code>false</code>, client VPN attempts to reconnect automatically. The default value is <code>true</code>.</p>
            endpoint_ip_address_type: <p>The IP address type for the Client VPN endpoint. Valid values are <code>ipv4</code> (default) for IPv4 addressing only, <code>ipv6</code> for IPv6 addressing only, or <code>dual-stack</code> for both IPv4 and IPv6 addressing. When set to <code>dual-stack,</code> clients can connect to the endpoint using either IPv4 or IPv6 addresses..</p>
            traffic_ip_address_type: <p>The IP address type for traffic within the Client VPN tunnel. Valid values are <code>ipv4</code> (default) for IPv4 traffic only, <code>ipv6</code> for IPv6 addressing only, or <code>dual-stack</code> for both IPv4 and IPv6 traffic. When set to <code>dual-stack</code>, clients can access both IPv4 and IPv6 resources through the VPN .</p>
            transit_gateway_configuration: <p>The Transit Gateway configuration for the Client VPN endpoint. Use this parameter to associate the endpoint with a Transit Gateway instead of a VPC. You cannot specify both <code>TransitGatewayConfiguration</code> and <code>VpcId</code>/<code>SecurityGroupIds</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.create_client_vpn_endpoint_request.CreateClientVpnEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.create_client_vpn_endpoint_result.CreateClientVpnEndpointResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.create_client_vpn_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.create_client_vpn_endpoint.async_create_client_vpn_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.create_client_vpn_endpoint_request.CreateClientVpnEndpointRequest = {}  # type: ignore[typeddict-item]
        if client_cidr_block is not None:
            input_["client_cidr_block"] = client_cidr_block
        input_["server_certificate_arn"] = server_certificate_arn
        input_["authentication_options"] = authentication_options
        input_["connection_log_options"] = connection_log_options
        if dns_servers is not None:
            input_["dns_servers"] = dns_servers
        if transport_protocol is not None:
            input_["transport_protocol"] = transport_protocol
        if vpn_port is not None:
            input_["vpn_port"] = vpn_port
        if description is not None:
            input_["description"] = description
        if split_tunnel is not None:
            input_["split_tunnel"] = split_tunnel
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if client_token is not None:
            input_["client_token"] = client_token
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if vpc_id is not None:
            input_["vpc_id"] = vpc_id
        if self_service_portal is not None:
            input_["self_service_portal"] = self_service_portal
        if client_connect_options is not None:
            input_["client_connect_options"] = client_connect_options
        if session_timeout_hours is not None:
            input_["session_timeout_hours"] = session_timeout_hours
        if client_login_banner_options is not None:
            input_["client_login_banner_options"] = client_login_banner_options
        if client_route_enforcement_options is not None:
            input_["client_route_enforcement_options"] = (
                client_route_enforcement_options
            )
        if disconnect_on_session_timeout is not None:
            input_["disconnect_on_session_timeout"] = disconnect_on_session_timeout
        if endpoint_ip_address_type is not None:
            input_["endpoint_ip_address_type"] = endpoint_ip_address_type
        if traffic_ip_address_type is not None:
            input_["traffic_ip_address_type"] = traffic_ip_address_type
        if transit_gateway_configuration is not None:
            input_["transit_gateway_configuration"] = transit_gateway_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_client_vpn_route(
        self,
        client_vpn_endpoint_id: "aws_sdk_ec2.types.client_vpn_endpoint_id.ClientVpnEndpointId",
        destination_cidr_block: "aws_sdk_ec2.types.string.String",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        target_vpc_subnet_id: Optional["aws_sdk_ec2.types.subnet_id.SubnetId"] = None,
        description: Optional["aws_sdk_ec2.types.string.String"] = None,
        client_token: Optional["aws_sdk_ec2.types.string.String"] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.create_client_vpn_route_result.CreateClientVpnRouteResult":
        r"""<p>Adds a route to a network to a Client VPN endpoint. Each Client VPN endpoint has a route table that describes the available destination network routes. Each route in the route table specifies the path for traﬃc to speciﬁc resources or networks.</p>

        Args:
            client_vpn_endpoint_id: <p>The ID of the Client VPN endpoint to which to add the route.</p>
            destination_cidr_block: <p>The IPv4 address range, in CIDR notation, of the route destination. For example:</p> <ul> <li> <p>To add a route for Internet access, enter <code>0.0.0.0/0</code> </p> </li> <li> <p>To add a route for a peered VPC, enter the peered VPC's IPv4 CIDR range</p> </li> <li> <p>To add a route for an on-premises network, enter the Amazon Web Services Site-to-Site VPN connection's IPv4 CIDR range</p> </li> <li> <p>To add a route for the local network, enter the client CIDR range</p> </li> </ul>
            target_vpc_subnet_id: <p>The ID of the subnet through which you want to route traffic. The specified subnet must be an existing target network of the Client VPN endpoint.</p> <p>Alternatively, if you're adding a route for the local network, specify <code>local</code>.</p> <p>This parameter is required for VPC-based Client VPN endpoints. For Transit Gateway-based endpoints, this parameter is not required.</p>
            description: <p>A brief description of the route.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.create_client_vpn_route_request.CreateClientVpnRouteRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.create_client_vpn_route_result.CreateClientVpnRouteResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.create_client_vpn_route

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.create_client_vpn_route.async_create_client_vpn_route(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.create_client_vpn_route_request.CreateClientVpnRouteRequest = {}  # type: ignore[typeddict-item]
        input_["client_vpn_endpoint_id"] = client_vpn_endpoint_id
        input_["destination_cidr_block"] = destination_cidr_block
        if target_vpc_subnet_id is not None:
            input_["target_vpc_subnet_id"] = target_vpc_subnet_id
        if description is not None:
            input_["description"] = description
        if client_token is not None:
            input_["client_token"] = client_token
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_coip_cidr(
        self,
        cidr: "aws_sdk_ec2.types.string.String",
        coip_pool_id: "aws_sdk_ec2.types.ipv4_pool_coip_id.Ipv4PoolCoipId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.create_coip_cidr_result.CreateCoipCidrResult":
        """<p> Creates a range of customer-owned IP addresses. </p>

        Args:
            cidr: <p> A customer-owned IP address range to create. </p>
            coip_pool_id: <p> The ID of the address pool. </p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.create_coip_cidr_request.CreateCoipCidrRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.create_coip_cidr_result.CreateCoipCidrResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.create_coip_cidr

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.create_coip_cidr.async_create_coip_cidr(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.create_coip_cidr_request.CreateCoipCidrRequest = {}  # type: ignore[typeddict-item]
        input_["cidr"] = cidr
        input_["coip_pool_id"] = coip_pool_id
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_coip_pool(
        self,
        local_gateway_route_table_id: "aws_sdk_ec2.types.local_gateway_routetable_id.LocalGatewayRoutetableId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.create_coip_pool_result.CreateCoipPoolResult":
        """<p> Creates a pool of customer-owned IP (CoIP) addresses. </p>

        Args:
            local_gateway_route_table_id: <p> The ID of the local gateway route table. </p>
            tag_specifications: <p> The tags to assign to the CoIP address pool. </p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.create_coip_pool_request.CreateCoipPoolRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.create_coip_pool_result.CreateCoipPoolResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.create_coip_pool

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.create_coip_pool.async_create_coip_pool(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.create_coip_pool_request.CreateCoipPoolRequest = {}  # type: ignore[typeddict-item]
        input_["local_gateway_route_table_id"] = local_gateway_route_table_id
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_customer_gateway(
        self,
        type: "aws_sdk_ec2.types.gateway_type.GatewayType",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        bgp_asn: Optional["aws_sdk_ec2.types.integer.Integer"] = None,
        public_ip: Optional["aws_sdk_ec2.types.string.String"] = None,
        certificate_arn: Optional["aws_sdk_ec2.types.string.String"] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
        device_name: Optional["aws_sdk_ec2.types.string.String"] = None,
        ip_address: Optional["aws_sdk_ec2.types.string.String"] = None,
        bgp_asn_extended: Optional["aws_sdk_ec2.types.long.Long"] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.create_customer_gateway_result.CreateCustomerGatewayResult":
        r"""<p>Provides information to Amazon Web Services about your customer gateway device. The customer gateway device is the appliance at your end of the VPN connection. You must provide the IP address of the customer gateway device’s external interface. The IP address must be static and can be behind a device performing network address translation (NAT).</p> <p>For devices that use Border Gateway Protocol (BGP), you can also provide the device's BGP Autonomous System Number (ASN). You can use an existing ASN assigned to your network. If you don't have an ASN already, you can use a private ASN. For more information, see <a href=\"https://docs.aws.amazon.com/vpn/latest/s2svpn/cgw-options.html\">Customer gateway options for your Site-to-Site VPN connection</a> in the <i>Amazon Web Services Site-to-Site VPN User Guide</i>.</p> <p>To create more than one customer gateway with the same VPN type, IP address, and BGP ASN, specify a unique device name for each customer gateway. An identical request returns information about the existing customer gateway; it doesn't create a new customer gateway.</p>

        Args:
            bgp_asn: <p>For customer gateway devices that support BGP, specify the device's ASN. You must specify either <code>BgpAsn</code> or <code>BgpAsnExtended</code> when creating the customer gateway. If the ASN is larger than <code>2,147,483,647</code>, you must use <code>BgpAsnExtended</code>.</p> <p>Default: 65000</p> <p>Valid values: <code>1</code> to <code>2,147,483,647</code> </p>
            public_ip: <p> <i>This member has been deprecated.</i> The Internet-routable IP address for the customer gateway's outside interface. The address must be static.</p>
            certificate_arn: <p>The Amazon Resource Name (ARN) for the customer gateway certificate.</p>
            type: <p>The type of VPN connection that this customer gateway supports (<code>ipsec.1</code>).</p>
            tag_specifications: <p>The tags to apply to the customer gateway.</p>
            device_name: <p>A name for the customer gateway device.</p> <p>Length Constraints: Up to 255 characters.</p>
            ip_address: <p>The IP address for the customer gateway device's outside interface. The address must be static. If <code>OutsideIpAddressType</code> in your VPN connection options is set to <code>PrivateIpv4</code>, you can use an RFC6598 or RFC1918 private IPv4 address. If <code>OutsideIpAddressType</code> is set to <code>Ipv6</code>, you can use an IPv6 address. </p>
            bgp_asn_extended: <p>For customer gateway devices that support BGP, specify the device's ASN. You must specify either <code>BgpAsn</code> or <code>BgpAsnExtended</code> when creating the customer gateway. If the ASN is larger than <code>2,147,483,647</code>, you must use <code>BgpAsnExtended</code>.</p> <p>Valid values: <code>2,147,483,648</code> to <code>4,294,967,295</code> </p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>

        Examples:
            To create a customer gateway
            This example creates a customer gateway with the specified IP address for its outside interface.

            >>> await client.create_customer_gateway(type='ipsec.1', public_ip='12.1.2.3', bgp_asn=65534)
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.create_customer_gateway_request.CreateCustomerGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.create_customer_gateway_result.CreateCustomerGatewayResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.create_customer_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.create_customer_gateway.async_create_customer_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.create_customer_gateway_request.CreateCustomerGatewayRequest = {}  # type: ignore[typeddict-item]
        if bgp_asn is not None:
            input_["bgp_asn"] = bgp_asn
        if public_ip is not None:
            input_["public_ip"] = public_ip
        if certificate_arn is not None:
            input_["certificate_arn"] = certificate_arn
        input_["type"] = type
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications
        if device_name is not None:
            input_["device_name"] = device_name
        if ip_address is not None:
            input_["ip_address"] = ip_address
        if bgp_asn_extended is not None:
            input_["bgp_asn_extended"] = bgp_asn_extended
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_default_subnet(
        self,
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        availability_zone: Optional[
            "aws_sdk_ec2.types.availability_zone_name.AvailabilityZoneName"
        ] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        ipv6_native: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        availability_zone_id: Optional[
            "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
        ] = None,
    ) -> "aws_sdk_ec2.types.create_default_subnet_result.CreateDefaultSubnetResult":
        r"""<p>Creates a default subnet with a size <code>/20</code> IPv4 CIDR block in the specified Availability Zone in your default VPC. You can have only one default subnet per Availability Zone. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/work-with-default-vpc.html#create-default-subnet\">Create a default subnet</a> in the <i>Amazon VPC User Guide</i>.</p>

        Args:
            availability_zone: <p>The Availability Zone in which to create the default subnet.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> must be specified, but not both.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            ipv6_native: <p>Indicates whether to create an IPv6 only subnet. If you already have a default subnet for this Availability Zone, you must delete it before you can create an IPv6 only subnet.</p>
            availability_zone_id: <p>The ID of the Availability Zone.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> must be specified, but not both.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.create_default_subnet_request.CreateDefaultSubnetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.create_default_subnet_result.CreateDefaultSubnetResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.create_default_subnet

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.create_default_subnet.async_create_default_subnet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.create_default_subnet_request.CreateDefaultSubnetRequest = {}  # type: ignore[typeddict-item]
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if ipv6_native is not None:
            input_["ipv6_native"] = ipv6_native
        if availability_zone_id is not None:
            input_["availability_zone_id"] = availability_zone_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_default_vpc(
        self,
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.create_default_vpc_result.CreateDefaultVpcResult":
        r"""<p>Creates a default VPC with a size <code>/16</code> IPv4 CIDR block and a default subnet in each Availability Zone. For more information about the components of a default VPC, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html\">Default VPCs</a> in the <i>Amazon VPC User Guide</i>. You cannot specify the components of the default VPC yourself.</p> <p>If you deleted your previous default VPC, you can create a default VPC. You cannot have more than one default VPC per Region.</p>

        Args:
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.create_default_vpc_request.CreateDefaultVpcRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.create_default_vpc_result.CreateDefaultVpcResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.create_default_vpc

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.create_default_vpc.async_create_default_vpc(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.create_default_vpc_request.CreateDefaultVpcRequest = {}  # type: ignore[typeddict-item]
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_delegate_mac_volume_ownership_task(
        self,
        instance_id: "aws_sdk_ec2.types.instance_id.InstanceId",
        mac_credentials: "aws_sdk_ec2.types.sensitive_mac_credentials.SensitiveMacCredentials",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        client_token: Optional["aws_sdk_ec2.types.string.String"] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
    ) -> "aws_sdk_ec2.types.create_delegate_mac_volume_ownership_task_result.CreateDelegateMacVolumeOwnershipTaskResult":
        r"""<p>Delegates ownership of the Amazon EBS root volume for an Apple silicon Mac instance to an administrative user.</p>

        Args:
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring Idempotency</a>.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            instance_id: <p>The ID of the Amazon EC2 Mac instance.</p>
            mac_credentials: <p>Specifies the following credentials:</p> <ul> <li> <p> <b>Internal disk administrative user</b> </p> <ul> <li> <p> <b>Username</b> - Only the default administrative user (<code>aws-managed-user</code>) is supported and it is used by default. You can't specify a different administrative user.</p> </li> <li> <p> <b>Password</b> - If you did not change the default password for <code>aws-managed-user</code>, specify the default password, which is <i>blank</i>. Otherwise, specify your password.</p> </li> </ul> </li> <li> <p> <b>Amazon EBS root volume administrative user</b> </p> <ul> <li> <p> <b>Username</b> - If you did not change the default administrative user, specify <code>ec2-user</code>. Otherwise, specify the username for your administrative user.</p> </li> <li> <p> <b>Password</b> - Specify the password for the administrative user.</p> </li> </ul> </li> </ul> <p>The credentials must be specified in the following JSON format:</p> <p> <code>{ \"internalDiskPassword\":\"<i>internal-disk-admin_password</i>\", \"rootVolumeUsername\":\"<i>root-volume-admin_username</i>\", \"rootVolumepassword\":\"<i>root-volume-admin_password</i>\" }</code> </p>
            tag_specifications: <p>The tags to assign to the volume ownership delegation task.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.create_delegate_mac_volume_ownership_task_request.CreateDelegateMacVolumeOwnershipTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.create_delegate_mac_volume_ownership_task_result.CreateDelegateMacVolumeOwnershipTaskResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.create_delegate_mac_volume_ownership_task

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.create_delegate_mac_volume_ownership_task.async_create_delegate_mac_volume_ownership_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.create_delegate_mac_volume_ownership_task_request.CreateDelegateMacVolumeOwnershipTaskRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        if dry_run is not None:
            input_["dry_run"] = dry_run
        input_["instance_id"] = instance_id
        input_["mac_credentials"] = mac_credentials
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_dhcp_options(
        self,
        dhcp_configurations: "aws_sdk_ec2.types.new_dhcp_configuration_list.NewDhcpConfigurationList",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.create_dhcp_options_result.CreateDhcpOptionsResult":
        r"""<p>Creates a custom set of DHCP options. After you create a DHCP option set, you associate it with a VPC. After you associate a DHCP option set with a VPC, all existing and newly launched instances in the VPC use this set of DHCP options.</p> <p>The following are the individual DHCP options you can specify. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html\">DHCP option sets</a> in the <i>Amazon VPC User Guide</i>.</p> <ul> <li> <p> <code>domain-name</code> - If you're using AmazonProvidedDNS in <code>us-east-1</code>, specify <code>ec2.internal</code>. If you're using AmazonProvidedDNS in any other Region, specify <code>region.compute.internal</code>. Otherwise, specify a custom domain name. This value is used to complete unqualified DNS hostnames.</p> <p>Some Linux operating systems accept multiple domain names separated by spaces. However, Windows and other Linux operating systems treat the value as a single domain, which results in unexpected behavior. If your DHCP option set is associated with a VPC that has instances running operating systems that treat the value as a single domain, specify only one domain name.</p> </li> <li> <p> <code>domain-name-servers</code> - The IP addresses of up to four DNS servers, or AmazonProvidedDNS. To specify multiple domain name servers in a single parameter, separate the IP addresses using commas. To have your instances receive custom DNS hostnames as specified in <code>domain-name</code>, you must specify a custom DNS server.</p> </li> <li> <p> <code>ntp-servers</code> - The IP addresses of up to eight Network Time Protocol (NTP) servers (four IPv4 addresses and four IPv6 addresses).</p> </li> <li> <p> <code>netbios-name-servers</code> - The IP addresses of up to four NetBIOS name servers.</p> </li> <li> <p> <code>netbios-node-type</code> - The NetBIOS node type (1, 2, 4, or 8). We recommend that you specify 2. Broadcast and multicast are not supported. For more information about NetBIOS node types, see <a href=\"https://www.ietf.org/rfc/rfc2132.txt\">RFC 2132</a>.</p> </li> <li> <p> <code>ipv6-address-preferred-lease-time</code> - A value (in seconds, minutes, hours, or years) for how frequently a running instance with an IPv6 assigned to it goes through DHCPv6 lease renewal. Acceptable values are between 140 and 2147483647 seconds (approximately 68 years). If no value is entered, the default lease time is 140 seconds. If you use long-term addressing for EC2 instances, you can increase the lease time and avoid frequent lease renewal requests. Lease renewal typically occurs when half of the lease time has elapsed.</p> </li> </ul>

        Args:
            dhcp_configurations: <p>A DHCP configuration option.</p>
            tag_specifications: <p>The tags to assign to the DHCP option.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>

        Examples:
            To create a DHCP options set
            This example creates a DHCP options set.

            >>> await client.create_dhcp_options(dhcp_configurations=[{'Key': 'domain-name-servers', 'Values': ['10.2.5.1', '10.2.5.2']}])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.create_dhcp_options_request.CreateDhcpOptionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.create_dhcp_options_result.CreateDhcpOptionsResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.create_dhcp_options

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.create_dhcp_options.async_create_dhcp_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.create_dhcp_options_request.CreateDhcpOptionsRequest = {}  # type: ignore[typeddict-item]
        input_["dhcp_configurations"] = dhcp_configurations
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_egress_only_internet_gateway(
        self,
        vpc_id: "aws_sdk_ec2.types.vpc_id.VpcId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        client_token: Optional["aws_sdk_ec2.types.string.String"] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
    ) -> "aws_sdk_ec2.types.create_egress_only_internet_gateway_result.CreateEgressOnlyInternetGatewayResult":
        r"""<p>[IPv6 only] Creates an egress-only internet gateway for your VPC. An egress-only internet gateway is used to enable outbound communication over IPv6 from instances in your VPC to the internet, and prevents hosts outside of your VPC from initiating an IPv6 connection with your instance.</p>

        Args:
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            vpc_id: <p>The ID of the VPC for which to create the egress-only internet gateway.</p>
            tag_specifications: <p>The tags to assign to the egress-only internet gateway.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.create_egress_only_internet_gateway_request.CreateEgressOnlyInternetGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.create_egress_only_internet_gateway_result.CreateEgressOnlyInternetGatewayResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.create_egress_only_internet_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.create_egress_only_internet_gateway.async_create_egress_only_internet_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.create_egress_only_internet_gateway_request.CreateEgressOnlyInternetGatewayRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        if dry_run is not None:
            input_["dry_run"] = dry_run
        input_["vpc_id"] = vpc_id
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_fleet(
        self,
        launch_template_configs: "aws_sdk_ec2.types.fleet_launch_template_config_list_request.FleetLaunchTemplateConfigListRequest",
        target_capacity_specification: "aws_sdk_ec2.types.target_capacity_specification_request.TargetCapacitySpecificationRequest",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        client_token: Optional["aws_sdk_ec2.types.string.String"] = None,
        spot_options: Optional[
            "aws_sdk_ec2.types.spot_options_request.SpotOptionsRequest"
        ] = None,
        on_demand_options: Optional[
            "aws_sdk_ec2.types.on_demand_options_request.OnDemandOptionsRequest"
        ] = None,
        reserved_capacity_options: Optional[
            "aws_sdk_ec2.types.reserved_capacity_options_request.ReservedCapacityOptionsRequest"
        ] = None,
        excess_capacity_termination_policy: Optional[
            "aws_sdk_ec2.types.fleet_excess_capacity_termination_policy.FleetExcessCapacityTerminationPolicy"
        ] = None,
        terminate_instances_with_expiration: Optional[
            "aws_sdk_ec2.types.boolean.Boolean"
        ] = None,
        type: Optional["aws_sdk_ec2.types.fleet_type.FleetType"] = None,
        valid_from: Optional["aws_sdk_ec2.types.date_time.DateTime"] = None,
        valid_until: Optional["aws_sdk_ec2.types.date_time.DateTime"] = None,
        replace_unhealthy_instances: Optional[
            "aws_sdk_ec2.types.boolean.Boolean"
        ] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
        context: Optional["aws_sdk_ec2.types.string.String"] = None,
    ) -> "aws_sdk_ec2.types.create_fleet_result.CreateFleetResult":
        r"""<p>Creates an EC2 Fleet that contains the configuration information for On-Demand Instances and Spot Instances. Instances are launched immediately if there is available capacity.</p> <p>A single EC2 Fleet can include multiple launch specifications that vary by instance type, AMI, Availability Zone, or subnet.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet.html\">EC2 Fleet</a> in the <i>Amazon EC2 User Guide</i>.</p>

        Args:
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            spot_options: <p>Describes the configuration of Spot Instances in an EC2 Fleet.</p>
            on_demand_options: <p>Describes the configuration of On-Demand Instances in an EC2 Fleet.</p>
            reserved_capacity_options: <p>Defines EC2 Fleet preferences for utilizing reserved capacity when DefaultTargetCapacityType is set to <code>reserved-capacity</code>.</p> <p>Supported only for fleets of type <code>instant</code>.</p>
            excess_capacity_termination_policy: <p>Indicates whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2 Fleet.</p> <p>Supported only for fleets of type <code>maintain</code>.</p>
            launch_template_configs: <p>The configuration for the EC2 Fleet.</p>
            target_capacity_specification: <p>The number of units to request.</p>
            terminate_instances_with_expiration: <p>Indicates whether running instances should be terminated when the EC2 Fleet expires.</p>
            type: <p>The fleet type. The default value is <code>maintain</code>.</p> <ul> <li> <p> <code>maintain</code> - The EC2 Fleet places an asynchronous request for your desired capacity, and continues to maintain your desired Spot capacity by replenishing interrupted Spot Instances.</p> </li> <li> <p> <code>request</code> - The EC2 Fleet places an asynchronous one-time request for your desired capacity, but does submit Spot requests in alternative capacity pools if Spot capacity is unavailable, and does not maintain Spot capacity if Spot Instances are interrupted.</p> </li> <li> <p> <code>instant</code> - The EC2 Fleet places a synchronous one-time request for your desired capacity, and returns errors for any instances that could not be launched.</p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-request-type.html\">EC2 Fleet request types</a> in the <i>Amazon EC2 User Guide</i>.</p>
            valid_from: <p>The start date and time of the request, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z). The default is to start fulfilling the request immediately.</p>
            valid_until: <p>The end date and time of the request, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z). At this point, no new EC2 Fleet requests are placed or able to fulfill the request. If no value is specified, the request remains until you cancel it.</p>
            replace_unhealthy_instances: <p>Indicates whether EC2 Fleet should replace unhealthy Spot Instances. Supported only for fleets of type <code>maintain</code>. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-ec2-fleet.html#ec2-fleet-health-checks\">EC2 Fleet health checks</a> in the <i>Amazon EC2 User Guide</i>.</p>
            tag_specifications: <p>The key-value pair for tagging the EC2 Fleet request on creation. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-resources\">Tag your resources</a>.</p> <p>If the fleet type is <code>instant</code>, specify a resource type of <code>fleet</code> to tag the fleet or <code>instance</code> to tag the instances at launch.</p> <p>If the fleet type is <code>maintain</code> or <code>request</code>, specify a resource type of <code>fleet</code> to tag the fleet. You cannot specify a resource type of <code>instance</code>. To tag instances at launch, specify the tags in a <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html#create-launch-template\">launch template</a>.</p>
            context: <p>Reserved.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.create_fleet_request.CreateFleetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.create_fleet_result.CreateFleetResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.create_fleet

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.create_fleet.async_create_fleet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.create_fleet_request.CreateFleetRequest = {}  # type: ignore[typeddict-item]
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if client_token is not None:
            input_["client_token"] = client_token
        if spot_options is not None:
            input_["spot_options"] = spot_options
        if on_demand_options is not None:
            input_["on_demand_options"] = on_demand_options
        if reserved_capacity_options is not None:
            input_["reserved_capacity_options"] = reserved_capacity_options
        if excess_capacity_termination_policy is not None:
            input_["excess_capacity_termination_policy"] = (
                excess_capacity_termination_policy
            )
        input_["launch_template_configs"] = launch_template_configs
        input_["target_capacity_specification"] = target_capacity_specification
        if terminate_instances_with_expiration is not None:
            input_["terminate_instances_with_expiration"] = (
                terminate_instances_with_expiration
            )
        if type is not None:
            input_["type"] = type
        if valid_from is not None:
            input_["valid_from"] = valid_from
        if valid_until is not None:
            input_["valid_until"] = valid_until
        if replace_unhealthy_instances is not None:
            input_["replace_unhealthy_instances"] = replace_unhealthy_instances
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications
        if context is not None:
            input_["context"] = context

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_flow_logs(
        self,
        resource_ids: "aws_sdk_ec2.types.flow_log_resource_ids.FlowLogResourceIds",
        resource_type: "aws_sdk_ec2.types.flow_logs_resource_type.FlowLogsResourceType",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        client_token: Optional["aws_sdk_ec2.types.string.String"] = None,
        deliver_logs_permission_arn: Optional["aws_sdk_ec2.types.string.String"] = None,
        deliver_cross_account_role: Optional["aws_sdk_ec2.types.string.String"] = None,
        log_group_name: Optional["aws_sdk_ec2.types.string.String"] = None,
        traffic_type: Optional["aws_sdk_ec2.types.traffic_type.TrafficType"] = None,
        log_destination_type: Optional[
            "aws_sdk_ec2.types.log_destination_type.LogDestinationType"
        ] = None,
        log_destination: Optional["aws_sdk_ec2.types.string.String"] = None,
        log_format: Optional["aws_sdk_ec2.types.string.String"] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
        max_aggregation_interval: Optional["aws_sdk_ec2.types.integer.Integer"] = None,
        destination_options: Optional[
            "aws_sdk_ec2.types.destination_options_request.DestinationOptionsRequest"
        ] = None,
    ) -> "aws_sdk_ec2.types.create_flow_logs_result.CreateFlowLogsResult":
        r"""<p>Creates one or more flow logs to capture information about IP traffic for a specific network interface, subnet, or VPC. </p> <p>Flow log data for a monitored network interface is recorded as flow log records, which are log events consisting of fields that describe the traffic flow. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html\">Flow log records</a> in the <i>Amazon VPC User Guide</i>.</p> <p>When publishing to CloudWatch Logs, flow log records are published to a log group, and each network interface has a unique log stream in the log group. When publishing to Amazon S3, flow log records for all of the monitored network interfaces are published to a single log file object that is stored in the specified bucket.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html\">VPC Flow Logs</a> in the <i>Amazon VPC User Guide</i>.</p>

        Args:
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">How to ensure idempotency</a>.</p>
            deliver_logs_permission_arn: <p>The ARN of the IAM role that allows Amazon EC2 to publish flow logs to the log destination.</p> <p>This parameter is required if the destination type is <code>cloud-watch-logs</code>, or if the destination type is <code>kinesis-data-firehose</code> and the delivery stream and the resources to monitor are in different accounts.</p>
            deliver_cross_account_role: <p>The ARN of the IAM role that allows Amazon EC2 to publish flow logs across accounts.</p>
            log_group_name: <p>The name of a new or existing CloudWatch Logs log group where Amazon EC2 publishes your flow logs.</p> <p>This parameter is valid only if the destination type is <code>cloud-watch-logs</code>.</p>
            resource_ids: <p>The IDs of the resources to monitor. For example, if the resource type is <code>VPC</code>, specify the IDs of the VPCs.</p> <p>Constraints: Maximum of 25 for transit gateway resource types. Maximum of 1000 for the other resource types.</p>
            resource_type: <p>The type of resource to monitor.</p>
            traffic_type: <p>The type of traffic to monitor (accepted traffic, rejected traffic, or all traffic). This parameter is not supported for transit gateway resource types. It is required for the other resource types.</p>
            log_destination_type: <p>The type of destination for the flow log data.</p> <p>Default: <code>cloud-watch-logs</code> </p>
            log_destination: <p>The destination for the flow log data. The meaning of this parameter depends on the destination type.</p> <ul> <li> <p>If the destination type is <code>cloud-watch-logs</code>, specify the ARN of a CloudWatch Logs log group. For example:</p> <p>arn:aws:logs:<i>region</i>:<i>account_id</i>:log-group:<i>my_group</i> </p> <p>Alternatively, use the <code>LogGroupName</code> parameter.</p> </li> <li> <p>If the destination type is <code>s3</code>, specify the ARN of an S3 bucket. For example:</p> <p>arn:aws:s3:::<i>my_bucket</i>/<i>my_subfolder</i>/</p> <p>The subfolder is optional. Note that you can't use <code>AWSLogs</code> as a subfolder name.</p> </li> <li> <p>If the destination type is <code>kinesis-data-firehose</code>, specify the ARN of a Kinesis Data Firehose delivery stream. For example:</p> <p>arn:aws:firehose:<i>region</i>:<i>account_id</i>:deliverystream:<i>my_stream</i> </p> </li> </ul>
            log_format: <p>The fields to include in the flow log record. List the fields in the order in which they should appear. If you omit this parameter, the flow log is created using the default format. If you specify this parameter, you must include at least one field. For more information about the available fields, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html\">Flow log records</a> in the <i>Amazon VPC User Guide</i> or <a href=\"https://docs.aws.amazon.com/vpc/latest/tgw/tgw-flow-logs.html#flow-log-records\">Transit Gateway Flow Log records</a> in the <i>Amazon Web Services Transit Gateway Guide</i>.</p> <p>Specify the fields using the <code>${field-id}</code> format, separated by spaces.</p>
            tag_specifications: <p>The tags to apply to the flow logs.</p>
            max_aggregation_interval: <p>The maximum interval of time during which a flow of packets is captured and aggregated into a flow log record. The possible values are 60 seconds (1 minute) or 600 seconds (10 minutes). This parameter must be 60 seconds for transit gateway resource types.</p> <p>When a network interface is attached to a <a href=\"https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html\">Nitro-based instance</a>, the aggregation interval is always 60 seconds or less, regardless of the value that you specify.</p> <p>Default: 600</p>
            destination_options: <p>The destination options.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.create_flow_logs_request.CreateFlowLogsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.create_flow_logs_result.CreateFlowLogsResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.create_flow_logs

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.create_flow_logs.async_create_flow_logs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.create_flow_logs_request.CreateFlowLogsRequest = {}  # type: ignore[typeddict-item]
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if client_token is not None:
            input_["client_token"] = client_token
        if deliver_logs_permission_arn is not None:
            input_["deliver_logs_permission_arn"] = deliver_logs_permission_arn
        if deliver_cross_account_role is not None:
            input_["deliver_cross_account_role"] = deliver_cross_account_role
        if log_group_name is not None:
            input_["log_group_name"] = log_group_name
        input_["resource_ids"] = resource_ids
        input_["resource_type"] = resource_type
        if traffic_type is not None:
            input_["traffic_type"] = traffic_type
        if log_destination_type is not None:
            input_["log_destination_type"] = log_destination_type
        if log_destination is not None:
            input_["log_destination"] = log_destination
        if log_format is not None:
            input_["log_format"] = log_format
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications
        if max_aggregation_interval is not None:
            input_["max_aggregation_interval"] = max_aggregation_interval
        if destination_options is not None:
            input_["destination_options"] = destination_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_fpga_image(
        self,
        input_storage_location: "aws_sdk_ec2.types.storage_location.StorageLocation",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        logs_storage_location: Optional[
            "aws_sdk_ec2.types.storage_location.StorageLocation"
        ] = None,
        description: Optional["aws_sdk_ec2.types.string.String"] = None,
        name: Optional["aws_sdk_ec2.types.string.String"] = None,
        client_token: Optional["aws_sdk_ec2.types.string.String"] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
    ) -> "aws_sdk_ec2.types.create_fpga_image_result.CreateFpgaImageResult":
        r"""<p>Creates an Amazon FPGA Image (AFI) from the specified design checkpoint (DCP).</p> <p>The create operation is asynchronous. To verify that the AFI was successfully created and is ready for use, check the output logs.</p> <p>An AFI contains the FPGA bitstream that is ready to download to an FPGA. You can securely deploy an AFI on multiple FPGA-accelerated instances. For more information, see the <a href=\"https://github.com/aws/aws-fpga/\">Amazon Web Services FPGA Hardware Development Kit</a>.</p>

        Args:
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            input_storage_location: <p>The location of the encrypted design checkpoint in Amazon S3. The input must be a tarball.</p>
            logs_storage_location: <p>The location in Amazon S3 for the output logs.</p>
            description: <p>A description for the AFI.</p>
            name: <p>A name for the AFI.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring Idempotency</a>.</p>
            tag_specifications: <p>The tags to apply to the FPGA image during creation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.create_fpga_image_request.CreateFpgaImageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.create_fpga_image_result.CreateFpgaImageResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.create_fpga_image

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.create_fpga_image.async_create_fpga_image(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.create_fpga_image_request.CreateFpgaImageRequest = {}  # type: ignore[typeddict-item]
        if dry_run is not None:
            input_["dry_run"] = dry_run
        input_["input_storage_location"] = input_storage_location
        if logs_storage_location is not None:
            input_["logs_storage_location"] = logs_storage_location
        if description is not None:
            input_["description"] = description
        if name is not None:
            input_["name"] = name
        if client_token is not None:
            input_["client_token"] = client_token
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_image(
        self,
        instance_id: "aws_sdk_ec2.types.instance_id.InstanceId",
        name: "aws_sdk_ec2.types.image_name_request.ImageNameRequest",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
        snapshot_location: Optional[
            "aws_sdk_ec2.types.snapshot_location_enum.SnapshotLocationEnum"
        ] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        description: Optional[
            "aws_sdk_ec2.types.image_description_request.ImageDescriptionRequest"
        ] = None,
        no_reboot: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        block_device_mappings: Optional[
            "aws_sdk_ec2.types.block_device_mapping_request_list.BlockDeviceMappingRequestList"
        ] = None,
    ) -> "aws_sdk_ec2.types.create_image_result.CreateImageResult":
        r"""<p>Creates an Amazon EBS-backed AMI from an Amazon EBS-backed instance that is either running or stopped.</p> <p>If you customized your instance with instance store volumes or Amazon EBS volumes in addition to the root device volume, the new AMI contains block device mapping information for those volumes. When you launch an instance from this new AMI, the instance automatically launches with those additional volumes.</p> <p>The location of the source instance determines where you can create the snapshots of the AMI:</p> <ul> <li> <p>If the source instance is in a Region, you must create the snapshots in the same Region as the instance.</p> </li> <li> <p>If the source instance is in a Local Zone, you can create the snapshots in the same Local Zone or in its parent Region.</p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html\">Create an Amazon EBS-backed AMI</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p>

        Args:
            tag_specifications: <p>The tags to apply to the AMI and snapshots on creation. You can tag the AMI, the snapshots, or both.</p> <ul> <li> <p>To tag the AMI, the value for <code>ResourceType</code> must be <code>image</code>.</p> </li> <li> <p>To tag the snapshots that are created of the root volume and of other Amazon EBS volumes that are attached to the instance, the value for <code>ResourceType</code> must be <code>snapshot</code>. The same tag is applied to all of the snapshots that are created.</p> </li> </ul> <p>If you specify other values for <code>ResourceType</code>, the request fails.</p> <p>To tag an AMI or snapshot after it has been created, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html\">CreateTags</a>. </p>
            snapshot_location: <note> <p>Only supported for instances in Local Zones. If the source instance is not in a Local Zone, omit this parameter.</p> </note> <p>The Amazon S3 location where the snapshots will be stored.</p> <ul> <li> <p>To create local snapshots in the same Local Zone as the source instance, specify <code>local</code>.</p> </li> <li> <p>To create regional snapshots in the parent Region of the Local Zone, specify <code>regional</code> or omit this parameter.</p> </li> </ul> <p>Default: <code>regional</code> </p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            instance_id: <p>The ID of the instance.</p>
            name: <p>A name for the new image.</p> <p>Constraints: 3-128 alphanumeric characters, parentheses (()), square brackets ([]), spaces ( ), periods (.), slashes (/), dashes (-), single quotes ('), at-signs (@), or underscores(_)</p>
            description: <p>A description for the new image.</p>
            no_reboot: <p>Indicates whether or not the instance should be automatically rebooted before creating the image. Specify one of the following values:</p> <ul> <li> <p> <code>true</code> - The instance is not rebooted before creating the image. This creates crash-consistent snapshots that include only the data that has been written to the volumes at the time the snapshots are created. Buffered data and data in memory that has not yet been written to the volumes is not included in the snapshots.</p> </li> <li> <p> <code>false</code> - The instance is rebooted before creating the image. This ensures that all buffered data and data in memory is written to the volumes before the snapshots are created.</p> </li> </ul> <p>Default: <code>false</code> </p>
            block_device_mappings: <p>The block device mappings.</p> <p>When using the CreateImage action:</p> <ul> <li> <p>You can't change the volume size using the VolumeSize parameter. If you want a different volume size, you must first change the volume size of the source instance.</p> </li> <li> <p>You can't modify the encryption status of existing volumes or snapshots. To create an AMI with volumes or snapshots that have a different encryption status (for example, where the source volume and snapshots are unencrypted, and you want to create an AMI with encrypted volumes or snapshots), copy the image instead.</p> </li> <li> <p>The only option that can be changed for existing mappings or snapshots is <code>DeleteOnTermination</code>.</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.create_image_request.CreateImageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.create_image_result.CreateImageResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.create_image

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.create_image.async_create_image(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.create_image_request.CreateImageRequest = {}  # type: ignore[typeddict-item]
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications
        if snapshot_location is not None:
            input_["snapshot_location"] = snapshot_location
        if dry_run is not None:
            input_["dry_run"] = dry_run
        input_["instance_id"] = instance_id
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if no_reboot is not None:
            input_["no_reboot"] = no_reboot
        if block_device_mappings is not None:
            input_["block_device_mappings"] = block_device_mappings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_image_usage_report(
        self,
        image_id: "aws_sdk_ec2.types.image_id.ImageId",
        resource_types: "aws_sdk_ec2.types.image_usage_resource_type_request_list.ImageUsageResourceTypeRequestList",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        account_ids: Optional[
            "aws_sdk_ec2.types.image_usage_report_user_id_string_list.ImageUsageReportUserIdStringList"
        ] = None,
        client_token: Optional[
            "aws_sdk_ec2.types.create_image_usage_report_client_token.CreateImageUsageReportClientToken"
        ] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
    ) -> "aws_sdk_ec2.types.create_image_usage_report_result.CreateImageUsageReportResult":
        r"""<p>Creates a report that shows how your image is used across other Amazon Web Services accounts. The report provides visibility into which accounts are using the specified image, and how many resources (EC2 instances or launch templates) are referencing it.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/your-ec2-ami-usage.html\">View your AMI usage</a> in the <i>Amazon EC2 User Guide</i>.</p>

        Args:
            image_id: <p>The ID of the image to report on.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            resource_types: <p>The resource types to include in the report.</p>
            account_ids: <p>The Amazon Web Services account IDs to include in the report. To include all accounts, omit this parameter.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure idempotency of the request.</p>
            tag_specifications: <p>The tags to apply to the report on creation. The <code>ResourceType</code> must be set to <code>image-usage-report</code>; any other value will cause the report creation to fail.</p> <p>To tag a report after it has been created, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html\">CreateTags</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.create_image_usage_report_request.CreateImageUsageReportRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.create_image_usage_report_result.CreateImageUsageReportResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.create_image_usage_report

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.create_image_usage_report.async_create_image_usage_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.create_image_usage_report_request.CreateImageUsageReportRequest = {}  # type: ignore[typeddict-item]
        input_["image_id"] = image_id
        if dry_run is not None:
            input_["dry_run"] = dry_run
        input_["resource_types"] = resource_types
        if account_ids is not None:
            input_["account_ids"] = account_ids
        if client_token is not None:
            input_["client_token"] = client_token
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_instance_connect_endpoint(
        self,
        subnet_id: "aws_sdk_ec2.types.subnet_id.SubnetId",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        security_group_ids: Optional[
            "aws_sdk_ec2.types.security_group_id_string_list_request.SecurityGroupIdStringListRequest"
        ] = None,
        preserve_client_ip: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        client_token: Optional["aws_sdk_ec2.types.string.String"] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
        ip_address_type: Optional[
            "aws_sdk_ec2.types.ip_address_type.IpAddressType"
        ] = None,
    ) -> "aws_sdk_ec2.types.create_instance_connect_endpoint_result.CreateInstanceConnectEndpointResult":
        r"""<p>Creates an EC2 Instance Connect Endpoint.</p> <p>An EC2 Instance Connect Endpoint allows you to connect to an instance, without requiring the instance to have a public IPv4 or public IPv6 address. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect-Endpoint.html\">Connect to your instances using EC2 Instance Connect Endpoint</a> in the <i>Amazon EC2 User Guide</i>.</p>

        Args:
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            subnet_id: <p>The ID of the subnet in which to create the EC2 Instance Connect Endpoint.</p>
            security_group_ids: <p>One or more security groups to associate with the endpoint. If you don't specify a security group, the default security group for your VPC will be associated with the endpoint.</p>
            preserve_client_ip: <p>Indicates whether the client IP address is preserved as the source. The following are the possible values.</p> <ul> <li> <p> <code>true</code> - Use the client IP address as the source.</p> </li> <li> <p> <code>false</code> - Use the network interface IP address as the source.</p> </li> </ul> <note> <p> <code>PreserveClientIp</code> is only supported on IPv4 EC2 Instance Connect Endpoints. To use <code>PreserveClientIp</code>, the value for <code>IpAddressType</code> must be <code>ipv4</code>.</p> </note> <p>Default: <code>false</code> </p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            tag_specifications: <p>The tags to apply to the EC2 Instance Connect Endpoint during creation.</p>
            ip_address_type: <p>The IP address type of the endpoint.</p> <p>If no value is specified, the default value is determined by the IP address type of the subnet:</p> <ul> <li> <p> <code>dualstack</code> - If the subnet has both IPv4 and IPv6 CIDRs</p> </li> <li> <p> <code>ipv4</code> - If the subnet has only IPv4 CIDRs</p> </li> <li> <p> <code>ipv6</code> - If the subnet has only IPv6 CIDRs</p> </li> </ul> <note> <p> <code>PreserveClientIp</code> is only supported on IPv4 EC2 Instance Connect Endpoints. To use <code>PreserveClientIp</code>, the value for <code>IpAddressType</code> must be <code>ipv4</code>.</p> </note>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.create_instance_connect_endpoint_request.CreateInstanceConnectEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.create_instance_connect_endpoint_result.CreateInstanceConnectEndpointResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.create_instance_connect_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.create_instance_connect_endpoint.async_create_instance_connect_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.create_instance_connect_endpoint_request.CreateInstanceConnectEndpointRequest = {}  # type: ignore[typeddict-item]
        if dry_run is not None:
            input_["dry_run"] = dry_run
        input_["subnet_id"] = subnet_id
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if preserve_client_ip is not None:
            input_["preserve_client_ip"] = preserve_client_ip
        if client_token is not None:
            input_["client_token"] = client_token
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_instance_event_window(
        self,
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        name: Optional["aws_sdk_ec2.types.string.String"] = None,
        time_ranges: Optional[
            "aws_sdk_ec2.types.instance_event_window_time_range_request_set.InstanceEventWindowTimeRangeRequestSet"
        ] = None,
        cron_expression: Optional[
            "aws_sdk_ec2.types.instance_event_window_cron_expression.InstanceEventWindowCronExpression"
        ] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
    ) -> "aws_sdk_ec2.types.create_instance_event_window_result.CreateInstanceEventWindowResult":
        r"""<p>Creates an event window in which scheduled events for the associated Amazon EC2 instances can run.</p> <p>You can define either a set of time ranges or a cron expression when creating the event window, but not both. All event window times are in UTC.</p> <p>You can create up to 200 event windows per Amazon Web Services Region.</p> <p>When you create the event window, targets (instance IDs, Dedicated Host IDs, or tags) are not yet associated with it. To ensure that the event window can be used, you must associate one or more targets with it by using the <a>AssociateInstanceEventWindow</a> API.</p> <important> <p>Event windows are applicable only for scheduled events that stop, reboot, or terminate instances.</p> <p>Event windows are <i>not</i> applicable for:</p> <ul> <li> <p>Expedited scheduled events and network maintenance events. </p> </li> <li> <p>Unscheduled maintenance such as AutoRecovery and unplanned reboots.</p> </li> </ul> </important> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/event-windows.html\">Define event windows for scheduled events</a> in the <i>Amazon EC2 User Guide</i>.</p>

        Args:
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            name: <p>The name of the event window.</p>
            time_ranges: <p>The time range for the event window. If you specify a time range, you can't specify a cron expression.</p>
            cron_expression: <p>The cron expression for the event window, for example, <code>* 0-4,20-23 * * 1,5</code>. If you specify a cron expression, you can't specify a time range.</p> <p>Constraints:</p> <ul> <li> <p>Only hour and day of the week values are supported.</p> </li> <li> <p>For day of the week values, you can specify either integers <code>0</code> through <code>6</code>, or alternative single values <code>SUN</code> through <code>SAT</code>.</p> </li> <li> <p>The minute, month, and year must be specified by <code>*</code>.</p> </li> <li> <p>The hour value must be one or a multiple range, for example, <code>0-4</code> or <code>0-4,20-23</code>.</p> </li> <li> <p>Each hour range must be >= 2 hours, for example, <code>0-2</code> or <code>20-23</code>.</p> </li> <li> <p>The event window must be >= 4 hours. The combined total time ranges in the event window must be >= 4 hours.</p> </li> </ul> <p>For more information about cron expressions, see <a href=\"https://en.wikipedia.org/wiki/Cron\">cron</a> on the <i>Wikipedia website</i>.</p>
            tag_specifications: <p>The tags to apply to the event window.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.create_instance_event_window_request.CreateInstanceEventWindowRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.create_instance_event_window_result.CreateInstanceEventWindowResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.create_instance_event_window

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.create_instance_event_window.async_create_instance_event_window(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.create_instance_event_window_request.CreateInstanceEventWindowRequest = {}  # type: ignore[typeddict-item]
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if name is not None:
            input_["name"] = name
        if time_ranges is not None:
            input_["time_ranges"] = time_ranges
        if cron_expression is not None:
            input_["cron_expression"] = cron_expression
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_instance_export_task(
        self,
        instance_id: "aws_sdk_ec2.types.instance_id.InstanceId",
        target_environment: "aws_sdk_ec2.types.export_environment.ExportEnvironment",
        export_to_s3_task: "aws_sdk_ec2.types.export_to_s3_task_specification.ExportToS3TaskSpecification",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
        description: Optional["aws_sdk_ec2.types.string.String"] = None,
    ) -> "aws_sdk_ec2.types.create_instance_export_task_result.CreateInstanceExportTaskResult":
        r"""<p>Exports a running or stopped instance to an Amazon S3 bucket.</p> <p>For information about the prerequisites for your Amazon S3 bucket, supported operating systems, image formats, and known limitations for the types of instances you can export, see <a href=\"https://docs.aws.amazon.com/vm-import/latest/userguide/vmexport.html\">Exporting an instance as a VM Using VM Import/Export</a> in the <i>VM Import/Export User Guide</i>.</p>

        Args:
            tag_specifications: <p>The tags to apply to the export instance task during creation.</p>
            description: <p>A description for the conversion task or the resource being exported. The maximum length is 255 characters.</p>
            instance_id: <p>The ID of the instance.</p>
            target_environment: <p>The target virtualization environment.</p>
            export_to_s3_task: <p>The format and location for an export instance task.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.create_instance_export_task_request.CreateInstanceExportTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.create_instance_export_task_result.CreateInstanceExportTaskResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.create_instance_export_task

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.create_instance_export_task.async_create_instance_export_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.create_instance_export_task_request.CreateInstanceExportTaskRequest = {}  # type: ignore[typeddict-item]
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications
        if description is not None:
            input_["description"] = description
        input_["instance_id"] = instance_id
        input_["target_environment"] = target_environment
        input_["export_to_s3_task"] = export_to_s3_task

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_internet_gateway(
        self,
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_ec2.types.create_internet_gateway_result.CreateInternetGatewayResult":
        r"""<p>Creates an internet gateway for use with a VPC. After creating the internet gateway, you attach it to a VPC using <a>AttachInternetGateway</a>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html\">Internet gateways</a> in the <i>Amazon VPC User Guide</i>.</p>

        Args:
            tag_specifications: <p>The tags to assign to the internet gateway.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>

        Examples:
            To create an Internet gateway
            This example creates an Internet gateway.

            >>> await client.create_internet_gateway()
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.create_internet_gateway_request.CreateInternetGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.create_internet_gateway_result.CreateInternetGatewayResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.create_internet_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.create_internet_gateway.async_create_internet_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.create_internet_gateway_request.CreateInternetGatewayRequest = {}  # type: ignore[typeddict-item]
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_interruptible_capacity_reservation_allocation(
        self,
        capacity_reservation_id: "aws_sdk_ec2.types.capacity_reservation_id.CapacityReservationId",
        instance_count: "aws_sdk_ec2.types.integer.Integer",
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        client_token: Optional["aws_sdk_ec2.types.string.String"] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
    ) -> "aws_sdk_ec2.types.create_interruptible_capacity_reservation_allocation_result.CreateInterruptibleCapacityReservationAllocationResult":
        """<p> Creates an interruptible Capacity Reservation by specifying the number of unused instances you want to allocate from your source reservation. This helps you make unused capacity available for other workloads within your account while maintaining control to reclaim it. </p>

        Args:
            capacity_reservation_id: <p> The ID of the source Capacity Reservation from which to create the interruptible Capacity Reservation. Your Capacity Reservation must be in active state with no end date set and have available capacity for allocation. </p>
            instance_count: <p> The number of instances to allocate from your source reservation. You can only allocate available instances (also called unused capacity). </p>
            client_token: <p> Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. </p>
            dry_run: <p> Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. </p>
            tag_specifications: <p> The tags to apply to the interruptible Capacity Reservation during creation. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ec2.types.create_interruptible_capacity_reservation_allocation_request.CreateInterruptibleCapacityReservationAllocationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ec2.types.create_interruptible_capacity_reservation_allocation_result.CreateInterruptibleCapacityReservationAllocationResult"
        ]:
            import aws_sdk_ec2._operations.amazon_ec2.create_interruptible_capacity_reservation_allocation

            (
                output,
                http_response,
            ) = await aws_sdk_ec2._operations.amazon_ec2.create_interruptible_capacity_reservation_allocation.async_create_interruptible_capacity_reservation_allocation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ec2.types.create_interruptible_capacity_reservation_allocation_request.CreateInterruptibleCapacityReservationAllocationRequest = {}  # type: ignore[typeddict-item]
        input_["capacity_reservation_id"] = capacity_reservation_id
        input_["instance_count"] = instance_count
        if client_token is not None:
            input_["client_token"] = client_token
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if tag_specifications is not None:
            input_["tag_specifications"] = tag_specifications

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_ipam(
        self,
        *,
        config_overrides: Optional[AsyncEC2ClientConfig] = None,
        dry_run: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        description: Optional["aws_sdk_ec2.types.string.String"] = None,
        operating_regions: Optional[
            "aws_sdk_ec2.types.add_ipam_operating_region_set.AddIpamOperatingRegionSet"
        ] = None,
        tag_specifications: Optional[
            "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
        ] = None,
        client_token: Optional["aws_sdk_ec2.types.string.String"] = None,
        tier: Optional["aws_sdk_ec2.types.ipam_tier.IpamTier"] = None,
        enable_private_gua: Optional["aws_sdk_ec2.types.boolean.Boolean"] = None,
        metered_account: Optional[
            "aws_sdk_ec2.types.ipam_metered_account.IpamMeteredAccount"
        ] = None,
    ) -> "aws_sdk_ec2.types.create_ipam_result.CreateIpamResult":
        r"""<p>Create an IPAM. Amazon VPC IP Address Manager (IPAM) is a VPC feature that you can 